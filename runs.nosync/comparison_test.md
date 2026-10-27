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
| pplx-decider-v1.2 flat | 0.667 [0.621, 0.712] | 0.670 | 0.565 | 0.061 | 0.446 | 0.830 | 0 | 4294 | 0.086 | 0.42 / 0.59 |
| pplx-decider-v1.2 tree | 0.569 [0.520, 0.618] | 0.571 | 0.437 | 0.142 | 0.603 | 1.158 | 0 | 4114 | 0.082 | 0.40 / 0.56 |
| pplx-decider-v1.2 tree_hard | 0.586 [0.537, 0.633] | 0.591 | 0.484 | – | – | – | 0 | 4114 | 0.082 | 0.40 / 0.56 |
| pplx-decider-v1.2 tree_v2 | 0.690 [0.643, 0.734] | 0.692 | 0.555 | 0.053 | 0.449 | 0.919 | 0 | 4114 | 0.082 | 0.40 / 0.56 |
| pplx-decider-flash-v1.2 flat | 0.618 [0.571, 0.665] | 0.621 | 0.494 | 0.031 | 0.523 | 1.015 | 0 | 4294 | 0.043 | 0.31 / 0.45 |
| pplx-decider-flash-v1.2 tree | 0.466 [0.419, 0.515] | 0.473 | 0.311 | 0.159 | 0.696 | 1.387 | 0 | 19619 | 0.196 | 0.49 / 0.74 |
| pplx-decider-flash-v1.2 tree_hard | 0.483 [0.433, 0.530] | 0.493 | 0.364 | – | – | – | 0 | 19619 | 0.196 | 0.49 / 0.74 |
| pplx-decider-flash-v1.2 tree_v2 | 0.591 [0.544, 0.638] | 0.596 | 0.455 | 0.089 | 0.549 | 1.027 | 0 | 19619 | 0.196 | 0.49 / 0.74 |
| gpt-6-luna-decisions flat | 0.663 [0.616, 0.709] | 0.663 | 0.547 | 0.059 | 0.514 | 1.067 | 0 | 4146 | 0.415 | 0.35 / 0.56 |
| gpt-6-luna-decisions tree | 0.421 [0.374, 0.468] | 0.429 | 0.193 | 0.430 | 0.946 | 2.788 | 0 | 4498 | 0.450 | 0.38 / 0.66 |
| gpt-6-luna-decisions tree_hard | 0.421 [0.374, 0.468] | 0.431 | 0.193 | – | – | – | 0 | 4498 | 0.450 | 0.38 / 0.66 |
| gpt-6-luna-decisions tree_v2 | 0.500 [0.453, 0.549] | 0.502 | 0.315 | 0.352 | 0.793 | 1.884 | 0 | 4498 | 0.450 | 0.38 / 0.66 |
| d1 flat | 0.626 [0.576, 0.672] | 0.628 | 0.515 | 0.075 | 0.498 | 0.940 | 0 | 4226 | 0.085 | 0.41 / 0.56 |
| d1 tree | 0.448 [0.399, 0.498] | 0.448 | 0.319 | 0.223 | 0.730 | 1.438 | 0 | 4024 | 0.080 | 0.52 / 0.67 |
| d1 tree_hard | 0.478 [0.429, 0.527] | 0.478 | 0.393 | – | – | – | 0 | 4024 | 0.080 | 0.52 / 0.67 |
| d1 tree_v2 | 0.584 [0.537, 0.633] | 0.586 | 0.508 | 0.105 | 0.559 | 1.060 | 0 | 4024 | 0.080 | 0.52 / 0.67 |
| d1-ultra flat | 0.670 [0.623, 0.714] | 0.672 | 0.535 | 0.044 | 0.431 | 0.785 | 0 | 4226 | 0.178 | 0.46 / 0.72 |
| d1-ultra tree | 0.502 [0.453, 0.552] | 0.507 | 0.332 | 0.115 | 0.606 | 1.133 | 0 | 4024 | 0.169 | 0.49 / 0.81 |
| d1-ultra tree_hard | 0.564 [0.515, 0.613] | 0.571 | 0.443 | – | – | – | 0 | 4024 | 0.169 | 0.49 / 0.81 |
| d1-ultra tree_v2 | 0.628 [0.581, 0.675] | 0.633 | 0.478 | 0.082 | 0.506 | 0.958 | 0 | 4024 | 0.169 | 0.49 / 0.81 |
| microsoft-decision-1 flat | 0.581 [0.532, 0.628] | 0.594 | 0.502 | 0.188 | 0.577 | 1.141 | 0 | 4221 | 0.177 | 0.45 / 0.63 |
| microsoft-decision-1 tree | 0.411 [0.365, 0.458] | 0.416 | 0.267 | 0.299 | 0.822 | 1.656 | 0 | 3986 | 0.167 | 0.56 / 0.74 |
| microsoft-decision-1 tree_hard | 0.382 [0.335, 0.429] | 0.392 | 0.244 | – | – | – | 0 | 3986 | 0.167 | 0.56 / 0.74 |
| microsoft-decision-1 tree_v2 | 0.574 [0.525, 0.621] | 0.576 | 0.397 | 0.115 | 0.544 | 1.039 | 0 | 3986 | 0.167 | 0.56 / 0.74 |
| elephant-1 flat | 0.653 [0.608, 0.697] | 0.655 | 0.516 | 0.040 | 0.468 | 0.876 | 0 | 4305 | 0.000 | 0.48 / 0.60 |
| elephant-1 tree | 0.470 [0.424, 0.520] | 0.473 | 0.247 | 0.161 | 0.692 | 1.354 | 0 | 4251 | 0.000 | 0.41 / 0.61 |
| elephant-1 tree_hard | 0.507 [0.458, 0.554] | 0.515 | 0.376 | – | – | – | 0 | 4251 | 0.000 | 0.41 / 0.61 |
| elephant-1 tree_v2 | 0.594 [0.547, 0.640] | 0.596 | 0.413 | 0.063 | 0.549 | 1.024 | 0 | 4251 | 0.000 | 0.41 / 0.61 |
| mammoth-1 flat | 0.658 [0.611, 0.704] | 0.660 | 0.529 | 0.052 | 0.467 | 0.865 | 0 | 4305 | 0.000 | 0.59 / 0.84 |
| mammoth-1 tree | 0.483 [0.436, 0.532] | 0.488 | 0.308 | 0.154 | 0.655 | 1.246 | 0 | 4251 | 0.000 | 0.61 / 0.92 |
| mammoth-1 tree_hard | 0.525 [0.475, 0.574] | 0.542 | 0.401 | – | – | – | 0 | 4251 | 0.000 | 0.61 / 0.92 |
| mammoth-1 tree_v2 | 0.591 [0.544, 0.638] | 0.594 | 0.436 | 0.122 | 0.555 | 1.047 | 0 | 4251 | 0.000 | 0.61 / 0.92 |
| scaledown-classify-1 flat | 0.500 [0.451, 0.549] | 0.500 | 0.374 | 0.090 | 0.646 | 1.291 | 0 | 4758 | 0.238 | 0.72 / 1.53 |
| scaledown-classify-1 tree | 0.372 [0.325, 0.419] | 0.372 | 0.143 | 0.123 | 0.766 | 1.503 | 0 | 20043 | 1.002 | 0.74 / 1.56 |
| scaledown-classify-1 tree_hard | 0.330 [0.286, 0.374] | 0.330 | 0.209 | – | – | – | 0 | 20043 | 1.002 | 0.74 / 1.56 |
| scaledown-classify-1 tree_v2 | 0.399 [0.352, 0.448] | 0.399 | 0.179 | 0.095 | 0.690 | 1.286 | 0 | 20043 | 1.002 | 0.74 / 1.56 |
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
| pplx-decider-v1.2 flat | 0.675 | 0.594 | 0.764 | 0.672 | 0.118 |
| pplx-decider-v1.2 tree | 0.719 | 0.521 | 0.300 | 0.646 | 0.000 |
| pplx-decider-v1.2 tree_hard | 0.703 | 0.556 | 0.448 | 0.643 | 0.071 |
| pplx-decider-v1.2 tree_v2 | 0.703 | 0.615 | 0.798 | 0.660 | 0.000 |
| pplx-decider-flash-v1.2 flat | 0.669 | 0.536 | 0.691 | 0.577 | 0.000 |
| pplx-decider-flash-v1.2 tree | 0.635 | 0.441 | 0.000 | 0.384 | 0.095 |
| pplx-decider-flash-v1.2 tree_hard | 0.625 | 0.491 | 0.093 | 0.556 | 0.054 |
| pplx-decider-flash-v1.2 tree_v2 | 0.634 | 0.547 | 0.659 | 0.434 | 0.000 |
| gpt-6-luna-decisions flat | 0.700 | 0.672 | 0.637 | 0.727 | 0.000 |
| gpt-6-luna-decisions tree | 0.601 | 0.362 | 0.000 | 0.000 | 0.000 |
| gpt-6-luna-decisions tree_hard | 0.605 | 0.358 | 0.000 | 0.000 | 0.000 |
| gpt-6-luna-decisions tree_v2 | 0.601 | 0.403 | 0.468 | 0.103 | 0.000 |
| d1 flat | 0.630 | 0.584 | 0.698 | 0.662 | 0.000 |
| d1 tree | 0.635 | 0.381 | 0.000 | 0.246 | 0.333 |
| d1 tree_hard | 0.659 | 0.408 | 0.093 | 0.442 | 0.364 |
| d1 tree_v2 | 0.635 | 0.476 | 0.687 | 0.342 | 0.400 |
| d1-ultra flat | 0.692 | 0.573 | 0.782 | 0.627 | 0.000 |
| d1-ultra tree | 0.674 | 0.440 | 0.254 | 0.290 | 0.000 |
| d1-ultra tree_hard | 0.707 | 0.524 | 0.415 | 0.568 | 0.000 |
| d1-ultra tree_v2 | 0.662 | 0.483 | 0.776 | 0.468 | 0.000 |
| microsoft-decision-1 flat | 0.516 | 0.585 | 0.770 | 0.594 | 0.045 |
| microsoft-decision-1 tree | 0.622 | 0.429 | 0.000 | 0.102 | 0.182 |
| microsoft-decision-1 tree_hard | 0.548 | 0.433 | 0.019 | 0.127 | 0.091 |
| microsoft-decision-1 tree_v2 | 0.635 | 0.457 | 0.741 | 0.154 | 0.000 |
| elephant-1 flat | 0.696 | 0.595 | 0.702 | 0.585 | 0.000 |
| elephant-1 tree | 0.646 | 0.469 | 0.019 | 0.102 | 0.000 |
| elephant-1 tree_hard | 0.670 | 0.500 | 0.195 | 0.347 | 0.167 |
| elephant-1 tree_v2 | 0.657 | 0.513 | 0.678 | 0.219 | 0.000 |
| mammoth-1 flat | 0.689 | 0.545 | 0.785 | 0.625 | 0.000 |
| mammoth-1 tree | 0.626 | 0.435 | 0.269 | 0.212 | 0.000 |
| mammoth-1 tree_hard | 0.658 | 0.458 | 0.459 | 0.432 | 0.000 |
| mammoth-1 tree_v2 | 0.649 | 0.428 | 0.705 | 0.400 | 0.000 |
| scaledown-classify-1 flat | 0.600 | 0.423 | 0.573 | 0.275 | 0.000 |
| scaledown-classify-1 tree | 0.549 | 0.166 | 0.000 | 0.000 | 0.000 |
| scaledown-classify-1 tree_hard | 0.463 | 0.340 | 0.157 | 0.083 | 0.000 |
| scaledown-classify-1 tree_v2 | 0.544 | 0.070 | 0.283 | 0.000 | 0.000 |
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
| jev-1.13.0 flat vs pplx-decider-v1.2 flat | -0.049 [-0.091, -0.007] | 0.0308 |
| jev-1.13.0 flat vs pplx-decider-v1.2 tree | +0.049 [-0.007, +0.103] | 0.0978 |
| jev-1.13.0 flat vs pplx-decider-v1.2 tree_hard | +0.032 [-0.020, +0.081] | 0.25 |
| jev-1.13.0 flat vs pplx-decider-v1.2 tree_v2 | -0.071 [-0.118, -0.025] | 0.00346 |
| jev-1.13.0 flat vs pplx-decider-flash-v1.2 flat | +0.000 [-0.052, +0.052] | 1 |
| jev-1.13.0 flat vs pplx-decider-flash-v1.2 tree | +0.153 [+0.089, +0.217] | 5.69e-06 |
| jev-1.13.0 flat vs pplx-decider-flash-v1.2 tree_hard | +0.135 [+0.074, +0.197] | 2.51e-05 |
| jev-1.13.0 flat vs pplx-decider-flash-v1.2 tree_v2 | +0.027 [-0.030, +0.084] | 0.4 |
| jev-1.13.0 flat vs gpt-6-luna-decisions flat | -0.044 [-0.096, +0.007] | 0.114 |
| jev-1.13.0 flat vs gpt-6-luna-decisions tree | +0.197 [+0.128, +0.266] | 7.28e-08 |
| jev-1.13.0 flat vs gpt-6-luna-decisions tree_hard | +0.197 [+0.128, +0.266] | 7.28e-08 |
| jev-1.13.0 flat vs gpt-6-luna-decisions tree_v2 | +0.118 [+0.052, +0.185] | 0.000699 |
| jev-1.13.0 flat vs d1 flat | -0.007 [-0.054, +0.037] | 0.83 |
| jev-1.13.0 flat vs d1 tree | +0.170 [+0.103, +0.236] | 7.59e-07 |
| jev-1.13.0 flat vs d1 tree_hard | +0.140 [+0.081, +0.200] | 8.29e-06 |
| jev-1.13.0 flat vs d1 tree_v2 | +0.034 [-0.022, +0.094] | 0.275 |
| jev-1.13.0 flat vs d1-ultra flat | -0.052 [-0.099, -0.005] | 0.0354 |
| jev-1.13.0 flat vs d1-ultra tree | +0.116 [+0.052, +0.180] | 0.000472 |
| jev-1.13.0 flat vs d1-ultra tree_hard | +0.054 [-0.002, +0.111] | 0.0693 |
| jev-1.13.0 flat vs d1-ultra tree_v2 | -0.010 [-0.069, +0.049] | 0.801 |
| jev-1.13.0 flat vs microsoft-decision-1 flat | +0.037 [-0.007, +0.081] | 0.133 |
| jev-1.13.0 flat vs microsoft-decision-1 tree | +0.207 [+0.145, +0.268] | 1.78e-10 |
| jev-1.13.0 flat vs microsoft-decision-1 tree_hard | +0.236 [+0.177, +0.296] | 1.36e-13 |
| jev-1.13.0 flat vs microsoft-decision-1 tree_v2 | +0.044 [-0.012, +0.101] | 0.151 |
| jev-1.13.0 flat vs elephant-1 flat | -0.034 [-0.084, +0.017] | 0.211 |
| jev-1.13.0 flat vs elephant-1 tree | +0.148 [+0.081, +0.214] | 2.18e-05 |
| jev-1.13.0 flat vs elephant-1 tree_hard | +0.111 [+0.047, +0.175] | 0.000831 |
| jev-1.13.0 flat vs elephant-1 tree_v2 | +0.025 [-0.037, +0.086] | 0.477 |
| jev-1.13.0 flat vs mammoth-1 flat | -0.039 [-0.086, +0.007] | 0.117 |
| jev-1.13.0 flat vs mammoth-1 tree | +0.135 [+0.071, +0.200] | 5.29e-05 |
| jev-1.13.0 flat vs mammoth-1 tree_hard | +0.094 [+0.037, +0.150] | 0.0018 |
| jev-1.13.0 flat vs mammoth-1 tree_v2 | +0.027 [-0.034, +0.086] | 0.416 |
| jev-1.13.0 flat vs scaledown-classify-1 flat | +0.118 [+0.057, +0.180] | 0.000201 |
| jev-1.13.0 flat vs scaledown-classify-1 tree | +0.246 [+0.175, +0.315] | 4.03e-11 |
| jev-1.13.0 flat vs scaledown-classify-1 tree_hard | +0.288 [+0.224, +0.350] | 3.22e-17 |
| jev-1.13.0 flat vs scaledown-classify-1 tree_v2 | +0.219 [+0.150, +0.286] | 1.65e-09 |
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
| jev-1.13.0 tree vs pplx-decider-v1.2 flat | -0.195 [-0.254, -0.135] | 7.65e-10 |
| jev-1.13.0 tree vs pplx-decider-v1.2 tree | -0.096 [-0.140, -0.052] | 3.48e-05 |
| jev-1.13.0 tree vs pplx-decider-v1.2 tree_hard | -0.113 [-0.160, -0.069] | 2.87e-06 |
| jev-1.13.0 tree vs pplx-decider-v1.2 tree_v2 | -0.217 [-0.271, -0.163] | 2.34e-13 |
| jev-1.13.0 tree vs pplx-decider-flash-v1.2 flat | -0.145 [-0.202, -0.089] | 1.05e-06 |
| jev-1.13.0 tree vs pplx-decider-flash-v1.2 tree | +0.007 [-0.032, +0.047] | 0.807 |
| jev-1.13.0 tree vs pplx-decider-flash-v1.2 tree_hard | -0.010 [-0.049, +0.030] | 0.716 |
| jev-1.13.0 tree vs pplx-decider-flash-v1.2 tree_v2 | -0.118 [-0.170, -0.067] | 2.28e-05 |
| jev-1.13.0 tree vs gpt-6-luna-decisions flat | -0.190 [-0.244, -0.135] | 1.37e-10 |
| jev-1.13.0 tree vs gpt-6-luna-decisions tree | +0.052 [+0.005, +0.096] | 0.0334 |
| jev-1.13.0 tree vs gpt-6-luna-decisions tree_hard | +0.052 [+0.005, +0.096] | 0.0334 |
| jev-1.13.0 tree vs gpt-6-luna-decisions tree_v2 | -0.027 [-0.081, +0.027] | 0.371 |
| jev-1.13.0 tree vs d1 flat | -0.153 [-0.214, -0.091] | 2.99e-06 |
| jev-1.13.0 tree vs d1 tree | +0.025 [-0.015, +0.064] | 0.282 |
| jev-1.13.0 tree vs d1 tree_hard | -0.005 [-0.047, +0.034] | 0.905 |
| jev-1.13.0 tree vs d1 tree_v2 | -0.111 [-0.165, -0.057] | 0.000134 |
| jev-1.13.0 tree vs d1-ultra flat | -0.197 [-0.259, -0.135] | 1.71e-09 |
| jev-1.13.0 tree vs d1-ultra tree | -0.030 [-0.074, +0.015] | 0.241 |
| jev-1.13.0 tree vs d1-ultra tree_hard | -0.091 [-0.138, -0.044] | 0.000186 |
| jev-1.13.0 tree vs d1-ultra tree_v2 | -0.155 [-0.212, -0.096] | 5.34e-07 |
| jev-1.13.0 tree vs microsoft-decision-1 flat | -0.108 [-0.175, -0.042] | 0.00174 |
| jev-1.13.0 tree vs microsoft-decision-1 tree | +0.062 [+0.027, +0.096] | 0.000802 |
| jev-1.13.0 tree vs microsoft-decision-1 tree_hard | +0.091 [+0.054, +0.131] | 4.48e-06 |
| jev-1.13.0 tree vs microsoft-decision-1 tree_v2 | -0.101 [-0.163, -0.039] | 0.00176 |
| jev-1.13.0 tree vs elephant-1 flat | -0.180 [-0.234, -0.126] | 5.45e-10 |
| jev-1.13.0 tree vs elephant-1 tree | +0.002 [-0.037, +0.042] | 1 |
| jev-1.13.0 tree vs elephant-1 tree_hard | -0.034 [-0.074, +0.005] | 0.12 |
| jev-1.13.0 tree vs elephant-1 tree_v2 | -0.121 [-0.177, -0.067] | 3.94e-05 |
| jev-1.13.0 tree vs mammoth-1 flat | -0.185 [-0.246, -0.123] | 1.64e-08 |
| jev-1.13.0 tree vs mammoth-1 tree | -0.010 [-0.057, +0.037] | 0.755 |
| jev-1.13.0 tree vs mammoth-1 tree_hard | -0.052 [-0.101, -0.002] | 0.0572 |
| jev-1.13.0 tree vs mammoth-1 tree_v2 | -0.118 [-0.175, -0.059] | 0.000122 |
| jev-1.13.0 tree vs scaledown-classify-1 flat | -0.027 [-0.086, +0.030] | 0.41 |
| jev-1.13.0 tree vs scaledown-classify-1 tree | +0.101 [+0.049, +0.150] | 0.000189 |
| jev-1.13.0 tree vs scaledown-classify-1 tree_hard | +0.143 [+0.091, +0.195] | 1.86e-07 |
| jev-1.13.0 tree vs scaledown-classify-1 tree_v2 | +0.074 [+0.017, +0.128] | 0.0113 |
| jev-1.13.0 tree vs gemini-2.5-flash paper_llm | -0.140 [-0.202, -0.079] | 2.2e-05 |
| jev-1.13.0 tree vs gemini-2.5-flash paper_llm_thinking | -0.106 [-0.172, -0.042] | 0.00217 |
| jev-1.13.0 tree vs gemini-3.8-flash paper_llm_low | -0.227 [-0.281, -0.172] | 1.46e-14 |
| jev-1.13.0 tree vs gemini-3.8-flash paper_llm_thinking | -0.195 [-0.251, -0.135] | 1.98e-10 |
| jev-1.13.0 tree_hard vs jev-1.13.0 tree_v2 | -0.172 [-0.227, -0.118] | 2.56e-09 |
| jev-1.13.0 tree_hard vs jev-1.14.0 flat | -0.133 [-0.192, -0.074] | 2.09e-05 |
| jev-1.13.0 tree_hard vs jev-1.14.0 tree | +0.012 [-0.012, +0.037] | 0.442 |
| jev-1.13.0 tree_hard vs jev-1.14.0 tree_hard | +0.017 [-0.005, +0.039] | 0.21 |
| jev-1.13.0 tree_hard vs jev-1.14.0 tree_v2 | -0.165 [-0.217, -0.113] | 4.96e-09 |
| jev-1.13.0 tree_hard vs pplx-decider-v1.2 flat | -0.204 [-0.261, -0.145] | 1.19e-10 |
| jev-1.13.0 tree_hard vs pplx-decider-v1.2 tree | -0.106 [-0.150, -0.062] | 7.35e-06 |
| jev-1.13.0 tree_hard vs pplx-decider-v1.2 tree_hard | -0.123 [-0.170, -0.076] | 4.22e-07 |
| jev-1.13.0 tree_hard vs pplx-decider-v1.2 tree_v2 | -0.227 [-0.281, -0.172] | 2.31e-14 |
| jev-1.13.0 tree_hard vs pplx-decider-flash-v1.2 flat | -0.155 [-0.214, -0.096] | 5.34e-07 |
| jev-1.13.0 tree_hard vs pplx-decider-flash-v1.2 tree | -0.002 [-0.049, +0.042] | 1 |
| jev-1.13.0 tree_hard vs pplx-decider-flash-v1.2 tree_hard | -0.020 [-0.064, +0.025] | 0.445 |
| jev-1.13.0 tree_hard vs pplx-decider-flash-v1.2 tree_v2 | -0.128 [-0.185, -0.071] | 2.02e-05 |
| jev-1.13.0 tree_hard vs gpt-6-luna-decisions flat | -0.200 [-0.254, -0.145] | 8.5e-12 |
| jev-1.13.0 tree_hard vs gpt-6-luna-decisions tree | +0.042 [-0.010, +0.094] | 0.135 |
| jev-1.13.0 tree_hard vs gpt-6-luna-decisions tree_hard | +0.042 [-0.010, +0.094] | 0.135 |
| jev-1.13.0 tree_hard vs gpt-6-luna-decisions tree_v2 | -0.037 [-0.094, +0.022] | 0.248 |
| jev-1.13.0 tree_hard vs d1 flat | -0.163 [-0.222, -0.101] | 3.81e-07 |
| jev-1.13.0 tree_hard vs d1 tree | +0.015 [-0.032, +0.062] | 0.606 |
| jev-1.13.0 tree_hard vs d1 tree_hard | -0.015 [-0.059, +0.027] | 0.576 |
| jev-1.13.0 tree_hard vs d1 tree_v2 | -0.121 [-0.177, -0.062] | 8.21e-05 |
| jev-1.13.0 tree_hard vs d1-ultra flat | -0.207 [-0.268, -0.145] | 3.73e-10 |
| jev-1.13.0 tree_hard vs d1-ultra tree | -0.039 [-0.091, +0.010] | 0.152 |
| jev-1.13.0 tree_hard vs d1-ultra tree_hard | -0.101 [-0.150, -0.052] | 0.000125 |
| jev-1.13.0 tree_hard vs d1-ultra tree_v2 | -0.165 [-0.227, -0.103] | 3.78e-07 |
| jev-1.13.0 tree_hard vs microsoft-decision-1 flat | -0.118 [-0.180, -0.057] | 0.000287 |
| jev-1.13.0 tree_hard vs microsoft-decision-1 tree | +0.052 [+0.017, +0.086] | 0.00549 |
| jev-1.13.0 tree_hard vs microsoft-decision-1 tree_hard | +0.081 [+0.044, +0.116] | 1.31e-05 |
| jev-1.13.0 tree_hard vs microsoft-decision-1 tree_v2 | -0.111 [-0.170, -0.052] | 0.000447 |
| jev-1.13.0 tree_hard vs elephant-1 flat | -0.190 [-0.246, -0.131] | 7.79e-10 |
| jev-1.13.0 tree_hard vs elephant-1 tree | -0.007 [-0.052, +0.037] | 0.832 |
| jev-1.13.0 tree_hard vs elephant-1 tree_hard | -0.044 [-0.089, -0.002] | 0.0598 |
| jev-1.13.0 tree_hard vs elephant-1 tree_v2 | -0.131 [-0.190, -0.071] | 3.58e-05 |
| jev-1.13.0 tree_hard vs mammoth-1 flat | -0.195 [-0.256, -0.133] | 5.78e-09 |
| jev-1.13.0 tree_hard vs mammoth-1 tree | -0.020 [-0.071, +0.032] | 0.516 |
| jev-1.13.0 tree_hard vs mammoth-1 tree_hard | -0.062 [-0.116, -0.007] | 0.0356 |
| jev-1.13.0 tree_hard vs mammoth-1 tree_v2 | -0.128 [-0.187, -0.067] | 7.37e-05 |
| jev-1.13.0 tree_hard vs scaledown-classify-1 flat | -0.037 [-0.096, +0.020] | 0.255 |
| jev-1.13.0 tree_hard vs scaledown-classify-1 tree | +0.091 [+0.032, +0.148] | 0.00249 |
| jev-1.13.0 tree_hard vs scaledown-classify-1 tree_hard | +0.133 [+0.079, +0.187] | 2.01e-06 |
| jev-1.13.0 tree_hard vs scaledown-classify-1 tree_v2 | +0.064 [+0.002, +0.126] | 0.0464 |
| jev-1.13.0 tree_hard vs gemini-2.5-flash paper_llm | -0.150 [-0.209, -0.091] | 2.69e-06 |
| jev-1.13.0 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.116 [-0.180, -0.054] | 0.000437 |
| jev-1.13.0 tree_hard vs gemini-3.8-flash paper_llm_low | -0.236 [-0.288, -0.182] | 7.71e-16 |
| jev-1.13.0 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.204 [-0.259, -0.148] | 7.2e-12 |
| jev-1.13.0 tree_v2 vs jev-1.14.0 flat | +0.039 [-0.015, +0.096] | 0.191 |
| jev-1.13.0 tree_v2 vs jev-1.14.0 tree | +0.185 [+0.131, +0.239] | 5.97e-11 |
| jev-1.13.0 tree_v2 vs jev-1.14.0 tree_hard | +0.190 [+0.135, +0.244] | 1.87e-10 |
| jev-1.13.0 tree_v2 vs jev-1.14.0 tree_v2 | +0.007 [-0.015, +0.030] | 0.664 |
| jev-1.13.0 tree_v2 vs pplx-decider-v1.2 flat | -0.032 [-0.079, +0.015] | 0.228 |
| jev-1.13.0 tree_v2 vs pplx-decider-v1.2 tree | +0.067 [+0.010, +0.123] | 0.0305 |
| jev-1.13.0 tree_v2 vs pplx-decider-v1.2 tree_hard | +0.049 [-0.005, +0.103] | 0.0978 |
| jev-1.13.0 tree_v2 vs pplx-decider-v1.2 tree_v2 | -0.054 [-0.096, -0.012] | 0.0198 |
| jev-1.13.0 tree_v2 vs pplx-decider-flash-v1.2 flat | +0.017 [-0.034, +0.069] | 0.582 |
| jev-1.13.0 tree_v2 vs pplx-decider-flash-v1.2 tree | +0.170 [+0.111, +0.229] | 3.49e-08 |
| jev-1.13.0 tree_v2 vs pplx-decider-flash-v1.2 tree_hard | +0.153 [+0.096, +0.212] | 7.53e-07 |
| jev-1.13.0 tree_v2 vs pplx-decider-flash-v1.2 tree_v2 | +0.044 [-0.002, +0.091] | 0.0854 |
| jev-1.13.0 tree_v2 vs gpt-6-luna-decisions flat | -0.027 [-0.086, +0.032] | 0.413 |
| jev-1.13.0 tree_v2 vs gpt-6-luna-decisions tree | +0.214 [+0.150, +0.276] | 1.49e-10 |
| jev-1.13.0 tree_v2 vs gpt-6-luna-decisions tree_hard | +0.214 [+0.150, +0.276] | 1.49e-10 |
| jev-1.13.0 tree_v2 vs gpt-6-luna-decisions tree_v2 | +0.135 [+0.079, +0.192] | 7.74e-06 |
| jev-1.13.0 tree_v2 vs d1 flat | +0.010 [-0.047, +0.067] | 0.8 |
| jev-1.13.0 tree_v2 vs d1 tree | +0.187 [+0.131, +0.246] | 1.5e-09 |
| jev-1.13.0 tree_v2 vs d1 tree_hard | +0.158 [+0.101, +0.214] | 2.62e-07 |
| jev-1.13.0 tree_v2 vs d1 tree_v2 | +0.052 [+0.002, +0.099] | 0.0482 |
| jev-1.13.0 tree_v2 vs d1-ultra flat | -0.034 [-0.084, +0.017] | 0.215 |
| jev-1.13.0 tree_v2 vs d1-ultra tree | +0.133 [+0.076, +0.190] | 9.24e-06 |
| jev-1.13.0 tree_v2 vs d1-ultra tree_hard | +0.071 [+0.015, +0.128] | 0.0181 |
| jev-1.13.0 tree_v2 vs d1-ultra tree_v2 | +0.007 [-0.039, +0.052] | 0.834 |
| jev-1.13.0 tree_v2 vs microsoft-decision-1 flat | +0.054 [-0.005, +0.113] | 0.0819 |
| jev-1.13.0 tree_v2 vs microsoft-decision-1 tree | +0.224 [+0.165, +0.283] | 1.22e-12 |
| jev-1.13.0 tree_v2 vs microsoft-decision-1 tree_hard | +0.254 [+0.195, +0.313] | 5.91e-15 |
| jev-1.13.0 tree_v2 vs microsoft-decision-1 tree_v2 | +0.062 [+0.022, +0.101] | 0.00263 |
| jev-1.13.0 tree_v2 vs elephant-1 flat | -0.017 [-0.069, +0.034] | 0.579 |
| jev-1.13.0 tree_v2 vs elephant-1 tree | +0.165 [+0.106, +0.224] | 1.32e-07 |
| jev-1.13.0 tree_v2 vs elephant-1 tree_hard | +0.128 [+0.069, +0.185] | 4.28e-05 |
| jev-1.13.0 tree_v2 vs elephant-1 tree_v2 | +0.042 [-0.005, +0.089] | 0.1 |
| jev-1.13.0 tree_v2 vs mammoth-1 flat | -0.022 [-0.071, +0.027] | 0.439 |
| jev-1.13.0 tree_v2 vs mammoth-1 tree | +0.153 [+0.096, +0.209] | 3.64e-07 |
| jev-1.13.0 tree_v2 vs mammoth-1 tree_hard | +0.111 [+0.057, +0.165] | 0.000119 |
| jev-1.13.0 tree_v2 vs mammoth-1 tree_v2 | +0.044 [-0.002, +0.091] | 0.0822 |
| jev-1.13.0 tree_v2 vs scaledown-classify-1 flat | +0.135 [+0.081, +0.190] | 2.47e-06 |
| jev-1.13.0 tree_v2 vs scaledown-classify-1 tree | +0.264 [+0.202, +0.325] | 1.42e-15 |
| jev-1.13.0 tree_v2 vs scaledown-classify-1 tree_hard | +0.305 [+0.241, +0.367] | 1.9e-18 |
| jev-1.13.0 tree_v2 vs scaledown-classify-1 tree_v2 | +0.236 [+0.177, +0.293] | 2.98e-14 |
| jev-1.13.0 tree_v2 vs gemini-2.5-flash paper_llm | +0.022 [-0.034, +0.079] | 0.491 |
| jev-1.13.0 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.057 [+0.002, +0.113] | 0.0542 |
| jev-1.13.0 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.064 [-0.116, -0.015] | 0.0188 |
| jev-1.13.0 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.032 [-0.084, +0.020] | 0.271 |
| jev-1.14.0 flat vs jev-1.14.0 tree | +0.145 [+0.084, +0.207] | 7.55e-06 |
| jev-1.14.0 flat vs jev-1.14.0 tree_hard | +0.150 [+0.091, +0.209] | 1.47e-06 |
| jev-1.14.0 flat vs jev-1.14.0 tree_v2 | -0.032 [-0.086, +0.022] | 0.291 |
| jev-1.14.0 flat vs pplx-decider-v1.2 flat | -0.071 [-0.116, -0.027] | 0.00248 |
| jev-1.14.0 flat vs pplx-decider-v1.2 tree | +0.027 [-0.032, +0.086] | 0.406 |
| jev-1.14.0 flat vs pplx-decider-v1.2 tree_hard | +0.010 [-0.042, +0.062] | 0.783 |
| jev-1.14.0 flat vs pplx-decider-v1.2 tree_v2 | -0.094 [-0.143, -0.042] | 0.000371 |
| jev-1.14.0 flat vs pplx-decider-flash-v1.2 flat | -0.022 [-0.074, +0.030] | 0.448 |
| jev-1.14.0 flat vs pplx-decider-flash-v1.2 tree | +0.131 [+0.064, +0.197] | 0.000195 |
| jev-1.14.0 flat vs pplx-decider-flash-v1.2 tree_hard | +0.113 [+0.049, +0.177] | 0.000605 |
| jev-1.14.0 flat vs pplx-decider-flash-v1.2 tree_v2 | +0.005 [-0.054, +0.064] | 0.936 |
| jev-1.14.0 flat vs gpt-6-luna-decisions flat | -0.067 [-0.121, -0.015] | 0.0159 |
| jev-1.14.0 flat vs gpt-6-luna-decisions tree | +0.175 [+0.103, +0.249] | 3.48e-06 |
| jev-1.14.0 flat vs gpt-6-luna-decisions tree_hard | +0.175 [+0.103, +0.249] | 3.48e-06 |
| jev-1.14.0 flat vs gpt-6-luna-decisions tree_v2 | +0.096 [+0.027, +0.165] | 0.00811 |
| jev-1.14.0 flat vs d1 flat | -0.030 [-0.076, +0.017] | 0.241 |
| jev-1.14.0 flat vs d1 tree | +0.148 [+0.079, +0.217] | 3.2e-05 |
| jev-1.14.0 flat vs d1 tree_hard | +0.118 [+0.054, +0.182] | 0.000339 |
| jev-1.14.0 flat vs d1 tree_v2 | +0.012 [-0.047, +0.074] | 0.748 |
| jev-1.14.0 flat vs d1-ultra flat | -0.074 [-0.121, -0.027] | 0.00259 |
| jev-1.14.0 flat vs d1-ultra tree | +0.094 [+0.027, +0.160] | 0.00711 |
| jev-1.14.0 flat vs d1-ultra tree_hard | +0.032 [-0.027, +0.091] | 0.319 |
| jev-1.14.0 flat vs d1-ultra tree_v2 | -0.032 [-0.094, +0.030] | 0.338 |
| jev-1.14.0 flat vs microsoft-decision-1 flat | +0.015 [-0.027, +0.057] | 0.567 |
| jev-1.14.0 flat vs microsoft-decision-1 tree | +0.185 [+0.123, +0.249] | 2e-08 |
| jev-1.14.0 flat vs microsoft-decision-1 tree_hard | +0.214 [+0.155, +0.273] | 2.33e-11 |
| jev-1.14.0 flat vs microsoft-decision-1 tree_v2 | +0.022 [-0.034, +0.081] | 0.504 |
| jev-1.14.0 flat vs elephant-1 flat | -0.057 [-0.111, -0.002] | 0.0433 |
| jev-1.14.0 flat vs elephant-1 tree | +0.126 [+0.057, +0.197] | 0.000513 |
| jev-1.14.0 flat vs elephant-1 tree_hard | +0.089 [+0.025, +0.155] | 0.0101 |
| jev-1.14.0 flat vs elephant-1 tree_v2 | +0.002 [-0.062, +0.067] | 1 |
| jev-1.14.0 flat vs mammoth-1 flat | -0.062 [-0.108, -0.012] | 0.0144 |
| jev-1.14.0 flat vs mammoth-1 tree | +0.113 [+0.047, +0.182] | 0.00125 |
| jev-1.14.0 flat vs mammoth-1 tree_hard | +0.071 [+0.012, +0.133] | 0.0233 |
| jev-1.14.0 flat vs mammoth-1 tree_v2 | +0.005 [-0.059, +0.067] | 0.938 |
| jev-1.14.0 flat vs scaledown-classify-1 flat | +0.096 [+0.032, +0.160] | 0.00394 |
| jev-1.14.0 flat vs scaledown-classify-1 tree | +0.224 [+0.153, +0.296] | 4.46e-09 |
| jev-1.14.0 flat vs scaledown-classify-1 tree_hard | +0.266 [+0.202, +0.330] | 5.78e-15 |
| jev-1.14.0 flat vs scaledown-classify-1 tree_v2 | +0.197 [+0.126, +0.268] | 1.26e-07 |
| jev-1.14.0 flat vs gemini-2.5-flash paper_llm | -0.017 [-0.067, +0.032] | 0.558 |
| jev-1.14.0 flat vs gemini-2.5-flash paper_llm_thinking | +0.017 [-0.025, +0.062] | 0.5 |
| jev-1.14.0 flat vs gemini-3.8-flash paper_llm_low | -0.103 [-0.148, -0.059] | 8.5e-06 |
| jev-1.14.0 flat vs gemini-3.8-flash paper_llm_thinking | -0.071 [-0.116, -0.027] | 0.00219 |
| jev-1.14.0 tree vs jev-1.14.0 tree_hard | +0.005 [-0.020, +0.030] | 0.845 |
| jev-1.14.0 tree vs jev-1.14.0 tree_v2 | -0.177 [-0.229, -0.128] | 7.47e-11 |
| jev-1.14.0 tree vs pplx-decider-v1.2 flat | -0.217 [-0.273, -0.158] | 4.48e-12 |
| jev-1.14.0 tree vs pplx-decider-v1.2 tree | -0.118 [-0.160, -0.074] | 2.77e-07 |
| jev-1.14.0 tree vs pplx-decider-v1.2 tree_hard | -0.135 [-0.182, -0.091] | 1.72e-08 |
| jev-1.14.0 tree vs pplx-decider-v1.2 tree_v2 | -0.239 [-0.293, -0.185] | 4.69e-16 |
| jev-1.14.0 tree vs pplx-decider-flash-v1.2 flat | -0.167 [-0.224, -0.111] | 2.61e-08 |
| jev-1.14.0 tree vs pplx-decider-flash-v1.2 tree | -0.015 [-0.059, +0.027] | 0.572 |
| jev-1.14.0 tree vs pplx-decider-flash-v1.2 tree_hard | -0.032 [-0.074, +0.012] | 0.182 |
| jev-1.14.0 tree vs pplx-decider-flash-v1.2 tree_v2 | -0.140 [-0.195, -0.086] | 1.47e-06 |
| jev-1.14.0 tree vs gpt-6-luna-decisions flat | -0.212 [-0.266, -0.158] | 2.55e-13 |
| jev-1.14.0 tree vs gpt-6-luna-decisions tree | +0.030 [-0.017, +0.076] | 0.256 |
| jev-1.14.0 tree vs gpt-6-luna-decisions tree_hard | +0.030 [-0.017, +0.076] | 0.256 |
| jev-1.14.0 tree vs gpt-6-luna-decisions tree_v2 | -0.049 [-0.106, +0.005] | 0.0978 |
| jev-1.14.0 tree vs d1 flat | -0.175 [-0.236, -0.113] | 9.73e-08 |
| jev-1.14.0 tree vs d1 tree | +0.002 [-0.039, +0.044] | 1 |
| jev-1.14.0 tree vs d1 tree_hard | -0.027 [-0.069, +0.015] | 0.254 |
| jev-1.14.0 tree vs d1 tree_v2 | -0.133 [-0.190, -0.076] | 6.82e-06 |
| jev-1.14.0 tree vs d1-ultra flat | -0.219 [-0.281, -0.155] | 5.32e-11 |
| jev-1.14.0 tree vs d1-ultra tree | -0.052 [-0.099, -0.005] | 0.0375 |
| jev-1.14.0 tree vs d1-ultra tree_hard | -0.113 [-0.160, -0.067] | 7.37e-06 |
| jev-1.14.0 tree vs d1-ultra tree_v2 | -0.177 [-0.236, -0.118] | 2.17e-08 |
| jev-1.14.0 tree vs microsoft-decision-1 flat | -0.131 [-0.197, -0.064] | 0.000154 |
| jev-1.14.0 tree vs microsoft-decision-1 tree | +0.039 [+0.007, +0.071] | 0.0226 |
| jev-1.14.0 tree vs microsoft-decision-1 tree_hard | +0.069 [+0.034, +0.106] | 0.000234 |
| jev-1.14.0 tree vs microsoft-decision-1 tree_v2 | -0.123 [-0.182, -0.064] | 9.5e-05 |
| jev-1.14.0 tree vs elephant-1 flat | -0.202 [-0.256, -0.145] | 1.58e-11 |
| jev-1.14.0 tree vs elephant-1 tree | -0.020 [-0.059, +0.022] | 0.41 |
| jev-1.14.0 tree vs elephant-1 tree_hard | -0.057 [-0.099, -0.015] | 0.0128 |
| jev-1.14.0 tree vs elephant-1 tree_v2 | -0.143 [-0.200, -0.086] | 2.1e-06 |
| jev-1.14.0 tree vs mammoth-1 flat | -0.207 [-0.268, -0.145] | 3.73e-10 |
| jev-1.14.0 tree vs mammoth-1 tree | -0.032 [-0.079, +0.015] | 0.228 |
| jev-1.14.0 tree vs mammoth-1 tree_hard | -0.074 [-0.126, -0.022] | 0.00683 |
| jev-1.14.0 tree vs mammoth-1 tree_v2 | -0.140 [-0.200, -0.081] | 8.29e-06 |
| jev-1.14.0 tree vs scaledown-classify-1 flat | -0.049 [-0.108, +0.007] | 0.113 |
| jev-1.14.0 tree vs scaledown-classify-1 tree | +0.079 [+0.025, +0.131] | 0.00446 |
| jev-1.14.0 tree vs scaledown-classify-1 tree_hard | +0.121 [+0.069, +0.172] | 1.39e-05 |
| jev-1.14.0 tree vs scaledown-classify-1 tree_v2 | +0.052 [-0.005, +0.108] | 0.0895 |
| jev-1.14.0 tree vs gemini-2.5-flash paper_llm | -0.163 [-0.224, -0.101] | 9.69e-07 |
| jev-1.14.0 tree vs gemini-2.5-flash paper_llm_thinking | -0.128 [-0.195, -0.064] | 0.000198 |
| jev-1.14.0 tree vs gemini-3.8-flash paper_llm_low | -0.249 [-0.303, -0.195] | 3.62e-17 |
| jev-1.14.0 tree vs gemini-3.8-flash paper_llm_thinking | -0.217 [-0.273, -0.160] | 1.12e-12 |
| jev-1.14.0 tree_hard vs jev-1.14.0 tree_v2 | -0.182 [-0.234, -0.130] | 1.33e-10 |
| jev-1.14.0 tree_hard vs pplx-decider-v1.2 flat | -0.222 [-0.281, -0.163] | 4.96e-12 |
| jev-1.14.0 tree_hard vs pplx-decider-v1.2 tree | -0.123 [-0.167, -0.076] | 3.11e-07 |
| jev-1.14.0 tree_hard vs pplx-decider-v1.2 tree_hard | -0.140 [-0.187, -0.094] | 1.01e-08 |
| jev-1.14.0 tree_hard vs pplx-decider-v1.2 tree_v2 | -0.244 [-0.298, -0.187] | 7.92e-16 |
| jev-1.14.0 tree_hard vs pplx-decider-flash-v1.2 flat | -0.172 [-0.232, -0.113] | 3.67e-08 |
| jev-1.14.0 tree_hard vs pplx-decider-flash-v1.2 tree | -0.020 [-0.067, +0.030] | 0.48 |
| jev-1.14.0 tree_hard vs pplx-decider-flash-v1.2 tree_hard | -0.037 [-0.084, +0.010] | 0.151 |
| jev-1.14.0 tree_hard vs pplx-decider-flash-v1.2 tree_v2 | -0.145 [-0.202, -0.086] | 2.44e-06 |
| jev-1.14.0 tree_hard vs gpt-6-luna-decisions flat | -0.217 [-0.271, -0.163] | 2.34e-13 |
| jev-1.14.0 tree_hard vs gpt-6-luna-decisions tree | +0.025 [-0.027, +0.076] | 0.407 |
| jev-1.14.0 tree_hard vs gpt-6-luna-decisions tree_hard | +0.025 [-0.027, +0.076] | 0.407 |
| jev-1.14.0 tree_hard vs gpt-6-luna-decisions tree_v2 | -0.054 [-0.113, +0.005] | 0.0882 |
| jev-1.14.0 tree_hard vs d1 flat | -0.180 [-0.241, -0.118] | 4.87e-08 |
| jev-1.14.0 tree_hard vs d1 tree | -0.002 [-0.052, +0.047] | 1 |
| jev-1.14.0 tree_hard vs d1 tree_hard | -0.032 [-0.076, +0.015] | 0.208 |
| jev-1.14.0 tree_hard vs d1 tree_v2 | -0.138 [-0.197, -0.079] | 9.9e-06 |
| jev-1.14.0 tree_hard vs d1-ultra flat | -0.224 [-0.286, -0.160] | 4.03e-11 |
| jev-1.14.0 tree_hard vs d1-ultra tree | -0.057 [-0.108, -0.005] | 0.038 |
| jev-1.14.0 tree_hard vs d1-ultra tree_hard | -0.118 [-0.170, -0.069] | 1.16e-05 |
| jev-1.14.0 tree_hard vs d1-ultra tree_v2 | -0.182 [-0.244, -0.121] | 4.12e-08 |
| jev-1.14.0 tree_hard vs microsoft-decision-1 flat | -0.135 [-0.200, -0.071] | 3.9e-05 |
| jev-1.14.0 tree_hard vs microsoft-decision-1 tree | +0.034 [-0.002, +0.071] | 0.0814 |
| jev-1.14.0 tree_hard vs microsoft-decision-1 tree_hard | +0.064 [+0.027, +0.101] | 0.000862 |
| jev-1.14.0 tree_hard vs microsoft-decision-1 tree_v2 | -0.128 [-0.190, -0.069] | 5.98e-05 |
| jev-1.14.0 tree_hard vs elephant-1 flat | -0.207 [-0.266, -0.148] | 6.01e-11 |
| jev-1.14.0 tree_hard vs elephant-1 tree | -0.025 [-0.071, +0.022] | 0.358 |
| jev-1.14.0 tree_hard vs elephant-1 tree_hard | -0.062 [-0.108, -0.015] | 0.0124 |
| jev-1.14.0 tree_hard vs elephant-1 tree_v2 | -0.148 [-0.209, -0.086] | 4.87e-06 |
| jev-1.14.0 tree_hard vs mammoth-1 flat | -0.212 [-0.273, -0.148] | 4.39e-10 |
| jev-1.14.0 tree_hard vs mammoth-1 tree | -0.037 [-0.091, +0.015] | 0.203 |
| jev-1.14.0 tree_hard vs mammoth-1 tree_hard | -0.079 [-0.133, -0.022] | 0.00718 |
| jev-1.14.0 tree_hard vs mammoth-1 tree_v2 | -0.145 [-0.207, -0.084] | 9.69e-06 |
| jev-1.14.0 tree_hard vs scaledown-classify-1 flat | -0.054 [-0.113, +0.002] | 0.084 |
| jev-1.14.0 tree_hard vs scaledown-classify-1 tree | +0.074 [+0.015, +0.131] | 0.0161 |
| jev-1.14.0 tree_hard vs scaledown-classify-1 tree_hard | +0.116 [+0.062, +0.170] | 4.27e-05 |
| jev-1.14.0 tree_hard vs scaledown-classify-1 tree_v2 | +0.047 [-0.017, +0.108] | 0.161 |
| jev-1.14.0 tree_hard vs gemini-2.5-flash paper_llm | -0.167 [-0.229, -0.106] | 3.18e-07 |
| jev-1.14.0 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.133 [-0.197, -0.069] | 6.31e-05 |
| jev-1.14.0 tree_hard vs gemini-3.8-flash paper_llm_low | -0.254 [-0.308, -0.200] | 3.95e-17 |
| jev-1.14.0 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.222 [-0.278, -0.163] | 6.62e-13 |
| jev-1.14.0 tree_v2 vs pplx-decider-v1.2 flat | -0.039 [-0.089, +0.010] | 0.137 |
| jev-1.14.0 tree_v2 vs pplx-decider-v1.2 tree | +0.059 [+0.002, +0.116] | 0.0566 |
| jev-1.14.0 tree_v2 vs pplx-decider-v1.2 tree_hard | +0.042 [-0.012, +0.096] | 0.162 |
| jev-1.14.0 tree_v2 vs pplx-decider-v1.2 tree_v2 | -0.062 [-0.103, -0.020] | 0.00728 |
| jev-1.14.0 tree_v2 vs pplx-decider-flash-v1.2 flat | +0.010 [-0.044, +0.064] | 0.791 |
| jev-1.14.0 tree_v2 vs pplx-decider-flash-v1.2 tree | +0.163 [+0.103, +0.222] | 3.81e-07 |
| jev-1.14.0 tree_v2 vs pplx-decider-flash-v1.2 tree_hard | +0.145 [+0.084, +0.204] | 5.08e-06 |
| jev-1.14.0 tree_v2 vs pplx-decider-flash-v1.2 tree_v2 | +0.037 [-0.012, +0.086] | 0.18 |
| jev-1.14.0 tree_v2 vs gpt-6-luna-decisions flat | -0.034 [-0.091, +0.022] | 0.279 |
| jev-1.14.0 tree_v2 vs gpt-6-luna-decisions tree | +0.207 [+0.143, +0.271] | 1.41e-09 |
| jev-1.14.0 tree_v2 vs gpt-6-luna-decisions tree_hard | +0.207 [+0.143, +0.271] | 1.41e-09 |
| jev-1.14.0 tree_v2 vs gpt-6-luna-decisions tree_v2 | +0.128 [+0.069, +0.187] | 3.81e-05 |
| jev-1.14.0 tree_v2 vs d1 flat | +0.002 [-0.054, +0.059] | 1 |
| jev-1.14.0 tree_v2 vs d1 tree | +0.180 [+0.121, +0.239] | 1.85e-08 |
| jev-1.14.0 tree_v2 vs d1 tree_hard | +0.150 [+0.091, +0.209] | 1.47e-06 |
| jev-1.14.0 tree_v2 vs d1 tree_v2 | +0.044 [-0.005, +0.091] | 0.101 |
| jev-1.14.0 tree_v2 vs d1-ultra flat | -0.042 [-0.094, +0.010] | 0.132 |
| jev-1.14.0 tree_v2 vs d1-ultra tree | +0.126 [+0.067, +0.185] | 4.55e-05 |
| jev-1.14.0 tree_v2 vs d1-ultra tree_hard | +0.064 [+0.007, +0.123] | 0.0382 |
| jev-1.14.0 tree_v2 vs d1-ultra tree_v2 | +0.000 [-0.049, +0.047] | 1 |
| jev-1.14.0 tree_v2 vs microsoft-decision-1 flat | +0.047 [-0.010, +0.106] | 0.132 |
| jev-1.14.0 tree_v2 vs microsoft-decision-1 tree | +0.217 [+0.158, +0.273] | 4.48e-12 |
| jev-1.14.0 tree_v2 vs microsoft-decision-1 tree_hard | +0.246 [+0.187, +0.305] | 1.56e-14 |
| jev-1.14.0 tree_v2 vs microsoft-decision-1 tree_v2 | +0.054 [+0.015, +0.094] | 0.00815 |
| jev-1.14.0 tree_v2 vs elephant-1 flat | -0.025 [-0.079, +0.030] | 0.426 |
| jev-1.14.0 tree_v2 vs elephant-1 tree | +0.158 [+0.099, +0.219] | 1.02e-06 |
| jev-1.14.0 tree_v2 vs elephant-1 tree_hard | +0.121 [+0.062, +0.180] | 0.000139 |
| jev-1.14.0 tree_v2 vs elephant-1 tree_v2 | +0.034 [-0.015, +0.084] | 0.206 |
| jev-1.14.0 tree_v2 vs mammoth-1 flat | -0.030 [-0.081, +0.022] | 0.307 |
| jev-1.14.0 tree_v2 vs mammoth-1 tree | +0.145 [+0.086, +0.202] | 2.44e-06 |
| jev-1.14.0 tree_v2 vs mammoth-1 tree_hard | +0.103 [+0.049, +0.158] | 0.000441 |
| jev-1.14.0 tree_v2 vs mammoth-1 tree_v2 | +0.037 [-0.012, +0.084] | 0.163 |
| jev-1.14.0 tree_v2 vs scaledown-classify-1 flat | +0.128 [+0.071, +0.182] | 9.67e-06 |
| jev-1.14.0 tree_v2 vs scaledown-classify-1 tree | +0.256 [+0.192, +0.318] | 4.6e-14 |
| jev-1.14.0 tree_v2 vs scaledown-classify-1 tree_hard | +0.298 [+0.234, +0.360] | 7.65e-18 |
| jev-1.14.0 tree_v2 vs scaledown-classify-1 tree_v2 | +0.229 [+0.170, +0.288] | 1.01e-12 |
| jev-1.14.0 tree_v2 vs gemini-2.5-flash paper_llm | +0.015 [-0.042, +0.071] | 0.668 |
| jev-1.14.0 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.049 [-0.005, +0.103] | 0.0927 |
| jev-1.14.0 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.071 [-0.121, -0.022] | 0.00758 |
| jev-1.14.0 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.039 [-0.091, +0.012] | 0.167 |
| pplx-decider-v1.2 flat vs pplx-decider-v1.2 tree | +0.099 [+0.052, +0.145] | 9.31e-05 |
| pplx-decider-v1.2 flat vs pplx-decider-v1.2 tree_hard | +0.081 [+0.037, +0.126] | 0.000705 |
| pplx-decider-v1.2 flat vs pplx-decider-v1.2 tree_v2 | -0.022 [-0.054, +0.010] | 0.233 |
| pplx-decider-v1.2 flat vs pplx-decider-flash-v1.2 flat | +0.049 [+0.005, +0.094] | 0.0399 |
| pplx-decider-v1.2 flat vs pplx-decider-flash-v1.2 tree | +0.202 [+0.145, +0.256] | 3.06e-11 |
| pplx-decider-v1.2 flat vs pplx-decider-flash-v1.2 tree_hard | +0.185 [+0.131, +0.239] | 8.54e-11 |
| pplx-decider-v1.2 flat vs pplx-decider-flash-v1.2 tree_v2 | +0.076 [+0.027, +0.123] | 0.00265 |
| pplx-decider-v1.2 flat vs gpt-6-luna-decisions flat | +0.005 [-0.047, +0.057] | 0.925 |
| pplx-decider-v1.2 flat vs gpt-6-luna-decisions tree | +0.246 [+0.185, +0.305] | 4.76e-14 |
| pplx-decider-v1.2 flat vs gpt-6-luna-decisions tree_hard | +0.246 [+0.185, +0.305] | 4.76e-14 |
| pplx-decider-v1.2 flat vs gpt-6-luna-decisions tree_v2 | +0.167 [+0.111, +0.222] | 2.61e-08 |
| pplx-decider-v1.2 flat vs d1 flat | +0.042 [-0.002, +0.084] | 0.0675 |
| pplx-decider-v1.2 flat vs d1 tree | +0.219 [+0.163, +0.276] | 1.47e-12 |
| pplx-decider-v1.2 flat vs d1 tree_hard | +0.190 [+0.135, +0.244] | 9.89e-11 |
| pplx-decider-v1.2 flat vs d1 tree_v2 | +0.084 [+0.037, +0.131] | 0.00111 |
| pplx-decider-v1.2 flat vs d1-ultra flat | -0.002 [-0.039, +0.034] | 1 |
| pplx-decider-v1.2 flat vs d1-ultra tree | +0.165 [+0.108, +0.222] | 4.76e-08 |
| pplx-decider-v1.2 flat vs d1-ultra tree_hard | +0.103 [+0.054, +0.153] | 6.55e-05 |
| pplx-decider-v1.2 flat vs d1-ultra tree_v2 | +0.039 [-0.010, +0.089] | 0.145 |
| pplx-decider-v1.2 flat vs microsoft-decision-1 flat | +0.086 [+0.034, +0.138] | 0.00171 |
| pplx-decider-v1.2 flat vs microsoft-decision-1 tree | +0.256 [+0.197, +0.315] | 8.04e-15 |
| pplx-decider-v1.2 flat vs microsoft-decision-1 tree_hard | +0.286 [+0.224, +0.345] | 9.24e-18 |
| pplx-decider-v1.2 flat vs microsoft-decision-1 tree_v2 | +0.094 [+0.039, +0.148] | 0.00109 |
| pplx-decider-v1.2 flat vs elephant-1 flat | +0.015 [-0.025, +0.054] | 0.55 |
| pplx-decider-v1.2 flat vs elephant-1 tree | +0.197 [+0.138, +0.254] | 3.98e-10 |
| pplx-decider-v1.2 flat vs elephant-1 tree_hard | +0.160 [+0.103, +0.214] | 1e-07 |
| pplx-decider-v1.2 flat vs elephant-1 tree_v2 | +0.074 [+0.022, +0.123] | 0.00635 |
| pplx-decider-v1.2 flat vs mammoth-1 flat | +0.010 [-0.025, +0.044] | 0.678 |
| pplx-decider-v1.2 flat vs mammoth-1 tree | +0.185 [+0.128, +0.241] | 7.71e-10 |
| pplx-decider-v1.2 flat vs mammoth-1 tree_hard | +0.143 [+0.094, +0.190] | 2.61e-08 |
| pplx-decider-v1.2 flat vs mammoth-1 tree_v2 | +0.076 [+0.027, +0.126] | 0.00353 |
| pplx-decider-v1.2 flat vs scaledown-classify-1 flat | +0.167 [+0.111, +0.224] | 2.07e-08 |
| pplx-decider-v1.2 flat vs scaledown-classify-1 tree | +0.296 [+0.234, +0.357] | 5.24e-18 |
| pplx-decider-v1.2 flat vs scaledown-classify-1 tree_hard | +0.337 [+0.273, +0.397] | 1.12e-22 |
| pplx-decider-v1.2 flat vs scaledown-classify-1 tree_v2 | +0.268 [+0.209, +0.328] | 2.49e-16 |
| pplx-decider-v1.2 flat vs gemini-2.5-flash paper_llm | +0.054 [+0.002, +0.106] | 0.0487 |
| pplx-decider-v1.2 flat vs gemini-2.5-flash paper_llm_thinking | +0.089 [+0.037, +0.140] | 0.00107 |
| pplx-decider-v1.2 flat vs gemini-3.8-flash paper_llm_low | -0.032 [-0.071, +0.005] | 0.136 |
| pplx-decider-v1.2 flat vs gemini-3.8-flash paper_llm_thinking | +0.000 [-0.039, +0.039] | 1 |
| pplx-decider-v1.2 tree vs pplx-decider-v1.2 tree_hard | -0.017 [-0.047, +0.012] | 0.311 |
| pplx-decider-v1.2 tree vs pplx-decider-v1.2 tree_v2 | -0.121 [-0.160, -0.081] | 2.63e-09 |
| pplx-decider-v1.2 tree vs pplx-decider-flash-v1.2 flat | -0.049 [-0.103, +0.005] | 0.0978 |
| pplx-decider-v1.2 tree vs pplx-decider-flash-v1.2 tree | +0.103 [+0.059, +0.148] | 1.38e-05 |
| pplx-decider-v1.2 tree vs pplx-decider-flash-v1.2 tree_hard | +0.086 [+0.044, +0.128] | 8.22e-05 |
| pplx-decider-v1.2 tree vs pplx-decider-flash-v1.2 tree_v2 | -0.022 [-0.074, +0.030] | 0.456 |
| pplx-decider-v1.2 tree vs gpt-6-luna-decisions flat | -0.094 [-0.148, -0.039] | 0.00109 |
| pplx-decider-v1.2 tree vs gpt-6-luna-decisions tree | +0.148 [+0.099, +0.200] | 2.09e-08 |
| pplx-decider-v1.2 tree vs gpt-6-luna-decisions tree_hard | +0.148 [+0.099, +0.200] | 2.09e-08 |
| pplx-decider-v1.2 tree vs gpt-6-luna-decisions tree_v2 | +0.069 [+0.012, +0.123] | 0.0193 |
| pplx-decider-v1.2 tree vs d1 flat | -0.057 [-0.111, -0.002] | 0.0487 |
| pplx-decider-v1.2 tree vs d1 tree | +0.121 [+0.076, +0.165] | 2.51e-07 |
| pplx-decider-v1.2 tree vs d1 tree_hard | +0.091 [+0.049, +0.133] | 3.76e-05 |
| pplx-decider-v1.2 tree vs d1 tree_v2 | -0.015 [-0.069, +0.037] | 0.648 |
| pplx-decider-v1.2 tree vs d1-ultra flat | -0.101 [-0.155, -0.044] | 0.000527 |
| pplx-decider-v1.2 tree vs d1-ultra tree | +0.067 [+0.022, +0.111] | 0.00501 |
| pplx-decider-v1.2 tree vs d1-ultra tree_hard | +0.005 [-0.037, +0.047] | 0.908 |
| pplx-decider-v1.2 tree vs d1-ultra tree_v2 | -0.059 [-0.113, -0.005] | 0.0465 |
| pplx-decider-v1.2 tree vs microsoft-decision-1 flat | -0.012 [-0.074, +0.052] | 0.757 |
| pplx-decider-v1.2 tree vs microsoft-decision-1 tree | +0.158 [+0.111, +0.204] | 2.58e-10 |
| pplx-decider-v1.2 tree vs microsoft-decision-1 tree_hard | +0.187 [+0.138, +0.236] | 7.27e-13 |
| pplx-decider-v1.2 tree vs microsoft-decision-1 tree_v2 | -0.005 [-0.067, +0.059] | 0.939 |
| pplx-decider-v1.2 tree vs elephant-1 flat | -0.084 [-0.133, -0.034] | 0.00153 |
| pplx-decider-v1.2 tree vs elephant-1 tree | +0.099 [+0.054, +0.145] | 3.67e-05 |
| pplx-decider-v1.2 tree vs elephant-1 tree_hard | +0.062 [+0.020, +0.103] | 0.00655 |
| pplx-decider-v1.2 tree vs elephant-1 tree_v2 | -0.025 [-0.079, +0.030] | 0.434 |
| pplx-decider-v1.2 tree vs mammoth-1 flat | -0.089 [-0.140, -0.034] | 0.00156 |
| pplx-decider-v1.2 tree vs mammoth-1 tree | +0.086 [+0.042, +0.131] | 0.000313 |
| pplx-decider-v1.2 tree vs mammoth-1 tree_hard | +0.044 [+0.000, +0.089] | 0.0598 |
| pplx-decider-v1.2 tree vs mammoth-1 tree_v2 | -0.022 [-0.074, +0.030] | 0.463 |
| pplx-decider-v1.2 tree vs scaledown-classify-1 flat | +0.069 [+0.010, +0.128] | 0.0303 |
| pplx-decider-v1.2 tree vs scaledown-classify-1 tree | +0.197 [+0.143, +0.251] | 4.2e-12 |
| pplx-decider-v1.2 tree vs scaledown-classify-1 tree_hard | +0.239 [+0.180, +0.296] | 1.88e-14 |
| pplx-decider-v1.2 tree vs scaledown-classify-1 tree_v2 | +0.170 [+0.113, +0.227] | 1.41e-08 |
| pplx-decider-v1.2 tree vs gemini-2.5-flash paper_llm | -0.044 [-0.103, +0.017] | 0.181 |
| pplx-decider-v1.2 tree vs gemini-2.5-flash paper_llm_thinking | -0.010 [-0.076, +0.054] | 0.824 |
| pplx-decider-v1.2 tree vs gemini-3.8-flash paper_llm_low | -0.131 [-0.177, -0.081] | 3.78e-07 |
| pplx-decider-v1.2 tree vs gemini-3.8-flash paper_llm_thinking | -0.099 [-0.150, -0.047] | 0.000227 |
| pplx-decider-v1.2 tree_hard vs pplx-decider-v1.2 tree_v2 | -0.103 [-0.143, -0.067] | 2.75e-07 |
| pplx-decider-v1.2 tree_hard vs pplx-decider-flash-v1.2 flat | -0.032 [-0.084, +0.017] | 0.259 |
| pplx-decider-v1.2 tree_hard vs pplx-decider-flash-v1.2 tree | +0.121 [+0.069, +0.172] | 6.78e-06 |
| pplx-decider-v1.2 tree_hard vs pplx-decider-flash-v1.2 tree_hard | +0.103 [+0.059, +0.148] | 1.09e-05 |
| pplx-decider-v1.2 tree_hard vs pplx-decider-flash-v1.2 tree_v2 | -0.005 [-0.059, +0.049] | 0.928 |
| pplx-decider-v1.2 tree_hard vs gpt-6-luna-decisions flat | -0.076 [-0.126, -0.025] | 0.00455 |
| pplx-decider-v1.2 tree_hard vs gpt-6-luna-decisions tree | +0.165 [+0.108, +0.224] | 3.82e-08 |
| pplx-decider-v1.2 tree_hard vs gpt-6-luna-decisions tree_hard | +0.165 [+0.108, +0.224] | 3.82e-08 |
| pplx-decider-v1.2 tree_hard vs gpt-6-luna-decisions tree_v2 | +0.086 [+0.027, +0.145] | 0.00487 |
| pplx-decider-v1.2 tree_hard vs d1 flat | -0.039 [-0.091, +0.012] | 0.16 |
| pplx-decider-v1.2 tree_hard vs d1 tree | +0.138 [+0.086, +0.192] | 5.09e-07 |
| pplx-decider-v1.2 tree_hard vs d1 tree_hard | +0.108 [+0.062, +0.155] | 8.05e-06 |
| pplx-decider-v1.2 tree_hard vs d1 tree_v2 | +0.002 [-0.052, +0.057] | 1 |
| pplx-decider-v1.2 tree_hard vs d1-ultra flat | -0.084 [-0.135, -0.032] | 0.00245 |
| pplx-decider-v1.2 tree_hard vs d1-ultra tree | +0.084 [+0.034, +0.133] | 0.00153 |
| pplx-decider-v1.2 tree_hard vs d1-ultra tree_hard | +0.022 [-0.017, +0.062] | 0.336 |
| pplx-decider-v1.2 tree_hard vs d1-ultra tree_v2 | -0.042 [-0.099, +0.015] | 0.175 |
| pplx-decider-v1.2 tree_hard vs microsoft-decision-1 flat | +0.005 [-0.052, +0.062] | 0.932 |
| pplx-decider-v1.2 tree_hard vs microsoft-decision-1 tree | +0.175 [+0.128, +0.222] | 5.25e-12 |
| pplx-decider-v1.2 tree_hard vs microsoft-decision-1 tree_hard | +0.204 [+0.155, +0.254] | 3.37e-15 |
| pplx-decider-v1.2 tree_hard vs microsoft-decision-1 tree_v2 | +0.012 [-0.044, +0.071] | 0.745 |
| pplx-decider-v1.2 tree_hard vs elephant-1 flat | -0.067 [-0.113, -0.017] | 0.0101 |
| pplx-decider-v1.2 tree_hard vs elephant-1 tree | +0.116 [+0.064, +0.170] | 3.18e-05 |
| pplx-decider-v1.2 tree_hard vs elephant-1 tree_hard | +0.079 [+0.032, +0.126] | 0.0016 |
| pplx-decider-v1.2 tree_hard vs elephant-1 tree_v2 | -0.007 [-0.064, +0.049] | 0.865 |
| pplx-decider-v1.2 tree_hard vs mammoth-1 flat | -0.071 [-0.121, -0.020] | 0.00815 |
| pplx-decider-v1.2 tree_hard vs mammoth-1 tree | +0.103 [+0.054, +0.155] | 0.000104 |
| pplx-decider-v1.2 tree_hard vs mammoth-1 tree_hard | +0.062 [+0.017, +0.106] | 0.00884 |
| pplx-decider-v1.2 tree_hard vs mammoth-1 tree_v2 | -0.005 [-0.059, +0.049] | 0.93 |
| pplx-decider-v1.2 tree_hard vs scaledown-classify-1 flat | +0.086 [+0.027, +0.145] | 0.00613 |
| pplx-decider-v1.2 tree_hard vs scaledown-classify-1 tree | +0.214 [+0.155, +0.273] | 1.74e-11 |
| pplx-decider-v1.2 tree_hard vs scaledown-classify-1 tree_hard | +0.256 [+0.197, +0.315] | 4.61e-16 |
| pplx-decider-v1.2 tree_hard vs scaledown-classify-1 tree_v2 | +0.187 [+0.126, +0.249] | 9.34e-09 |
| pplx-decider-v1.2 tree_hard vs gemini-2.5-flash paper_llm | -0.027 [-0.084, +0.032] | 0.413 |
| pplx-decider-v1.2 tree_hard vs gemini-2.5-flash paper_llm_thinking | +0.007 [-0.052, +0.067] | 0.871 |
| pplx-decider-v1.2 tree_hard vs gemini-3.8-flash paper_llm_low | -0.113 [-0.158, -0.069] | 2.2e-06 |
| pplx-decider-v1.2 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.081 [-0.128, -0.034] | 0.00133 |
| pplx-decider-v1.2 tree_v2 vs pplx-decider-flash-v1.2 flat | +0.071 [+0.022, +0.121] | 0.00508 |
| pplx-decider-v1.2 tree_v2 vs pplx-decider-flash-v1.2 tree | +0.224 [+0.170, +0.278] | 5.76e-14 |
| pplx-decider-v1.2 tree_v2 vs pplx-decider-flash-v1.2 tree_hard | +0.207 [+0.155, +0.259] | 1.71e-13 |
| pplx-decider-v1.2 tree_v2 vs pplx-decider-flash-v1.2 tree_v2 | +0.099 [+0.052, +0.145] | 4.5e-05 |
| pplx-decider-v1.2 tree_v2 vs gpt-6-luna-decisions flat | +0.027 [-0.025, +0.079] | 0.351 |
| pplx-decider-v1.2 tree_v2 vs gpt-6-luna-decisions tree | +0.268 [+0.209, +0.328] | 4.19e-17 |
| pplx-decider-v1.2 tree_v2 vs gpt-6-luna-decisions tree_hard | +0.268 [+0.209, +0.328] | 4.19e-17 |
| pplx-decider-v1.2 tree_v2 vs gpt-6-luna-decisions tree_v2 | +0.190 [+0.135, +0.244] | 7.09e-11 |
| pplx-decider-v1.2 tree_v2 vs d1 flat | +0.064 [+0.017, +0.111] | 0.00878 |
| pplx-decider-v1.2 tree_v2 vs d1 tree | +0.241 [+0.187, +0.296] | 4.78e-16 |
| pplx-decider-v1.2 tree_v2 vs d1 tree_hard | +0.212 [+0.160, +0.264] | 2.36e-14 |
| pplx-decider-v1.2 tree_v2 vs d1 tree_v2 | +0.106 [+0.062, +0.153] | 1.18e-05 |
| pplx-decider-v1.2 tree_v2 vs d1-ultra flat | +0.020 [-0.022, +0.064] | 0.434 |
| pplx-decider-v1.2 tree_v2 vs d1-ultra tree | +0.187 [+0.133, +0.241] | 3.82e-11 |
| pplx-decider-v1.2 tree_v2 vs d1-ultra tree_hard | +0.126 [+0.079, +0.172] | 6.49e-07 |
| pplx-decider-v1.2 tree_v2 vs d1-ultra tree_v2 | +0.062 [+0.017, +0.106] | 0.0105 |
| pplx-decider-v1.2 tree_v2 vs microsoft-decision-1 flat | +0.108 [+0.054, +0.163] | 0.000125 |
| pplx-decider-v1.2 tree_v2 vs microsoft-decision-1 tree | +0.278 [+0.222, +0.335] | 4.35e-19 |
| pplx-decider-v1.2 tree_v2 vs microsoft-decision-1 tree_hard | +0.308 [+0.251, +0.365] | 2.47e-22 |
| pplx-decider-v1.2 tree_v2 vs microsoft-decision-1 tree_v2 | +0.116 [+0.067, +0.165] | 9.45e-06 |
| pplx-decider-v1.2 tree_v2 vs elephant-1 flat | +0.037 [-0.005, +0.081] | 0.119 |
| pplx-decider-v1.2 tree_v2 vs elephant-1 tree | +0.219 [+0.163, +0.276] | 3.33e-13 |
| pplx-decider-v1.2 tree_v2 vs elephant-1 tree_hard | +0.182 [+0.131, +0.234] | 9.32e-11 |
| pplx-decider-v1.2 tree_v2 vs elephant-1 tree_v2 | +0.096 [+0.049, +0.143] | 0.000111 |
| pplx-decider-v1.2 tree_v2 vs mammoth-1 flat | +0.032 [-0.010, +0.074] | 0.165 |
| pplx-decider-v1.2 tree_v2 vs mammoth-1 tree | +0.207 [+0.155, +0.261] | 2.71e-13 |
| pplx-decider-v1.2 tree_v2 vs mammoth-1 tree_hard | +0.165 [+0.118, +0.209] | 7.85e-12 |
| pplx-decider-v1.2 tree_v2 vs mammoth-1 tree_v2 | +0.099 [+0.054, +0.143] | 2.37e-05 |
| pplx-decider-v1.2 tree_v2 vs scaledown-classify-1 flat | +0.190 [+0.135, +0.246] | 9.89e-11 |
| pplx-decider-v1.2 tree_v2 vs scaledown-classify-1 tree | +0.318 [+0.256, +0.377] | 1.21e-21 |
| pplx-decider-v1.2 tree_v2 vs scaledown-classify-1 tree_hard | +0.360 [+0.300, +0.419] | 2.49e-26 |
| pplx-decider-v1.2 tree_v2 vs scaledown-classify-1 tree_v2 | +0.291 [+0.232, +0.347] | 1.05e-19 |
| pplx-decider-v1.2 tree_v2 vs gemini-2.5-flash paper_llm | +0.076 [+0.025, +0.128] | 0.00615 |
| pplx-decider-v1.2 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.111 [+0.057, +0.163] | 8.06e-05 |
| pplx-decider-v1.2 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.010 [-0.049, +0.030] | 0.72 |
| pplx-decider-v1.2 tree_v2 vs gemini-3.8-flash paper_llm_thinking | +0.022 [-0.020, +0.064] | 0.356 |
| pplx-decider-flash-v1.2 flat vs pplx-decider-flash-v1.2 tree | +0.153 [+0.099, +0.207] | 1.03e-07 |
| pplx-decider-flash-v1.2 flat vs pplx-decider-flash-v1.2 tree_hard | +0.135 [+0.084, +0.187] | 7.43e-07 |
| pplx-decider-flash-v1.2 flat vs pplx-decider-flash-v1.2 tree_v2 | +0.027 [-0.020, +0.074] | 0.294 |
| pplx-decider-flash-v1.2 flat vs gpt-6-luna-decisions flat | -0.044 [-0.094, +0.005] | 0.0918 |
| pplx-decider-flash-v1.2 flat vs gpt-6-luna-decisions tree | +0.197 [+0.140, +0.254] | 9.74e-11 |
| pplx-decider-flash-v1.2 flat vs gpt-6-luna-decisions tree_hard | +0.197 [+0.140, +0.254] | 9.74e-11 |
| pplx-decider-flash-v1.2 flat vs gpt-6-luna-decisions tree_v2 | +0.118 [+0.062, +0.172] | 4.71e-05 |
| pplx-decider-flash-v1.2 flat vs d1 flat | -0.007 [-0.049, +0.034] | 0.822 |
| pplx-decider-flash-v1.2 flat vs d1 tree | +0.170 [+0.113, +0.227] | 2.25e-08 |
| pplx-decider-flash-v1.2 flat vs d1 tree_hard | +0.140 [+0.084, +0.195] | 2.1e-06 |
| pplx-decider-flash-v1.2 flat vs d1 tree_v2 | +0.034 [-0.015, +0.084] | 0.211 |
| pplx-decider-flash-v1.2 flat vs d1-ultra flat | -0.052 [-0.096, -0.010] | 0.0275 |
| pplx-decider-flash-v1.2 flat vs d1-ultra tree | +0.116 [+0.062, +0.170] | 4.92e-05 |
| pplx-decider-flash-v1.2 flat vs d1-ultra tree_hard | +0.054 [+0.005, +0.103] | 0.039 |
| pplx-decider-flash-v1.2 flat vs d1-ultra tree_v2 | -0.010 [-0.059, +0.039] | 0.771 |
| pplx-decider-flash-v1.2 flat vs microsoft-decision-1 flat | +0.037 [-0.017, +0.091] | 0.199 |
| pplx-decider-flash-v1.2 flat vs microsoft-decision-1 tree | +0.207 [+0.150, +0.264] | 9.3e-12 |
| pplx-decider-flash-v1.2 flat vs microsoft-decision-1 tree_hard | +0.236 [+0.180, +0.293] | 1.98e-14 |
| pplx-decider-flash-v1.2 flat vs microsoft-decision-1 tree_v2 | +0.044 [-0.010, +0.101] | 0.139 |
| pplx-decider-flash-v1.2 flat vs elephant-1 flat | -0.034 [-0.071, +0.002] | 0.0814 |
| pplx-decider-flash-v1.2 flat vs elephant-1 tree | +0.148 [+0.089, +0.204] | 1.26e-06 |
| pplx-decider-flash-v1.2 flat vs elephant-1 tree_hard | +0.111 [+0.054, +0.167] | 0.000232 |
| pplx-decider-flash-v1.2 flat vs elephant-1 tree_v2 | +0.025 [-0.025, +0.074] | 0.387 |
| pplx-decider-flash-v1.2 flat vs mammoth-1 flat | -0.039 [-0.084, +0.002] | 0.0888 |
| pplx-decider-flash-v1.2 flat vs mammoth-1 tree | +0.135 [+0.079, +0.192] | 3.51e-06 |
| pplx-decider-flash-v1.2 flat vs mammoth-1 tree_hard | +0.094 [+0.044, +0.143] | 0.000475 |
| pplx-decider-flash-v1.2 flat vs mammoth-1 tree_v2 | +0.027 [-0.025, +0.076] | 0.343 |
| pplx-decider-flash-v1.2 flat vs scaledown-classify-1 flat | +0.118 [+0.062, +0.175] | 8.77e-05 |
| pplx-decider-flash-v1.2 flat vs scaledown-classify-1 tree | +0.246 [+0.185, +0.305] | 4.76e-14 |
| pplx-decider-flash-v1.2 flat vs scaledown-classify-1 tree_hard | +0.288 [+0.229, +0.345] | 1.75e-19 |
| pplx-decider-flash-v1.2 flat vs scaledown-classify-1 tree_v2 | +0.219 [+0.160, +0.276] | 2.08e-12 |
| pplx-decider-flash-v1.2 flat vs gemini-2.5-flash paper_llm | +0.005 [-0.049, +0.059] | 0.928 |
| pplx-decider-flash-v1.2 flat vs gemini-2.5-flash paper_llm_thinking | +0.039 [-0.015, +0.094] | 0.181 |
| pplx-decider-flash-v1.2 flat vs gemini-3.8-flash paper_llm_low | -0.081 [-0.126, -0.037] | 0.00061 |
| pplx-decider-flash-v1.2 flat vs gemini-3.8-flash paper_llm_thinking | -0.049 [-0.096, -0.002] | 0.047 |
| pplx-decider-flash-v1.2 tree vs pplx-decider-flash-v1.2 tree_hard | -0.017 [-0.047, +0.012] | 0.337 |
| pplx-decider-flash-v1.2 tree vs pplx-decider-flash-v1.2 tree_v2 | -0.126 [-0.165, -0.089] | 1.02e-10 |
| pplx-decider-flash-v1.2 tree vs gpt-6-luna-decisions flat | -0.197 [-0.256, -0.138] | 5.16e-10 |
| pplx-decider-flash-v1.2 tree vs gpt-6-luna-decisions tree | +0.044 [+0.007, +0.081] | 0.0273 |
| pplx-decider-flash-v1.2 tree vs gpt-6-luna-decisions tree_hard | +0.044 [+0.007, +0.081] | 0.0273 |
| pplx-decider-flash-v1.2 tree vs gpt-6-luna-decisions tree_v2 | -0.034 [-0.081, +0.012] | 0.18 |
| pplx-decider-flash-v1.2 tree vs d1 flat | -0.160 [-0.219, -0.099] | 3.81e-07 |
| pplx-decider-flash-v1.2 tree vs d1 tree | +0.017 [-0.017, +0.052] | 0.392 |
| pplx-decider-flash-v1.2 tree vs d1 tree_hard | -0.012 [-0.052, +0.027] | 0.625 |
| pplx-decider-flash-v1.2 tree vs d1 tree_v2 | -0.118 [-0.170, -0.069] | 1.16e-05 |
| pplx-decider-flash-v1.2 tree vs d1-ultra flat | -0.204 [-0.264, -0.145] | 9.05e-11 |
| pplx-decider-flash-v1.2 tree vs d1-ultra tree | -0.037 [-0.074, +0.000] | 0.0627 |
| pplx-decider-flash-v1.2 tree vs d1-ultra tree_hard | -0.099 [-0.140, -0.057] | 8.58e-06 |
| pplx-decider-flash-v1.2 tree vs d1-ultra tree_v2 | -0.163 [-0.209, -0.113] | 5.31e-10 |
| pplx-decider-flash-v1.2 tree vs microsoft-decision-1 flat | -0.116 [-0.187, -0.047] | 0.00164 |
| pplx-decider-flash-v1.2 tree vs microsoft-decision-1 tree | +0.054 [+0.010, +0.101] | 0.028 |
| pplx-decider-flash-v1.2 tree vs microsoft-decision-1 tree_hard | +0.084 [+0.034, +0.135] | 0.00169 |
| pplx-decider-flash-v1.2 tree vs microsoft-decision-1 tree_v2 | -0.108 [-0.170, -0.044] | 0.00146 |
| pplx-decider-flash-v1.2 tree vs elephant-1 flat | -0.187 [-0.236, -0.138] | 3.19e-12 |
| pplx-decider-flash-v1.2 tree vs elephant-1 tree | -0.005 [-0.037, +0.027] | 0.878 |
| pplx-decider-flash-v1.2 tree vs elephant-1 tree_hard | -0.042 [-0.079, -0.005] | 0.0363 |
| pplx-decider-flash-v1.2 tree vs elephant-1 tree_v2 | -0.128 [-0.175, -0.081] | 2.45e-07 |
| pplx-decider-flash-v1.2 tree vs mammoth-1 flat | -0.192 [-0.251, -0.133] | 6.8e-10 |
| pplx-decider-flash-v1.2 tree vs mammoth-1 tree | -0.017 [-0.054, +0.020] | 0.435 |
| pplx-decider-flash-v1.2 tree vs mammoth-1 tree_hard | -0.059 [-0.101, -0.017] | 0.00877 |
| pplx-decider-flash-v1.2 tree vs mammoth-1 tree_v2 | -0.126 [-0.175, -0.076] | 1.37e-06 |
| pplx-decider-flash-v1.2 tree vs scaledown-classify-1 flat | -0.034 [-0.096, +0.025] | 0.301 |
| pplx-decider-flash-v1.2 tree vs scaledown-classify-1 tree | +0.094 [+0.052, +0.135] | 1.95e-05 |
| pplx-decider-flash-v1.2 tree vs scaledown-classify-1 tree_hard | +0.135 [+0.084, +0.187] | 1.7e-06 |
| pplx-decider-flash-v1.2 tree vs scaledown-classify-1 tree_v2 | +0.067 [+0.020, +0.111] | 0.00731 |
| pplx-decider-flash-v1.2 tree vs gemini-2.5-flash paper_llm | -0.148 [-0.214, -0.084] | 1.6e-05 |
| pplx-decider-flash-v1.2 tree vs gemini-2.5-flash paper_llm_thinking | -0.113 [-0.182, -0.044] | 0.00203 |
| pplx-decider-flash-v1.2 tree vs gemini-3.8-flash paper_llm_low | -0.234 [-0.291, -0.177] | 4.71e-14 |
| pplx-decider-flash-v1.2 tree vs gemini-3.8-flash paper_llm_thinking | -0.202 [-0.261, -0.143] | 1.79e-10 |
| pplx-decider-flash-v1.2 tree_hard vs pplx-decider-flash-v1.2 tree_v2 | -0.108 [-0.153, -0.067] | 2.15e-06 |
| pplx-decider-flash-v1.2 tree_hard vs gpt-6-luna-decisions flat | -0.180 [-0.236, -0.123] | 3.79e-09 |
| pplx-decider-flash-v1.2 tree_hard vs gpt-6-luna-decisions tree | +0.062 [+0.015, +0.108] | 0.0134 |
| pplx-decider-flash-v1.2 tree_hard vs gpt-6-luna-decisions tree_hard | +0.062 [+0.015, +0.108] | 0.0134 |
| pplx-decider-flash-v1.2 tree_hard vs gpt-6-luna-decisions tree_v2 | -0.017 [-0.069, +0.034] | 0.586 |
| pplx-decider-flash-v1.2 tree_hard vs d1 flat | -0.143 [-0.200, -0.084] | 2.47e-06 |
| pplx-decider-flash-v1.2 tree_hard vs d1 tree | +0.034 [-0.007, +0.076] | 0.13 |
| pplx-decider-flash-v1.2 tree_hard vs d1 tree_hard | +0.005 [-0.034, +0.044] | 0.905 |
| pplx-decider-flash-v1.2 tree_hard vs d1 tree_v2 | -0.101 [-0.155, -0.049] | 0.000387 |
| pplx-decider-flash-v1.2 tree_hard vs d1-ultra flat | -0.187 [-0.244, -0.131] | 1.16e-09 |
| pplx-decider-flash-v1.2 tree_hard vs d1-ultra tree | -0.020 [-0.064, +0.025] | 0.445 |
| pplx-decider-flash-v1.2 tree_hard vs d1-ultra tree_hard | -0.081 [-0.123, -0.039] | 0.000264 |
| pplx-decider-flash-v1.2 tree_hard vs d1-ultra tree_v2 | -0.145 [-0.200, -0.091] | 3.96e-07 |
| pplx-decider-flash-v1.2 tree_hard vs microsoft-decision-1 flat | -0.099 [-0.165, -0.032] | 0.00432 |
| pplx-decider-flash-v1.2 tree_hard vs microsoft-decision-1 tree | +0.071 [+0.027, +0.118] | 0.00311 |
| pplx-decider-flash-v1.2 tree_hard vs microsoft-decision-1 tree_hard | +0.101 [+0.054, +0.148] | 6.6e-05 |
| pplx-decider-flash-v1.2 tree_hard vs microsoft-decision-1 tree_v2 | -0.091 [-0.153, -0.029] | 0.00604 |
| pplx-decider-flash-v1.2 tree_hard vs elephant-1 flat | -0.170 [-0.222, -0.118] | 4.2e-10 |
| pplx-decider-flash-v1.2 tree_hard vs elephant-1 tree | +0.012 [-0.027, +0.052] | 0.625 |
| pplx-decider-flash-v1.2 tree_hard vs elephant-1 tree_hard | -0.025 [-0.062, +0.012] | 0.237 |
| pplx-decider-flash-v1.2 tree_hard vs elephant-1 tree_v2 | -0.111 [-0.163, -0.059] | 5.27e-05 |
| pplx-decider-flash-v1.2 tree_hard vs mammoth-1 flat | -0.175 [-0.232, -0.118] | 6.47e-09 |
| pplx-decider-flash-v1.2 tree_hard vs mammoth-1 tree | +0.000 [-0.044, +0.042] | 1 |
| pplx-decider-flash-v1.2 tree_hard vs mammoth-1 tree_hard | -0.042 [-0.086, +0.002] | 0.0893 |
| pplx-decider-flash-v1.2 tree_hard vs mammoth-1 tree_v2 | -0.108 [-0.160, -0.057] | 9.65e-05 |
| pplx-decider-flash-v1.2 tree_hard vs scaledown-classify-1 flat | -0.017 [-0.079, +0.042] | 0.632 |
| pplx-decider-flash-v1.2 tree_hard vs scaledown-classify-1 tree | +0.111 [+0.059, +0.163] | 3.87e-05 |
| pplx-decider-flash-v1.2 tree_hard vs scaledown-classify-1 tree_hard | +0.153 [+0.096, +0.207] | 1.61e-07 |
| pplx-decider-flash-v1.2 tree_hard vs scaledown-classify-1 tree_v2 | +0.084 [+0.032, +0.138] | 0.00363 |
| pplx-decider-flash-v1.2 tree_hard vs gemini-2.5-flash paper_llm | -0.131 [-0.192, -0.069] | 6.83e-05 |
| pplx-decider-flash-v1.2 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.096 [-0.165, -0.030] | 0.00663 |
| pplx-decider-flash-v1.2 tree_hard vs gemini-3.8-flash paper_llm_low | -0.217 [-0.271, -0.163] | 1.53e-13 |
| pplx-decider-flash-v1.2 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.185 [-0.241, -0.128] | 1.02e-09 |
| pplx-decider-flash-v1.2 tree_v2 vs gpt-6-luna-decisions flat | -0.071 [-0.128, -0.015] | 0.0181 |
| pplx-decider-flash-v1.2 tree_v2 vs gpt-6-luna-decisions tree | +0.170 [+0.118, +0.222] | 1.99e-10 |
| pplx-decider-flash-v1.2 tree_v2 vs gpt-6-luna-decisions tree_hard | +0.170 [+0.118, +0.222] | 1.99e-10 |
| pplx-decider-flash-v1.2 tree_v2 vs gpt-6-luna-decisions tree_v2 | +0.091 [+0.044, +0.138] | 0.000158 |
| pplx-decider-flash-v1.2 tree_v2 vs d1 flat | -0.034 [-0.086, +0.020] | 0.235 |
| pplx-decider-flash-v1.2 tree_v2 vs d1 tree | +0.143 [+0.094, +0.192] | 1.88e-08 |
| pplx-decider-flash-v1.2 tree_v2 vs d1 tree_hard | +0.113 [+0.062, +0.165] | 3.24e-05 |
| pplx-decider-flash-v1.2 tree_v2 vs d1 tree_v2 | +0.007 [-0.032, +0.049] | 0.813 |
| pplx-decider-flash-v1.2 tree_v2 vs d1-ultra flat | -0.079 [-0.131, -0.027] | 0.00412 |
| pplx-decider-flash-v1.2 tree_v2 vs d1-ultra tree | +0.089 [+0.044, +0.133] | 0.000157 |
| pplx-decider-flash-v1.2 tree_v2 vs d1-ultra tree_hard | +0.027 [-0.017, +0.074] | 0.294 |
| pplx-decider-flash-v1.2 tree_v2 vs d1-ultra tree_v2 | -0.037 [-0.076, +0.002] | 0.0864 |
| pplx-decider-flash-v1.2 tree_v2 vs microsoft-decision-1 flat | +0.010 [-0.052, +0.071] | 0.816 |
| pplx-decider-flash-v1.2 tree_v2 vs microsoft-decision-1 tree | +0.180 [+0.123, +0.236] | 3.79e-09 |
| pplx-decider-flash-v1.2 tree_v2 vs microsoft-decision-1 tree_hard | +0.209 [+0.150, +0.268] | 7e-11 |
| pplx-decider-flash-v1.2 tree_v2 vs microsoft-decision-1 tree_v2 | +0.017 [-0.037, +0.071] | 0.595 |
| pplx-decider-flash-v1.2 tree_v2 vs elephant-1 flat | -0.062 [-0.103, -0.020] | 0.00523 |
| pplx-decider-flash-v1.2 tree_v2 vs elephant-1 tree | +0.121 [+0.074, +0.167] | 1.12e-06 |
| pplx-decider-flash-v1.2 tree_v2 vs elephant-1 tree_hard | +0.084 [+0.034, +0.133] | 0.00153 |
| pplx-decider-flash-v1.2 tree_v2 vs elephant-1 tree_v2 | -0.002 [-0.037, +0.032] | 1 |
| pplx-decider-flash-v1.2 tree_v2 vs mammoth-1 flat | -0.067 [-0.116, -0.017] | 0.0116 |
| pplx-decider-flash-v1.2 tree_v2 vs mammoth-1 tree | +0.108 [+0.064, +0.153] | 2.15e-06 |
| pplx-decider-flash-v1.2 tree_v2 vs mammoth-1 tree_hard | +0.067 [+0.022, +0.111] | 0.00501 |
| pplx-decider-flash-v1.2 tree_v2 vs mammoth-1 tree_v2 | +0.000 [-0.037, +0.037] | 1 |
| pplx-decider-flash-v1.2 tree_v2 vs scaledown-classify-1 flat | +0.091 [+0.032, +0.148] | 0.00267 |
| pplx-decider-flash-v1.2 tree_v2 vs scaledown-classify-1 tree | +0.219 [+0.167, +0.271] | 1.71e-15 |
| pplx-decider-flash-v1.2 tree_v2 vs scaledown-classify-1 tree_hard | +0.261 [+0.204, +0.318] | 6.9e-17 |
| pplx-decider-flash-v1.2 tree_v2 vs scaledown-classify-1 tree_v2 | +0.192 [+0.143, +0.241] | 2.66e-13 |
| pplx-decider-flash-v1.2 tree_v2 vs gemini-2.5-flash paper_llm | -0.022 [-0.079, +0.037] | 0.507 |
| pplx-decider-flash-v1.2 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.012 [-0.049, +0.076] | 0.757 |
| pplx-decider-flash-v1.2 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.108 [-0.160, -0.057] | 5.4e-05 |
| pplx-decider-flash-v1.2 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.076 [-0.131, -0.022] | 0.00659 |
| gpt-6-luna-decisions flat vs gpt-6-luna-decisions tree | +0.241 [+0.182, +0.303] | 1.15e-13 |
| gpt-6-luna-decisions flat vs gpt-6-luna-decisions tree_hard | +0.241 [+0.182, +0.303] | 1.15e-13 |
| gpt-6-luna-decisions flat vs gpt-6-luna-decisions tree_v2 | +0.163 [+0.103, +0.222] | 2.26e-07 |
| gpt-6-luna-decisions flat vs d1 flat | +0.037 [-0.012, +0.086] | 0.172 |
| gpt-6-luna-decisions flat vs d1 tree | +0.214 [+0.155, +0.276] | 5.38e-11 |
| gpt-6-luna-decisions flat vs d1 tree_hard | +0.185 [+0.126, +0.241] | 3.62e-09 |
| gpt-6-luna-decisions flat vs d1 tree_v2 | +0.079 [+0.022, +0.138] | 0.0111 |
| gpt-6-luna-decisions flat vs d1-ultra flat | -0.007 [-0.057, +0.044] | 0.851 |
| gpt-6-luna-decisions flat vs d1-ultra tree | +0.160 [+0.103, +0.217] | 1.23e-07 |
| gpt-6-luna-decisions flat vs d1-ultra tree_hard | +0.099 [+0.047, +0.150] | 0.000293 |
| gpt-6-luna-decisions flat vs d1-ultra tree_v2 | +0.034 [-0.022, +0.091] | 0.275 |
| gpt-6-luna-decisions flat vs microsoft-decision-1 flat | +0.081 [+0.027, +0.135] | 0.00402 |
| gpt-6-luna-decisions flat vs microsoft-decision-1 tree | +0.251 [+0.197, +0.305] | 6.52e-17 |
| gpt-6-luna-decisions flat vs microsoft-decision-1 tree_hard | +0.281 [+0.227, +0.337] | 4.34e-20 |
| gpt-6-luna-decisions flat vs microsoft-decision-1 tree_v2 | +0.089 [+0.030, +0.150] | 0.00579 |
| gpt-6-luna-decisions flat vs elephant-1 flat | +0.010 [-0.039, +0.059] | 0.764 |
| gpt-6-luna-decisions flat vs elephant-1 tree | +0.192 [+0.133, +0.251] | 2.31e-09 |
| gpt-6-luna-decisions flat vs elephant-1 tree_hard | +0.155 [+0.099, +0.212] | 4.47e-07 |
| gpt-6-luna-decisions flat vs elephant-1 tree_v2 | +0.069 [+0.010, +0.128] | 0.0272 |
| gpt-6-luna-decisions flat vs mammoth-1 flat | +0.005 [-0.047, +0.059] | 0.926 |
| gpt-6-luna-decisions flat vs mammoth-1 tree | +0.180 [+0.123, +0.239] | 7.77e-09 |
| gpt-6-luna-decisions flat vs mammoth-1 tree_hard | +0.138 [+0.086, +0.190] | 9.7e-07 |
| gpt-6-luna-decisions flat vs mammoth-1 tree_v2 | +0.071 [+0.012, +0.131] | 0.0215 |
| gpt-6-luna-decisions flat vs scaledown-classify-1 flat | +0.163 [+0.108, +0.217] | 1.69e-08 |
| gpt-6-luna-decisions flat vs scaledown-classify-1 tree | +0.291 [+0.227, +0.355] | 1.42e-16 |
| gpt-6-luna-decisions flat vs scaledown-classify-1 tree_hard | +0.333 [+0.273, +0.392] | 5.58e-23 |
| gpt-6-luna-decisions flat vs scaledown-classify-1 tree_v2 | +0.264 [+0.200, +0.328] | 2.44e-14 |
| gpt-6-luna-decisions flat vs gemini-2.5-flash paper_llm | +0.049 [-0.005, +0.103] | 0.0901 |
| gpt-6-luna-decisions flat vs gemini-2.5-flash paper_llm_thinking | +0.084 [+0.027, +0.143] | 0.00577 |
| gpt-6-luna-decisions flat vs gemini-3.8-flash paper_llm_low | -0.037 [-0.081, +0.007] | 0.128 |
| gpt-6-luna-decisions flat vs gemini-3.8-flash paper_llm_thinking | -0.005 [-0.052, +0.042] | 0.92 |
| gpt-6-luna-decisions tree vs gpt-6-luna-decisions tree_hard | +0.000 [+0.000, +0.000] | 1 |
| gpt-6-luna-decisions tree vs gpt-6-luna-decisions tree_v2 | -0.079 [-0.108, -0.049] | 1.86e-07 |
| gpt-6-luna-decisions tree vs d1 flat | -0.204 [-0.266, -0.143] | 6.9e-10 |
| gpt-6-luna-decisions tree vs d1 tree | -0.027 [-0.059, +0.005] | 0.135 |
| gpt-6-luna-decisions tree vs d1 tree_hard | -0.057 [-0.099, -0.015] | 0.0106 |
| gpt-6-luna-decisions tree vs d1 tree_v2 | -0.163 [-0.209, -0.116] | 1.55e-10 |
| gpt-6-luna-decisions tree vs d1-ultra flat | -0.249 [-0.308, -0.187] | 3.06e-14 |
| gpt-6-luna-decisions tree vs d1-ultra tree | -0.081 [-0.121, -0.044] | 3.76e-05 |
| gpt-6-luna-decisions tree vs d1-ultra tree_hard | -0.143 [-0.192, -0.094] | 2.61e-08 |
| gpt-6-luna-decisions tree vs d1-ultra tree_v2 | -0.207 [-0.256, -0.155] | 3.79e-14 |
| gpt-6-luna-decisions tree vs microsoft-decision-1 flat | -0.160 [-0.234, -0.086] | 3.38e-05 |
| gpt-6-luna-decisions tree vs microsoft-decision-1 tree | +0.010 [-0.039, +0.059] | 0.769 |
| gpt-6-luna-decisions tree vs microsoft-decision-1 tree_hard | +0.039 [-0.012, +0.094] | 0.178 |
| gpt-6-luna-decisions tree vs microsoft-decision-1 tree_v2 | -0.153 [-0.219, -0.086] | 1.25e-05 |
| gpt-6-luna-decisions tree vs elephant-1 flat | -0.232 [-0.283, -0.177] | 1.24e-15 |
| gpt-6-luna-decisions tree vs elephant-1 tree | -0.049 [-0.079, -0.020] | 0.00222 |
| gpt-6-luna-decisions tree vs elephant-1 tree_hard | -0.086 [-0.128, -0.044] | 0.000103 |
| gpt-6-luna-decisions tree vs elephant-1 tree_v2 | -0.172 [-0.219, -0.126] | 5.13e-12 |
| gpt-6-luna-decisions tree vs mammoth-1 flat | -0.236 [-0.296, -0.177] | 1.94e-13 |
| gpt-6-luna-decisions tree vs mammoth-1 tree | -0.062 [-0.099, -0.025] | 0.00187 |
| gpt-6-luna-decisions tree vs mammoth-1 tree_hard | -0.103 [-0.150, -0.057] | 2.15e-05 |
| gpt-6-luna-decisions tree vs mammoth-1 tree_v2 | -0.170 [-0.219, -0.118] | 1.34e-10 |
| gpt-6-luna-decisions tree vs scaledown-classify-1 flat | -0.079 [-0.138, -0.020] | 0.0117 |
| gpt-6-luna-decisions tree vs scaledown-classify-1 tree | +0.049 [+0.017, +0.081] | 0.00289 |
| gpt-6-luna-decisions tree vs scaledown-classify-1 tree_hard | +0.091 [+0.039, +0.143] | 0.00131 |
| gpt-6-luna-decisions tree vs scaledown-classify-1 tree_v2 | +0.022 [-0.015, +0.059] | 0.298 |
| gpt-6-luna-decisions tree vs gemini-2.5-flash paper_llm | -0.192 [-0.259, -0.128] | 2.98e-08 |
| gpt-6-luna-decisions tree vs gemini-2.5-flash paper_llm_thinking | -0.158 [-0.232, -0.086] | 3.44e-05 |
| gpt-6-luna-decisions tree vs gemini-3.8-flash paper_llm_low | -0.278 [-0.337, -0.217] | 1.56e-17 |
| gpt-6-luna-decisions tree vs gemini-3.8-flash paper_llm_thinking | -0.246 [-0.305, -0.185] | 6.76e-14 |
| gpt-6-luna-decisions tree_hard vs gpt-6-luna-decisions tree_v2 | -0.079 [-0.108, -0.049] | 1.86e-07 |
| gpt-6-luna-decisions tree_hard vs d1 flat | -0.204 [-0.266, -0.143] | 6.9e-10 |
| gpt-6-luna-decisions tree_hard vs d1 tree | -0.027 [-0.059, +0.005] | 0.135 |
| gpt-6-luna-decisions tree_hard vs d1 tree_hard | -0.057 [-0.099, -0.015] | 0.0106 |
| gpt-6-luna-decisions tree_hard vs d1 tree_v2 | -0.163 [-0.209, -0.116] | 1.55e-10 |
| gpt-6-luna-decisions tree_hard vs d1-ultra flat | -0.249 [-0.308, -0.187] | 3.06e-14 |
| gpt-6-luna-decisions tree_hard vs d1-ultra tree | -0.081 [-0.121, -0.044] | 3.76e-05 |
| gpt-6-luna-decisions tree_hard vs d1-ultra tree_hard | -0.143 [-0.192, -0.094] | 2.61e-08 |
| gpt-6-luna-decisions tree_hard vs d1-ultra tree_v2 | -0.207 [-0.256, -0.155] | 3.79e-14 |
| gpt-6-luna-decisions tree_hard vs microsoft-decision-1 flat | -0.160 [-0.234, -0.086] | 3.38e-05 |
| gpt-6-luna-decisions tree_hard vs microsoft-decision-1 tree | +0.010 [-0.039, +0.059] | 0.769 |
| gpt-6-luna-decisions tree_hard vs microsoft-decision-1 tree_hard | +0.039 [-0.012, +0.094] | 0.178 |
| gpt-6-luna-decisions tree_hard vs microsoft-decision-1 tree_v2 | -0.153 [-0.219, -0.086] | 1.25e-05 |
| gpt-6-luna-decisions tree_hard vs elephant-1 flat | -0.232 [-0.283, -0.177] | 1.24e-15 |
| gpt-6-luna-decisions tree_hard vs elephant-1 tree | -0.049 [-0.079, -0.020] | 0.00222 |
| gpt-6-luna-decisions tree_hard vs elephant-1 tree_hard | -0.086 [-0.128, -0.044] | 0.000103 |
| gpt-6-luna-decisions tree_hard vs elephant-1 tree_v2 | -0.172 [-0.219, -0.126] | 5.13e-12 |
| gpt-6-luna-decisions tree_hard vs mammoth-1 flat | -0.236 [-0.296, -0.177] | 1.94e-13 |
| gpt-6-luna-decisions tree_hard vs mammoth-1 tree | -0.062 [-0.099, -0.025] | 0.00187 |
| gpt-6-luna-decisions tree_hard vs mammoth-1 tree_hard | -0.103 [-0.150, -0.057] | 2.15e-05 |
| gpt-6-luna-decisions tree_hard vs mammoth-1 tree_v2 | -0.170 [-0.219, -0.118] | 1.34e-10 |
| gpt-6-luna-decisions tree_hard vs scaledown-classify-1 flat | -0.079 [-0.138, -0.020] | 0.0117 |
| gpt-6-luna-decisions tree_hard vs scaledown-classify-1 tree | +0.049 [+0.017, +0.081] | 0.00289 |
| gpt-6-luna-decisions tree_hard vs scaledown-classify-1 tree_hard | +0.091 [+0.039, +0.143] | 0.00131 |
| gpt-6-luna-decisions tree_hard vs scaledown-classify-1 tree_v2 | +0.022 [-0.015, +0.059] | 0.298 |
| gpt-6-luna-decisions tree_hard vs gemini-2.5-flash paper_llm | -0.192 [-0.259, -0.128] | 2.98e-08 |
| gpt-6-luna-decisions tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.158 [-0.232, -0.086] | 3.44e-05 |
| gpt-6-luna-decisions tree_hard vs gemini-3.8-flash paper_llm_low | -0.278 [-0.337, -0.217] | 1.56e-17 |
| gpt-6-luna-decisions tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.246 [-0.305, -0.185] | 6.76e-14 |
| gpt-6-luna-decisions tree_v2 vs d1 flat | -0.126 [-0.182, -0.064] | 5.74e-05 |
| gpt-6-luna-decisions tree_v2 vs d1 tree | +0.052 [+0.010, +0.094] | 0.0238 |
| gpt-6-luna-decisions tree_v2 vs d1 tree_hard | +0.022 [-0.027, +0.071] | 0.431 |
| gpt-6-luna-decisions tree_v2 vs d1 tree_v2 | -0.084 [-0.126, -0.042] | 0.000149 |
| gpt-6-luna-decisions tree_v2 vs d1-ultra flat | -0.170 [-0.227, -0.111] | 1.79e-08 |
| gpt-6-luna-decisions tree_v2 vs d1-ultra tree | -0.002 [-0.044, +0.039] | 1 |
| gpt-6-luna-decisions tree_v2 vs d1-ultra tree_hard | -0.064 [-0.113, -0.012] | 0.0167 |
| gpt-6-luna-decisions tree_v2 vs d1-ultra tree_v2 | -0.128 [-0.172, -0.081] | 9.44e-08 |
| gpt-6-luna-decisions tree_v2 vs microsoft-decision-1 flat | -0.081 [-0.150, -0.010] | 0.0274 |
| gpt-6-luna-decisions tree_v2 vs microsoft-decision-1 tree | +0.089 [+0.032, +0.148] | 0.00339 |
| gpt-6-luna-decisions tree_v2 vs microsoft-decision-1 tree_hard | +0.118 [+0.059, +0.180] | 0.000221 |
| gpt-6-luna-decisions tree_v2 vs microsoft-decision-1 tree_v2 | -0.074 [-0.133, -0.012] | 0.0232 |
| gpt-6-luna-decisions tree_v2 vs elephant-1 flat | -0.153 [-0.202, -0.101] | 1.65e-08 |
| gpt-6-luna-decisions tree_v2 vs elephant-1 tree | +0.030 [-0.012, +0.071] | 0.201 |
| gpt-6-luna-decisions tree_v2 vs elephant-1 tree_hard | -0.007 [-0.054, +0.042] | 0.844 |
| gpt-6-luna-decisions tree_v2 vs elephant-1 tree_v2 | -0.094 [-0.135, -0.052] | 1.95e-05 |
| gpt-6-luna-decisions tree_v2 vs mammoth-1 flat | -0.158 [-0.214, -0.101] | 1.17e-07 |
| gpt-6-luna-decisions tree_v2 vs mammoth-1 tree | +0.017 [-0.022, +0.057] | 0.477 |
| gpt-6-luna-decisions tree_v2 vs mammoth-1 tree_hard | -0.025 [-0.069, +0.020] | 0.343 |
| gpt-6-luna-decisions tree_v2 vs mammoth-1 tree_v2 | -0.091 [-0.133, -0.047] | 7.4e-05 |
| gpt-6-luna-decisions tree_v2 vs scaledown-classify-1 flat | +0.000 [-0.057, +0.057] | 1 |
| gpt-6-luna-decisions tree_v2 vs scaledown-classify-1 tree | +0.128 [+0.089, +0.167] | 5.32e-10 |
| gpt-6-luna-decisions tree_v2 vs scaledown-classify-1 tree_hard | +0.170 [+0.116, +0.224] | 8.6e-09 |
| gpt-6-luna-decisions tree_v2 vs scaledown-classify-1 tree_v2 | +0.101 [+0.062, +0.143] | 1.53e-06 |
| gpt-6-luna-decisions tree_v2 vs gemini-2.5-flash paper_llm | -0.113 [-0.175, -0.052] | 0.00052 |
| gpt-6-luna-decisions tree_v2 vs gemini-2.5-flash paper_llm_thinking | -0.079 [-0.148, -0.012] | 0.0289 |
| gpt-6-luna-decisions tree_v2 vs gemini-3.8-flash paper_llm_low | -0.200 [-0.256, -0.140] | 1.55e-10 |
| gpt-6-luna-decisions tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.167 [-0.227, -0.108] | 9.23e-08 |
| d1 flat vs d1 tree | +0.177 [+0.116, +0.236] | 2.17e-08 |
| d1 flat vs d1 tree_hard | +0.148 [+0.089, +0.204] | 1.06e-06 |
| d1 flat vs d1 tree_v2 | +0.042 [-0.010, +0.094] | 0.132 |
| d1 flat vs d1-ultra flat | -0.044 [-0.084, -0.005] | 0.0385 |
| d1 flat vs d1-ultra tree | +0.123 [+0.064, +0.180] | 5.45e-05 |
| d1 flat vs d1-ultra tree_hard | +0.062 [+0.007, +0.113] | 0.0274 |
| d1 flat vs d1-ultra tree_v2 | -0.002 [-0.054, +0.049] | 1 |
| d1 flat vs microsoft-decision-1 flat | +0.044 [-0.005, +0.096] | 0.0982 |
| d1 flat vs microsoft-decision-1 tree | +0.214 [+0.153, +0.276] | 9.07e-11 |
| d1 flat vs microsoft-decision-1 tree_hard | +0.244 [+0.182, +0.303] | 1.05e-13 |
| d1 flat vs microsoft-decision-1 tree_v2 | +0.052 [-0.007, +0.111] | 0.103 |
| d1 flat vs elephant-1 flat | -0.027 [-0.069, +0.017] | 0.26 |
| d1 flat vs elephant-1 tree | +0.155 [+0.094, +0.217] | 1.41e-06 |
| d1 flat vs elephant-1 tree_hard | +0.118 [+0.059, +0.177] | 0.000166 |
| d1 flat vs elephant-1 tree_v2 | +0.032 [-0.025, +0.089] | 0.298 |
| d1 flat vs mammoth-1 flat | -0.032 [-0.074, +0.010] | 0.16 |
| d1 flat vs mammoth-1 tree | +0.143 [+0.084, +0.202] | 3.94e-06 |
| d1 flat vs mammoth-1 tree_hard | +0.101 [+0.047, +0.155] | 0.000276 |
| d1 flat vs mammoth-1 tree_v2 | +0.034 [-0.020, +0.089] | 0.239 |
| d1 flat vs scaledown-classify-1 flat | +0.126 [+0.067, +0.187] | 7.15e-05 |
| d1 flat vs scaledown-classify-1 tree | +0.254 [+0.190, +0.318] | 1.81e-13 |
| d1 flat vs scaledown-classify-1 tree_hard | +0.296 [+0.236, +0.355] | 6.64e-20 |
| d1 flat vs scaledown-classify-1 tree_v2 | +0.227 [+0.163, +0.288] | 9.4e-12 |
| d1 flat vs gemini-2.5-flash paper_llm | +0.012 [-0.039, +0.062] | 0.707 |
| d1 flat vs gemini-2.5-flash paper_llm_thinking | +0.047 [-0.005, +0.099] | 0.0985 |
| d1 flat vs gemini-3.8-flash paper_llm_low | -0.074 [-0.118, -0.030] | 0.00182 |
| d1 flat vs gemini-3.8-flash paper_llm_thinking | -0.042 [-0.089, +0.005] | 0.0893 |
| d1 tree vs d1 tree_hard | -0.030 [-0.059, +0.000] | 0.073 |
| d1 tree vs d1 tree_v2 | -0.135 [-0.175, -0.096] | 2.38e-11 |
| d1 tree vs d1-ultra flat | -0.222 [-0.281, -0.163] | 2.63e-12 |
| d1 tree vs d1-ultra tree | -0.054 [-0.089, -0.020] | 0.00319 |
| d1 tree vs d1-ultra tree_hard | -0.116 [-0.163, -0.069] | 1.46e-06 |
| d1 tree vs d1-ultra tree_v2 | -0.180 [-0.229, -0.131] | 8.54e-12 |
| d1 tree vs microsoft-decision-1 flat | -0.133 [-0.207, -0.059] | 0.000476 |
| d1 tree vs microsoft-decision-1 tree | +0.037 [-0.007, +0.084] | 0.142 |
| d1 tree vs microsoft-decision-1 tree_hard | +0.067 [+0.017, +0.118] | 0.0132 |
| d1 tree vs microsoft-decision-1 tree_v2 | -0.126 [-0.190, -0.059] | 0.000218 |
| d1 tree vs elephant-1 flat | -0.204 [-0.256, -0.153] | 6.81e-13 |
| d1 tree vs elephant-1 tree | -0.022 [-0.052, +0.007] | 0.188 |
| d1 tree vs elephant-1 tree_hard | -0.059 [-0.099, -0.020] | 0.0049 |
| d1 tree vs elephant-1 tree_v2 | -0.145 [-0.192, -0.099] | 2.73e-09 |
| d1 tree vs mammoth-1 flat | -0.209 [-0.268, -0.150] | 2.2e-11 |
| d1 tree vs mammoth-1 tree | -0.034 [-0.069, +0.000] | 0.0704 |
| d1 tree vs mammoth-1 tree_hard | -0.076 [-0.118, -0.034] | 0.00045 |
| d1 tree vs mammoth-1 tree_v2 | -0.143 [-0.190, -0.094] | 1.88e-08 |
| d1 tree vs scaledown-classify-1 flat | -0.052 [-0.111, +0.010] | 0.108 |
| d1 tree vs scaledown-classify-1 tree | +0.076 [+0.039, +0.113] | 8.84e-05 |
| d1 tree vs scaledown-classify-1 tree_hard | +0.118 [+0.067, +0.170] | 2.28e-05 |
| d1 tree vs scaledown-classify-1 tree_v2 | +0.049 [+0.007, +0.094] | 0.033 |
| d1 tree vs gemini-2.5-flash paper_llm | -0.165 [-0.229, -0.101] | 1.08e-06 |
| d1 tree vs gemini-2.5-flash paper_llm_thinking | -0.131 [-0.202, -0.059] | 0.000417 |
| d1 tree vs gemini-3.8-flash paper_llm_low | -0.251 [-0.310, -0.192] | 4.23e-15 |
| d1 tree vs gemini-3.8-flash paper_llm_thinking | -0.219 [-0.278, -0.160] | 5.54e-12 |
| d1 tree_hard vs d1 tree_v2 | -0.106 [-0.148, -0.064] | 3.28e-06 |
| d1 tree_hard vs d1-ultra flat | -0.192 [-0.246, -0.135] | 1.22e-10 |
| d1 tree_hard vs d1-ultra tree | -0.025 [-0.064, +0.017] | 0.282 |
| d1 tree_hard vs d1-ultra tree_hard | -0.086 [-0.131, -0.042] | 0.000155 |
| d1 tree_hard vs d1-ultra tree_v2 | -0.150 [-0.202, -0.096] | 7.34e-08 |
| d1 tree_hard vs microsoft-decision-1 flat | -0.103 [-0.172, -0.034] | 0.00363 |
| d1 tree_hard vs microsoft-decision-1 tree | +0.067 [+0.020, +0.113] | 0.00731 |
| d1 tree_hard vs microsoft-decision-1 tree_hard | +0.096 [+0.049, +0.145] | 0.000206 |
| d1 tree_hard vs microsoft-decision-1 tree_v2 | -0.096 [-0.160, -0.032] | 0.00483 |
| d1 tree_hard vs elephant-1 flat | -0.175 [-0.227, -0.123] | 4.91e-10 |
| d1 tree_hard vs elephant-1 tree | +0.007 [-0.030, +0.044] | 0.795 |
| d1 tree_hard vs elephant-1 tree_hard | -0.030 [-0.069, +0.012] | 0.188 |
| d1 tree_hard vs elephant-1 tree_v2 | -0.116 [-0.167, -0.064] | 2.72e-05 |
| d1 tree_hard vs mammoth-1 flat | -0.180 [-0.234, -0.123] | 9.91e-10 |
| d1 tree_hard vs mammoth-1 tree | -0.005 [-0.047, +0.037] | 0.91 |
| d1 tree_hard vs mammoth-1 tree_hard | -0.047 [-0.091, +0.000] | 0.0558 |
| d1 tree_hard vs mammoth-1 tree_v2 | -0.113 [-0.165, -0.062] | 4.41e-05 |
| d1 tree_hard vs scaledown-classify-1 flat | -0.022 [-0.081, +0.037] | 0.515 |
| d1 tree_hard vs scaledown-classify-1 tree | +0.106 [+0.059, +0.153] | 1.48e-05 |
| d1 tree_hard vs scaledown-classify-1 tree_hard | +0.148 [+0.094, +0.202] | 1.75e-07 |
| d1 tree_hard vs scaledown-classify-1 tree_v2 | +0.079 [+0.030, +0.131] | 0.00294 |
| d1 tree_hard vs gemini-2.5-flash paper_llm | -0.135 [-0.200, -0.071] | 4.32e-05 |
| d1 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.101 [-0.170, -0.034] | 0.00426 |
| d1 tree_hard vs gemini-3.8-flash paper_llm_low | -0.222 [-0.276, -0.165] | 9.21e-14 |
| d1 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.190 [-0.244, -0.133] | 1.87e-10 |
| d1 tree_v2 vs d1-ultra flat | -0.086 [-0.135, -0.034] | 0.00128 |
| d1 tree_v2 vs d1-ultra tree | +0.081 [+0.039, +0.126] | 0.000524 |
| d1 tree_v2 vs d1-ultra tree_hard | +0.020 [-0.027, +0.069] | 0.488 |
| d1 tree_v2 vs d1-ultra tree_v2 | -0.044 [-0.084, -0.005] | 0.0356 |
| d1 tree_v2 vs microsoft-decision-1 flat | +0.002 [-0.062, +0.069] | 1 |
| d1 tree_v2 vs microsoft-decision-1 tree | +0.172 [+0.113, +0.229] | 2.4e-08 |
| d1 tree_v2 vs microsoft-decision-1 tree_hard | +0.202 [+0.140, +0.261] | 4.99e-10 |
| d1 tree_v2 vs microsoft-decision-1 tree_v2 | +0.010 [-0.042, +0.064] | 0.791 |
| d1 tree_v2 vs elephant-1 flat | -0.069 [-0.116, -0.022] | 0.00461 |
| d1 tree_v2 vs elephant-1 tree | +0.113 [+0.067, +0.160] | 5.91e-06 |
| d1 tree_v2 vs elephant-1 tree_hard | +0.076 [+0.027, +0.126] | 0.00353 |
| d1 tree_v2 vs elephant-1 tree_v2 | -0.010 [-0.047, +0.027] | 0.699 |
| d1 tree_v2 vs mammoth-1 flat | -0.074 [-0.123, -0.025] | 0.00423 |
| d1 tree_v2 vs mammoth-1 tree | +0.101 [+0.059, +0.145] | 7.51e-06 |
| d1 tree_v2 vs mammoth-1 tree_hard | +0.059 [+0.017, +0.101] | 0.00877 |
| d1 tree_v2 vs mammoth-1 tree_v2 | -0.007 [-0.044, +0.030] | 0.791 |
| d1 tree_v2 vs scaledown-classify-1 flat | +0.084 [+0.030, +0.138] | 0.00448 |
| d1 tree_v2 vs scaledown-classify-1 tree | +0.212 [+0.163, +0.261] | 3.41e-16 |
| d1 tree_v2 vs scaledown-classify-1 tree_hard | +0.254 [+0.197, +0.310] | 1.83e-16 |
| d1 tree_v2 vs scaledown-classify-1 tree_v2 | +0.185 [+0.138, +0.232] | 2.26e-13 |
| d1 tree_v2 vs gemini-2.5-flash paper_llm | -0.030 [-0.089, +0.027] | 0.363 |
| d1 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.005 [-0.059, +0.067] | 0.939 |
| d1 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.116 [-0.167, -0.064] | 2.72e-05 |
| d1 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.084 [-0.135, -0.032] | 0.00245 |
| d1-ultra flat vs d1-ultra tree | +0.167 [+0.108, +0.224] | 3.27e-08 |
| d1-ultra flat vs d1-ultra tree_hard | +0.106 [+0.054, +0.155] | 7.52e-05 |
| d1-ultra flat vs d1-ultra tree_v2 | +0.042 [-0.005, +0.089] | 0.104 |
| d1-ultra flat vs microsoft-decision-1 flat | +0.089 [+0.037, +0.140] | 0.00118 |
| d1-ultra flat vs microsoft-decision-1 tree | +0.259 [+0.197, +0.320] | 4.16e-14 |
| d1-ultra flat vs microsoft-decision-1 tree_hard | +0.288 [+0.224, +0.350] | 7.17e-17 |
| d1-ultra flat vs microsoft-decision-1 tree_v2 | +0.096 [+0.042, +0.150] | 0.000913 |
| d1-ultra flat vs elephant-1 flat | +0.017 [-0.025, +0.059] | 0.5 |
| d1-ultra flat vs elephant-1 tree | +0.200 [+0.138, +0.261] | 9.3e-10 |
| d1-ultra flat vs elephant-1 tree_hard | +0.163 [+0.101, +0.222] | 3.21e-07 |
| d1-ultra flat vs elephant-1 tree_v2 | +0.076 [+0.022, +0.128] | 0.00705 |
| d1-ultra flat vs mammoth-1 flat | +0.012 [-0.020, +0.044] | 0.551 |
| d1-ultra flat vs mammoth-1 tree | +0.187 [+0.128, +0.244] | 6.78e-10 |
| d1-ultra flat vs mammoth-1 tree_hard | +0.145 [+0.096, +0.195] | 4.28e-08 |
| d1-ultra flat vs mammoth-1 tree_v2 | +0.079 [+0.027, +0.128] | 0.00322 |
| d1-ultra flat vs scaledown-classify-1 flat | +0.170 [+0.113, +0.227] | 8.6e-09 |
| d1-ultra flat vs scaledown-classify-1 tree | +0.298 [+0.236, +0.357] | 5.26e-19 |
| d1-ultra flat vs scaledown-classify-1 tree_hard | +0.340 [+0.278, +0.399] | 2.15e-23 |
| d1-ultra flat vs scaledown-classify-1 tree_v2 | +0.271 [+0.212, +0.328] | 2.59e-17 |
| d1-ultra flat vs gemini-2.5-flash paper_llm | +0.057 [+0.007, +0.103] | 0.0265 |
| d1-ultra flat vs gemini-2.5-flash paper_llm_thinking | +0.091 [+0.042, +0.140] | 0.000505 |
| d1-ultra flat vs gemini-3.8-flash paper_llm_low | -0.030 [-0.074, +0.015] | 0.224 |
| d1-ultra flat vs gemini-3.8-flash paper_llm_thinking | +0.002 [-0.039, +0.044] | 1 |
| d1-ultra tree vs d1-ultra tree_hard | -0.062 [-0.101, -0.025] | 0.00223 |
| d1-ultra tree vs d1-ultra tree_v2 | -0.126 [-0.165, -0.086] | 3.02e-09 |
| d1-ultra tree vs microsoft-decision-1 flat | -0.079 [-0.148, -0.010] | 0.0313 |
| d1-ultra tree vs microsoft-decision-1 tree | +0.091 [+0.042, +0.140] | 0.000505 |
| d1-ultra tree vs microsoft-decision-1 tree_hard | +0.121 [+0.067, +0.175] | 1.91e-05 |
| d1-ultra tree vs microsoft-decision-1 tree_v2 | -0.071 [-0.133, -0.007] | 0.0309 |
| d1-ultra tree vs elephant-1 flat | -0.150 [-0.200, -0.101] | 7.12e-09 |
| d1-ultra tree vs elephant-1 tree | +0.032 [-0.002, +0.067] | 0.0984 |
| d1-ultra tree vs elephant-1 tree_hard | -0.005 [-0.047, +0.037] | 0.906 |
| d1-ultra tree vs elephant-1 tree_v2 | -0.091 [-0.135, -0.049] | 7.4e-05 |
| d1-ultra tree vs mammoth-1 flat | -0.155 [-0.209, -0.099] | 1.37e-07 |
| d1-ultra tree vs mammoth-1 tree | +0.020 [-0.010, +0.052] | 0.268 |
| d1-ultra tree vs mammoth-1 tree_hard | -0.022 [-0.062, +0.017] | 0.321 |
| d1-ultra tree vs mammoth-1 tree_v2 | -0.089 [-0.133, -0.044] | 0.000157 |
| d1-ultra tree vs scaledown-classify-1 flat | +0.002 [-0.057, +0.062] | 1 |
| d1-ultra tree vs scaledown-classify-1 tree | +0.131 [+0.091, +0.172] | 5.92e-10 |
| d1-ultra tree vs scaledown-classify-1 tree_hard | +0.172 [+0.118, +0.227] | 2.56e-09 |
| d1-ultra tree vs scaledown-classify-1 tree_v2 | +0.103 [+0.059, +0.148] | 6.54e-06 |
| d1-ultra tree vs gemini-2.5-flash paper_llm | -0.111 [-0.175, -0.047] | 0.000953 |
| d1-ultra tree vs gemini-2.5-flash paper_llm_thinking | -0.076 [-0.143, -0.007] | 0.0341 |
| d1-ultra tree vs gemini-3.8-flash paper_llm_low | -0.197 [-0.254, -0.140] | 7.16e-11 |
| d1-ultra tree vs gemini-3.8-flash paper_llm_thinking | -0.165 [-0.222, -0.106] | 5.91e-08 |
| d1-ultra tree_hard vs d1-ultra tree_v2 | -0.064 [-0.111, -0.017] | 0.00878 |
| d1-ultra tree_hard vs microsoft-decision-1 flat | -0.017 [-0.079, +0.044] | 0.636 |
| d1-ultra tree_hard vs microsoft-decision-1 tree | +0.153 [+0.103, +0.202] | 4.59e-09 |
| d1-ultra tree_hard vs microsoft-decision-1 tree_hard | +0.182 [+0.131, +0.234] | 4.43e-11 |
| d1-ultra tree_hard vs microsoft-decision-1 tree_v2 | -0.010 [-0.069, +0.049] | 0.811 |
| d1-ultra tree_hard vs elephant-1 flat | -0.089 [-0.133, -0.044] | 0.00013 |
| d1-ultra tree_hard vs elephant-1 tree | +0.094 [+0.047, +0.140] | 9.26e-05 |
| d1-ultra tree_hard vs elephant-1 tree_hard | +0.057 [+0.010, +0.103] | 0.0206 |
| d1-ultra tree_hard vs elephant-1 tree_v2 | -0.030 [-0.079, +0.020] | 0.285 |
| d1-ultra tree_hard vs mammoth-1 flat | -0.094 [-0.145, -0.044] | 0.000421 |
| d1-ultra tree_hard vs mammoth-1 tree | +0.081 [+0.039, +0.123] | 0.000176 |
| d1-ultra tree_hard vs mammoth-1 tree_hard | +0.039 [+0.002, +0.076] | 0.044 |
| d1-ultra tree_hard vs mammoth-1 tree_v2 | -0.027 [-0.076, +0.022] | 0.329 |
| d1-ultra tree_hard vs scaledown-classify-1 flat | +0.064 [+0.005, +0.123] | 0.0436 |
| d1-ultra tree_hard vs scaledown-classify-1 tree | +0.192 [+0.138, +0.246] | 1.05e-11 |
| d1-ultra tree_hard vs scaledown-classify-1 tree_hard | +0.234 [+0.177, +0.288] | 1.35e-14 |
| d1-ultra tree_hard vs scaledown-classify-1 tree_v2 | +0.165 [+0.111, +0.219] | 1.47e-08 |
| d1-ultra tree_hard vs gemini-2.5-flash paper_llm | -0.049 [-0.106, +0.007] | 0.108 |
| d1-ultra tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.015 [-0.076, +0.047] | 0.696 |
| d1-ultra tree_hard vs gemini-3.8-flash paper_llm_low | -0.135 [-0.182, -0.089] | 9.37e-08 |
| d1-ultra tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.103 [-0.153, -0.054] | 8.98e-05 |
| d1-ultra tree_v2 vs microsoft-decision-1 flat | +0.047 [-0.015, +0.111] | 0.163 |
| d1-ultra tree_v2 vs microsoft-decision-1 tree | +0.217 [+0.155, +0.278] | 4.71e-11 |
| d1-ultra tree_v2 vs microsoft-decision-1 tree_hard | +0.246 [+0.182, +0.310] | 8.39e-13 |
| d1-ultra tree_v2 vs microsoft-decision-1 tree_v2 | +0.054 [+0.002, +0.108] | 0.0527 |
| d1-ultra tree_v2 vs elephant-1 flat | -0.025 [-0.067, +0.020] | 0.314 |
| d1-ultra tree_v2 vs elephant-1 tree | +0.158 [+0.106, +0.209] | 9.61e-09 |
| d1-ultra tree_v2 vs elephant-1 tree_hard | +0.121 [+0.069, +0.175] | 2.23e-05 |
| d1-ultra tree_v2 vs elephant-1 tree_v2 | +0.034 [-0.005, +0.074] | 0.103 |
| d1-ultra tree_v2 vs mammoth-1 flat | -0.030 [-0.074, +0.017] | 0.251 |
| d1-ultra tree_v2 vs mammoth-1 tree | +0.145 [+0.101, +0.190] | 4.45e-10 |
| d1-ultra tree_v2 vs mammoth-1 tree_hard | +0.103 [+0.062, +0.148] | 6.54e-06 |
| d1-ultra tree_v2 vs mammoth-1 tree_v2 | +0.037 [+0.005, +0.069] | 0.0315 |
| d1-ultra tree_v2 vs scaledown-classify-1 flat | +0.128 [+0.071, +0.185] | 1.13e-05 |
| d1-ultra tree_v2 vs scaledown-classify-1 tree | +0.256 [+0.204, +0.305] | 6.91e-21 |
| d1-ultra tree_v2 vs scaledown-classify-1 tree_hard | +0.298 [+0.236, +0.360] | 2.11e-18 |
| d1-ultra tree_v2 vs scaledown-classify-1 tree_v2 | +0.229 [+0.182, +0.276] | 1.04e-19 |
| d1-ultra tree_v2 vs gemini-2.5-flash paper_llm | +0.015 [-0.042, +0.071] | 0.668 |
| d1-ultra tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.049 [-0.012, +0.111] | 0.13 |
| d1-ultra tree_v2 vs gemini-3.8-flash paper_llm_low | -0.071 [-0.123, -0.020] | 0.00934 |
| d1-ultra tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.039 [-0.091, +0.015] | 0.171 |
| microsoft-decision-1 flat vs microsoft-decision-1 tree | +0.170 [+0.108, +0.234] | 1.93e-07 |
| microsoft-decision-1 flat vs microsoft-decision-1 tree_hard | +0.200 [+0.143, +0.256] | 3.4e-11 |
| microsoft-decision-1 flat vs microsoft-decision-1 tree_v2 | +0.007 [-0.047, +0.062] | 0.859 |
| microsoft-decision-1 flat vs elephant-1 flat | -0.071 [-0.126, -0.017] | 0.012 |
| microsoft-decision-1 flat vs elephant-1 tree | +0.111 [+0.037, +0.185] | 0.00341 |
| microsoft-decision-1 flat vs elephant-1 tree_hard | +0.074 [+0.007, +0.140] | 0.0371 |
| microsoft-decision-1 flat vs elephant-1 tree_v2 | -0.012 [-0.079, +0.054] | 0.766 |
| microsoft-decision-1 flat vs mammoth-1 flat | -0.076 [-0.128, -0.025] | 0.00532 |
| microsoft-decision-1 flat vs mammoth-1 tree | +0.099 [+0.027, +0.167] | 0.00753 |
| microsoft-decision-1 flat vs mammoth-1 tree_hard | +0.057 [-0.010, +0.121] | 0.0998 |
| microsoft-decision-1 flat vs mammoth-1 tree_v2 | -0.010 [-0.076, +0.054] | 0.82 |
| microsoft-decision-1 flat vs scaledown-classify-1 flat | +0.081 [+0.017, +0.145] | 0.0147 |
| microsoft-decision-1 flat vs scaledown-classify-1 tree | +0.209 [+0.133, +0.286] | 1.75e-07 |
| microsoft-decision-1 flat vs scaledown-classify-1 tree_hard | +0.251 [+0.187, +0.315] | 6.54e-13 |
| microsoft-decision-1 flat vs scaledown-classify-1 tree_v2 | +0.182 [+0.106, +0.256] | 3.33e-06 |
| microsoft-decision-1 flat vs gemini-2.5-flash paper_llm | -0.032 [-0.081, +0.017] | 0.241 |
| microsoft-decision-1 flat vs gemini-2.5-flash paper_llm_thinking | +0.002 [-0.042, +0.047] | 1 |
| microsoft-decision-1 flat vs gemini-3.8-flash paper_llm_low | -0.118 [-0.167, -0.069] | 3.45e-06 |
| microsoft-decision-1 flat vs gemini-3.8-flash paper_llm_thinking | -0.086 [-0.138, -0.037] | 0.00103 |
| microsoft-decision-1 tree vs microsoft-decision-1 tree_hard | +0.030 [+0.007, +0.052] | 0.0169 |
| microsoft-decision-1 tree vs microsoft-decision-1 tree_v2 | -0.163 [-0.214, -0.108] | 4.16e-09 |
| microsoft-decision-1 tree vs elephant-1 flat | -0.241 [-0.296, -0.187] | 7.91e-16 |
| microsoft-decision-1 tree vs elephant-1 tree | -0.059 [-0.103, -0.015] | 0.0127 |
| microsoft-decision-1 tree vs elephant-1 tree_hard | -0.096 [-0.140, -0.052] | 3.48e-05 |
| microsoft-decision-1 tree vs elephant-1 tree_v2 | -0.182 [-0.241, -0.123] | 4.19e-09 |
| microsoft-decision-1 tree vs mammoth-1 flat | -0.246 [-0.310, -0.182] | 8.39e-13 |
| microsoft-decision-1 tree vs mammoth-1 tree | -0.071 [-0.123, -0.020] | 0.0106 |
| microsoft-decision-1 tree vs mammoth-1 tree_hard | -0.113 [-0.167, -0.059] | 9.9e-05 |
| microsoft-decision-1 tree vs mammoth-1 tree_v2 | -0.180 [-0.241, -0.116] | 5.83e-08 |
| microsoft-decision-1 tree vs scaledown-classify-1 flat | -0.089 [-0.150, -0.030] | 0.00491 |
| microsoft-decision-1 tree vs scaledown-classify-1 tree | +0.039 [-0.017, +0.094] | 0.195 |
| microsoft-decision-1 tree vs scaledown-classify-1 tree_hard | +0.081 [+0.030, +0.133] | 0.00345 |
| microsoft-decision-1 tree vs scaledown-classify-1 tree_v2 | +0.012 [-0.049, +0.071] | 0.75 |
| microsoft-decision-1 tree vs gemini-2.5-flash paper_llm | -0.202 [-0.266, -0.140] | 1.94e-09 |
| microsoft-decision-1 tree vs gemini-2.5-flash paper_llm_thinking | -0.167 [-0.232, -0.106] | 5.09e-07 |
| microsoft-decision-1 tree vs gemini-3.8-flash paper_llm_low | -0.288 [-0.345, -0.232] | 9.99e-20 |
| microsoft-decision-1 tree vs gemini-3.8-flash paper_llm_thinking | -0.256 [-0.315, -0.197] | 2.52e-15 |
| microsoft-decision-1 tree_hard vs microsoft-decision-1 tree_v2 | -0.192 [-0.246, -0.135] | 6.42e-11 |
| microsoft-decision-1 tree_hard vs elephant-1 flat | -0.271 [-0.328, -0.212] | 1.6e-17 |
| microsoft-decision-1 tree_hard vs elephant-1 tree | -0.089 [-0.138, -0.039] | 0.000684 |
| microsoft-decision-1 tree_hard vs elephant-1 tree_hard | -0.126 [-0.172, -0.079] | 4.95e-07 |
| microsoft-decision-1 tree_hard vs elephant-1 tree_v2 | -0.212 [-0.273, -0.150] | 1.04e-10 |
| microsoft-decision-1 tree_hard vs mammoth-1 flat | -0.276 [-0.340, -0.209] | 2.84e-15 |
| microsoft-decision-1 tree_hard vs mammoth-1 tree | -0.101 [-0.155, -0.047] | 0.000638 |
| microsoft-decision-1 tree_hard vs mammoth-1 tree_hard | -0.143 [-0.200, -0.084] | 3.39e-06 |
| microsoft-decision-1 tree_hard vs mammoth-1 tree_v2 | -0.209 [-0.273, -0.145] | 1.21e-09 |
| microsoft-decision-1 tree_hard vs scaledown-classify-1 flat | -0.118 [-0.180, -0.059] | 0.000241 |
| microsoft-decision-1 tree_hard vs scaledown-classify-1 tree | +0.010 [-0.049, +0.069] | 0.809 |
| microsoft-decision-1 tree_hard vs scaledown-classify-1 tree_hard | +0.052 [+0.000, +0.103] | 0.0617 |
| microsoft-decision-1 tree_hard vs scaledown-classify-1 tree_v2 | -0.017 [-0.081, +0.044] | 0.65 |
| microsoft-decision-1 tree_hard vs gemini-2.5-flash paper_llm | -0.232 [-0.291, -0.172] | 2.31e-12 |
| microsoft-decision-1 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.197 [-0.256, -0.138] | 6.64e-10 |
| microsoft-decision-1 tree_hard vs gemini-3.8-flash paper_llm_low | -0.318 [-0.374, -0.264] | 1.47e-23 |
| microsoft-decision-1 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.286 [-0.342, -0.227] | 8.35e-19 |
| microsoft-decision-1 tree_v2 vs elephant-1 flat | -0.079 [-0.135, -0.025] | 0.00762 |
| microsoft-decision-1 tree_v2 vs elephant-1 tree | +0.103 [+0.039, +0.167] | 0.00216 |
| microsoft-decision-1 tree_v2 vs elephant-1 tree_hard | +0.067 [+0.005, +0.128] | 0.0452 |
| microsoft-decision-1 tree_v2 vs elephant-1 tree_v2 | -0.020 [-0.071, +0.030] | 0.512 |
| microsoft-decision-1 tree_v2 vs mammoth-1 flat | -0.084 [-0.140, -0.030] | 0.00419 |
| microsoft-decision-1 tree_v2 vs mammoth-1 tree | +0.091 [+0.027, +0.153] | 0.00634 |
| microsoft-decision-1 tree_v2 vs mammoth-1 tree_hard | +0.049 [-0.012, +0.108] | 0.135 |
| microsoft-decision-1 tree_v2 vs mammoth-1 tree_v2 | -0.017 [-0.071, +0.037] | 0.597 |
| microsoft-decision-1 tree_v2 vs scaledown-classify-1 flat | +0.074 [+0.015, +0.131] | 0.0176 |
| microsoft-decision-1 tree_v2 vs scaledown-classify-1 tree | +0.202 [+0.135, +0.266] | 6.31e-09 |
| microsoft-decision-1 tree_v2 vs scaledown-classify-1 tree_hard | +0.244 [+0.177, +0.305] | 1.67e-12 |
| microsoft-decision-1 tree_v2 vs scaledown-classify-1 tree_v2 | +0.175 [+0.111, +0.239] | 1.62e-07 |
| microsoft-decision-1 tree_v2 vs gemini-2.5-flash paper_llm | -0.039 [-0.096, +0.017] | 0.205 |
| microsoft-decision-1 tree_v2 vs gemini-2.5-flash paper_llm_thinking | -0.005 [-0.062, +0.049] | 0.931 |
| microsoft-decision-1 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.126 [-0.182, -0.071] | 1.82e-05 |
| microsoft-decision-1 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.094 [-0.150, -0.037] | 0.00194 |
| elephant-1 flat vs elephant-1 tree | +0.182 [+0.131, +0.232] | 2.99e-11 |
| elephant-1 flat vs elephant-1 tree_hard | +0.145 [+0.094, +0.195] | 7.48e-08 |
| elephant-1 flat vs elephant-1 tree_v2 | +0.059 [+0.017, +0.101] | 0.00877 |
| elephant-1 flat vs mammoth-1 flat | -0.005 [-0.042, +0.034] | 0.901 |
| elephant-1 flat vs mammoth-1 tree | +0.170 [+0.121, +0.219] | 1.34e-10 |
| elephant-1 flat vs mammoth-1 tree_hard | +0.128 [+0.084, +0.172] | 4.61e-08 |
| elephant-1 flat vs mammoth-1 tree_v2 | +0.062 [+0.017, +0.106] | 0.00804 |
| elephant-1 flat vs scaledown-classify-1 flat | +0.153 [+0.099, +0.207] | 1.99e-07 |
| elephant-1 flat vs scaledown-classify-1 tree | +0.281 [+0.224, +0.337] | 1.46e-19 |
| elephant-1 flat vs scaledown-classify-1 tree_hard | +0.323 [+0.261, +0.382] | 2.43e-22 |
| elephant-1 flat vs scaledown-classify-1 tree_v2 | +0.254 [+0.200, +0.308] | 7.27e-18 |
| elephant-1 flat vs gemini-2.5-flash paper_llm | +0.039 [-0.012, +0.091] | 0.163 |
| elephant-1 flat vs gemini-2.5-flash paper_llm_thinking | +0.074 [+0.020, +0.131] | 0.012 |
| elephant-1 flat vs gemini-3.8-flash paper_llm_low | -0.047 [-0.089, -0.005] | 0.0395 |
| elephant-1 flat vs gemini-3.8-flash paper_llm_thinking | -0.015 [-0.059, +0.027] | 0.576 |
| elephant-1 tree vs elephant-1 tree_hard | -0.037 [-0.069, -0.005] | 0.04 |
| elephant-1 tree vs elephant-1 tree_v2 | -0.123 [-0.165, -0.084] | 8.58e-09 |
| elephant-1 tree vs mammoth-1 flat | -0.187 [-0.246, -0.128] | 1.93e-09 |
| elephant-1 tree vs mammoth-1 tree | -0.012 [-0.047, +0.020] | 0.568 |
| elephant-1 tree vs mammoth-1 tree_hard | -0.054 [-0.096, -0.012] | 0.0169 |
| elephant-1 tree vs mammoth-1 tree_v2 | -0.121 [-0.170, -0.071] | 4.55e-06 |
| elephant-1 tree vs scaledown-classify-1 flat | -0.030 [-0.091, +0.030] | 0.375 |
| elephant-1 tree vs scaledown-classify-1 tree | +0.099 [+0.062, +0.135] | 2.78e-07 |
| elephant-1 tree vs scaledown-classify-1 tree_hard | +0.140 [+0.089, +0.192] | 3.47e-07 |
| elephant-1 tree vs scaledown-classify-1 tree_v2 | +0.071 [+0.030, +0.113] | 0.00147 |
| elephant-1 tree vs gemini-2.5-flash paper_llm | -0.143 [-0.209, -0.079] | 3.11e-05 |
| elephant-1 tree vs gemini-2.5-flash paper_llm_thinking | -0.108 [-0.180, -0.039] | 0.00349 |
| elephant-1 tree vs gemini-3.8-flash paper_llm_low | -0.229 [-0.288, -0.167] | 1.01e-12 |
| elephant-1 tree vs gemini-3.8-flash paper_llm_thinking | -0.197 [-0.259, -0.135] | 1.36e-09 |
| elephant-1 tree_hard vs elephant-1 tree_v2 | -0.086 [-0.133, -0.039] | 0.000562 |
| elephant-1 tree_hard vs mammoth-1 flat | -0.150 [-0.207, -0.091] | 1.06e-06 |
| elephant-1 tree_hard vs mammoth-1 tree | +0.025 [-0.017, +0.067] | 0.295 |
| elephant-1 tree_hard vs mammoth-1 tree_hard | -0.017 [-0.062, +0.027] | 0.52 |
| elephant-1 tree_hard vs mammoth-1 tree_v2 | -0.084 [-0.135, -0.032] | 0.00205 |
| elephant-1 tree_hard vs scaledown-classify-1 flat | +0.007 [-0.052, +0.067] | 0.87 |
| elephant-1 tree_hard vs scaledown-classify-1 tree | +0.135 [+0.089, +0.182] | 6.88e-08 |
| elephant-1 tree_hard vs scaledown-classify-1 tree_hard | +0.177 [+0.123, +0.229] | 4.43e-10 |
| elephant-1 tree_hard vs scaledown-classify-1 tree_v2 | +0.108 [+0.057, +0.160] | 8.41e-05 |
| elephant-1 tree_hard vs gemini-2.5-flash paper_llm | -0.106 [-0.167, -0.047] | 0.00109 |
| elephant-1 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.071 [-0.140, -0.002] | 0.0469 |
| elephant-1 tree_hard vs gemini-3.8-flash paper_llm_low | -0.192 [-0.249, -0.135] | 3.97e-10 |
| elephant-1 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.160 [-0.219, -0.101] | 3.81e-07 |
| elephant-1 tree_v2 vs mammoth-1 flat | -0.064 [-0.113, -0.015] | 0.0157 |
| elephant-1 tree_v2 vs mammoth-1 tree | +0.111 [+0.069, +0.153] | 3.59e-07 |
| elephant-1 tree_v2 vs mammoth-1 tree_hard | +0.069 [+0.025, +0.113] | 0.00264 |
| elephant-1 tree_v2 vs mammoth-1 tree_v2 | +0.002 [-0.030, +0.034] | 1 |
| elephant-1 tree_v2 vs scaledown-classify-1 flat | +0.094 [+0.037, +0.150] | 0.00154 |
| elephant-1 tree_v2 vs scaledown-classify-1 tree | +0.222 [+0.175, +0.268] | 1.51e-18 |
| elephant-1 tree_v2 vs scaledown-classify-1 tree_hard | +0.264 [+0.204, +0.320] | 1.73e-16 |
| elephant-1 tree_v2 vs scaledown-classify-1 tree_v2 | +0.195 [+0.150, +0.239] | 5.52e-17 |
| elephant-1 tree_v2 vs gemini-2.5-flash paper_llm | -0.020 [-0.079, +0.039] | 0.568 |
| elephant-1 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.015 [-0.049, +0.079] | 0.7 |
| elephant-1 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.106 [-0.160, -0.052] | 0.000192 |
| elephant-1 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.074 [-0.128, -0.017] | 0.0107 |
| mammoth-1 flat vs mammoth-1 tree | +0.175 [+0.121, +0.229] | 2.25e-09 |
| mammoth-1 flat vs mammoth-1 tree_hard | +0.133 [+0.086, +0.182] | 1.43e-07 |
| mammoth-1 flat vs mammoth-1 tree_v2 | +0.067 [+0.020, +0.113] | 0.00796 |
| mammoth-1 flat vs scaledown-classify-1 flat | +0.158 [+0.101, +0.214] | 9.45e-08 |
| mammoth-1 flat vs scaledown-classify-1 tree | +0.286 [+0.224, +0.345] | 3.67e-18 |
| mammoth-1 flat vs scaledown-classify-1 tree_hard | +0.328 [+0.264, +0.389] | 4.01e-21 |
| mammoth-1 flat vs scaledown-classify-1 tree_v2 | +0.259 [+0.200, +0.315] | 1.12e-16 |
| mammoth-1 flat vs gemini-2.5-flash paper_llm | +0.044 [-0.007, +0.094] | 0.101 |
| mammoth-1 flat vs gemini-2.5-flash paper_llm_thinking | +0.079 [+0.025, +0.131] | 0.00516 |
| mammoth-1 flat vs gemini-3.8-flash paper_llm_low | -0.042 [-0.081, -0.002] | 0.0498 |
| mammoth-1 flat vs gemini-3.8-flash paper_llm_thinking | -0.010 [-0.052, +0.032] | 0.728 |
| mammoth-1 tree vs mammoth-1 tree_hard | -0.042 [-0.074, -0.010] | 0.0161 |
| mammoth-1 tree vs mammoth-1 tree_v2 | -0.108 [-0.148, -0.069] | 6.21e-08 |
| mammoth-1 tree vs scaledown-classify-1 flat | -0.017 [-0.076, +0.039] | 0.616 |
| mammoth-1 tree vs scaledown-classify-1 tree | +0.111 [+0.074, +0.150] | 2.15e-08 |
| mammoth-1 tree vs scaledown-classify-1 tree_hard | +0.153 [+0.096, +0.207] | 2.99e-07 |
| mammoth-1 tree vs scaledown-classify-1 tree_v2 | +0.084 [+0.042, +0.126] | 9.61e-05 |
| mammoth-1 tree vs gemini-2.5-flash paper_llm | -0.131 [-0.195, -0.069] | 7.53e-05 |
| mammoth-1 tree vs gemini-2.5-flash paper_llm_thinking | -0.096 [-0.165, -0.027] | 0.0078 |
| mammoth-1 tree vs gemini-3.8-flash paper_llm_low | -0.217 [-0.273, -0.160] | 5.25e-13 |
| mammoth-1 tree vs gemini-3.8-flash paper_llm_thinking | -0.185 [-0.241, -0.128] | 1.02e-09 |
| mammoth-1 tree_hard vs mammoth-1 tree_v2 | -0.067 [-0.106, -0.030] | 0.000898 |
| mammoth-1 tree_hard vs scaledown-classify-1 flat | +0.025 [-0.032, +0.081] | 0.44 |
| mammoth-1 tree_hard vs scaledown-classify-1 tree | +0.153 [+0.103, +0.202] | 1.52e-09 |
| mammoth-1 tree_hard vs scaledown-classify-1 tree_hard | +0.195 [+0.135, +0.251] | 4.56e-10 |
| mammoth-1 tree_hard vs scaledown-classify-1 tree_v2 | +0.126 [+0.076, +0.175] | 8.42e-07 |
| mammoth-1 tree_hard vs gemini-2.5-flash paper_llm | -0.089 [-0.145, -0.032] | 0.00339 |
| mammoth-1 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.054 [-0.118, +0.010] | 0.117 |
| mammoth-1 tree_hard vs gemini-3.8-flash paper_llm_low | -0.175 [-0.224, -0.126] | 2.23e-11 |
| mammoth-1 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.143 [-0.195, -0.094] | 1.12e-07 |
| mammoth-1 tree_v2 vs scaledown-classify-1 flat | +0.091 [+0.037, +0.145] | 0.00143 |
| mammoth-1 tree_v2 vs scaledown-classify-1 tree | +0.219 [+0.170, +0.268] | 3.16e-17 |
| mammoth-1 tree_v2 vs scaledown-classify-1 tree_hard | +0.261 [+0.200, +0.320] | 4.76e-15 |
| mammoth-1 tree_v2 vs scaledown-classify-1 tree_v2 | +0.192 [+0.145, +0.239] | 3.06e-15 |
| mammoth-1 tree_v2 vs gemini-2.5-flash paper_llm | -0.022 [-0.079, +0.034] | 0.504 |
| mammoth-1 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.012 [-0.052, +0.076] | 0.761 |
| mammoth-1 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.108 [-0.160, -0.054] | 8.41e-05 |
| mammoth-1 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.076 [-0.128, -0.022] | 0.00615 |
| scaledown-classify-1 flat vs scaledown-classify-1 tree | +0.128 [+0.069, +0.187] | 4.28e-05 |
| scaledown-classify-1 flat vs scaledown-classify-1 tree_hard | +0.170 [+0.111, +0.232] | 1.36e-07 |
| scaledown-classify-1 flat vs scaledown-classify-1 tree_v2 | +0.101 [+0.042, +0.160] | 0.00106 |
| scaledown-classify-1 flat vs gemini-2.5-flash paper_llm | -0.113 [-0.175, -0.054] | 0.000344 |
| scaledown-classify-1 flat vs gemini-2.5-flash paper_llm_thinking | -0.079 [-0.140, -0.017] | 0.0159 |
| scaledown-classify-1 flat vs gemini-3.8-flash paper_llm_low | -0.200 [-0.256, -0.143] | 4.69e-11 |
| scaledown-classify-1 flat vs gemini-3.8-flash paper_llm_thinking | -0.167 [-0.224, -0.108] | 4.08e-08 |
| scaledown-classify-1 tree vs scaledown-classify-1 tree_hard | +0.042 [-0.012, +0.096] | 0.159 |
| scaledown-classify-1 tree vs scaledown-classify-1 tree_v2 | -0.027 [-0.052, -0.002] | 0.0522 |
| scaledown-classify-1 tree vs gemini-2.5-flash paper_llm | -0.241 [-0.310, -0.175] | 1.85e-11 |
| scaledown-classify-1 tree vs gemini-2.5-flash paper_llm_thinking | -0.207 [-0.281, -0.133] | 1.04e-07 |
| scaledown-classify-1 tree vs gemini-3.8-flash paper_llm_low | -0.328 [-0.389, -0.264] | 4.01e-21 |
| scaledown-classify-1 tree vs gemini-3.8-flash paper_llm_thinking | -0.296 [-0.357, -0.232] | 1.21e-17 |
| scaledown-classify-1 tree_hard vs scaledown-classify-1 tree_v2 | -0.069 [-0.126, -0.012] | 0.0282 |
| scaledown-classify-1 tree_hard vs gemini-2.5-flash paper_llm | -0.283 [-0.345, -0.222] | 2.31e-17 |
| scaledown-classify-1 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.249 [-0.313, -0.182] | 1.68e-12 |
| scaledown-classify-1 tree_hard vs gemini-3.8-flash paper_llm_low | -0.369 [-0.429, -0.308] | 5.79e-27 |
| scaledown-classify-1 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.337 [-0.399, -0.273] | 1.12e-22 |
| scaledown-classify-1 tree_v2 vs gemini-2.5-flash paper_llm | -0.214 [-0.281, -0.148] | 1.31e-09 |
| scaledown-classify-1 tree_v2 vs gemini-2.5-flash paper_llm_thinking | -0.180 [-0.251, -0.108] | 1.79e-06 |
| scaledown-classify-1 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.300 [-0.362, -0.239] | 3.24e-19 |
| scaledown-classify-1 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.268 [-0.328, -0.207] | 5.68e-16 |
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

