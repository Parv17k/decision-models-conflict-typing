# Decision log

The study covers typed decision models as a class: every decision model one gateway served on 2026-10-25 (see
"Decision-model lens and the full hosted census" below). It began as a study of one model, Jev 1.13, which is why
the early entries are written about Jev; they are kept as written because this file is a dated record. Since
2026-10-25 the repository is `Parv17k/decision-models-conflict-typing` (formerly `jev-conflict-classifier`) and the
package `dmconflict` (formerly `jevconflict`); commands below that use the old name run as `dmconflict`, and decision-
model methods now need an explicit `--model`.
The per-subset reports named in older entries (`comparison_decision_models_*`, `comparison_full_*`,
`cascade_decision_models_test.md`, `cascade_jev114_test.md`) were consolidated into `runs/comparison_{test,all}.md`,
`runs/cascade_{test,all}.md` and `runs/diagnostics_test.md`, which now cover every model; their numbers are unchanged.

Rule: every setting is chosen on the development split only (52 queries, stratified, `data/splits.json`),
frozen, then run once on the test split (406 queries). Test numbers are the results; development
numbers are tuning evidence.

| Date | Decision | Evidence |
|---|---|---|
| 2026-10-25 | Input = paper's per-result concatenation (URL, title, snippet, date if not "NA", 512-token segment), results in dataset order as `result_1..n` | Cattan et al. §5.1. 16% of results have an empty segment and keep only URL/title/snippet; inputs are 3.4k–42k chars (fits Jev's 32k-token state) |
| 2026-10-25 | Flat question = paper's five category definitions with one example each (Figure 2), unchanged | Same information the paper's LLM classifiers got, so the 65.3% Gemini 2.5 Flash number is a fair reference |
| 2026-10-25 | Tree = five yes/no questions (differ, compatible, opinion, outdated, misinformation) in one request | One call per query, same cost as flat (~$0.18 per 1k queries, ~0.3 s) |
| 2026-10-25 | Added `tree_v2`: the same five answers combined as differ → opinion → compatible → outdated, with misinformation as the remainder. `tree` (v1) and `tree_hard` kept and reported | Dev, Jev 1.13: `compatible` answered yes for opinion topics (mean 0.69 vs 0.81 for complementary), sending 12/13 opinion queries to complementary; `opinion` separates the two well (AUROC 0.83). `misinformation` answered yes for every class (mean 0.53–0.79), the yes-bias reported for batched yes/no questions (arXiv 2609.37647). Dev accuracy: tree 0.481 → tree_v2 0.635 |

