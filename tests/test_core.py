import numpy as np
import pytest

from dmconflict.data import LABEL_OF, LABELS, load, make_split
from dmconflict.methods import combine_tree, flat, tree, tree_hard
from dmconflict.metrics import accuracy, ece, macro_f1, mcnemar_exact, paired_bootstrap
from dmconflict.prompts import CATEGORIES, TREE_QUESTIONS, format_result, state

ROW = {"id": 0, "label": "outdated", "question": "who is the ceo of x",
       "results": [{"url": "u1", "title": "t1", "snippet": "s1", "date": "2024-01-02", "short_text": "body"},
                   {"url": "u2", "title": "t2", "snippet": "s2", "date": "NA", "short_text": ""}]}


def test_labels_cover_dataset_strings():
    assert set(LABEL_OF.values()) == set(LABELS) == set(CATEGORIES)


def test_state_omits_missing_date_and_text():
    s = state(ROW)
    assert list(s) == ["query", "result_1", "result_2"]
    assert "Date: 2024-01-02" in s["result_1"] and "Text: body" in s["result_1"]
    assert "Date" not in s["result_2"] and "Text" not in s["result_2"]
    assert format_result({}).startswith("URL: ")


def test_combine_tree_is_a_distribution():
    for p in [dict(differ=0.9, compatible=0.2, opinion=0.1, outdated=0.8, misinformation=0.1),
              dict(differ=0.5, compatible=0.5, opinion=0.0, outdated=0.0, misinformation=0.0)]:
        q = combine_tree(p)
        assert list(q) == LABELS and abs(sum(q.values()) - 1) < 1e-9 and min(q.values()) >= 0


def test_combine_tree_follows_the_branches():
    pick = lambda p: max(LABELS, key=combine_tree(p).get)
    assert pick(dict(differ=0.1, compatible=0.9, opinion=0.9, outdated=0.9, misinformation=0.9)) == "no_conflict"
    assert pick(dict(differ=0.9, compatible=0.9, opinion=0.1, outdated=0.1, misinformation=0.1)) == "complementary"
    assert pick(dict(differ=0.9, compatible=0.1, opinion=0.1, outdated=0.8, misinformation=0.2)) == "outdated"


def test_tree_hard():
    assert tree_hard(dict(differ=0.4, compatible=0, opinion=1, outdated=1, misinformation=1)) == "no_conflict"
    assert tree_hard(dict(differ=0.6, compatible=0.6, opinion=1, outdated=1, misinformation=1)) == "complementary"
    assert tree_hard(dict(differ=0.6, compatible=0.4, opinion=0.2, outdated=0.1, misinformation=0.7)) == "misinformation"


class FakeGateway:
    def __init__(self, answers):
        self.answers, self.seen = answers, []

    def evaluate(self, state, questions):
        self.seen.append(questions)
        return {"answers": self.answers, "usage": {"input_tokens": 100}, "_latency_s": 0.2, "_cached": False,
                "providerMetadata": {"gateway": {"cost": "0.00001"}}}


def test_flat_renormalises_rounded_probabilities():
    gw = FakeGateway({"conflict_type": {"probabilities": {"outdated": 0.6, "complementary": 0.39}}})
    rec = flat(gw, ROW)
    assert rec["pred"] == "outdated" and abs(sum(rec["probs"].values()) - 1) < 1e-9
    assert rec["cost_usd"] == pytest.approx(1e-5) and rec["latency_s"] == 0.2
    assert list(gw.seen[0]) == ["conflict_type"] and gw.seen[0]["conflict_type"]["type"] == "choice"


def test_tree_asks_all_questions_in_one_request():
    answers = {k: {"probability": 0.1} for k in TREE_QUESTIONS} | {"differ": {"probability": 0.9}, "misinformation": {"noul": 0.9}}
    gw = FakeGateway(answers)
    rec = tree(gw, ROW)
    assert len(gw.seen) == 1 and set(gw.seen[0]) == set(TREE_QUESTIONS)
    assert all(q["type"] == "boolean" for q in gw.seen[0].values())
    assert rec["raw"]["misinformation"] == 0.9 and rec["pred"] == "misinformation"