**pplx-decider-flash-v1.2 flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 106 | 18 | 2 | 15 | 2 |
| Comp | 34 | 56 | 4 | 7 | 1 |
| Opin | 14 | 27 | 57 | 1 | 3 |
| Outd | 17 | 6 | 0 | 32 | 0 |
| Misi | 3 | 0 | 0 | 1 | 0 |

**pplx-decider-flash-v1.2 tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 125 | 8 | 0 | 2 | 8 |
| Comp | 48 | 49 | 0 | 2 | 3 |
| Opin | 46 | 54 | 0 | 0 | 2 |
| Outd | 29 | 9 | 0 | 14 | 3 |
| Misi | 3 | 0 | 0 | 0 | 1 |

**pplx-decider-flash-v1.2 tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 109 | 10 | 1 | 8 | 15 |
| Comp | 41 | 56 | 0 | 2 | 3 |
| Opin | 33 | 54 | 5 | 0 | 10 |
| Outd | 20 | 6 | 0 | 25 | 4 |
| Misi | 3 | 0 | 0 | 0 | 1 |

**pplx-decider-flash-v1.2 tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 124 | 6 | 2 | 7 | 4 |
| Comp | 49 | 44 | 4 | 2 | 3 |
| Opin | 44 | 3 | 54 | 0 | 1 |
| Outd | 28 | 6 | 2 | 18 | 1 |
| Misi | 3 | 0 | 0 | 1 | 0 |

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

