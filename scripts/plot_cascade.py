"""Paper figure: accuracy vs cost for every decision model alone, as a cascade stage, and the LLMs alone.

Reads the stored runs (no API calls) and writes figures/cascade_cost_accuracy.{pdf,png} and the paper's
copy, paper/figures/cascade_cost_accuracy.pdf.
Static print figure: white surface, no hover layer, no in-figure title (the LaTeX caption carries it),
drawn at its printed size (0.78 of the 16 cm text width) in the paper's serif face with embedded TrueType
fonts. The numbers are in runs/cascade_test.md and runs/comparison_test.md. Palette: the first three categorical slots, validated all-pairs
(scripts/validate_palette.js, light); aqua is below 3:1 on the surface, so every aqua point is
direct-labelled and drawn with its own marker shape.

    .venv/bin/python scripts/plot_cascade.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FixedLocator, FuncFormatter, NullLocator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dmconflict.cascade import curve  # noqa: E402
from dmconflict.run import DECISION_MODELS, _load_system  # noqa: E402

SURFACE, INK, INK_2, MUTED, GRID, AXIS = "#ffffff", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
SPLIT = "test"
GRID_DARK = "#b9b8ae"
FREE_X = 0.022
EXPENSIVE = "google/gemini-3.8-flash:paper_llm_low"


def usd_per_1k(recs):
    return 1000 * float(np.mean([r["cost_usd"] or 0.0 for r in recs]))


def acc(recs):
    return float(np.mean([r["pred"] == r["label"] for r in recs]))


def main() -> None:
    plt.rcParams.update({"font.family": "serif", "font.serif": ["Times New Roman", "Times", "STIXGeneral"],
                         "mathtext.fontset": "stix", "pdf.fonttype": 42, "ps.fonttype": 42,
                         "font.size": 8, "axes.edgecolor": AXIS, "axes.labelcolor": INK,
                         "xtick.color": INK_2, "ytick.color": INK_2, "text.color": INK})
    fig, ax = plt.subplots(figsize=(4.9, 2.9), dpi=300)
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)

    expensive = _load_system(EXPENSIVE, SPLIT)
    # Every decision model alone (flat question) and as the cheap stage at 25% escalated, joined by a thin line.
    for i, model in enumerate(DECISION_MODELS):
        cheap = _load_system(f"{model}:flat", SPLIT)
        rows = {r["f"]: r for r in curve(cheap, expensive)}
        a, c = rows[0.0], rows[0.25]
        x0 = a["usd_per_1k"] or FREE_X   # billed $0 cannot sit on a log axis: drawn at the "free" tick
        ax.plot([x0, c["usd_per_1k"]], [a["acc"], c["acc"]], color=GRID_DARK, lw=0.8, zorder=2)
        ax.scatter(x0, a["acc"], s=26, color=BLUE, edgecolors=SURFACE, linewidths=1.2, zorder=4,
                   label="Decision model alone (flat question)" if i == 0 else None)
        ax.scatter(c["usd_per_1k"], c["acc"], s=26, color=ORANGE, edgecolors=SURFACE, linewidths=1.2, zorder=4,
                   label="With 25% sent to Gemini 3.8 Flash" if i == 0 else None)

    alone = [("google/gemini-3.8-flash:paper_llm_low", "Gemini 3.8 Flash\n(thinking low)", (6, 4), "left"),
             ("google/gemini-3.8-flash:paper_llm_thinking", "Gemini 3.8 Flash\n(default thinking)", (6, -2), "left"),
             ("google/gemini-2.5-flash:paper_llm", "Gemini 2.5 Flash, thinking off\n(the paper's setup)", (6, -9), "left"),
             ("google/gemini-2.5-flash:paper_llm_thinking", "Gemini 2.5 Flash\n(thinking on)", (-8, -4), "right")]
    for i, (spec, label, off, ha) in enumerate(alone):
        recs = _load_system(spec, SPLIT)
        ax.scatter(usd_per_1k(recs), acc(recs), s=30, marker="D", color=AQUA, edgecolors=SURFACE, linewidths=1.2,
                   zorder=4, label="LLM alone" if i == 0 else None)
        ax.annotate(label, (usd_per_1k(recs), acc(recs)), xytext=off, textcoords="offset points",
                    ha=ha, va="center", fontsize=7, color=INK_2, zorder=5,
                    bbox=dict(boxstyle="square,pad=0.1", facecolor=SURFACE, edgecolor="none"))

    ax.set_xscale("log")
    ticks = [FREE_X, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]
    ax.xaxis.set_major_locator(FixedLocator(ticks))
    ax.xaxis.set_minor_locator(NullLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: "free" if v == FREE_X else f"${v:g}"))
    ax.set_xlim(0.018, 12)
    ax.axvline(FREE_X, color=GRID, lw=0.8, ls=(0, (2, 2)), zorder=1)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0%}"))
    ax.set_xlabel("Cost per 1,000 queries (USD, billed, log scale)")
    ax.set_ylabel("Conflict-type accuracy (5 classes)")
    ax.grid(True, axis="both", color=GRID, lw=0.8)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(length=0, pad=4)
    leg = ax.legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncol=3, frameon=False, fontsize=7,
                    handlelength=1.2, columnspacing=1.4, borderaxespad=0.2, labelcolor=INK_2)
    for t in leg.get_texts():
        t.set_color(INK_2)

    out = ROOT / "figures"
    out.mkdir(exist_ok=True)
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(out / f"cascade_cost_accuracy.{ext}", facecolor=SURFACE)
    # The LaTeX source reads its own copy (paper/figures), so the paper builds standalone.
    fig.savefig(ROOT / "paper" / "figures" / "cascade_cost_accuracy.pdf", facecolor=SURFACE)
    print(f"wrote {out}/cascade_cost_accuracy.pdf and .png, and paper/figures/cascade_cost_accuracy.pdf")


if __name__ == "__main__":
    main()
