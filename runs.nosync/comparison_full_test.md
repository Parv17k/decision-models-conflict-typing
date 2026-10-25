# Conflict-type classification on CONFLICTS, split `test` (n = 406)

| System | Accuracy [95% CI] | 4-class acc. | Macro-F1 | ECE | Brier | NLL | Unparsed | Input tokens | $/1k queries | Latency mean / p95 (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| jev-1.13.0 flat | 0.618 [0.569, 0.665] | 0.633 | 0.549 | 0.103 | 0.534 | 1.112 | 0 | 4611 | 0.194 | 0.26 / 0.40 |
| jev-1.13.0 tree | 0.473 [0.424, 0.520] | 0.483 | 0.293 | 0.153 | 0.678 | 1.296 | 0 | 4299 | 0.181 | 0.25 / 0.35 |
| jev-1.13.0 tree_hard | 0.463 [0.416, 0.510] | 0.485 | 0.321 | – | – | – | 0 | 4299 | 0.181 | 0.25 / 0.35 |
| jev-1.13.0 tree_v2 | 0.635 [0.589, 0.682] | 0.638 | 0.459 | 0.026 | 0.488 | 0.934 | 0 | 4299 | 0.181 | 0.25 / 0.35 |
| jev-1.14.0 flat | 0.596 [0.547, 0.645] | 0.608 | 0.533 | 0.113 | 0.561 | 1.172 | 0 | 4611 | 0.194 | 0.28 / 0.40 |
| jev-1.14.0 tree | 0.451 [0.404, 0.498] | 0.461 | 0.276 | 0.193 | 0.697 | 1.327 | 0 | 4299 | 0.181 | 0.27 / 0.40 |
| jev-1.14.0 tree_hard | 0.446 [0.397, 0.495] | 0.461 | 0.310 | – | – | – | 0 | 4299 | 0.181 | 0.27 / 0.40 |
| jev-1.14.0 tree_v2 | 0.628 [0.581, 0.675] | 0.631 | 0.457 | 0.031 | 0.490 | 0.939 | 0 | 4299 | 0.181 | 0.27 / 0.40 |
| microsoft-decision-1 flat | 0.581 [0.532, 0.628] | 0.594 | 0.502 | 0.188 | 0.577 | 1.141 | 0 | 4221 | 0.177 | 0.45 / 0.63 |
| microsoft-decision-1 tree | 0.411 [0.365, 0.458] | 0.416 | 0.267 | 0.299 | 0.822 | 1.656 | 0 | 3986 | 0.167 | 0.56 / 0.74 |
| microsoft-decision-1 tree_hard | 0.382 [0.335, 0.429] | 0.392 | 0.244 | – | – | – | 0 | 3986 | 0.167 | 0.56 / 0.74 |
| microsoft-decision-1 tree_v2 | 0.574 [0.525, 0.621] | 0.576 | 0.397 | 0.115 | 0.544 | 1.039 | 0 | 3986 | 0.167 | 0.56 / 0.74 |
| d1 flat | 0.626 [0.576, 0.672] | 0.628 | 0.515 | 0.075 | 0.498 | 0.940 | 0 | 4226 | 0.085 | 0.41 / 0.56 |
| d1 tree | 0.448 [0.399, 0.498] | 0.448 | 0.319 | 0.223 | 0.730 | 1.438 | 0 | 4024 | 0.080 | 0.52 / 0.67 |
| d1 tree_hard | 0.478 [0.429, 0.527] | 0.478 | 0.393 | – | – | – | 0 | 4024 | 0.080 | 0.52 / 0.67 |
| d1 tree_v2 | 0.584 [0.537, 0.633] | 0.586 | 0.508 | 0.105 | 0.559 | 1.060 | 0 | 4024 | 0.080 | 0.52 / 0.67 |
| pplx-decider-v1.2 flat | 0.667 [0.621, 0.712] | 0.670 | 0.565 | 0.061 | 0.446 | 0.830 | 0 | 4294 | 0.086 | 0.42 / 0.59 |
| pplx-decider-v1.2 tree | 0.569 [0.520, 0.618] | 0.571 | 0.437 | 0.142 | 0.603 | 1.158 | 0 | 4114 | 0.082 | 0.40 / 0.56 |
| pplx-decider-v1.2 tree_hard | 0.586 [0.537, 0.633] | 0.591 | 0.484 | – | – | – | 0 | 4114 | 0.082 | 0.40 / 0.56 |
| pplx-decider-v1.2 tree_v2 | 0.690 [0.643, 0.734] | 0.692 | 0.555 | 0.053 | 0.449 | 0.919 | 0 | 4114 | 0.082 | 0.40 / 0.56 |
| gpt-6-luna-decisions flat | 0.663 [0.616, 0.709] | 0.663 | 0.547 | 0.059 | 0.514 | 1.067 | 0 | 4146 | 0.415 | 0.35 / 0.56 |
| gpt-6-luna-decisions tree | 0.421 [0.374, 0.468] | 0.429 | 0.193 | 0.430 | 0.946 | 2.788 | 0 | 4498 | 0.450 | 0.38 / 0.66 |
| gpt-6-luna-decisions tree_hard | 0.421 [0.374, 0.468] | 0.431 | 0.193 | – | – | – | 0 | 4498 | 0.450 | 0.38 / 0.66 |
| gpt-6-luna-decisions tree_v2 | 0.500 [0.453, 0.549] | 0.502 | 0.315 | 0.352 | 0.793 | 1.884 | 0 | 4498 | 0.450 | 0.38 / 0.66 |
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
| jev-1.14.0 flat | 0.592 | 0.633 | 0.737 | 0.613 | 0.090 |
| jev-1.14.0 tree | 0.688 | 0.460 | 0.019 | 0.069 | 0.143 |
| jev-1.14.0 tree_hard | 0.639 | 0.477 | 0.093 | 0.188 | 0.154 |
| jev-1.14.0 tree_v2 | 0.683 | 0.526 | 0.757 | 0.319 | 0.000 |
| microsoft-decision-1 flat | 0.516 | 0.585 | 0.770 | 0.594 | 0.045 |
| microsoft-decision-1 tree | 0.622 | 0.429 | 0.000 | 0.102 | 0.182 |
| microsoft-decision-1 tree_hard | 0.548 | 0.433 | 0.019 | 0.127 | 0.091 |
| microsoft-decision-1 tree_v2 | 0.635 | 0.457 | 0.741 | 0.154 | 0.000 |
| d1 flat | 0.630 | 0.584 | 0.698 | 0.662 | 0.000 |
| d1 tree | 0.635 | 0.381 | 0.000 | 0.246 | 0.333 |
| d1 tree_hard | 0.659 | 0.408 | 0.093 | 0.442 | 0.364 |
| d1 tree_v2 | 0.635 | 0.476 | 0.687 | 0.342 | 0.400 |
| pplx-decider-v1.2 flat | 0.675 | 0.594 | 0.764 | 0.672 | 0.118 |
| pplx-decider-v1.2 tree | 0.719 | 0.521 | 0.300 | 0.646 | 0.000 |
| pplx-decider-v1.2 tree_hard | 0.703 | 0.556 | 0.448 | 0.643 | 0.071 |
| pplx-decider-v1.2 tree_v2 | 0.703 | 0.615 | 0.798 | 0.660 | 0.000 |
| gpt-6-luna-decisions flat | 0.700 | 0.672 | 0.637 | 0.727 | 0.000 |
| gpt-6-luna-decisions tree | 0.601 | 0.362 | 0.000 | 0.000 | 0.000 |
| gpt-6-luna-decisions tree_hard | 0.605 | 0.358 | 0.000 | 0.000 | 0.000 |
| gpt-6-luna-decisions tree_v2 | 0.601 | 0.403 | 0.468 | 0.103 | 0.000 |
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
| jev-1.13.0 flat vs jev-1.14.0 flat | +0.022 [-0.002, +0.047] | 0.122 |
| jev-1.13.0 flat vs jev-1.14.0 tree | +0.167 [+0.108, +0.227] | 6.2e-08 |
| jev-1.13.0 flat vs jev-1.14.0 tree_hard | +0.172 [+0.113, +0.229] | 1.54e-08 |
| jev-1.13.0 flat vs jev-1.14.0 tree_v2 | -0.010 [-0.062, +0.042] | 0.783 |
| jev-1.13.0 flat vs microsoft-decision-1 flat | +0.037 [-0.007, +0.081] | 0.133 |
| jev-1.13.0 flat vs microsoft-decision-1 tree | +0.207 [+0.145, +0.268] | 1.78e-10 |
| jev-1.13.0 flat vs microsoft-decision-1 tree_hard | +0.236 [+0.177, +0.296] | 1.36e-13 |
| jev-1.13.0 flat vs microsoft-decision-1 tree_v2 | +0.044 [-0.012, +0.101] | 0.151 |
| jev-1.13.0 flat vs d1 flat | -0.007 [-0.054, +0.037] | 0.83 |
| jev-1.13.0 flat vs d1 tree | +0.170 [+0.103, +0.236] | 7.59e-07 |
| jev-1.13.0 flat vs d1 tree_hard | +0.140 [+0.081, +0.200] | 8.29e-06 |
| jev-1.13.0 flat vs d1 tree_v2 | +0.034 [-0.022, +0.094] | 0.275 |
| jev-1.13.0 flat vs pplx-decider-v1.2 flat | -0.049 [-0.091, -0.007] | 0.0308 |
| jev-1.13.0 flat vs pplx-decider-v1.2 tree | +0.049 [-0.007, +0.103] | 0.0978 |
| jev-1.13.0 flat vs pplx-decider-v1.2 tree_hard | +0.032 [-0.020, +0.081] | 0.25 |
| jev-1.13.0 flat vs pplx-decider-v1.2 tree_v2 | -0.071 [-0.118, -0.025] | 0.00346 |
| jev-1.13.0 flat vs gpt-6-luna-decisions flat | -0.044 [-0.096, +0.007] | 0.114 |
| jev-1.13.0 flat vs gpt-6-luna-decisions tree | +0.197 [+0.128, +0.266] | 7.28e-08 |
| jev-1.13.0 flat vs gpt-6-luna-decisions tree_hard | +0.197 [+0.128, +0.266] | 7.28e-08 |
| jev-1.13.0 flat vs gpt-6-luna-decisions tree_v2 | +0.118 [+0.052, +0.185] | 0.000699 |
| jev-1.13.0 flat vs gemini-2.5-flash paper_llm | +0.005 [-0.044, +0.054] | 0.922 |
| jev-1.13.0 flat vs gemini-2.5-flash paper_llm_thinking | +0.039 [-0.002, +0.081] | 0.0888 |
| jev-1.13.0 flat vs gemini-3.8-flash paper_llm_low | -0.081 [-0.123, -0.039] | 0.000317 |
| jev-1.13.0 flat vs gemini-3.8-flash paper_llm_thinking | -0.049 [-0.094, -0.007] | 0.0308 |
| jev-1.13.0 tree vs jev-1.13.0 tree_hard | +0.010 [-0.015, +0.034] | 0.572 |
| jev-1.13.0 tree vs jev-1.13.0 tree_v2 | -0.163 [-0.214, -0.111] | 4.16e-09 |
| jev-1.13.0 tree vs jev-1.14.0 flat | -0.123 [-0.187, -0.062] | 0.000185 |
| jev-1.13.0 tree vs jev-1.14.0 tree | +0.022 [+0.002, +0.042] | 0.049 |
| jev-1.13.0 tree vs jev-1.14.0 tree_hard | +0.027 [-0.002, +0.057] | 0.108 |
| jev-1.13.0 tree vs jev-1.14.0 tree_v2 | -0.155 [-0.209, -0.103] | 4.29e-08 |
| jev-1.13.0 tree vs microsoft-decision-1 flat | -0.108 [-0.175, -0.042] | 0.00174 |
| jev-1.13.0 tree vs microsoft-decision-1 tree | +0.062 [+0.027, +0.096] | 0.000802 |
| jev-1.13.0 tree vs microsoft-decision-1 tree_hard | +0.091 [+0.054, +0.131] | 4.48e-06 |
| jev-1.13.0 tree vs microsoft-decision-1 tree_v2 | -0.101 [-0.163, -0.039] | 0.00176 |
| jev-1.13.0 tree vs d1 flat | -0.153 [-0.214, -0.091] | 2.99e-06 |
| jev-1.13.0 tree vs d1 tree | +0.025 [-0.015, +0.064] | 0.282 |
| jev-1.13.0 tree vs d1 tree_hard | -0.005 [-0.047, +0.034] | 0.905 |
| jev-1.13.0 tree vs d1 tree_v2 | -0.111 [-0.165, -0.057] | 0.000134 |
| jev-1.13.0 tree vs pplx-decider-v1.2 flat | -0.195 [-0.254, -0.135] | 7.65e-10 |
| jev-1.13.0 tree vs pplx-decider-v1.2 tree | -0.096 [-0.140, -0.052] | 3.48e-05 |
| jev-1.13.0 tree vs pplx-decider-v1.2 tree_hard | -0.113 [-0.160, -0.069] | 2.87e-06 |
| jev-1.13.0 tree vs pplx-decider-v1.2 tree_v2 | -0.217 [-0.271, -0.163] | 2.34e-13 |
| jev-1.13.0 tree vs gpt-6-luna-decisions flat | -0.190 [-0.244, -0.135] | 1.37e-10 |
| jev-1.13.0 tree vs gpt-6-luna-decisions tree | +0.052 [+0.005, +0.096] | 0.0334 |
| jev-1.13.0 tree vs gpt-6-luna-decisions tree_hard | +0.052 [+0.005, +0.096] | 0.0334 |
| jev-1.13.0 tree vs gpt-6-luna-decisions tree_v2 | -0.027 [-0.081, +0.027] | 0.371 |
| jev-1.13.0 tree vs gemini-2.5-flash paper_llm | -0.140 [-0.202, -0.079] | 2.2e-05 |
| jev-1.13.0 tree vs gemini-2.5-flash paper_llm_thinking | -0.106 [-0.172, -0.042] | 0.00217 |
| jev-1.13.0 tree vs gemini-3.8-flash paper_llm_low | -0.227 [-0.281, -0.172] | 1.46e-14 |
| jev-1.13.0 tree vs gemini-3.8-flash paper_llm_thinking | -0.195 [-0.251, -0.135] | 1.98e-10 |
| jev-1.13.0 tree_hard vs jev-1.13.0 tree_v2 | -0.172 [-0.227, -0.118] | 2.56e-09 |
| jev-1.13.0 tree_hard vs jev-1.14.0 flat | -0.133 [-0.192, -0.074] | 2.09e-05 |
| jev-1.13.0 tree_hard vs jev-1.14.0 tree | +0.012 [-0.012, +0.037] | 0.442 |
| jev-1.13.0 tree_hard vs jev-1.14.0 tree_hard | +0.017 [-0.005, +0.039] | 0.21 |
| jev-1.13.0 tree_hard vs jev-1.14.0 tree_v2 | -0.165 [-0.217, -0.113] | 4.96e-09 |
| jev-1.13.0 tree_hard vs microsoft-decision-1 flat | -0.118 [-0.180, -0.057] | 0.000287 |
| jev-1.13.0 tree_hard vs microsoft-decision-1 tree | +0.052 [+0.017, +0.086] | 0.00549 |
| jev-1.13.0 tree_hard vs microsoft-decision-1 tree_hard | +0.081 [+0.044, +0.116] | 1.31e-05 |
| jev-1.13.0 tree_hard vs microsoft-decision-1 tree_v2 | -0.111 [-0.170, -0.052] | 0.000447 |
| jev-1.13.0 tree_hard vs d1 flat | -0.163 [-0.222, -0.101] | 3.81e-07 |
| jev-1.13.0 tree_hard vs d1 tree | +0.015 [-0.032, +0.062] | 0.606 |
| jev-1.13.0 tree_hard vs d1 tree_hard | -0.015 [-0.059, +0.027] | 0.576 |
| jev-1.13.0 tree_hard vs d1 tree_v2 | -0.121 [-0.177, -0.062] | 8.21e-05 |
| jev-1.13.0 tree_hard vs pplx-decider-v1.2 flat | -0.204 [-0.261, -0.145] | 1.19e-10 |
| jev-1.13.0 tree_hard vs pplx-decider-v1.2 tree | -0.106 [-0.150, -0.062] | 7.35e-06 |
| jev-1.13.0 tree_hard vs pplx-decider-v1.2 tree_hard | -0.123 [-0.170, -0.076] | 4.22e-07 |
| jev-1.13.0 tree_hard vs pplx-decider-v1.2 tree_v2 | -0.227 [-0.281, -0.172] | 2.31e-14 |
| jev-1.13.0 tree_hard vs gpt-6-luna-decisions flat | -0.200 [-0.254, -0.145] | 8.5e-12 |
| jev-1.13.0 tree_hard vs gpt-6-luna-decisions tree | +0.042 [-0.010, +0.094] | 0.135 |
| jev-1.13.0 tree_hard vs gpt-6-luna-decisions tree_hard | +0.042 [-0.010, +0.094] | 0.135 |
| jev-1.13.0 tree_hard vs gpt-6-luna-decisions tree_v2 | -0.037 [-0.094, +0.022] | 0.248 |
| jev-1.13.0 tree_hard vs gemini-2.5-flash paper_llm | -0.150 [-0.209, -0.091] | 2.69e-06 |
| jev-1.13.0 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.116 [-0.180, -0.054] | 0.000437 |
| jev-1.13.0 tree_hard vs gemini-3.8-flash paper_llm_low | -0.236 [-0.288, -0.182] | 7.71e-16 |
| jev-1.13.0 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.204 [-0.259, -0.148] | 7.2e-12 |
| jev-1.13.0 tree_v2 vs jev-1.14.0 flat | +0.039 [-0.015, +0.096] | 0.191 |
| jev-1.13.0 tree_v2 vs jev-1.14.0 tree | +0.185 [+0.131, +0.239] | 5.97e-11 |
| jev-1.13.0 tree_v2 vs jev-1.14.0 tree_hard | +0.190 [+0.135, +0.244] | 1.87e-10 |
| jev-1.13.0 tree_v2 vs jev-1.14.0 tree_v2 | +0.007 [-0.015, +0.030] | 0.664 |
| jev-1.13.0 tree_v2 vs microsoft-decision-1 flat | +0.054 [-0.005, +0.113] | 0.0819 |
| jev-1.13.0 tree_v2 vs microsoft-decision-1 tree | +0.224 [+0.165, +0.283] | 1.22e-12 |
| jev-1.13.0 tree_v2 vs microsoft-decision-1 tree_hard | +0.254 [+0.195, +0.313] | 5.91e-15 |
| jev-1.13.0 tree_v2 vs microsoft-decision-1 tree_v2 | +0.062 [+0.022, +0.101] | 0.00263 |
| jev-1.13.0 tree_v2 vs d1 flat | +0.010 [-0.047, +0.067] | 0.8 |
| jev-1.13.0 tree_v2 vs d1 tree | +0.187 [+0.131, +0.246] | 1.5e-09 |
| jev-1.13.0 tree_v2 vs d1 tree_hard | +0.158 [+0.101, +0.214] | 2.62e-07 |
| jev-1.13.0 tree_v2 vs d1 tree_v2 | +0.052 [+0.002, +0.099] | 0.0482 |
| jev-1.13.0 tree_v2 vs pplx-decider-v1.2 flat | -0.032 [-0.079, +0.015] | 0.228 |
| jev-1.13.0 tree_v2 vs pplx-decider-v1.2 tree | +0.067 [+0.010, +0.123] | 0.0305 |
| jev-1.13.0 tree_v2 vs pplx-decider-v1.2 tree_hard | +0.049 [-0.005, +0.103] | 0.0978 |
| jev-1.13.0 tree_v2 vs pplx-decider-v1.2 tree_v2 | -0.054 [-0.096, -0.012] | 0.0198 |
| jev-1.13.0 tree_v2 vs gpt-6-luna-decisions flat | -0.027 [-0.086, +0.032] | 0.413 |
| jev-1.13.0 tree_v2 vs gpt-6-luna-decisions tree | +0.214 [+0.150, +0.276] | 1.49e-10 |
| jev-1.13.0 tree_v2 vs gpt-6-luna-decisions tree_hard | +0.214 [+0.150, +0.276] | 1.49e-10 |
| jev-1.13.0 tree_v2 vs gpt-6-luna-decisions tree_v2 | +0.135 [+0.079, +0.192] | 7.74e-06 |
| jev-1.13.0 tree_v2 vs gemini-2.5-flash paper_llm | +0.022 [-0.034, +0.079] | 0.491 |
| jev-1.13.0 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.057 [+0.002, +0.113] | 0.0542 |
| jev-1.13.0 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.064 [-0.116, -0.015] | 0.0188 |
| jev-1.13.0 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.032 [-0.084, +0.020] | 0.271 |
| jev-1.14.0 flat vs jev-1.14.0 tree | +0.145 [+0.084, +0.207] | 7.55e-06 |
| jev-1.14.0 flat vs jev-1.14.0 tree_hard | +0.150 [+0.091, +0.209] | 1.47e-06 |
| jev-1.14.0 flat vs jev-1.14.0 tree_v2 | -0.032 [-0.086, +0.022] | 0.291 |
| jev-1.14.0 flat vs microsoft-decision-1 flat | +0.015 [-0.027, +0.057] | 0.567 |
| jev-1.14.0 flat vs microsoft-decision-1 tree | +0.185 [+0.123, +0.249] | 2e-08 |
| jev-1.14.0 flat vs microsoft-decision-1 tree_hard | +0.214 [+0.155, +0.273] | 2.33e-11 |
| jev-1.14.0 flat vs microsoft-decision-1 tree_v2 | +0.022 [-0.034, +0.081] | 0.504 |
| jev-1.14.0 flat vs d1 flat | -0.030 [-0.076, +0.017] | 0.241 |
| jev-1.14.0 flat vs d1 tree | +0.148 [+0.079, +0.217] | 3.2e-05 |
| jev-1.14.0 flat vs d1 tree_hard | +0.118 [+0.054, +0.182] | 0.000339 |
| jev-1.14.0 flat vs d1 tree_v2 | +0.012 [-0.047, +0.074] | 0.748 |
| jev-1.14.0 flat vs pplx-decider-v1.2 flat | -0.071 [-0.116, -0.027] | 0.00248 |
| jev-1.14.0 flat vs pplx-decider-v1.2 tree | +0.027 [-0.032, +0.086] | 0.406 |
| jev-1.14.0 flat vs pplx-decider-v1.2 tree_hard | +0.010 [-0.042, +0.062] | 0.783 |
| jev-1.14.0 flat vs pplx-decider-v1.2 tree_v2 | -0.094 [-0.143, -0.042] | 0.000371 |
| jev-1.14.0 flat vs gpt-6-luna-decisions flat | -0.067 [-0.121, -0.015] | 0.0159 |
| jev-1.14.0 flat vs gpt-6-luna-decisions tree | +0.175 [+0.103, +0.249] | 3.48e-06 |
| jev-1.14.0 flat vs gpt-6-luna-decisions tree_hard | +0.175 [+0.103, +0.249] | 3.48e-06 |
| jev-1.14.0 flat vs gpt-6-luna-decisions tree_v2 | +0.096 [+0.027, +0.165] | 0.00811 |
| jev-1.14.0 flat vs gemini-2.5-flash paper_llm | -0.017 [-0.067, +0.032] | 0.558 |
| jev-1.14.0 flat vs gemini-2.5-flash paper_llm_thinking | +0.017 [-0.025, +0.062] | 0.5 |
| jev-1.14.0 flat vs gemini-3.8-flash paper_llm_low | -0.103 [-0.148, -0.059] | 8.5e-06 |
| jev-1.14.0 flat vs gemini-3.8-flash paper_llm_thinking | -0.071 [-0.116, -0.027] | 0.00219 |
| jev-1.14.0 tree vs jev-1.14.0 tree_hard | +0.005 [-0.020, +0.030] | 0.845 |
| jev-1.14.0 tree vs jev-1.14.0 tree_v2 | -0.177 [-0.229, -0.128] | 7.47e-11 |
| jev-1.14.0 tree vs microsoft-decision-1 flat | -0.131 [-0.197, -0.064] | 0.000154 |
| jev-1.14.0 tree vs microsoft-decision-1 tree | +0.039 [+0.007, +0.071] | 0.0226 |
| jev-1.14.0 tree vs microsoft-decision-1 tree_hard | +0.069 [+0.034, +0.106] | 0.000234 |
| jev-1.14.0 tree vs microsoft-decision-1 tree_v2 | -0.123 [-0.182, -0.064] | 9.5e-05 |
| jev-1.14.0 tree vs d1 flat | -0.175 [-0.236, -0.113] | 9.73e-08 |
| jev-1.14.0 tree vs d1 tree | +0.002 [-0.039, +0.044] | 1 |
| jev-1.14.0 tree vs d1 tree_hard | -0.027 [-0.069, +0.015] | 0.254 |
| jev-1.14.0 tree vs d1 tree_v2 | -0.133 [-0.190, -0.076] | 6.82e-06 |
| jev-1.14.0 tree vs pplx-decider-v1.2 flat | -0.217 [-0.273, -0.158] | 4.48e-12 |
| jev-1.14.0 tree vs pplx-decider-v1.2 tree | -0.118 [-0.160, -0.074] | 2.77e-07 |
| jev-1.14.0 tree vs pplx-decider-v1.2 tree_hard | -0.135 [-0.182, -0.091] | 1.72e-08 |
| jev-1.14.0 tree vs pplx-decider-v1.2 tree_v2 | -0.239 [-0.293, -0.185] | 4.69e-16 |
| jev-1.14.0 tree vs gpt-6-luna-decisions flat | -0.212 [-0.266, -0.158] | 2.55e-13 |
| jev-1.14.0 tree vs gpt-6-luna-decisions tree | +0.030 [-0.017, +0.076] | 0.256 |
| jev-1.14.0 tree vs gpt-6-luna-decisions tree_hard | +0.030 [-0.017, +0.076] | 0.256 |
| jev-1.14.0 tree vs gpt-6-luna-decisions tree_v2 | -0.049 [-0.106, +0.005] | 0.0978 |
| jev-1.14.0 tree vs gemini-2.5-flash paper_llm | -0.163 [-0.224, -0.101] | 9.69e-07 |
| jev-1.14.0 tree vs gemini-2.5-flash paper_llm_thinking | -0.128 [-0.195, -0.064] | 0.000198 |
| jev-1.14.0 tree vs gemini-3.8-flash paper_llm_low | -0.249 [-0.303, -0.195] | 3.62e-17 |
| jev-1.14.0 tree vs gemini-3.8-flash paper_llm_thinking | -0.217 [-0.273, -0.160] | 1.12e-12 |
| jev-1.14.0 tree_hard vs jev-1.14.0 tree_v2 | -0.182 [-0.234, -0.130] | 1.33e-10 |
| jev-1.14.0 tree_hard vs microsoft-decision-1 flat | -0.135 [-0.200, -0.071] | 3.9e-05 |
| jev-1.14.0 tree_hard vs microsoft-decision-1 tree | +0.034 [-0.002, +0.071] | 0.0814 |
| jev-1.14.0 tree_hard vs microsoft-decision-1 tree_hard | +0.064 [+0.027, +0.101] | 0.000862 |
| jev-1.14.0 tree_hard vs microsoft-decision-1 tree_v2 | -0.128 [-0.190, -0.069] | 5.98e-05 |
| jev-1.14.0 tree_hard vs d1 flat | -0.180 [-0.241, -0.118] | 4.87e-08 |
| jev-1.14.0 tree_hard vs d1 tree | -0.002 [-0.052, +0.047] | 1 |
| jev-1.14.0 tree_hard vs d1 tree_hard | -0.032 [-0.076, +0.015] | 0.208 |
| jev-1.14.0 tree_hard vs d1 tree_v2 | -0.138 [-0.197, -0.079] | 9.9e-06 |
| jev-1.14.0 tree_hard vs pplx-decider-v1.2 flat | -0.222 [-0.281, -0.163] | 4.96e-12 |
| jev-1.14.0 tree_hard vs pplx-decider-v1.2 tree | -0.123 [-0.167, -0.076] | 3.11e-07 |
| jev-1.14.0 tree_hard vs pplx-decider-v1.2 tree_hard | -0.140 [-0.187, -0.094] | 1.01e-08 |
| jev-1.14.0 tree_hard vs pplx-decider-v1.2 tree_v2 | -0.244 [-0.298, -0.187] | 7.92e-16 |
| jev-1.14.0 tree_hard vs gpt-6-luna-decisions flat | -0.217 [-0.271, -0.163] | 2.34e-13 |
| jev-1.14.0 tree_hard vs gpt-6-luna-decisions tree | +0.025 [-0.027, +0.076] | 0.407 |
| jev-1.14.0 tree_hard vs gpt-6-luna-decisions tree_hard | +0.025 [-0.027, +0.076] | 0.407 |
| jev-1.14.0 tree_hard vs gpt-6-luna-decisions tree_v2 | -0.054 [-0.113, +0.005] | 0.0882 |
| jev-1.14.0 tree_hard vs gemini-2.5-flash paper_llm | -0.167 [-0.229, -0.106] | 3.18e-07 |
| jev-1.14.0 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.133 [-0.197, -0.069] | 6.31e-05 |
| jev-1.14.0 tree_hard vs gemini-3.8-flash paper_llm_low | -0.254 [-0.308, -0.200] | 3.95e-17 |
| jev-1.14.0 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.222 [-0.278, -0.163] | 6.62e-13 |
| jev-1.14.0 tree_v2 vs microsoft-decision-1 flat | +0.047 [-0.010, +0.106] | 0.132 |
| jev-1.14.0 tree_v2 vs microsoft-decision-1 tree | +0.217 [+0.158, +0.273] | 4.48e-12 |
| jev-1.14.0 tree_v2 vs microsoft-decision-1 tree_hard | +0.246 [+0.187, +0.305] | 1.56e-14 |
| jev-1.14.0 tree_v2 vs microsoft-decision-1 tree_v2 | +0.054 [+0.015, +0.094] | 0.00815 |
| jev-1.14.0 tree_v2 vs d1 flat | +0.002 [-0.054, +0.059] | 1 |
| jev-1.14.0 tree_v2 vs d1 tree | +0.180 [+0.121, +0.239] | 1.85e-08 |
| jev-1.14.0 tree_v2 vs d1 tree_hard | +0.150 [+0.091, +0.209] | 1.47e-06 |
| jev-1.14.0 tree_v2 vs d1 tree_v2 | +0.044 [-0.005, +0.091] | 0.101 |
| jev-1.14.0 tree_v2 vs pplx-decider-v1.2 flat | -0.039 [-0.089, +0.010] | 0.137 |
| jev-1.14.0 tree_v2 vs pplx-decider-v1.2 tree | +0.059 [+0.002, +0.116] | 0.0566 |
| jev-1.14.0 tree_v2 vs pplx-decider-v1.2 tree_hard | +0.042 [-0.012, +0.096] | 0.162 |
| jev-1.14.0 tree_v2 vs pplx-decider-v1.2 tree_v2 | -0.062 [-0.103, -0.020] | 0.00728 |
| jev-1.14.0 tree_v2 vs gpt-6-luna-decisions flat | -0.034 [-0.091, +0.022] | 0.279 |
| jev-1.14.0 tree_v2 vs gpt-6-luna-decisions tree | +0.207 [+0.143, +0.271] | 1.41e-09 |
| jev-1.14.0 tree_v2 vs gpt-6-luna-decisions tree_hard | +0.207 [+0.143, +0.271] | 1.41e-09 |
| jev-1.14.0 tree_v2 vs gpt-6-luna-decisions tree_v2 | +0.128 [+0.069, +0.187] | 3.81e-05 |
| jev-1.14.0 tree_v2 vs gemini-2.5-flash paper_llm | +0.015 [-0.042, +0.071] | 0.668 |
| jev-1.14.0 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.049 [-0.005, +0.103] | 0.0927 |
| jev-1.14.0 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.071 [-0.121, -0.022] | 0.00758 |
| jev-1.14.0 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.039 [-0.091, +0.012] | 0.167 |
| microsoft-decision-1 flat vs microsoft-decision-1 tree | +0.170 [+0.108, +0.234] | 1.93e-07 |
| microsoft-decision-1 flat vs microsoft-decision-1 tree_hard | +0.200 [+0.143, +0.256] | 3.4e-11 |
| microsoft-decision-1 flat vs microsoft-decision-1 tree_v2 | +0.007 [-0.047, +0.062] | 0.859 |
| microsoft-decision-1 flat vs d1 flat | -0.044 [-0.096, +0.005] | 0.0982 |
| microsoft-decision-1 flat vs d1 tree | +0.133 [+0.059, +0.207] | 0.000476 |
| microsoft-decision-1 flat vs d1 tree_hard | +0.103 [+0.034, +0.172] | 0.00363 |
| microsoft-decision-1 flat vs d1 tree_v2 | -0.002 [-0.069, +0.062] | 1 |
| microsoft-decision-1 flat vs pplx-decider-v1.2 flat | -0.086 [-0.138, -0.034] | 0.00171 |
| microsoft-decision-1 flat vs pplx-decider-v1.2 tree | +0.012 [-0.052, +0.074] | 0.757 |
| microsoft-decision-1 flat vs pplx-decider-v1.2 tree_hard | -0.005 [-0.062, +0.052] | 0.932 |
| microsoft-decision-1 flat vs pplx-decider-v1.2 tree_v2 | -0.108 [-0.163, -0.054] | 0.000125 |
| microsoft-decision-1 flat vs gpt-6-luna-decisions flat | -0.081 [-0.135, -0.027] | 0.00402 |
| microsoft-decision-1 flat vs gpt-6-luna-decisions tree | +0.160 [+0.086, +0.234] | 3.38e-05 |
| microsoft-decision-1 flat vs gpt-6-luna-decisions tree_hard | +0.160 [+0.086, +0.234] | 3.38e-05 |
| microsoft-decision-1 flat vs gpt-6-luna-decisions tree_v2 | +0.081 [+0.010, +0.150] | 0.0274 |
| microsoft-decision-1 flat vs gemini-2.5-flash paper_llm | -0.032 [-0.081, +0.017] | 0.241 |
| microsoft-decision-1 flat vs gemini-2.5-flash paper_llm_thinking | +0.002 [-0.042, +0.047] | 1 |
| microsoft-decision-1 flat vs gemini-3.8-flash paper_llm_low | -0.118 [-0.167, -0.069] | 3.45e-06 |
| microsoft-decision-1 flat vs gemini-3.8-flash paper_llm_thinking | -0.086 [-0.138, -0.037] | 0.00103 |
| microsoft-decision-1 tree vs microsoft-decision-1 tree_hard | +0.030 [+0.007, +0.052] | 0.0169 |
| microsoft-decision-1 tree vs microsoft-decision-1 tree_v2 | -0.163 [-0.214, -0.108] | 4.16e-09 |
| microsoft-decision-1 tree vs d1 flat | -0.214 [-0.276, -0.153] | 9.07e-11 |
| microsoft-decision-1 tree vs d1 tree | -0.037 [-0.084, +0.007] | 0.142 |
| microsoft-decision-1 tree vs d1 tree_hard | -0.067 [-0.113, -0.020] | 0.00731 |
| microsoft-decision-1 tree vs d1 tree_v2 | -0.172 [-0.229, -0.113] | 2.4e-08 |
| microsoft-decision-1 tree vs pplx-decider-v1.2 flat | -0.256 [-0.315, -0.197] | 8.04e-15 |
| microsoft-decision-1 tree vs pplx-decider-v1.2 tree | -0.158 [-0.204, -0.111] | 2.58e-10 |
| microsoft-decision-1 tree vs pplx-decider-v1.2 tree_hard | -0.175 [-0.222, -0.128] | 5.25e-12 |
| microsoft-decision-1 tree vs pplx-decider-v1.2 tree_v2 | -0.278 [-0.335, -0.222] | 4.35e-19 |
| microsoft-decision-1 tree vs gpt-6-luna-decisions flat | -0.251 [-0.305, -0.197] | 6.52e-17 |
| microsoft-decision-1 tree vs gpt-6-luna-decisions tree | -0.010 [-0.059, +0.039] | 0.769 |
| microsoft-decision-1 tree vs gpt-6-luna-decisions tree_hard | -0.010 [-0.059, +0.039] | 0.769 |
| microsoft-decision-1 tree vs gpt-6-luna-decisions tree_v2 | -0.089 [-0.148, -0.032] | 0.00339 |
| microsoft-decision-1 tree vs gemini-2.5-flash paper_llm | -0.202 [-0.266, -0.140] | 1.94e-09 |
| microsoft-decision-1 tree vs gemini-2.5-flash paper_llm_thinking | -0.167 [-0.232, -0.106] | 5.09e-07 |
| microsoft-decision-1 tree vs gemini-3.8-flash paper_llm_low | -0.288 [-0.345, -0.232] | 9.99e-20 |
| microsoft-decision-1 tree vs gemini-3.8-flash paper_llm_thinking | -0.256 [-0.315, -0.197] | 2.52e-15 |
| microsoft-decision-1 tree_hard vs microsoft-decision-1 tree_v2 | -0.192 [-0.246, -0.135] | 6.42e-11 |
| microsoft-decision-1 tree_hard vs d1 flat | -0.244 [-0.303, -0.182] | 1.05e-13 |
| microsoft-decision-1 tree_hard vs d1 tree | -0.067 [-0.118, -0.017] | 0.0132 |
| microsoft-decision-1 tree_hard vs d1 tree_hard | -0.096 [-0.145, -0.049] | 0.000206 |
| microsoft-decision-1 tree_hard vs d1 tree_v2 | -0.202 [-0.261, -0.140] | 4.99e-10 |
| microsoft-decision-1 tree_hard vs pplx-decider-v1.2 flat | -0.286 [-0.345, -0.224] | 9.24e-18 |
| microsoft-decision-1 tree_hard vs pplx-decider-v1.2 tree | -0.187 [-0.236, -0.138] | 7.27e-13 |
| microsoft-decision-1 tree_hard vs pplx-decider-v1.2 tree_hard | -0.204 [-0.254, -0.155] | 3.37e-15 |
| microsoft-decision-1 tree_hard vs pplx-decider-v1.2 tree_v2 | -0.308 [-0.365, -0.251] | 2.47e-22 |
| microsoft-decision-1 tree_hard vs gpt-6-luna-decisions flat | -0.281 [-0.337, -0.227] | 4.34e-20 |
| microsoft-decision-1 tree_hard vs gpt-6-luna-decisions tree | -0.039 [-0.094, +0.012] | 0.178 |
| microsoft-decision-1 tree_hard vs gpt-6-luna-decisions tree_hard | -0.039 [-0.094, +0.012] | 0.178 |
| microsoft-decision-1 tree_hard vs gpt-6-luna-decisions tree_v2 | -0.118 [-0.180, -0.059] | 0.000221 |
| microsoft-decision-1 tree_hard vs gemini-2.5-flash paper_llm | -0.232 [-0.291, -0.172] | 2.31e-12 |
| microsoft-decision-1 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.197 [-0.256, -0.138] | 6.64e-10 |
| microsoft-decision-1 tree_hard vs gemini-3.8-flash paper_llm_low | -0.318 [-0.374, -0.264] | 1.47e-23 |
| microsoft-decision-1 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.286 [-0.342, -0.227] | 8.35e-19 |
| microsoft-decision-1 tree_v2 vs d1 flat | -0.052 [-0.111, +0.007] | 0.103 |
| microsoft-decision-1 tree_v2 vs d1 tree | +0.126 [+0.059, +0.190] | 0.000218 |
| microsoft-decision-1 tree_v2 vs d1 tree_hard | +0.096 [+0.032, +0.160] | 0.00483 |
| microsoft-decision-1 tree_v2 vs d1 tree_v2 | -0.010 [-0.064, +0.042] | 0.791 |
| microsoft-decision-1 tree_v2 vs pplx-decider-v1.2 flat | -0.094 [-0.148, -0.039] | 0.00109 |
| microsoft-decision-1 tree_v2 vs pplx-decider-v1.2 tree | +0.005 [-0.059, +0.067] | 0.939 |
| microsoft-decision-1 tree_v2 vs pplx-decider-v1.2 tree_hard | -0.012 [-0.071, +0.044] | 0.745 |
| microsoft-decision-1 tree_v2 vs pplx-decider-v1.2 tree_v2 | -0.116 [-0.165, -0.067] | 9.45e-06 |
| microsoft-decision-1 tree_v2 vs gpt-6-luna-decisions flat | -0.089 [-0.150, -0.030] | 0.00579 |
| microsoft-decision-1 tree_v2 vs gpt-6-luna-decisions tree | +0.153 [+0.086, +0.219] | 1.25e-05 |
| microsoft-decision-1 tree_v2 vs gpt-6-luna-decisions tree_hard | +0.153 [+0.086, +0.219] | 1.25e-05 |
| microsoft-decision-1 tree_v2 vs gpt-6-luna-decisions tree_v2 | +0.074 [+0.012, +0.133] | 0.0232 |
| microsoft-decision-1 tree_v2 vs gemini-2.5-flash paper_llm | -0.039 [-0.096, +0.017] | 0.205 |
| microsoft-decision-1 tree_v2 vs gemini-2.5-flash paper_llm_thinking | -0.005 [-0.062, +0.049] | 0.931 |
| microsoft-decision-1 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.126 [-0.182, -0.071] | 1.82e-05 |
| microsoft-decision-1 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.094 [-0.150, -0.037] | 0.00194 |
| d1 flat vs d1 tree | +0.177 [+0.116, +0.236] | 2.17e-08 |
| d1 flat vs d1 tree_hard | +0.148 [+0.089, +0.204] | 1.06e-06 |
| d1 flat vs d1 tree_v2 | +0.042 [-0.010, +0.094] | 0.132 |
| d1 flat vs pplx-decider-v1.2 flat | -0.042 [-0.084, +0.002] | 0.0675 |
| d1 flat vs pplx-decider-v1.2 tree | +0.057 [+0.002, +0.111] | 0.0487 |
| d1 flat vs pplx-decider-v1.2 tree_hard | +0.039 [-0.012, +0.091] | 0.16 |
| d1 flat vs pplx-decider-v1.2 tree_v2 | -0.064 [-0.111, -0.017] | 0.00878 |
| d1 flat vs gpt-6-luna-decisions flat | -0.037 [-0.086, +0.012] | 0.172 |
| d1 flat vs gpt-6-luna-decisions tree | +0.204 [+0.143, +0.266] | 6.9e-10 |
| d1 flat vs gpt-6-luna-decisions tree_hard | +0.204 [+0.143, +0.266] | 6.9e-10 |
| d1 flat vs gpt-6-luna-decisions tree_v2 | +0.126 [+0.064, +0.182] | 5.74e-05 |
| d1 flat vs gemini-2.5-flash paper_llm | +0.012 [-0.039, +0.062] | 0.707 |
| d1 flat vs gemini-2.5-flash paper_llm_thinking | +0.047 [-0.005, +0.099] | 0.0985 |
| d1 flat vs gemini-3.8-flash paper_llm_low | -0.074 [-0.118, -0.030] | 0.00182 |
| d1 flat vs gemini-3.8-flash paper_llm_thinking | -0.042 [-0.089, +0.005] | 0.0893 |
| d1 tree vs d1 tree_hard | -0.030 [-0.059, +0.000] | 0.073 |
| d1 tree vs d1 tree_v2 | -0.135 [-0.175, -0.096] | 2.38e-11 |
| d1 tree vs pplx-decider-v1.2 flat | -0.219 [-0.276, -0.163] | 1.47e-12 |
| d1 tree vs pplx-decider-v1.2 tree | -0.121 [-0.165, -0.076] | 2.51e-07 |
| d1 tree vs pplx-decider-v1.2 tree_hard | -0.138 [-0.192, -0.086] | 5.09e-07 |
| d1 tree vs pplx-decider-v1.2 tree_v2 | -0.241 [-0.296, -0.187] | 4.78e-16 |
| d1 tree vs gpt-6-luna-decisions flat | -0.214 [-0.276, -0.155] | 5.38e-11 |
| d1 tree vs gpt-6-luna-decisions tree | +0.027 [-0.005, +0.059] | 0.135 |
| d1 tree vs gpt-6-luna-decisions tree_hard | +0.027 [-0.005, +0.059] | 0.135 |
| d1 tree vs gpt-6-luna-decisions tree_v2 | -0.052 [-0.094, -0.010] | 0.0238 |
| d1 tree vs gemini-2.5-flash paper_llm | -0.165 [-0.229, -0.101] | 1.08e-06 |
| d1 tree vs gemini-2.5-flash paper_llm_thinking | -0.131 [-0.202, -0.059] | 0.000417 |
| d1 tree vs gemini-3.8-flash paper_llm_low | -0.251 [-0.310, -0.192] | 4.23e-15 |
| d1 tree vs gemini-3.8-flash paper_llm_thinking | -0.219 [-0.278, -0.160] | 5.54e-12 |
| d1 tree_hard vs d1 tree_v2 | -0.106 [-0.148, -0.064] | 3.28e-06 |
| d1 tree_hard vs pplx-decider-v1.2 flat | -0.190 [-0.244, -0.135] | 9.89e-11 |
| d1 tree_hard vs pplx-decider-v1.2 tree | -0.091 [-0.133, -0.049] | 3.76e-05 |
| d1 tree_hard vs pplx-decider-v1.2 tree_hard | -0.108 [-0.155, -0.062] | 8.05e-06 |
| d1 tree_hard vs pplx-decider-v1.2 tree_v2 | -0.212 [-0.264, -0.160] | 2.36e-14 |
| d1 tree_hard vs gpt-6-luna-decisions flat | -0.185 [-0.241, -0.126] | 3.62e-09 |
| d1 tree_hard vs gpt-6-luna-decisions tree | +0.057 [+0.015, +0.099] | 0.0106 |
| d1 tree_hard vs gpt-6-luna-decisions tree_hard | +0.057 [+0.015, +0.099] | 0.0106 |
| d1 tree_hard vs gpt-6-luna-decisions tree_v2 | -0.022 [-0.071, +0.027] | 0.431 |
| d1 tree_hard vs gemini-2.5-flash paper_llm | -0.135 [-0.200, -0.071] | 4.32e-05 |
| d1 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.101 [-0.170, -0.034] | 0.00426 |
| d1 tree_hard vs gemini-3.8-flash paper_llm_low | -0.222 [-0.276, -0.165] | 9.21e-14 |
| d1 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.190 [-0.244, -0.133] | 1.87e-10 |
| d1 tree_v2 vs pplx-decider-v1.2 flat | -0.084 [-0.131, -0.037] | 0.00111 |
| d1 tree_v2 vs pplx-decider-v1.2 tree | +0.015 [-0.037, +0.069] | 0.648 |
| d1 tree_v2 vs pplx-decider-v1.2 tree_hard | -0.002 [-0.057, +0.052] | 1 |
| d1 tree_v2 vs pplx-decider-v1.2 tree_v2 | -0.106 [-0.153, -0.062] | 1.18e-05 |
| d1 tree_v2 vs gpt-6-luna-decisions flat | -0.079 [-0.138, -0.022] | 0.0111 |
| d1 tree_v2 vs gpt-6-luna-decisions tree | +0.163 [+0.116, +0.209] | 1.55e-10 |
| d1 tree_v2 vs gpt-6-luna-decisions tree_hard | +0.163 [+0.116, +0.209] | 1.55e-10 |
| d1 tree_v2 vs gpt-6-luna-decisions tree_v2 | +0.084 [+0.042, +0.126] | 0.000149 |
| d1 tree_v2 vs gemini-2.5-flash paper_llm | -0.030 [-0.089, +0.027] | 0.363 |
| d1 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.005 [-0.059, +0.067] | 0.939 |
| d1 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.116 [-0.167, -0.064] | 2.72e-05 |
| d1 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.084 [-0.135, -0.032] | 0.00245 |
| pplx-decider-v1.2 flat vs pplx-decider-v1.2 tree | +0.099 [+0.052, +0.145] | 9.31e-05 |
| pplx-decider-v1.2 flat vs pplx-decider-v1.2 tree_hard | +0.081 [+0.037, +0.126] | 0.000705 |
| pplx-decider-v1.2 flat vs pplx-decider-v1.2 tree_v2 | -0.022 [-0.054, +0.010] | 0.233 |
| pplx-decider-v1.2 flat vs gpt-6-luna-decisions flat | +0.005 [-0.047, +0.057] | 0.925 |
| pplx-decider-v1.2 flat vs gpt-6-luna-decisions tree | +0.246 [+0.185, +0.305] | 4.76e-14 |
| pplx-decider-v1.2 flat vs gpt-6-luna-decisions tree_hard | +0.246 [+0.185, +0.305] | 4.76e-14 |
| pplx-decider-v1.2 flat vs gpt-6-luna-decisions tree_v2 | +0.167 [+0.111, +0.222] | 2.61e-08 |
| pplx-decider-v1.2 flat vs gemini-2.5-flash paper_llm | +0.054 [+0.002, +0.106] | 0.0487 |
| pplx-decider-v1.2 flat vs gemini-2.5-flash paper_llm_thinking | +0.089 [+0.037, +0.140] | 0.00107 |
| pplx-decider-v1.2 flat vs gemini-3.8-flash paper_llm_low | -0.032 [-0.071, +0.005] | 0.136 |
| pplx-decider-v1.2 flat vs gemini-3.8-flash paper_llm_thinking | +0.000 [-0.039, +0.039] | 1 |
| pplx-decider-v1.2 tree vs pplx-decider-v1.2 tree_hard | -0.017 [-0.047, +0.012] | 0.311 |
| pplx-decider-v1.2 tree vs pplx-decider-v1.2 tree_v2 | -0.121 [-0.160, -0.081] | 2.63e-09 |
| pplx-decider-v1.2 tree vs gpt-6-luna-decisions flat | -0.094 [-0.148, -0.039] | 0.00109 |
| pplx-decider-v1.2 tree vs gpt-6-luna-decisions tree | +0.148 [+0.099, +0.200] | 2.09e-08 |
| pplx-decider-v1.2 tree vs gpt-6-luna-decisions tree_hard | +0.148 [+0.099, +0.200] | 2.09e-08 |
| pplx-decider-v1.2 tree vs gpt-6-luna-decisions tree_v2 | +0.069 [+0.012, +0.123] | 0.0193 |
| pplx-decider-v1.2 tree vs gemini-2.5-flash paper_llm | -0.044 [-0.103, +0.017] | 0.181 |
| pplx-decider-v1.2 tree vs gemini-2.5-flash paper_llm_thinking | -0.010 [-0.076, +0.054] | 0.824 |
| pplx-decider-v1.2 tree vs gemini-3.8-flash paper_llm_low | -0.131 [-0.177, -0.081] | 3.78e-07 |
| pplx-decider-v1.2 tree vs gemini-3.8-flash paper_llm_thinking | -0.099 [-0.150, -0.047] | 0.000227 |
| pplx-decider-v1.2 tree_hard vs pplx-decider-v1.2 tree_v2 | -0.103 [-0.143, -0.067] | 2.75e-07 |
| pplx-decider-v1.2 tree_hard vs gpt-6-luna-decisions flat | -0.076 [-0.126, -0.025] | 0.00455 |
| pplx-decider-v1.2 tree_hard vs gpt-6-luna-decisions tree | +0.165 [+0.108, +0.224] | 3.82e-08 |
| pplx-decider-v1.2 tree_hard vs gpt-6-luna-decisions tree_hard | +0.165 [+0.108, +0.224] | 3.82e-08 |
| pplx-decider-v1.2 tree_hard vs gpt-6-luna-decisions tree_v2 | +0.086 [+0.027, +0.145] | 0.00487 |
| pplx-decider-v1.2 tree_hard vs gemini-2.5-flash paper_llm | -0.027 [-0.084, +0.032] | 0.413 |
| pplx-decider-v1.2 tree_hard vs gemini-2.5-flash paper_llm_thinking | +0.007 [-0.052, +0.067] | 0.871 |
| pplx-decider-v1.2 tree_hard vs gemini-3.8-flash paper_llm_low | -0.113 [-0.158, -0.069] | 2.2e-06 |
| pplx-decider-v1.2 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.081 [-0.128, -0.034] | 0.00133 |
| pplx-decider-v1.2 tree_v2 vs gpt-6-luna-decisions flat | +0.027 [-0.025, +0.079] | 0.351 |
| pplx-decider-v1.2 tree_v2 vs gpt-6-luna-decisions tree | +0.268 [+0.209, +0.328] | 4.19e-17 |
| pplx-decider-v1.2 tree_v2 vs gpt-6-luna-decisions tree_hard | +0.268 [+0.209, +0.328] | 4.19e-17 |
| pplx-decider-v1.2 tree_v2 vs gpt-6-luna-decisions tree_v2 | +0.190 [+0.135, +0.244] | 7.09e-11 |
| pplx-decider-v1.2 tree_v2 vs gemini-2.5-flash paper_llm | +0.076 [+0.025, +0.128] | 0.00615 |
| pplx-decider-v1.2 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.111 [+0.057, +0.163] | 8.06e-05 |
| pplx-decider-v1.2 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.010 [-0.049, +0.030] | 0.72 |
| pplx-decider-v1.2 tree_v2 vs gemini-3.8-flash paper_llm_thinking | +0.022 [-0.020, +0.064] | 0.356 |
| gpt-6-luna-decisions flat vs gpt-6-luna-decisions tree | +0.241 [+0.182, +0.303] | 1.15e-13 |
| gpt-6-luna-decisions flat vs gpt-6-luna-decisions tree_hard | +0.241 [+0.182, +0.303] | 1.15e-13 |
| gpt-6-luna-decisions flat vs gpt-6-luna-decisions tree_v2 | +0.163 [+0.103, +0.222] | 2.26e-07 |
| gpt-6-luna-decisions flat vs gemini-2.5-flash paper_llm | +0.049 [-0.005, +0.103] | 0.0901 |
| gpt-6-luna-decisions flat vs gemini-2.5-flash paper_llm_thinking | +0.084 [+0.027, +0.143] | 0.00577 |
| gpt-6-luna-decisions flat vs gemini-3.8-flash paper_llm_low | -0.037 [-0.081, +0.007] | 0.128 |
| gpt-6-luna-decisions flat vs gemini-3.8-flash paper_llm_thinking | -0.005 [-0.052, +0.042] | 0.92 |
| gpt-6-luna-decisions tree vs gpt-6-luna-decisions tree_hard | +0.000 [+0.000, +0.000] | 1 |
| gpt-6-luna-decisions tree vs gpt-6-luna-decisions tree_v2 | -0.079 [-0.108, -0.049] | 1.86e-07 |
| gpt-6-luna-decisions tree vs gemini-2.5-flash paper_llm | -0.192 [-0.259, -0.128] | 2.98e-08 |
| gpt-6-luna-decisions tree vs gemini-2.5-flash paper_llm_thinking | -0.158 [-0.232, -0.086] | 3.44e-05 |
| gpt-6-luna-decisions tree vs gemini-3.8-flash paper_llm_low | -0.278 [-0.337, -0.217] | 1.56e-17 |
| gpt-6-luna-decisions tree vs gemini-3.8-flash paper_llm_thinking | -0.246 [-0.305, -0.185] | 6.76e-14 |
| gpt-6-luna-decisions tree_hard vs gpt-6-luna-decisions tree_v2 | -0.079 [-0.108, -0.049] | 1.86e-07 |
| gpt-6-luna-decisions tree_hard vs gemini-2.5-flash paper_llm | -0.192 [-0.259, -0.128] | 2.98e-08 |
| gpt-6-luna-decisions tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.158 [-0.232, -0.086] | 3.44e-05 |
| gpt-6-luna-decisions tree_hard vs gemini-3.8-flash paper_llm_low | -0.278 [-0.337, -0.217] | 1.56e-17 |
| gpt-6-luna-decisions tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.246 [-0.305, -0.185] | 6.76e-14 |
| gpt-6-luna-decisions tree_v2 vs gemini-2.5-flash paper_llm | -0.113 [-0.175, -0.052] | 0.00052 |
| gpt-6-luna-decisions tree_v2 vs gemini-2.5-flash paper_llm_thinking | -0.079 [-0.148, -0.012] | 0.0289 |
| gpt-6-luna-decisions tree_v2 vs gemini-3.8-flash paper_llm_low | -0.200 [-0.256, -0.140] | 1.55e-10 |
| gpt-6-luna-decisions tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.167 [-0.227, -0.108] | 9.23e-08 |
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

**jev-1.14.0 flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 69 | 15 | 5 | 25 | 29 |
| Comp | 10 | 62 | 6 | 12 | 12 |
| Opin | 4 | 15 | 66 | 3 | 14 |
| Outd | 7 | 1 | 0 | 42 | 5 |
| Misi | 0 | 1 | 0 | 0 | 3 |

**jev-1.14.0 tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 98 | 41 | 0 | 1 | 3 |
| Comp | 21 | 81 | 0 | 0 | 0 |
| Opin | 6 | 93 | 1 | 0 | 2 |
| Outd | 17 | 32 | 0 | 2 | 4 |
| Misi | 0 | 3 | 0 | 0 | 1 |

**jev-1.14.0 tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 84 | 49 | 0 | 2 | 8 |
| Comp | 18 | 84 | 0 | 0 | 0 |
| Opin | 4 | 86 | 5 | 1 | 6 |
| Outd | 14 | 29 | 0 | 6 | 6 |
| Misi | 0 | 2 | 0 | 0 | 2 |

**jev-1.14.0 tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 100 | 24 | 15 | 2 | 2 |
| Comp | 24 | 55 | 23 | 0 | 0 |
| Opin | 9 | 4 | 89 | 0 | 0 |
| Outd | 17 | 21 | 6 | 11 | 0 |
| Misi | 0 | 3 | 0 | 1 | 0 |

**microsoft-decision-1 flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 56 | 34 | 7 | 24 | 22 |
| Comp | 9 | 69 | 6 | 11 | 7 |
| Opin | 1 | 24 | 72 | 0 | 5 |
| Outd | 8 | 4 | 0 | 38 | 5 |
| Misi | 0 | 3 | 0 | 0 | 1 |

**microsoft-decision-1 tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 83 | 56 | 0 | 1 | 3 |
| Comp | 21 | 80 | 0 | 0 | 1 |
| Opin | 7 | 95 | 0 | 0 | 0 |
| Outd | 13 | 37 | 0 | 3 | 2 |
| Misi | 0 | 3 | 0 | 0 | 1 |

**microsoft-decision-1 tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 66 | 63 | 0 | 4 | 10 |
| Comp | 18 | 83 | 0 | 0 | 1 |
| Opin | 6 | 93 | 1 | 0 | 2 |
| Outd | 8 | 39 | 0 | 4 | 4 |
| Misi | 0 | 3 | 0 | 0 | 1 |

**microsoft-decision-1 tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 87 | 34 | 16 | 5 | 1 |
| Comp | 23 | 51 | 27 | 0 | 1 |
| Opin | 7 | 5 | 90 | 0 | 0 |
| Outd | 14 | 29 | 6 | 5 | 1 |
| Misi | 0 | 2 | 2 | 0 | 0 |

**d1 flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 96 | 13 | 5 | 23 | 6 |
| Comp | 34 | 54 | 3 | 10 | 1 |
| Opin | 20 | 15 | 59 | 2 | 6 |
| Outd | 9 | 1 | 0 | 45 | 0 |
| Misi | 3 | 0 | 0 | 1 | 0 |

**d1 tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 128 | 13 | 0 | 2 | 0 |
| Comp | 57 | 45 | 0 | 0 | 0 |
| Opin | 42 | 59 | 0 | 0 | 1 |
| Outd | 31 | 16 | 0 | 8 | 0 |
| Misi | 2 | 1 | 0 | 0 | 1 |

**d1 tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 116 | 12 | 1 | 10 | 4 |
| Comp | 49 | 52 | 0 | 1 | 0 |
| Opin | 26 | 69 | 5 | 1 | 1 |
| Outd | 17 | 19 | 0 | 19 | 0 |
| Misi | 1 | 1 | 0 | 0 | 2 |

**d1 tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 126 | 9 | 2 | 6 | 0 |
| Comp | 58 | 40 | 3 | 1 | 0 |
| Opin | 41 | 4 | 57 | 0 | 0 |
| Outd | 27 | 13 | 2 | 13 | 0 |
| Misi | 2 | 0 | 0 | 1 | 1 |

**pplx-decider-v1.2 flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 105 | 9 | 9 | 17 | 3 |
| Comp | 34 | 49 | 7 | 8 | 4 |
| Opin | 15 | 5 | 73 | 4 | 5 |
| Outd | 12 | 0 | 0 | 43 | 0 |
| Misi | 2 | 0 | 0 | 1 | 1 |

**pplx-decider-v1.2 tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 114 | 19 | 0 | 6 | 4 |
| Comp | 29 | 67 | 0 | 3 | 3 |
| Opin | 15 | 59 | 18 | 2 | 8 |
| Outd | 15 | 8 | 0 | 32 | 0 |
| Misi | 1 | 2 | 0 | 1 | 0 |

**pplx-decider-v1.2 tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 102 | 21 | 1 | 12 | 7 |
| Comp | 24 | 69 | 1 | 4 | 4 |
| Opin | 12 | 45 | 30 | 4 | 11 |
| Outd | 9 | 9 | 0 | 36 | 1 |
| Misi | 0 | 2 | 0 | 1 | 1 |

**pplx-decider-v1.2 tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 111 | 17 | 4 | 9 | 2 |
| Comp | 31 | 59 | 7 | 3 | 2 |
| Opin | 18 | 4 | 75 | 3 | 2 |
| Outd | 12 | 8 | 0 | 35 | 0 |
| Misi | 1 | 2 | 0 | 1 | 0 |

**gpt-6-luna-decisions flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 98 | 25 | 4 | 12 | 4 |
| Comp | 15 | 80 | 3 | 3 | 1 |
| Opin | 7 | 29 | 51 | 0 | 15 |
| Outd | 13 | 2 | 0 | 40 | 0 |
| Misi | 4 | 0 | 0 | 0 | 0 |

**gpt-6-luna-decisions tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 135 | 8 | 0 | 0 | 0 |
| Comp | 66 | 36 | 0 | 0 | 0 |
| Opin | 68 | 34 | 0 | 0 | 0 |
| Outd | 33 | 19 | 0 | 0 | 3 |
| Misi | 4 | 0 | 0 | 0 | 0 |

**gpt-6-luna-decisions tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 135 | 8 | 0 | 0 | 0 |
| Comp | 66 | 36 | 0 | 0 | 0 |
| Opin | 66 | 36 | 0 | 0 | 0 |
| Outd | 32 | 19 | 0 | 0 | 4 |
| Misi | 4 | 0 | 0 | 0 | 0 |

**gpt-6-luna-decisions tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 135 | 6 | 2 | 0 | 0 |
| Comp | 66 | 32 | 4 | 0 | 0 |
| Opin | 68 | 1 | 33 | 0 | 0 |
| Outd | 33 | 18 | 0 | 3 | 1 |
| Misi | 4 | 0 | 0 | 0 | 0 |

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
