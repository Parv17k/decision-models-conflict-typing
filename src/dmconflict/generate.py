"""End-to-end experiment: answers conditioned on a conflict type, and the judges that score them.

Follows Cattan et al. (§3, §4, App. A; protocol in NOTES.md). `VANILLA_PROMPT` is their Figure 3
verbatim. For Pipeline and Oracle they "add a description of the conflict type to the Vanilla
prompt" without publishing the wording; `TYPE_DESCRIPTIONS` are their §2 definitions and expected
behaviours with citations and worked examples removed. Their judge prompts are not published either:
`behaviour_prompt` is rebuilt from their description (query, type description and expected
behaviour, adherent / non-adherent examples from their Table 3, candidate response; binary verdict).

One answer is generated per (query, type) and per query for Vanilla. A predictor's Pipeline answer
is the answer for the type it predicts, so every predictor that supplies the same type gets the same
answer.
"""

from __future__ import annotations

import json
import re

from .client import Chat, billed_cost
from .data import LABELS
from .prompts import numbered_results

GENERATOR = "google/gemini-2.5-flash"
JUDGE = "google/gemini-2.5-flash"
THINKING_OFF = {"providerOptions": {"google": {"thinkingConfig": {"thinkingBudget": 0}}}}
VANILLA = "vanilla"
CONDITIONS = [VANILLA, *LABELS]

VANILLA_PROMPT = """Write a high-quality and concise answer for the given question using only the provided search results.
For each sentence, cite the corresponding sources using [1][2][3].

QUERY: {query}
SEARCH RESULTS: {search_results}"""

TYPE_PROMPT = """Write a high-quality and concise answer for the given question using only the provided search results.
For each sentence, cite the corresponding sources using [1][2][3].

TYPE OF KNOWLEDGE CONFLICT IN THE SEARCH RESULTS: {description}

QUERY: {query}
SEARCH RESULTS: {search_results}"""

TYPE_DESCRIPTIONS = {
    "no_conflict": (
        "No conflict. The retrieved documents provide answers to the query that are equivalent or nearly "
        "equivalent, referring to the same real-world entity, fact, or concept. Minor variations, such as "
        "differences in surface presentation or level of granularity, do not constitute a conflict. Additionally, "
        "retrieved documents that are topically related to the query but do not directly answer it are not "
        "considered sources of conflict. The expected behavior for this category is to provide a clear and direct "
        "answer without introducing alternative viewpoints or uncertainty."),
    "complementary": (
        "Complementary information. The retrieved documents provide answers to the query that refer to different "
        "real-world concepts but are mutually compatible, meaning that a single person can reasonably agree with all "
        "of them simultaneously. This can happen when there are multiple correct answers to the same query or when "
        "the query is underspecified and can be answered with multiple complementary perspectives. The expected "
        "behavior for this category is to consolidate and reconcile the different partial answers provided by the "
        "retrieved documents, without framing the response as a debate."),
    "conflicting_opinions": (
        "Conflicting opinions or research outcomes. The retrieved documents provide answers to the query that are "
        "not mutually compatible. This category includes subjective queries that elicit conflicting opinions, "
        "queries with contradictory research findings, lack of historical consensus, etc., where the retrieved "
        "sources disagree and argue towards a specific side. The expected behavior for this category is to "
        "explicitly reflect the debate between the retrieved sources and to neutrally summarize the different "
        "viewpoints."),
    "outdated": (
        "Conflict due to outdated information. The retrieved documents provide answers to the query that are not "
        "mutually compatible, but the conflict stems from temporal discrepancies: some sources reflect outdated "
        "information, while others provide more recent updates. The expected behavior is to prioritize the "
        "up-to-date information, while optionally acknowledging the presence of outdated sources."),
    "misinformation": (
        "Conflict due to misinformation. The retrieved documents provide answers that are not mutually compatible, "
        "where at least one source contains information that is likely false, misleading, or inaccurate. The "
        "expected behavior for this category is to disregard inaccurate sources and to provide a response grounded "
        "in reliable and verified information."),
}

