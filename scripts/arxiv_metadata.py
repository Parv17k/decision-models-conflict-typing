"""Prints the arXiv submission metadata, with the abstract as plain text (number macros expanded,
LaTeX markup removed), checked against arXiv's 1,920-character abstract limit.

    .venv/bin/python scripts/arxiv_metadata.py
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
AUTHORS = ["Parv Khatri", "Harshul Jain", "Mehak Kapoor", "Tanya Sah"]
REPO = "https://github.com/Parv17k/decision-models-conflict-typing"


def counts() -> tuple[int, int, int]:
    """Pages, figures and tables of the built preprint (the arXiv build's .log and .aux are deleted, so the
    numbers are read from paper/main_final.*, which has the same content and layout)."""
    log = (PAPER / "main_final.log").read_text(errors="ignore")
    aux = (PAPER / "main_final.aux").read_text(errors="ignore")
    pages = int(re.search(r"Output written on main_final.pdf \((\d+) pages", log).group(1))
    return pages, len(re.findall(r"\\newlabel\{fig:[^}]*\}\{\{", aux)), len(re.findall(r"\\newlabel\{tab:[^}]*\}\{\{", aux))


def macros() -> dict[str, str]:
    nums = (PAPER / "generated" / "numbers.tex").read_text()
    out = {k: v.replace("\\xspace", "") for k, v in re.findall(r"\\newcommand\{\\(\w+)\}\{(.*)\}$", nums, re.M)}
    out |= {"jev": "Jev", "conflicts": "CONFLICTS"}
    return out


def plain(tex: str) -> str:
    m = macros()
    tex = tex.replace(r"\citet{cattan2025dragged}", "Cattan et al. (2025)")
    tex = tex.replace(r"\releasenote", f" at {REPO}")   # the arXiv version links the code
    tex = re.sub(r"\\(\w+)(?![a-zA-Z])", lambda x: m.get(x.group(1), x.group(0)), tex)
    tex = re.sub(r"\\emph\{([^}]*)\}", r"\1", tex)
    for a, b in [("$\\times$", "x"), ("$p", "p"), ("$", ""), ("\\%", "%"), ("~", " "), ("\\ ", " "),
                 ("{<}", "<"), ("p=", "p = "), ("p<", "p < "), ("vs.\\", "vs.")]:
        tex = tex.replace(a, b)
    leftover = re.findall(r".{0,20}\\.{0,20}", tex)
    assert not leftover, f"unexpanded LaTeX left in abstract: {leftover}"
    return re.sub(r"\s+", " ", tex).strip()


def main() -> None:
    # The title is the \title{...} block, which ends before the first blank line.
    title = re.search(r"\\title\{(.*?)\}\s*\n\s*\n", (PAPER / "main.tex").read_text(), re.S).group(1)
    title = re.sub(r"\s+", " ", title.replace("\\\\", " ")).strip()
    abstract = plain((PAPER / "sections" / "abstract.tex").read_text())
    pages, figs, tabs = counts()
    assert len(abstract) <= 1920, f"abstract is {len(abstract)} characters; arXiv allows 1,920"
    print(f"Title:\n{title}\n")
    print(f"Authors (arXiv form, comma-separated, in order):\n{', '.join(AUTHORS)}\n")
    print(f"Abstract ({len(abstract)} of 1,920 characters):\n{abstract}\n")
    print("Primary category: cs.CL (Computation and Language)\nCross-list: cs.IR (Information Retrieval) only; a cs.AI cross-list draws extra moderation\n")
    print("Comments (suggested; edit before submitting):\n"
          f"{pages} pages, {figs} figures, {tabs} tables. Code, prompts and all model outputs: {REPO}\n")
    print("License (paper): choose at submission, e.g. CC BY 4.0 or the arXiv non-exclusive licence.\n"
          "License (code): Apache-2.0, in the repository's LICENSE file.")


if __name__ == "__main__":
    main()
