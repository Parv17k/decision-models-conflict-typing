# Conflict-type classification on CONFLICTS, split `all` (n = 458)

| System | Accuracy [95% CI] | 4-class acc. | Macro-F1 | ECE | Brier | NLL | Unparsed | Input tokens | $/1k queries | Latency mean / p95 (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| jev-1.13.0 flat | 0.609 [0.563, 0.653] | 0.622 | 0.539 | 0.109 | 0.538 | 1.109 | 0 | 4612 | 0.194 | 0.26 / 0.40 |
| jev-1.13.0 tree | 0.474 [0.428, 0.517] | 0.483 | 0.291 | 0.150 | 0.677 | 1.300 | 0 | 4300 | 0.181 | 0.25 / 0.37 |
| jev-1.13.0 tree_hard | 0.461 [0.415, 0.507] | 0.480 | 0.324 | – | – | – | 0 | 4300 | 0.181 | 0.25 / 0.37 |
| jev-1.13.0 tree_v2 | 0.635 [0.592, 0.677] | 0.638 | 0.459 | 0.036 | 0.492 | 0.944 | 0 | 4300 | 0.181 | 0.25 / 0.37 |
| gemini-2.5-flash paper_llm | 0.607 [0.561, 0.651] | 0.614 | 0.523 | – | – | – | 0 | 4357 | 1.655 | 1.56 / 2.17 |
| gemini-2.5-flash paper_llm_thinking | 0.581 [0.535, 0.627] | 0.605 | 0.518 | – | – | – | 0 | 4357 | 6.068 | 9.62 / 17.95 |
| gemini-3.8-flash paper_llm_low | 0.690 [0.646, 0.731] | 0.692 | 0.596 | – | – | – | 0 | 4357 | 3.641 | 2.20 / 3.08 |
| gemini-3.8-flash paper_llm_thinking | 0.666 [0.622, 0.707] | 0.668 | 0.598 | – | – | – | 0 | 4357 | 5.545 | 5.07 / 9.84 |
| Gemini 2.5 Flash, as published (paper Table 4) | 0.653 | – | – | – | – | – | – | – | – | – |

4-class accuracy merges Outdated and Misinformation, as the paper does for behaviour.
Hard-label systems (paper_llm, tree_hard) have no probabilities, so calibration is not defined.
Unparsed answers count as wrong. tree_hard and tree_v2 reuse the tree's calls (same cost and latency).

## Per-class F1

| System | no_conflict | complementary | conflicting_opinions | outdated | misinformation |
|---|---|---|---|---|---|
| jev-1.13.0 flat | 0.638 | 0.634 | 0.700 | 0.633 | 0.088 |
| jev-1.13.0 tree | 0.709 | 0.486 | 0.034 | 0.119 | 0.105 |
| jev-1.13.0 tree_hard | 0.649 | 0.507 | 0.099 | 0.213 | 0.154 |
| jev-1.13.0 tree_v2 | 0.694 | 0.557 | 0.746 | 0.296 | 0.000 |
| gemini-2.5-flash paper_llm | 0.614 | 0.590 | 0.737 | 0.579 | 0.093 |
| gemini-2.5-flash paper_llm_thinking | 0.559 | 0.594 | 0.749 | 0.551 | 0.139 |
| gemini-3.8-flash paper_llm_low | 0.714 | 0.684 | 0.726 | 0.656 | 0.200 |
| gemini-3.8-flash paper_llm_thinking | 0.701 | 0.637 | 0.697 | 0.657 | 0.296 |

## Paired comparisons (same queries)

| A vs B | Acc. A − B [95% CI] | McNemar p |
|---|---|---|
| jev-1.13.0 flat vs jev-1.13.0 tree | +0.135 [+0.081, +0.190] | 3.42e-06 |
| jev-1.13.0 flat vs jev-1.13.0 tree_hard | +0.148 [+0.096, +0.201] | 1.12e-07 |
| jev-1.13.0 flat vs jev-1.13.0 tree_v2 | -0.026 [-0.079, +0.024] | 0.349 |
| jev-1.13.0 flat vs gemini-2.5-flash paper_llm | +0.002 [-0.044, +0.048] | 1 |
| jev-1.13.0 flat vs gemini-2.5-flash paper_llm_thinking | +0.028 [-0.013, +0.068] | 0.208 |
| jev-1.13.0 flat vs gemini-3.8-flash paper_llm_low | -0.081 [-0.120, -0.041] | 0.00011 |
| jev-1.13.0 flat vs gemini-3.8-flash paper_llm_thinking | -0.057 [-0.096, -0.017] | 0.00805 |
| jev-1.13.0 tree vs jev-1.13.0 tree_hard | +0.013 [-0.011, +0.037] | 0.377 |
| jev-1.13.0 tree vs jev-1.13.0 tree_v2 | -0.162 [-0.212, -0.114] | 4.86e-10 |
| jev-1.13.0 tree vs gemini-2.5-flash paper_llm | -0.133 [-0.192, -0.076] | 1.34e-05 |
| jev-1.13.0 tree vs gemini-2.5-flash paper_llm_thinking | -0.107 [-0.168, -0.046] | 0.000908 |
| jev-1.13.0 tree vs gemini-3.8-flash paper_llm_low | -0.216 [-0.266, -0.166] | 2.02e-15 |
| jev-1.13.0 tree vs gemini-3.8-flash paper_llm_thinking | -0.192 [-0.245, -0.140] | 1.15e-11 |
| jev-1.13.0 tree_hard vs jev-1.13.0 tree_v2 | -0.175 [-0.225, -0.124] | 1.75e-10 |
| jev-1.13.0 tree_hard vs gemini-2.5-flash paper_llm | -0.146 [-0.201, -0.090] | 9.38e-07 |
| jev-1.13.0 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.120 [-0.177, -0.063] | 9.18e-05 |
| jev-1.13.0 tree_hard vs gemini-3.8-flash paper_llm_low | -0.229 [-0.279, -0.179] | 6.88e-17 |
| jev-1.13.0 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.205 [-0.258, -0.155] | 1.1e-13 |
| jev-1.13.0 tree_v2 vs gemini-2.5-flash paper_llm | +0.028 [-0.024, +0.081] | 0.332 |
| jev-1.13.0 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.055 [+0.002, +0.107] | 0.0459 |
| jev-1.13.0 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.055 [-0.103, -0.004] | 0.0356 |
| jev-1.13.0 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.031 [-0.081, +0.020] | 0.265 |
| gemini-2.5-flash paper_llm vs gemini-2.5-flash paper_llm_thinking | +0.026 [-0.020, +0.072] | 0.303 |
| gemini-2.5-flash paper_llm vs gemini-3.8-flash paper_llm_low | -0.083 [-0.127, -0.039] | 0.000371 |
| gemini-2.5-flash paper_llm vs gemini-3.8-flash paper_llm_thinking | -0.059 [-0.105, -0.013] | 0.0168 |
| gemini-2.5-flash paper_llm_thinking vs gemini-3.8-flash paper_llm_low | -0.109 [-0.157, -0.063] | 8.27e-06 |
| gemini-2.5-flash paper_llm_thinking vs gemini-3.8-flash paper_llm_thinking | -0.085 [-0.131, -0.041] | 0.00031 |
| gemini-3.8-flash paper_llm_low vs gemini-3.8-flash paper_llm_thinking | +0.024 [+0.000, +0.048] | 0.0801 |

## Confusion matrices (rows = gold, columns = predicted)

**jev-1.13.0 flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 89 | 18 | 8 | 20 | 26 |
| Comp | 11 | 72 | 8 | 11 | 13 |
| Opin | 7 | 20 | 71 | 2 | 15 |
| Outd | 11 | 1 | 0 | 44 | 6 |
| Misi | 0 | 1 | 1 | 0 | 3 |

**jev-1.13.0 tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 117 | 36 | 0 | 1 | 7 |
| Comp | 22 | 93 | 0 | 0 | 0 |
| Opin | 10 | 101 | 2 | 0 | 2 |
| Outd | 20 | 34 | 0 | 4 | 4 |
| Misi | 0 | 4 | 0 | 0 | 1 |

**jev-1.13.0 tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 98 | 43 | 0 | 5 | 15 |
| Comp | 19 | 96 | 0 | 0 | 0 |
| Opin | 8 | 94 | 6 | 0 | 7 |
| Outd | 16 | 29 | 0 | 8 | 9 |
| Misi | 0 | 2 | 0 | 0 | 3 |

**jev-1.13.0 tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 118 | 17 | 17 | 6 | 3 |
| Comp | 26 | 61 | 28 | 0 | 0 |
| Opin | 14 | 1 | 100 | 0 | 0 |
| Outd | 20 | 24 | 6 | 12 | 0 |
| Misi | 1 | 1 | 2 | 1 | 0 |

**gemini-2.5-flash paper_llm**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 97 | 21 | 6 | 14 | 23 |
| Comp | 26 | 67 | 8 | 9 | 5 |
| Opin | 11 | 21 | 77 | 1 | 5 |
| Outd | 18 | 3 | 3 | 35 | 3 |
| Misi | 3 | 0 | 0 | 0 | 2 |

**gemini-2.5-flash paper_llm_thinking**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 73 | 26 | 15 | 19 | 28 |
| Comp | 12 | 68 | 12 | 10 | 13 |
| Opin | 3 | 16 | 85 | 1 | 10 |
| Outd | 12 | 4 | 0 | 35 | 11 |
| Misi | 0 | 0 | 0 | 0 | 5 |

**gemini-3.8-flash paper_llm_low**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 121 | 13 | 5 | 17 | 5 |
| Comp | 22 | 78 | 8 | 5 | 2 |
| Opin | 14 | 21 | 73 | 1 | 6 |
| Outd | 19 | 1 | 0 | 42 | 0 |
| Misi | 2 | 0 | 0 | 1 | 2 |

**gemini-3.8-flash paper_llm_thinking**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 116 | 16 | 5 | 17 | 7 |
| Comp | 23 | 72 | 9 | 8 | 3 |
| Opin | 14 | 22 | 69 | 2 | 8 |
| Outd | 17 | 1 | 0 | 44 | 0 |
| Misi | 0 | 0 | 0 | 1 | 4 |