**d1-ultra flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 108 | 5 | 9 | 19 | 2 |
| Comp | 33 | 45 | 9 | 14 | 1 |
| Opin | 13 | 4 | 77 | 3 | 5 |
| Outd | 12 | 1 | 0 | 42 | 0 |
| Misi | 3 | 0 | 0 | 1 | 0 |

**d1-ultra tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 131 | 8 | 0 | 2 | 2 |
| Comp | 52 | 48 | 1 | 0 | 1 |
| Opin | 28 | 48 | 15 | 1 | 10 |
| Outd | 32 | 12 | 0 | 10 | 1 |
| Misi | 3 | 0 | 0 | 1 | 0 |

**d1-ultra tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 116 | 11 | 0 | 8 | 8 |
| Comp | 36 | 59 | 1 | 2 | 4 |
| Opin | 14 | 43 | 27 | 2 | 16 |
| Outd | 17 | 9 | 0 | 27 | 2 |
| Misi | 2 | 1 | 0 | 1 | 0 |

**d1-ultra tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 130 | 6 | 3 | 2 | 2 |
| Comp | 58 | 36 | 5 | 1 | 2 |
| Opin | 29 | 1 | 71 | 0 | 1 |
| Outd | 30 | 4 | 2 | 18 | 1 |
| Misi | 3 | 0 | 0 | 1 | 0 |

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

