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
from jevconflict.cascade import auroc, curve, summary_stats  # noqa: E402
from jevconflict.data import LABELS, load, split_ids  # noqa: E402
from jevconflict.metrics import bootstrap_ci, mcnemar_exact, paired_bootstrap  # noqa: E402
from jevconflict.run import _derived, _load_system, out_path, read_jsonl, summarise  # noqa: E402

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
    return f"{p:.2f}" if p >= 0.01 else f"{p:.3f}"


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
        r"\caption{CONFLICTS \citep{cattan2025dragged} and our frozen split. The development split (stratified, "
        r"fixed seed) is used only to choose settings; all reported results are on the test split unless stated.}",
        r"\label{tab:data}", r"\end{table}"]))


# --- Main comparison ------------------------------------------------------------------------

MAIN = [
    ("Decision model (one forward pass)", None, None),
    ("Jev 1.13, flat", J13, "flat"),
    ("Jev 1.13, tree v1", J13, "tree"),
    ("Jev 1.13, tree v2$^\\dagger$", J13, "tree_v2"),
    ("Jev 1.14, flat", J14, "flat"),
    ("Jev 1.14, tree v2$^\\dagger$", J14, "tree_v2"),
    ("Generative LLM, paper's prompt", None, None),
    ("Gemini 2.5 Flash, thinking off", G25, "paper_llm"),
    ("Gemini 2.5 Flash, thinking on", G25, "paper_llm_thinking"),
    ("Gemini 3.8 Flash, thinking low", G38, "paper_llm_low"),
    ("Gemini 3.8 Flash, default thinking", G38, "paper_llm_thinking"),
]


def table_main() -> dict:
    stats = {}
    body = []
    for label, model, method in MAIN:
        if model is None:
            body.append(rf"\multicolumn{{6}}{{l}}{{\emph{{{label}}}}} \\")
            continue
        s = summarise(load_test(f"{model}:{method}"), PRICE)
        stats[(model, method)] = s
        ece = "--" if s["ece"] != s["ece"] else f"{s['ece']:.3f}"
        body.append(f"\\quad {label} & {pct(s['acc'])} [{pct(s['acc_lo'])}, {pct(s['acc_hi'])}] & "
                    f"{pct(s['macro_f1'])} & {ece} & {s['usd_per_1k']:.2f} & {s['lat_mean']:.2f} \\\\")
    body.append(r"\midrule")
    body.append(r"\quad Gemini 2.5 Flash, as published$^\ddagger$ & 65.3 & -- & -- & -- & -- \\")
    write("tab_main.tex", "\n".join([
        r"\begin{table*}[t]", r"\centering\small", r"\begin{tabular}{lccccc}", r"\toprule",
        r"System & Accuracy [95\% CI] & Macro-F1 & ECE & \$ / 1k queries & Latency (s) \\", r"\midrule",
        *body, r"\bottomrule", r"\end{tabular}",
        rf"\caption{{Conflict-type classification on the CONFLICTS test split ($n={NUM['ntest']}$), five classes. "
        r"All systems see identical inputs; the LLMs receive the paper's prompt verbatim and Jev's \emph{flat} question "
        r"carries the same instructions, definitions and examples. Cost is billed cost through one gateway; latency is "
        r"the mean per query. ECE is undefined for hard-label systems. $^\dagger$Combination order revised on the "
        r"development split (\S\ref{sec:formulation}). $^\ddagger$Reported by \citet{cattan2025dragged} on all 458 "
        r"queries; not comparable query by query.}", r"\label{tab:main}", r"\end{table*}"]))
    return stats


