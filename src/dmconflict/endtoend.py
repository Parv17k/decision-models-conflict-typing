"""CLI commands of the end-to-end experiment (protocol in NOTES.md).

    dmconflict generate --split test        # one answer per (query, type) and per query for Vanilla
    dmconflict judge --split test           # expected-behaviour and answer-recall verdicts
    dmconflict endtoend --split test        # every predictor's Pipeline score -> runs/endtoend_test.md
    dmconflict human-sample --split test    # blind sheet for the judge validation
    dmconflict agreement human_eval/behaviour_sample.csv
"""

from __future__ import annotations

import csv
import random
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
from tqdm import tqdm

from .cascade import escalate_mask
from .client import ROOT, Cache, Chat
from .data import LABELS, load, split_ids
from .generate import (
    CONDITIONS,
    GENERATOR,
    JUDGE,
    THINKING_OFF,
    TYPE_DESCRIPTIONS,
    VANILLA,
    generate,
    has_gold_answer,
    judge,
    to_json,
)
from .metrics import mcnemar_exact, paired_bootstrap
from .run import DECISION_MODELS, RUNS, _load_system, out_path, read_jsonl

HUMAN = ROOT / "human_eval"
CHEAP_LLM = "google/gemini-3.8-flash:paper_llm_low"


def _rows(split: str) -> dict[int, dict]:
    rows = {r["id"]: r for r in load()}
    return {i: rows[i] for i in split_ids(list(rows.values()), split)}