**elephant-1 flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 120 | 8 | 2 | 13 | 0 |
| Comp | 36 | 55 | 5 | 5 | 1 |
| Opin | 19 | 20 | 59 | 1 | 3 |
| Outd | 24 | 0 | 0 | 31 | 0 |
| Misi | 3 | 0 | 0 | 1 | 0 |

**elephant-1 tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 134 | 6 | 0 | 1 | 2 |
| Comp | 48 | 53 | 0 | 0 | 1 |
| Opin | 50 | 50 | 1 | 0 | 1 |
| Outd | 36 | 15 | 0 | 3 | 1 |
| Misi | 4 | 0 | 0 | 0 | 0 |

**elephant-1 tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 118 | 10 | 0 | 7 | 8 |
| Comp | 39 | 62 | 0 | 0 | 1 |
| Opin | 27 | 58 | 11 | 0 | 6 |
| Outd | 23 | 16 | 0 | 13 | 3 |
| Misi | 2 | 0 | 0 | 0 | 2 |

**elephant-1 tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 135 | 4 | 1 | 2 | 1 |
| Comp | 52 | 40 | 9 | 0 | 1 |
| Opin | 41 | 2 | 59 | 0 | 0 |
| Outd | 36 | 8 | 3 | 7 | 1 |
| Misi | 4 | 0 | 0 | 0 | 0 |