def numbers_main(stats: dict) -> None:
    j, g25, g38 = stats[(J13, "flat")], stats[(G25, "paper_llm")], stats[(G38, "paper_llm_low")]
    num("jevacc", pct(j["acc"]))
    num("jevlo", pct(j["acc_lo"]))
    num("jevhi", pct(j["acc_hi"]))
    num("jevcost", f"{j['usd_per_1k']:.2f}")
    num("jevlat", f"{j['lat_mean']:.2f}")
    num("jevece", f"{j['ece']:.3f}")
    num("gtwofiveacc", pct(g25["acc"]))
    num("gtwofivecost", f"{g25['usd_per_1k']:.2f}")
    num("gtwofivelat", f"{g25['lat_mean']:.2f}")
    num("gthreeeightacc", pct(g38["acc"]))
    num("gthreeeightcost", f"{g38['usd_per_1k']:.2f}")
    num("gthreeeightlat", f"{g38['lat_mean']:.2f}")
    num("costratiotwofive", f"{g25['usd_per_1k'] / j['usd_per_1k']:.1f}")
    num("costratiothreeeight", f"{g38['usd_per_1k'] / j['usd_per_1k']:.0f}")
    num("latratiotwofive", f"{g25['lat_mean'] / j['lat_mean']:.1f}")
    num("latratiothreeeight", f"{g38['lat_mean'] / j['lat_mean']:.1f}")
    for key, a, b in [("jevvstwofive", (J13, "flat"), (G25, "paper_llm")),
                      ("jevvsthreeeight", (J13, "flat"), (G38, "paper_llm_low")),
                      ("treevtwovsthreeeight", (J13, "tree_v2"), (G38, "paper_llm_low")),
                      ("treevtwovsgthreeeightdefault", (J13, "tree_v2"), (G38, "paper_llm_thinking")),
                      ("flatvstree", (J13, "flat"), (J13, "tree")),
                      ("flatvstreevtwo", (J13, "flat"), (J13, "tree_v2")),
                      ("onefourvsonethree", (J14, "flat"), (J13, "flat")),
                      ("onefourtreevsonethree", (J14, "tree_v2"), (J13, "tree_v2")),
                      ("onefourvstwofive", (J14, "flat"), (G25, "paper_llm")),
                      ("gthreeeightvstwofive", (G38, "paper_llm_low"), (G25, "paper_llm")),
                      ("gthinkvsnothink", (G38, "paper_llm_thinking"), (G38, "paper_llm_low")),
                      ("gtwofivethinkvsnothink", (G25, "paper_llm_thinking"), (G25, "paper_llm"))]:
        pb = paired_bootstrap(stats[a]["correct"], stats[b]["correct"])
        num(key + "diff", signed_pts(pb["diff"]))
        num(key + "lo", signed_pts(pb["lo"]))
        num(key + "hi", signed_pts(pb["hi"]))
        nump(key + "p", mcnemar_exact(stats[a]["correct"], stats[b]["correct"]))
    for k, (m, me) in {"treeone": (J13, "tree"), "treetwo": (J13, "tree_v2"), "onefour": (J14, "flat"),
                       "onefourtree": (J14, "tree_v2"), "gtwofivethink": (G25, "paper_llm_thinking"),
                       "gthreeeightdefault": (G38, "paper_llm_thinking")}.items():
        num(k + "acc", pct(stats[(m, me)]["acc"]))
        if stats[(m, me)]["ece"] == stats[(m, me)]["ece"]:
            num(k + "ece", f"{stats[(m, me)]['ece']:.3f}")
    num("mftreeone", pct(stats[(J13, "tree")]["macro_f1"]))
    num("mftreetwo", pct(stats[(J13, "tree_v2")]["macro_f1"]))
    num("mfjev", pct(j["macro_f1"]))


# --- Per-class ------------------------------------------------------------------------------

def table_perclass(stats: dict) -> None:
    systems = [("Jev 1.13, flat", (J13, "flat")), ("Jev 1.13, tree v1", (J13, "tree")),
               ("Jev 1.13, tree v2$^\\dagger$", (J13, "tree_v2")),
               ("Gemini 2.5 Flash (off)", (G25, "paper_llm")), ("Gemini 3.8 Flash (low)", (G38, "paper_llm_low"))]
    test = load_test(f"{J13}:flat")
    support = {k: sum(r["label"] == k for r in test) for k in LABELS}
    head = " & ".join([f"NC ({support['no_conflict']})", f"Comp.\\ ({support['complementary']})",
                       f"Opin.\\ ({support['conflicting_opinions']})", f"Outd.\\ ({support['outdated']})",
                       f"Misinf.\\ ({support['misinformation']})"])
    body = [f"{name} & " + " & ".join(pct(stats[key]["f1"][k]) for k in LABELS) + r" \\" for name, key in systems]
    write("tab_perclass.tex", "\n".join([
        r"\begin{table*}[t]", r"\centering\small", r"\begin{tabular}{lccccc}", r"\toprule",
        f"F1 & {head} \\\\", r"\midrule", *body, r"\bottomrule", r"\end{tabular}",
        r"\caption{Per-class F1 on the test split (support in parentheses). Tree v1 almost never predicts "
        r"\emph{Conflicting opinions}; flat Jev is strongest on \emph{Outdated}. $^\dagger$Revised on development data.}",
        r"\label{tab:perclass}", r"\end{table*}"]))
    num("treeoneopinf", pct(stats[(J13, "tree")]["f1"]["conflicting_opinions"]))
    num("jevoutdf", pct(stats[(J13, "flat")]["f1"]["outdated"]))
    num("gthreeeightoutdf", pct(stats[(G38, "paper_llm_low")]["f1"]["outdated"]))
    num("treetwooutdf", pct(stats[(J13, "tree_v2")]["f1"]["outdated"]))