| 2026-10-25 | Flat question now carries the paper's prompt **word for word** (instructions, five definitions, the examples with their example search results), taken from the arXiv LaTeX source (`prompts/conflict_type_prediction.tex`). The earlier paraphrase run is kept as `dev/flat_paraphrase_superseded.jsonl` and not reported | Protocol fidelity, not tuning: decided without looking at results. A test fails if any word differs |
| 2026-10-25 | Added the paper's baseline on identical inputs and queries: Gemini 2.5 Flash (`google/gemini-2.5-flash` via Vercel), the paper's prompt verbatim, thinking off (paper lists "Gemini 2.5 Flash" and "… Thinking" separately), temperature 0, results numbered [1], [2], … (the paper doesn't say how it joined them; its generation prompts cite [1][2]). Unparsed answers count as wrong | A published number (65.3%) can't be compared query by query; a rerun on the same split can (paired bootstrap + McNemar) |

## Frozen protocol (2026-10-25, before any test-set call)

- Split: `data/splits.json` (dev 52, test 406), sha256 `f9068dae…5e94a`.
- Questions and prompts: `src/jevconflict/prompts.py` sha256 `c6bd8ca1…ffca90`; combination rules: `src/jevconflict/methods.py` sha256 `091f48b0…f0a8`.
- Systems reported: Jev 1.13.0 `flat`, `tree` (v1), `tree_hard` (v1, 0.5 thresholds), `tree_v2` (dev-revised; stated as such), Gemini 2.5 Flash `paper_llm`.
- Primary result: test split (406). Also reported: all 458, which is what the paper's 65.3% covers (the paper does not say otherwise). On all 458, `tree_v2` includes the 52 queries it was revised on; flat, tree v1 and Gemini were not tuned on anything.
- Metrics: 5-class accuracy (the paper's metric) with 95% bootstrap CI; 4-class accuracy (Outdated + Misinformation merged); macro-F1; per-class F1; ECE/Brier/NLL for probabilistic systems; paired bootstrap and exact McNemar on identical queries; billed $ and latency.
- Known, unavoidable differences from the paper: Jev returns probabilities over the options instead of JSON with an explanation; the paper doesn't state how search results were joined or whether thinking was on for Table 4; a hosted Gemini 2.5 Flash today may differ from the one the paper used.

## Changes after the frozen protocol (baseline only; Jev untouched)

| Date | Change | Why |
|---|---|---|
| 2026-10-25 | Added `paper_llm_thinking` (Gemini 2.5 Flash, provider-default dynamic thinking) as a sensitivity check | Our thinking-off rerun scored 60.7% vs 65.3% published; the paper doesn't say whether Table 4 used thinking. Reported whatever the result |
| 2026-10-25 | Answer parser made lenient (accepts `category: 4`, `**Category:** 4`, `\boxed{4}`; last statement wins), and stored Gemini answers re-parsed with no new calls | 15 thinking-mode answers stated a category outside JSON; counting them wrong would handicap the baseline. No strictly-JSON answer changed |

## Results (frozen; full tables in `runs/comparison_test.md`, `runs/comparison_all.md`)

| System | Test acc. (n = 406) [95% CI] | All 458 | Macro-F1 (test) | ECE (test) | $/1k queries | Latency mean (s) |
|---|---|---|---|---|---|---|
| Jev 1.13 flat (paper's prompt, untuned) | 0.618 [0.569, 0.665] | 0.609 | 0.549 | 0.103 | 0.19 | 0.26 |
| Jev 1.13 tree v1 | 0.473 [0.424, 0.520] | 0.474 | 0.293 | 0.153 | 0.18 | 0.25 |
| Jev 1.13 tree_hard v1 | 0.463 [0.416, 0.510] | 0.461 | 0.321 | – | 0.18 | 0.25 |
| Jev 1.13 tree v2 (dev-revised) | 0.635 [0.589, 0.682] | 0.635 | 0.459 | 0.026 | 0.18 | 0.25 |
| Gemini 2.5 Flash, paper prompt, thinking off | 0.613 [0.567, 0.660] | 0.607 | 0.531 | – | 1.66 | 1.55 |
| Gemini 2.5 Flash, paper prompt, thinking on | 0.579 [0.530, 0.628] | 0.581 | 0.514 | – | 6.04 | 9.57 |
| Gemini 2.5 Flash, as published | – | 0.653 | – | – | – | – |

Paired (test): flat vs Gemini-off +0.005 (p = 0.92); tree_v2 vs Gemini-off +0.022 (p = 0.49);
flat vs tree v1 +0.145 (p < 1e-5); flat vs tree_v2 −0.017 (p = 0.59). Total billed: about $3.7.

## Laya: dropped from the comparison (2026-10-25)

Hosted Laya (`convaiinnovations/laya` on Vercel, same key) can't run the frozen protocol. Probes on a dev query:
- The flat question with the paper's definitions is rejected (HTTP 422) even with a near-empty state. Laya caps each
  option at 48 tokens and the whole question head at 192 (`laya.common.build_head`); hosted Laya rejects instead of truncating.
- The short tree questions are accepted, but the state then holds about 1,700 characters (~400 tokens). A median query's
  sources are about 15,000 characters.
- Fitting it would need shortened definitions and sources cut to about a tenth: a different task, plus a Jev control on
  the same cut inputs. Prior work has Laya near chance zero-shot (26.3% on JEVal, arXiv 2610.03935).
Decision (authors): leave Laya out; mention it in one sentence in the paper. No Laya results were produced.

Re-checked 2026-10-25 when `laya-multilingual` (sliding window to 8,192 tokens) was suggested. The gateway lists only
`convaiinnovations/laya` and `laya-free`, both already advertising an 8,192-token context window. Probes on one dev
query (free model): the paper's question is rejected (422) even with a 200-character state; with five short labels in
place of the definitions, the request is still rejected at 3,000 characters of state and accepted at 1,500, where it
returned near-uniform probabilities (0.15–0.25). The paper's definitions are 261–409 characters each, so the
per-option cap blocks the frozen question regardless of the context window. No change to the decision.

## Added baseline: Gemini 3.8 Flash (2026-10-25)

Newest Flash on the gateway (`google/gemini-3.8-flash`). Same frozen protocol: the paper's prompt verbatim, same inputs,
same 458 queries, same lenient parser, temperature 0. Thinking can't be switched off on 3.8 (budget 0 still reasons;
`minimal` is rejected), so two settings: `low` (lowest accepted level; 0 reasoning tokens on the probes) and the
provider default. Settings fixed before any run; both reported.

| System (test, n = 406) | Accuracy [95% CI] | Macro-F1 | $/1k queries | Latency mean (s) |
|---|---|---|---|---|
| Gemini 3.8 Flash, thinking low | 0.700 [0.655, 0.744] | 0.613 | 3.65 | 2.18 |
| Gemini 3.8 Flash, thinking default | 0.667 [0.621, 0.712] | 0.594 | 5.51 | 5.01 |

Paired (test): Jev flat − Gemini 3.8 low = −0.081 [−0.123, −0.039], McNemar p = 0.0003; Jev tree_v2 − Gemini 3.8 low =
−0.064 (p = 0.019); Jev tree_v2 − Gemini 3.8 default = −0.032 (p = 0.27). Gemini 3.8 low beats Gemini 2.5 Flash
(thinking off) by 8.6 points (p = 0.0006). Spend for 3.8: $4.21.

## Cascade protocol (fixed 2026-10-25, before computing any cascade number)

Offline from stored answers; no new calls.
- Cheap stage: Jev 1.13 `flat` (untuned) and, separately, `tree_v2` (dev-revised; stated as such). Confidence = top probability.
- Expensive stage: Gemini 3.8 Flash, thinking low (best baseline). Escalated queries take Gemini's answer.
- Escalate the fraction f of queries with the lowest Jev confidence, f = 0, 5, …, 100%. The threshold is a quantile
  of Jev's confidences on the evaluated queries; it uses no labels, so the whole curve can be computed on test.
- Headline operating points, chosen now: f = 25% and f = 50%.
- Cost per query = Jev's billed cost (always paid) + Gemini's billed cost on escalated queries. Latency = Jev latency
  + Gemini latency on escalated queries (sequential).
- Controls: random escalation at the same f (expected accuracy (1 − f)·acc_Jev + f·acc_Gemini, exact by linearity);
  selective-prediction AUROC of Jev confidence for Jev being correct.
- Tests: paired bootstrap and exact McNemar, cascade vs Gemini 3.8 alone, on the same queries.

### Cascade results (full curves: `runs/cascade_test.md`, `runs/cascade_all.md`)

Test, n = 406; expensive stage Gemini 3.8 Flash (thinking low): 0.700 at $3.65/1k, 2.18 s.

| Cheap stage | f | Accuracy | Random escalation | − Gemini alone [95% CI] | McNemar p | Cost vs Gemini | Latency mean / p95 (s) |
|---|---|---|---|---|---|---|---|
| Jev flat | 25% | 0.685 | 0.639 | −0.015 [−0.044, +0.015] | 0.41 | 30% | 0.81 / 2.64 |
| Jev flat | 50% | 0.692 | 0.659 | −0.007 [−0.027, +0.010] | 0.61 | 54% | 1.34 / 2.89 |
| Jev tree_v2 | 25% | 0.685 | 0.652 | −0.015 [−0.054, +0.025] | 0.54 | 29% | 0.81 / 2.62 |
| Jev tree_v2 | 50% | 0.714 | 0.667 | +0.015 [−0.007, +0.039] | 0.31 | 54% | 1.33 / 2.82 |

- Confidence-gated escalation beats random escalation at every f (e.g. flat at 25%: +4.6 points).
  AUROC of Jev confidence for Jev correct: flat 0.701, tree_v2 0.732.
- No cascade point is significantly different from Gemini alone. "Not significant" is not equivalence: at flat 25%
  the interval rules out a loss larger than 4.4 points.
- tree_v2 at 30–55% is numerically above Gemini alone (complementary errors: Jev right / Gemini wrong on 44 queries).
  Not significant, and tree_v2 is dev-revised; report it as a trend.
- All 458 queries: the same picture (flat 25%: 0.675 vs 0.690, p = 0.34, 30% of cost; tree_v2 50%: 0.703 vs 0.690, p = 0.35).

## Diagnostic protocol (fixed 2026-10-25, before building or running any perturbation)

Systems: Jev 1.13 `flat`, Jev 1.13 `tree` (scored as v1 and v2), Gemini 3.8 Flash thinking low. Split: test (406).
Prompts, questions and combination rules are unchanged; only the search results are perturbed, identically for
every system. Each perturbed run is compared with the same system's original run on the same queries.

| ID | Perturbation | Question it answers | Measures |
|---|---|---|---|
| R0 | Rerun the identical request, bypassing the cache | Noise floor: how often does a system change its answer with nothing changed? | Flip rate |
| D1a | Remove the date from every result | Does the system use dates at all? | Accuracy; Outdated-class recall and F1; McNemar vs original |
| D1b | Dates parsed in code: each dated result gets `Recency: k of N dated results (1 = newest); D days older than the newest` | Does doing the date arithmetic in code fix the Outdated class (Jev's documented date weakness)? | Same as D1a |
| D2 | Shuffle result order (seeds 1 and 2) | Order sensitivity | Flip rate vs R0 noise floor; accuracy change; for Jev, mean total-variation distance between probability vectors |
| D3 | Plant one false source: in a No-conflict query whose gold answer appears verbatim in some result, pick one such result (seeded), replace every occurrence of the gold answer in its title, snippet and text with a plausible wrong answer. Wrong answers come from `openai/gpt-4.1-mini` (a third vendor, so neither classifier grades its own text), temperature 0, prompt in `perturb.py` | Does a single contradicting source get noticed, and labelled Misinformation? | Share predicted Misinformation (expected label by construction); share predicted any conflict; vs the same queries unperturbed |

- D1b parses `YYYY-MM-DD`, `YYYY-MM-DD hh:mm:ss`, `Mon D, YYYY`; relative dates ("4 days ago", 27 results) are left as text
  without a recency line. Queries with fewer than two parseable dates get no recency lines.
- D3 population: the 115 test No-conflict queries with the gold answer verbatim in at least one result.
- Amendment (2026-10-25, after generating wrong answers, before any plant run): matching is whole-word
  (substring matching would have turned "2019" into "2029" when planting "1" → "2"), and Yes/No answers are excluded
  (flipping every "no" in a text is not an entity substitution). D3 population: 96 queries.
- Not tuned on anything; every perturbation runs once, all results reported.
- Estimated spend: Jev ≈ $0.8, Gemini 3.8 ≈ $8, wrong-answer generation < $0.05.

### Diagnostic results (test; full report `runs/diagnostics_test.md`; spend $8.55)

**R0, noise floor.** Neither system is deterministic: an identical rerun changes the predicted type on 2.0% of queries
(Jev flat), 2.5% (tree_v2), 3.4% (Gemini 3.8 low). Jev flat's probability vectors are identical on only 14.5% of reruns.

**D1, dates. The date hypothesis is not supported.** Removing dates or adding code-computed recency changes no system's
accuracy beyond rerun noise (all |Δ| ≤ 1.0 point, all p ≥ 0.34) or Outdated recall (Jev flat 0.727 → 0.745 / 0.764;
Gemini 0.691 → 0.673 / 0.727). Jev flat's Outdated recall (0.727) is already above Gemini's (0.691). Outdated is
detected from content ("former", "as of", conflicting values), not dates. The weak Outdated class seen earlier was
specific to the tree (the `outdated` yes/no question), not a date problem.

**D2, order.** Shuffling raises flip rates well above rerun noise for every system: Jev flat 11.6% [9.4, 13.8] vs 2.0%;
tree_v2 9.1% vs 2.5%; Gemini 9.4% [7.5, 11.5] vs 3.4%. Jev flat vs Gemini on the same shuffles: not significant
(p = 0.23, 0.49). Accuracy changes are within ±2.7 points; only tree v1 on seed 2 crosses p < 0.05 (−2.2, p = 0.035).
Order sensitivity is real but not specific to Jev.

**D3, one planted false source (96 No-conflict queries).**

| System | Misinfo hit (planted) | Misinfo false alarm (same queries, clean) | Youden | Any-conflict hit / false alarm |
|---|---|---|---|---|
| Jev flat | 0.667 | 0.177 | +0.490 | 0.854 / 0.417 |
| Jev tree_v2 | 0.198 | 0.021 | +0.177 | 0.677 / 0.250 |
| Gemini 3.8 low | 0.521 | 0.031 | +0.490 | 0.719 / 0.250 |

Jev flat flags more planted sources than Gemini (p = 0.004) but also more clean ones (p = 0.0005); net discrimination
is identical (Youden difference +0.000 [−0.115, +0.104]). Jev flat's P(Misinformation) separates planted from clean
copies with AUROC 0.806, so a threshold could trade hits for false alarms. tree_v2's residual-misinformation rule
(chosen on dev, where misinformation had 1 query) misses planted sources: 0.198. That is a cost of the v2 revision,
to state with it.

## Other decision models (protocol fixed 2026-10-25, before any run)

- Models (Vercel `/v1/evaluate`, same key): `microsoft/microsoft-decision-1`, `liquid/d1`, `perplexity/pplx-decider-v1.2`,
  `openai/gpt-6-luna-decisions`. All four accepted the largest test query (~10k tokens) with both question formats.
  `microsoft-decision-1`, `d1` and `gpt-6-luna-decisions` have no version in their ids; record the run date.
- Exactly Jev's frozen questions (`flat`, `tree`), inputs and combination rules (v1, tree_hard, tree_v2). tree_v2's
  order was chosen on Jev's dev answers; it is applied unchanged, not re-fitted per model.
- Runs on dev and test (all 458); test is primary. Nothing tuned per model.
- Reported: the comparison table (accuracy, macro-F1, calibration, cost, latency, paired tests vs Jev flat and vs
  Gemini 3.8 low), and each model's `flat` as the cheap stage of the same cascade (headline f = 25%, 50%).

### Results (test, n = 406; run 2026-10-25; spend $0.71; tables `runs/comparison_decision_models_{test,all}.md`, cascades `runs/cascade_decision_models_test.md`)

| Model | flat acc. [95% CI] | tree_v2 acc. | flat macro-F1 | flat ECE | $/1k | Latency (s) | flat − Gemini 3.8 low (p) |
|---|---|---|---|---|---|---|---|
| Perplexity decider v1.2 | 0.667 [0.621, 0.712] | **0.690** | 0.565 | 0.061 | 0.086 | 0.42 | −0.032 (0.14); tree_v2 −0.010 (0.72) |
| OpenAI GPT-6-luna decisions | 0.663 [0.616, 0.709] | 0.500 | 0.547 | 0.059 | 0.415 | 0.35 | −0.037 (0.13) |
| Liquid d1 | 0.626 [0.576, 0.672] | 0.584 | 0.515 | 0.075 | 0.085 | 0.41 | −0.074 (0.002) |
| Jev 1.13 | 0.618 [0.569, 0.665] | 0.635 | 0.549 | 0.103 | 0.194 | 0.26 | −0.081 (0.0003) |
| Microsoft decision-1 | 0.581 [0.532, 0.628] | 0.574 | 0.502 | 0.188 | 0.177 | 0.45 | −0.118 (<0.0001) |
| Gemini 3.8 Flash, thinking low | 0.700 [0.655, 0.744] | – | 0.613 | – | 3.646 | 2.18 | – |

- Jev flat vs Perplexity flat: −0.049, p = 0.031 (Perplexity better). Jev vs Liquid, Microsoft, GPT-6-luna: not significant.
- Perplexity tree_v2 is statistically tied with Gemini 3.8 Flash at about 1/45 of the cost and a fifth of the latency.
- tree_v2 (fitted on Jev's dev answers) helps Jev and Perplexity, hurts Liquid, Microsoft and especially GPT-6-luna
  (0.663 → 0.500). The tree design does not transfer across models; flat is the robust format.
- Calibration: Perplexity, GPT-6-luna and Liquid (ECE 0.06–0.08) beat Jev (0.10) and Microsoft (0.19) on flat.
- Cascades (flat → Gemini 3.8 low, f = 25%): Perplexity 0.702 at 27% of Gemini's cost (Δ +0.002, p = 1); Jev 0.685
  (30%); Liquid 0.675 (27%); GPT-6-luna 0.670 (37%); Microsoft 0.660 (29%, p = 0.048). GPT-6-luna's confidence is
  barely informative (AUROC 0.648): its 25% cascade equals random escalation (0.670 vs 0.672).

## Jev 1.14.0 (protocol fixed 2026-10-25, before any run)

`typesafe-ai/jev-1.14.0` on the gateway, same key. Exactly the frozen 1.13 protocol: same questions, inputs, combination
rules (tree_v2 unchanged), all 458 queries, test primary. Reported next to 1.13 with paired tests (1.14 vs 1.13, and vs
Gemini 3.8 low), and as the cheap stage of the same cascade. Purpose: version stability of the paper's claims. 1.13
stays the primary model (all diagnostics were run on it); 1.14 is a robustness row.

### Jev 1.14.0 results (test, n = 406; spend ≈ $0.16; `runs/comparison_full_test.md`, `runs/cascade_jev114_test.md`)

| Version | flat acc. [95% CI] | tree v1 | tree_v2 | flat ECE | tree_v2 ECE | $/1k | Latency (s) |
|---|---|---|---|---|---|---|---|
| Jev 1.13.0 | 0.618 [0.569, 0.665] | 0.473 | 0.635 | 0.103 | 0.026 | 0.19 | 0.26 |
| Jev 1.14.0 | 0.596 [0.547, 0.645] | 0.451 | 0.628 | 0.113 | 0.031 | 0.19 | 0.28 |

- 1.14 vs 1.13: flat −2.2 (p = 0.12), tree_v2 −0.7 (p = 0.66): no significant change. Claims hold across versions.
- 1.14 vs Gemini 2.5 Flash (paper's setup): flat −1.7 (p = 0.56), tree_v2 +1.5 (p = 0.67): still tied.
- 1.14 vs Gemini 3.8 low: flat −10.3 (p < 0.0001), tree_v2 −7.1 (p = 0.008).
- Same failure pattern: tree v1's opinion F1 0.019 (1.13: 0.038); Outdated is again flat's strength (F1 0.613).
- Cascade → Gemini 3.8 low: flat 25% 0.658 (−4.2, p = 0.016), 50% 0.687 (p = 0.36); tree_v2 50% 0.727 (+2.7 vs Gemini
  alone, p = 0.052, borderline; report as a trend).

## Paper framing (decided by the authors, 2026-10-25)

Jev-centred: Jev is the subject; LLMs (Gemini 2.5 / 3.8 Flash) and the other four decision models are comparison
context. All five decision models stay in the main comparison table (dropping the one that beats Jev would be
selective reporting). Claims must stay inside the evidence:
- Supported: first study of Jev for RAG context-conflict typing; ties the paper's Gemini 2.5 Flash at ~1/9 the cost and
  6x faster; fastest of all systems tested (0.26 s); cascade with Gemini 3.8 recovers most of the gap at ~30% cost;
  matches Gemini 3.8 on order robustness and planted-source discrimination.
- Not supported: "best decision model" (Perplexity is better, p = 0.03); "cheapest" (Liquid, Perplexity ~$0.09 vs
  $0.19 per 1k); "on par with the current LLM" (−8.1 vs Gemini 3.8, p = 0.0003); "first study of Jev as a classifier"
  (arXiv 2609.37647, 2610.11978, 2610.03935 already evaluate Jev on classification; the novelty is the conflict task).

## Decision-model lens and the full hosted census (protocol fixed 2026-10-25, before any run)

Authors' decision: the paper's subject becomes typed decision models as a class, not Jev. No model is singled out in
the title, abstract or contributions; Jev is one of the models. This supersedes "Paper framing" above for the paper's
framing; that section's evidence rules still apply to every model.

- Census: every `type: evaluation` model on the gateway on 2026-10-25. Already run: `typesafe-ai/jev-1.13.0`,
  `typesafe-ai/jev-1.14.0`, `perplexity/pplx-decider-v1.2`, `openai/gpt-6-luna-decisions`, `liquid/d1`,
  `microsoft/microsoft-decision-1`. Added now: `perplexity/pplx-decider-flash-v1.2`, `liquid/d1-ultra`,
  `baseten/elephant-1`, `baseten/mammoth-1`, `scaledown/scaledown-classify-1`. Not run: `typesafe-ai/jev` (floating
  alias of a pinned version), `convaiinnovations/laya` and `laya-free` (input limits, see Laya section).
- Acceptance probe before any run: the largest test query (by state size) with the flat and the tree question; HTTP
  status only, no outputs read. A model that rejects is reported as excluded with the reason, as Laya was.
- Protocol identical to "Other decision models": Jev's frozen `flat` and `tree` questions, same inputs, combination
  rules applied unchanged (tree_v2 stays as fitted on Jev 1.13's dev answers and is reported as such), dev + test,
  nothing tuned per model. Each model's `flat` is the cheap stage of the same cascade (f = 25%, 50%).
- Diagnostics extended to every decision model's `flat` (all 11 accepted models): rerun, no_dates, dates_in_code,
  shuffle1, shuffle2, and plant on the frozen `data/plants.json`. Reason: under the new lens, the hypotheses are about
  decision models, so one model is not enough. Hypotheses, perturbations and metrics unchanged. Tree diagnostics stay
  Jev-only (already run).
- Jev 1.14 stays a version-stability row; Jev 1.13 is the Jev entry everywhere else (unchanged from before).

Acceptance probe (largest test query, 44,264 characters of state): Perplexity decider flash v1.2, Liquid d1 ultra,
Baseten Elephant-1 and Mammoth-1 accept both questions. ScaleDown Classify-1 rejects any state without a `text` or
`document` field (422, a schema requirement, not a length limit). Amendment, fixed before any ScaleDown run: ScaleDown
receives the same content as one `text` field, rendered exactly as the LLMs' numbered results block
(`Query: ...` then `[1] ...`, `[2] ...`); questions unchanged. It accepted both questions on the largest query. Reported
with a footnote on the input format.

### Census results (test, n = 406; run 2026-10-25; spend about $1.5; all numbers in `paper/generated/`)

- Flat accuracy 50.0–67.0% (median 62.6). Against Gemini 2.5 Flash (paper's setup, 61.3%): 8 tied, 2 better
  (Liquid d1 Ultra +5.7, p = 0.027; Perplexity v1.2 +5.4, p = 0.049), 1 worse (ScaleDown −11.3). Against Gemini 3.8
  low (70.0%): 3 tied (Liquid d1 Ultra, Perplexity v1.2, GPT-6 Luna), 8 worse. Baseten Elephant-1 and Mammoth-1 were
  billed $0 (free on the gateway).
- Tree v1 significantly worse than flat for all 11. Tree v2 (fitted on Jev 1.13 dev): better for 0, tied 7, worse 4.
- Cascade at 25% → Gemini 3.8 low: 8 of 11 tied with the LLM at 25–37% of its cost; confidence beats random for 10
  of 11 (GPT-6 Luna is the exception, AUROC 0.65).
- Diagnostics (flat): dates significant in 0 of 22 tests. 5 models deterministic on rerun. Shuffle flips 5.4–42.1%
  (Gemini 9.4%); paired vs Gemini, 4 flip more, 1 less, 6 no different; accuracy changes in 2 of 22 shuffle tests
  (both GPT-6 Luna). Planted source: as hard labels 8 of 11 significantly worse than Gemini 3.8 (Youden), 3 tied
  (Jev 1.13 equals it at +0.490); P(Misinformation) AUROC ≥ 0.75 for 10 of 11.
- Draft claims corrected after these results (before any text was shared): "no system is deterministic", "order
  sensitivity is shared with the LLM", "most decision models detect a planted source as well as the LLM".

## End-to-end experiment: does a cheaper type predictor keep the Pipeline gain? (protocol fixed 2026-10-25, before any generation call)

Question: Cattan et al. report that giving the generator a *predicted* conflict type raises expected-behaviour
adherence by about 9 points over Vanilla (their "Pipeline"; gold type, "Oracle", about 24). Do decision-model and
cascade predictions keep that gain at a fraction of the classification cost?

Generation (follows Cattan et al. §4 and App. A; their source is the reference):
- Generator: `google/gemini-2.5-flash`, thinking off, temperature 0 (their "Gemini 2.5 Flash" row: Vanilla 65.7,
  Pipeline 75.1, Oracle 88.0). Inputs: the same numbered search results as the classification runs.
- Vanilla prompt: their Figure 3 verbatim. Type-conditioned prompt: Vanilla plus a description of the conflict type
  ("we add a description of the conflict type to the Vanilla prompt"; the exact wording is not published). Ours: the
  type's definition and expected behaviour from their §2, with citations and worked examples removed, inserted between
  the instruction and the query. Fixed before any call; same text for every predictor.
- Design: for each test query, one answer per possible type (5) plus Vanilla, generated once. A predictor's Pipeline
  answer for a query is the answer generated for the type it predicts. Conditional on the type, every predictor
  therefore gets the identical answer, so differences between predictors come only from the types they supply.
  Unparsed LLM predictions fall back to Vanilla.

Evaluation (rebuilt from their §3; their grader prompts are not published):
- Expected-behaviour adherence: binary LLM judge, `google/gemini-2.5-flash` (their judge model), thinking off,
  temperature 0. One prompt per *gold* type containing the query, the type's definition and expected behaviour, the
  adherent / non-adherent example pair from their Table 3 (for No conflict, which has no published pair, one pair we
  write around their Titanic example), and the candidate response. No search results, as in their description. Output:
  short reason, then a yes/no verdict. Same judge for every condition.
- Answer recall: LLM judge of semantic inclusion of the gold answer, on gold No conflict, Outdated and Misinformation
  queries (202 test queries), same judge model.
- Factual grounding (their third metric) is not measured: generation is identical across predictors given a type, and
  the question is behaviour. Stated as a limitation.
- Judge validation: 100 answers sampled with a fixed seed, stratified by gold type (20 each; Misinformation takes all
  of its answers and the rest goes to the other types) and by condition (half Vanilla, half type-conditioned), labelled
  by co-authors blind to the judge's verdict and to the condition. Agreement reported as accuracy (Cattan et al.: 0.89)
  and Cohen's kappa. Pre-specified fallback: if agreement is below 0.80, rerun the same judge prompts with
  `google/gemini-3.8-flash` (thinking low) and report both judges.

Conditions (test split, 406 queries), all computed from the one answer table:
- Vanilla; Oracle (gold type).
- Pipeline with types from: Gemini 2.5 Flash (thinking off; Cattan et al.'s Pipeline predictor), Gemini 3.8 Flash
  (thinking low); each of the 11 decision models (flat question); each decision model's cascade to Gemini 3.8 Flash
  at f = 25% and 50%. All predictions are the stored classification runs; no new classification calls.
- Reported: adherence (overall and per gold type), answer recall, paired bootstrap CI and exact McNemar against
  Vanilla and against the Gemini 2.5 Flash Pipeline, share of the Oracle gain recovered, and classification cost per
  1k queries. Primary claims: (a) reproduction of the Pipeline gain over Vanilla; (b) for each decision model and
  cascade, tied / better / worse than the Gemini 2.5 Flash Pipeline.
- Development split: the same pipeline runs on the 52 dev queries first, to check prompts, parsing and costs only.
  No prompt is changed on the basis of dev scores; bug fixes are logged here.
- Estimated spend: about $8 (2,436 generations and about 2,640 judge calls on test, plus dev).

Dev pipeline check (2026-10-25, 52 queries, $0.63): 312 answers, none empty; 312 behaviour and 156 recall verdicts,
none unparsed. No code or prompt changed afterwards. Observation recorded, not acted on (the protocol forbids tuning
on dev scores): Vanilla adherence is 0.846 on dev against 0.657 in Cattan et al. for the same generator, so our judge
may be more lenient than theirs (it sees no search results, as their description says, but its prompts and examples
differ). The human validation decides; the fallback judge is pre-specified above.

### Test results (2026-10-25; judge validated 2026-10-26, below; spend $5.14; `runs/endtoend_test.md`)

2,436 answers, 2,436 behaviour and 1,212 recall verdicts; none empty or unparsed.
- Vanilla 0.879, Oracle 0.953 (+7.4, p < 0.001). Gemini 2.5 Flash Pipeline 0.916 (+3.7 over Vanilla, p = 0.03;
  half of the Oracle gain). Cattan et al.: Vanilla 0.657, Pipeline 0.751, Oracle 0.880 for this generator. Our judge
  rates Vanilla far higher, which compresses every gain (ceiling); the ordering Vanilla < Pipeline < Oracle holds.
- Decision models (flat) as the Pipeline predictor: 10 of 11 not significantly different from the Gemini 2.5 Flash
  Pipeline (−1.5 to +0.7 points); ScaleDown is significantly worse (−3.9, p = 0.011) and equal to Vanilla.
  GPT-6 Luna −2.7 (p = 0.052). Cascades at 25%: all 11 within −1.0 to +0.7 of the Gemini 2.5 Pipeline.
- Gains concentrate where Cattan et al. found them: Conflicting opinions (Vanilla 0.824 → Oracle 0.971) and Outdated
  (0.727 → 0.873). No conflict is at ceiling (0.951 → 0.958).
- Answer recall 0.906 (Vanilla) to 0.931; no condition lowers it.
- Human validation sheet: `human_eval/behaviour_sample.csv` (100 items, seed 13, 20 per gold type, 44 Vanilla); key
  in `runs/human_eval_key_test.csv`. The judge says "follows" for 94 of the 100, so kappa, not accuracy alone, is the
  informative statistic.

### Judge validation (2026-10-26): the primary judge meets the pre-specified threshold

Two co-authors labelled the 100 items blind (`human_eval/behaviour_sample_1.csv`, `_2.csv`). One label is excluded:
in sheet 2, the row for item 99 shows item 98's response.

| Agreement on the 100 items | Accuracy | Kappa |
|---|---|---|
| Annotator 1 vs annotator 2 | 0.920 | 0.668 |
| Primary judge (Gemini 2.5 Flash) vs majority (ties count as follows, as coded before labelling) | 0.920 | 0.459 |
| Primary judge vs annotator 1 / annotator 2 | 0.910 / 0.870 | 0.484 / 0.323 |
| Primary judge vs both, where they agree (n = 92) | 0.924 | 0.497 |
| Fallback judge (Gemini 3.8 Flash low) vs majority; vs annotator 1 / 2 | 0.870; 0.840 / 0.820 | 0.244; 0.186 / 0.155 |

Per gold type, primary judge where the annotators agree: No conflict 0.900 (n = 20), Complementary 0.947 (19),
Conflicting opinions 0.889 (18), Outdated 0.938 (16), Misinformation 0.947 (19). Kappa is moderate because both
humans and judge say "follows" for about 90% of items.

Claude Sonnet 5.5 given the annotators' README
(`scripts/llm_annotator.py`, not pre-specified, $0.35) is in `human_eval/behaviour_sample_llm_claude-sonnet-5.5.csv`.

Fallback judge results on test (run on all answers while the validation was in progress; 3,648 verdicts, none
unparsed, $2.54; `runs/endtoend_test_judge_gemini-3.8-flash.md`, next to the primary judge's `runs/endtoend_test.md`):
- Vanilla 0.911, Oracle 0.968 (+5.7, p < 0.001), Gemini 2.5 Flash Pipeline 0.897 (−1.5 vs Vanilla, p = 0.47). The
  Pipeline gain over Vanilla (claim a) is therefore judge-dependent: +3.7 (p = 0.03) under the primary judge, none
  under the fallback. The Oracle gain holds under both.
- Claim (b) holds under both judges: of 34 predictors (11 decision models, their 25% and 50% cascades, Gemini 3.8),
  one differs significantly from the Gemini 2.5 Flash Pipeline under each judge (primary: ScaleDown −3.9, p = 0.011;
  fallback: Microsoft Decision-1 → Gemini 3.8 at 25%, +2.7, p = 0.035), a rate consistent with chance over 34 tests.
- Answer recall 0.871–0.896 under the fallback (primary 0.906–0.931).

## Development results (Jev 1.13.0, n = 52; flat here is the superseded paraphrase)

| Method | Accuracy [95% CI] | Macro-F1 | ECE |
|---|---|---|---|
| flat | 0.519 [0.385, 0.654] | 0.448 | 0.191 |
| tree (v1) | 0.481 [0.346, 0.615] | 0.296 | 0.169 |
| tree_hard (v1, 0.5 thresholds) | 0.442 [0.308, 0.577] | 0.344 | – |
| tree_v2 | 0.635 [0.500, 0.769] | 0.455 | 0.122 |

Open observations for the diagnostic experiments:
- Outdated is the weakest class for every method (tree_v2: 1/7 correct). That matches Jev's documented
  date-ordering weakness; next test is dates handled in code.
- Flat confuses Conflicting opinions with Misinformation (6/13) and No conflict with Outdated (5/18).
- Flat is over-confident: mean top probability 0.71 at accuracy 0.52.