def test_split_is_stratified_disjoint_and_deterministic():
    rows = [{"id": i, "label": LABELS[i % 5] if i < 400 else "no_conflict"} for i in range(458)]
    a, b = make_split(rows), make_split(rows)
    assert a == b and not set(a["dev"]) & set(a["test"]) and len(a["dev"]) + len(a["test"]) == 458
    assert {rows[i]["label"] for i in a["dev"]} == set(LABELS)


def test_metrics():
    y = ["a", "a", "b", "b"]
    assert accuracy(y, ["a", "b", "b", "b"]) == 0.75
    assert macro_f1(y, y, ["a", "b", "c"]) == 1.0
    assert ece(np.array([1.0, 1.0]), np.array([1.0, 1.0])) == 0.0
    a = np.array([True, True, False, True]); b = np.array([True, False, False, False])
    assert paired_bootstrap(a, b)["diff"] == 0.5
    assert mcnemar_exact(a, b) == mcnemar_exact(b, a) and mcnemar_exact(a, a) == 1.0


def test_real_dataset_loads():
    rows = load()
    assert len(rows) == 458 and {r["label"] for r in rows} == set(LABELS)


def test_combine_tree_v2_asks_opinion_first_and_misinformation_is_the_residual():
    from dmconflict.methods import combine_tree_v2
    pick = lambda p: max(LABELS, key=combine_tree_v2(p).get)
    base = dict(differ=0.9, compatible=0.8, opinion=0.1, outdated=0.1, misinformation=0.9)
    assert abs(sum(combine_tree_v2(base).values()) - 1) < 1e-9
    assert pick(base) == "complementary"
    assert pick(base | {"opinion": 0.7}) == "conflicting_opinions"   # compatible is ignored once opinion wins
    assert pick(base | {"compatible": 0.1, "outdated": 0.8}) == "outdated"
    assert pick(base | {"compatible": 0.1, "outdated": 0.2, "misinformation": 0.0}) == "misinformation"


def test_flat_question_is_the_papers_text_word_for_word():
    import re

    from dmconflict.prompts import FLAT_INSTRUCTIONS, PAPER_PROMPT
    norm = lambda s: re.sub(r"[\s*]+", " ", s).replace(" Example: Query:", "").replace(" Search Results:", "").strip()
    paper = norm(PAPER_PROMPT.replace("*Example:*", "").replace("*Query:*", "").replace("*Search Results:*", ""))
    assert norm(FLAT_INSTRUCTIONS) in paper
    for text in CATEGORIES.values():
        assert norm(text) in paper, text[:40]


def test_paper_prompt_fills_query_and_numbered_results():
    from dmconflict.prompts import paper_prompt
    p = paper_prompt(ROW)
    assert "QUERY: who is the ceo of x" in p and "[1]\nURL: u1" in p and "[2]\nURL: u2" in p
    assert "{query}" not in p and "{search_results}" not in p


def test_parse_category():
    from dmconflict.methods import parse_category
    assert parse_category('```json\n{"explanation": "x", "category": 4}\n```') == "outdated"
    assert parse_category('{"category": "2", "explanation": "y"}') == "complementary"
    assert parse_category('{"category": 7}') == "unparsed" and parse_category("no json") == "unparsed"
    assert parse_category("...\n\n*   **Category:** 5") == "misinformation"
    assert parse_category("explanation: x\n\ncategory: 2") == "complementary"
    assert parse_category("The final answer is $\\boxed{4}$") == "outdated"
    assert parse_category("*   **category:** 3") == "conflicting_opinions"
    assert parse_category("not category 5 of anything") == "unparsed"