# --- Other decision models ------------------------------------------------------------------

OTHERS = [("Jev 1.13", J13), ("Perplexity v1.2", "perplexity/pplx-decider-v1.2"),
          ("GPT-6-luna", "openai/gpt-6-luna-decisions"), ("Liquid d1", "liquid/d1"),
          ("Microsoft d-1", "microsoft/microsoft-decision-1")]


def table_decision_models() -> None:
    jev = ok(load_test(f"{J13}:flat"))
    g38 = ok(load_test(f"{G38}:paper_llm_low"))
    body = []
    for name, model in OTHERS:
        f = summarise(load_test(f"{model}:flat"), PRICE)
        t = summarise(load_test(f"{model}:tree_v2"), PRICE)
        vs_j = "--" if model == J13 else f"{signed_pts(paired_bootstrap(f['correct'], jev)['diff'])} ({pval(mcnemar_exact(f['correct'], jev))})"
        vs_g = f"{signed_pts(paired_bootstrap(f['correct'], g38)['diff'])} ({pval(mcnemar_exact(f['correct'], g38))})"
        body.append(f"{name} & {pct(f['acc'])} & {pct(t['acc'])} & {f['ece']:.3f} & {f['usd_per_1k']:.2f} & "
                    f"{f['lat_mean']:.2f} & {vs_j} & {vs_g} \\\\")
        key = {J13: "jev", "perplexity/pplx-decider-v1.2": "pplx", "openai/gpt-6-luna-decisions": "luna",
               "liquid/d1": "liquid", "microsoft/microsoft-decision-1": "msft"}[model]
        num(key + "flatacc", pct(f["acc"]))
        num(key + "treeacc", pct(t["acc"]))
        num(key + "cost", f"{f['usd_per_1k']:.2f}")
        num(key + "lat", f"{f['lat_mean']:.2f}")
        num(key + "ece", f"{f['ece']:.3f}")
    pt = ok(load_test("perplexity/pplx-decider-v1.2:tree_v2"))
    num("pplxtreevsgdiff", signed_pts(paired_bootstrap(pt, g38)["diff"]))
    nump("pplxtreevsgp", mcnemar_exact(pt, g38))
    pf = ok(load_test("perplexity/pplx-decider-v1.2:flat"))
    num("pplxvsjevdiff", signed_pts(paired_bootstrap(pf, jev)["diff"]))
    nump("pplxvsjevp", mcnemar_exact(pf, jev))
    write("tab_decision_models.tex", "\n".join([
        r"\begin{table*}[t]", r"\centering\small\setlength{\tabcolsep}{5pt}", r"\begin{tabular}{lccccccc}", r"\toprule",
        r"Decision model & Flat & Tree v2 & ECE & \$ / 1k & Lat.\ (s) & "
        r"$\Delta$ Jev ($p$) & $\Delta$ Gemini 3.8 ($p$) \\", r"\midrule", *body, r"\bottomrule", r"\end{tabular}",
        r"\caption{Jev against the other decision models available through the same gateway, with Jev's frozen "
        r"questions and inputs, nothing tuned per model (test split). Flat, Tree v2: accuracy (\%). ECE and "
        r"latency for the flat question. $\Delta$: accuracy difference of the flat question from Jev and from "
        r"Gemini~3.8 Flash in points, with exact McNemar $p$. Models: Perplexity decider v1.2, OpenAI GPT-6-luna "
        r"decisions, Liquid d1, Microsoft decision-1. Gemini 3.8 Flash (thinking low) scores "
        rf"{NUM['gthreeeightacc']}\% at \${NUM['gthreeeightcost']} per 1k queries.}}",
        r"\label{tab:decision_models}", r"\end{table*}"]))


