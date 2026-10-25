"""CLI: `run` queries a model and stores one JSON line per query; `evaluate` scores stored runs
side by side on the queries they all answered.

    jevconflict run --method flat --split test
    jevconflict run --method tree --split test
    jevconflict run --method paper_llm --split test        # Google's prompt on Gemini 2.5 Flash
    jevconflict evaluate --split test

Runs resume: queries already in the output file are skipped. Paid calls are cached in
runs/api_cache.sqlite, shared by every model, method and split.
"""

from __future__ import annotations

import argparse
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
from tqdm import tqdm

from .client import ROOT, Cache, Chat, Gateway
from .data import DATA, LABELS, MERGED, load, split_ids
from .perturb import PERTURBATIONS, WRONG_ANSWER_PROMPT, apply, plant_candidates
from .methods import METHODS, combine_tree_v2, tree_hard
from .metrics import (accuracy, bootstrap_ci, brier, confusion, ece, macro_f1, mcnemar_exact, nll,
                      paired_bootstrap, per_class_f1)

RUNS = ROOT / "runs"
PLANTS = DATA / "plants.json"
PLANT_MODEL = "openai/gpt-4.1-mini"
PAPER = {"Gemini 2.5 Flash, as published (paper Table 4)": 0.653}
DEFAULT_SYSTEMS = ["typesafe-ai/jev-1.13.0:flat", "typesafe-ai/jev-1.13.0:tree", "google/gemini-2.5-flash:paper_llm",
                   "google/gemini-2.5-flash:paper_llm_thinking", "google/gemini-3.8-flash:paper_llm_low",
                   "google/gemini-3.8-flash:paper_llm_thinking"]


def out_path(model: str, split: str, method: str, perturb: str | None = None) -> Path:
    name = f"{method}@{perturb}" if perturb else method
    return RUNS / model.replace("/", "__") / split / f"{name}.jsonl"


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []


def cmd_run(args) -> None:
    fn, kind, default_model, extra = METHODS[args.method]
    model = args.model or default_model
    rows = {r["id"]: r for r in load()}
    ids = split_ids(list(rows.values()), args.split)
    if args.perturb:
        plants = json.loads(PLANTS.read_text()) if args.perturb == "plant" else None
        rows = {i: p for i in ids if (p := apply(args.perturb, rows[i], plants)) is not None}
        ids = [i for i in ids if i in rows]
    ids = ids[: args.limit]
    path = out_path(model, args.split, args.method, args.perturb)
    path.parent.mkdir(parents=True, exist_ok=True)
    done = {r["id"] for r in read_jsonl(path)}
    todo = [i for i in ids if i not in done]
    print(f"{model} {args.method}{'@' + args.perturb if args.perturb else ''} on {args.split}: "
          f"{len(todo)} to run, {len(done)} already done -> {path}")
    cache = Cache(RUNS / "api_cache.sqlite")
    salt = "rerun-1" if args.perturb == "rerun" else ""
    if kind == "decision":
        client = Gateway(model, cache, salt=salt)
    else:
        client = Chat(model, cache, extra=extra, salt=salt)
    with open(path, "a") as f, ThreadPoolExecutor(args.concurrency) as pool:
        for rec in tqdm(pool.map(lambda i: fn(client, rows[i]), todo), total=len(todo)):
            f.write(json.dumps(rec) + "\n")
            f.flush()
    client.close()


def _derived(recs: list[dict]) -> dict[str, list[dict]]:
    """Variants computed from the tree's stored yes-probabilities, with no extra calls."""
    hard = [r | {"method": "tree_hard", "pred": tree_hard(r["raw"]), "hard": True,
                 "probs": {k: float(k == tree_hard(r["raw"])) for k in LABELS}} for r in recs]
    v2 = []
    for r in recs:
        probs = combine_tree_v2(r["raw"])
        v2.append(r | {"method": "tree_v2", "probs": probs, "pred": max(LABELS, key=probs.get)})
    return {"tree_hard": hard, "tree_v2": v2}


def _input_tokens(rec: dict) -> int:
    # The gateway says inputTokens or prompt_tokens; TypeSafe's native API says input_tokens.
    u = rec.get("usage") or {}
    return u.get("inputTokens") or u.get("prompt_tokens") or u.get("input_tokens") or 0