def test_paper_llm_record_is_hard_label():
    from dmconflict.methods import paper_llm

    class FakeChat:
        def complete(self, prompt):
            return {"choices": [{"message": {"content": '{"explanation": "e", "category": 3}'}}],
                    "usage": {"prompt_tokens": 50, "cost": 0.0002}, "_latency_s": 1.0}

    rec = paper_llm(FakeChat(), ROW)
    assert rec["pred"] == "conflicting_opinions" and rec["hard"] and rec["cost_usd"] == 0.0002


def _rec(i, label, pred, top, usd=1.0, lat=1.0):
    others = (1 - top) / 4
    return {"id": i, "label": label, "pred": pred, "cost_usd": usd, "latency_s": lat,
            "probs": {k: (top if k == pred else others) for k in LABELS}}


def test_escalate_mask_takes_least_confident():
    from dmconflict.cascade import escalate_mask
    m = escalate_mask(np.array([0.9, 0.2, 0.5, 0.3]), 0.5)
    assert m.tolist() == [False, True, False, True]
    assert not escalate_mask(np.array([0.1, 0.2]), 0).any() and escalate_mask(np.array([0.1, 0.2]), 1).all()


def test_cascade_curve_endpoints_and_cost():
    from dmconflict.cascade import auroc, curve
    cheap = [_rec(0, "outdated", "outdated", 0.9, usd=0.1), _rec(1, "complementary", "no_conflict", 0.3, usd=0.1)]
    exp = [_rec(0, "outdated", "no_conflict", 1.0, usd=2.0, lat=3.0), _rec(1, "complementary", "complementary", 1.0, usd=2.0, lat=3.0)]
    rows = {r["f"]: r for r in curve(cheap, exp, fractions=[0.0, 0.5, 1.0])}
    assert rows[0.0]["acc"] == 0.5 and rows[1.0]["acc"] == 0.5
    assert rows[0.5]["acc"] == 1.0 and rows[0.5]["acc_random"] == 0.5   # the uncertain one was escalated
    assert rows[0.5]["usd_per_1k"] == pytest.approx(1000 * (0.1 + 1.0)) and rows[0.5]["lat_mean"] == pytest.approx(1 + 1.5)
    assert auroc(np.array([0.9, 0.3]), np.array([True, False])) == 1.0


def _prow():
    return {"id": 7, "label": "no_conflict", "question": "q", "answer": "Paris",
            "results": [{"url": "a", "title": "Paris facts", "snippet": "The capital is Paris.", "date": "2024-01-10", "short_text": "PARIS is big"},
                        {"url": "b", "title": "t", "snippet": "s", "date": "Jan 5, 2020", "short_text": "no answer here"},
                        {"url": "c", "title": "t", "snippet": "s", "date": "4 days ago", "short_text": ""}]}


def test_parse_date_formats():
    from dmconflict.perturb import parse_date
    assert parse_date("2025-01-17 00:00:00").year == 2025 and parse_date("Nov 7, 2024").month == 11
    assert parse_date("2024-02-15").day == 15 and parse_date("4 days ago") is None and parse_date("NA") is None


def test_unperturbed_input_is_unchanged_so_cached_runs_stay_valid():
    from dmconflict.perturb import apply
    row = _prow()
    assert state(apply("rerun", row)) == state(row)
    assert "Recency" not in state(row)["result_1"]


def test_date_perturbations():
    from dmconflict.perturb import dates_in_code, no_dates
    row = _prow()
    nd = no_dates(row)
    assert all("Date:" not in v for k, v in state(nd).items() if k != "query") and row["results"][0]["date"] == "2024-01-10"
    dc = dates_in_code(row)
    assert dc["results"][0]["recency"].startswith("1 of 2") and "0 days older" in dc["results"][0]["recency"]
    assert dc["results"][1]["recency"].startswith("2 of 2") and "recency" not in dc["results"][2]
    assert "Recency: 1 of 2" in state(dc)["result_1"]
    one = _prow(); one["results"][1]["date"] = "NA"
    assert all("recency" not in r for r in dates_in_code(one)["results"])   # fewer than two parseable dates