**mammoth-1 flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 113 | 0 | 7 | 17 | 6 |
| Comp | 37 | 39 | 7 | 15 | 4 |
| Opin | 17 | 2 | 75 | 0 | 8 |
| Outd | 15 | 0 | 0 | 40 | 0 |
| Misi | 3 | 0 | 0 | 1 | 0 |

**mammoth-1 tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 133 | 7 | 0 | 2 | 1 |
| Comp | 57 | 40 | 1 | 0 | 4 |
| Opin | 53 | 24 | 16 | 1 | 8 |
| Outd | 36 | 11 | 0 | 7 | 1 |
| Misi | 3 | 0 | 0 | 1 | 0 |

**mammoth-1 tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 122 | 7 | 1 | 6 | 7 |
| Comp | 50 | 41 | 1 | 5 | 5 |
| Opin | 32 | 20 | 31 | 2 | 17 |
| Outd | 21 | 9 | 0 | 19 | 6 |
| Misi | 3 | 0 | 0 | 1 | 0 |

**mammoth-1 tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 131 | 5 | 2 | 4 | 1 |
| Comp | 56 | 31 | 9 | 4 | 2 |
| Opin | 40 | 0 | 62 | 0 | 0 |
| Outd | 31 | 7 | 1 | 16 | 0 |
| Misi | 3 | 0 | 0 | 1 | 0 |