# --- Cascade --------------------------------------------------------------------------------

def table_cascade() -> None:
    expensive = load_test(f"{G38}:paper_llm_low")
    g_usd = 1000 * float(np.mean([r["cost_usd"] or 0 for r in expensive]))
    body = []
    for name, spec, key in [("Jev 1.13, flat", f"{J13}:flat", "flat"),
                            ("Jev 1.13, tree v2$^\\dagger$", f"{J13}:tree_v2", "tree"),
                            ("Jev 1.14, flat", f"{J14}:flat", "onefour")]:
        cheap = load_test(spec)
        st = summary_stats(cheap, expensive)
        num(f"casc{key}auroc", f"{st['auroc']:.3f}")
        rows = {r["f"]: r for r in curve(cheap, expensive)}
        body.append(rf"\multicolumn{{7}}{{l}}{{\emph{{Cheap stage: {name}}} (AUROC of confidence {st['auroc']:.2f})}} \\")
        for f in (0.0, 0.10, 0.25, 0.50):
            r = rows[f]
            v = r["vs_expensive"]
            body.append(f"\\quad {int(f * 100)}\\% & {pct(r['acc'])} & {pct(r['acc_random'])} & {signed_pts(v['diff'])} "
                        f"[{signed_pts(v['lo'])}, {signed_pts(v['hi'])}] & {pval(r['p_vs_expensive'])} & "
                        f"{100 * r['usd_per_1k'] / g_usd:.0f}\\% & {r['lat_mean']:.2f} \\\\")
            fk = {0.0: "zero", 0.10: "ten", 0.25: "tf", 0.50: "fifty"}[f]
            num(f"casc{key}{fk}acc", pct(r["acc"]))
            num(f"casc{key}{fk}rand", pct(r["acc_random"]))
            num(f"casc{key}{fk}cost", f"{100 * r['usd_per_1k'] / g_usd:.0f}")
            num(f"casc{key}{fk}diff", signed_pts(v["diff"]))
            num(f"casc{key}{fk}lo", signed_pts(v["lo"]))
            num(f"casc{key}{fk}hi", signed_pts(v["hi"]))
            nump(f"casc{key}{fk}p", r["p_vs_expensive"])
            num(f"casc{key}{fk}lat", f"{r['lat_mean']:.2f}")
        best = max(curve(cheap, expensive), key=lambda r: r["acc"])
        num(f"casc{key}bestacc", pct(best["acc"]))
        num(f"casc{key}bestf", f"{int(round(best['f'] * 100))}")
    pp = load_test("perplexity/pplx-decider-v1.2:flat")
    r = {x["f"]: x for x in curve(pp, expensive)}[0.25]
    num("cascpplxtfacc", pct(r["acc"]))
    num("cascpplxtfcost", f"{100 * r['usd_per_1k'] / g_usd:.0f}")
    write("tab_cascade.tex", "\n".join([
        r"\begin{table*}[t]", r"\centering\small", r"\begin{tabular}{lcccccc}", r"\toprule",
        r"$f$ & Acc. & Random & $\Delta$ vs LLM [95\% CI] & $p$ & Cost & Lat.\ (s) \\", r"\midrule", *body,
        r"\bottomrule", r"\end{tabular}",
        r"\caption{Confidence-gated cascade: the fraction $f$ of queries with the lowest Jev top probability goes to "
        rf"Gemini 3.8 Flash (thinking low; {NUM['gthreeeightacc']}\% alone). \emph{{Random}}: expected accuracy when the same "
        r"number of queries is escalated at random. Cost is relative to the LLM alone. Thresholds are label-free "
        r"quantiles, fixed before computing. $^\dagger$Revised on development data.}",
        r"\label{tab:cascade}", r"\end{table*}"]))


# --- Diagnostics ----------------------------------------------------------------------------

def _diag_load(model, method, pert=None):
    base = "tree" if method == "tree_v2" else method
    recs = read_jsonl(out_path(model, SPLIT, base, pert))
    if method == "tree_v2":
        recs = _derived(recs)["tree_v2"]
    return {r["id"]: r for r in recs}


