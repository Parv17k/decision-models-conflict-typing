"""Search-result perturbations for the diagnostic experiments (protocol in NOTES.md).

Every perturbation is a pure, seeded function row -> row; the original row is never modified.
The question and the prompts stay the same, so any change in a system's answer comes from the
perturbed results.
"""

from __future__ import annotations

import copy
import random
import re
from datetime import datetime

# --- D1: dates ---------------------------------------------------------------------------

_FORMATS = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d", "%b %d, %Y"]


def parse_date(text: str | None) -> datetime | None:
    """Absolute dates only; relative ones ("4 days ago") and "NA" give None."""
    if not text or text == "NA":
        return None
    for fmt in _FORMATS:
        try:
            return datetime.strptime(text.strip(), fmt)
        except ValueError:
            pass
    return None


def no_dates(row: dict) -> dict:
    out = copy.deepcopy(row)
    for r in out["results"]:
        r["date"] = "NA"
    return out


def dates_in_code(row: dict) -> dict:
    """Adds a recency line to each result with a parseable date, if at least two parse."""
    out = copy.deepcopy(row)
    dated = [(i, d) for i, r in enumerate(out["results"]) if (d := parse_date(r.get("date")))]
    if len(dated) < 2:
        return out
    newest = max(d for _, d in dated)
    # Rank 1 = newest; equal dates share a rank.
    distinct = sorted({d for _, d in dated}, reverse=True)
    for i, d in dated:
        out["results"][i]["recency"] = (f"{distinct.index(d) + 1} of {len(distinct)} distinct dates among "
                                        f"{len(dated)} dated results (1 = newest); "
                                        f"{(newest - d).days} days older than the newest")
    return out


# --- D2: order -----------------------------------------------------------------------------

def shuffle(row: dict, seed: int) -> dict:
    out = copy.deepcopy(row)
    random.Random(f"{seed}-{row['id']}").shuffle(out["results"])
    return out


# --- D3: one planted false source ------------------------------------------------------------

WRONG_ANSWER_PROMPT = (
    "Question: {question}\nCorrect answer: {answer}\n\n"
    "Give one plausible but incorrect answer to the question, of the same type and format as the "
    "correct answer (a different name, place, number or date). Reply with the incorrect answer only."
)
_FIELDS = ("title", "snippet", "short_text")


_POLARITY = {"yes", "no"}


def _pattern(answer: str) -> re.Pattern:
    # Whole words only, so "1" doesn't match inside "2019" and "Paris" not inside "Parisian".
    return re.compile(r"(?<!\w)" + re.escape(answer) + r"(?!\w)", re.IGNORECASE)


def plant_candidates(row: dict, answer: str) -> list[int]:
    """Indices of results that state the gold answer verbatim (whole words, case-insensitive).
    Yes/no answers are excluded: flipping them is not an entity substitution."""
    if not answer or answer.lower() in _POLARITY:
        return []
    pat = _pattern(answer)
    return [i for i, r in enumerate(row["results"]) if any(pat.search(r.get(f) or "") for f in _FIELDS)]


def plant(row: dict, answer: str, wrong: str, seed: int = 0) -> dict | None:
    """Rewrites one result that states `answer` so it states `wrong` instead. The expected label
    becomes Misinformation. None if no result states the answer or the wrong answer is unusable."""
    cands = plant_candidates(row, answer)
    if not cands or not wrong or wrong.lower() == answer.lower():
        return None
    out = copy.deepcopy(row)
    i = random.Random(f"{seed}-{row['id']}").choice(cands)
    pat = _pattern(answer)
    for f in _FIELDS:
        if out["results"][i].get(f):
            out["results"][i][f] = pat.sub(wrong, out["results"][i][f])
    out["label"] = "misinformation"
    out["planted"] = {"result": i + 1, "answer": answer, "wrong": wrong}
    return out


PERTURBATIONS = ["rerun", "no_dates", "dates_in_code", "shuffle1", "shuffle2", "plant"]


def apply(name: str, row: dict, plants: dict | None = None) -> dict | None:
    """None means the query is not part of this perturbation's population."""
    if name == "rerun":
        return row
    if name == "no_dates":
        return no_dates(row)
    if name == "dates_in_code":
        return dates_in_code(row)
    if name.startswith("shuffle"):
        return shuffle(row, int(name[len("shuffle"):]))
    if name == "plant":
        p = (plants or {}).get(str(row["id"]))
        return plant(row, p["answer"], p["wrong"]) if p and row["label"] == "no_conflict" else None
    raise ValueError(name)
