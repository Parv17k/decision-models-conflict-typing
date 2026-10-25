"""Ways of getting a conflict type for one query.

Decision model (Jev):
- `flat`: one choice question whose options are the five categories (direct classification).
- `tree`: five yes/no questions in one request, combined in code into a distribution over the
  same five categories. `tree_hard` (same tree, fixed thresholds) and `tree_v2` (the same answers
  combined in a revised order) need no extra calls, so they are computed offline from the tree's
  stored probabilities.

Generative model (the paper's baseline):
- `paper_llm`: the paper's prompt, verbatim, answered as JSON. It gives a hard label only.
"""

from __future__ import annotations

import re

from .client import Chat, Gateway, billed_cost
from .data import LABELS
from .prompts import FLAT_QUESTION, PAPER_NUMBER, paper_prompt, state, tree_questions

CAUSES = ["conflicting_opinions", "outdated", "misinformation"]
CAUSE_QUESTION = {"conflicting_opinions": "opinion", "outdated": "outdated", "misinformation": "misinformation"}
LABEL_OF_NUMBER = {n: k for k, n in PAPER_NUMBER.items()}
UNPARSED = "unparsed"


def _boolean_prob(answer: dict) -> float:
    return float(answer["noul"] if "noul" in answer else answer["probability"])


def combine_tree(p: dict[str, float]) -> dict[str, float]:
    """P(no conflict) = 1 - P(differ); P(complementary) = P(differ) P(compatible); the remaining
    mass, P(differ) (1 - P(compatible)), is split over the three causes in proportion to their
    yes-probabilities (evenly if all three are zero). The result sums to 1."""
    d, c = p["differ"], p["compatible"]
    out = {"no_conflict": 1 - d, "complementary": d * c}
    cause = {k: p[CAUSE_QUESTION[k]] for k in CAUSES}
    total = sum(cause.values())
    for k in CAUSES:
        out[k] = d * (1 - c) * (cause[k] / total if total > 0 else 1 / len(CAUSES))
    return {k: out[k] for k in LABELS}


def combine_tree_v2(p: dict[str, float]) -> dict[str, float]:
    """Revised from development data (52 queries; see NOTES.md): ask `opinion` before
    `compatible`, because Jev answered `compatible` yes for opinion topics (mean 0.69); and make
    misinformation the factual conflict not explained by time, because the `misinformation`
    question said yes for every class (mean 0.53-0.79). Same five answers, different tree."""
    d, o, c, t = p["differ"], p["opinion"], p["compatible"], p["outdated"]
    factual = d * (1 - o) * (1 - c)
    out = {"no_conflict": 1 - d, "conflicting_opinions": d * o, "complementary": d * (1 - o) * c,
           "outdated": factual * t, "misinformation": factual * (1 - t)}
    return {k: out[k] for k in LABELS}


def tree_hard(p: dict[str, float], t: float = 0.5) -> str:
    if p["differ"] < t:
        return "no_conflict"
    if p["compatible"] >= t:
        return "complementary"
    return max(CAUSES, key=lambda k: p[CAUSE_QUESTION[k]])


def _record(row: dict, method: str, probs: dict, data: dict, pred: str | None = None, **extra) -> dict:
    return {"id": row["id"], "label": row["label"], "method": method,
            "pred": pred or max(LABELS, key=lambda k: probs[k]), "probs": probs,
            "usage": data.get("usage"), "cost_usd": billed_cost(data),
            "latency_s": data.get("_latency_s"), "cached": data.get("_cached"), **extra}


def flat(gw: Gateway, row: dict) -> dict:
    data = gw.evaluate(state(row), {"conflict_type": FLAT_QUESTION})
    raw = data["answers"]["conflict_type"]["probabilities"]
    probs = {k: float(raw.get(k, 0.0)) for k in LABELS}
    # Returned probabilities are rounded to two decimals; renormalise so they sum to 1.
    total = sum(probs.values())
    probs = {k: v / total for k, v in probs.items()} if total > 0 else {k: 1 / len(LABELS) for k in LABELS}
    return _record(row, "flat", probs, data, raw=raw)


def tree(gw: Gateway, row: dict) -> dict:
    data = gw.evaluate(state(row), tree_questions())
    raw = {k: _boolean_prob(a) for k, a in data["answers"].items()}
    return _record(row, "tree", combine_tree(raw), data, raw=raw)


def parse_category(text: str) -> str:
    """The stated category number; UNPARSED if absent or out of range.

    Lenient on purpose, so the baseline is not penalised for format: besides the requested JSON
    field it accepts `category: 4`, `**Category:** 4` and `\\boxed{4}`, which thinking mode
    sometimes writes instead. The last statement in the answer wins."""
    hits = re.findall(r'"?\bcategory\b"?\s*(?:\*\*)?\s*:\s*(?:\*\*)?\s*"?\s*([1-5])\b|\\boxed\{\s*([1-5])\s*\}',
                      text, flags=re.IGNORECASE)
    if not hits:
        return UNPARSED
    a, b = hits[-1]
    return LABEL_OF_NUMBER[int(a or b)]


def paper_llm(chat: Chat, row: dict) -> dict:
    data = chat.complete(paper_prompt(row))
    text = Chat.text(data)
    pred = parse_category(text)
    # A hard label: no probabilities, so calibration metrics are not defined for this method.
    probs = {k: float(k == pred) for k in LABELS}
    return _record(row, "paper_llm", probs, data, pred=pred, hard=True, text=text)


def _thinking(config: dict) -> dict:
    return {"providerOptions": {"google": {"thinkingConfig": config}}}


# name -> (function, kind of client, default model, extra chat request fields)
METHODS = {
    "flat": (flat, "decision", "typesafe-ai/jev-1.13.0", None),
    "tree": (tree, "decision", "typesafe-ai/jev-1.13.0", None),
    # The paper lists "Gemini 2.5 Flash" and "... Thinking" separately, so the plain model runs
    # with thinking off (budget 0 disables it on 2.5; Gemini 3.x still thinks at budget 0).
    "paper_llm": (paper_llm, "chat", "google/gemini-2.5-flash", _thinking({"thinkingBudget": 0})),
    # The provider's default thinking, for any Gemini.
    "paper_llm_thinking": (paper_llm, "chat", "google/gemini-2.5-flash", {}),
    # The lowest thinking level Gemini 3.x accepts ("minimal" is rejected by 3.8 Flash).
    "paper_llm_low": (paper_llm, "chat", "google/gemini-3.8-flash", _thinking({"thinkingLevel": "low"})),
}