def table_diagnostics() -> None:
    systems = [("Jev flat", J13, "flat", "jf"), ("Jev tree v2$^\\dagger$", J13, "tree_v2", "jt"),
               ("Gemini 3.8", G38, "paper_llm_low", "gm")]
    perts = [("rerun", "Rerun"), ("no_dates", "No dates"), ("dates_in_code", "Recency in code"),
             ("shuffle1", "Shuffle, seed 1"), ("shuffle2", "Shuffle, seed 2")]
    body = []
    for pk, pname in perts:
        cells = []
        for _, m, me, key in systems:
            o, p = _diag_load(m, me), _diag_load(m, me, pk)
            ids = sorted(set(o) & set(p))
            a = np.array([o[i]["pred"] == o[i]["label"] for i in ids])
            b = np.array([p[i]["pred"] == p[i]["label"] for i in ids])
            flips = np.array([o[i]["pred"] != p[i]["pred"] for i in ids])
            outd = [i for i in ids if o[i]["label"] == "outdated"]
            rec = np.mean([p[i]["pred"] == "outdated" for i in outd])
            d = paired_bootstrap(b, a)["diff"]
            cells.append(f"{signed_pts(d)} ({pval(mcnemar_exact(b, a))}) & {pct(flips.mean())} & {pct(rec)}")
            num(f"diag{key}{pk.replace('_', '').replace('1', 'one').replace('2', 'two')}flip", pct(flips.mean()))
            num(f"diag{key}{pk.replace('_', '').replace('1', 'one').replace('2', 'two')}rec", pct(rec))
            num(f"diag{key}{pk.replace('_', '').replace('1', 'one').replace('2', 'two')}diff", signed_pts(d))
            nump(f"diag{key}{pk.replace('_', '').replace('1', 'one').replace('2', 'two')}p", mcnemar_exact(b, a))
            if pk == "rerun":
                num(f"diag{key}origrec", pct(np.mean([o[i]["pred"] == "outdated" for i in outd])))
        body.append(f"{pname} & " + " & ".join(cells) + r" \\")
    # Pooled shuffle flips with CI, and Jev-vs-Gemini flip comparison.
    for _, m, me, key in systems:
        o = _diag_load(m, me)
        fl = np.concatenate([[o[i]["pred"] != _diag_load(m, me, s)[i]["pred"] for i in sorted(o)] for s in ("shuffle1", "shuffle2")])
        lo, hi = bootstrap_ci(fl.astype(float))
        num(f"diag{key}shuffleflip", pct(fl.mean()))
        num(f"diag{key}shufflelo", pct(lo))
        num(f"diag{key}shufflehi", pct(hi))
    for s in ("shuffle1", "shuffle2"):
        oj, pj = _diag_load(J13, "flat"), _diag_load(J13, "flat", s)
        og, pg = _diag_load(G38, "paper_llm_low"), _diag_load(G38, "paper_llm_low", s)
        ids = sorted(set(oj) & set(og))
        fj = np.array([oj[i]["pred"] != pj[i]["pred"] for i in ids])
        fg = np.array([og[i]["pred"] != pg[i]["pred"] for i in ids])
        nump(f"diagflipjevvsg{'one' if s.endswith('1') else 'two'}p", mcnemar_exact(fj, fg))
    head = " & ".join(rf"\multicolumn{{3}}{{c}}{{{n}}}" for n, *_ in systems)
    write("tab_diagnostics.tex", "\n".join([
        r"\begin{table*}[t]", r"\centering\footnotesize\setlength{\tabcolsep}{4pt}", r"\begin{tabular}{lccccccccc}", r"\toprule",
        f" & {head} \\\\", r"\cmidrule(lr){2-4}\cmidrule(lr){5-7}\cmidrule(lr){8-10}",
        "Perturbation & " + " & ".join([r"$\Delta$Acc ($p$) & Flip & Outd."] * 3) + r" \\", r"\midrule",
        *body, r"\midrule",
        "Original Outd.\\ recall & " + " & ".join(f"\\multicolumn{{3}}{{c}}{{{NUM['diag' + k + 'origrec']}}}" for *_, k in systems) + r" \\",
        r"\bottomrule", r"\end{tabular}",
        r"\caption{Diagnostics on the test split. Each perturbed run is compared with the same system's original run. "
        r"$\Delta$Acc: accuracy change in points (exact McNemar $p$). Flip: share of queries whose predicted type "
        r"changed (\%). Outd.: recall (\%) on the 55 \emph{Outdated} queries after the perturbation. The identical rerun is "
        r"the noise floor. $^\dagger$Revised on development data.}", r"\label{tab:diagnostics}", r"\end{table*}"]))


