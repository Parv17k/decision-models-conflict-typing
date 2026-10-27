"""CONFLICTS loading, label names, and the frozen development/test split.

The dataset ships as one file with no splits. Prompt wording is chosen on a small stratified
development sample only; the remaining queries are the test set. The split is written to
`data/splits.json` the first time and read from there afterwards, so it never changes.
"""

from __future__ import annotations

import json
import random
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"

# Short keys used everywhere in code, in the order of the paper's taxonomy (Figure 2).
LABELS = ["no_conflict", "complementary", "conflicting_opinions", "outdated", "misinformation"]
LABEL_OF = {
    "No conflict": "no_conflict",
    "Complementary information": "complementary",
    "Conflicting opinions and research outcomes": "conflicting_opinions",
    "Conflict due to outdated information": "outdated",
    "Conflict due to misinformation": "misinformation",
}
# The paper merges these two when reporting behaviour ("both require selecting the correct response").
MERGED = {"outdated": "outdated_or_misinfo", "misinformation": "outdated_or_misinfo"}


def load(path: Path = DATA / "conflicts.jsonl") -> list[dict]:
    rows = []
    with open(path) as f:
        for i, line in enumerate(f):
            r = json.loads(line)
            # correct_answer is a single space for types without a gold answer.
            rows.append({"id": i, "source": r["source"], "question": r["question"],
                         "results": r["search_results"], "label": LABEL_OF[r["conflict_type"]],
                         "answer": r["correct_answer"].strip()})
    return rows


def make_split(rows: list[dict], dev_size: int = 50, seed: int = 13) -> dict[str, list[int]]:
    """Stratified by label; every label gets at least one development query."""
    rng = random.Random(seed)
    by_label: dict[str, list[int]] = {}
    for r in rows:
        by_label.setdefault(r["label"], []).append(r["id"])
    dev = []
    for ids in by_label.values():
        k = max(1, round(dev_size * len(ids) / len(rows)))
        dev += rng.sample(ids, k)
    dev = sorted(dev)
    return {"dev": dev, "test": sorted(set(r["id"] for r in rows) - set(dev))}


def split_ids(rows: list[dict], split: str, path: Path = DATA / "splits.json") -> list[int]:
    if not path.exists():
        path.write_text(json.dumps(make_split(rows), indent=1))
    splits = json.loads(path.read_text())
    return [r["id"] for r in rows] if split == "all" else splits[split]
