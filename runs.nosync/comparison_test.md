# Conflict-type classification on CONFLICTS, split `test` (n = 406)

| System | Accuracy [95% CI] | 4-class acc. | Macro-F1 | ECE | Brier | NLL | Unparsed | Input tokens | $/1k queries | Latency mean / p95 (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| jev-1.13.0 flat | 0.618 [0.569, 0.665] | 0.633 | 0.549 | 0.103 | 0.534 | 1.112 | 0 | 4611 | 0.194 | 0.26 / 0.40 |
| jev-1.13.0 tree | 0.473 [0.424, 0.520] | 0.483 | 0.293 | 0.153 | 0.678 | 1.296 | 0 | 4299 | 0.181 | 0.25 / 0.35 |
| jev-1.13.0 tree_hard | 0.463 [0.416, 0.510] | 0.485 | 0.321 | – | – | – | 0 | 4299 | 0.181 | 0.25 / 0.35 |
| jev-1.13.0 tree_v2 | 0.635 [0.589, 0.682] | 0.638 | 0.459 | 0.026 | 0.488 | 0.934 | 0 | 4299 | 0.181 | 0.25 / 0.35 |
| gemini-2.5-flash paper_llm | 0.613 [0.567, 0.660] | 0.621 | 0.531 | – | – | – | 0 | 4359 | 1.656 | 1.55 / 2.13 |
| gemini-2.5-flash paper_llm_thinking | 0.579 [0.530, 0.628] | 0.606 | 0.514 | – | – | – | 0 | 4359 | 6.037 | 9.57 / 18.17 |
| gemini-3.8-flash paper_llm_low | 0.700 [0.655, 0.744] | 0.702 | 0.613 | – | – | – | 0 | 4359 | 3.646 | 2.18 / 2.91 |
| gemini-3.8-flash paper_llm_thinking | 0.667 [0.621, 0.712] | 0.670 | 0.594 | – | – | – | 0 | 4359 | 5.510 | 5.01 / 9.38 |
| Gemini 2.5 Flash, as published (paper Table 4) | 0.653 | – | – | – | – | – | – | – | – | – |

4-class accuracy merges Outdated and Misinformation, as the paper does for behaviour.
Hard-label systems (paper_llm, tree_hard) have no probabilities, so calibration is not defined.
Unparsed answers count as wrong. tree_hard and tree_v2 reuse the tree's calls (same cost and latency).

## Per-class F1

| System | no_conflict | complementary | conflicting_opinions | outdated | misinformation |
|---|---|---|---|---|---|
| jev-1.13.0 flat | 0.640 | 0.627 | 0.725 | 0.650 | 0.102 |
| jev-1.13.0 tree | 0.712 | 0.478 | 0.038 | 0.102 | 0.133 |
| jev-1.13.0 tree_hard | 0.659 | 0.503 | 0.111 | 0.212 | 0.118 |
| jev-1.13.0 tree_v2 | 0.695 | 0.549 | 0.743 | 0.310 | 0.000 |
| gemini-2.5-flash paper_llm | 0.609 | 0.597 | 0.762 | 0.590 | 0.098 |
| gemini-2.5-flash paper_llm_thinking | 0.560 | 0.594 | 0.756 | 0.541 | 0.121 |
| gemini-3.8-flash paper_llm_low | 0.718 | 0.683 | 0.751 | 0.661 | 0.250 |
| gemini-3.8-flash paper_llm_thinking | 0.707 | 0.620 | 0.712 | 0.655 | 0.273 |

## Paired comparisons (same queries)

| A vs B | Acc. A − B [95% CI] | McNemar p |
|---|---|---|
| jev-1.13.0 flat vs jev-1.13.0 tree | +0.145 [+0.086, +0.204] | 4.42e-06 |
| jev-1.13.0 flat vs jev-1.13.0 tree_hard | +0.155 [+0.099, +0.212] | 2.54e-07 |
| jev-1.13.0 flat vs jev-1.13.0 tree_v2 | -0.017 [-0.071, +0.034] | 0.586 |
| jev-1.13.0 flat vs gemini-2.5-flash paper_llm | +0.005 [-0.044, +0.054] | 0.922 |
| jev-1.13.0 flat vs gemini-2.5-flash paper_llm_thinking | +0.039 [-0.002, +0.081] | 0.0888 |
| jev-1.13.0 flat vs gemini-3.8-flash paper_llm_low | -0.081 [-0.123, -0.039] | 0.000317 |
| jev-1.13.0 flat vs gemini-3.8-flash paper_llm_thinking | -0.049 [-0.094, -0.007] | 0.0308 |
| jev-1.13.0 tree vs jev-1.13.0 tree_hard | +0.010 [-0.015, +0.034] | 0.572 |
| jev-1.13.0 tree vs jev-1.13.0 tree_v2 | -0.163 [-0.214, -0.111] | 4.16e-09 |
| jev-1.13.0 tree vs gemini-2.5-flash paper_llm | -0.140 [-0.202, -0.079] | 2.2e-05 |
| jev-1.13.0 tree vs gemini-2.5-flash paper_llm_thinking | -0.106 [-0.172, -0.042] | 0.00217 |
| jev-1.13.0 tree vs gemini-3.8-flash paper_llm_low | -0.227 [-0.281, -0.172] | 1.46e-14 |
| jev-1.13.0 tree vs gemini-3.8-flash paper_llm_thinking | -0.195 [-0.251, -0.135] | 1.98e-10 |
| jev-1.13.0 tree_hard vs jev-1.13.0 tree_v2 | -0.172 [-0.227, -0.118] | 2.56e-09 |
| jev-1.13.0 tree_hard vs gemini-2.5-flash paper_llm | -0.150 [-0.209, -0.091] | 2.69e-06 |
| jev-1.13.0 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.116 [-0.180, -0.054] | 0.000437 |
| jev-1.13.0 tree_hard vs gemini-3.8-flash paper_llm_low | -0.236 [-0.288, -0.182] | 7.71e-16 |
| jev-1.13.0 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.204 [-0.259, -0.148] | 7.2e-12 |
| jev-1.13.0 tree_v2 vs gemini-2.5-flash paper_llm | +0.022 [-0.034, +0.079] | 0.491 |
| jev-1.13.0 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.057 [+0.002, +0.113] | 0.0542 |
| jev-1.13.0 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.064 [-0.116, -0.015] | 0.0188 |
| jev-1.13.0 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.032 [-0.084, +0.020] | 0.271 |
| gemini-2.5-flash paper_llm vs gemini-2.5-flash paper_llm_thinking | +0.034 [-0.015, +0.084] | 0.193 |
| gemini-2.5-flash paper_llm vs gemini-3.8-flash paper_llm_low | -0.086 [-0.133, -0.039] | 0.000641 |
| gemini-2.5-flash paper_llm vs gemini-3.8-flash paper_llm_thinking | -0.054 [-0.103, -0.005] | 0.0428 |
| gemini-2.5-flash paper_llm_thinking vs gemini-3.8-flash paper_llm_low | -0.121 [-0.168, -0.071] | 2.35e-06 |
| gemini-2.5-flash paper_llm_thinking vs gemini-3.8-flash paper_llm_thinking | -0.089 [-0.135, -0.042] | 0.000355 |
| gemini-3.8-flash paper_llm_low vs gemini-3.8-flash paper_llm_thinking | +0.032 [+0.007, +0.057] | 0.0192 |

## Confusion matrices (rows = gold, columns = predicted)

**jev-1.13.0 flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 79 | 17 | 7 | 16 | 24 |
| Comp | 11 | 63 | 7 | 10 | 11 |
| Opin | 6 | 17 | 66 | 2 | 11 |
| Outd | 8 | 1 | 0 | 40 | 6 |
| Misi | 0 | 1 | 0 | 0 | 3 |

**jev-1.13.0 tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 105 | 33 | 0 | 1 | 4 |
| Comp | 21 | 81 | 0 | 0 | 0 |
| Opin | 9 | 89 | 2 | 0 | 2 |
| Outd | 17 | 31 | 0 | 3 | 4 |
| Misi | 0 | 3 | 0 | 0 | 1 |

**jev-1.13.0 tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 89 | 38 | 0 | 4 | 12 |
| Comp | 18 | 84 | 0 | 0 | 0 |
| Opin | 7 | 82 | 6 | 0 | 7 |
| Outd | 13 | 26 | 0 | 7 | 9 |
| Misi | 0 | 2 | 0 | 0 | 2 |

**jev-1.13.0 tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 106 | 15 | 16 | 4 | 2 |
| Comp | 25 | 53 | 24 | 0 | 0 |
| Opin | 13 | 1 | 88 | 0 | 0 |
| Outd | 17 | 21 | 6 | 11 | 0 |
| Misi | 1 | 1 | 1 | 1 | 0 |

**gemini-2.5-flash paper_llm**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 84 | 20 | 6 | 11 | 22 |
| Comp | 24 | 60 | 6 | 7 | 5 |
| Opin | 8 | 16 | 72 | 1 | 5 |
| Outd | 15 | 3 | 3 | 31 | 3 |
| Misi | 2 | 0 | 0 | 0 | 2 |

**gemini-2.5-flash paper_llm_thinking**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 65 | 24 | 13 | 15 | 26 |
| Comp | 11 | 60 | 10 | 10 | 11 |
| Opin | 3 | 12 | 76 | 1 | 10 |
| Outd | 10 | 4 | 0 | 30 | 11 |
| Misi | 0 | 0 | 0 | 0 | 4 |

**gemini-3.8-flash paper_llm_low**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 107 | 13 | 4 | 16 | 3 |
| Comp | 21 | 69 | 7 | 4 | 1 |
| Opin | 10 | 17 | 68 | 1 | 6 |
| Outd | 16 | 1 | 0 | 38 | 0 |
| Misi | 1 | 0 | 0 | 1 | 2 |

**gemini-3.8-flash paper_llm_thinking**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 104 | 16 | 4 | 15 | 4 |
| Comp | 22 | 62 | 8 | 7 | 3 |
| Opin | 10 | 19 | 63 | 2 | 8 |
| Outd | 15 | 1 | 0 | 39 | 0 |
| Misi | 0 | 0 | 0 | 1 | 3 |