def table_plant() -> None:
    systems = [("Jev 1.13, flat", J13, "flat", "jf"), ("Jev 1.13, tree v2$^\\dagger$", J13, "tree_v2", "jt"),
               ("Gemini 3.8 Flash (low)", G38, "paper_llm_low", "gm")]
    body, det = [], {}
    for name, m, me, key in systems:
        o, p = _diag_load(m, me), _diag_load(m, me, "plant")
        ids = sorted(p)
        hit = np.array([p[i]["pred"] == "misinformation" for i in ids])
        fa = np.array([o[i]["pred"] == "misinformation" for i in ids])
        hc = np.array([p[i]["pred"] != "no_conflict" for i in ids])
        fc = np.array([o[i]["pred"] != "no_conflict" for i in ids])
        det[key] = (hit, fa)
        au = "--"
        if me != "paper_llm_low":
            sc = np.array([p[i]["probs"]["misinformation"] for i in ids] + [o[i]["probs"]["misinformation"] for i in ids])
            lab = np.array([True] * len(ids) + [False] * len(ids))
            au = f"{auroc(sc, lab):.2f}"
            num(f"plant{key}auroc", au)
        body.append(f"{name} & {pct(hit.mean())} & {pct(fa.mean())} & {hit.mean() - fa.mean():+.3f} & "
                    f"{pct(hc.mean())} / {pct(fc.mean())} & {au} \\\\")
        num(f"plant{key}hit", pct(hit.mean()))
        num(f"plant{key}fa", pct(fa.mean()))
        num(f"plant{key}youden", f"{hit.mean() - fa.mean():+.3f}")
        num("nplant", str(len(ids)))
    a, g = det["jf"], det["gm"]
    nump("planthitp", mcnemar_exact(a[0], g[0]))
    nump("plantfap", mcnemar_exact(a[1], g[1]))
    d = (a[0].astype(int) - a[1].astype(int)) - (g[0].astype(int) - g[1].astype(int))
    lo, hi = bootstrap_ci(d.astype(float))
    num("plantyoudendiff", f"{d.mean():+.3f}")
    num("plantyoudenlo", f"{lo:+.3f}".replace("-", "$-$"))
    num("plantyoudenhi", f"{hi:+.3f}")
    write("tab_plant.tex", "\n".join([
        r"\begin{table*}[t]", r"\centering\small", r"\begin{tabular}{lccccc}", r"\toprule",
        r"System & Hit & False al. & Youden & Any conflict & AUROC \\", r"\midrule", *body, r"\bottomrule", r"\end{tabular}",
        rf"\caption{{One planted false source in {NUM['nplant']} \emph{{No conflict}} test queries (expected label: "
        r"\emph{Misinformation}). Hit: planted copy labelled Misinformation. False al.: clean copy of the same query "
        r"labelled Misinformation. Youden = hit $-$ false alarm. Any conflict: planted / clean copy not labelled No "
        r"conflict. AUROC: P(Misinformation) separating planted from clean copies. $^\dagger$Revised on development data.}",
        r"\label{tab:plant}", r"\end{table*}"]))


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
    # Test: tree v1 sends opinion queries to Complementary; flat over-confidence.
    t1 = load_test(f"{J13}:tree")
    num("testopintocomp", str(sum(r["label"] == "conflicting_opinions" and r["pred"] == "complementary" for r in t1)))
    num("testnopin", str(sum(r["label"] == "conflicting_opinions" for r in t1)))
    fl = load_test(f"{J13}:flat")
    num("flatmeanconf", pct(float(np.mean([max(r["probs"].values()) for r in fl]))))
    # All 458 queries (the paper's scope) for the reproduction gap.
    for key, spec in [("allgtwofive", f"{G25}:paper_llm"), ("alljev", f"{J13}:flat")]:
        num(key, pct(float(ok(_load_system(spec, "all")).mean())))
    # Latency ranking over every model configuration run on the test split.
    configs = [f"{m}:{me}" for m in (J13, J14, "perplexity/pplx-decider-v1.2", "openai/gpt-6-luna-decisions",
                                     "liquid/d1", "microsoft/microsoft-decision-1") for me in ("flat", "tree")]
    configs += [f"{G25}:paper_llm", f"{G25}:paper_llm_thinking", f"{G38}:paper_llm_low", f"{G38}:paper_llm_thinking"]
    lat = {c: float(np.mean([r["latency_s"] for r in load_test(c)])) for c in configs}
    fastest_other = min(v for c, v in lat.items() if not c.startswith("typesafe-ai/"))
    num("nconfigs", str(len(configs)))
    num("fastestother", f"{fastest_other:.2f}")
    assert min(lat, key=lat.get).startswith(J13), "the text says Jev 1.13 is the fastest"
    # Version and decision-model numbers quoted in prose.
    for key, spec in [("onefourcascfifty", f"{J14}:tree_v2")]:
        r = {x["f"]: x for x in curve(load_test(spec), load_test(f"{G38}:paper_llm_low"))}[0.5]
        num(key + "acc", pct(r["acc"]))
        nump(key + "p", r["p_vs_expensive"])
    # Lenient parsing: Gemini answers whose category is not in the requested JSON field.
    import re
    strict = re.compile(r'"category"\s*:\s*"?\s*([1-5])\b')
    gem = [r for m in (G25, G38) for p in sorted((ROOT / "runs" / m.replace("/", "__")).glob("*/*.jsonl"))
           for r in read_jsonl(p)]
    num("ngemini", f"{len(gem):,}")
    num("nlenient", str(sum(not strict.search(r["text"]) for r in gem)))
    j = summarise(load_test(f"{J13}:flat"), PRICE)
    num("cihalf", f"{100 * (j['acc_hi'] - j['acc_lo']) / 2:.1f}")
    num("medtokens", f"{int(np.median([r['usage']['inputTokens'] for r in load_test(f'{J13}:flat')])):,}")
    num("nmisitest", str(sum(r["label"] == "misinformation" for r in load_test(f"{J13}:flat"))))
    luna = load_test("openai/gpt-6-luna-decisions:flat")
    g = load_test(f"{G38}:paper_llm_low")
    st = summary_stats(luna, g)
    r = {x["f"]: x for x in curve(luna, g)}[0.25]
    num("lunaauroc", f"{st['auroc']:.2f}")
    num("lunacasctf", pct(r["acc"]))
    num("lunacasctfrand", pct(r["acc_random"]))


