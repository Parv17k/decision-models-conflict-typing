"""Paper figure: accuracy vs cost for the Jev → Gemini 3.8 Flash cascades and the LLMs alone.

Reads the stored runs (no API calls) and writes figures/cascade_cost_accuracy.{pdf,png}.
Static print figure: light surface only, no hover layer; the numbers are in runs/cascade_test.md
and runs/comparison_test.md. Palette: the first three categorical slots, validated all-pairs
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
from jevconflict.cascade import HEADLINE, curve  # noqa: E402
from jevconflict.run import _load_system  # noqa: E402

SURFACE, INK, INK_2, MUTED, GRID, AXIS = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
SPLIT = "test"
EXPENSIVE = "google/gemini-3.8-flash:paper_llm_low"


def usd_per_1k(recs):
    return 1000 * float(np.mean([r["cost_usd"] or 0.0 for r in recs]))


def acc(recs):
    return float(np.mean([r["pred"] == r["label"] for r in recs]))


def main() -> None:
    plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Arial", "DejaVu Sans"],
                         "font.size": 8.5, "axes.edgecolor": AXIS, "axes.labelcolor": INK_2,
                         "xtick.color": MUTED, "ytick.color": MUTED, "text.color": INK})
    fig, ax = plt.subplots(figsize=(6.4, 3.9), dpi=200)
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)

    expensive = _load_system(EXPENSIVE, SPLIT)
    cascades = [("typesafe-ai/jev-1.13.0:flat", "Jev flat → Gemini 3.8 Flash", BLUE),
                ("typesafe-ai/jev-1.13.0:tree_v2", "Jev tree v2 → Gemini 3.8 Flash", ORANGE)]
    for spec, label, color in cascades:
        rows = curve(_load_system(spec, SPLIT), expensive)
        x = [r["usd_per_1k"] for r in rows]
        y = [r["acc"] for r in rows]
        ax.plot(x, y, color=color, lw=2, solid_joinstyle="round", solid_capstyle="round", label=label, zorder=3)
        head = [r for r in rows if r["f"] in HEADLINE]
        ax.scatter([r["usd_per_1k"] for r in head], [r["acc"] for r in head], s=42, color=color,
                   edgecolors=SURFACE, linewidths=2, zorder=4)
        # Label the 25% point of the flat curve only: the headline the text cites.
        if spec.endswith(":flat"):
            r = next(r for r in rows if r["f"] == 0.25)
            ax.annotate(f"25% sent to Gemini\n{r['acc']:.3f} at {r['usd_per_1k'] / usd_per_1k(expensive):.0%} of its cost",
                        (r["usd_per_1k"], r["acc"]), xytext=(34, -52), textcoords="offset points",
                        ha="left", va="top", fontsize=7.5, color=INK_2,
                        arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8, shrinkA=0, shrinkB=4))
        start = rows[0]
        flat_curve = spec.endswith(":flat")
        ax.annotate("Jev flat alone" if flat_curve else "Jev tree v2 alone", (start["usd_per_1k"], start["acc"]),
                    xytext=(2, -11) if flat_curve else (2, 9), textcoords="offset points", ha="left",
                    va="center", fontsize=7.5, color=INK_2)

    alone = [("google/gemini-3.8-flash:paper_llm_low", "Gemini 3.8 Flash\n(thinking low)", (6, 4), "left"),
             ("google/gemini-3.8-flash:paper_llm_thinking", "Gemini 3.8 Flash\n(default thinking)", (6, -2), "left"),
             ("google/gemini-2.5-flash:paper_llm", "Gemini 2.5 Flash, thinking off\n(the paper's setup)", (-8, 6), "right"),
             ("google/gemini-2.5-flash:paper_llm_thinking", "Gemini 2.5 Flash\n(thinking on)", (-8, -4), "right")]
    for i, (spec, label, off, ha) in enumerate(alone):
        recs = _load_system(spec, SPLIT)
        ax.scatter(usd_per_1k(recs), acc(recs), s=46, marker="D", color=AQUA, edgecolors=SURFACE, linewidths=2,
                   zorder=4, label="LLM alone (paper's prompt)" if i == 0 else None)
        ax.annotate(label, (usd_per_1k(recs), acc(recs)), xytext=off, textcoords="offset points",
                    ha=ha, va="center", fontsize=7.5, color=INK_2)

    ax.set_xscale("log")
    ticks = [0.2, 0.5, 1, 2, 5]
    ax.xaxis.set_major_locator(FixedLocator(ticks))
    ax.xaxis.set_minor_locator(NullLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v:g}"))
    ax.set_xlim(0.15, 9)
    ax.set_ylim(0.555, 0.735)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0%}"))
    ax.set_xlabel("Cost per 1,000 queries (USD, billed, log scale)")
    ax.set_ylabel("Conflict-type accuracy (5 classes)")
    ax.grid(True, axis="both", color=GRID, lw=0.8)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(length=0, pad=4)
    leg = ax.legend(loc="upper left", frameon=False, fontsize=7.5, handlelength=1.6, labelcolor=INK_2)
    for t in leg.get_texts():
        t.set_color(INK_2)
    ax.set_title("Jev answers first; its least-confident queries go to Gemini 3.8 Flash",
                 loc="left", fontsize=9.5, color=INK, pad=10)
    ax.text(0, 1.005, "CONFLICTS test split, n = 406. Dots on the curves: 25% and 50% of queries sent to Gemini.",
            transform=ax.transAxes, fontsize=7.5, color=INK_2, va="bottom")

    out = ROOT / "figures"
    out.mkdir(exist_ok=True)
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(out / f"cascade_cost_accuracy.{ext}", facecolor=SURFACE)
    print(f"wrote {out}/cascade_cost_accuracy.pdf and .png")


if __name__ == "__main__":
    main()
