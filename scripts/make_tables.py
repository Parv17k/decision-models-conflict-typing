"""Builds every table and in-text number of the paper from the stored runs (no API calls).

Writes paper/generated/*.tex. The paper never types a result by hand: tables are \\input and
numbers are macros from numbers.tex, so a rerun of this script updates the whole paper.

    .venv/bin/python scripts/make_tables.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dmconflict.cascade import auroc, curve, summary_stats  # noqa: E402
from dmconflict.data import LABELS, load, split_ids  # noqa: E402
from dmconflict.metrics import bootstrap_ci, mcnemar_exact, paired_bootstrap  # noqa: E402
from dmconflict.run import _derived, _load_system, out_path, read_jsonl, summarise  # noqa: E402

OUT = ROOT / "paper" / "generated"
SPLIT = "test"
J13, J14 = "typesafe-ai/jev-1.13.0", "typesafe-ai/jev-1.14.0"
G25, G38 = "google/gemini-2.5-flash", "google/gemini-3.8-flash"
PRICE = 0.042
NUM: dict[str, str] = {}


def pct(x: float, nd: int = 1) -> str:
    return f"{100 * x:.{nd}f}"


def signed_pts(x: float) -> str:
    return f"{100 * x:+.1f}".replace("-", "$-$")


def pval(p: float) -> str:
    if p < 0.001:
        return "{<}0.001"   # works in text and inside $...$
    # Three decimals below 0.1, so a p-value near 0.05 never rounds onto the wrong side of it.
    return f"{p:.2f}" if p >= 0.1 else f"{p:.3f}"


def num(name: str, value: str) -> None:
    NUM[name] = value
    # Signed point differences also get an unsigned twin for prose ("trails by 8.1 points").
    if value.startswith(("$-$", "+")):
        NUM[name + "abs"] = value.replace("$-$", "").lstrip("+")


def nump(name: str, p: float) -> None:
    """A p-value macro for prose, written as $p\\name$, so it carries its relation: "=0.04", "<0.001"."""
    NUM[name] = "<0.001" if p < 0.001 else "=" + pval(p)


def write(name: str, text: str) -> None:
    # \fitwidth (paper/main.tex) shrinks a table only when it is wider than the column.
    text = text.replace(r"\begin{tabular}", r"\fitwidth{\begin{tabular}").replace(r"\end{tabular}", r"\end{tabular}}")
    (OUT / name).write_text(text + "\n")


def ok(recs):
    return np.array([r["pred"] == r["label"] for r in recs])


def load_test(spec: str) -> list[dict]:
    return _load_system(spec, SPLIT)


# --- Data -----------------------------------------------------------------------------------

def table_data() -> None:
    rows = load()
    dev, test = set(split_ids(rows, "dev")), set(split_ids(rows, "test"))
    names = {"no_conflict": "No conflict", "complementary": "Complementary information",
             "conflicting_opinions": "Conflicting opinions", "outdated": "Outdated information",
             "misinformation": "Misinformation"}
    body = []
    for k in LABELS:
        d = sum(r["label"] == k and r["id"] in dev for r in rows)
        t = sum(r["label"] == k and r["id"] in test for r in rows)
        body.append(f"{names[k]} & {d} & {t} & {d + t} \\\\")
    num("ndev", str(len(dev)))
    num("ntest", str(len(test)))
    num("nall", str(len(rows)))
    nres = np.mean([len(r["results"]) for r in rows])
    num("avgresults", f"{nres:.1f}")
    write("tab_data.tex", "\n".join([
        r"\begin{table}[t]", r"\centering\small", r"\begin{tabular}{lrrr}", r"\toprule",
        r"Conflict type & Dev & Test & All \\", r"\midrule", *body, r"\midrule",
        f"Total & {len(dev)} & {len(test)} & {len(rows)} \\\\", r"\bottomrule", r"\end{tabular}",
        r"\caption{\conflicts \citep{cattan2025dragged} and our frozen split. The development split (stratified, "
        r"fixed seed) is used only to choose settings; all reported results are on the test split unless stated.}",
        r"\label{tab:data}", r"\end{table}"]))


# --- Systems --------------------------------------------------------------------------------

# Every hosted decision model on the gateway (census of 2026-10-25, NOTES.md). Keys name the macros.
DM = [("Jev 1.13", J13, "jev"), ("Jev 1.14", J14, "jevnew"),
      ("Perplexity Decider v1.2", "perplexity/pplx-decider-v1.2", "pplx"),
      ("Perplexity Decider Flash v1.2", "perplexity/pplx-decider-flash-v1.2", "pplxflash"),
      ("OpenAI GPT-6 Luna Decisions", "openai/gpt-6-luna-decisions", "luna"),
      ("Liquid d1", "liquid/d1", "liquid"), ("Liquid d1 Ultra", "liquid/d1-ultra", "liquidultra"),
      ("Microsoft Decision-1", "microsoft/microsoft-decision-1", "msft"),
      ("Baseten Elephant-1", "baseten/elephant-1", "elephant"), ("Baseten Mammoth-1", "baseten/mammoth-1", "mammoth"),
      ("ScaleDown Classify-1$^\\S$", "scaledown/scaledown-classify-1", "scaledown")]
LLMS = [("Gemini 2.5 Flash, thinking off", G25, "paper_llm", "gtwofive"),
        ("Gemini 2.5 Flash, thinking on", G25, "paper_llm_thinking", "gtwofivethink"),
        ("Gemini 3.8 Flash, thinking low", G38, "paper_llm_low", "gthreeeight"),
        ("Gemini 3.8 Flash, default thinking", G38, "paper_llm_thinking", "gthreeeightdefault")]
LLM_REF, LLM_NOW = (G25, "paper_llm"), (G38, "paper_llm_low")   # the paper's setup; the current model
SCALEDOWN_NOTE = (r"$^\S$Its API accepts only a single text field, so it receives the same content as one text "
                  r"(the LLMs' numbered results).")
FREE_NOTE = r"$^\P$Free on the gateway at the time of the runs (billed \$0)."


def usd(x: float) -> str:
    return r"0$^\P$" if x == 0 else f"{x:.2f}"


DAGGER_NOTE = r"$^\dagger$Combination order revised on one model's (Jev~1.13) development answers (\S\ref{sec:formulation})."


def compare(a: np.ndarray, b: np.ndarray) -> dict:
    pb = paired_bootstrap(a, b)
    return {"diff": pb["diff"], "lo": pb["lo"], "hi": pb["hi"], "p": mcnemar_exact(a, b)}


def num_compare(key: str, c: dict) -> None:
    num(key + "diff", signed_pts(c["diff"]))
    num(key + "lo", signed_pts(c["lo"]))
    num(key + "hi", signed_pts(c["hi"]))
    nump(key + "p", c["p"])


def cell(c: dict) -> str:
    return f"{signed_pts(c['diff'])} ({pval(c['p'])})"


STATS: dict = {}


def stats(model: str, method: str) -> dict:
    if (model, method) not in STATS:
        STATS[(model, method)] = summarise(load_test(f"{model}:{method}"), PRICE)
    return STATS[(model, method)]


# Short names for the single-column tables.
SHORT = {"Perplexity Decider v1.2": "Perplexity v1.2", "Perplexity Decider Flash v1.2": "Perplexity Flash v1.2",
         "OpenAI GPT-6 Luna Decisions": "GPT-6 Luna", "Baseten Mammoth-1": "Mammoth-1",
         "Baseten Elephant-1": "Elephant-1", "Microsoft Decision-1": "Microsoft D-1",
         "ScaleDown Classify-1$^\\S$": "ScaleDown C-1$^\\S$"}


def short(name: str) -> str:
    return SHORT.get(name, name)


def by_flat_acc() -> list:
    return sorted(DM, key=lambda d: -stats(d[1], "flat")["acc"])


# --- Main comparison ------------------------------------------------------------------------

def table_main() -> None:
    ref, now = stats(*LLM_REF)["correct"], stats(*LLM_NOW)["correct"]
    body = [r"\multicolumn{8}{l}{\emph{Decision models, flat question (one forward pass)}} \\"]
    for name, model, key in by_flat_acc():
        s = stats(model, "flat")
        cr, cn = compare(s["correct"], ref), compare(s["correct"], now)
        body.append(f"\\quad {name} & {pct(s['acc'])} [{pct(s['acc_lo'])}, {pct(s['acc_hi'])}] & {pct(s['macro_f1'])} & "
                    f"{s['ece']:.3f} & {usd(s['usd_per_1k'])} & {s['lat_mean']:.2f} & {cell(cr)} & {cell(cn)} \\\\")
        num(key + "flatacc", pct(s["acc"]))
        num(key + "flatlo", pct(s["acc_lo"]))
        num(key + "flathi", pct(s["acc_hi"]))
        num(key + "mf", pct(s["macro_f1"]))
        num(key + "ece", f"{s['ece']:.3f}")
        num(key + "cost", f"{s['usd_per_1k']:.2f}")
        num(key + "lat", f"{s['lat_mean']:.2f}")
        num_compare(key + "vsref", cr)
        num_compare(key + "vsnow", cn)
    body.append(r"\multicolumn{8}{l}{\emph{Generative LLMs, the paper's prompt}} \\")
    for name, model, method, key in LLMS:
        s = stats(model, method)
        cr = "--" if (model, method) == LLM_REF else cell(compare(s["correct"], ref))
        cn = "--" if (model, method) == LLM_NOW else cell(compare(s["correct"], now))
        body.append(f"\\quad {name} & {pct(s['acc'])} [{pct(s['acc_lo'])}, {pct(s['acc_hi'])}] & {pct(s['macro_f1'])} & "
                    f"-- & {s['usd_per_1k']:.2f} & {s['lat_mean']:.2f} & {cr} & {cn} \\\\")
        num(key + "acc", pct(s["acc"]))
        num(key + "lo", pct(s["acc_lo"]))
        num(key + "hi", pct(s["acc_hi"]))
        num(key + "mf", pct(s["macro_f1"]))
        num(key + "cost", f"{s['usd_per_1k']:.2f}")
        num(key + "lat", f"{s['lat_mean']:.2f}")
    body += [r"\midrule", r"\quad Gemini 2.5 Flash, as published$^\ddagger$ & 65.3 & -- & -- & -- & -- & -- & -- \\"]
    write("tab_main.tex", "\n".join([
        r"\begin{table*}[t]", r"\centering\small\setlength{\tabcolsep}{4.5pt}", r"\begin{tabular}{lccccccc}", r"\toprule",
        r"System & Accuracy [95\% CI] & Macro-F1 & ECE & \$ / 1k & Lat.\ (s) & $\Delta$ Gem.\ 2.5 ($p$) & "
        r"$\Delta$ Gem.\ 3.8 ($p$) \\", r"\midrule", *body, r"\bottomrule", r"\end{tabular}",
        rf"\caption{{Conflict-type classification on the \conflicts test split ($n={NUM['ntest']}$), five classes, "
        r"sorted by accuracy. Every system sees the same inputs; the LLMs receive the paper's prompt verbatim and the "
        r"decision models a choice question with the same instructions, definitions and examples. Cost: billed cost "
        r"per 1,000 queries through one gateway (USD). Latency: mean per query. ECE is undefined for text answers. "
        r"$\Delta$: accuracy difference in points from Gemini~2.5 Flash (thinking off, the paper's setup) and from "
        r"Gemini~3.8 Flash (thinking low), exact McNemar $p$. " + SCALEDOWN_NOTE + " " + FREE_NOTE +
        r" $^\ddagger$Reported by \citet{cattan2025dragged} on all 458 queries; not comparable query by query.}",
        r"\label{tab:main}", r"\end{table*}"]))


def numbers_census() -> None:
    """Counts and ranges quoted in the abstract and introduction."""
    flat = {key: stats(model, "flat") for _, model, key in DM}
    ref, now = stats(*LLM_REF), stats(*LLM_NOW)
    vs_ref = {k: compare(s["correct"], ref["correct"]) for k, s in flat.items()}
    vs_now = {k: compare(s["correct"], now["correct"]) for k, s in flat.items()}
    num("ndm", str(len(DM)))
    num("nproviders", str(len({m.split("/")[0] for _, m, _ in DM})))
    accs = [s["acc"] for s in flat.values()]
    num("dmaccmin", pct(min(accs)))
    num("dmaccmax", pct(max(accs)))
    num("dmaccmedian", pct(float(np.median(accs))))
    num("ntiedref", str(sum(c["p"] >= 0.05 for c in vs_ref.values())))
    num("nbetterref", str(sum(c["p"] < 0.05 and c["diff"] > 0 for c in vs_ref.values())))
    num("nworseref", str(sum(c["p"] < 0.05 and c["diff"] < 0 for c in vs_ref.values())))
    num("ntiednow", str(sum(c["p"] >= 0.05 for c in vs_now.values())))
    num("nworsenow", str(sum(c["p"] < 0.05 and c["diff"] < 0 for c in vs_now.values())))
    costs = [s["usd_per_1k"] for s in flat.values() if s["usd_per_1k"] > 0]
    num("nfree", str(sum(s["usd_per_1k"] == 0 for s in flat.values())))
    lats = [s["lat_mean"] for s in flat.values()]
    num("dmcostmin", f"{min(costs):.2f}")
    num("dmcostmax", f"{max(costs):.2f}")
    num("dmlatmin", f"{min(lats):.2f}")
    num("dmlatmax", f"{max(lats):.2f}")
    # Cost and latency advantage of the decision models that tie or beat the paper's LLM.
    at_par = [k for k, c in vs_ref.items() if c["p"] >= 0.05 or c["diff"] > 0]
    num("natpar", str(len(at_par)))
    paid = [k for k in at_par if flat[k]["usd_per_1k"] > 0]
    num("costratiorefmin", f"{min(ref['usd_per_1k'] / flat[k]['usd_per_1k'] for k in paid):.0f}")
    num("costratiorefmax", f"{max(ref['usd_per_1k'] / flat[k]['usd_per_1k'] for k in paid):.0f}")
    num("latratiorefmin", f"{min(ref['lat_mean'] / flat[k]['lat_mean'] for k in at_par):.1f}")
    num("latratiorefmax", f"{max(ref['lat_mean'] / flat[k]['lat_mean'] for k in at_par):.1f}")
    num("nconfigsdm", str(2 * len(DM)))
    num("eceminimum", f"{min(s['ece'] for s in flat.values()):.3f}")
    num("ecemaximum", f"{max(s['ece'] for s in flat.values()):.3f}")
    for key, a, b in [("gthreeeightvstwofive", LLM_NOW, LLM_REF),
                      ("gthinkvsnothink", (G38, "paper_llm_thinking"), LLM_NOW),
                      ("gtwofivethinkvsnothink", (G25, "paper_llm_thinking"), LLM_REF)]:
        num_compare(key, compare(stats(*a)["correct"], stats(*b)["correct"]))
    num("costratiorefnow", f"{now['usd_per_1k'] / ref['usd_per_1k']:.1f}")


# --- Per-class ------------------------------------------------------------------------------

def table_perclass() -> None:
    test = load_test(f"{J13}:flat")
    support = {k: sum(r["label"] == k for r in test) for k in LABELS}
    head = "NC & Comp.\\ & Opin.\\ & Outd.\\ & Mis."
    sup = ", ".join(f"{n} {support[k]}" for n, k in zip(("No conflict", "Complementary", "Opinions", "Outdated",
                                                            "Misinformation"), LABELS))
    rows = [(short(name), stats(model, "flat")) for name, model, _ in by_flat_acc()]
    rows += [(n, stats(*spec)) for n, spec in (("Gemini 2.5 (off)", LLM_REF), ("Gemini 3.8 (low)", LLM_NOW))]
    body = [f"{name} & " + " & ".join(pct(s["f1"][k]) for k in LABELS) + r" \\" for name, s in rows]
    body.insert(len(DM), r"\midrule")
    write("tab_perclass.tex", "\n".join([
        r"\begin{table}[t]", r"\centering\footnotesize\setlength{\tabcolsep}{3pt}", r"\begin{tabular}{lccccc}", r"\toprule",
        f"F1 & {head} \\\\", r"\midrule", *body, r"\bottomrule", r"\end{tabular}",
        r"\caption{Per-class F1 on the test split (support: " + sup + "): decision models with the flat question, "
        r"then Gemini~2.5 Flash (thinking off) and Gemini~3.8 Flash (thinking low). " + SCALEDOWN_NOTE + "}",
        r"\label{tab:perclass}", r"\end{table}"]))
    outd = {key: stats(model, "flat")["f1"]["outdated"] for _, model, key in DM}
    misi = {key: stats(model, "flat")["f1"]["misinformation"] for _, model, key in DM}
    num("outdfmin", pct(min(outd.values())))
    num("outdfmax", pct(max(outd.values())))
    num("misifmax", pct(max(misi.values())))
    num("gthreeeightoutdf", pct(stats(*LLM_NOW)["f1"]["outdated"]))
    num("gthreeeightmisif", pct(stats(*LLM_NOW)["f1"]["misinformation"]))


# --- Question format ------------------------------------------------------------------------

def table_formulation() -> None:
    body = []
    n_v1_worse = n_v2_better = n_v2_worse = 0
    for name, model, key in by_flat_acc():
        f, t1, t2 = stats(model, "flat"), stats(model, "tree"), stats(model, "tree_v2")
        c1, c2 = compare(t1["correct"], f["correct"]), compare(t2["correct"], f["correct"])
        n_v1_worse += c1["p"] < 0.05 and c1["diff"] < 0
        n_v2_better += c2["p"] < 0.05 and c2["diff"] > 0
        n_v2_worse += c2["p"] < 0.05 and c2["diff"] < 0
        body.append(f"{short(name)} & {pct(f['acc'])} & {pct(t1['acc'])} & {pct(t2['acc'])} & {cell(c2)} \\\\")
        num(key + "treeoneacc", pct(t1["acc"]))
        num(key + "treeacc", pct(t2["acc"]))
        num(key + "treeece", f"{t2['ece']:.3f}")
        num_compare(key + "treevsflat", c2)
        num_compare(key + "treeonevsflat", c1)
        num_compare(key + "treevsnow", compare(t2["correct"], stats(*LLM_NOW)["correct"]))
    num("nvoneworse", str(n_v1_worse))
    num("nvtwobetter", str(n_v2_better))
    num("nvtwoworse", str(n_v2_worse))
    num("nvtwotied", str(len(DM) - n_v2_better - n_v2_worse))
    num("mftreeone", pct(stats(J13, "tree")["macro_f1"]))
    num("treeoneopinf", pct(stats(J13, "tree")["f1"]["conflicting_opinions"]))
    write("tab_formulation.tex", "\n".join([
        r"\begin{table}[t]", r"\centering\footnotesize\setlength{\tabcolsep}{3.5pt}", r"\begin{tabular}{lcccc}", r"\toprule",
        r"Decision model & Flat & Tree v1 & Tree v2$^\dagger$ & v2 $-$ flat ($p$) \\", r"\midrule", *body,
        r"\bottomrule", r"\end{tabular}",
        r"\caption{Accuracy (\%) by question format on the test split. The yes/no questions are identical for every "
        r"model and asked in one request. " + DAGGER_NOTE + " " + SCALEDOWN_NOTE + "}",
        r"\label{tab:formulation}", r"\end{table}"]))


# --- Cascade --------------------------------------------------------------------------------

def table_cascade() -> None:
    expensive = load_test(f"{G38}:paper_llm_low")
    g_usd = 1000 * float(np.mean([r["cost_usd"] or 0 for r in expensive]))
    body, tied, aurocs, gains, tied_cost = [], 0, [], [], []
    for name, model, key in by_flat_acc():
        cheap = load_test(f"{model}:flat")
        st = summary_stats(cheap, expensive)
        rows = {r["f"]: r for r in curve(cheap, expensive)}
        q, h = rows[0.25], rows[0.50]
        tied += q["p_vs_expensive"] >= 0.05
        if q["p_vs_expensive"] >= 0.05:
            tied_cost.append(100 * q["usd_per_1k"] / g_usd)
        aurocs.append(st["auroc"])
        gains.append(q["acc"] - q["acc_random"])
        body.append(f"{name} & {st['auroc']:.2f} & {pct(q['acc'])} & {pct(q['acc_random'])} & "
                    f"{signed_pts(q['vs_expensive']['diff'])} ({pval(q['p_vs_expensive'])}) & "
                    f"{100 * q['usd_per_1k'] / g_usd:.0f}\\% & {pct(h['acc'])} & "
                    f"{signed_pts(h['vs_expensive']['diff'])} ({pval(h['p_vs_expensive'])}) & "
                    f"{100 * h['usd_per_1k'] / g_usd:.0f}\\% \\\\")
        num(key + "auroc", f"{st['auroc']:.2f}")
        for fk, r in (("tf", q), ("fifty", h)):
            num(f"casc{key}{fk}acc", pct(r["acc"]))
            num(f"casc{key}{fk}rand", pct(r["acc_random"]))
            num(f"casc{key}{fk}cost", f"{100 * r['usd_per_1k'] / g_usd:.0f}")
            num(f"casc{key}{fk}lat", f"{r['lat_mean']:.2f}")
            num_compare(f"casc{key}{fk}", {**r["vs_expensive"], "p": r["p_vs_expensive"]})
    num("ncasctied", str(tied))
    num("casctiedcostmin", f"{min(tied_cost):.0f}")
    num("casctiedcostmax", f"{max(tied_cost):.0f}")
    num("aurocmin", f"{min(aurocs):.2f}")
    num("aurocmax", f"{max(aurocs):.2f}")
    num("nbeatrandom", str(sum(g > 0 for g in gains)))
    num("cascgainmin", f"{100 * min(gains):.1f}")
    num("cascgainmax", f"{100 * max(gains):.1f}")
    write("tab_cascade.tex", "\n".join([
        r"\begin{table*}[t]", r"\centering\small\setlength{\tabcolsep}{4.5pt}", r"\begin{tabular}{lccccccccc}", r"\toprule",
        r" & & \multicolumn{4}{c}{25\% escalated} & \multicolumn{3}{c}{50\% escalated} \\",
        r"\cmidrule(lr){3-6}\cmidrule(lr){7-9}",
        r"Cheap stage (flat) & AUROC & Acc. & Random & $\Delta$ LLM ($p$) & Cost & Acc. & $\Delta$ LLM ($p$) & Cost \\",
        r"\midrule", *body, r"\bottomrule", r"\end{tabular}",
        r"\caption{Confidence-gated cascade on the test split: the decision model answers every query and the "
        r"fraction with the lowest top probability goes to Gemini~3.8 Flash (thinking low; "
        rf"{NUM['gthreeeightacc']}\% alone). AUROC: how well the decision model's confidence separates its correct from "
        r"its wrong answers. Random: expected accuracy when the same number of queries is escalated at random. "
        r"$\Delta$ LLM: difference from the LLM alone in points (exact McNemar $p$). Cost: relative to the LLM alone. "
        r"Thresholds are label-free quantiles, fixed before computing. " + SCALEDOWN_NOTE + "}",
        r"\label{tab:cascade}", r"\end{table*}"]))


# --- Diagnostics ----------------------------------------------------------------------------

def _diag_load(model, method, pert=None):
    base = "tree" if method == "tree_v2" else method
    recs = read_jsonl(out_path(model, SPLIT, base, pert))
    if method == "tree_v2":
        recs = _derived(recs)["tree_v2"]
    return {r["id"]: r for r in recs}


def _pert(model, method, pert):
    o, p = _diag_load(model, method), _diag_load(model, method, pert)
    ids = sorted(set(o) & set(p))
    a = np.array([o[i]["pred"] == o[i]["label"] for i in ids])
    b = np.array([p[i]["pred"] == p[i]["label"] for i in ids])
    flips = np.array([o[i]["pred"] != p[i]["pred"] for i in ids])
    outd = [i for i in ids if o[i]["label"] == "outdated"]
    return {"cmp": compare(b, a), "flips": flips, "n": len(ids),
            "rec_o": float(np.mean([o[i]["pred"] == "outdated" for i in outd])),
            "rec_p": float(np.mean([p[i]["pred"] == "outdated" for i in outd]))}



def table_diagnostics() -> None:
    systems = [(name, model, "flat", key) for name, model, key in by_flat_acc()]
    systems.append(("Gemini 3.8 Flash (low)", G38, "paper_llm_low", "gm"))
    body, n_date_sig, above_floor, recs_ok = [], 0, 0, 0
    floor_all, shuf_all = [], []
    n_det = n_more = n_less = n_shuf_sig = 0
    g1, g2 = _pert(G38, "paper_llm_low", "shuffle1"), _pert(G38, "paper_llm_low", "shuffle2")
    gm_flips = np.concatenate([g1["flips"], g2["flips"]])
    for name, model, method, key in systems:
        rr, nd, dc = _pert(model, method, "rerun"), _pert(model, method, "no_dates"), _pert(model, method, "dates_in_code")
        s1, s2 = _pert(model, method, "shuffle1"), _pert(model, method, "shuffle2")
        shuf = np.concatenate([s1["flips"], s2["flips"]]).astype(float)
        lo, hi = bootstrap_ci(shuf)
        if key != "gm":
            n_date_sig += (nd["cmp"]["p"] < 0.05) + (dc["cmp"]["p"] < 0.05)
            above_floor += lo > rr["flips"].mean()
            floor_all.append(rr["flips"].mean())
            shuf_all.append(shuf.mean())
            recs_ok += nd["rec_p"] >= nd["rec_o"] - 0.05
            n_det += rr["flips"].sum() == 0
            mine = np.concatenate([s1["flips"], s2["flips"]])
            pf = mcnemar_exact(mine, gm_flips)   # same queries and shuffles, paired
            n_more += pf < 0.05 and mine.mean() > gm_flips.mean()
            n_less += pf < 0.05 and mine.mean() < gm_flips.mean()
            n_shuf_sig += (s1["cmp"]["p"] < 0.05) + (s2["cmp"]["p"] < 0.05)
            num_compare(f"diag{key}shuffleone", s1["cmp"])
            num_compare(f"diag{key}shuffletwo", s2["cmp"])
        body.append(f"{name} & {pct(rr['flips'].mean())} & {cell(nd['cmp'])} & {cell(dc['cmp'])} & "
                    f"{pct(nd['rec_o'])} / {pct(nd['rec_p'])} & {pct(shuf.mean())} [{pct(lo)}, {pct(hi)}] & "
                    f"{cell(s1['cmp'])} & {cell(s2['cmp'])} \\\\")
        num(f"diag{key}rerunflip", pct(rr["flips"].mean()))
        num(f"diag{key}shuffleflip", pct(shuf.mean()))
        num(f"diag{key}shufflelo", pct(lo))
        num(f"diag{key}shufflehi", pct(hi))
        num_compare(f"diag{key}nodates", nd["cmp"])
        num_compare(f"diag{key}datesincode", dc["cmp"])
        num(f"diag{key}origrec", pct(nd["rec_o"]))
        num(f"diag{key}nodatesrec", pct(nd["rec_p"]))
        num(f"diag{key}datesincoderec", pct(dc["rec_p"]))
    body.insert(len(systems) - 1, r"\midrule")
    num("ndatetests", str(2 * len(DM)))
    num("ndeterministic", str(n_det))
    num("nflipmore", str(n_more))
    num("nflipless", str(n_less))
    num("nflipsame", str(len(DM) - n_more - n_less))
    num("nshufflesig", str(n_shuf_sig))
    num("ndatesig", str(n_date_sig))
    num("nshuffleabovefloor", str(above_floor))
    num("rerunflipmin", pct(min(floor_all)))
    num("rerunflipmax", pct(max(floor_all)))
    num("shuffleflipmin", pct(min(shuf_all)))
    num("shuffleflipmax", pct(max(shuf_all)))
    write("tab_diagnostics.tex", "\n".join([
        r"\begin{table*}[t]", r"\centering\footnotesize\setlength{\tabcolsep}{4pt}", r"\begin{tabular}{lccccccc}", r"\toprule",
        r" & Rerun & \multicolumn{3}{c}{Dates} & \multicolumn{3}{c}{Source order} \\",
        r"\cmidrule(lr){3-5}\cmidrule(lr){6-8}",
        r"System & Flip & No dates & Recency in code & Outd.\ recall & Flip [95\% CI] & Shuffle 1 & Shuffle 2 \\",
        r"\midrule", *body, r"\bottomrule", r"\end{tabular}",
        r"\caption{Diagnostics on the test split, flat question. Each perturbed run is compared with the same system's "
        r"original run on the same queries. Flip: share of queries whose predicted type changed (\%); for source order, "
        r"pooled over two shuffles. No dates, Recency in code, Shuffle: accuracy change in points (exact McNemar $p$). "
        r"Outd.\ recall: recall (\%) on the 55 \emph{Outdated} queries, original / without dates. The identical rerun "
        r"is the noise floor. " + SCALEDOWN_NOTE + "}", r"\label{tab:diagnostics}", r"\end{table*}"]))


def table_plant() -> None:
    systems = [(short(name), model, "flat", key) for name, model, key in by_flat_acc()]
    systems.append(("Gemini 3.8 (low)", G38, "paper_llm_low", "gm"))
    body, youdens, aurocs, ydiff, hits = [], {}, [], {}, []
    gm_o, gm_p = _diag_load(G38, "paper_llm_low"), _diag_load(G38, "paper_llm_low", "plant")
    for name, m, me, key in systems:
        o, p = _diag_load(m, me), _diag_load(m, me, "plant")
        ids = sorted(p)
        hit = np.array([p[i]["pred"] == "misinformation" for i in ids])
        fa = np.array([o[i]["pred"] == "misinformation" for i in ids])
        hc = np.array([p[i]["pred"] != "no_conflict" for i in ids])
        fc = np.array([o[i]["pred"] != "no_conflict" for i in ids])
        au = "--"
        if me != "paper_llm_low":
            sc = np.array([p[i]["probs"]["misinformation"] for i in ids] + [o[i]["probs"]["misinformation"] for i in ids])
            lab = np.array([True] * len(ids) + [False] * len(ids))
            a = auroc(sc, lab)
            aurocs.append(a)
            au = f"{a:.2f}"
            num(f"plant{key}auroc", au)
            youdens[key] = hit.mean() - fa.mean()
            g_hit = np.array([gm_p[i]["pred"] == "misinformation" for i in ids])
            g_fa = np.array([gm_o[i]["pred"] == "misinformation" for i in ids])
            d = (hit.astype(int) - fa.astype(int)) - (g_hit.astype(int) - g_fa.astype(int))
            lo, hi = bootstrap_ci(d.astype(float))
            ydiff[key] = (d.mean(), lo, hi)
            hits.append(hit.mean())
        body.append(f"{name} & {pct(hit.mean())} & {pct(fa.mean())} & {hit.mean() - fa.mean():+.3f} & "
                    f"{pct(hc.mean())} / {pct(fc.mean())} & {au} \\\\")
        num(f"plant{key}hit", pct(hit.mean()))
        num(f"plant{key}fa", pct(fa.mean()))
        num(f"plant{key}youden", f"{hit.mean() - fa.mean():+.3f}")
        num("nplant", str(len(ids)))
    body.insert(len(systems) - 1, r"\midrule")
    gy = float(np.mean([gm_p[i]["pred"] == "misinformation" for i in sorted(gm_p)]) -
               np.mean([gm_o[i]["pred"] == "misinformation" for i in sorted(gm_p)]))
    num("nyoudenatleastgm", str(sum(y >= gy - 1e-9 for y in youdens.values())))
    num("nyoudenlower", str(sum(hi < 0 for _, _, hi in ydiff.values())))
    num("nyoudentied", str(sum(lo <= 0 <= hi for _, lo, hi in ydiff.values())))
    num("planthitmin", pct(min(hits)))
    num("planthitmax", pct(max(hits)))
    num("nplantaurochigh", str(sum(a >= 0.75 for a in aurocs)))
    num("youdenmin", f"{min(youdens.values()):+.3f}")
    num("youdenmax", f"{max(youdens.values()):+.3f}")
    num("plantaurocmin", f"{min(aurocs):.2f}")
    num("plantaurocmax", f"{max(aurocs):.2f}")
    jt_p = _diag_load(J13, "tree_v2", "plant")
    num("plantjthit", pct(float(np.mean([jt_p[i]["pred"] == "misinformation" for i in sorted(jt_p)]))))
    write("tab_plant.tex", "\n".join([
        r"\begin{table}[t]", r"\centering\footnotesize\setlength{\tabcolsep}{3pt}", r"\begin{tabular}{lccccc}", r"\toprule",
        r"System & Hit & F.A. & Youden & Any & AUROC \\", r"\midrule", *body, r"\bottomrule", r"\end{tabular}",
        rf"\caption{{One planted false source in {NUM['nplant']} \emph{{No conflict}} test queries (expected label: "
        r"\emph{Misinformation}), flat question. Hit: planted copy labelled Misinformation (\%). F.A.: clean copy of "
        r"the same query labelled Misinformation (\%). Youden: hit $-$ false alarm. Any: planted / clean copy not "
        r"labelled No conflict (\%). AUROC: P(Misinformation) separating planted from clean copies. " + SCALEDOWN_NOTE + "}",
        r"\label{tab:plant}", r"\end{table}"]))


# --- End to end -----------------------------------------------------------------------------

# Judge validation sheets (human_eval/README.md). Annotator 2's sheet shows item 98's response under item 99, so
# that label is for another text and is excluded.
SHEETS = ["behaviour_sample_1.csv", "behaviour_sample_2.csv"]
EXCLUDE = {("behaviour_sample_2.csv", 99)}


def judge_validation(judges: dict) -> None:
    import csv

    from dmconflict.endtoend import _kappa, judge_path

    key = {int(r["item"]): r for r in csv.DictReader(open(ROOT / "runs" / f"human_eval_key_{SPLIT}.csv"))}
    labels: dict[int, dict] = {}
    for sheet in SHEETS:
        for r in csv.DictReader(open(ROOT / "human_eval" / sheet, encoding="utf-8-sig")):
            if (sheet, int(r["item"])) not in EXCLUDE:
                labels.setdefault(int(r["item"]), {})[sheet] = int(r["follows (1/0)"])
    items = sorted(labels)
    # Majority of the annotators; a tie counts as "follows" (coded before labelling).
    human = np.array([round(np.mean(list(labels[i].values())) + 1e-9) for i in items])
    num("nvalid", str(len(items)))
    both = [i for i in items if len(labels[i]) == 2]
    a, b = (np.array([labels[i][s] for i in both]) for s in SHEETS)
    num("iaa", pct(float(np.mean(a == b)), 0))
    num("iaakappa", f"{_kappa(a, b):.2f}")
    num("humanfollows", pct(float(human.mean()), 0))
    for key_, model in judges.items():
        v = {(r["id"], r["cond"]): r["verdict"] for r in read_jsonl(judge_path(SPLIT, "behaviour", model))}
        j = np.array([v[(int(key[i]["id"]), key[i]["cond"])] for i in items]).astype(int)
        num(key_ + "valacc", pct(float(np.mean(j == human)), 0))
        num(key_ + "valkappa", f"{_kappa(human, j):.2f}")
        num(key_ + "follows", pct(float(j.mean()), 0))
        for n, s in enumerate(SHEETS, 1):
            sub = [k for k, i in enumerate(items) if s in labels[i]]
            num(key_ + "valacc" + ["one", "two"][n - 1],
                pct(float(np.mean(j[sub] == np.array([labels[items[k]][s] for k in sub]))), 0))


def table_endtoend() -> None:
    from dmconflict.endtoend import scores

    judges = {"ee": G25, "fb": G38}   # primary judge; second judge, pre-specified
    sc = {k: scores(SPLIT, m) for k, m in judges.items()}
    judge_validation(judges)
    rows = [("Vanilla (no type)", "Vanilla", None, "van"),
            ("Gemini 2.5 Flash, thinking off$^\\ast$", "Gemini 2.5 Flash (thinking off)", stats(*LLM_REF), "pipe"),
            ("Gemini 3.8 Flash, thinking low", "Gemini 3.8 Flash (thinking low)", stats(*LLM_NOW), "gthreeeight")]
    rows += [(short(name), model.split("/")[-1], stats(model, "flat"), key) for name, model, key in by_flat_acc()]
    rows.append(("Gold type (Oracle)", "Oracle (gold type)", None, "oracle"))

    def adh(j, cond):
        return sc[j][cond]["behaviour"]

    body, tied, worse, casc_tied, fb_tied, diffs, cdiffs = [], {}, {}, {}, {}, [], []
    for name, cond, st, key in rows:
        ref = {j: adh(j, "Gemini 2.5 Flash (thinking off)") for j in judges}
        van = {j: adh(j, "Vanilla") for j in judges}
        c = {j: compare(adh(j, cond), ref[j]) for j in judges}
        cv = {j: compare(adh(j, cond), van[j]) for j in judges}
        for j in judges:
            num(f"{j}{key}", pct(float(adh(j, cond).mean())))
            num_compare(f"{j}{key}vsvan", cv[j])
            num_compare(f"{j}{key}vspipe", c[j])
        typ = "--" if st is None and key == "van" else ("100" if st is None else pct(st["acc"]))
        cost = "--" if st is None else usd(st["usd_per_1k"])
        same = cond == "Gemini 2.5 Flash (thinking off)"
        line = (f"{name} & {typ} & {cost} & {pct(float(adh('ee', cond).mean()))} & "
                f"{'--' if same else cell(c['ee'])} & {pct(float(adh('fb', cond).mean()))} & "
                f"{'--' if same else cell(c['fb'])}")
        if st is not None and key not in ("pipe", "gthreeeight"):
            cc = compare(adh("ee", f"{cond} → Gemini 3.8 (25%)"), ref["ee"])
            line += f" & {pct(float(adh('ee', cond + ' → Gemini 3.8 (25%)').mean()))} & {cell(cc)}"
            tied[key], fb_tied[key], casc_tied[key] = c["ee"]["p"] >= 0.05, c["fb"]["p"] >= 0.05, cc["p"] >= 0.05
            worse[key] = c["ee"]["p"] < 0.05 and c["ee"]["diff"] < 0
            diffs.append(c["ee"]["diff"])
            cdiffs.append(cc["diff"])
        else:
            line += " & &"
        if key == "oracle":
            body.append(r"\midrule")
        body.append(line + r" \\")
        if key == "pipe":
            body.append(r"\midrule")
    num("eentied", str(sum(tied.values())))
    num("eenworse", str(sum(worse.values())))
    num("eedmdiffmin", signed_pts(min(diffs)))
    num("eedmdiffmax", signed_pts(max(diffs)))
    num("eencasctied", str(sum(casc_tied.values())))
    num("eecascdiffmin", signed_pts(min(cdiffs)))
    num("eecascdiffmax", signed_pts(max(cdiffs)))
    num("fbntied", str(sum(fb_tied.values())))
    # Share of the gold type's gain that each predictor recovers (primary judge).
    for j in judges:
        v, o = adh(j, "Vanilla").mean(), adh(j, "Oracle (gold type)").mean()
        num(f"{j}pipeshare", f"{100 * (adh(j, 'Gemini 2.5 Flash (thinking off)').mean() - v) / (o - v):.0f}")
    # Gains by gold type and answer recall.
    labs = {"no_conflict": "noconf", "complementary": "comp", "conflicting_opinions": "opin", "outdated": "outd",
            "misinformation": "misi"}
    for cond, key in (("Vanilla", "van"), ("Oracle (gold type)", "oracle"), ("Gemini 2.5 Flash (thinking off)", "pipe")):
        for lab, lk in labs.items():
            num(f"ee{key}{lk}", pct(sc["ee"][cond]["per_type"][lab]))
    recalls = {j: [float(s["recall"].mean()) for s in sc[j].values()] for j in judges}
    num("eenrecall", str(len(next(iter(sc["ee"].values()))["recall"])))
    for j in judges:
        num(f"{j}recallmin", pct(min(recalls[j])))
        num(f"{j}recallmax", pct(max(recalls[j])))
    num("eenanswers", f"{sum(1 for _ in read_jsonl(ROOT / 'runs' / G25.replace('/', '__') / SPLIT / 'answers.jsonl')):,}")
    write("tab_endtoend.tex", "\n".join([
        r"\begin{table*}[t]", r"\centering\small\setlength{\tabcolsep}{4.5pt}", r"\begin{tabular}{lcccccccc}", r"\toprule",
        r" & \multicolumn{2}{c}{Type predictor} & \multicolumn{2}{c}{Judge: Gemini 2.5} & "
        r"\multicolumn{2}{c}{Judge: Gemini 3.8} & \multicolumn{2}{c}{25\% to Gemini 3.8$^\dagger$} \\",
        r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}",
        r"Type given to the generator & Acc. & \$ / 1k & Adh. & $\Delta$ ($p$) & Adh. & $\Delta$ ($p$) & "
        r"Adh. & $\Delta$ ($p$) \\",
        r"\midrule", *body, r"\bottomrule", r"\end{tabular}",
        rf"\caption{{End to end on the test split ($n={NUM['ntest']}$): Gemini~2.5 Flash answers given the type from "
        r"the first column (the Pipeline of \citet{cattan2025dragged}). Acc.: type accuracy (\%). \$ / 1k: "
        r"classification cost per 1,000 queries. Adh.: answers following the gold type's expected behaviour (\%), "
        r"per LLM judge. $\Delta$: points from the original setup$^\ast$ (exact McNemar $p$). $^\dagger$Cascade of "
        r"Table~\ref{tab:cascade}, primary judge. $^\S$Single text field (Table~\ref{tab:main}). "
        r"$^\P$Billed \$0.}",
        r"\label{tab:endtoend}", r"\end{table*}"]))


def extras() -> None:
    """Numbers quoted in the text that no table holds."""
    # Development-split evidence for the tree v2 revision (Jev 1.13 tree v1 answers).
    dev = {r["id"]: r for r in read_jsonl(out_path(J13, "dev", "tree"))}
    mean = lambda q, lab: float(np.mean([r["raw"][q] for r in dev.values() if r["label"] == lab]))
    num("devcompatopin", f"{mean('compatible', 'conflicting_opinions'):.2f}")
    num("devcompatcomp", f"{mean('compatible', 'complementary'):.2f}")
    misinfo_means = [mean("misinformation", lab) for lab in LABELS]
    num("devmisinfolo", f"{min(misinfo_means):.2f}")
    num("devmisinfohi", f"{max(misinfo_means):.2f}")
    op = np.array([r["raw"]["opinion"] for r in dev.values() if r["label"] in ("conflicting_opinions", "complementary")])
    lab = np.array([r["label"] == "conflicting_opinions" for r in dev.values() if r["label"] in ("conflicting_opinions", "complementary")])
    num("devopinionauroc", f"{auroc(op, lab):.2f}")
    num("devopintocomp", str(sum(r["label"] == "conflicting_opinions" and r["pred"] == "complementary" for r in dev.values())))
    num("devnopin", str(sum(r["label"] == "conflicting_opinions" for r in dev.values())))
    t1 = load_test(f"{J13}:tree")
    num("testopintocomp", str(sum(r["label"] == "conflicting_opinions" and r["pred"] == "complementary" for r in t1)))
    num("testnopin", str(sum(r["label"] == "conflicting_opinions" for r in t1)))
    # Over-confidence: mean top probability against accuracy, per decision model.
    gaps = {key: float(np.mean([max(r["probs"].values()) for r in load_test(f"{m}:flat")])) - stats(m, "flat")["acc"]
            for _, m, key in DM}
    num("noverconf", str(sum(g > 0 for g in gaps.values())))
    num_compare("versions", compare(stats(J14, "flat")["correct"], stats(J13, "flat")["correct"]))
    num_compare("versionstree", compare(stats(J14, "tree_v2")["correct"], stats(J13, "tree_v2")["correct"]))
    # All 458 queries (the paper's scope) for the reproduction gap.
    num("allgtwofive", pct(float(ok(_load_system(f"{G25}:paper_llm", "all")).mean())))
    # Latency ranking over every configuration run on the test split.
    configs = [f"{m}:{me}" for _, m, _ in DM for me in ("flat", "tree")]
    configs += [f"{m}:{me}" for _, m, me, _ in LLMS]
    lat = {c: float(np.mean([r["latency_s"] for r in load_test(c)])) for c in configs}
    num("nconfigs", str(len(configs)))
    llm_fastest = min(v for c, v in lat.items() if c.startswith("google/"))
    num("nfasterthanllm", str(sum(v < llm_fastest for c, v in lat.items() if not c.startswith("google/"))))
    # Lenient parsing: Gemini answers whose category is not in the requested JSON field.
    strict = re.compile(r'"category"\s*:\s*"?\s*([1-5])\b')
    gem = [r for m in (G25, G38) for p in sorted((ROOT / "runs" / m.replace("/", "__")).glob("*/*.jsonl"))
           for r in read_jsonl(p)]
    num("ngemini", f"{len(gem):,}")
    num("nlenient", str(sum(not strict.search(r["text"]) for r in gem)))
    j = stats(J13, "flat")
    num("cihalf", f"{100 * (j['acc_hi'] - j['acc_lo']) / 2:.1f}")
    num("medtokens", f"{int(np.median([r['usage']['inputTokens'] for r in load_test(f'{J13}:flat')])):,}")
    num("nmisitest", str(sum(r["label"] == "misinformation" for r in load_test(f"{J13}:flat"))))


def prompt_files() -> None:
    """The exact prompt texts, for verbatim listings in the appendix."""
    from dmconflict.perturb import WRONG_ANSWER_PROMPT
    from dmconflict.prompts import FLAT_INSTRUCTIONS, PAPER_PROMPT, TREE_QUESTIONS

    (OUT / "paper_prompt.txt").write_text(PAPER_PROMPT + "\n")
    (OUT / "flat_question.txt").write_text(
        "type: choice\ninstructions: " + FLAT_INSTRUCTIONS + "\noptions: the five category definitions of the prompt "
        "above, each with its example, keyed no_conflict, complementary, conflicting_opinions, outdated, misinformation\n")
    (OUT / "tree_questions.txt").write_text("".join(f"{k} (yes/no): {v}\n" for k, v in TREE_QUESTIONS.items()))
    (OUT / "wrong_answer_prompt.txt").write_text(WRONG_ANSWER_PROMPT + "\n")
    # End to end: the generation prompt with a type, and the judge prompts (shown for Misinformation).
    from dmconflict.generate import TYPE_PROMPT, behaviour_prompt, recall_prompt
    (OUT / "type_prompt.txt").write_text(TYPE_PROMPT + "\n")
    row = {"label": "misinformation", "question": "{query}", "answer": "{gold answer}"}
    (OUT / "judge_prompt.txt").write_text(behaviour_prompt(row, "{response}") + "\n")
    (OUT / "recall_prompt.txt").write_text(recall_prompt(row, "{response}") + "\n")


def write_numbers() -> None:
    lines = ["% Generated by scripts/make_tables.py from the stored runs. Do not edit."]
    for k, v in sorted(NUM.items()):
        assert k.isalpha(), k  # LaTeX macro names: letters only
        lines.append(f"\\newcommand{{\\{k}}}{{{v}\\xspace}}")
    write("numbers.tex", "\n".join(lines))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    table_data()
    table_main()
    numbers_census()
    table_perclass()
    table_formulation()
    table_cascade()
    table_diagnostics()
    table_plant()
    table_endtoend()
    extras()
    prompt_files()
    write_numbers()
    print(f"wrote {len(list(OUT.glob('*.tex')))} files and {len(NUM)} numbers to {OUT}")


if __name__ == "__main__":
    main()
