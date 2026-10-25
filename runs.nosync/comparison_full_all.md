# Conflict-type classification on CONFLICTS, split `all` (n = 458)

| System | Accuracy [95% CI] | 4-class acc. | Macro-F1 | ECE | Brier | NLL | Unparsed | Input tokens | $/1k queries | Latency mean / p95 (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| jev-1.13.0 flat | 0.609 [0.563, 0.653] | 0.622 | 0.539 | 0.109 | 0.538 | 1.109 | 0 | 4612 | 0.194 | 0.26 / 0.40 |
| jev-1.13.0 tree | 0.474 [0.428, 0.517] | 0.483 | 0.291 | 0.150 | 0.677 | 1.300 | 0 | 4300 | 0.181 | 0.25 / 0.37 |
| jev-1.13.0 tree_hard | 0.461 [0.415, 0.507] | 0.480 | 0.324 | – | – | – | 0 | 4300 | 0.181 | 0.25 / 0.37 |
| jev-1.13.0 tree_v2 | 0.635 [0.592, 0.677] | 0.638 | 0.459 | 0.036 | 0.492 | 0.944 | 0 | 4300 | 0.181 | 0.25 / 0.37 |
| jev-1.14.0 flat | 0.592 [0.546, 0.635] | 0.605 | 0.527 | 0.119 | 0.565 | 1.178 | 0 | 4612 | 0.194 | 0.28 / 0.42 |
| jev-1.14.0 tree | 0.454 [0.408, 0.500] | 0.463 | 0.277 | 0.189 | 0.694 | 1.330 | 0 | 4300 | 0.181 | 0.27 / 0.41 |
| jev-1.14.0 tree_hard | 0.445 [0.400, 0.491] | 0.459 | 0.306 | – | – | – | 0 | 4300 | 0.181 | 0.27 / 0.41 |
| jev-1.14.0 tree_v2 | 0.627 [0.581, 0.670] | 0.629 | 0.456 | 0.026 | 0.495 | 0.952 | 0 | 4300 | 0.181 | 0.27 / 0.41 |
| microsoft-decision-1 flat | 0.581 [0.535, 0.627] | 0.594 | 0.500 | 0.186 | 0.577 | 1.131 | 0 | 4220 | 0.177 | 0.45 / 0.65 |
| microsoft-decision-1 tree | 0.413 [0.367, 0.459] | 0.417 | 0.262 | 0.298 | 0.822 | 1.659 | 0 | 3985 | 0.167 | 0.56 / 0.74 |
| microsoft-decision-1 tree_hard | 0.380 [0.336, 0.424] | 0.391 | 0.238 | – | – | – | 0 | 3985 | 0.167 | 0.56 / 0.74 |
| microsoft-decision-1 tree_v2 | 0.568 [0.522, 0.611] | 0.570 | 0.391 | 0.117 | 0.550 | 1.050 | 0 | 3985 | 0.167 | 0.56 / 0.74 |
| d1 flat | 0.614 [0.570, 0.657] | 0.616 | 0.504 | 0.080 | 0.514 | 0.977 | 0 | 4226 | 0.085 | 0.42 / 0.59 |
| d1 tree | 0.441 [0.395, 0.487] | 0.441 | 0.295 | 0.229 | 0.735 | 1.450 | 0 | 4024 | 0.080 | 0.52 / 0.69 |
| d1 tree_hard | 0.467 [0.421, 0.513] | 0.467 | 0.367 | – | – | – | 0 | 4024 | 0.080 | 0.52 / 0.69 |
| d1 tree_v2 | 0.561 [0.515, 0.605] | 0.563 | 0.464 | 0.123 | 0.576 | 1.092 | 0 | 4024 | 0.080 | 0.52 / 0.69 |
| pplx-decider-v1.2 flat | 0.659 [0.616, 0.701] | 0.662 | 0.554 | 0.054 | 0.453 | 0.839 | 0 | 4293 | 0.086 | 0.42 / 0.59 |
| pplx-decider-v1.2 tree | 0.566 [0.520, 0.609] | 0.568 | 0.431 | 0.146 | 0.607 | 1.171 | 0 | 4113 | 0.082 | 0.40 / 0.58 |
| pplx-decider-v1.2 tree_hard | 0.576 [0.531, 0.620] | 0.581 | 0.471 | – | – | – | 0 | 4113 | 0.082 | 0.40 / 0.58 |
| pplx-decider-v1.2 tree_v2 | 0.677 [0.633, 0.718] | 0.679 | 0.544 | 0.060 | 0.461 | 0.939 | 0 | 4113 | 0.082 | 0.40 / 0.58 |
| gpt-6-luna-decisions flat | 0.657 [0.614, 0.701] | 0.657 | 0.540 | 0.073 | 0.529 | 1.091 | 0 | 4145 | 0.414 | 0.36 / 0.61 |
| gpt-6-luna-decisions tree | 0.421 [0.376, 0.467] | 0.428 | 0.193 | 0.431 | 0.948 | 2.842 | 0 | 4497 | 0.450 | 0.39 / 0.70 |
| gpt-6-luna-decisions tree_hard | 0.421 [0.376, 0.467] | 0.430 | 0.193 | – | – | – | 0 | 4497 | 0.450 | 0.39 / 0.70 |
| gpt-6-luna-decisions tree_v2 | 0.496 [0.450, 0.541] | 0.498 | 0.310 | 0.353 | 0.800 | 1.931 | 0 | 4497 | 0.450 | 0.39 / 0.70 |
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
| jev-1.14.0 flat | 0.601 | 0.643 | 0.716 | 0.597 | 0.078 |
| jev-1.14.0 tree | 0.690 | 0.467 | 0.017 | 0.091 | 0.118 |
| jev-1.14.0 tree_hard | 0.637 | 0.482 | 0.083 | 0.192 | 0.133 |
| jev-1.14.0 tree_v2 | 0.681 | 0.536 | 0.755 | 0.308 | 0.000 |
| microsoft-decision-1 flat | 0.537 | 0.594 | 0.750 | 0.583 | 0.038 |
| microsoft-decision-1 tree | 0.623 | 0.432 | 0.000 | 0.091 | 0.167 |
| microsoft-decision-1 tree_hard | 0.543 | 0.437 | 0.017 | 0.113 | 0.080 |
| microsoft-decision-1 tree_v2 | 0.634 | 0.449 | 0.733 | 0.139 | 0.000 |
| d1 flat | 0.622 | 0.580 | 0.667 | 0.650 | 0.000 |
| d1 tree | 0.623 | 0.383 | 0.000 | 0.219 | 0.250 |
| d1 tree_hard | 0.645 | 0.404 | 0.083 | 0.417 | 0.286 |
| d1 tree_v2 | 0.619 | 0.457 | 0.656 | 0.302 | 0.286 |
| pplx-decider-v1.2 flat | 0.674 | 0.599 | 0.749 | 0.653 | 0.095 |
| pplx-decider-v1.2 tree | 0.711 | 0.531 | 0.284 | 0.631 | 0.000 |
| pplx-decider-v1.2 tree_hard | 0.693 | 0.556 | 0.430 | 0.614 | 0.065 |
| pplx-decider-v1.2 tree_v2 | 0.693 | 0.624 | 0.771 | 0.633 | 0.000 |
| gpt-6-luna-decisions flat | 0.692 | 0.682 | 0.633 | 0.694 | 0.000 |
| gpt-6-luna-decisions tree | 0.597 | 0.369 | 0.000 | 0.000 | 0.000 |
| gpt-6-luna-decisions tree_hard | 0.602 | 0.364 | 0.000 | 0.000 | 0.000 |
| gpt-6-luna-decisions tree_v2 | 0.596 | 0.404 | 0.459 | 0.092 | 0.000 |
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
| jev-1.13.0 flat vs jev-1.14.0 flat | +0.017 [-0.007, +0.041] | 0.215 |
| jev-1.13.0 flat vs jev-1.14.0 tree | +0.155 [+0.100, +0.210] | 8.15e-08 |
| jev-1.13.0 flat vs jev-1.14.0 tree_hard | +0.164 [+0.109, +0.216] | 8.88e-09 |
| jev-1.13.0 flat vs jev-1.14.0 tree_v2 | -0.017 [-0.068, +0.033] | 0.551 |
| jev-1.13.0 flat vs microsoft-decision-1 flat | +0.028 [-0.015, +0.070] | 0.232 |
| jev-1.13.0 flat vs microsoft-decision-1 tree | +0.197 [+0.140, +0.253] | 5.95e-11 |
| jev-1.13.0 flat vs microsoft-decision-1 tree_hard | +0.229 [+0.175, +0.284] | 7.44e-15 |
| jev-1.13.0 flat vs microsoft-decision-1 tree_v2 | +0.041 [-0.013, +0.096] | 0.156 |
| jev-1.13.0 flat vs d1 flat | -0.004 [-0.046, +0.039] | 0.92 |
| jev-1.13.0 flat vs d1 tree | +0.168 [+0.107, +0.229] | 1.63e-07 |
| jev-1.13.0 flat vs d1 tree_hard | +0.142 [+0.087, +0.199] | 1.33e-06 |
| jev-1.13.0 flat vs d1 tree_v2 | +0.048 [-0.007, +0.103] | 0.0987 |
| jev-1.13.0 flat vs pplx-decider-v1.2 flat | -0.050 [-0.090, -0.009] | 0.0178 |
| jev-1.13.0 flat vs pplx-decider-v1.2 tree | +0.044 [-0.007, +0.094] | 0.113 |
| jev-1.13.0 flat vs pplx-decider-v1.2 tree_hard | +0.033 [-0.013, +0.079] | 0.203 |
| jev-1.13.0 flat vs pplx-decider-v1.2 tree_v2 | -0.068 [-0.111, -0.024] | 0.00322 |
| jev-1.13.0 flat vs gpt-6-luna-decisions flat | -0.048 [-0.096, +0.000] | 0.0609 |
| jev-1.13.0 flat vs gpt-6-luna-decisions tree | +0.188 [+0.124, +0.253] | 3.37e-08 |
| jev-1.13.0 flat vs gpt-6-luna-decisions tree_hard | +0.188 [+0.124, +0.253] | 3.37e-08 |
| jev-1.13.0 flat vs gpt-6-luna-decisions tree_v2 | +0.114 [+0.052, +0.175] | 0.000462 |
| jev-1.13.0 flat vs gemini-2.5-flash paper_llm | +0.002 [-0.044, +0.048] | 1 |
| jev-1.13.0 flat vs gemini-2.5-flash paper_llm_thinking | +0.028 [-0.013, +0.068] | 0.208 |
| jev-1.13.0 flat vs gemini-3.8-flash paper_llm_low | -0.081 [-0.120, -0.041] | 0.00011 |
| jev-1.13.0 flat vs gemini-3.8-flash paper_llm_thinking | -0.057 [-0.096, -0.017] | 0.00805 |
| jev-1.13.0 tree vs jev-1.13.0 tree_hard | +0.013 [-0.011, +0.037] | 0.377 |
| jev-1.13.0 tree vs jev-1.13.0 tree_v2 | -0.162 [-0.212, -0.114] | 4.86e-10 |
| jev-1.13.0 tree vs jev-1.14.0 flat | -0.118 [-0.177, -0.061] | 0.0001 |
| jev-1.13.0 tree vs jev-1.14.0 tree | +0.020 [+0.000, +0.039] | 0.0784 |
| jev-1.13.0 tree vs jev-1.14.0 tree_hard | +0.028 [+0.000, +0.057] | 0.066 |
| jev-1.13.0 tree vs jev-1.14.0 tree_v2 | -0.153 [-0.203, -0.105] | 9.56e-09 |
| jev-1.13.0 tree vs microsoft-decision-1 flat | -0.107 [-0.168, -0.048] | 0.000761 |
| jev-1.13.0 tree vs microsoft-decision-1 tree | +0.061 [+0.028, +0.094] | 0.000307 |
| jev-1.13.0 tree vs microsoft-decision-1 tree_hard | +0.094 [+0.059, +0.129] | 2.67e-07 |
| jev-1.13.0 tree vs microsoft-decision-1 tree_v2 | -0.094 [-0.153, -0.037] | 0.00194 |
| jev-1.13.0 tree vs d1 flat | -0.140 [-0.197, -0.083] | 3.99e-06 |
| jev-1.13.0 tree vs d1 tree | +0.033 [-0.007, +0.072] | 0.119 |
| jev-1.13.0 tree vs d1 tree_hard | +0.007 [-0.033, +0.046] | 0.822 |
| jev-1.13.0 tree vs d1 tree_v2 | -0.087 [-0.140, -0.037] | 0.00137 |
| jev-1.13.0 tree vs pplx-decider-v1.2 flat | -0.186 [-0.240, -0.131] | 2.54e-10 |
| jev-1.13.0 tree vs pplx-decider-v1.2 tree | -0.092 [-0.133, -0.050] | 2.15e-05 |
| jev-1.13.0 tree vs pplx-decider-v1.2 tree_hard | -0.103 [-0.146, -0.059] | 6.28e-06 |
| jev-1.13.0 tree vs pplx-decider-v1.2 tree_v2 | -0.203 [-0.255, -0.153] | 1.18e-13 |
| jev-1.13.0 tree vs gpt-6-luna-decisions flat | -0.183 [-0.236, -0.133] | 1.3e-11 |
| jev-1.13.0 tree vs gpt-6-luna-decisions tree | +0.052 [+0.009, +0.094] | 0.0223 |
| jev-1.13.0 tree vs gpt-6-luna-decisions tree_hard | +0.052 [+0.009, +0.094] | 0.0223 |
| jev-1.13.0 tree vs gpt-6-luna-decisions tree_v2 | -0.022 [-0.072, +0.028] | 0.45 |
| jev-1.13.0 tree vs gemini-2.5-flash paper_llm | -0.133 [-0.192, -0.076] | 1.34e-05 |
| jev-1.13.0 tree vs gemini-2.5-flash paper_llm_thinking | -0.107 [-0.168, -0.046] | 0.000908 |
| jev-1.13.0 tree vs gemini-3.8-flash paper_llm_low | -0.216 [-0.266, -0.166] | 2.02e-15 |
| jev-1.13.0 tree vs gemini-3.8-flash paper_llm_thinking | -0.192 [-0.245, -0.140] | 1.15e-11 |
| jev-1.13.0 tree_hard vs jev-1.13.0 tree_v2 | -0.175 [-0.225, -0.124] | 1.75e-10 |
| jev-1.13.0 tree_hard vs jev-1.14.0 flat | -0.131 [-0.186, -0.079] | 5.56e-06 |
| jev-1.13.0 tree_hard vs jev-1.14.0 tree | +0.007 [-0.017, +0.031] | 0.728 |
| jev-1.13.0 tree_hard vs jev-1.14.0 tree_hard | +0.015 [-0.007, +0.037] | 0.248 |
| jev-1.13.0 tree_hard vs jev-1.14.0 tree_v2 | -0.166 [-0.216, -0.116] | 5.12e-10 |
| jev-1.13.0 tree_hard vs microsoft-decision-1 flat | -0.120 [-0.179, -0.063] | 6.4e-05 |
| jev-1.13.0 tree_hard vs microsoft-decision-1 tree | +0.048 [+0.015, +0.081] | 0.00535 |
| jev-1.13.0 tree_hard vs microsoft-decision-1 tree_hard | +0.081 [+0.048, +0.114] | 1.97e-06 |
| jev-1.13.0 tree_hard vs microsoft-decision-1 tree_v2 | -0.107 [-0.164, -0.050] | 0.000309 |
| jev-1.13.0 tree_hard vs d1 flat | -0.153 [-0.210, -0.098] | 3.09e-07 |
| jev-1.13.0 tree_hard vs d1 tree | +0.020 [-0.024, +0.063] | 0.444 |
| jev-1.13.0 tree_hard vs d1 tree_hard | -0.007 [-0.048, +0.035] | 0.836 |
| jev-1.13.0 tree_hard vs d1 tree_v2 | -0.100 [-0.155, -0.046] | 0.00052 |
| jev-1.13.0 tree_hard vs pplx-decider-v1.2 flat | -0.199 [-0.255, -0.144] | 2.41e-11 |
| jev-1.13.0 tree_hard vs pplx-decider-v1.2 tree | -0.105 [-0.148, -0.061] | 2.74e-06 |
| jev-1.13.0 tree_hard vs pplx-decider-v1.2 tree_hard | -0.116 [-0.159, -0.072] | 4.91e-07 |
| jev-1.13.0 tree_hard vs pplx-decider-v1.2 tree_v2 | -0.216 [-0.269, -0.166] | 4.89e-15 |
| jev-1.13.0 tree_hard vs gpt-6-luna-decisions flat | -0.197 [-0.249, -0.146] | 3.12e-13 |
| jev-1.13.0 tree_hard vs gpt-6-luna-decisions tree | +0.039 [-0.009, +0.087] | 0.139 |
| jev-1.13.0 tree_hard vs gpt-6-luna-decisions tree_hard | +0.039 [-0.009, +0.087] | 0.139 |
| jev-1.13.0 tree_hard vs gpt-6-luna-decisions tree_v2 | -0.035 [-0.090, +0.020] | 0.247 |
| jev-1.13.0 tree_hard vs gemini-2.5-flash paper_llm | -0.146 [-0.201, -0.090] | 9.38e-07 |
| jev-1.13.0 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.120 [-0.177, -0.063] | 9.18e-05 |
| jev-1.13.0 tree_hard vs gemini-3.8-flash paper_llm_low | -0.229 [-0.279, -0.179] | 6.88e-17 |
| jev-1.13.0 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.205 [-0.258, -0.155] | 1.1e-13 |
| jev-1.13.0 tree_v2 vs jev-1.14.0 flat | +0.044 [-0.009, +0.096] | 0.118 |
| jev-1.13.0 tree_v2 vs jev-1.14.0 tree | +0.181 [+0.131, +0.231] | 1.44e-11 |
| jev-1.13.0 tree_v2 vs jev-1.14.0 tree_hard | +0.190 [+0.138, +0.242] | 1.29e-11 |
| jev-1.13.0 tree_v2 vs jev-1.14.0 tree_v2 | +0.009 [-0.013, +0.031] | 0.557 |
| jev-1.13.0 tree_v2 vs microsoft-decision-1 flat | +0.055 [+0.000, +0.109] | 0.0598 |
| jev-1.13.0 tree_v2 vs microsoft-decision-1 tree | +0.223 [+0.168, +0.277] | 5.61e-14 |
| jev-1.13.0 tree_v2 vs microsoft-decision-1 tree_hard | +0.255 [+0.199, +0.310] | 4.83e-17 |
| jev-1.13.0 tree_v2 vs microsoft-decision-1 tree_v2 | +0.068 [+0.031, +0.105] | 0.000371 |
| jev-1.13.0 tree_v2 vs d1 flat | +0.022 [-0.033, +0.076] | 0.482 |
| jev-1.13.0 tree_v2 vs d1 tree | +0.194 [+0.140, +0.249] | 3.15e-11 |
| jev-1.13.0 tree_v2 vs d1 tree_hard | +0.168 [+0.114, +0.223] | 6.48e-09 |
| jev-1.13.0 tree_v2 vs d1 tree_v2 | +0.074 [+0.028, +0.122] | 0.00266 |
| jev-1.13.0 tree_v2 vs pplx-decider-v1.2 flat | -0.024 [-0.070, +0.024] | 0.355 |
| jev-1.13.0 tree_v2 vs pplx-decider-v1.2 tree | +0.070 [+0.015, +0.124] | 0.0159 |
| jev-1.13.0 tree_v2 vs pplx-decider-v1.2 tree_hard | +0.059 [+0.007, +0.109] | 0.0352 |
| jev-1.13.0 tree_v2 vs pplx-decider-v1.2 tree_v2 | -0.041 [-0.083, +0.002] | 0.0728 |
| jev-1.13.0 tree_v2 vs gpt-6-luna-decisions flat | -0.022 [-0.079, +0.033] | 0.48 |
| jev-1.13.0 tree_v2 vs gpt-6-luna-decisions tree | +0.214 [+0.155, +0.273] | 9.1e-12 |
| jev-1.13.0 tree_v2 vs gpt-6-luna-decisions tree_hard | +0.214 [+0.155, +0.273] | 9.1e-12 |
| jev-1.13.0 tree_v2 vs gpt-6-luna-decisions tree_v2 | +0.140 [+0.085, +0.194] | 1.02e-06 |
| jev-1.13.0 tree_v2 vs gemini-2.5-flash paper_llm | +0.028 [-0.024, +0.081] | 0.332 |
| jev-1.13.0 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.055 [+0.002, +0.107] | 0.0459 |
| jev-1.13.0 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.055 [-0.103, -0.004] | 0.0356 |
| jev-1.13.0 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.031 [-0.081, +0.020] | 0.265 |
| jev-1.14.0 flat vs jev-1.14.0 tree | +0.138 [+0.081, +0.194] | 5.37e-06 |
| jev-1.14.0 flat vs jev-1.14.0 tree_hard | +0.146 [+0.092, +0.201] | 4.44e-07 |
| jev-1.14.0 flat vs jev-1.14.0 tree_v2 | -0.035 [-0.087, +0.015] | 0.214 |
| jev-1.14.0 flat vs microsoft-decision-1 flat | +0.011 [-0.028, +0.050] | 0.668 |
| jev-1.14.0 flat vs microsoft-decision-1 tree | +0.179 [+0.122, +0.236] | 3.57e-09 |
| jev-1.14.0 flat vs microsoft-decision-1 tree_hard | +0.212 [+0.157, +0.266] | 8.94e-13 |
| jev-1.14.0 flat vs microsoft-decision-1 tree_v2 | +0.024 [-0.031, +0.076] | 0.431 |
| jev-1.14.0 flat vs d1 flat | -0.022 [-0.066, +0.022] | 0.363 |
| jev-1.14.0 flat vs d1 tree | +0.151 [+0.087, +0.216] | 5.45e-06 |
| jev-1.14.0 flat vs d1 tree_hard | +0.124 [+0.066, +0.183] | 4.94e-05 |
| jev-1.14.0 flat vs d1 tree_v2 | +0.031 [-0.026, +0.087] | 0.327 |
| jev-1.14.0 flat vs pplx-decider-v1.2 flat | -0.068 [-0.109, -0.026] | 0.00215 |
| jev-1.14.0 flat vs pplx-decider-v1.2 tree | +0.026 [-0.026, +0.081] | 0.382 |
| jev-1.14.0 flat vs pplx-decider-v1.2 tree_hard | +0.015 [-0.033, +0.063] | 0.597 |
| jev-1.14.0 flat vs pplx-decider-v1.2 tree_v2 | -0.085 [-0.131, -0.039] | 0.000499 |
| jev-1.14.0 flat vs gpt-6-luna-decisions flat | -0.066 [-0.114, -0.017] | 0.00893 |
| jev-1.14.0 flat vs gpt-6-luna-decisions tree | +0.170 [+0.105, +0.238] | 1.13e-06 |
| jev-1.14.0 flat vs gpt-6-luna-decisions tree_hard | +0.170 [+0.105, +0.238] | 1.13e-06 |
| jev-1.14.0 flat vs gpt-6-luna-decisions tree_v2 | +0.096 [+0.033, +0.162] | 0.0043 |
| jev-1.14.0 flat vs gemini-2.5-flash paper_llm | -0.015 [-0.061, +0.031] | 0.576 |
| jev-1.14.0 flat vs gemini-2.5-flash paper_llm_thinking | +0.011 [-0.031, +0.052] | 0.679 |
| jev-1.14.0 flat vs gemini-3.8-flash paper_llm_low | -0.098 [-0.140, -0.057] | 5.46e-06 |
| jev-1.14.0 flat vs gemini-3.8-flash paper_llm_thinking | -0.074 [-0.116, -0.033] | 0.000675 |
| jev-1.14.0 tree vs jev-1.14.0 tree_hard | +0.009 [-0.013, +0.031] | 0.572 |
| jev-1.14.0 tree vs jev-1.14.0 tree_v2 | -0.172 [-0.221, -0.127] | 1.44e-11 |
| jev-1.14.0 tree vs microsoft-decision-1 flat | -0.127 [-0.188, -0.068] | 6.45e-05 |
| jev-1.14.0 tree vs microsoft-decision-1 tree | +0.041 [+0.011, +0.072] | 0.011 |
| jev-1.14.0 tree vs microsoft-decision-1 tree_hard | +0.074 [+0.041, +0.107] | 2.44e-05 |
| jev-1.14.0 tree vs microsoft-decision-1 tree_v2 | -0.114 [-0.170, -0.057] | 0.000142 |
| jev-1.14.0 tree vs d1 flat | -0.159 [-0.216, -0.103] | 2.13e-07 |
| jev-1.14.0 tree vs d1 tree | +0.013 [-0.026, +0.052] | 0.59 |
| jev-1.14.0 tree vs d1 tree_hard | -0.013 [-0.052, +0.026] | 0.594 |
| jev-1.14.0 tree vs d1 tree_v2 | -0.107 [-0.159, -0.055] | 0.000126 |
| jev-1.14.0 tree vs pplx-decider-v1.2 flat | -0.205 [-0.260, -0.151] | 3.11e-12 |
| jev-1.14.0 tree vs pplx-decider-v1.2 tree | -0.111 [-0.153, -0.070] | 2.77e-07 |
| jev-1.14.0 tree vs pplx-decider-v1.2 tree_hard | -0.122 [-0.166, -0.079] | 1.11e-07 |
| jev-1.14.0 tree vs pplx-decider-v1.2 tree_v2 | -0.223 [-0.273, -0.172] | 4.79e-16 |
| jev-1.14.0 tree vs gpt-6-luna-decisions flat | -0.203 [-0.253, -0.153] | 5.27e-14 |
| jev-1.14.0 tree vs gpt-6-luna-decisions tree | +0.033 [-0.011, +0.076] | 0.176 |
| jev-1.14.0 tree vs gpt-6-luna-decisions tree_hard | +0.033 [-0.011, +0.076] | 0.176 |
| jev-1.14.0 tree vs gpt-6-luna-decisions tree_v2 | -0.041 [-0.092, +0.011] | 0.14 |
| jev-1.14.0 tree vs gemini-2.5-flash paper_llm | -0.153 [-0.210, -0.094] | 8.33e-07 |
| jev-1.14.0 tree vs gemini-2.5-flash paper_llm_thinking | -0.127 [-0.188, -0.066] | 9.62e-05 |
| jev-1.14.0 tree vs gemini-3.8-flash paper_llm_low | -0.236 [-0.286, -0.186] | 9.36e-18 |
| jev-1.14.0 tree vs gemini-3.8-flash paper_llm_thinking | -0.212 [-0.264, -0.159] | 1.25e-13 |
| jev-1.14.0 tree_hard vs jev-1.14.0 tree_v2 | -0.181 [-0.229, -0.131] | 7.2e-12 |
| jev-1.14.0 tree_hard vs microsoft-decision-1 flat | -0.135 [-0.192, -0.081] | 7.21e-06 |
| jev-1.14.0 tree_hard vs microsoft-decision-1 tree | +0.033 [-0.002, +0.068] | 0.0769 |
| jev-1.14.0 tree_hard vs microsoft-decision-1 tree_hard | +0.066 [+0.033, +0.098] | 0.000227 |
| jev-1.14.0 tree_hard vs microsoft-decision-1 tree_v2 | -0.122 [-0.179, -0.066] | 4.88e-05 |
| jev-1.14.0 tree_hard vs d1 flat | -0.168 [-0.225, -0.111] | 4.17e-08 |
| jev-1.14.0 tree_hard vs d1 tree | +0.004 [-0.039, +0.050] | 0.925 |
| jev-1.14.0 tree_hard vs d1 tree_hard | -0.022 [-0.063, +0.020] | 0.373 |
| jev-1.14.0 tree_hard vs d1 tree_v2 | -0.116 [-0.170, -0.061] | 7.53e-05 |
| jev-1.14.0 tree_hard vs pplx-decider-v1.2 flat | -0.214 [-0.269, -0.159] | 1.07e-12 |
| jev-1.14.0 tree_hard vs pplx-decider-v1.2 tree | -0.120 [-0.164, -0.076] | 1.26e-07 |
| jev-1.14.0 tree_hard vs pplx-decider-v1.2 tree_hard | -0.131 [-0.175, -0.087] | 1.53e-08 |
| jev-1.14.0 tree_hard vs pplx-decider-v1.2 tree_v2 | -0.231 [-0.284, -0.179] | 1.77e-16 |
| jev-1.14.0 tree_hard vs gpt-6-luna-decisions flat | -0.212 [-0.262, -0.162] | 8.13e-15 |
| jev-1.14.0 tree_hard vs gpt-6-luna-decisions tree | +0.024 [-0.024, +0.074] | 0.386 |
| jev-1.14.0 tree_hard vs gpt-6-luna-decisions tree_hard | +0.024 [-0.024, +0.074] | 0.386 |
| jev-1.14.0 tree_hard vs gpt-6-luna-decisions tree_v2 | -0.050 [-0.105, +0.004] | 0.0922 |
| jev-1.14.0 tree_hard vs gemini-2.5-flash paper_llm | -0.162 [-0.218, -0.105] | 1.13e-07 |
| jev-1.14.0 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.135 [-0.194, -0.076] | 1.53e-05 |
| jev-1.14.0 tree_hard vs gemini-3.8-flash paper_llm_low | -0.245 [-0.297, -0.192] | 3.62e-18 |
| jev-1.14.0 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.221 [-0.273, -0.168] | 1.46e-14 |
| jev-1.14.0 tree_v2 vs microsoft-decision-1 flat | +0.046 [-0.007, +0.098] | 0.11 |
| jev-1.14.0 tree_v2 vs microsoft-decision-1 tree | +0.214 [+0.157, +0.269] | 4.31e-13 |
| jev-1.14.0 tree_v2 vs microsoft-decision-1 tree_hard | +0.247 [+0.190, +0.301] | 2.02e-16 |
| jev-1.14.0 tree_v2 vs microsoft-decision-1 tree_v2 | +0.059 [+0.022, +0.096] | 0.00244 |
| jev-1.14.0 tree_v2 vs d1 flat | +0.013 [-0.041, +0.068] | 0.696 |
| jev-1.14.0 tree_v2 vs d1 tree | +0.186 [+0.129, +0.242] | 7.93e-10 |
| jev-1.14.0 tree_v2 vs d1 tree_hard | +0.159 [+0.103, +0.214] | 5.83e-08 |
| jev-1.14.0 tree_v2 vs d1 tree_v2 | +0.066 [+0.020, +0.114] | 0.0101 |
| jev-1.14.0 tree_v2 vs pplx-decider-v1.2 flat | -0.033 [-0.079, +0.015] | 0.203 |
| jev-1.14.0 tree_v2 vs pplx-decider-v1.2 tree | +0.061 [+0.007, +0.116] | 0.0369 |
| jev-1.14.0 tree_v2 vs pplx-decider-v1.2 tree_hard | +0.050 [-0.002, +0.103] | 0.075 |
| jev-1.14.0 tree_v2 vs pplx-decider-v1.2 tree_v2 | -0.050 [-0.092, -0.009] | 0.0281 |
| jev-1.14.0 tree_v2 vs gpt-6-luna-decisions flat | -0.031 [-0.085, +0.024] | 0.301 |
| jev-1.14.0 tree_v2 vs gpt-6-luna-decisions tree | +0.205 [+0.146, +0.266] | 1.57e-10 |
| jev-1.14.0 tree_v2 vs gpt-6-luna-decisions tree_hard | +0.205 [+0.146, +0.266] | 1.57e-10 |
| jev-1.14.0 tree_v2 vs gpt-6-luna-decisions tree_v2 | +0.131 [+0.076, +0.188] | 8.11e-06 |
| jev-1.14.0 tree_v2 vs gemini-2.5-flash paper_llm | +0.020 [-0.033, +0.072] | 0.521 |
| jev-1.14.0 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.046 [-0.004, +0.098] | 0.0964 |
| jev-1.14.0 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.063 [-0.111, -0.015] | 0.0134 |
| jev-1.14.0 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.039 [-0.090, +0.011] | 0.145 |
| microsoft-decision-1 flat vs microsoft-decision-1 tree | +0.168 [+0.111, +0.225] | 2.97e-08 |
| microsoft-decision-1 flat vs microsoft-decision-1 tree_hard | +0.201 [+0.148, +0.253] | 7.92e-13 |
| microsoft-decision-1 flat vs microsoft-decision-1 tree_v2 | +0.013 [-0.037, +0.063] | 0.679 |
| microsoft-decision-1 flat vs d1 flat | -0.033 [-0.079, +0.015] | 0.199 |
| microsoft-decision-1 flat vs d1 tree | +0.140 [+0.072, +0.207] | 6.65e-05 |
| microsoft-decision-1 flat vs d1 tree_hard | +0.114 [+0.050, +0.177] | 0.000523 |
| microsoft-decision-1 flat vs d1 tree_v2 | +0.020 [-0.041, +0.081] | 0.569 |
| microsoft-decision-1 flat vs pplx-decider-v1.2 flat | -0.079 [-0.127, -0.028] | 0.00202 |
| microsoft-decision-1 flat vs pplx-decider-v1.2 tree | +0.015 [-0.041, +0.074] | 0.657 |
| microsoft-decision-1 flat vs pplx-decider-v1.2 tree_hard | +0.004 [-0.048, +0.057] | 0.936 |
| microsoft-decision-1 flat vs pplx-decider-v1.2 tree_v2 | -0.096 [-0.146, -0.044] | 0.000278 |
| microsoft-decision-1 flat vs gpt-6-luna-decisions flat | -0.076 [-0.124, -0.028] | 0.00305 |
| microsoft-decision-1 flat vs gpt-6-luna-decisions tree | +0.159 [+0.092, +0.229] | 9.32e-06 |
| microsoft-decision-1 flat vs gpt-6-luna-decisions tree_hard | +0.159 [+0.092, +0.229] | 9.32e-06 |
| microsoft-decision-1 flat vs gpt-6-luna-decisions tree_v2 | +0.085 [+0.022, +0.151] | 0.0126 |
| microsoft-decision-1 flat vs gemini-2.5-flash paper_llm | -0.026 [-0.072, +0.022] | 0.315 |
| microsoft-decision-1 flat vs gemini-2.5-flash paper_llm_thinking | +0.000 [-0.044, +0.046] | 1 |
| microsoft-decision-1 flat vs gemini-3.8-flash paper_llm_low | -0.109 [-0.155, -0.063] | 6.91e-06 |
| microsoft-decision-1 flat vs gemini-3.8-flash paper_llm_thinking | -0.085 [-0.131, -0.039] | 0.000556 |
| microsoft-decision-1 tree vs microsoft-decision-1 tree_hard | +0.033 [+0.011, +0.055] | 0.00592 |
| microsoft-decision-1 tree vs microsoft-decision-1 tree_v2 | -0.155 [-0.205, -0.107] | 2.25e-09 |
| microsoft-decision-1 tree vs d1 flat | -0.201 [-0.258, -0.144] | 5.67e-11 |
| microsoft-decision-1 tree vs d1 tree | -0.028 [-0.070, +0.015] | 0.232 |
| microsoft-decision-1 tree vs d1 tree_hard | -0.055 [-0.100, -0.009] | 0.0199 |
| microsoft-decision-1 tree vs d1 tree_v2 | -0.148 [-0.201, -0.094] | 2.7e-07 |
| microsoft-decision-1 tree vs pplx-decider-v1.2 flat | -0.247 [-0.303, -0.190] | 1.3e-15 |
| microsoft-decision-1 tree vs pplx-decider-v1.2 tree | -0.153 [-0.197, -0.109] | 5.56e-11 |
| microsoft-decision-1 tree vs pplx-decider-v1.2 tree_hard | -0.164 [-0.210, -0.118] | 8.09e-12 |
| microsoft-decision-1 tree vs pplx-decider-v1.2 tree_v2 | -0.264 [-0.317, -0.210] | 4.01e-20 |
| microsoft-decision-1 tree vs gpt-6-luna-decisions flat | -0.245 [-0.297, -0.192] | 1.26e-18 |
| microsoft-decision-1 tree vs gpt-6-luna-decisions tree | -0.009 [-0.055, +0.039] | 0.781 |
| microsoft-decision-1 tree vs gpt-6-luna-decisions tree_hard | -0.009 [-0.055, +0.039] | 0.781 |
| microsoft-decision-1 tree vs gpt-6-luna-decisions tree_v2 | -0.083 [-0.135, -0.028] | 0.00332 |
| microsoft-decision-1 tree vs gemini-2.5-flash paper_llm | -0.194 [-0.251, -0.135] | 5.21e-10 |
| microsoft-decision-1 tree vs gemini-2.5-flash paper_llm_thinking | -0.168 [-0.227, -0.109] | 7.88e-08 |
| microsoft-decision-1 tree vs gemini-3.8-flash paper_llm_low | -0.277 [-0.332, -0.223] | 3.35e-21 |
| microsoft-decision-1 tree vs gemini-3.8-flash paper_llm_thinking | -0.253 [-0.308, -0.197] | 3.38e-17 |
| microsoft-decision-1 tree_hard vs microsoft-decision-1 tree_v2 | -0.188 [-0.240, -0.135] | 1.44e-11 |
| microsoft-decision-1 tree_hard vs d1 flat | -0.234 [-0.290, -0.177] | 2.44e-14 |
| microsoft-decision-1 tree_hard vs d1 tree | -0.061 [-0.109, -0.013] | 0.0158 |
| microsoft-decision-1 tree_hard vs d1 tree_hard | -0.087 [-0.133, -0.041] | 0.000371 |
| microsoft-decision-1 tree_hard vs d1 tree_v2 | -0.181 [-0.238, -0.124] | 2.49e-09 |
| microsoft-decision-1 tree_hard vs pplx-decider-v1.2 flat | -0.279 [-0.336, -0.223] | 2.91e-19 |
| microsoft-decision-1 tree_hard vs pplx-decider-v1.2 tree | -0.186 [-0.231, -0.140] | 3.89e-14 |
| microsoft-decision-1 tree_hard vs pplx-decider-v1.2 tree_hard | -0.197 [-0.242, -0.151] | 1.02e-15 |
| microsoft-decision-1 tree_hard vs pplx-decider-v1.2 tree_v2 | -0.297 [-0.349, -0.245] | 5.15e-24 |
| microsoft-decision-1 tree_hard vs gpt-6-luna-decisions flat | -0.277 [-0.330, -0.225] | 8.52e-23 |
| microsoft-decision-1 tree_hard vs gpt-6-luna-decisions tree | -0.041 [-0.092, +0.011] | 0.129 |
| microsoft-decision-1 tree_hard vs gpt-6-luna-decisions tree_hard | -0.041 [-0.092, +0.011] | 0.129 |
| microsoft-decision-1 tree_hard vs gpt-6-luna-decisions tree_v2 | -0.116 [-0.172, -0.059] | 0.000119 |
| microsoft-decision-1 tree_hard vs gemini-2.5-flash paper_llm | -0.227 [-0.284, -0.170] | 1.61e-13 |
| microsoft-decision-1 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.201 [-0.255, -0.146] | 2.11e-11 |
| microsoft-decision-1 tree_hard vs gemini-3.8-flash paper_llm_low | -0.310 [-0.362, -0.255] | 1.07e-25 |
| microsoft-decision-1 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.286 [-0.341, -0.231] | 1.34e-21 |
| microsoft-decision-1 tree_v2 vs d1 flat | -0.046 [-0.100, +0.011] | 0.128 |
| microsoft-decision-1 tree_v2 vs d1 tree | +0.127 [+0.066, +0.188] | 5.92e-05 |
| microsoft-decision-1 tree_v2 vs d1 tree_hard | +0.100 [+0.039, +0.164] | 0.00165 |
| microsoft-decision-1 tree_v2 vs d1 tree_v2 | +0.007 [-0.046, +0.059] | 0.868 |
| microsoft-decision-1 tree_v2 vs pplx-decider-v1.2 flat | -0.092 [-0.142, -0.039] | 0.00076 |
| microsoft-decision-1 tree_v2 vs pplx-decider-v1.2 tree | +0.002 [-0.057, +0.061] | 1 |
| microsoft-decision-1 tree_v2 vs pplx-decider-v1.2 tree_hard | -0.009 [-0.066, +0.048] | 0.819 |
| microsoft-decision-1 tree_v2 vs pplx-decider-v1.2 tree_v2 | -0.109 [-0.155, -0.061] | 1.17e-05 |
| microsoft-decision-1 tree_v2 vs gpt-6-luna-decisions flat | -0.090 [-0.146, -0.033] | 0.00269 |
| microsoft-decision-1 tree_v2 vs gpt-6-luna-decisions tree | +0.146 [+0.085, +0.207] | 7.02e-06 |
| microsoft-decision-1 tree_v2 vs gpt-6-luna-decisions tree_hard | +0.146 [+0.085, +0.207] | 7.02e-06 |
| microsoft-decision-1 tree_v2 vs gpt-6-luna-decisions tree_v2 | +0.072 [+0.015, +0.131] | 0.0171 |
| microsoft-decision-1 tree_v2 vs gemini-2.5-flash paper_llm | -0.039 [-0.094, +0.015] | 0.179 |
| microsoft-decision-1 tree_v2 vs gemini-2.5-flash paper_llm_thinking | -0.013 [-0.066, +0.039] | 0.683 |
| microsoft-decision-1 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.122 [-0.175, -0.070] | 9.9e-06 |
| microsoft-decision-1 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.098 [-0.151, -0.044] | 0.000528 |
| d1 flat vs d1 tree | +0.172 [+0.118, +0.229] | 4.72e-09 |
| d1 flat vs d1 tree_hard | +0.146 [+0.094, +0.201] | 1.59e-07 |
| d1 flat vs d1 tree_v2 | +0.052 [+0.007, +0.100] | 0.0416 |
| d1 flat vs pplx-decider-v1.2 flat | -0.046 [-0.085, -0.007] | 0.0295 |
| d1 flat vs pplx-decider-v1.2 tree | +0.048 [+0.000, +0.098] | 0.0714 |
| d1 flat vs pplx-decider-v1.2 tree_hard | +0.037 [-0.011, +0.085] | 0.149 |
| d1 flat vs pplx-decider-v1.2 tree_v2 | -0.063 [-0.105, -0.020] | 0.00508 |
| d1 flat vs gpt-6-luna-decisions flat | -0.044 [-0.090, +0.002] | 0.0773 |
| d1 flat vs gpt-6-luna-decisions tree | +0.192 [+0.133, +0.251] | 6.11e-10 |
| d1 flat vs gpt-6-luna-decisions tree_hard | +0.192 [+0.133, +0.251] | 6.11e-10 |
| d1 flat vs gpt-6-luna-decisions tree_v2 | +0.118 [+0.063, +0.175] | 5.16e-05 |
| d1 flat vs gemini-2.5-flash paper_llm | +0.007 [-0.041, +0.052] | 0.857 |
| d1 flat vs gemini-2.5-flash paper_llm_thinking | +0.033 [-0.017, +0.081] | 0.232 |
| d1 flat vs gemini-3.8-flash paper_llm_low | -0.076 [-0.118, -0.035] | 0.000562 |
| d1 flat vs gemini-3.8-flash paper_llm_thinking | -0.052 [-0.096, -0.011] | 0.021 |
| d1 tree vs d1 tree_hard | -0.026 [-0.055, +0.000] | 0.0884 |
| d1 tree vs d1 tree_v2 | -0.120 [-0.157, -0.085] | 2.05e-10 |
| d1 tree vs pplx-decider-v1.2 flat | -0.218 [-0.273, -0.166] | 3.32e-14 |
| d1 tree vs pplx-decider-v1.2 tree | -0.124 [-0.166, -0.083] | 1.01e-08 |
| d1 tree vs pplx-decider-v1.2 tree_hard | -0.135 [-0.186, -0.087] | 1.29e-07 |
| d1 tree vs pplx-decider-v1.2 tree_v2 | -0.236 [-0.286, -0.186] | 9.36e-18 |
| d1 tree vs gpt-6-luna-decisions flat | -0.216 [-0.275, -0.159] | 9.49e-13 |
| d1 tree vs gpt-6-luna-decisions tree | +0.020 [-0.011, +0.050] | 0.272 |
| d1 tree vs gpt-6-luna-decisions tree_hard | +0.020 [-0.011, +0.050] | 0.272 |
| d1 tree vs gpt-6-luna-decisions tree_v2 | -0.055 [-0.094, -0.013] | 0.0105 |
| d1 tree vs gemini-2.5-flash paper_llm | -0.166 [-0.225, -0.105] | 1.46e-07 |
| d1 tree vs gemini-2.5-flash paper_llm_thinking | -0.140 [-0.207, -0.072] | 6.21e-05 |
| d1 tree vs gemini-3.8-flash paper_llm_low | -0.249 [-0.306, -0.194] | 5.64e-17 |
| d1 tree vs gemini-3.8-flash paper_llm_thinking | -0.225 [-0.282, -0.168] | 5.09e-14 |
| d1 tree_hard vs d1 tree_v2 | -0.094 [-0.133, -0.055] | 7.35e-06 |
| d1 tree_hard vs pplx-decider-v1.2 flat | -0.192 [-0.245, -0.142] | 1.12e-12 |
| d1 tree_hard vs pplx-decider-v1.2 tree | -0.098 [-0.138, -0.061] | 1.41e-06 |
| d1 tree_hard vs pplx-decider-v1.2 tree_hard | -0.109 [-0.153, -0.066] | 1.25e-06 |
| d1 tree_hard vs pplx-decider-v1.2 tree_v2 | -0.210 [-0.258, -0.162] | 4.55e-16 |
| d1 tree_hard vs gpt-6-luna-decisions flat | -0.190 [-0.245, -0.133] | 5.38e-11 |
| d1 tree_hard vs gpt-6-luna-decisions tree | +0.046 [+0.009, +0.085] | 0.0295 |
| d1 tree_hard vs gpt-6-luna-decisions tree_hard | +0.046 [+0.009, +0.085] | 0.0295 |
| d1 tree_hard vs gpt-6-luna-decisions tree_v2 | -0.028 [-0.074, +0.017] | 0.263 |
| d1 tree_hard vs gemini-2.5-flash paper_llm | -0.140 [-0.199, -0.083] | 5.06e-06 |
| d1 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.114 [-0.177, -0.050] | 0.000623 |
| d1 tree_hard vs gemini-3.8-flash paper_llm_low | -0.223 [-0.275, -0.172] | 7.6e-16 |
| d1 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.199 [-0.251, -0.146] | 1.22e-12 |
| d1 tree_v2 vs pplx-decider-v1.2 flat | -0.098 [-0.144, -0.052] | 3.87e-05 |
| d1 tree_v2 vs pplx-decider-v1.2 tree | -0.004 [-0.052, +0.044] | 0.931 |
| d1 tree_v2 vs pplx-decider-v1.2 tree_hard | -0.015 [-0.066, +0.035] | 0.614 |
| d1 tree_v2 vs pplx-decider-v1.2 tree_v2 | -0.116 [-0.159, -0.074] | 3.78e-07 |
| d1 tree_v2 vs gpt-6-luna-decisions flat | -0.096 [-0.151, -0.041] | 0.000855 |
| d1 tree_v2 vs gpt-6-luna-decisions tree | +0.140 [+0.096, +0.186] | 3.77e-09 |
| d1 tree_v2 vs gpt-6-luna-decisions tree_hard | +0.140 [+0.096, +0.186] | 3.77e-09 |
| d1 tree_v2 vs gpt-6-luna-decisions tree_v2 | +0.066 [+0.028, +0.105] | 0.00161 |
| d1 tree_v2 vs gemini-2.5-flash paper_llm | -0.046 [-0.100, +0.009] | 0.117 |
| d1 tree_v2 vs gemini-2.5-flash paper_llm_thinking | -0.020 [-0.079, +0.039] | 0.567 |
| d1 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.129 [-0.177, -0.081] | 5.96e-07 |
| d1 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.105 [-0.155, -0.055] | 6.11e-05 |
| pplx-decider-v1.2 flat vs pplx-decider-v1.2 tree | +0.094 [+0.050, +0.140] | 5.49e-05 |
| pplx-decider-v1.2 flat vs pplx-decider-v1.2 tree_hard | +0.083 [+0.041, +0.125] | 0.000183 |
| pplx-decider-v1.2 flat vs pplx-decider-v1.2 tree_v2 | -0.017 [-0.048, +0.013] | 0.332 |
| pplx-decider-v1.2 flat vs gpt-6-luna-decisions flat | +0.002 [-0.046, +0.050] | 1 |
| pplx-decider-v1.2 flat vs gpt-6-luna-decisions tree | +0.238 [+0.183, +0.295] | 7.43e-15 |
| pplx-decider-v1.2 flat vs gpt-6-luna-decisions tree_hard | +0.238 [+0.183, +0.295] | 7.43e-15 |
| pplx-decider-v1.2 flat vs gpt-6-luna-decisions tree_v2 | +0.164 [+0.111, +0.218] | 5.74e-09 |
| pplx-decider-v1.2 flat vs gemini-2.5-flash paper_llm | +0.052 [+0.004, +0.100] | 0.0384 |
| pplx-decider-v1.2 flat vs gemini-2.5-flash paper_llm_thinking | +0.079 [+0.031, +0.129] | 0.00256 |
| pplx-decider-v1.2 flat vs gemini-3.8-flash paper_llm_low | -0.031 [-0.068, +0.007] | 0.125 |
| pplx-decider-v1.2 flat vs gemini-3.8-flash paper_llm_thinking | -0.007 [-0.044, +0.031] | 0.815 |
| pplx-decider-v1.2 tree vs pplx-decider-v1.2 tree_hard | -0.011 [-0.037, +0.015] | 0.522 |
| pplx-decider-v1.2 tree vs pplx-decider-v1.2 tree_v2 | -0.111 [-0.148, -0.076] | 3.02e-09 |
| pplx-decider-v1.2 tree vs gpt-6-luna-decisions flat | -0.092 [-0.142, -0.041] | 0.000534 |
| pplx-decider-v1.2 tree vs gpt-6-luna-decisions tree | +0.144 [+0.098, +0.190] | 4.16e-09 |
| pplx-decider-v1.2 tree vs gpt-6-luna-decisions tree_hard | +0.144 [+0.098, +0.190] | 4.16e-09 |
| pplx-decider-v1.2 tree vs gpt-6-luna-decisions tree_v2 | +0.070 [+0.020, +0.120] | 0.0101 |
| pplx-decider-v1.2 tree vs gemini-2.5-flash paper_llm | -0.041 [-0.096, +0.015] | 0.173 |
| pplx-decider-v1.2 tree vs gemini-2.5-flash paper_llm_thinking | -0.015 [-0.076, +0.044] | 0.674 |
| pplx-decider-v1.2 tree vs gemini-3.8-flash paper_llm_low | -0.124 [-0.170, -0.081] | 1.28e-07 |
| pplx-decider-v1.2 tree vs gemini-3.8-flash paper_llm_thinking | -0.100 [-0.148, -0.055] | 5.88e-05 |
| pplx-decider-v1.2 tree_hard vs pplx-decider-v1.2 tree_v2 | -0.100 [-0.135, -0.066] | 6.22e-08 |
| pplx-decider-v1.2 tree_hard vs gpt-6-luna-decisions flat | -0.081 [-0.129, -0.033] | 0.00108 |
| pplx-decider-v1.2 tree_hard vs gpt-6-luna-decisions tree | +0.155 [+0.103, +0.207] | 3.13e-08 |
| pplx-decider-v1.2 tree_hard vs gpt-6-luna-decisions tree_hard | +0.155 [+0.103, +0.207] | 3.13e-08 |
| pplx-decider-v1.2 tree_hard vs gpt-6-luna-decisions tree_v2 | +0.081 [+0.028, +0.135] | 0.00466 |
| pplx-decider-v1.2 tree_hard vs gemini-2.5-flash paper_llm | -0.031 [-0.083, +0.024] | 0.304 |
| pplx-decider-v1.2 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.004 [-0.059, +0.050] | 0.939 |
| pplx-decider-v1.2 tree_hard vs gemini-3.8-flash paper_llm_low | -0.114 [-0.157, -0.072] | 2.45e-07 |
| pplx-decider-v1.2 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.090 [-0.133, -0.046] | 0.000125 |
| pplx-decider-v1.2 tree_v2 vs gpt-6-luna-decisions flat | +0.020 [-0.028, +0.068] | 0.474 |
| pplx-decider-v1.2 tree_v2 vs gpt-6-luna-decisions tree | +0.255 [+0.201, +0.310] | 8.98e-18 |
| pplx-decider-v1.2 tree_v2 vs gpt-6-luna-decisions tree_hard | +0.255 [+0.201, +0.310] | 8.98e-18 |
| pplx-decider-v1.2 tree_v2 vs gpt-6-luna-decisions tree_v2 | +0.181 [+0.131, +0.231] | 2e-11 |
| pplx-decider-v1.2 tree_v2 vs gemini-2.5-flash paper_llm | +0.070 [+0.022, +0.118] | 0.00675 |
| pplx-decider-v1.2 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.096 [+0.046, +0.146] | 0.000373 |
| pplx-decider-v1.2 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.013 [-0.050, +0.024] | 0.567 |
| pplx-decider-v1.2 tree_v2 vs gemini-3.8-flash paper_llm_thinking | +0.011 [-0.028, +0.050] | 0.661 |
| gpt-6-luna-decisions flat vs gpt-6-luna-decisions tree | +0.236 [+0.179, +0.293] | 8.17e-15 |
| gpt-6-luna-decisions flat vs gpt-6-luna-decisions tree_hard | +0.236 [+0.179, +0.293] | 8.17e-15 |
| gpt-6-luna-decisions flat vs gpt-6-luna-decisions tree_v2 | +0.162 [+0.107, +0.216] | 3.43e-08 |
| gpt-6-luna-decisions flat vs gemini-2.5-flash paper_llm | +0.050 [+0.000, +0.100] | 0.0616 |
| gpt-6-luna-decisions flat vs gemini-2.5-flash paper_llm_thinking | +0.076 [+0.022, +0.131] | 0.00682 |
| gpt-6-luna-decisions flat vs gemini-3.8-flash paper_llm_low | -0.033 [-0.074, +0.009] | 0.151 |
| gpt-6-luna-decisions flat vs gemini-3.8-flash paper_llm_thinking | -0.009 [-0.052, +0.035] | 0.773 |
| gpt-6-luna-decisions tree vs gpt-6-luna-decisions tree_hard | +0.000 [+0.000, +0.000] | 1 |
| gpt-6-luna-decisions tree vs gpt-6-luna-decisions tree_v2 | -0.074 [-0.103, -0.048] | 1.41e-07 |
| gpt-6-luna-decisions tree vs gemini-2.5-flash paper_llm | -0.186 [-0.247, -0.124] | 7.68e-09 |
| gpt-6-luna-decisions tree vs gemini-2.5-flash paper_llm_thinking | -0.159 [-0.227, -0.092] | 7.94e-06 |
| gpt-6-luna-decisions tree vs gemini-3.8-flash paper_llm_low | -0.269 [-0.323, -0.214] | 8.15e-19 |
| gpt-6-luna-decisions tree vs gemini-3.8-flash paper_llm_thinking | -0.245 [-0.301, -0.188] | 2.84e-15 |
| gpt-6-luna-decisions tree_hard vs gpt-6-luna-decisions tree_v2 | -0.074 [-0.103, -0.048] | 1.41e-07 |
| gpt-6-luna-decisions tree_hard vs gemini-2.5-flash paper_llm | -0.186 [-0.247, -0.124] | 7.68e-09 |
| gpt-6-luna-decisions tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.159 [-0.227, -0.092] | 7.94e-06 |
| gpt-6-luna-decisions tree_hard vs gemini-3.8-flash paper_llm_low | -0.269 [-0.323, -0.214] | 8.15e-19 |
| gpt-6-luna-decisions tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.245 [-0.301, -0.188] | 2.84e-15 |
| gpt-6-luna-decisions tree_v2 vs gemini-2.5-flash paper_llm | -0.111 [-0.168, -0.055] | 0.000236 |
| gpt-6-luna-decisions tree_v2 vs gemini-2.5-flash paper_llm_thinking | -0.085 [-0.151, -0.022] | 0.0119 |
| gpt-6-luna-decisions tree_v2 vs gemini-3.8-flash paper_llm_low | -0.194 [-0.249, -0.140] | 1.82e-11 |
| gpt-6-luna-decisions tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.170 [-0.227, -0.114] | 8.29e-09 |
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

**jev-1.14.0 flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 79 | 16 | 6 | 30 | 30 |
| Comp | 10 | 71 | 7 | 13 | 14 |
| Opin | 4 | 17 | 72 | 3 | 19 |
| Outd | 9 | 1 | 0 | 46 | 6 |
| Misi | 0 | 1 | 1 | 0 | 3 |

**jev-1.14.0 tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 110 | 45 | 0 | 1 | 5 |
| Comp | 22 | 93 | 0 | 0 | 0 |
| Opin | 6 | 106 | 1 | 0 | 2 |
| Outd | 20 | 35 | 0 | 3 | 4 |
| Misi | 0 | 4 | 0 | 0 | 1 |

**jev-1.14.0 tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 94 | 53 | 0 | 3 | 11 |
| Comp | 19 | 96 | 0 | 0 | 0 |
| Opin | 4 | 99 | 5 | 1 | 6 |
| Outd | 17 | 32 | 0 | 7 | 6 |
| Misi | 0 | 3 | 0 | 0 | 2 |

**jev-1.14.0 tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 111 | 27 | 17 | 3 | 3 |
| Comp | 25 | 64 | 26 | 0 | 0 |
| Opin | 9 | 6 | 100 | 0 | 0 |
| Outd | 20 | 24 | 6 | 12 | 0 |
| Misi | 0 | 3 | 1 | 1 | 0 |

**microsoft-decision-1 flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 66 | 36 | 7 | 28 | 24 |
| Comp | 9 | 79 | 7 | 12 | 8 |
| Opin | 1 | 28 | 78 | 0 | 8 |
| Outd | 9 | 5 | 0 | 42 | 6 |
| Misi | 0 | 3 | 1 | 0 | 1 |

**microsoft-decision-1 tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 94 | 63 | 0 | 1 | 3 |
| Comp | 23 | 91 | 0 | 0 | 1 |
| Opin | 8 | 107 | 0 | 0 | 0 |
| Outd | 15 | 42 | 0 | 3 | 2 |
| Misi | 1 | 3 | 0 | 0 | 1 |

**microsoft-decision-1 tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 73 | 72 | 0 | 5 | 11 |
| Comp | 19 | 95 | 0 | 0 | 1 |
| Opin | 7 | 105 | 1 | 0 | 2 |
| Outd | 9 | 44 | 0 | 4 | 5 |
| Misi | 0 | 4 | 0 | 0 | 1 |

**microsoft-decision-1 tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 98 | 39 | 18 | 5 | 1 |
| Comp | 25 | 57 | 32 | 0 | 1 |
| Opin | 8 | 7 | 100 | 0 | 0 |
| Outd | 16 | 34 | 6 | 5 | 1 |
| Misi | 1 | 2 | 2 | 0 | 0 |

**d1 flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 108 | 14 | 5 | 27 | 7 |
| Comp | 36 | 60 | 4 | 14 | 1 |
| Opin | 28 | 17 | 62 | 2 | 6 |
| Outd | 10 | 1 | 0 | 51 | 0 |
| Misi | 4 | 0 | 0 | 1 | 0 |

**d1 tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 143 | 14 | 0 | 3 | 1 |
| Comp | 65 | 50 | 0 | 0 | 0 |
| Opin | 52 | 62 | 0 | 0 | 1 |
| Outd | 35 | 19 | 0 | 8 | 0 |
| Misi | 3 | 1 | 0 | 0 | 1 |

**d1 tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 130 | 13 | 1 | 12 | 5 |
| Comp | 56 | 57 | 0 | 1 | 1 |
| Opin | 34 | 74 | 5 | 1 | 1 |
| Outd | 20 | 22 | 0 | 20 | 0 |
| Misi | 2 | 1 | 0 | 0 | 2 |

**d1 tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 140 | 10 | 2 | 8 | 1 |
| Comp | 66 | 43 | 4 | 2 | 0 |
| Opin | 51 | 4 | 60 | 0 | 0 |
| Outd | 31 | 16 | 2 | 13 | 0 |
| Misi | 3 | 0 | 0 | 1 | 1 |

**pplx-decider-v1.2 flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 119 | 9 | 9 | 20 | 4 |
| Comp | 36 | 56 | 8 | 10 | 5 |
| Opin | 19 | 7 | 79 | 4 | 6 |
| Outd | 15 | 0 | 0 | 47 | 0 |
| Misi | 3 | 0 | 0 | 1 | 1 |

**pplx-decider-v1.2 tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 129 | 19 | 0 | 8 | 5 |
| Comp | 32 | 76 | 0 | 3 | 4 |
| Opin | 21 | 65 | 19 | 2 | 8 |
| Outd | 18 | 9 | 0 | 35 | 0 |
| Misi | 2 | 2 | 0 | 1 | 0 |

**pplx-decider-v1.2 tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 115 | 21 | 1 | 16 | 8 |
| Comp | 27 | 77 | 1 | 5 | 5 |
| Opin | 16 | 52 | 32 | 4 | 11 |
| Outd | 12 | 10 | 0 | 39 | 1 |
| Misi | 1 | 2 | 0 | 1 | 1 |

**pplx-decider-v1.2 tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 125 | 17 | 4 | 12 | 3 |
| Comp | 34 | 68 | 7 | 4 | 2 |
| Opin | 24 | 7 | 79 | 3 | 2 |
| Outd | 15 | 9 | 0 | 38 | 0 |
| Misi | 2 | 2 | 0 | 1 | 0 |

**gpt-6-luna-decisions flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 110 | 26 | 4 | 16 | 5 |
| Comp | 16 | 91 | 4 | 3 | 1 |
| Opin | 9 | 33 | 57 | 0 | 16 |
| Outd | 17 | 2 | 0 | 43 | 0 |
| Misi | 5 | 0 | 0 | 0 | 0 |

**gpt-6-luna-decisions tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 152 | 9 | 0 | 0 | 0 |
| Comp | 74 | 41 | 0 | 0 | 0 |
| Opin | 78 | 37 | 0 | 0 | 0 |
| Outd | 39 | 20 | 0 | 0 | 3 |
| Misi | 5 | 0 | 0 | 0 | 0 |

**gpt-6-luna-decisions tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 152 | 9 | 0 | 0 | 0 |
| Comp | 74 | 41 | 0 | 0 | 0 |
| Opin | 75 | 40 | 0 | 0 | 0 |
| Outd | 38 | 20 | 0 | 0 | 4 |
| Misi | 5 | 0 | 0 | 0 | 0 |

**gpt-6-luna-decisions tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 152 | 7 | 2 | 0 | 0 |
| Comp | 75 | 36 | 4 | 0 | 0 |
| Opin | 78 | 1 | 36 | 0 | 0 |
| Outd | 39 | 19 | 0 | 3 | 1 |
| Misi | 5 | 0 | 0 | 0 | 0 |

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