def test_shuffle_is_seeded_and_a_permutation():
    from dmconflict.perturb import shuffle
    row = _prow()
    a, b = shuffle(row, 1), shuffle(row, 1)
    assert a == b and sorted(r["url"] for r in a["results"]) == ["a", "b", "c"]
    assert [r["url"] for r in row["results"]] == ["a", "b", "c"]


def test_plant_replaces_answer_in_one_result_case_insensitively():
    from dmconflict.perturb import apply, plant, plant_candidates
    row = _prow()
    assert plant_candidates(row, "Paris") == [0]
    p = plant(row, "Paris", "Lyon")
    r = p["results"][0]
    assert p["label"] == "misinformation" and p["planted"]["result"] == 1
    assert "Paris" not in r["title"] + r["snippet"] + r["short_text"] and r["short_text"] == "Lyon is big"
    assert row["results"][0]["snippet"] == "The capital is Paris."
    assert plant(row, "Paris", "paris") is None and plant(row, "Rome", "Lyon") is None
    assert apply("plant", row, {"7": {"answer": "Paris", "wrong": "Lyon"}})["label"] == "misinformation"
    assert apply("plant", row | {"label": "outdated"}, {"7": {"answer": "Paris", "wrong": "Lyon"}}) is None


def test_plant_matches_whole_words_and_skips_yes_no():
    from dmconflict.perturb import plant, plant_candidates
    row = {"id": 1, "label": "no_conflict", "question": "q",
           "results": [{"title": "", "snippet": "In 2019 there was 1 winner, not 10.", "short_text": "", "date": "NA"}]}
    p = plant(row, "1", "2")
    assert p["results"][0]["snippet"] == "In 2019 there was 2 winner, not 10."
    yn = {"id": 2, "label": "no_conflict", "question": "q",
          "results": [{"title": "", "snippet": "Yes, it is. No doubt.", "short_text": "", "date": "NA"}]}
    assert plant_candidates(yn, "Yes") == [] and plant_candidates(yn, "no") == []


def test_text_state_carries_the_same_content():
    from dmconflict.prompts import state, text_state
    row = {"question": "Q?", "results": [{"url": "u1", "title": "t1", "snippet": "s1", "text": "x1"},
                                         {"url": "u2", "title": "t2", "snippet": "s2", "text": "x2"}]}
    text = text_state(row)["text"]
    assert text.startswith("Query: Q?\n\n[1]\n")
    for v in state(row).values():
        assert v in text


def test_vanilla_prompt_is_the_papers_and_types_only_add_a_description():
    from dmconflict.generate import TYPE_DESCRIPTIONS, generation_prompt
    row = {"question": "Q?", "label": "outdated", "answer": "A",
           "results": [{"url": "u", "title": "t", "snippet": "s", "text": "x"}]}
    van = generation_prompt(row, "vanilla")
    assert van.startswith("Write a high-quality and concise answer for the given question using only the provided "
                          "search results.\nFor each sentence, cite the corresponding sources using [1][2][3].")
    assert "QUERY: Q?" in van and "[1]" in van and "TYPE OF KNOWLEDGE CONFLICT" not in van
    typed = generation_prompt(row, "outdated")
    assert TYPE_DESCRIPTIONS["outdated"] in typed
    assert typed.replace("TYPE OF KNOWLEDGE CONFLICT IN THE SEARCH RESULTS: " + TYPE_DESCRIPTIONS["outdated"] + "\n\n", "") == van


def test_judge_verdict_parsing():
    from dmconflict.generate import parse_verdict
    assert parse_verdict('{"explanation": "x", "adheres": true}', "adheres") is True
    assert parse_verdict('```json\n{"adheres": false}\n```', "adheres") is False
    assert parse_verdict('"includes_answer": TRUE', "includes_answer") is True
    assert parse_verdict("no verdict here", "adheres") is None
