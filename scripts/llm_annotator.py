"""Label the blind judge-validation sheet with an LLM given the human annotators' instructions.

The LLM is a third judge, not a third annotator: its sheet is compared with the human labels and is
never pooled with them. It sees exactly what the humans saw (human_eval/README.md and the blind
sheet), one item at a time.

    .venv/bin/python scripts/llm_annotator.py --model anthropic/claude-sonnet-5.5
"""

from __future__ import annotations

import argparse
import csv
import json
from concurrent.futures import ThreadPoolExecutor

import numpy as np

from dmconflict.client import ROOT, Cache, Chat, billed_cost
from dmconflict.endtoend import HUMAN, _kappa
from dmconflict.generate import parse_verdict
from dmconflict.run import RUNS

COLUMNS = ["item", "query", "conflict_type_and_expected_behaviour", "response", "follows (1/0)", "notes"]


def instructions() -> str:
    readme = (HUMAN / "README.md").read_text()
    start = readme.index("You do not see the search results")
    return readme[start:readme.index("## After labelling")].strip()


def prompt(row: dict) -> str:
    return f"""You are annotating answers for a study of how answers handle conflicting search results. For the item below, read the query, the conflict type and expected behaviour, and the response, and decide whether the response follows the expected behaviour for that conflict type.

{instructions()}

ITEM
Query: {row["query"]}
Conflict type and expected behaviour: {row["conflict_type_and_expected_behaviour"]}
Response: {row["response"]}

Reply with a JSON object: {{"note": "<one sentence>", "follows": true or false}}"""


def label(chat: Chat, row: dict) -> dict:
    data = chat.complete(prompt(row))
    text = Chat.text(data)
    try:
        note = json.loads(text[text.index("{"):text.rindex("}") + 1]).get("note", "")
    except ValueError:
        note = ""
    return {**row, "follows (1/0)": {True: "1", False: "0", None: ""}[parse_verdict(text, "follows")],
            "notes": note, "_cost": billed_cost(data) or 0.0}


def read(path) -> dict[int, int]:
    return {int(r["item"]): int(r["follows (1/0)"]) for r in csv.DictReader(open(path, encoding="utf-8-sig"))
            if r["follows (1/0)"].strip() in ("0", "1")}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="anthropic/claude-sonnet-5.5")
    ap.add_argument("--humans", nargs="+", default=[str(HUMAN / "behaviour_sample_1.csv"),
                                                     str(HUMAN / "behaviour_sample_2.csv")])
    args = ap.parse_args()
    rows = list(csv.DictReader(open(HUMAN / "behaviour_sample.csv", encoding="utf-8-sig")))
    chat = Chat(args.model, Cache(RUNS / "api_cache.sqlite"))
    with ThreadPoolExecutor(8) as pool:
        out = list(pool.map(lambda r: label(chat, r), rows))
    chat.close()
    path = HUMAN / f"behaviour_sample_llm_{args.model.split('/')[-1]}.csv"
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, COLUMNS, extrasaction="ignore")
        w.writeheader()
        w.writerows(out)
    print(f"wrote {path.relative_to(ROOT)}; unparsed {sum(not r['follows (1/0)'] for r in out)}, "
          f"cost ${sum(r['_cost'] for r in out):.3f}")

    llm = read(path)
    humans = [read(p) for p in args.humans]
    items = sorted(set(llm).intersection(*humans))
    j = np.array([llm[i] for i in items])
    for p, h in zip(args.humans, humans):
        a = np.array([h[i] for i in items])
        print(f"  vs {p.split('/')[-1]:<26} accuracy {np.mean(a == j):.3f}  kappa {_kappa(a, j):.3f}  "
              f"follows: human {a.mean():.2f}, LLM {j.mean():.2f}")
    if len(humans) == 2:
        a, b = (np.array([h[i] for i in items]) for h in humans)
        agreed = a == b
        print(f"  vs both, where they agree (n={agreed.sum()})  accuracy {np.mean(a[agreed] == j[agreed]):.3f}  "
              f"kappa {_kappa(a[agreed], j[agreed]):.3f}")


if __name__ == "__main__":
    main()