def summarise(recs: list[dict], price_per_m: float) -> dict:
    y = [r["label"] for r in recs]
    pred = [r["pred"] for r in recs]
    correct = np.array([a == b for a, b in zip(y, pred)])
    P = np.array([[r["probs"][k] for k in LABELS] for r in recs])
    y_idx = np.array([LABELS.index(c) for c in y])
    hard = any(r.get("hard") for r in recs)
    usd = [r["cost_usd"] if r["cost_usd"] is not None else _input_tokens(r) * price_per_m / 1e6 for r in recs]
    lat = np.array([r["latency_s"] for r in recs if r.get("latency_s") is not None])
    lo, hi = bootstrap_ci(correct.astype(float))
    nan = float("nan")
    return {
        "n": len(recs), "acc": accuracy(y, pred), "acc_lo": lo, "acc_hi": hi,
        "acc_merged": accuracy([MERGED.get(c, c) for c in y], [MERGED.get(c, c) for c in pred]),
        "macro_f1": macro_f1(y, pred, LABELS), "f1": per_class_f1(y, pred, LABELS),
        "ece": nan if hard else ece(P.max(axis=1), correct),
        "brier": nan if hard else brier(P, y_idx), "nll": nan if hard else nll(P, y_idx),
        "unparsed": sum(p not in LABELS for p in pred),
        "usd_per_1k": 1000 * float(np.mean(usd)), "tokens_in": float(np.mean([_input_tokens(r) for r in recs])),
        "lat_mean": float(lat.mean()) if len(lat) else nan,
        "lat_p95": float(np.percentile(lat, 95)) if len(lat) else nan,
        "confusion": confusion(y, pred, LABELS), "correct": correct,
    }


def _fmt(x: float, nd: int = 3) -> str:
    return "–" if x != x else f"{x:.{nd}f}"