def prompt_files() -> None:
    """The exact prompt texts, for verbatim listings in the appendix."""
    from jevconflict.perturb import WRONG_ANSWER_PROMPT
    from jevconflict.prompts import FLAT_INSTRUCTIONS, PAPER_PROMPT, TREE_QUESTIONS

    (OUT / "paper_prompt.txt").write_text(PAPER_PROMPT + "\n")
    (OUT / "flat_question.txt").write_text(
        "type: choice\ninstructions: " + FLAT_INSTRUCTIONS + "\noptions: the five category definitions of the prompt "
        "above, each with its example, keyed no_conflict, complementary, conflicting_opinions, outdated, misinformation\n")
    (OUT / "tree_questions.txt").write_text("".join(f"{k} (yes/no): {v}\n" for k, v in TREE_QUESTIONS.items()))
    (OUT / "wrong_answer_prompt.txt").write_text(WRONG_ANSWER_PROMPT + "\n")


def write_numbers() -> None:
    lines = ["% Generated by scripts/make_tables.py from the stored runs. Do not edit."]
    for k, v in sorted(NUM.items()):
        assert k.isalpha(), k  # LaTeX macro names: letters only
        lines.append(f"\\newcommand{{\\{k}}}{{{v}\\xspace}}")
    write("numbers.tex", "\n".join(lines))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    table_data()
    stats = table_main()
    numbers_main(stats)
    table_perclass(stats)
    table_decision_models()
    table_cascade()
    table_diagnostics()
    table_plant()
    extras()
    prompt_files()
    write_numbers()
    print(f"wrote {len(list(OUT.glob('*.tex')))} files and {len(NUM)} numbers to {OUT}")


if __name__ == "__main__":
    main()