# (query, response, adheres, reason). From Cattan et al. Table 3, except No conflict, which has no
# published pair: ours, built around their Titanic example (Table 1).
JUDGE_EXAMPLES = {
    "no_conflict": [
        ("When did the Titanic set sail?",
         "Sources differ on when the Titanic set sail: some give 10 April 1912 [1][2], while another mentions "
         "11 April 1912 [3].", False,
         "The response presents a related detail (the anchoring in Queenstown on 11 April) as a disagreement and "
         "introduces uncertainty, although the sources agree."),
        ("When did the Titanic set sail?",
         "The Titanic set sail from Southampton on its maiden voyage on 10 April 1912 [1][2].", True,
         "The response gives a clear and direct answer."),
    ],
    "complementary": [
        ("Who has the biggest airport?",
         "The King Fahd International Airport in Saudi Arabia is the largest airport in the world by land area "
         "[1][6][7]. It spans nearly 300 square miles, an area comparable to the size of New York City's five "
         "boroughs combined [6].", False,
         "The response gives only one perspective, the largest airport by land area."),
        ("Who has the biggest airport?",
         "The world's largest airport can be defined in several ways, including by land area, passenger volume, or "
         "flight volume [6]. King Fahd International Airport in Saudi Arabia is the largest airport by total area "
         "[1]. In terms of passenger traffic, Hartsfield-Jackson Atlanta International Airport in the United States "
         "is the busiest airport in the world [4, 5].", True,
         "The response presents several aspects of what is considered a big airport, by land area and by passenger "
         "volume."),
    ],
    "conflicting_opinions": [
        ("Where did the style hot dog originated?",
         "The Chicago-style hot dog originated during the Great Depression in the 1930s in Chicago [1]. It was "
         "created to provide a hearty and affordable meal, with a nickel buying a hot dog loaded with condiments "
         "[1].", False,
         "The response only gives the origin of one specific hot dog (Chicago-style)."),
        ("Where did the style hot dog originated?",
         "The exact origin of the hot dog is not definitively clear, making it a subject of some debate among "
         "historians [6]. Two European cities, Frankfurt, Germany, and Vienna, Austria, both claim to be the "
         "birthplace of the sausage that served as the precursor to the hot dog [7]. The Chicago-style hot dog, with "
         "its specific set of toppings, emerged later, during the Great Depression in the 1930s [1].", True,
         "The response presents the debate around the origin of the hot dog."),
    ],
    "outdated": [
        ("How many people have been on the International Space Station?",
         "As of May 2022, 258 individuals from 20 countries have visited the International Space Station (ISS) [5]. "
         "Other sources state over 260 individuals from 20 countries and five International Partners have visited "
         "the station [7].", False,
         "The response presents the figures as differing views, whereas source [5] is outdated."),
        ("How many people have been on the International Space Station?",
         "As of March 2024, 279 individuals from 22 countries have visited the International Space Station [2]. "
         "Older figures indicate that as of May 2022, 258 people from 20 countries had visited the station [5], and "
         "as of September 12, 2021, 244 people had made 403 spaceflights to the ISS [3].", True,
         "The response clearly answers with the most recent figure and acknowledges older figures from other "
         "sources."),
    ],
    "misinformation": [
        ("When did season 5 of prison break come out?",
         "Season 5 of Prison Break premiered on April 4, 2017, on Fox [3]. The season was released on May 30, 2017 "
         "[4].", False,
         "The response tries to reconcile the sources, although source [4] is incorrect."),
        ("When did season 5 of prison break come out?",
         "Season 5 of Prison Break premiered on April 4, 2017 [2][3]. The first episode aired on this date [2].", True,
         "The response provides a clear and coherent answer to the question."),
    ],
}


def generation_prompt(row: dict, cond: str) -> str:
    results = "\n" + numbered_results(row)
    if cond == VANILLA:
        return VANILLA_PROMPT.replace("{query}", row["question"]).replace("{search_results}", results)
    return (TYPE_PROMPT.replace("{description}", TYPE_DESCRIPTIONS[cond]).replace("{query}", row["question"])
            .replace("{search_results}", results))


def behaviour_prompt(row: dict, response: str) -> str:
    """Judge prompt for the query's gold type."""
    examples = "\n\n".join(
        f"Query: {q}\nResponse: {r}\nVerdict: {'follows' if ok else 'does not follow'} the expected behavior. "
        f"Reason: {why}" for q, r, ok, why in JUDGE_EXAMPLES[row["label"]])
    return f"""You are evaluating whether a response to a search query follows the expected behavior for the type of knowledge conflict among the query's search results.

CONFLICT TYPE: {TYPE_DESCRIPTIONS[row["label"]]}

EXAMPLES:

{examples}

RESPONSE TO EVALUATE:
Query: {row["question"]}
Response: {response}

Does the response follow the expected behavior for this conflict type? Judge how the response handles the sources, as the expected behavior describes; do not judge its length or writing quality.
Reply with a JSON object: {{"explanation": "<one or two sentences>", "adheres": true or false}}"""


def recall_prompt(row: dict, response: str) -> str:
    return f"""You are checking whether a response contains the correct answer to a question.

QUESTION: {row["question"]}
CORRECT ANSWER: {row["answer"]}
RESPONSE: {response}

Does the response state the correct answer? Count paraphrases, equivalent formats and answers with more detail as correct; the response may also mention other information.
Reply with a JSON object: {{"explanation": "<one sentence>", "includes_answer": true or false}}"""


def parse_verdict(text: str, field: str) -> bool | None:
    """The boolean `field` of the judge's JSON; None if absent. The last statement wins."""
    hits = re.findall(rf'"?{field}"?\s*:\s*(true|false)', text, flags=re.IGNORECASE)
    return hits[-1].lower() == "true" if hits else None


def generate(chat: Chat, row: dict, cond: str) -> dict:
    data = chat.complete(generation_prompt(row, cond))
    return {"id": row["id"], "label": row["label"], "cond": cond, "text": Chat.text(data),
            "usage": data.get("usage"), "cost_usd": billed_cost(data), "latency_s": data.get("_latency_s"),
            "cached": data.get("_cached")}


def judge(chat: Chat, row: dict, answer: dict, kind: str) -> dict:
    prompt, field = ((behaviour_prompt, "adheres") if kind == "behaviour" else (recall_prompt, "includes_answer"))
    data = chat.complete(prompt(row, answer["text"]))
    text = Chat.text(data)
    return {"id": row["id"], "label": row["label"], "cond": answer["cond"], "kind": kind,
            "verdict": parse_verdict(text, field), "text": text, "cost_usd": billed_cost(data),
            "cached": data.get("_cached")}


def has_gold_answer(row: dict) -> bool:
    """Answer recall applies to No conflict, Outdated and Misinformation (Cattan et al. §3)."""
    return row["label"] in ("no_conflict", "outdated", "misinformation") and bool(row["answer"])


def to_json(rec: dict) -> str:
    return json.dumps(rec, ensure_ascii=False)
