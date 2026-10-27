"""Inputs and questions sent to the models.

`PAPER_PROMPT` is the conflict-type prompt of Cattan et al. copied verbatim from the arXiv
source (`prompts/conflict_type_prediction.tex`, v2); only the LaTeX bold markers are removed. It
is used unchanged for the LLM baseline. The flat decision-model question carries the same instructions,
definitions and examples, word for word (checked by tests/test_core.py); only the output part
differs, because a decision model returns probabilities instead of JSON.

Each search result is the paper's concatenation of URL, title, Google snippet, publication date
(if available) and the 512-token segment (§5.1), in the dataset's order.
"""

from __future__ import annotations

PAPER_PROMPT = """You are tasked with analyzing the search results provided for a given query and classifying the type of knowledge conflict present (if any).
Consider the query and the search results carefully, then classify the conflict into *one* of the following categories, using the descriptions and examples provided below.

1. No Conflict: The search results refer to the same concept and are in agreement. Differences are superficial, such as variations in detail or granularity.
    *   *Example:*
        *   *Query:* What is the meaning of the name Apoorva?
        *   *Search Results:* Unique, Quite new, Not seen before
2.  Complementary Information: The question is underspecified or allows for multiple valid perspectives or answers that do not contradict each other. All provided answers can be considered correct.
    *   *Example:*
        *   *Query:* Is public transportation faster than driving in cities?
        *   *Search Results:* Depends on the city and situation (e.g., rush hour vs. off-peak), specific routes matter, availability of parking is relevant.
3.  Conflicting Opinions or Research Outcomes: The query addresses a subjective or contentious topic, leading to genuinely opposing viewpoints or contradictory research findings.
    *   *Example:*
        *   *Query:* Is online learning as effective as traditional classroom learning?
        *   *Search Results:* Some sources argue "yes," citing flexibility and accessibility. Others argue "no," emphasizing the importance of in-person interaction.
4.  Conflict Due to Outdated Information: The question has a verifiable factual answer, but the search results contain conflicting information due to changes over time.
    *   *Example:*
        *   *Query:* Do Tesla and X Corp. have the same CEO?
        *   *Search Results:* Some articles say yes (dated before the change), others say no (dated after the change).
5.  Conflict Due to Misinformation: The question has a verifiable factual answer, but some of the search results contain factually incorrect or misleading information.
    *   *Example:*
        *   *Query:* What is the capital of Israel?
        *   *Search Results:* One source correctly states Jerusalem, while another incorrectly states Tel Aviv.


Input:
*   QUERY: {query}
*   SEARCH RESULTS: {search_results}

Output:
Please provide your response as a JSON object with the following fields:
*   explanation: (String) A brief explanation of why you chose this category.
*   category: (Integer) The number (1-5) corresponding to the category of the knowledge conflict."""

# Category numbers in PAPER_PROMPT, in data.LABELS order.
PAPER_NUMBER = {"no_conflict": 1, "complementary": 2, "conflicting_opinions": 3, "outdated": 4, "misinformation": 5}

# --- Experiment 1: one choice question over the five categories ----------------------------

