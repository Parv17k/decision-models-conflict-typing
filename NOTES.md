# Decision log

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