def _append(path: Path, todo: list, fn, workers: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a") as f, ThreadPoolExecutor(workers) as pool:
        for rec in tqdm(pool.map(fn, todo), total=len(todo)):
            f.write(to_json(rec) + "\n")
            f.flush()


def answers_path(split: str) -> Path:
    return out_path(GENERATOR, split, "answers")


def judge_path(split: str, kind: str, judge_model: str = JUDGE) -> Path:
    return out_path(judge_model, split, f"judge_{kind}")


def cmd_generate(args) -> None:
    rows = _rows(args.split)
    path = answers_path(args.split)
    done = {(r["id"], r["cond"]) for r in read_jsonl(path)}
    todo = [(i, c) for i in rows for c in CONDITIONS if (i, c) not in done][: args.limit]
    print(f"{GENERATOR} answers on {args.split}: {len(todo)} to run, {len(done)} done -> {path}")
    chat = Chat(GENERATOR, Cache(RUNS / "api_cache.sqlite"), extra=THINKING_OFF)
    _append(path, todo, lambda t: generate(chat, rows[t[0]], t[1]), args.concurrency)
    chat.close()


def cmd_judge(args) -> None:
    rows = _rows(args.split)
    answers = read_jsonl(answers_path(args.split))
    extra = THINKING_OFF if args.judge == JUDGE else {"providerOptions": {"google": {"thinkingConfig": {"thinkingLevel": "low"}}}}
    chat = Chat(args.judge, Cache(RUNS / "api_cache.sqlite"), extra=extra)
    for kind in ("behaviour", "recall"):
        path = judge_path(args.split, kind, args.judge)
        done = {(r["id"], r["cond"]) for r in read_jsonl(path)}
        todo = [a for a in answers if (a["id"], a["cond"]) not in done
                and (kind == "behaviour" or has_gold_answer(rows[a["id"]]))]
        print(f"{args.judge} {kind} on {args.split}: {len(todo)} to run, {len(done)} done -> {path}")
        _append(path, todo, lambda a, kind=kind: judge(chat, rows[a["id"]], a, kind), args.concurrency)
    chat.close()


# --- Scoring ---------------------------------------------------------------------------------

def _type_of(rec: dict) -> str:
    return rec["pred"] if rec["pred"] in LABELS else VANILLA   # unparsed LLM answers: no type


def predictors(split: str) -> dict[str, dict[int, str]]:
    """Condition name -> the type each query's answer is conditioned on."""
    rows = _rows(split)
    out = {"Vanilla": {i: VANILLA for i in rows}, "Oracle (gold type)": {i: r["label"] for i, r in rows.items()}}
    for name, spec in [("Gemini 2.5 Flash (thinking off)", "google/gemini-2.5-flash:paper_llm"),
                       ("Gemini 3.8 Flash (thinking low)", CHEAP_LLM)]:
        out[name] = {r["id"]: _type_of(r) for r in _load_system(spec, split)}
    expensive = {r["id"]: r for r in _load_system(CHEAP_LLM, split)}
    for model in DECISION_MODELS:
        cheap = _load_system(f"{model}:flat", split)
        name = model.split("/")[-1]
        out[name] = {r["id"]: r["pred"] for r in cheap}
        conf = np.array([max(r["probs"].values()) for r in cheap])
        for f in (0.25, 0.50):
            esc = escalate_mask(conf, f)
            out[f"{name} → Gemini 3.8 ({int(f * 100)}%)"] = {
                r["id"]: (_type_of(expensive[r["id"]]) if e else r["pred"]) for r, e in zip(cheap, esc)}
    return out


def scores(split: str, judge_model: str = JUDGE) -> dict:
    rows = _rows(split)
    beh = {(r["id"], r["cond"]): r["verdict"] for r in read_jsonl(judge_path(split, "behaviour", judge_model))}
    rec = {(r["id"], r["cond"]): r["verdict"] for r in read_jsonl(judge_path(split, "recall", judge_model))}
    ids = sorted(rows)
    recall_ids = [i for i in ids if has_gold_answer(rows[i])]
    out = {}
    for name, typ in predictors(split).items():
        b = np.array([bool(beh.get((i, typ[i]))) for i in ids])
        r = np.array([bool(rec.get((i, typ[i]))) for i in recall_ids])
        missing = sum(beh.get((i, typ[i])) is None for i in ids)
        acc = float(np.mean([typ[i] == rows[i]["label"] for i in ids]))
        per = {k: float(np.mean([b[n] for n, i in enumerate(ids) if rows[i]["label"] == k])) for k in LABELS}
        out[name] = {"behaviour": b, "recall": r, "missing": missing, "type_acc": acc, "per_type": per, "types": typ}
    return out


def cmd_endtoend(args) -> None:
    sc = scores(args.split, args.judge)
    van, ora = sc["Vanilla"]["behaviour"], sc["Oracle (gold type)"]["behaviour"]
    ref = sc["Gemini 2.5 Flash (thinking off)"]["behaviour"]
    lines = [f"# End-to-end: expected-behaviour adherence on CONFLICTS, split `{args.split}` (n = {len(van)})", "",
             f"Generator {GENERATOR} (thinking off); judge {args.judge}. Protocol in NOTES.md. "
             "Share of Oracle gain = (condition − Vanilla) / (Oracle − Vanilla).", "",
             "| Condition | Type acc. | Behaviour | Δ Vanilla [95% CI] (p) | Δ Gemini 2.5 Pipeline (p) | Share of Oracle gain | Answer recall | Unjudged |",
             "|---|---|---|---|---|---|---|---|"]
    for name, s in sc.items():
        b = s["behaviour"]
        dv, dr = paired_bootstrap(b, van), paired_bootstrap(b, ref)
        share = (b.mean() - van.mean()) / (ora.mean() - van.mean()) if ora.mean() > van.mean() else float("nan")
        lines.append(f"| {name} | {s['type_acc']:.3f} | {b.mean():.3f} | {dv['diff']:+.3f} [{dv['lo']:+.3f}, {dv['hi']:+.3f}] "
                     f"({mcnemar_exact(b, van):.3g}) | {dr['diff']:+.3f} ({mcnemar_exact(b, ref):.3g}) | {share:.2f} | "
                     f"{s['recall'].mean():.3f} | {s['missing']} |")
    lines += ["", "## Behaviour by gold type", "", "| Condition | " + " | ".join(LABELS) + " |",
              "|---|" + "---|" * len(LABELS)]
    for name, s in sc.items():
        lines.append(f"| {name} | " + " | ".join(f"{s['per_type'][k]:.3f}" for k in LABELS) + " |")
    text = "\n".join(lines)
    suffix = "" if args.judge == JUDGE else "_judge_" + args.judge.split("/")[-1]
    (RUNS / f"endtoend_{args.split}{suffix}.md").write_text(text)
    print(text)


# --- Judge validation ------------------------------------------------------------------------

def cmd_human_sample(args) -> None:
    rows = _rows(args.split)
    answers = read_jsonl(answers_path(args.split))
    beh = {(r["id"], r["cond"]): r for r in read_jsonl(judge_path(args.split, "behaviour"))}
    rng = random.Random(args.seed)
    per_type = args.n // len(LABELS)
    picked = []
    for k in LABELS:
        van = [a for a in answers if a["label"] == k and a["cond"] == VANILLA]
        typed = [a for a in answers if a["label"] == k and a["cond"] != VANILLA]
        rng.shuffle(van), rng.shuffle(typed)
        nv = min(per_type // 2, len(van))
        picked += van[:nv] + typed[: per_type - nv]
    rng.shuffle(picked)
    HUMAN.mkdir(exist_ok=True)
    sheet, key = HUMAN / "behaviour_sample.csv", RUNS / f"human_eval_key_{args.split}.csv"
    with open(sheet, "w", newline="") as f, open(key, "w", newline="") as g:
        w, k = csv.writer(f), csv.writer(g)
        w.writerow(["item", "query", "conflict_type_and_expected_behaviour", "response", "follows (1/0)", "notes"])
        k.writerow(["item", "id", "cond", "judge_verdict"])
        for n, a in enumerate(picked, 1):
            r = rows[a["id"]]
            w.writerow([n, r["question"], TYPE_DESCRIPTIONS[r["label"]], a["text"], "", ""])
            k.writerow([n, a["id"], a["cond"], (beh.get((a["id"], a["cond"])) or {}).get("verdict")])
    print(f"wrote {sheet} ({len(picked)} items, blind) and the key {key}")


def _kappa(a: np.ndarray, b: np.ndarray) -> float:
    po = float(np.mean(a == b))
    pe = float(np.mean(a) * np.mean(b) + (1 - np.mean(a)) * (1 - np.mean(b)))
    return (po - pe) / (1 - pe) if pe < 1 else float("nan")


def cmd_agreement(args) -> None:
    key = {int(r["item"]): r for r in csv.DictReader(open(RUNS / f"human_eval_key_{args.split}.csv"))}
    labels = {}
    for path in args.sheets:
        for r in csv.DictReader(open(path, encoding="utf-8-sig")):
            v = r["follows (1/0)"].strip()
            if v in ("0", "1"):
                labels.setdefault(int(r["item"]), []).append(int(v))
    verdicts = {(r["id"], r["cond"]): r["verdict"] for r in read_jsonl(judge_path(args.split, "behaviour", args.judge))}
    verdict = {i: verdicts.get((int(key[i]["id"]), key[i]["cond"])) for i in key}
    items = sorted(i for i in labels if verdict[i] is not None)
    judge_v = np.array([verdict[i] for i in items]).astype(int)

    def report(name: str, human: np.ndarray, sel: np.ndarray | None = None) -> None:
        h, j = (human, judge_v) if sel is None else (human[sel], judge_v[sel])
        print(f"  {name:<42} n={len(h):>3}  accuracy {np.mean(h == j):.3f}  kappa {_kappa(h, j):.3f}  "
              f"follows: human {h.mean():.2f}, judge {j.mean():.2f}")

    print(f"{args.judge} on {len(items)} labelled items")
    report("vs majority (ties count as follows)", np.array([round(np.mean(labels[i]) + 1e-9) for i in items]))
    if len(args.sheets) > 1:
        both = [n for n, i in enumerate(items) if len(labels[i]) >= 2]
        a = np.array([labels[items[n]][0] for n in both])
        b = np.array([labels[items[n]][1] for n in both])
        if len(both) == len(items):
            report("vs annotator 1", a)
            report("vs annotator 2", b)
            agreed = a == b
            report("vs both, where they agree", a, agreed)
            gold = np.array([_rows(args.split)[int(key[i]["id"])]["label"] for i in items])
            for t in LABELS:
                report(f"  gold {t}, where they agree", a, agreed & (gold == t))
        print(f"Annotator 1 vs 2 on {len(both)} items: agreement {np.mean(a == b):.3f}, kappa {_kappa(a, b):.3f}")


def add_commands(sub) -> dict:
    g = sub.add_parser("generate")
    g.add_argument("--split", choices=["dev", "test"], required=True)
    g.add_argument("--limit", type=int, default=None)
    g.add_argument("--concurrency", type=int, default=8)
    j = sub.add_parser("judge")
    j.add_argument("--split", choices=["dev", "test"], required=True)
    j.add_argument("--judge", default=JUDGE)
    j.add_argument("--concurrency", type=int, default=8)
    e = sub.add_parser("endtoend")
    e.add_argument("--split", choices=["dev", "test"], required=True)
    e.add_argument("--judge", default=JUDGE)
    h = sub.add_parser("human-sample")
    h.add_argument("--split", choices=["dev", "test"], default="test")
    h.add_argument("--n", type=int, default=100)
    h.add_argument("--seed", type=int, default=13)
    a = sub.add_parser("agreement")
    a.add_argument("sheets", nargs="+", help="labelled copies of human_eval/behaviour_sample.csv, one per annotator")
    a.add_argument("--split", choices=["dev", "test"], default="test")
    a.add_argument("--judge", default=JUDGE)
    return {"generate": cmd_generate, "judge": cmd_judge, "endtoend": cmd_endtoend,
            "human-sample": cmd_human_sample, "agreement": cmd_agreement}