def cmd_evaluate(args) -> None:
    runs: dict[str, list[dict]] = {}
    for spec in args.systems:
        model, method = spec.rsplit(":", 1)
        # `all` is the union of the dev and test runs (the same calls, nothing re-run).
        splits = ["dev", "test"] if args.split == "all" else [args.split]
        recs = sorted((r for sp in splits for r in read_jsonl(out_path(model, sp, method))), key=lambda r: r["id"])
        if not recs:
            print(f"skipping {spec}: no runs on {args.split}")
            continue
        short = model.split("/")[-1]
        runs[f"{short} {method}"] = recs
        if method == "tree":
            runs |= {f"{short} {m}": r for m, r in _derived(recs).items()}
    if not runs:
        raise SystemExit("nothing to evaluate")
    # Every system is scored on the same queries: those all of them answered.
    common = set.intersection(*({r["id"] for r in recs} for recs in runs.values()))
    runs = {m: [r for r in recs if r["id"] in common] for m, recs in runs.items()}
    s = {m: summarise(recs, args.price_per_m) for m, recs in runs.items()}

    lines = [f"# Conflict-type classification on CONFLICTS, split `{args.split}` (n = {len(common)})", "",
             "| System | Accuracy [95% CI] | 4-class acc. | Macro-F1 | ECE | Brier | NLL | Unparsed | Input tokens | $/1k queries | Latency mean / p95 (s) |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for m, x in s.items():
        lines.append(f"| {m} | {x['acc']:.3f} [{x['acc_lo']:.3f}, {x['acc_hi']:.3f}] | {x['acc_merged']:.3f} | "
                     f"{x['macro_f1']:.3f} | {_fmt(x['ece'])} | {_fmt(x['brier'])} | {_fmt(x['nll'])} | {x['unparsed']} | "
                     f"{x['tokens_in']:.0f} | {x['usd_per_1k']:.3f} | {_fmt(x['lat_mean'], 2)} / {_fmt(x['lat_p95'], 2)} |")
    for name, acc in PAPER.items():
        lines.append(f"| {name} | {acc:.3f} | – | – | – | – | – | – | – | – | – |")
    lines += ["", "4-class accuracy merges Outdated and Misinformation, as the paper does for behaviour.",
              "Hard-label systems (paper_llm, tree_hard) have no probabilities, so calibration is not defined.",
              "Unparsed answers count as wrong. tree_hard and tree_v2 reuse the tree's calls (same cost and latency).",
              "", "## Per-class F1", "", "| System | " + " | ".join(LABELS) + " |", "|---|" + "---|" * len(LABELS)]
    for m, x in s.items():
        lines.append(f"| {m} | " + " | ".join(f"{x['f1'][c]:.3f}" for c in LABELS) + " |")
    lines += ["", "## Paired comparisons (same queries)", "",
              "| A vs B | Acc. A − B [95% CI] | McNemar p |", "|---|---|---|"]
    ms = list(s)
    for i, a in enumerate(ms):
        for b in ms[i + 1:]:
            pb = paired_bootstrap(s[a]["correct"], s[b]["correct"])
            p = mcnemar_exact(s[a]["correct"], s[b]["correct"])
            lines.append(f"| {a} vs {b} | {pb['diff']:+.3f} [{pb['lo']:+.3f}, {pb['hi']:+.3f}] | {p:.3g} |")
    lines += ["", "## Confusion matrices (rows = gold, columns = predicted)", ""]
    short = ["NC", "Comp", "Opin", "Outd", "Misi"]
    for m, x in s.items():
        lines += [f"**{m}**", "", "| gold \\ pred | " + " | ".join(short) + " |", "|---|" + "---|" * len(short)]
        lines += [f"| {short[i]} | " + " | ".join(str(v) for v in row) + " |" for i, row in enumerate(x["confusion"])]
        lines.append("")
    text = "\n".join(lines)
    (RUNS / f"comparison_{args.split}.md").write_text(text)
    print(text)


def _load_system(spec: str, split: str) -> list[dict]:
    """Records of `model:method` on a split (`all` = dev + test), sorted by query id. `tree_v2`
    is derived from the stored `tree` run."""
    model, method = spec.rsplit(":", 1)
    base = "tree" if method == "tree_v2" else method
    splits = ["dev", "test"] if split == "all" else [split]
    recs = sorted((r for sp in splits for r in read_jsonl(out_path(model, sp, base))), key=lambda r: r["id"])
    return _derived(recs)["tree_v2"] if method == "tree_v2" else recs


def cmd_cascade(args) -> None:
    from .cascade import HEADLINE, curve, summary_stats

    expensive = _load_system(args.expensive, args.split)
    lines = [f"# Cascade: Jev → {args.expensive.split('/')[-1]} on CONFLICTS, split `{args.split}`", "",
             "Escalate the fraction f of queries with the lowest Jev top probability; escalated queries take the "
             "LLM's answer. Thresholds are label-free quantiles. Protocol fixed in NOTES.md before computing.", ""]
    for cheap_spec in args.cheap:
        cheap = _load_system(cheap_spec, args.split)
        ids = {r["id"] for r in cheap} & {r["id"] for r in expensive}
        c = [r for r in cheap if r["id"] in ids]
        e = [r for r in expensive if r["id"] in ids]
        st, rows = summary_stats(c, e), curve(c, e)
        name = cheap_spec.split("/")[-1].replace(":", " ")
        lines += [f"## Cheap stage: {name} (n = {len(ids)})", "",
                  f"Cheap stage alone {st['acc_cheap']:.3f}; LLM alone {st['acc_expensive']:.3f} at ${st['usd_expensive']:.2f}/1k "
                  f"and {st['lat_expensive']:.2f} s. AUROC of its confidence for it being correct: {st['auroc']:.3f}. "
                  f"Queries where it is wrong and the LLM right: {st['jev_wrong_llm_right']}; the reverse: "
                  f"{st['jev_right_llm_wrong']}.", "",
                  "| f escalated | Accuracy | Random escalation | Cascade − LLM alone [95% CI] | McNemar p | $/1k queries | Cost vs LLM | Latency mean / p95 (s) |",
                  "|---|---|---|---|---|---|---|---|"]
        for r in rows:
            mark = " **(headline)**" if r["f"] in HEADLINE else ""
            v = r["vs_expensive"]
            lines.append(f"| {r['f']:.0%}{mark} | {r['acc']:.3f} | {r['acc_random']:.3f} | "
                         f"{v['diff']:+.3f} [{v['lo']:+.3f}, {v['hi']:+.3f}] | {r['p_vs_expensive']:.3g} | "
                         f"{r['usd_per_1k']:.2f} | {r['usd_per_1k'] / st['usd_expensive']:.0%} | "
                         f"{r['lat_mean']:.2f} / {r['lat_p95']:.2f} |")
        lines.append("")
    text = "\n".join(lines)
    (RUNS / f"cascade_{args.split}.md").write_text(text)
    print(text)


def cmd_make_plants(args) -> None:
    """Writes data/plants.json: a plausible wrong answer for every eligible No-conflict query."""
    rows = load()
    ids = [i for i in split_ids(rows, args.split)
           if rows[i]["label"] == "no_conflict" and plant_candidates(rows[i], rows[i]["answer"])]
    chat = Chat(PLANT_MODEL, Cache(RUNS / "api_cache.sqlite"))
    plants = json.loads(PLANTS.read_text()) if PLANTS.exists() else {}
    for i in tqdm(ids):
        r = rows[i]
        data = chat.complete(WRONG_ANSWER_PROMPT.format(question=r["question"], answer=r["answer"]))
        wrong = Chat.text(data).strip().strip('"').rstrip(".")
        plants[str(i)] = {"answer": r["answer"], "wrong": wrong, "model": PLANT_MODEL}
    chat.close()
    PLANTS.write_text(json.dumps(plants, indent=1))
    print(f"{len(ids)} plants -> {PLANTS}")


def cmd_diagnose(args) -> None:
    from .metrics import mcnemar_exact, paired_bootstrap

    lines = [f"# Diagnostics on CONFLICTS, split `{args.split}`", "",
             "Each perturbed run is compared with the same system's original run on the same queries. "
             "Flip rate = share of queries whose predicted type changed. TV = mean total-variation distance "
             "between probability vectors (probabilistic systems only). Protocol in NOTES.md.", ""]
    for spec in args.systems:
        model, method = spec.rsplit(":", 1)
        base = "tree" if method in ("tree_v2",) else method
        orig = {r["id"]: r for r in read_jsonl(out_path(model, args.split, base))}
        if method == "tree_v2":
            orig = {r["id"]: r for r in _derived(list(orig.values()))["tree_v2"]}
        if not orig:
            continue
        lines += [f"## {model.split('/')[-1]} {method}", "",
                  "| Perturbation | n | Acc. original → perturbed | Δ [95% CI] | McNemar p | Flip rate | TV | Outdated recall orig → pert | Outdated F1 orig → pert |",
                  "|---|---|---|---|---|---|---|---|---|"]
        for pert in [p for p in PERTURBATIONS if p != "plant"]:
            pr = read_jsonl(out_path(model, args.split, base, pert))
            if method == "tree_v2":
                pr = _derived(pr)["tree_v2"]
            pr = {r["id"]: r for r in pr}
            ids = sorted(set(pr) & set(orig))
            if not ids:
                continue
            o = [orig[i] for i in ids]
            p = [pr[i] for i in ids]
            ok_o = np.array([r["pred"] == r["label"] for r in o])
            ok_p = np.array([r["pred"] == r["label"] for r in p])
            pb = paired_bootstrap(ok_p, ok_o)
            flips = np.mean([a["pred"] != b["pred"] for a, b in zip(o, p)])
            hard = any(r.get("hard") for r in o)
            tv = "–" if hard else f"{np.mean([0.5 * sum(abs(a['probs'][k] - b['probs'][k]) for k in LABELS) for a, b in zip(o, p)]):.3f}"
            out_ids = [k for k, i in enumerate(ids) if o[k]["label"] == "outdated"]
            rec_o = np.mean([o[k]["pred"] == "outdated" for k in out_ids]) if out_ids else float("nan")
            rec_p = np.mean([p[k]["pred"] == "outdated" for k in out_ids]) if out_ids else float("nan")
            f1_o = per_class_f1([r["label"] for r in o], [r["pred"] for r in o], LABELS)["outdated"]
            f1_p = per_class_f1([r["label"] for r in p], [r["pred"] for r in p], LABELS)["outdated"]
            lines.append(f"| {pert} | {len(ids)} | {ok_o.mean():.3f} → {ok_p.mean():.3f} | {pb['diff']:+.3f} "
                         f"[{pb['lo']:+.3f}, {pb['hi']:+.3f}] | {mcnemar_exact(ok_p, ok_o):.3g} | {flips:.3f} | {tv} | "
                         f"{rec_o:.3f} → {rec_p:.3f} | {f1_o:.3f} → {f1_p:.3f} |")
        pl = {r["id"]: r for r in read_jsonl(out_path(model, args.split, base, "plant"))}
        if method == "tree_v2":
            pl = {r["id"]: r for r in _derived(list(pl.values()))["tree_v2"]}
        ids = sorted(set(pl) & set(orig))
        if ids:
            o = [orig[i] for i in ids]
            p = [pl[i] for i in ids]
            share = lambda rs, f: float(np.mean([f(r["pred"]) for r in rs]))
            lines += ["", f"Planted false source (n = {len(ids)} No-conflict queries; expected label Misinformation):", "",
                      "| | Original | Planted |", "|---|---|---|",
                      f"| Predicted Misinformation | {share(o, lambda x: x == 'misinformation'):.3f} | {share(p, lambda x: x == 'misinformation'):.3f} |",
                      f"| Predicted any conflict (not No conflict) | {share(o, lambda x: x != 'no_conflict'):.3f} | {share(p, lambda x: x != 'no_conflict'):.3f} |",
                      f"| Predicted Outdated | {share(o, lambda x: x == 'outdated'):.3f} | {share(p, lambda x: x == 'outdated'):.3f} |"]
            if not any(r.get("hard") for r in o):
                pm = lambda rs: float(np.mean([r["probs"]["misinformation"] for r in rs]))
                pnc = lambda rs: float(np.mean([r["probs"]["no_conflict"] for r in rs]))
                lines += [f"| Mean P(Misinformation) | {pm(o):.3f} | {pm(p):.3f} |",
                          f"| Mean P(No conflict) | {pnc(o):.3f} | {pnc(p):.3f} |"]
        lines.append("")
    text = "\n".join(lines)
    (RUNS / f"diagnostics_{args.split}.md").write_text(text)
    print(text)


def main() -> None:
    ap = argparse.ArgumentParser(prog="jevconflict")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--method", choices=list(METHODS), required=True)
    r.add_argument("--model", default=None, help="default: the method's model in methods.METHODS")
    r.add_argument("--split", choices=["dev", "test", "all"], required=True)
    r.add_argument("--limit", type=int, default=None)
    r.add_argument("--concurrency", type=int, default=8)
    r.add_argument("--perturb", choices=PERTURBATIONS, default=None)
    e = sub.add_parser("evaluate")
    e.add_argument("--split", choices=["dev", "test", "all"], required=True)
    e.add_argument("--systems", nargs="+", default=DEFAULT_SYSTEMS, help="model:method pairs")
    e.add_argument("--price-per-m", type=float, default=0.042, help="list price, used only if no billed cost")
    c = sub.add_parser("cascade")
    c.add_argument("--split", choices=["dev", "test", "all"], required=True)
    c.add_argument("--cheap", nargs="+", default=["typesafe-ai/jev-1.13.0:flat", "typesafe-ai/jev-1.13.0:tree_v2"])
    c.add_argument("--expensive", default="google/gemini-3.8-flash:paper_llm_low")
    mp = sub.add_parser("make-plants")
    mp.add_argument("--split", choices=["dev", "test", "all"], default="test")
    d = sub.add_parser("diagnose")
    d.add_argument("--split", choices=["dev", "test", "all"], default="test")
    d.add_argument("--systems", nargs="+", default=["typesafe-ai/jev-1.13.0:flat", "typesafe-ai/jev-1.13.0:tree",
                                                    "typesafe-ai/jev-1.13.0:tree_v2",
                                                    "google/gemini-3.8-flash:paper_llm_low"])
    args = ap.parse_args()
    {"run": cmd_run, "evaluate": cmd_evaluate, "cascade": cmd_cascade,
     "make-plants": cmd_make_plants, "diagnose": cmd_diagnose}[args.cmd](args)


if __name__ == "__main__":
    main()