**scaledown-classify-1 flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 90 | 33 | 10 | 7 | 3 |
| Comp | 33 | 51 | 9 | 6 | 3 |
| Opin | 8 | 39 | 51 | 1 | 3 |
| Outd | 22 | 16 | 6 | 11 | 0 |
| Misi | 4 | 0 | 0 | 0 | 0 |

**scaledown-classify-1 tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 139 | 4 | 0 | 0 | 0 |
| Comp | 90 | 12 | 0 | 0 | 0 |
| Opin | 87 | 15 | 0 | 0 | 0 |
| Outd | 43 | 12 | 0 | 0 | 0 |
| Misi | 4 | 0 | 0 | 0 | 0 |

**scaledown-classify-1 tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 66 | 64 | 3 | 7 | 3 |
| Comp | 39 | 56 | 1 | 4 | 2 |
| Opin | 27 | 61 | 9 | 3 | 2 |
| Outd | 10 | 42 | 0 | 3 | 0 |
| Misi | 0 | 4 | 0 | 0 | 0 |

**scaledown-classify-1 tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 141 | 2 | 0 | 0 | 0 |
| Comp | 98 | 4 | 0 | 0 | 0 |
| Opin | 84 | 1 | 17 | 0 | 0 |
| Outd | 48 | 6 | 1 | 0 | 0 |
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