FLAT_INSTRUCTIONS = (
    "You are tasked with analyzing the search results provided for a given query and classifying "
    "the type of knowledge conflict present (if any).\nConsider the query and the search results "
    "carefully, then classify the conflict into *one* of the following categories, using the "
    "descriptions and examples provided below."
)
CATEGORIES = {
    "no_conflict": (
        "No Conflict: The search results refer to the same concept and are in agreement. "
        "Differences are superficial, such as variations in detail or granularity. "
        "Example: Query: What is the meaning of the name Apoorva? "
        "Search Results: Unique, Quite new, Not seen before"
    ),
    "complementary": (
        "Complementary Information: The question is underspecified or allows for multiple valid "
        "perspectives or answers that do not contradict each other. All provided answers can be "
        "considered correct. Example: Query: Is public transportation faster than driving in cities? "
        "Search Results: Depends on the city and situation (e.g., rush hour vs. off-peak), specific "
        "routes matter, availability of parking is relevant."
    ),
    "conflicting_opinions": (
        "Conflicting Opinions or Research Outcomes: The query addresses a subjective or contentious "
        "topic, leading to genuinely opposing viewpoints or contradictory research findings. "
        "Example: Query: Is online learning as effective as traditional classroom learning? "
        "Search Results: Some sources argue \"yes,\" citing flexibility and accessibility. Others "
        "argue \"no,\" emphasizing the importance of in-person interaction."
    ),
    "outdated": (
        "Conflict Due to Outdated Information: The question has a verifiable factual answer, but "
        "the search results contain conflicting information due to changes over time. "
        "Example: Query: Do Tesla and X Corp. have the same CEO? "
        "Search Results: Some articles say yes (dated before the change), others say no (dated "
        "after the change)."
    ),
    "misinformation": (
        "Conflict Due to Misinformation: The question has a verifiable factual answer, but some of "
        "the search results contain factually incorrect or misleading information. "
        "Example: Query: What is the capital of Israel? "
        "Search Results: One source correctly states Jerusalem, while another incorrectly states "
        "Tel Aviv."
    ),
}
FLAT_QUESTION = {"type": "choice", "instructions": FLAT_INSTRUCTIONS, "criteria": CATEGORIES}

# --- Experiment 2: the taxonomy as yes/no questions, all asked in one request ---------------
# `differ` separates No conflict from the rest, `compatible` separates Complementary from real
# conflicts, and the last three name the cause of an incompatible conflict. methods.combine_tree
# turns the five probabilities into one distribution over the categories.

TREE_QUESTIONS = {
    "differ": (
        "Beyond superficial differences in wording, detail or granularity, do the search results "
        "give different answers to the query?"
    ),
    "compatible": (
        "Could all the different answers in the search results be correct at the same time, for "
        "example because the query is underspecified or allows several valid answers?"
    ),
    "opinion": (
        "Is the query a subjective or contentious topic on which the search results present "
        "opposing viewpoints or contradictory research findings?"
    ),
    "outdated": (
        "Does the query have a verifiable factual answer on which the search results disagree "
        "because the answer changed over time, so some results are outdated?"
    ),
    "misinformation": (
        "Does the query have a verifiable factual answer on which some of the search results are "
        "factually incorrect or misleading?"
    ),
}


def tree_questions() -> dict[str, dict]:
    # The gateway calls TypeSafe's `noul` type `boolean`.
    return {k: {"type": "boolean", "instructions": v} for k, v in TREE_QUESTIONS.items()}


def format_result(r: dict) -> str:
    parts = [f"URL: {r.get('url', '')}", f"Title: {r.get('title', '')}", f"Snippet: {r.get('snippet', '')}"]
    if (date := r.get("date")) and date != "NA":
        parts.append(f"Date: {date}")
    # Only the dates-in-code diagnostic sets this (perturb.dates_in_code).
    if recency := r.get("recency"):
        parts.append(f"Recency: {recency}")
    if text := r.get("short_text"):
        parts.append(f"Text: {text}")
    return "\n".join(parts)


def state(row: dict) -> dict:
    """Decision-model input: results keep the dataset's order and are numbered from 1."""
    return {"query": row["question"],
            **{f"result_{i + 1}": format_result(r) for i, r in enumerate(row["results"])}}


def numbered_results(row: dict) -> str:
    """The results numbered [1], [2], ... as in the paper's generation prompts."""
    return "\n\n".join(f"[{i + 1}]\n{format_result(r)}" for i, r in enumerate(row["results"]))


def text_state(row: dict) -> dict:
    """The same content as `state`, as one `text` field, for decision models whose schema requires it."""
    return {"text": f"Query: {row['question']}\n\n{numbered_results(row)}"}


def paper_prompt(row: dict) -> str:
    """LLM input: the same results, numbered [1], [2], ... as in the paper's generation prompts."""
    return PAPER_PROMPT.replace("{query}", row["question"]).replace("{search_results}", "\n" + numbered_results(row))
