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
| pplx-decider-v1.2 flat | 0.659 [0.616, 0.701] | 0.662 | 0.554 | 0.054 | 0.453 | 0.839 | 0 | 4293 | 0.086 | 0.42 / 0.59 |
| pplx-decider-v1.2 tree | 0.566 [0.520, 0.609] | 0.568 | 0.431 | 0.146 | 0.607 | 1.171 | 0 | 4113 | 0.082 | 0.40 / 0.58 |
| pplx-decider-v1.2 tree_hard | 0.576 [0.531, 0.620] | 0.581 | 0.471 | – | – | – | 0 | 4113 | 0.082 | 0.40 / 0.58 |
| pplx-decider-v1.2 tree_v2 | 0.677 [0.633, 0.718] | 0.679 | 0.544 | 0.060 | 0.461 | 0.939 | 0 | 4113 | 0.082 | 0.40 / 0.58 |
| pplx-decider-flash-v1.2 flat | 0.607 [0.561, 0.651] | 0.609 | 0.484 | 0.029 | 0.528 | 1.025 | 0 | 4293 | 0.043 | 0.31 / 0.47 |
| pplx-decider-flash-v1.2 tree | 0.465 [0.419, 0.511] | 0.472 | 0.307 | 0.161 | 0.697 | 1.396 | 0 | 19614 | 0.196 | 0.49 / 0.74 |
| pplx-decider-flash-v1.2 tree_hard | 0.478 [0.432, 0.524] | 0.489 | 0.354 | – | – | – | 0 | 19614 | 0.196 | 0.49 / 0.74 |
| pplx-decider-flash-v1.2 tree_v2 | 0.581 [0.535, 0.624] | 0.585 | 0.446 | 0.091 | 0.559 | 1.047 | 0 | 19614 | 0.196 | 0.49 / 0.74 |
| gpt-6-luna-decisions flat | 0.657 [0.614, 0.701] | 0.657 | 0.540 | 0.073 | 0.529 | 1.091 | 0 | 4145 | 0.414 | 0.36 / 0.61 |
| gpt-6-luna-decisions tree | 0.421 [0.376, 0.467] | 0.428 | 0.193 | 0.431 | 0.948 | 2.842 | 0 | 4497 | 0.450 | 0.39 / 0.70 |
| gpt-6-luna-decisions tree_hard | 0.421 [0.376, 0.467] | 0.430 | 0.193 | – | – | – | 0 | 4497 | 0.450 | 0.39 / 0.70 |
| gpt-6-luna-decisions tree_v2 | 0.496 [0.450, 0.541] | 0.498 | 0.310 | 0.353 | 0.800 | 1.931 | 0 | 4497 | 0.450 | 0.39 / 0.70 |
| d1 flat | 0.614 [0.570, 0.657] | 0.616 | 0.504 | 0.080 | 0.514 | 0.977 | 0 | 4226 | 0.085 | 0.42 / 0.59 |
| d1 tree | 0.441 [0.395, 0.487] | 0.441 | 0.295 | 0.229 | 0.735 | 1.450 | 0 | 4024 | 0.080 | 0.52 / 0.69 |
| d1 tree_hard | 0.467 [0.421, 0.513] | 0.467 | 0.367 | – | – | – | 0 | 4024 | 0.080 | 0.52 / 0.69 |
| d1 tree_v2 | 0.561 [0.515, 0.605] | 0.563 | 0.464 | 0.123 | 0.576 | 1.092 | 0 | 4024 | 0.080 | 0.52 / 0.69 |
| d1-ultra flat | 0.668 [0.624, 0.710] | 0.670 | 0.533 | 0.024 | 0.437 | 0.793 | 0 | 4226 | 0.177 | 0.46 / 0.71 |
| d1-ultra tree | 0.500 [0.452, 0.544] | 0.504 | 0.329 | 0.116 | 0.611 | 1.147 | 0 | 4024 | 0.169 | 0.49 / 0.81 |
| d1-ultra tree_hard | 0.555 [0.509, 0.598] | 0.561 | 0.434 | – | – | – | 0 | 4024 | 0.169 | 0.49 / 0.81 |
| d1-ultra tree_v2 | 0.614 [0.568, 0.657] | 0.618 | 0.465 | 0.070 | 0.515 | 0.975 | 0 | 4024 | 0.169 | 0.49 / 0.81 |
| microsoft-decision-1 flat | 0.581 [0.535, 0.627] | 0.594 | 0.500 | 0.186 | 0.577 | 1.131 | 0 | 4220 | 0.177 | 0.45 / 0.65 |
| microsoft-decision-1 tree | 0.413 [0.367, 0.459] | 0.417 | 0.262 | 0.298 | 0.822 | 1.659 | 0 | 3985 | 0.167 | 0.56 / 0.74 |
| microsoft-decision-1 tree_hard | 0.380 [0.336, 0.424] | 0.391 | 0.238 | – | – | – | 0 | 3985 | 0.167 | 0.56 / 0.74 |
| microsoft-decision-1 tree_v2 | 0.568 [0.522, 0.611] | 0.570 | 0.391 | 0.117 | 0.550 | 1.050 | 0 | 3985 | 0.167 | 0.56 / 0.74 |
| elephant-1 flat | 0.646 [0.603, 0.690] | 0.648 | 0.510 | 0.038 | 0.472 | 0.883 | 0 | 4304 | 0.000 | 0.49 / 0.72 |
| elephant-1 tree | 0.469 [0.424, 0.515] | 0.472 | 0.246 | 0.163 | 0.688 | 1.348 | 0 | 4250 | 0.000 | 0.42 / 0.65 |
| elephant-1 tree_hard | 0.511 [0.465, 0.557] | 0.517 | 0.373 | – | – | – | 0 | 4250 | 0.000 | 0.42 / 0.65 |
| elephant-1 tree_v2 | 0.581 [0.535, 0.627] | 0.583 | 0.401 | 0.070 | 0.554 | 1.029 | 0 | 4250 | 0.000 | 0.42 / 0.65 |
| mammoth-1 flat | 0.653 [0.609, 0.697] | 0.655 | 0.525 | 0.053 | 0.476 | 0.881 | 0 | 4304 | 0.000 | 0.60 / 0.86 |
| mammoth-1 tree | 0.480 [0.434, 0.526] | 0.485 | 0.307 | 0.159 | 0.659 | 1.254 | 0 | 4250 | 0.000 | 0.62 / 0.94 |
| mammoth-1 tree_hard | 0.520 [0.474, 0.566] | 0.535 | 0.398 | – | – | – | 0 | 4250 | 0.000 | 0.62 / 0.94 |
| mammoth-1 tree_v2 | 0.581 [0.535, 0.624] | 0.583 | 0.431 | 0.135 | 0.562 | 1.060 | 0 | 4250 | 0.000 | 0.62 / 0.94 |
| scaledown-classify-1 flat | 0.500 [0.454, 0.546] | 0.500 | 0.373 | 0.077 | 0.642 | 1.285 | 0 | 4757 | 0.238 | 0.72 / 1.58 |
| scaledown-classify-1 tree | 0.371 [0.325, 0.415] | 0.371 | 0.145 | 0.122 | 0.768 | 1.511 | 0 | 20039 | 1.002 | 0.73 / 1.56 |
| scaledown-classify-1 tree_hard | 0.332 [0.288, 0.376] | 0.332 | 0.212 | – | – | – | 0 | 20039 | 1.002 | 0.73 / 1.56 |
| scaledown-classify-1 tree_v2 | 0.393 [0.347, 0.437] | 0.393 | 0.174 | 0.098 | 0.693 | 1.293 | 0 | 20039 | 1.002 | 0.73 / 1.56 |
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
| pplx-decider-v1.2 flat | 0.674 | 0.599 | 0.749 | 0.653 | 0.095 |
| pplx-decider-v1.2 tree | 0.711 | 0.531 | 0.284 | 0.631 | 0.000 |
| pplx-decider-v1.2 tree_hard | 0.693 | 0.556 | 0.430 | 0.614 | 0.065 |
| pplx-decider-v1.2 tree_v2 | 0.693 | 0.624 | 0.771 | 0.633 | 0.000 |
| pplx-decider-flash-v1.2 flat | 0.661 | 0.546 | 0.656 | 0.556 | 0.000 |
| pplx-decider-flash-v1.2 tree | 0.631 | 0.450 | 0.000 | 0.370 | 0.083 |
| pplx-decider-flash-v1.2 tree_hard | 0.623 | 0.492 | 0.083 | 0.524 | 0.049 |
| pplx-decider-flash-v1.2 tree_v2 | 0.626 | 0.552 | 0.630 | 0.421 | 0.000 |
| gpt-6-luna-decisions flat | 0.692 | 0.682 | 0.633 | 0.694 | 0.000 |
| gpt-6-luna-decisions tree | 0.597 | 0.369 | 0.000 | 0.000 | 0.000 |
| gpt-6-luna-decisions tree_hard | 0.602 | 0.364 | 0.000 | 0.000 | 0.000 |
| gpt-6-luna-decisions tree_v2 | 0.596 | 0.404 | 0.459 | 0.092 | 0.000 |
| d1 flat | 0.622 | 0.580 | 0.667 | 0.650 | 0.000 |
| d1 tree | 0.623 | 0.383 | 0.000 | 0.219 | 0.250 |
| d1 tree_hard | 0.645 | 0.404 | 0.083 | 0.417 | 0.286 |
| d1 tree_v2 | 0.619 | 0.457 | 0.656 | 0.302 | 0.286 |
| d1-ultra flat | 0.697 | 0.565 | 0.784 | 0.618 | 0.000 |
| d1-ultra tree | 0.665 | 0.453 | 0.242 | 0.286 | 0.000 |
| d1-ultra tree_hard | 0.699 | 0.538 | 0.389 | 0.544 | 0.000 |
| d1-ultra tree_v2 | 0.656 | 0.491 | 0.736 | 0.442 | 0.000 |
| microsoft-decision-1 flat | 0.537 | 0.594 | 0.750 | 0.583 | 0.038 |
| microsoft-decision-1 tree | 0.623 | 0.432 | 0.000 | 0.091 | 0.167 |
| microsoft-decision-1 tree_hard | 0.543 | 0.437 | 0.017 | 0.113 | 0.080 |
| microsoft-decision-1 tree_v2 | 0.634 | 0.449 | 0.733 | 0.139 | 0.000 |
| elephant-1 flat | 0.694 | 0.596 | 0.681 | 0.581 | 0.000 |
| elephant-1 tree | 0.640 | 0.480 | 0.017 | 0.091 | 0.000 |
| elephant-1 tree_hard | 0.670 | 0.516 | 0.175 | 0.357 | 0.148 |
| elephant-1 tree_v2 | 0.649 | 0.511 | 0.649 | 0.197 | 0.000 |
| mammoth-1 flat | 0.688 | 0.552 | 0.776 | 0.611 | 0.000 |
| mammoth-1 tree | 0.622 | 0.440 | 0.256 | 0.216 | 0.000 |
| mammoth-1 tree_hard | 0.652 | 0.468 | 0.430 | 0.440 | 0.000 |
| mammoth-1 tree_v2 | 0.639 | 0.436 | 0.684 | 0.396 | 0.000 |
| scaledown-classify-1 flat | 0.612 | 0.428 | 0.554 | 0.270 | 0.000 |
| scaledown-classify-1 tree | 0.545 | 0.182 | 0.000 | 0.000 | 0.000 |
| scaledown-classify-1 tree_hard | 0.454 | 0.351 | 0.155 | 0.098 | 0.000 |
| scaledown-classify-1 tree_v2 | 0.540 | 0.076 | 0.256 | 0.000 | 0.000 |
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
| jev-1.13.0 flat vs pplx-decider-v1.2 flat | -0.050 [-0.090, -0.009] | 0.0178 |
| jev-1.13.0 flat vs pplx-decider-v1.2 tree | +0.044 [-0.007, +0.094] | 0.113 |
| jev-1.13.0 flat vs pplx-decider-v1.2 tree_hard | +0.033 [-0.013, +0.079] | 0.203 |
| jev-1.13.0 flat vs pplx-decider-v1.2 tree_v2 | -0.068 [-0.111, -0.024] | 0.00322 |
| jev-1.13.0 flat vs pplx-decider-flash-v1.2 flat | +0.002 [-0.046, +0.050] | 1 |
| jev-1.13.0 flat vs pplx-decider-flash-v1.2 tree | +0.144 [+0.085, +0.203] | 3.98e-06 |
| jev-1.13.0 flat vs pplx-decider-flash-v1.2 tree_hard | +0.131 [+0.074, +0.186] | 1.03e-05 |
| jev-1.13.0 flat vs pplx-decider-flash-v1.2 tree_v2 | +0.028 [-0.024, +0.083] | 0.338 |
| jev-1.13.0 flat vs gpt-6-luna-decisions flat | -0.048 [-0.096, +0.000] | 0.0609 |
| jev-1.13.0 flat vs gpt-6-luna-decisions tree | +0.188 [+0.124, +0.253] | 3.37e-08 |
| jev-1.13.0 flat vs gpt-6-luna-decisions tree_hard | +0.188 [+0.124, +0.253] | 3.37e-08 |
| jev-1.13.0 flat vs gpt-6-luna-decisions tree_v2 | +0.114 [+0.052, +0.175] | 0.000462 |
| jev-1.13.0 flat vs d1 flat | -0.004 [-0.046, +0.039] | 0.92 |
| jev-1.13.0 flat vs d1 tree | +0.168 [+0.107, +0.229] | 1.63e-07 |
| jev-1.13.0 flat vs d1 tree_hard | +0.142 [+0.087, +0.199] | 1.33e-06 |
| jev-1.13.0 flat vs d1 tree_v2 | +0.048 [-0.007, +0.103] | 0.0987 |
| jev-1.13.0 flat vs d1-ultra flat | -0.059 [-0.105, -0.015] | 0.0116 |
| jev-1.13.0 flat vs d1-ultra tree | +0.109 [+0.052, +0.168] | 0.000379 |
| jev-1.13.0 flat vs d1-ultra tree_hard | +0.055 [+0.004, +0.107] | 0.0489 |
| jev-1.13.0 flat vs d1-ultra tree_v2 | -0.004 [-0.057, +0.050] | 0.937 |
| jev-1.13.0 flat vs microsoft-decision-1 flat | +0.028 [-0.015, +0.070] | 0.232 |
| jev-1.13.0 flat vs microsoft-decision-1 tree | +0.197 [+0.140, +0.253] | 5.95e-11 |
| jev-1.13.0 flat vs microsoft-decision-1 tree_hard | +0.229 [+0.175, +0.284] | 7.44e-15 |
| jev-1.13.0 flat vs microsoft-decision-1 tree_v2 | +0.041 [-0.013, +0.096] | 0.156 |
| jev-1.13.0 flat vs elephant-1 flat | -0.037 [-0.083, +0.011] | 0.145 |
| jev-1.13.0 flat vs elephant-1 tree | +0.140 [+0.079, +0.201] | 1.59e-05 |
| jev-1.13.0 flat vs elephant-1 tree_hard | +0.098 [+0.039, +0.157] | 0.00147 |
| jev-1.13.0 flat vs elephant-1 tree_v2 | +0.028 [-0.028, +0.085] | 0.372 |
| jev-1.13.0 flat vs mammoth-1 flat | -0.044 [-0.087, +0.000] | 0.0619 |
| jev-1.13.0 flat vs mammoth-1 tree | +0.129 [+0.070, +0.188] | 3.16e-05 |
| jev-1.13.0 flat vs mammoth-1 tree_hard | +0.090 [+0.037, +0.142] | 0.00124 |
| jev-1.13.0 flat vs mammoth-1 tree_v2 | +0.028 [-0.026, +0.083] | 0.353 |
| jev-1.13.0 flat vs scaledown-classify-1 flat | +0.109 [+0.052, +0.166] | 0.000259 |
| jev-1.13.0 flat vs scaledown-classify-1 tree | +0.238 [+0.175, +0.303] | 6.46e-12 |
| jev-1.13.0 flat vs scaledown-classify-1 tree_hard | +0.277 [+0.221, +0.336] | 2.46e-18 |
| jev-1.13.0 flat vs scaledown-classify-1 tree_v2 | +0.216 [+0.155, +0.282] | 2.19e-10 |
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
| jev-1.13.0 tree vs pplx-decider-v1.2 flat | -0.186 [-0.240, -0.131] | 2.54e-10 |
| jev-1.13.0 tree vs pplx-decider-v1.2 tree | -0.092 [-0.133, -0.050] | 2.15e-05 |
| jev-1.13.0 tree vs pplx-decider-v1.2 tree_hard | -0.103 [-0.146, -0.059] | 6.28e-06 |
| jev-1.13.0 tree vs pplx-decider-v1.2 tree_v2 | -0.203 [-0.255, -0.153] | 1.18e-13 |
| jev-1.13.0 tree vs pplx-decider-flash-v1.2 flat | -0.133 [-0.186, -0.083] | 1.06e-06 |
| jev-1.13.0 tree vs pplx-decider-flash-v1.2 tree | +0.009 [-0.028, +0.046] | 0.731 |
| jev-1.13.0 tree vs pplx-decider-flash-v1.2 tree_hard | -0.004 [-0.041, +0.033] | 0.909 |
| jev-1.13.0 tree vs pplx-decider-flash-v1.2 tree_v2 | -0.107 [-0.157, -0.059] | 3.94e-05 |
| jev-1.13.0 tree vs gpt-6-luna-decisions flat | -0.183 [-0.236, -0.133] | 1.3e-11 |
| jev-1.13.0 tree vs gpt-6-luna-decisions tree | +0.052 [+0.009, +0.094] | 0.0223 |
| jev-1.13.0 tree vs gpt-6-luna-decisions tree_hard | +0.052 [+0.009, +0.094] | 0.0223 |
| jev-1.13.0 tree vs gpt-6-luna-decisions tree_v2 | -0.022 [-0.072, +0.028] | 0.45 |
| jev-1.13.0 tree vs d1 flat | -0.140 [-0.197, -0.083] | 3.99e-06 |
| jev-1.13.0 tree vs d1 tree | +0.033 [-0.007, +0.072] | 0.119 |
| jev-1.13.0 tree vs d1 tree_hard | +0.007 [-0.033, +0.046] | 0.822 |
| jev-1.13.0 tree vs d1 tree_v2 | -0.087 [-0.140, -0.037] | 0.00137 |
| jev-1.13.0 tree vs d1-ultra flat | -0.194 [-0.251, -0.138] | 2.77e-10 |
| jev-1.13.0 tree vs d1-ultra tree | -0.026 [-0.068, +0.015] | 0.266 |
| jev-1.13.0 tree vs d1-ultra tree_hard | -0.081 [-0.124, -0.039] | 0.000296 |
| jev-1.13.0 tree vs d1-ultra tree_v2 | -0.140 [-0.192, -0.087] | 1.02e-06 |
| jev-1.13.0 tree vs microsoft-decision-1 flat | -0.107 [-0.168, -0.048] | 0.000761 |
| jev-1.13.0 tree vs microsoft-decision-1 tree | +0.061 [+0.028, +0.094] | 0.000307 |
| jev-1.13.0 tree vs microsoft-decision-1 tree_hard | +0.094 [+0.059, +0.129] | 2.67e-07 |
| jev-1.13.0 tree vs microsoft-decision-1 tree_v2 | -0.094 [-0.153, -0.037] | 0.00194 |
| jev-1.13.0 tree vs elephant-1 flat | -0.172 [-0.223, -0.122] | 2.64e-10 |
| jev-1.13.0 tree vs elephant-1 tree | +0.004 [-0.033, +0.041] | 0.908 |
| jev-1.13.0 tree vs elephant-1 tree_hard | -0.037 [-0.074, +0.000] | 0.0675 |
| jev-1.13.0 tree vs elephant-1 tree_v2 | -0.107 [-0.159, -0.057] | 9.18e-05 |
| jev-1.13.0 tree vs mammoth-1 flat | -0.179 [-0.236, -0.124] | 4.33e-09 |
| jev-1.13.0 tree vs mammoth-1 tree | -0.007 [-0.050, +0.037] | 0.844 |
| jev-1.13.0 tree vs mammoth-1 tree_hard | -0.046 [-0.094, +0.000] | 0.0709 |
| jev-1.13.0 tree vs mammoth-1 tree_v2 | -0.107 [-0.159, -0.055] | 0.000185 |
| jev-1.13.0 tree vs scaledown-classify-1 flat | -0.026 [-0.081, +0.028] | 0.385 |
| jev-1.13.0 tree vs scaledown-classify-1 tree | +0.103 [+0.055, +0.151] | 5.63e-05 |
| jev-1.13.0 tree vs scaledown-classify-1 tree_hard | +0.142 [+0.094, +0.190] | 1.94e-08 |
| jev-1.13.0 tree vs scaledown-classify-1 tree_v2 | +0.081 [+0.028, +0.133] | 0.00326 |
| jev-1.13.0 tree vs gemini-2.5-flash paper_llm | -0.133 [-0.192, -0.076] | 1.34e-05 |
| jev-1.13.0 tree vs gemini-2.5-flash paper_llm_thinking | -0.107 [-0.168, -0.046] | 0.000908 |
| jev-1.13.0 tree vs gemini-3.8-flash paper_llm_low | -0.216 [-0.266, -0.166] | 2.02e-15 |
| jev-1.13.0 tree vs gemini-3.8-flash paper_llm_thinking | -0.192 [-0.245, -0.140] | 1.15e-11 |
| jev-1.13.0 tree_hard vs jev-1.13.0 tree_v2 | -0.175 [-0.225, -0.124] | 1.75e-10 |
| jev-1.13.0 tree_hard vs jev-1.14.0 flat | -0.131 [-0.186, -0.079] | 5.56e-06 |
| jev-1.13.0 tree_hard vs jev-1.14.0 tree | +0.007 [-0.017, +0.031] | 0.728 |
| jev-1.13.0 tree_hard vs jev-1.14.0 tree_hard | +0.015 [-0.007, +0.037] | 0.248 |
| jev-1.13.0 tree_hard vs jev-1.14.0 tree_v2 | -0.166 [-0.216, -0.116] | 5.12e-10 |
| jev-1.13.0 tree_hard vs pplx-decider-v1.2 flat | -0.199 [-0.255, -0.144] | 2.41e-11 |
| jev-1.13.0 tree_hard vs pplx-decider-v1.2 tree | -0.105 [-0.148, -0.061] | 2.74e-06 |
| jev-1.13.0 tree_hard vs pplx-decider-v1.2 tree_hard | -0.116 [-0.159, -0.072] | 4.91e-07 |
| jev-1.13.0 tree_hard vs pplx-decider-v1.2 tree_v2 | -0.216 [-0.269, -0.166] | 4.89e-15 |
| jev-1.13.0 tree_hard vs pplx-decider-flash-v1.2 flat | -0.146 [-0.201, -0.094] | 3.21e-07 |
| jev-1.13.0 tree_hard vs pplx-decider-flash-v1.2 tree | -0.004 [-0.048, +0.039] | 0.922 |
| jev-1.13.0 tree_hard vs pplx-decider-flash-v1.2 tree_hard | -0.017 [-0.059, +0.024] | 0.475 |
| jev-1.13.0 tree_hard vs pplx-decider-flash-v1.2 tree_v2 | -0.120 [-0.172, -0.066] | 1.98e-05 |
| jev-1.13.0 tree_hard vs gpt-6-luna-decisions flat | -0.197 [-0.249, -0.146] | 3.12e-13 |
| jev-1.13.0 tree_hard vs gpt-6-luna-decisions tree | +0.039 [-0.009, +0.087] | 0.139 |
| jev-1.13.0 tree_hard vs gpt-6-luna-decisions tree_hard | +0.039 [-0.009, +0.087] | 0.139 |
| jev-1.13.0 tree_hard vs gpt-6-luna-decisions tree_v2 | -0.035 [-0.090, +0.020] | 0.247 |
| jev-1.13.0 tree_hard vs d1 flat | -0.153 [-0.210, -0.098] | 3.09e-07 |
| jev-1.13.0 tree_hard vs d1 tree | +0.020 [-0.024, +0.063] | 0.444 |
| jev-1.13.0 tree_hard vs d1 tree_hard | -0.007 [-0.048, +0.035] | 0.836 |
| jev-1.13.0 tree_hard vs d1 tree_v2 | -0.100 [-0.155, -0.046] | 0.00052 |
| jev-1.13.0 tree_hard vs d1-ultra flat | -0.207 [-0.266, -0.151] | 3.64e-11 |
| jev-1.13.0 tree_hard vs d1-ultra tree | -0.039 [-0.085, +0.009] | 0.127 |
| jev-1.13.0 tree_hard vs d1-ultra tree_hard | -0.094 [-0.140, -0.048] | 0.000115 |
| jev-1.13.0 tree_hard vs d1-ultra tree_v2 | -0.153 [-0.210, -0.096] | 4.16e-07 |
| jev-1.13.0 tree_hard vs microsoft-decision-1 flat | -0.120 [-0.179, -0.063] | 6.4e-05 |
| jev-1.13.0 tree_hard vs microsoft-decision-1 tree | +0.048 [+0.015, +0.081] | 0.00535 |
| jev-1.13.0 tree_hard vs microsoft-decision-1 tree_hard | +0.081 [+0.048, +0.114] | 1.97e-06 |
| jev-1.13.0 tree_hard vs microsoft-decision-1 tree_v2 | -0.107 [-0.164, -0.050] | 0.000309 |
| jev-1.13.0 tree_hard vs elephant-1 flat | -0.186 [-0.240, -0.131] | 1.55e-10 |
| jev-1.13.0 tree_hard vs elephant-1 tree | -0.009 [-0.052, +0.035] | 0.767 |
| jev-1.13.0 tree_hard vs elephant-1 tree_hard | -0.050 [-0.092, -0.009] | 0.022 |
| jev-1.13.0 tree_hard vs elephant-1 tree_v2 | -0.120 [-0.177, -0.066] | 4.79e-05 |
| jev-1.13.0 tree_hard vs mammoth-1 flat | -0.192 [-0.251, -0.135] | 9.13e-10 |
| jev-1.13.0 tree_hard vs mammoth-1 tree | -0.020 [-0.070, +0.031] | 0.485 |
| jev-1.13.0 tree_hard vs mammoth-1 tree_hard | -0.059 [-0.111, -0.009] | 0.0316 |
| jev-1.13.0 tree_hard vs mammoth-1 tree_v2 | -0.120 [-0.177, -0.063] | 7.03e-05 |
| jev-1.13.0 tree_hard vs scaledown-classify-1 flat | -0.039 [-0.094, +0.015] | 0.19 |
| jev-1.13.0 tree_hard vs scaledown-classify-1 tree | +0.090 [+0.037, +0.144] | 0.00154 |
| jev-1.13.0 tree_hard vs scaledown-classify-1 tree_hard | +0.129 [+0.081, +0.177] | 4.87e-07 |
| jev-1.13.0 tree_hard vs scaledown-classify-1 tree_v2 | +0.068 [+0.011, +0.124] | 0.0247 |
| jev-1.13.0 tree_hard vs gemini-2.5-flash paper_llm | -0.146 [-0.201, -0.090] | 9.38e-07 |
| jev-1.13.0 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.120 [-0.177, -0.063] | 9.18e-05 |
| jev-1.13.0 tree_hard vs gemini-3.8-flash paper_llm_low | -0.229 [-0.279, -0.179] | 6.88e-17 |
| jev-1.13.0 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.205 [-0.258, -0.155] | 1.1e-13 |
| jev-1.13.0 tree_v2 vs jev-1.14.0 flat | +0.044 [-0.009, +0.096] | 0.118 |
| jev-1.13.0 tree_v2 vs jev-1.14.0 tree | +0.181 [+0.131, +0.231] | 1.44e-11 |
| jev-1.13.0 tree_v2 vs jev-1.14.0 tree_hard | +0.190 [+0.138, +0.242] | 1.29e-11 |
| jev-1.13.0 tree_v2 vs jev-1.14.0 tree_v2 | +0.009 [-0.013, +0.031] | 0.557 |
| jev-1.13.0 tree_v2 vs pplx-decider-v1.2 flat | -0.024 [-0.070, +0.024] | 0.355 |
| jev-1.13.0 tree_v2 vs pplx-decider-v1.2 tree | +0.070 [+0.015, +0.124] | 0.0159 |
| jev-1.13.0 tree_v2 vs pplx-decider-v1.2 tree_hard | +0.059 [+0.007, +0.109] | 0.0352 |
| jev-1.13.0 tree_v2 vs pplx-decider-v1.2 tree_v2 | -0.041 [-0.083, +0.002] | 0.0728 |
| jev-1.13.0 tree_v2 vs pplx-decider-flash-v1.2 flat | +0.028 [-0.022, +0.081] | 0.312 |
| jev-1.13.0 tree_v2 vs pplx-decider-flash-v1.2 tree | +0.170 [+0.116, +0.227] | 5.53e-09 |
| jev-1.13.0 tree_v2 vs pplx-decider-flash-v1.2 tree_hard | +0.157 [+0.103, +0.212] | 6.89e-08 |
| jev-1.13.0 tree_v2 vs pplx-decider-flash-v1.2 tree_v2 | +0.055 [+0.009, +0.100] | 0.0261 |
| jev-1.13.0 tree_v2 vs gpt-6-luna-decisions flat | -0.022 [-0.079, +0.033] | 0.48 |
| jev-1.13.0 tree_v2 vs gpt-6-luna-decisions tree | +0.214 [+0.155, +0.273] | 9.1e-12 |
| jev-1.13.0 tree_v2 vs gpt-6-luna-decisions tree_hard | +0.214 [+0.155, +0.273] | 9.1e-12 |
| jev-1.13.0 tree_v2 vs gpt-6-luna-decisions tree_v2 | +0.140 [+0.085, +0.194] | 1.02e-06 |
| jev-1.13.0 tree_v2 vs d1 flat | +0.022 [-0.033, +0.076] | 0.482 |
| jev-1.13.0 tree_v2 vs d1 tree | +0.194 [+0.140, +0.249] | 3.15e-11 |
| jev-1.13.0 tree_v2 vs d1 tree_hard | +0.168 [+0.114, +0.223] | 6.48e-09 |
| jev-1.13.0 tree_v2 vs d1 tree_v2 | +0.074 [+0.028, +0.122] | 0.00266 |
| jev-1.13.0 tree_v2 vs d1-ultra flat | -0.033 [-0.079, +0.015] | 0.21 |
| jev-1.13.0 tree_v2 vs d1-ultra tree | +0.135 [+0.081, +0.190] | 1.95e-06 |
| jev-1.13.0 tree_v2 vs d1-ultra tree_hard | +0.081 [+0.026, +0.135] | 0.0044 |
| jev-1.13.0 tree_v2 vs d1-ultra tree_v2 | +0.022 [-0.022, +0.068] | 0.391 |
| jev-1.13.0 tree_v2 vs microsoft-decision-1 flat | +0.055 [+0.000, +0.109] | 0.0598 |
| jev-1.13.0 tree_v2 vs microsoft-decision-1 tree | +0.223 [+0.168, +0.277] | 5.61e-14 |
| jev-1.13.0 tree_v2 vs microsoft-decision-1 tree_hard | +0.255 [+0.199, +0.310] | 4.83e-17 |
| jev-1.13.0 tree_v2 vs microsoft-decision-1 tree_v2 | +0.068 [+0.031, +0.105] | 0.000371 |
| jev-1.13.0 tree_v2 vs elephant-1 flat | -0.011 [-0.059, +0.039] | 0.733 |
| jev-1.13.0 tree_v2 vs elephant-1 tree | +0.166 [+0.111, +0.221] | 2.05e-08 |
| jev-1.13.0 tree_v2 vs elephant-1 tree_hard | +0.124 [+0.068, +0.181] | 2.45e-05 |
| jev-1.13.0 tree_v2 vs elephant-1 tree_v2 | +0.055 [+0.009, +0.100] | 0.0248 |
| jev-1.13.0 tree_v2 vs mammoth-1 flat | -0.017 [-0.066, +0.028] | 0.526 |
| jev-1.13.0 tree_v2 vs mammoth-1 tree | +0.155 [+0.103, +0.210] | 5.64e-08 |
| jev-1.13.0 tree_v2 vs mammoth-1 tree_hard | +0.116 [+0.063, +0.168] | 2.82e-05 |
| jev-1.13.0 tree_v2 vs mammoth-1 tree_v2 | +0.055 [+0.011, +0.100] | 0.0248 |
| jev-1.13.0 tree_v2 vs scaledown-classify-1 flat | +0.135 [+0.083, +0.188] | 7.53e-07 |
| jev-1.13.0 tree_v2 vs scaledown-classify-1 tree | +0.264 [+0.207, +0.321] | 3.72e-17 |
| jev-1.13.0 tree_v2 vs scaledown-classify-1 tree_hard | +0.303 [+0.245, +0.362] | 1.45e-20 |
| jev-1.13.0 tree_v2 vs scaledown-classify-1 tree_v2 | +0.242 [+0.188, +0.297] | 3.39e-16 |
| jev-1.13.0 tree_v2 vs gemini-2.5-flash paper_llm | +0.028 [-0.024, +0.081] | 0.332 |
| jev-1.13.0 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.055 [+0.002, +0.107] | 0.0459 |
| jev-1.13.0 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.055 [-0.103, -0.004] | 0.0356 |
| jev-1.13.0 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.031 [-0.081, +0.020] | 0.265 |
| jev-1.14.0 flat vs jev-1.14.0 tree | +0.138 [+0.081, +0.194] | 5.37e-06 |
| jev-1.14.0 flat vs jev-1.14.0 tree_hard | +0.146 [+0.092, +0.201] | 4.44e-07 |
| jev-1.14.0 flat vs jev-1.14.0 tree_v2 | -0.035 [-0.087, +0.015] | 0.214 |
| jev-1.14.0 flat vs pplx-decider-v1.2 flat | -0.068 [-0.109, -0.026] | 0.00215 |
| jev-1.14.0 flat vs pplx-decider-v1.2 tree | +0.026 [-0.026, +0.081] | 0.382 |
| jev-1.14.0 flat vs pplx-decider-v1.2 tree_hard | +0.015 [-0.033, +0.063] | 0.597 |
| jev-1.14.0 flat vs pplx-decider-v1.2 tree_v2 | -0.085 [-0.131, -0.039] | 0.000499 |
| jev-1.14.0 flat vs pplx-decider-flash-v1.2 flat | -0.015 [-0.061, +0.033] | 0.592 |
| jev-1.14.0 flat vs pplx-decider-flash-v1.2 tree | +0.127 [+0.066, +0.190] | 9.62e-05 |
| jev-1.14.0 flat vs pplx-decider-flash-v1.2 tree_hard | +0.114 [+0.057, +0.172] | 0.000198 |
| jev-1.14.0 flat vs pplx-decider-flash-v1.2 tree_v2 | +0.011 [-0.044, +0.068] | 0.76 |
| jev-1.14.0 flat vs gpt-6-luna-decisions flat | -0.066 [-0.114, -0.017] | 0.00893 |
| jev-1.14.0 flat vs gpt-6-luna-decisions tree | +0.170 [+0.105, +0.238] | 1.13e-06 |
| jev-1.14.0 flat vs gpt-6-luna-decisions tree_hard | +0.170 [+0.105, +0.238] | 1.13e-06 |
| jev-1.14.0 flat vs gpt-6-luna-decisions tree_v2 | +0.096 [+0.033, +0.162] | 0.0043 |
| jev-1.14.0 flat vs d1 flat | -0.022 [-0.066, +0.022] | 0.363 |
| jev-1.14.0 flat vs d1 tree | +0.151 [+0.087, +0.216] | 5.45e-06 |
| jev-1.14.0 flat vs d1 tree_hard | +0.124 [+0.066, +0.183] | 4.94e-05 |
| jev-1.14.0 flat vs d1 tree_v2 | +0.031 [-0.026, +0.087] | 0.327 |
| jev-1.14.0 flat vs d1-ultra flat | -0.076 [-0.120, -0.033] | 0.000923 |
| jev-1.14.0 flat vs d1-ultra tree | +0.092 [+0.033, +0.153] | 0.00436 |
| jev-1.14.0 flat vs d1-ultra tree_hard | +0.037 [-0.017, +0.092] | 0.207 |
| jev-1.14.0 flat vs d1-ultra tree_v2 | -0.022 [-0.079, +0.035] | 0.495 |
| jev-1.14.0 flat vs microsoft-decision-1 flat | +0.011 [-0.028, +0.050] | 0.668 |
| jev-1.14.0 flat vs microsoft-decision-1 tree | +0.179 [+0.122, +0.236] | 3.57e-09 |
| jev-1.14.0 flat vs microsoft-decision-1 tree_hard | +0.212 [+0.157, +0.266] | 8.94e-13 |
| jev-1.14.0 flat vs microsoft-decision-1 tree_v2 | +0.024 [-0.031, +0.076] | 0.431 |
| jev-1.14.0 flat vs elephant-1 flat | -0.055 [-0.103, -0.004] | 0.0356 |
| jev-1.14.0 flat vs elephant-1 tree | +0.122 [+0.059, +0.188] | 0.00027 |
| jev-1.14.0 flat vs elephant-1 tree_hard | +0.081 [+0.020, +0.142] | 0.0117 |
| jev-1.14.0 flat vs elephant-1 tree_v2 | +0.011 [-0.048, +0.072] | 0.775 |
| jev-1.14.0 flat vs mammoth-1 flat | -0.061 [-0.105, -0.017] | 0.00842 |
| jev-1.14.0 flat vs mammoth-1 tree | +0.111 [+0.050, +0.172] | 0.00058 |
| jev-1.14.0 flat vs mammoth-1 tree_hard | +0.072 [+0.017, +0.127] | 0.013 |
| jev-1.14.0 flat vs mammoth-1 tree_v2 | +0.011 [-0.046, +0.068] | 0.766 |
| jev-1.14.0 flat vs scaledown-classify-1 flat | +0.092 [+0.033, +0.151] | 0.0033 |
| jev-1.14.0 flat vs scaledown-classify-1 tree | +0.221 [+0.155, +0.288] | 5.04e-10 |
| jev-1.14.0 flat vs scaledown-classify-1 tree_hard | +0.260 [+0.201, +0.319] | 1.88e-16 |
| jev-1.14.0 flat vs scaledown-classify-1 tree_v2 | +0.199 [+0.133, +0.266] | 1.23e-08 |
| jev-1.14.0 flat vs gemini-2.5-flash paper_llm | -0.015 [-0.061, +0.031] | 0.576 |
| jev-1.14.0 flat vs gemini-2.5-flash paper_llm_thinking | +0.011 [-0.031, +0.052] | 0.679 |
| jev-1.14.0 flat vs gemini-3.8-flash paper_llm_low | -0.098 [-0.140, -0.057] | 5.46e-06 |
| jev-1.14.0 flat vs gemini-3.8-flash paper_llm_thinking | -0.074 [-0.116, -0.033] | 0.000675 |
| jev-1.14.0 tree vs jev-1.14.0 tree_hard | +0.009 [-0.013, +0.031] | 0.572 |
| jev-1.14.0 tree vs jev-1.14.0 tree_v2 | -0.172 [-0.221, -0.127] | 1.44e-11 |
| jev-1.14.0 tree vs pplx-decider-v1.2 flat | -0.205 [-0.260, -0.151] | 3.11e-12 |
| jev-1.14.0 tree vs pplx-decider-v1.2 tree | -0.111 [-0.153, -0.070] | 2.77e-07 |
| jev-1.14.0 tree vs pplx-decider-v1.2 tree_hard | -0.122 [-0.166, -0.079] | 1.11e-07 |
| jev-1.14.0 tree vs pplx-decider-v1.2 tree_v2 | -0.223 [-0.273, -0.172] | 4.79e-16 |
| jev-1.14.0 tree vs pplx-decider-flash-v1.2 flat | -0.153 [-0.205, -0.103] | 3.67e-08 |
| jev-1.14.0 tree vs pplx-decider-flash-v1.2 tree | -0.011 [-0.050, +0.028] | 0.672 |
| jev-1.14.0 tree vs pplx-decider-flash-v1.2 tree_hard | -0.024 [-0.063, +0.017] | 0.3 |
| jev-1.14.0 tree vs pplx-decider-flash-v1.2 tree_v2 | -0.127 [-0.177, -0.074] | 3.94e-06 |
| jev-1.14.0 tree vs gpt-6-luna-decisions flat | -0.203 [-0.253, -0.153] | 5.27e-14 |
| jev-1.14.0 tree vs gpt-6-luna-decisions tree | +0.033 [-0.011, +0.076] | 0.176 |
| jev-1.14.0 tree vs gpt-6-luna-decisions tree_hard | +0.033 [-0.011, +0.076] | 0.176 |
| jev-1.14.0 tree vs gpt-6-luna-decisions tree_v2 | -0.041 [-0.092, +0.011] | 0.14 |
| jev-1.14.0 tree vs d1 flat | -0.159 [-0.216, -0.103] | 2.13e-07 |
| jev-1.14.0 tree vs d1 tree | +0.013 [-0.026, +0.052] | 0.59 |
| jev-1.14.0 tree vs d1 tree_hard | -0.013 [-0.052, +0.026] | 0.594 |
| jev-1.14.0 tree vs d1 tree_v2 | -0.107 [-0.159, -0.055] | 0.000126 |
| jev-1.14.0 tree vs d1-ultra flat | -0.214 [-0.271, -0.157] | 1.16e-11 |
| jev-1.14.0 tree vs d1-ultra tree | -0.046 [-0.087, -0.004] | 0.0482 |
| jev-1.14.0 tree vs d1-ultra tree_hard | -0.100 [-0.144, -0.057] | 1.64e-05 |
| jev-1.14.0 tree vs d1-ultra tree_v2 | -0.159 [-0.214, -0.107] | 4.87e-08 |
| jev-1.14.0 tree vs microsoft-decision-1 flat | -0.127 [-0.188, -0.068] | 6.45e-05 |
| jev-1.14.0 tree vs microsoft-decision-1 tree | +0.041 [+0.011, +0.072] | 0.011 |
| jev-1.14.0 tree vs microsoft-decision-1 tree_hard | +0.074 [+0.041, +0.107] | 2.44e-05 |
| jev-1.14.0 tree vs microsoft-decision-1 tree_v2 | -0.114 [-0.170, -0.057] | 0.000142 |
| jev-1.14.0 tree vs elephant-1 flat | -0.192 [-0.245, -0.140] | 1.54e-11 |
| jev-1.14.0 tree vs elephant-1 tree | -0.015 [-0.055, +0.024] | 0.505 |
| jev-1.14.0 tree vs elephant-1 tree_hard | -0.057 [-0.096, -0.017] | 0.00734 |
| jev-1.14.0 tree vs elephant-1 tree_v2 | -0.127 [-0.179, -0.074] | 6.06e-06 |
| jev-1.14.0 tree vs mammoth-1 flat | -0.199 [-0.255, -0.142] | 1.64e-10 |
| jev-1.14.0 tree vs mammoth-1 tree | -0.026 [-0.072, +0.017] | 0.294 |
| jev-1.14.0 tree vs mammoth-1 tree_hard | -0.066 [-0.114, -0.017] | 0.0107 |
| jev-1.14.0 tree vs mammoth-1 tree_v2 | -0.127 [-0.181, -0.072] | 1.65e-05 |
| jev-1.14.0 tree vs scaledown-classify-1 flat | -0.046 [-0.100, +0.007] | 0.11 |
| jev-1.14.0 tree vs scaledown-classify-1 tree | +0.083 [+0.035, +0.131] | 0.00142 |
| jev-1.14.0 tree vs scaledown-classify-1 tree_hard | +0.122 [+0.074, +0.170] | 1.74e-06 |
| jev-1.14.0 tree vs scaledown-classify-1 tree_v2 | +0.061 [+0.009, +0.114] | 0.0314 |
| jev-1.14.0 tree vs gemini-2.5-flash paper_llm | -0.153 [-0.210, -0.094] | 8.33e-07 |
| jev-1.14.0 tree vs gemini-2.5-flash paper_llm_thinking | -0.127 [-0.188, -0.066] | 9.62e-05 |
| jev-1.14.0 tree vs gemini-3.8-flash paper_llm_low | -0.236 [-0.286, -0.186] | 9.36e-18 |
| jev-1.14.0 tree vs gemini-3.8-flash paper_llm_thinking | -0.212 [-0.264, -0.159] | 1.25e-13 |
| jev-1.14.0 tree_hard vs jev-1.14.0 tree_v2 | -0.181 [-0.229, -0.131] | 7.2e-12 |
| jev-1.14.0 tree_hard vs pplx-decider-v1.2 flat | -0.214 [-0.269, -0.159] | 1.07e-12 |
| jev-1.14.0 tree_hard vs pplx-decider-v1.2 tree | -0.120 [-0.164, -0.076] | 1.26e-07 |
| jev-1.14.0 tree_hard vs pplx-decider-v1.2 tree_hard | -0.131 [-0.175, -0.087] | 1.53e-08 |
| jev-1.14.0 tree_hard vs pplx-decider-v1.2 tree_v2 | -0.231 [-0.284, -0.179] | 1.77e-16 |
| jev-1.14.0 tree_hard vs pplx-decider-flash-v1.2 flat | -0.162 [-0.216, -0.107] | 1.93e-08 |
| jev-1.14.0 tree_hard vs pplx-decider-flash-v1.2 tree | -0.020 [-0.063, +0.024] | 0.448 |
| jev-1.14.0 tree_hard vs pplx-decider-flash-v1.2 tree_hard | -0.033 [-0.076, +0.011] | 0.176 |
| jev-1.14.0 tree_hard vs pplx-decider-flash-v1.2 tree_v2 | -0.135 [-0.190, -0.081] | 2.6e-06 |
| jev-1.14.0 tree_hard vs gpt-6-luna-decisions flat | -0.212 [-0.262, -0.162] | 8.13e-15 |
| jev-1.14.0 tree_hard vs gpt-6-luna-decisions tree | +0.024 [-0.024, +0.074] | 0.386 |
| jev-1.14.0 tree_hard vs gpt-6-luna-decisions tree_hard | +0.024 [-0.024, +0.074] | 0.386 |
| jev-1.14.0 tree_hard vs gpt-6-luna-decisions tree_v2 | -0.050 [-0.105, +0.004] | 0.0922 |
| jev-1.14.0 tree_hard vs d1 flat | -0.168 [-0.225, -0.111] | 4.17e-08 |
| jev-1.14.0 tree_hard vs d1 tree | +0.004 [-0.039, +0.050] | 0.925 |
| jev-1.14.0 tree_hard vs d1 tree_hard | -0.022 [-0.063, +0.020] | 0.373 |
| jev-1.14.0 tree_hard vs d1 tree_v2 | -0.116 [-0.170, -0.061] | 7.53e-05 |
| jev-1.14.0 tree_hard vs d1-ultra flat | -0.223 [-0.282, -0.164] | 3.15e-12 |
| jev-1.14.0 tree_hard vs d1-ultra tree | -0.055 [-0.100, -0.009] | 0.0314 |
| jev-1.14.0 tree_hard vs d1-ultra tree_hard | -0.109 [-0.155, -0.063] | 9.85e-06 |
| jev-1.14.0 tree_hard vs d1-ultra tree_v2 | -0.168 [-0.225, -0.111] | 4.17e-08 |
| jev-1.14.0 tree_hard vs microsoft-decision-1 flat | -0.135 [-0.192, -0.081] | 7.21e-06 |
| jev-1.14.0 tree_hard vs microsoft-decision-1 tree | +0.033 [-0.002, +0.068] | 0.0769 |
| jev-1.14.0 tree_hard vs microsoft-decision-1 tree_hard | +0.066 [+0.033, +0.098] | 0.000227 |
| jev-1.14.0 tree_hard vs microsoft-decision-1 tree_v2 | -0.122 [-0.179, -0.066] | 4.88e-05 |
| jev-1.14.0 tree_hard vs elephant-1 flat | -0.201 [-0.255, -0.146] | 1.24e-11 |
| jev-1.14.0 tree_hard vs elephant-1 tree | -0.024 [-0.068, +0.020] | 0.334 |
| jev-1.14.0 tree_hard vs elephant-1 tree_hard | -0.066 [-0.109, -0.022] | 0.00423 |
| jev-1.14.0 tree_hard vs elephant-1 tree_v2 | -0.135 [-0.192, -0.079] | 6.41e-06 |
| jev-1.14.0 tree_hard vs mammoth-1 flat | -0.207 [-0.266, -0.151] | 7.12e-11 |
| jev-1.14.0 tree_hard vs mammoth-1 tree | -0.035 [-0.083, +0.015] | 0.195 |
| jev-1.14.0 tree_hard vs mammoth-1 tree_hard | -0.074 [-0.124, -0.024] | 0.00648 |
| jev-1.14.0 tree_hard vs mammoth-1 tree_v2 | -0.135 [-0.192, -0.079] | 9.05e-06 |
| jev-1.14.0 tree_hard vs scaledown-classify-1 flat | -0.055 [-0.109, -0.002] | 0.0598 |
| jev-1.14.0 tree_hard vs scaledown-classify-1 tree | +0.074 [+0.022, +0.129] | 0.00976 |
| jev-1.14.0 tree_hard vs scaledown-classify-1 tree_hard | +0.114 [+0.066, +0.164] | 1.13e-05 |
| jev-1.14.0 tree_hard vs scaledown-classify-1 tree_v2 | +0.052 [-0.004, +0.109] | 0.0914 |
| jev-1.14.0 tree_hard vs gemini-2.5-flash paper_llm | -0.162 [-0.218, -0.105] | 1.13e-07 |
| jev-1.14.0 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.135 [-0.194, -0.076] | 1.53e-05 |
| jev-1.14.0 tree_hard vs gemini-3.8-flash paper_llm_low | -0.245 [-0.297, -0.192] | 3.62e-18 |
| jev-1.14.0 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.221 [-0.273, -0.168] | 1.46e-14 |
| jev-1.14.0 tree_v2 vs pplx-decider-v1.2 flat | -0.033 [-0.079, +0.015] | 0.203 |
| jev-1.14.0 tree_v2 vs pplx-decider-v1.2 tree | +0.061 [+0.007, +0.116] | 0.0369 |
| jev-1.14.0 tree_v2 vs pplx-decider-v1.2 tree_hard | +0.050 [-0.002, +0.103] | 0.075 |
| jev-1.14.0 tree_v2 vs pplx-decider-v1.2 tree_v2 | -0.050 [-0.092, -0.009] | 0.0281 |
| jev-1.14.0 tree_v2 vs pplx-decider-flash-v1.2 flat | +0.020 [-0.033, +0.072] | 0.512 |
| jev-1.14.0 tree_v2 vs pplx-decider-flash-v1.2 tree | +0.162 [+0.105, +0.218] | 9.66e-08 |
| jev-1.14.0 tree_v2 vs pplx-decider-flash-v1.2 tree_hard | +0.148 [+0.094, +0.205] | 7.87e-07 |
| jev-1.14.0 tree_v2 vs pplx-decider-flash-v1.2 tree_v2 | +0.046 [-0.002, +0.094] | 0.0778 |
| jev-1.14.0 tree_v2 vs gpt-6-luna-decisions flat | -0.031 [-0.085, +0.024] | 0.301 |
| jev-1.14.0 tree_v2 vs gpt-6-luna-decisions tree | +0.205 [+0.146, +0.266] | 1.57e-10 |
| jev-1.14.0 tree_v2 vs gpt-6-luna-decisions tree_hard | +0.205 [+0.146, +0.266] | 1.57e-10 |
| jev-1.14.0 tree_v2 vs gpt-6-luna-decisions tree_v2 | +0.131 [+0.076, +0.188] | 8.11e-06 |
| jev-1.14.0 tree_v2 vs d1 flat | +0.013 [-0.041, +0.068] | 0.696 |
| jev-1.14.0 tree_v2 vs d1 tree | +0.186 [+0.129, +0.242] | 7.93e-10 |
| jev-1.14.0 tree_v2 vs d1 tree_hard | +0.159 [+0.103, +0.214] | 5.83e-08 |
| jev-1.14.0 tree_v2 vs d1 tree_v2 | +0.066 [+0.020, +0.114] | 0.0101 |
| jev-1.14.0 tree_v2 vs d1-ultra flat | -0.041 [-0.090, +0.007] | 0.11 |
| jev-1.14.0 tree_v2 vs d1-ultra tree | +0.127 [+0.072, +0.181] | 1.31e-05 |
| jev-1.14.0 tree_v2 vs d1-ultra tree_hard | +0.072 [+0.017, +0.127] | 0.0125 |
| jev-1.14.0 tree_v2 vs d1-ultra tree_v2 | +0.013 [-0.033, +0.059] | 0.643 |
| jev-1.14.0 tree_v2 vs microsoft-decision-1 flat | +0.046 [-0.007, +0.098] | 0.11 |
| jev-1.14.0 tree_v2 vs microsoft-decision-1 tree | +0.214 [+0.157, +0.269] | 4.31e-13 |
| jev-1.14.0 tree_v2 vs microsoft-decision-1 tree_hard | +0.247 [+0.190, +0.301] | 2.02e-16 |
| jev-1.14.0 tree_v2 vs microsoft-decision-1 tree_v2 | +0.059 [+0.022, +0.096] | 0.00244 |
| jev-1.14.0 tree_v2 vs elephant-1 flat | -0.020 [-0.072, +0.033] | 0.512 |
| jev-1.14.0 tree_v2 vs elephant-1 tree | +0.157 [+0.100, +0.214] | 2.18e-07 |
| jev-1.14.0 tree_v2 vs elephant-1 tree_hard | +0.116 [+0.059, +0.170] | 0.000109 |
| jev-1.14.0 tree_v2 vs elephant-1 tree_v2 | +0.046 [-0.002, +0.094] | 0.0732 |
| jev-1.14.0 tree_v2 vs mammoth-1 flat | -0.026 [-0.074, +0.022] | 0.338 |
| jev-1.14.0 tree_v2 vs mammoth-1 tree | +0.146 [+0.092, +0.203] | 5.19e-07 |
| jev-1.14.0 tree_v2 vs mammoth-1 tree_hard | +0.107 [+0.055, +0.162] | 0.000139 |
| jev-1.14.0 tree_v2 vs mammoth-1 tree_v2 | +0.046 [+0.002, +0.092] | 0.0663 |
| jev-1.14.0 tree_v2 vs scaledown-classify-1 flat | +0.127 [+0.074, +0.179] | 3.94e-06 |
| jev-1.14.0 tree_v2 vs scaledown-classify-1 tree | +0.255 [+0.197, +0.314] | 1.72e-15 |
| jev-1.14.0 tree_v2 vs scaledown-classify-1 tree_hard | +0.295 [+0.236, +0.354] | 6.13e-20 |
| jev-1.14.0 tree_v2 vs scaledown-classify-1 tree_v2 | +0.234 [+0.177, +0.290] | 2.44e-14 |
| jev-1.14.0 tree_v2 vs gemini-2.5-flash paper_llm | +0.020 [-0.033, +0.072] | 0.521 |
| jev-1.14.0 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.046 [-0.004, +0.098] | 0.0964 |
| jev-1.14.0 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.063 [-0.111, -0.015] | 0.0134 |
| jev-1.14.0 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.039 [-0.090, +0.011] | 0.145 |
| pplx-decider-v1.2 flat vs pplx-decider-v1.2 tree | +0.094 [+0.050, +0.140] | 5.49e-05 |
| pplx-decider-v1.2 flat vs pplx-decider-v1.2 tree_hard | +0.083 [+0.041, +0.125] | 0.000183 |
| pplx-decider-v1.2 flat vs pplx-decider-v1.2 tree_v2 | -0.017 [-0.048, +0.013] | 0.332 |
| pplx-decider-v1.2 flat vs pplx-decider-flash-v1.2 flat | +0.052 [+0.011, +0.094] | 0.0184 |
| pplx-decider-v1.2 flat vs pplx-decider-flash-v1.2 tree | +0.194 [+0.142, +0.247] | 4.04e-12 |
| pplx-decider-v1.2 flat vs pplx-decider-flash-v1.2 tree_hard | +0.181 [+0.133, +0.229] | 3.46e-12 |
| pplx-decider-v1.2 flat vs pplx-decider-flash-v1.2 tree_v2 | +0.079 [+0.035, +0.122] | 0.000769 |
| pplx-decider-v1.2 flat vs gpt-6-luna-decisions flat | +0.002 [-0.046, +0.050] | 1 |
| pplx-decider-v1.2 flat vs gpt-6-luna-decisions tree | +0.238 [+0.183, +0.295] | 7.43e-15 |
| pplx-decider-v1.2 flat vs gpt-6-luna-decisions tree_hard | +0.238 [+0.183, +0.295] | 7.43e-15 |
| pplx-decider-v1.2 flat vs gpt-6-luna-decisions tree_v2 | +0.164 [+0.111, +0.218] | 5.74e-09 |
| pplx-decider-v1.2 flat vs d1 flat | +0.046 [+0.007, +0.085] | 0.0295 |
| pplx-decider-v1.2 flat vs d1 tree | +0.218 [+0.166, +0.273] | 3.32e-14 |
| pplx-decider-v1.2 flat vs d1 tree_hard | +0.192 [+0.142, +0.245] | 1.12e-12 |
| pplx-decider-v1.2 flat vs d1 tree_v2 | +0.098 [+0.052, +0.144] | 3.87e-05 |
| pplx-decider-v1.2 flat vs d1-ultra flat | -0.009 [-0.044, +0.026] | 0.712 |
| pplx-decider-v1.2 flat vs d1-ultra tree | +0.159 [+0.107, +0.212] | 1.21e-08 |
| pplx-decider-v1.2 flat vs d1-ultra tree_hard | +0.105 [+0.061, +0.151] | 1.39e-05 |
| pplx-decider-v1.2 flat vs d1-ultra tree_v2 | +0.046 [+0.000, +0.092] | 0.0663 |
| pplx-decider-v1.2 flat vs microsoft-decision-1 flat | +0.079 [+0.028, +0.127] | 0.00202 |
| pplx-decider-v1.2 flat vs microsoft-decision-1 tree | +0.247 [+0.190, +0.303] | 1.3e-15 |
| pplx-decider-v1.2 flat vs microsoft-decision-1 tree_hard | +0.279 [+0.223, +0.336] | 2.91e-19 |
| pplx-decider-v1.2 flat vs microsoft-decision-1 tree_v2 | +0.092 [+0.039, +0.142] | 0.00076 |
| pplx-decider-v1.2 flat vs elephant-1 flat | +0.013 [-0.024, +0.050] | 0.567 |
| pplx-decider-v1.2 flat vs elephant-1 tree | +0.190 [+0.135, +0.245] | 9.07e-11 |
| pplx-decider-v1.2 flat vs elephant-1 tree_hard | +0.148 [+0.096, +0.201] | 1.12e-07 |
| pplx-decider-v1.2 flat vs elephant-1 tree_v2 | +0.079 [+0.033, +0.127] | 0.00186 |
| pplx-decider-v1.2 flat vs mammoth-1 flat | +0.007 [-0.026, +0.039] | 0.788 |
| pplx-decider-v1.2 flat vs mammoth-1 tree | +0.179 [+0.129, +0.231] | 1.03e-10 |
| pplx-decider-v1.2 flat vs mammoth-1 tree_hard | +0.140 [+0.094, +0.186] | 3.77e-09 |
| pplx-decider-v1.2 flat vs mammoth-1 tree_v2 | +0.079 [+0.035, +0.124] | 0.00107 |
| pplx-decider-v1.2 flat vs scaledown-classify-1 flat | +0.159 [+0.107, +0.212] | 1.5e-08 |
| pplx-decider-v1.2 flat vs scaledown-classify-1 tree | +0.288 [+0.231, +0.345] | 1.06e-19 |
| pplx-decider-v1.2 flat vs scaledown-classify-1 tree_hard | +0.328 [+0.271, +0.384] | 4.2e-24 |
| pplx-decider-v1.2 flat vs scaledown-classify-1 tree_v2 | +0.266 [+0.212, +0.323] | 4.81e-18 |
| pplx-decider-v1.2 flat vs gemini-2.5-flash paper_llm | +0.052 [+0.004, +0.100] | 0.0384 |
| pplx-decider-v1.2 flat vs gemini-2.5-flash paper_llm_thinking | +0.079 [+0.031, +0.129] | 0.00256 |
| pplx-decider-v1.2 flat vs gemini-3.8-flash paper_llm_low | -0.031 [-0.068, +0.007] | 0.125 |
| pplx-decider-v1.2 flat vs gemini-3.8-flash paper_llm_thinking | -0.007 [-0.044, +0.031] | 0.815 |
| pplx-decider-v1.2 tree vs pplx-decider-v1.2 tree_hard | -0.011 [-0.037, +0.015] | 0.522 |
| pplx-decider-v1.2 tree vs pplx-decider-v1.2 tree_v2 | -0.111 [-0.148, -0.076] | 3.02e-09 |
| pplx-decider-v1.2 tree vs pplx-decider-flash-v1.2 flat | -0.041 [-0.092, +0.009] | 0.135 |
| pplx-decider-v1.2 tree vs pplx-decider-flash-v1.2 tree | +0.100 [+0.059, +0.142] | 3.69e-06 |
| pplx-decider-v1.2 tree vs pplx-decider-flash-v1.2 tree_hard | +0.087 [+0.050, +0.124] | 1.13e-05 |
| pplx-decider-v1.2 tree vs pplx-decider-flash-v1.2 tree_v2 | -0.015 [-0.061, +0.033] | 0.592 |
| pplx-decider-v1.2 tree vs gpt-6-luna-decisions flat | -0.092 [-0.142, -0.041] | 0.000534 |
| pplx-decider-v1.2 tree vs gpt-6-luna-decisions tree | +0.144 [+0.098, +0.190] | 4.16e-09 |
| pplx-decider-v1.2 tree vs gpt-6-luna-decisions tree_hard | +0.144 [+0.098, +0.190] | 4.16e-09 |
| pplx-decider-v1.2 tree vs gpt-6-luna-decisions tree_v2 | +0.070 [+0.020, +0.120] | 0.0101 |
| pplx-decider-v1.2 tree vs d1 flat | -0.048 [-0.098, +0.000] | 0.0714 |
| pplx-decider-v1.2 tree vs d1 tree | +0.124 [+0.083, +0.166] | 1.01e-08 |
| pplx-decider-v1.2 tree vs d1 tree_hard | +0.098 [+0.061, +0.138] | 1.41e-06 |
| pplx-decider-v1.2 tree vs d1 tree_v2 | +0.004 [-0.044, +0.052] | 0.931 |
| pplx-decider-v1.2 tree vs d1-ultra flat | -0.103 [-0.155, -0.052] | 0.00018 |
| pplx-decider-v1.2 tree vs d1-ultra tree | +0.066 [+0.026, +0.107] | 0.00259 |
| pplx-decider-v1.2 tree vs d1-ultra tree_hard | +0.011 [-0.028, +0.050] | 0.657 |
| pplx-decider-v1.2 tree vs d1-ultra tree_v2 | -0.048 [-0.098, +0.002] | 0.0777 |
| pplx-decider-v1.2 tree vs microsoft-decision-1 flat | -0.015 [-0.074, +0.041] | 0.657 |
| pplx-decider-v1.2 tree vs microsoft-decision-1 tree | +0.153 [+0.109, +0.197] | 5.56e-11 |
| pplx-decider-v1.2 tree vs microsoft-decision-1 tree_hard | +0.186 [+0.140, +0.231] | 3.89e-14 |
| pplx-decider-v1.2 tree vs microsoft-decision-1 tree_v2 | -0.002 [-0.061, +0.057] | 1 |
| pplx-decider-v1.2 tree vs elephant-1 flat | -0.081 [-0.127, -0.035] | 0.00108 |
| pplx-decider-v1.2 tree vs elephant-1 tree | +0.096 [+0.055, +0.138] | 1.26e-05 |
| pplx-decider-v1.2 tree vs elephant-1 tree_hard | +0.055 [+0.015, +0.094] | 0.00884 |
| pplx-decider-v1.2 tree vs elephant-1 tree_v2 | -0.015 [-0.066, +0.035] | 0.618 |
| pplx-decider-v1.2 tree vs mammoth-1 flat | -0.087 [-0.135, -0.039] | 0.000763 |
| pplx-decider-v1.2 tree vs mammoth-1 tree | +0.085 [+0.044, +0.127] | 0.000111 |
| pplx-decider-v1.2 tree vs mammoth-1 tree_hard | +0.046 [+0.007, +0.085] | 0.0334 |
| pplx-decider-v1.2 tree vs mammoth-1 tree_v2 | -0.015 [-0.063, +0.033] | 0.6 |
| pplx-decider-v1.2 tree vs scaledown-classify-1 flat | +0.066 [+0.011, +0.120] | 0.025 |
| pplx-decider-v1.2 tree vs scaledown-classify-1 tree | +0.194 [+0.144, +0.245] | 2.23e-13 |
| pplx-decider-v1.2 tree vs scaledown-classify-1 tree_hard | +0.234 [+0.179, +0.288] | 1.42e-15 |
| pplx-decider-v1.2 tree vs scaledown-classify-1 tree_v2 | +0.172 [+0.120, +0.225] | 7.65e-10 |
| pplx-decider-v1.2 tree vs gemini-2.5-flash paper_llm | -0.041 [-0.096, +0.015] | 0.173 |
| pplx-decider-v1.2 tree vs gemini-2.5-flash paper_llm_thinking | -0.015 [-0.076, +0.044] | 0.674 |
| pplx-decider-v1.2 tree vs gemini-3.8-flash paper_llm_low | -0.124 [-0.170, -0.081] | 1.28e-07 |
| pplx-decider-v1.2 tree vs gemini-3.8-flash paper_llm_thinking | -0.100 [-0.148, -0.055] | 5.88e-05 |
| pplx-decider-v1.2 tree_hard vs pplx-decider-v1.2 tree_v2 | -0.100 [-0.135, -0.066] | 6.22e-08 |
| pplx-decider-v1.2 tree_hard vs pplx-decider-flash-v1.2 flat | -0.031 [-0.079, +0.017] | 0.247 |
| pplx-decider-v1.2 tree_hard vs pplx-decider-flash-v1.2 tree | +0.111 [+0.063, +0.159] | 6.97e-06 |
| pplx-decider-v1.2 tree_hard vs pplx-decider-flash-v1.2 tree_hard | +0.098 [+0.057, +0.140] | 5.46e-06 |
| pplx-decider-v1.2 tree_hard vs pplx-decider-flash-v1.2 tree_v2 | -0.004 [-0.052, +0.046] | 0.931 |
| pplx-decider-v1.2 tree_hard vs gpt-6-luna-decisions flat | -0.081 [-0.129, -0.033] | 0.00108 |
| pplx-decider-v1.2 tree_hard vs gpt-6-luna-decisions tree | +0.155 [+0.103, +0.207] | 3.13e-08 |
| pplx-decider-v1.2 tree_hard vs gpt-6-luna-decisions tree_hard | +0.155 [+0.103, +0.207] | 3.13e-08 |
| pplx-decider-v1.2 tree_hard vs gpt-6-luna-decisions tree_v2 | +0.081 [+0.028, +0.135] | 0.00466 |
| pplx-decider-v1.2 tree_hard vs d1 flat | -0.037 [-0.085, +0.011] | 0.149 |
| pplx-decider-v1.2 tree_hard vs d1 tree | +0.135 [+0.087, +0.186] | 1.29e-07 |
| pplx-decider-v1.2 tree_hard vs d1 tree_hard | +0.109 [+0.066, +0.153] | 1.25e-06 |
| pplx-decider-v1.2 tree_hard vs d1 tree_v2 | +0.015 [-0.035, +0.066] | 0.614 |
| pplx-decider-v1.2 tree_hard vs d1-ultra flat | -0.092 [-0.140, -0.044] | 0.000399 |
| pplx-decider-v1.2 tree_hard vs d1-ultra tree | +0.076 [+0.031, +0.122] | 0.00187 |
| pplx-decider-v1.2 tree_hard vs d1-ultra tree_hard | +0.022 [-0.015, +0.061] | 0.308 |
| pplx-decider-v1.2 tree_hard vs d1-ultra tree_v2 | -0.037 [-0.087, +0.015] | 0.193 |
| pplx-decider-v1.2 tree_hard vs microsoft-decision-1 flat | -0.004 [-0.057, +0.048] | 0.936 |
| pplx-decider-v1.2 tree_hard vs microsoft-decision-1 tree | +0.164 [+0.118, +0.210] | 8.09e-12 |
| pplx-decider-v1.2 tree_hard vs microsoft-decision-1 tree_hard | +0.197 [+0.151, +0.242] | 1.02e-15 |
| pplx-decider-v1.2 tree_hard vs microsoft-decision-1 tree_v2 | +0.009 [-0.048, +0.066] | 0.819 |
| pplx-decider-v1.2 tree_hard vs elephant-1 flat | -0.070 [-0.114, -0.026] | 0.0035 |
| pplx-decider-v1.2 tree_hard vs elephant-1 tree | +0.107 [+0.059, +0.157] | 3.44e-05 |
| pplx-decider-v1.2 tree_hard vs elephant-1 tree_hard | +0.066 [+0.022, +0.109] | 0.00502 |
| pplx-decider-v1.2 tree_hard vs elephant-1 tree_v2 | -0.004 [-0.057, +0.050] | 0.936 |
| pplx-decider-v1.2 tree_hard vs mammoth-1 flat | -0.076 [-0.124, -0.031] | 0.00223 |
| pplx-decider-v1.2 tree_hard vs mammoth-1 tree | +0.096 [+0.050, +0.144] | 9.65e-05 |
| pplx-decider-v1.2 tree_hard vs mammoth-1 tree_hard | +0.057 [+0.017, +0.098] | 0.00878 |
| pplx-decider-v1.2 tree_hard vs mammoth-1 tree_v2 | -0.004 [-0.055, +0.046] | 0.933 |
| pplx-decider-v1.2 tree_hard vs scaledown-classify-1 flat | +0.076 [+0.022, +0.131] | 0.00872 |
| pplx-decider-v1.2 tree_hard vs scaledown-classify-1 tree | +0.205 [+0.151, +0.260] | 4.16e-12 |
| pplx-decider-v1.2 tree_hard vs scaledown-classify-1 tree_hard | +0.245 [+0.190, +0.299] | 1.43e-16 |
| pplx-decider-v1.2 tree_hard vs scaledown-classify-1 tree_v2 | +0.183 [+0.127, +0.240] | 1.74e-09 |
| pplx-decider-v1.2 tree_hard vs gemini-2.5-flash paper_llm | -0.031 [-0.083, +0.024] | 0.304 |
| pplx-decider-v1.2 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.004 [-0.059, +0.050] | 0.939 |
| pplx-decider-v1.2 tree_hard vs gemini-3.8-flash paper_llm_low | -0.114 [-0.157, -0.072] | 2.45e-07 |
| pplx-decider-v1.2 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.090 [-0.133, -0.046] | 0.000125 |
| pplx-decider-v1.2 tree_v2 vs pplx-decider-flash-v1.2 flat | +0.070 [+0.024, +0.114] | 0.00322 |
| pplx-decider-v1.2 tree_v2 vs pplx-decider-flash-v1.2 tree | +0.212 [+0.162, +0.262] | 1.24e-14 |
| pplx-decider-v1.2 tree_v2 vs pplx-decider-flash-v1.2 tree_hard | +0.199 [+0.151, +0.247] | 1.48e-14 |
| pplx-decider-v1.2 tree_v2 vs pplx-decider-flash-v1.2 tree_v2 | +0.096 [+0.055, +0.138] | 1.89e-05 |
| pplx-decider-v1.2 tree_v2 vs gpt-6-luna-decisions flat | +0.020 [-0.028, +0.068] | 0.474 |
| pplx-decider-v1.2 tree_v2 vs gpt-6-luna-decisions tree | +0.255 [+0.201, +0.310] | 8.98e-18 |
| pplx-decider-v1.2 tree_v2 vs gpt-6-luna-decisions tree_hard | +0.255 [+0.201, +0.310] | 8.98e-18 |
| pplx-decider-v1.2 tree_v2 vs gpt-6-luna-decisions tree_v2 | +0.181 [+0.131, +0.231] | 2e-11 |
| pplx-decider-v1.2 tree_v2 vs d1 flat | +0.063 [+0.020, +0.105] | 0.00508 |
| pplx-decider-v1.2 tree_v2 vs d1 tree | +0.236 [+0.186, +0.286] | 9.36e-18 |
| pplx-decider-v1.2 tree_v2 vs d1 tree_hard | +0.210 [+0.162, +0.258] | 4.55e-16 |
| pplx-decider-v1.2 tree_v2 vs d1 tree_v2 | +0.116 [+0.074, +0.159] | 3.78e-07 |
| pplx-decider-v1.2 tree_v2 vs d1-ultra flat | +0.009 [-0.033, +0.050] | 0.76 |
| pplx-decider-v1.2 tree_v2 vs d1-ultra tree | +0.177 [+0.129, +0.225] | 1.22e-11 |
| pplx-decider-v1.2 tree_v2 vs d1-ultra tree_hard | +0.122 [+0.076, +0.166] | 1.92e-07 |
| pplx-decider-v1.2 tree_v2 vs d1-ultra tree_v2 | +0.063 [+0.022, +0.105] | 0.00464 |
| pplx-decider-v1.2 tree_v2 vs microsoft-decision-1 flat | +0.096 [+0.044, +0.146] | 0.000278 |
| pplx-decider-v1.2 tree_v2 vs microsoft-decision-1 tree | +0.264 [+0.210, +0.317] | 4.01e-20 |
| pplx-decider-v1.2 tree_v2 vs microsoft-decision-1 tree_hard | +0.297 [+0.245, +0.349] | 5.15e-24 |
| pplx-decider-v1.2 tree_v2 vs microsoft-decision-1 tree_v2 | +0.109 [+0.061, +0.155] | 1.17e-05 |
| pplx-decider-v1.2 tree_v2 vs elephant-1 flat | +0.031 [-0.009, +0.070] | 0.165 |
| pplx-decider-v1.2 tree_v2 vs elephant-1 tree | +0.207 [+0.155, +0.260] | 6.98e-14 |
| pplx-decider-v1.2 tree_v2 vs elephant-1 tree_hard | +0.166 [+0.118, +0.214] | 1.52e-10 |
| pplx-decider-v1.2 tree_v2 vs elephant-1 tree_v2 | +0.096 [+0.052, +0.140] | 3.3e-05 |
| pplx-decider-v1.2 tree_v2 vs mammoth-1 flat | +0.024 [-0.015, +0.063] | 0.278 |
| pplx-decider-v1.2 tree_v2 vs mammoth-1 tree | +0.197 [+0.148, +0.247] | 3.82e-14 |
| pplx-decider-v1.2 tree_v2 vs mammoth-1 tree_hard | +0.157 [+0.116, +0.201] | 1.87e-12 |
| pplx-decider-v1.2 tree_v2 vs mammoth-1 tree_v2 | +0.096 [+0.057, +0.138] | 1.01e-05 |
| pplx-decider-v1.2 tree_v2 vs scaledown-classify-1 flat | +0.177 [+0.124, +0.227] | 1.16e-10 |
| pplx-decider-v1.2 tree_v2 vs scaledown-classify-1 tree | +0.306 [+0.249, +0.362] | 2.45e-23 |
| pplx-decider-v1.2 tree_v2 vs scaledown-classify-1 tree_hard | +0.345 [+0.288, +0.400] | 1.18e-27 |
| pplx-decider-v1.2 tree_v2 vs scaledown-classify-1 tree_v2 | +0.284 [+0.229, +0.338] | 2.21e-21 |
| pplx-decider-v1.2 tree_v2 vs gemini-2.5-flash paper_llm | +0.070 [+0.022, +0.118] | 0.00675 |
| pplx-decider-v1.2 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.096 [+0.046, +0.146] | 0.000373 |
| pplx-decider-v1.2 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.013 [-0.050, +0.024] | 0.567 |
| pplx-decider-v1.2 tree_v2 vs gemini-3.8-flash paper_llm_thinking | +0.011 [-0.028, +0.050] | 0.661 |
| pplx-decider-flash-v1.2 flat vs pplx-decider-flash-v1.2 tree | +0.142 [+0.092, +0.192] | 8.09e-08 |
| pplx-decider-flash-v1.2 flat vs pplx-decider-flash-v1.2 tree_hard | +0.129 [+0.081, +0.177] | 3.19e-07 |
| pplx-decider-flash-v1.2 flat vs pplx-decider-flash-v1.2 tree_v2 | +0.026 [-0.015, +0.070] | 0.271 |
| pplx-decider-flash-v1.2 flat vs gpt-6-luna-decisions flat | -0.050 [-0.096, -0.004] | 0.0415 |
| pplx-decider-flash-v1.2 flat vs gpt-6-luna-decisions tree | +0.186 [+0.131, +0.240] | 9.18e-11 |
| pplx-decider-flash-v1.2 flat vs gpt-6-luna-decisions tree_hard | +0.186 [+0.131, +0.240] | 9.18e-11 |
| pplx-decider-flash-v1.2 flat vs gpt-6-luna-decisions tree_v2 | +0.111 [+0.061, +0.164] | 4.55e-05 |
| pplx-decider-flash-v1.2 flat vs d1 flat | -0.007 [-0.048, +0.033] | 0.832 |
| pplx-decider-flash-v1.2 flat vs d1 tree | +0.166 [+0.114, +0.218] | 3.12e-09 |
| pplx-decider-flash-v1.2 flat vs d1 tree_hard | +0.140 [+0.087, +0.192] | 2.62e-07 |
| pplx-decider-flash-v1.2 flat vs d1 tree_v2 | +0.046 [+0.000, +0.094] | 0.0686 |
| pplx-decider-flash-v1.2 flat vs d1-ultra flat | -0.061 [-0.103, -0.017] | 0.00664 |
| pplx-decider-flash-v1.2 flat vs d1-ultra tree | +0.107 [+0.059, +0.157] | 5.1e-05 |
| pplx-decider-flash-v1.2 flat vs d1-ultra tree_hard | +0.052 [+0.007, +0.098] | 0.0308 |
| pplx-decider-flash-v1.2 flat vs d1-ultra tree_v2 | -0.007 [-0.052, +0.039] | 0.855 |
| pplx-decider-flash-v1.2 flat vs microsoft-decision-1 flat | +0.026 [-0.024, +0.074] | 0.338 |
| pplx-decider-flash-v1.2 flat vs microsoft-decision-1 tree | +0.194 [+0.142, +0.247] | 4.04e-12 |
| pplx-decider-flash-v1.2 flat vs microsoft-decision-1 tree_hard | +0.227 [+0.175, +0.279] | 2.52e-15 |
| pplx-decider-flash-v1.2 flat vs microsoft-decision-1 tree_v2 | +0.039 [-0.013, +0.092] | 0.171 |
| pplx-decider-flash-v1.2 flat vs elephant-1 flat | -0.039 [-0.074, -0.004] | 0.0385 |
| pplx-decider-flash-v1.2 flat vs elephant-1 tree | +0.138 [+0.085, +0.192] | 1.04e-06 |
| pplx-decider-flash-v1.2 flat vs elephant-1 tree_hard | +0.096 [+0.044, +0.148] | 0.00058 |
| pplx-decider-flash-v1.2 flat vs elephant-1 tree_v2 | +0.026 [-0.022, +0.074] | 0.315 |
| pplx-decider-flash-v1.2 flat vs mammoth-1 flat | -0.046 [-0.087, -0.007] | 0.0354 |
| pplx-decider-flash-v1.2 flat vs mammoth-1 tree | +0.127 [+0.076, +0.179] | 2.9e-06 |
| pplx-decider-flash-v1.2 flat vs mammoth-1 tree_hard | +0.087 [+0.039, +0.135] | 0.000464 |
| pplx-decider-flash-v1.2 flat vs mammoth-1 tree_v2 | +0.026 [-0.022, +0.074] | 0.327 |
| pplx-decider-flash-v1.2 flat vs scaledown-classify-1 flat | +0.107 [+0.052, +0.162] | 0.000153 |
| pplx-decider-flash-v1.2 flat vs scaledown-classify-1 tree | +0.236 [+0.181, +0.293] | 5.78e-15 |
| pplx-decider-flash-v1.2 flat vs scaledown-classify-1 tree_hard | +0.275 [+0.221, +0.330] | 2.76e-20 |
| pplx-decider-flash-v1.2 flat vs scaledown-classify-1 tree_v2 | +0.214 [+0.159, +0.271] | 2.26e-13 |
| pplx-decider-flash-v1.2 flat vs gemini-2.5-flash paper_llm | +0.000 [-0.048, +0.050] | 1 |
| pplx-decider-flash-v1.2 flat vs gemini-2.5-flash paper_llm_thinking | +0.026 [-0.026, +0.079] | 0.369 |
| pplx-decider-flash-v1.2 flat vs gemini-3.8-flash paper_llm_low | -0.083 [-0.127, -0.041] | 0.000183 |
| pplx-decider-flash-v1.2 flat vs gemini-3.8-flash paper_llm_thinking | -0.059 [-0.103, -0.015] | 0.0108 |
| pplx-decider-flash-v1.2 tree vs pplx-decider-flash-v1.2 tree_hard | -0.013 [-0.041, +0.013] | 0.441 |
| pplx-decider-flash-v1.2 tree vs pplx-decider-flash-v1.2 tree_v2 | -0.116 [-0.151, -0.081] | 1.55e-10 |
| pplx-decider-flash-v1.2 tree vs gpt-6-luna-decisions flat | -0.192 [-0.247, -0.138] | 6.11e-11 |
| pplx-decider-flash-v1.2 tree vs gpt-6-luna-decisions tree | +0.044 [+0.009, +0.079] | 0.0205 |
| pplx-decider-flash-v1.2 tree vs gpt-6-luna-decisions tree_hard | +0.044 [+0.009, +0.079] | 0.0205 |
| pplx-decider-flash-v1.2 tree vs gpt-6-luna-decisions tree_v2 | -0.031 [-0.074, +0.015] | 0.202 |
| pplx-decider-flash-v1.2 tree vs d1 flat | -0.148 [-0.203, -0.094] | 3.18e-07 |
| pplx-decider-flash-v1.2 tree vs d1 tree | +0.024 [-0.007, +0.055] | 0.177 |
| pplx-decider-flash-v1.2 tree vs d1 tree_hard | -0.002 [-0.039, +0.033] | 1 |
| pplx-decider-flash-v1.2 tree vs d1 tree_v2 | -0.096 [-0.144, -0.050] | 0.000125 |
| pplx-decider-flash-v1.2 tree vs d1-ultra flat | -0.203 [-0.258, -0.148] | 6.26e-12 |
| pplx-decider-flash-v1.2 tree vs d1-ultra tree | -0.035 [-0.068, -0.002] | 0.0519 |
| pplx-decider-flash-v1.2 tree vs d1-ultra tree_hard | -0.090 [-0.129, -0.050] | 1.27e-05 |
| pplx-decider-flash-v1.2 tree vs d1-ultra tree_v2 | -0.148 [-0.192, -0.103] | 4.56e-10 |
| pplx-decider-flash-v1.2 tree vs microsoft-decision-1 flat | -0.116 [-0.181, -0.052] | 0.000627 |
| pplx-decider-flash-v1.2 tree vs microsoft-decision-1 tree | +0.052 [+0.009, +0.094] | 0.0223 |
| pplx-decider-flash-v1.2 tree vs microsoft-decision-1 tree_hard | +0.085 [+0.037, +0.131] | 0.000685 |
| pplx-decider-flash-v1.2 tree vs microsoft-decision-1 tree_v2 | -0.103 [-0.162, -0.044] | 0.00126 |
| pplx-decider-flash-v1.2 tree vs elephant-1 flat | -0.181 [-0.229, -0.133] | 1.04e-12 |
| pplx-decider-flash-v1.2 tree vs elephant-1 tree | -0.004 [-0.033, +0.024] | 0.883 |
| pplx-decider-flash-v1.2 tree vs elephant-1 tree_hard | -0.046 [-0.081, -0.013] | 0.0111 |
| pplx-decider-flash-v1.2 tree vs elephant-1 tree_v2 | -0.116 [-0.159, -0.074] | 3.78e-07 |
| pplx-decider-flash-v1.2 tree vs mammoth-1 flat | -0.188 [-0.242, -0.133] | 8.02e-11 |
| pplx-decider-flash-v1.2 tree vs mammoth-1 tree | -0.015 [-0.048, +0.017] | 0.457 |
| pplx-decider-flash-v1.2 tree vs mammoth-1 tree_hard | -0.055 [-0.094, -0.015] | 0.00967 |
| pplx-decider-flash-v1.2 tree vs mammoth-1 tree_v2 | -0.116 [-0.162, -0.070] | 1.94e-06 |
| pplx-decider-flash-v1.2 tree vs scaledown-classify-1 flat | -0.035 [-0.092, +0.020] | 0.253 |
| pplx-decider-flash-v1.2 tree vs scaledown-classify-1 tree | +0.094 [+0.055, +0.133] | 5.69e-06 |
| pplx-decider-flash-v1.2 tree vs scaledown-classify-1 tree_hard | +0.133 [+0.081, +0.183] | 6.26e-07 |
| pplx-decider-flash-v1.2 tree vs scaledown-classify-1 tree_v2 | +0.072 [+0.028, +0.116] | 0.00184 |
| pplx-decider-flash-v1.2 tree vs gemini-2.5-flash paper_llm | -0.142 [-0.201, -0.081] | 6.61e-06 |
| pplx-decider-flash-v1.2 tree vs gemini-2.5-flash paper_llm_thinking | -0.116 [-0.181, -0.050] | 0.000775 |
| pplx-decider-flash-v1.2 tree vs gemini-3.8-flash paper_llm_low | -0.225 [-0.277, -0.172] | 3.99e-15 |
| pplx-decider-flash-v1.2 tree vs gemini-3.8-flash paper_llm_thinking | -0.201 [-0.255, -0.144] | 1.24e-11 |
| pplx-decider-flash-v1.2 tree_hard vs pplx-decider-flash-v1.2 tree_v2 | -0.103 [-0.142, -0.063] | 1.1e-06 |
| pplx-decider-flash-v1.2 tree_hard vs gpt-6-luna-decisions flat | -0.179 [-0.234, -0.127] | 1.79e-10 |
| pplx-decider-flash-v1.2 tree_hard vs gpt-6-luna-decisions tree | +0.057 [+0.013, +0.100] | 0.0148 |
| pplx-decider-flash-v1.2 tree_hard vs gpt-6-luna-decisions tree_hard | +0.057 [+0.013, +0.100] | 0.0148 |
| pplx-decider-flash-v1.2 tree_hard vs gpt-6-luna-decisions tree_v2 | -0.017 [-0.066, +0.033] | 0.546 |
| pplx-decider-flash-v1.2 tree_hard vs d1 flat | -0.135 [-0.188, -0.083] | 1.05e-06 |
| pplx-decider-flash-v1.2 tree_hard vs d1 tree | +0.037 [-0.002, +0.076] | 0.0748 |
| pplx-decider-flash-v1.2 tree_hard vs d1 tree_hard | +0.011 [-0.026, +0.048] | 0.64 |
| pplx-decider-flash-v1.2 tree_hard vs d1 tree_v2 | -0.083 [-0.131, -0.035] | 0.00154 |
| pplx-decider-flash-v1.2 tree_hard vs d1-ultra flat | -0.190 [-0.242, -0.138] | 3.11e-11 |
| pplx-decider-flash-v1.2 tree_hard vs d1-ultra tree | -0.022 [-0.061, +0.017] | 0.343 |
| pplx-decider-flash-v1.2 tree_hard vs d1-ultra tree_hard | -0.076 [-0.116, -0.037] | 0.000187 |
| pplx-decider-flash-v1.2 tree_hard vs d1-ultra tree_v2 | -0.135 [-0.183, -0.087] | 2.45e-07 |
| pplx-decider-flash-v1.2 tree_hard vs microsoft-decision-1 flat | -0.103 [-0.164, -0.041] | 0.00119 |
| pplx-decider-flash-v1.2 tree_hard vs microsoft-decision-1 tree | +0.066 [+0.022, +0.107] | 0.00387 |
| pplx-decider-flash-v1.2 tree_hard vs microsoft-decision-1 tree_hard | +0.098 [+0.052, +0.144] | 3.87e-05 |
| pplx-decider-flash-v1.2 tree_hard vs microsoft-decision-1 tree_v2 | -0.090 [-0.148, -0.033] | 0.00406 |
| pplx-decider-flash-v1.2 tree_hard vs elephant-1 flat | -0.168 [-0.216, -0.122] | 3.52e-11 |
| pplx-decider-flash-v1.2 tree_hard vs elephant-1 tree | +0.009 [-0.028, +0.046] | 0.728 |
| pplx-decider-flash-v1.2 tree_hard vs elephant-1 tree_hard | -0.033 [-0.068, +0.002] | 0.0817 |
| pplx-decider-flash-v1.2 tree_hard vs elephant-1 tree_v2 | -0.103 [-0.151, -0.057] | 4.92e-05 |
| pplx-decider-flash-v1.2 tree_hard vs mammoth-1 flat | -0.175 [-0.227, -0.124] | 3.05e-10 |
| pplx-decider-flash-v1.2 tree_hard vs mammoth-1 tree | -0.002 [-0.041, +0.039] | 1 |
| pplx-decider-flash-v1.2 tree_hard vs mammoth-1 tree_hard | -0.041 [-0.083, +0.000] | 0.0671 |
| pplx-decider-flash-v1.2 tree_hard vs mammoth-1 tree_v2 | -0.103 [-0.149, -0.055] | 6.43e-05 |
| pplx-decider-flash-v1.2 tree_hard vs scaledown-classify-1 flat | -0.022 [-0.079, +0.035] | 0.493 |
| pplx-decider-flash-v1.2 tree_hard vs scaledown-classify-1 tree | +0.107 [+0.061, +0.155] | 1.91e-05 |
| pplx-decider-flash-v1.2 tree_hard vs scaledown-classify-1 tree_hard | +0.146 [+0.094, +0.199] | 8.92e-08 |
| pplx-decider-flash-v1.2 tree_hard vs scaledown-classify-1 tree_v2 | +0.085 [+0.035, +0.135] | 0.00151 |
| pplx-decider-flash-v1.2 tree_hard vs gemini-2.5-flash paper_llm | -0.129 [-0.186, -0.072] | 1.91e-05 |
| pplx-decider-flash-v1.2 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.103 [-0.164, -0.041] | 0.00191 |
| pplx-decider-flash-v1.2 tree_hard vs gemini-3.8-flash paper_llm_low | -0.212 [-0.262, -0.162] | 5.24e-15 |
| pplx-decider-flash-v1.2 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.188 [-0.240, -0.135] | 2.64e-11 |
| pplx-decider-flash-v1.2 tree_v2 vs gpt-6-luna-decisions flat | -0.076 [-0.131, -0.024] | 0.00647 |
| pplx-decider-flash-v1.2 tree_v2 vs gpt-6-luna-decisions tree | +0.159 [+0.114, +0.207] | 1.45e-10 |
| pplx-decider-flash-v1.2 tree_v2 vs gpt-6-luna-decisions tree_hard | +0.159 [+0.114, +0.207] | 1.45e-10 |
| pplx-decider-flash-v1.2 tree_v2 vs gpt-6-luna-decisions tree_v2 | +0.085 [+0.044, +0.129] | 0.000153 |
| pplx-decider-flash-v1.2 tree_v2 vs d1 flat | -0.033 [-0.081, +0.015] | 0.221 |
| pplx-decider-flash-v1.2 tree_v2 vs d1 tree | +0.140 [+0.094, +0.186] | 3.77e-09 |
| pplx-decider-flash-v1.2 tree_v2 vs d1 tree_hard | +0.114 [+0.066, +0.162] | 4.92e-06 |
| pplx-decider-flash-v1.2 tree_v2 vs d1 tree_v2 | +0.020 [-0.017, +0.057] | 0.362 |
| pplx-decider-flash-v1.2 tree_v2 vs d1-ultra flat | -0.087 [-0.135, -0.039] | 0.000631 |
| pplx-decider-flash-v1.2 tree_v2 vs d1-ultra tree | +0.081 [+0.039, +0.120] | 0.000186 |
| pplx-decider-flash-v1.2 tree_v2 vs d1-ultra tree_hard | +0.026 [-0.015, +0.068] | 0.271 |
| pplx-decider-flash-v1.2 tree_v2 vs d1-ultra tree_v2 | -0.033 [-0.068, +0.004] | 0.101 |
| pplx-decider-flash-v1.2 tree_v2 vs microsoft-decision-1 flat | +0.000 [-0.059, +0.057] | 1 |
| pplx-decider-flash-v1.2 tree_v2 vs microsoft-decision-1 tree | +0.168 [+0.114, +0.221] | 3.38e-09 |
| pplx-decider-flash-v1.2 tree_v2 vs microsoft-decision-1 tree_hard | +0.201 [+0.144, +0.255] | 2.11e-11 |
| pplx-decider-flash-v1.2 tree_v2 vs microsoft-decision-1 tree_v2 | +0.013 [-0.039, +0.063] | 0.679 |
| pplx-decider-flash-v1.2 tree_v2 vs elephant-1 flat | -0.066 [-0.105, -0.026] | 0.00161 |
| pplx-decider-flash-v1.2 tree_v2 vs elephant-1 tree | +0.111 [+0.068, +0.155] | 1.37e-06 |
| pplx-decider-flash-v1.2 tree_v2 vs elephant-1 tree_hard | +0.070 [+0.024, +0.116] | 0.00446 |
| pplx-decider-flash-v1.2 tree_v2 vs elephant-1 tree_v2 | +0.000 [-0.033, +0.033] | 1 |
| pplx-decider-flash-v1.2 tree_v2 vs mammoth-1 flat | -0.072 [-0.118, -0.026] | 0.00293 |
| pplx-decider-flash-v1.2 tree_v2 vs mammoth-1 tree | +0.100 [+0.059, +0.142] | 2.87e-06 |
| pplx-decider-flash-v1.2 tree_v2 vs mammoth-1 tree_hard | +0.061 [+0.020, +0.103] | 0.00557 |
| pplx-decider-flash-v1.2 tree_v2 vs mammoth-1 tree_v2 | +0.000 [-0.033, +0.035] | 1 |
| pplx-decider-flash-v1.2 tree_v2 vs scaledown-classify-1 flat | +0.081 [+0.026, +0.133] | 0.00416 |
| pplx-decider-flash-v1.2 tree_v2 vs scaledown-classify-1 tree | +0.210 [+0.162, +0.258] | 7.71e-16 |
| pplx-decider-flash-v1.2 tree_v2 vs scaledown-classify-1 tree_hard | +0.249 [+0.194, +0.303] | 3.69e-17 |
| pplx-decider-flash-v1.2 tree_v2 vs scaledown-classify-1 tree_v2 | +0.188 [+0.142, +0.234] | 3.94e-14 |
| pplx-decider-flash-v1.2 tree_v2 vs gemini-2.5-flash paper_llm | -0.026 [-0.079, +0.026] | 0.379 |
| pplx-decider-flash-v1.2 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.000 [-0.059, +0.057] | 1 |
| pplx-decider-flash-v1.2 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.109 [-0.157, -0.061] | 1.17e-05 |
| pplx-decider-flash-v1.2 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.085 [-0.135, -0.035] | 0.00119 |
| gpt-6-luna-decisions flat vs gpt-6-luna-decisions tree | +0.236 [+0.179, +0.293] | 8.17e-15 |
| gpt-6-luna-decisions flat vs gpt-6-luna-decisions tree_hard | +0.236 [+0.179, +0.293] | 8.17e-15 |
| gpt-6-luna-decisions flat vs gpt-6-luna-decisions tree_v2 | +0.162 [+0.107, +0.216] | 3.43e-08 |
| gpt-6-luna-decisions flat vs d1 flat | +0.044 [-0.002, +0.090] | 0.0773 |
| gpt-6-luna-decisions flat vs d1 tree | +0.216 [+0.159, +0.275] | 9.49e-13 |
| gpt-6-luna-decisions flat vs d1 tree_hard | +0.190 [+0.133, +0.245] | 5.38e-11 |
| gpt-6-luna-decisions flat vs d1 tree_v2 | +0.096 [+0.041, +0.151] | 0.000855 |
| gpt-6-luna-decisions flat vs d1-ultra flat | -0.011 [-0.059, +0.037] | 0.723 |
| gpt-6-luna-decisions flat vs d1-ultra tree | +0.157 [+0.105, +0.212] | 2.17e-08 |
| gpt-6-luna-decisions flat vs d1-ultra tree_hard | +0.103 [+0.055, +0.151] | 4.92e-05 |
| gpt-6-luna-decisions flat vs d1-ultra tree_v2 | +0.044 [-0.009, +0.098] | 0.128 |
| gpt-6-luna-decisions flat vs microsoft-decision-1 flat | +0.076 [+0.028, +0.124] | 0.00305 |
| gpt-6-luna-decisions flat vs microsoft-decision-1 tree | +0.245 [+0.192, +0.297] | 1.26e-18 |
| gpt-6-luna-decisions flat vs microsoft-decision-1 tree_hard | +0.277 [+0.225, +0.330] | 8.52e-23 |
| gpt-6-luna-decisions flat vs microsoft-decision-1 tree_v2 | +0.090 [+0.033, +0.146] | 0.00269 |
| gpt-6-luna-decisions flat vs elephant-1 flat | +0.011 [-0.035, +0.057] | 0.704 |
| gpt-6-luna-decisions flat vs elephant-1 tree | +0.188 [+0.131, +0.245] | 2.78e-10 |
| gpt-6-luna-decisions flat vs elephant-1 tree_hard | +0.146 [+0.092, +0.201] | 2.71e-07 |
| gpt-6-luna-decisions flat vs elephant-1 tree_v2 | +0.076 [+0.022, +0.131] | 0.00832 |
| gpt-6-luna-decisions flat vs mammoth-1 flat | +0.004 [-0.044, +0.052] | 0.93 |
| gpt-6-luna-decisions flat vs mammoth-1 tree | +0.177 [+0.122, +0.231] | 9.3e-10 |
| gpt-6-luna-decisions flat vs mammoth-1 tree_hard | +0.138 [+0.087, +0.188] | 1.7e-07 |
| gpt-6-luna-decisions flat vs mammoth-1 tree_v2 | +0.076 [+0.022, +0.133] | 0.00793 |
| gpt-6-luna-decisions flat vs scaledown-classify-1 flat | +0.157 [+0.105, +0.210] | 7.14e-09 |
| gpt-6-luna-decisions flat vs scaledown-classify-1 tree | +0.286 [+0.227, +0.347] | 2.74e-18 |
| gpt-6-luna-decisions flat vs scaledown-classify-1 tree_hard | +0.325 [+0.269, +0.382] | 1.32e-25 |
| gpt-6-luna-decisions flat vs scaledown-classify-1 tree_v2 | +0.264 [+0.205, +0.323] | 4.33e-16 |
| gpt-6-luna-decisions flat vs gemini-2.5-flash paper_llm | +0.050 [+0.000, +0.100] | 0.0616 |
| gpt-6-luna-decisions flat vs gemini-2.5-flash paper_llm_thinking | +0.076 [+0.022, +0.131] | 0.00682 |
| gpt-6-luna-decisions flat vs gemini-3.8-flash paper_llm_low | -0.033 [-0.074, +0.009] | 0.151 |
| gpt-6-luna-decisions flat vs gemini-3.8-flash paper_llm_thinking | -0.009 [-0.052, +0.035] | 0.773 |
| gpt-6-luna-decisions tree vs gpt-6-luna-decisions tree_hard | +0.000 [+0.000, +0.000] | 1 |
| gpt-6-luna-decisions tree vs gpt-6-luna-decisions tree_v2 | -0.074 [-0.103, -0.048] | 1.41e-07 |
| gpt-6-luna-decisions tree vs d1 flat | -0.192 [-0.251, -0.133] | 6.11e-10 |
| gpt-6-luna-decisions tree vs d1 tree | -0.020 [-0.050, +0.011] | 0.272 |
| gpt-6-luna-decisions tree vs d1 tree_hard | -0.046 [-0.085, -0.009] | 0.0295 |
| gpt-6-luna-decisions tree vs d1 tree_v2 | -0.140 [-0.186, -0.096] | 3.77e-09 |
| gpt-6-luna-decisions tree vs d1-ultra flat | -0.247 [-0.303, -0.190] | 9.11e-16 |
| gpt-6-luna-decisions tree vs d1-ultra tree | -0.079 [-0.116, -0.044] | 1.92e-05 |
| gpt-6-luna-decisions tree vs d1-ultra tree_hard | -0.133 [-0.179, -0.087] | 2.5e-08 |
| gpt-6-luna-decisions tree vs d1-ultra tree_v2 | -0.192 [-0.238, -0.144] | 1.46e-14 |
| gpt-6-luna-decisions tree vs microsoft-decision-1 flat | -0.159 [-0.229, -0.092] | 9.32e-06 |
| gpt-6-luna-decisions tree vs microsoft-decision-1 tree | +0.009 [-0.039, +0.055] | 0.781 |
| gpt-6-luna-decisions tree vs microsoft-decision-1 tree_hard | +0.041 [-0.011, +0.092] | 0.129 |
| gpt-6-luna-decisions tree vs microsoft-decision-1 tree_v2 | -0.146 [-0.207, -0.085] | 7.02e-06 |
| gpt-6-luna-decisions tree vs elephant-1 flat | -0.225 [-0.275, -0.172] | 2.96e-16 |
| gpt-6-luna-decisions tree vs elephant-1 tree | -0.048 [-0.076, -0.020] | 0.00164 |
| gpt-6-luna-decisions tree vs elephant-1 tree_hard | -0.090 [-0.129, -0.050] | 1.61e-05 |
| gpt-6-luna-decisions tree vs elephant-1 tree_v2 | -0.159 [-0.203, -0.116] | 5.31e-12 |
| gpt-6-luna-decisions tree vs mammoth-1 flat | -0.231 [-0.288, -0.177] | 1.95e-14 |
| gpt-6-luna-decisions tree vs mammoth-1 tree | -0.059 [-0.094, -0.024] | 0.00182 |
| gpt-6-luna-decisions tree vs mammoth-1 tree_hard | -0.098 [-0.142, -0.055] | 1.94e-05 |
| gpt-6-luna-decisions tree vs mammoth-1 tree_v2 | -0.159 [-0.205, -0.111] | 1.45e-10 |
| gpt-6-luna-decisions tree vs scaledown-classify-1 flat | -0.079 [-0.133, -0.024] | 0.0061 |
| gpt-6-luna-decisions tree vs scaledown-classify-1 tree | +0.050 [+0.020, +0.081] | 0.00219 |
| gpt-6-luna-decisions tree vs scaledown-classify-1 tree_hard | +0.090 [+0.037, +0.142] | 0.000833 |
| gpt-6-luna-decisions tree vs scaledown-classify-1 tree_v2 | +0.028 [-0.007, +0.063] | 0.142 |
| gpt-6-luna-decisions tree vs gemini-2.5-flash paper_llm | -0.186 [-0.247, -0.124] | 7.68e-09 |
| gpt-6-luna-decisions tree vs gemini-2.5-flash paper_llm_thinking | -0.159 [-0.227, -0.092] | 7.94e-06 |
| gpt-6-luna-decisions tree vs gemini-3.8-flash paper_llm_low | -0.269 [-0.323, -0.214] | 8.15e-19 |
| gpt-6-luna-decisions tree vs gemini-3.8-flash paper_llm_thinking | -0.245 [-0.301, -0.188] | 2.84e-15 |
| gpt-6-luna-decisions tree_hard vs gpt-6-luna-decisions tree_v2 | -0.074 [-0.103, -0.048] | 1.41e-07 |
| gpt-6-luna-decisions tree_hard vs d1 flat | -0.192 [-0.251, -0.133] | 6.11e-10 |
| gpt-6-luna-decisions tree_hard vs d1 tree | -0.020 [-0.050, +0.011] | 0.272 |
| gpt-6-luna-decisions tree_hard vs d1 tree_hard | -0.046 [-0.085, -0.009] | 0.0295 |
| gpt-6-luna-decisions tree_hard vs d1 tree_v2 | -0.140 [-0.186, -0.096] | 3.77e-09 |
| gpt-6-luna-decisions tree_hard vs d1-ultra flat | -0.247 [-0.303, -0.190] | 9.11e-16 |
| gpt-6-luna-decisions tree_hard vs d1-ultra tree | -0.079 [-0.116, -0.044] | 1.92e-05 |
| gpt-6-luna-decisions tree_hard vs d1-ultra tree_hard | -0.133 [-0.179, -0.087] | 2.5e-08 |
| gpt-6-luna-decisions tree_hard vs d1-ultra tree_v2 | -0.192 [-0.238, -0.144] | 1.46e-14 |
| gpt-6-luna-decisions tree_hard vs microsoft-decision-1 flat | -0.159 [-0.229, -0.092] | 9.32e-06 |
| gpt-6-luna-decisions tree_hard vs microsoft-decision-1 tree | +0.009 [-0.039, +0.055] | 0.781 |
| gpt-6-luna-decisions tree_hard vs microsoft-decision-1 tree_hard | +0.041 [-0.011, +0.092] | 0.129 |
| gpt-6-luna-decisions tree_hard vs microsoft-decision-1 tree_v2 | -0.146 [-0.207, -0.085] | 7.02e-06 |
| gpt-6-luna-decisions tree_hard vs elephant-1 flat | -0.225 [-0.275, -0.172] | 2.96e-16 |
| gpt-6-luna-decisions tree_hard vs elephant-1 tree | -0.048 [-0.076, -0.020] | 0.00164 |
| gpt-6-luna-decisions tree_hard vs elephant-1 tree_hard | -0.090 [-0.129, -0.050] | 1.61e-05 |
| gpt-6-luna-decisions tree_hard vs elephant-1 tree_v2 | -0.159 [-0.203, -0.116] | 5.31e-12 |
| gpt-6-luna-decisions tree_hard vs mammoth-1 flat | -0.231 [-0.288, -0.177] | 1.95e-14 |
| gpt-6-luna-decisions tree_hard vs mammoth-1 tree | -0.059 [-0.094, -0.024] | 0.00182 |
| gpt-6-luna-decisions tree_hard vs mammoth-1 tree_hard | -0.098 [-0.142, -0.055] | 1.94e-05 |
| gpt-6-luna-decisions tree_hard vs mammoth-1 tree_v2 | -0.159 [-0.205, -0.111] | 1.45e-10 |
| gpt-6-luna-decisions tree_hard vs scaledown-classify-1 flat | -0.079 [-0.133, -0.024] | 0.0061 |
| gpt-6-luna-decisions tree_hard vs scaledown-classify-1 tree | +0.050 [+0.020, +0.081] | 0.00219 |
| gpt-6-luna-decisions tree_hard vs scaledown-classify-1 tree_hard | +0.090 [+0.037, +0.142] | 0.000833 |
| gpt-6-luna-decisions tree_hard vs scaledown-classify-1 tree_v2 | +0.028 [-0.007, +0.063] | 0.142 |
| gpt-6-luna-decisions tree_hard vs gemini-2.5-flash paper_llm | -0.186 [-0.247, -0.124] | 7.68e-09 |
| gpt-6-luna-decisions tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.159 [-0.227, -0.092] | 7.94e-06 |
| gpt-6-luna-decisions tree_hard vs gemini-3.8-flash paper_llm_low | -0.269 [-0.323, -0.214] | 8.15e-19 |
| gpt-6-luna-decisions tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.245 [-0.301, -0.188] | 2.84e-15 |
| gpt-6-luna-decisions tree_v2 vs d1 flat | -0.118 [-0.175, -0.063] | 5.16e-05 |
| gpt-6-luna-decisions tree_v2 vs d1 tree | +0.055 [+0.013, +0.094] | 0.0105 |
| gpt-6-luna-decisions tree_v2 vs d1 tree_hard | +0.028 [-0.017, +0.074] | 0.263 |
| gpt-6-luna-decisions tree_v2 vs d1 tree_v2 | -0.066 [-0.105, -0.028] | 0.00161 |
| gpt-6-luna-decisions tree_v2 vs d1-ultra flat | -0.172 [-0.225, -0.120] | 1.25e-09 |
| gpt-6-luna-decisions tree_v2 vs d1-ultra tree | -0.004 [-0.044, +0.035] | 0.912 |
| gpt-6-luna-decisions tree_v2 vs d1-ultra tree_hard | -0.059 [-0.107, -0.013] | 0.0177 |
| gpt-6-luna-decisions tree_v2 vs d1-ultra tree_v2 | -0.118 [-0.159, -0.076] | 5.51e-08 |
| gpt-6-luna-decisions tree_v2 vs microsoft-decision-1 flat | -0.085 [-0.151, -0.022] | 0.0126 |
| gpt-6-luna-decisions tree_v2 vs microsoft-decision-1 tree | +0.083 [+0.028, +0.135] | 0.00332 |
| gpt-6-luna-decisions tree_v2 vs microsoft-decision-1 tree_hard | +0.116 [+0.059, +0.172] | 0.000119 |
| gpt-6-luna-decisions tree_v2 vs microsoft-decision-1 tree_v2 | -0.072 [-0.131, -0.015] | 0.0171 |
| gpt-6-luna-decisions tree_v2 vs elephant-1 flat | -0.151 [-0.199, -0.103] | 3.86e-09 |
| gpt-6-luna-decisions tree_v2 vs elephant-1 tree | +0.026 [-0.013, +0.066] | 0.224 |
| gpt-6-luna-decisions tree_v2 vs elephant-1 tree_hard | -0.015 [-0.061, +0.031] | 0.576 |
| gpt-6-luna-decisions tree_v2 vs elephant-1 tree_v2 | -0.085 [-0.124, -0.046] | 2.77e-05 |
| gpt-6-luna-decisions tree_v2 vs mammoth-1 flat | -0.157 [-0.210, -0.105] | 1.76e-08 |
| gpt-6-luna-decisions tree_v2 vs mammoth-1 tree | +0.015 [-0.024, +0.052] | 0.505 |
| gpt-6-luna-decisions tree_v2 vs mammoth-1 tree_hard | -0.024 [-0.068, +0.020] | 0.324 |
| gpt-6-luna-decisions tree_v2 vs mammoth-1 tree_v2 | -0.085 [-0.127, -0.044] | 9.34e-05 |
| gpt-6-luna-decisions tree_v2 vs scaledown-classify-1 flat | -0.004 [-0.057, +0.048] | 0.936 |
| gpt-6-luna-decisions tree_v2 vs scaledown-classify-1 tree | +0.124 [+0.087, +0.164] | 4.26e-10 |
| gpt-6-luna-decisions tree_v2 vs scaledown-classify-1 tree_hard | +0.164 [+0.111, +0.216] | 5.74e-09 |
| gpt-6-luna-decisions tree_v2 vs scaledown-classify-1 tree_v2 | +0.103 [+0.066, +0.142] | 2.11e-07 |
| gpt-6-luna-decisions tree_v2 vs gemini-2.5-flash paper_llm | -0.111 [-0.168, -0.055] | 0.000236 |
| gpt-6-luna-decisions tree_v2 vs gemini-2.5-flash paper_llm_thinking | -0.085 [-0.151, -0.022] | 0.0119 |
| gpt-6-luna-decisions tree_v2 vs gemini-3.8-flash paper_llm_low | -0.194 [-0.249, -0.140] | 1.82e-11 |
| gpt-6-luna-decisions tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.170 [-0.227, -0.114] | 8.29e-09 |
| d1 flat vs d1 tree | +0.172 [+0.118, +0.229] | 4.72e-09 |
| d1 flat vs d1 tree_hard | +0.146 [+0.094, +0.201] | 1.59e-07 |
| d1 flat vs d1 tree_v2 | +0.052 [+0.007, +0.100] | 0.0416 |
| d1 flat vs d1-ultra flat | -0.055 [-0.092, -0.015] | 0.00728 |
| d1 flat vs d1-ultra tree | +0.114 [+0.061, +0.166] | 5.98e-05 |
| d1 flat vs d1-ultra tree_hard | +0.059 [+0.011, +0.109] | 0.0238 |
| d1 flat vs d1-ultra tree_v2 | +0.000 [-0.046, +0.048] | 1 |
| d1 flat vs microsoft-decision-1 flat | +0.033 [-0.015, +0.079] | 0.199 |
| d1 flat vs microsoft-decision-1 tree | +0.201 [+0.144, +0.258] | 5.67e-11 |
| d1 flat vs microsoft-decision-1 tree_hard | +0.234 [+0.177, +0.290] | 2.44e-14 |
| d1 flat vs microsoft-decision-1 tree_v2 | +0.046 [-0.011, +0.100] | 0.128 |
| d1 flat vs elephant-1 flat | -0.033 [-0.072, +0.007] | 0.133 |
| d1 flat vs elephant-1 tree | +0.144 [+0.090, +0.201] | 1.48e-06 |
| d1 flat vs elephant-1 tree_hard | +0.103 [+0.048, +0.157] | 0.000437 |
| d1 flat vs elephant-1 tree_v2 | +0.033 [-0.020, +0.085] | 0.251 |
| d1 flat vs mammoth-1 flat | -0.039 [-0.079, +0.000] | 0.063 |
| d1 flat vs mammoth-1 tree | +0.133 [+0.079, +0.188] | 3.56e-06 |
| d1 flat vs mammoth-1 tree_hard | +0.094 [+0.046, +0.142] | 0.00027 |
| d1 flat vs mammoth-1 tree_v2 | +0.033 [-0.017, +0.083] | 0.232 |
| d1 flat vs scaledown-classify-1 flat | +0.114 [+0.057, +0.170] | 0.000142 |
| d1 flat vs scaledown-classify-1 tree | +0.242 [+0.183, +0.301] | 3.89e-14 |
| d1 flat vs scaledown-classify-1 tree_hard | +0.282 [+0.227, +0.336] | 1.73e-20 |
| d1 flat vs scaledown-classify-1 tree_v2 | +0.221 [+0.162, +0.279] | 1.68e-12 |
| d1 flat vs gemini-2.5-flash paper_llm | +0.007 [-0.041, +0.052] | 0.857 |
| d1 flat vs gemini-2.5-flash paper_llm_thinking | +0.033 [-0.017, +0.081] | 0.232 |
| d1 flat vs gemini-3.8-flash paper_llm_low | -0.076 [-0.118, -0.035] | 0.000562 |
| d1 flat vs gemini-3.8-flash paper_llm_thinking | -0.052 [-0.096, -0.011] | 0.021 |
| d1 tree vs d1 tree_hard | -0.026 [-0.055, +0.000] | 0.0884 |
| d1 tree vs d1 tree_v2 | -0.120 [-0.157, -0.085] | 2.05e-10 |
| d1 tree vs d1-ultra flat | -0.227 [-0.282, -0.172] | 2.35e-14 |
| d1 tree vs d1-ultra tree | -0.059 [-0.092, -0.026] | 0.000584 |
| d1 tree vs d1-ultra tree_hard | -0.114 [-0.157, -0.072] | 3.28e-07 |
| d1 tree vs d1-ultra tree_v2 | -0.172 [-0.218, -0.127] | 1.2e-12 |
| d1 tree vs microsoft-decision-1 flat | -0.140 [-0.207, -0.072] | 6.65e-05 |
| d1 tree vs microsoft-decision-1 tree | +0.028 [-0.015, +0.070] | 0.232 |
| d1 tree vs microsoft-decision-1 tree_hard | +0.061 [+0.013, +0.109] | 0.0158 |
| d1 tree vs microsoft-decision-1 tree_v2 | -0.127 [-0.188, -0.066] | 5.92e-05 |
| d1 tree vs elephant-1 flat | -0.205 [-0.255, -0.155] | 2.16e-14 |
| d1 tree vs elephant-1 tree | -0.028 [-0.057, +0.000] | 0.0596 |
| d1 tree vs elephant-1 tree_hard | -0.070 [-0.107, -0.033] | 0.000313 |
| d1 tree vs elephant-1 tree_v2 | -0.140 [-0.181, -0.096] | 3.99e-10 |
| d1 tree vs mammoth-1 flat | -0.212 [-0.269, -0.157] | 4.8e-13 |
| d1 tree vs mammoth-1 tree | -0.039 [-0.072, -0.007] | 0.0273 |
| d1 tree vs mammoth-1 tree_hard | -0.079 [-0.118, -0.039] | 0.00013 |
| d1 tree vs mammoth-1 tree_v2 | -0.140 [-0.186, -0.094] | 5.21e-09 |
| d1 tree vs scaledown-classify-1 flat | -0.059 [-0.114, -0.004] | 0.0439 |
| d1 tree vs scaledown-classify-1 tree | +0.070 [+0.035, +0.105] | 0.000131 |
| d1 tree vs scaledown-classify-1 tree_hard | +0.109 [+0.059, +0.159] | 3.29e-05 |
| d1 tree vs scaledown-classify-1 tree_v2 | +0.048 [+0.009, +0.090] | 0.0246 |
| d1 tree vs gemini-2.5-flash paper_llm | -0.166 [-0.225, -0.105] | 1.46e-07 |
| d1 tree vs gemini-2.5-flash paper_llm_thinking | -0.140 [-0.207, -0.072] | 6.21e-05 |
| d1 tree vs gemini-3.8-flash paper_llm_low | -0.249 [-0.306, -0.194] | 5.64e-17 |
| d1 tree vs gemini-3.8-flash paper_llm_thinking | -0.225 [-0.282, -0.168] | 5.09e-14 |
| d1 tree_hard vs d1 tree_v2 | -0.094 [-0.133, -0.055] | 7.35e-06 |
| d1 tree_hard vs d1-ultra flat | -0.201 [-0.253, -0.148] | 5.59e-13 |
| d1 tree_hard vs d1-ultra tree | -0.033 [-0.070, +0.004] | 0.105 |
| d1 tree_hard vs d1-ultra tree_hard | -0.087 [-0.129, -0.048] | 2.37e-05 |
| d1 tree_hard vs d1-ultra tree_v2 | -0.146 [-0.194, -0.098] | 8.69e-09 |
| d1 tree_hard vs microsoft-decision-1 flat | -0.114 [-0.177, -0.050] | 0.000523 |
| d1 tree_hard vs microsoft-decision-1 tree | +0.055 [+0.009, +0.100] | 0.0199 |
| d1 tree_hard vs microsoft-decision-1 tree_hard | +0.087 [+0.041, +0.133] | 0.000371 |
| d1 tree_hard vs microsoft-decision-1 tree_v2 | -0.100 [-0.164, -0.039] | 0.00165 |
| d1 tree_hard vs elephant-1 flat | -0.179 [-0.229, -0.129] | 1.12e-11 |
| d1 tree_hard vs elephant-1 tree | -0.002 [-0.037, +0.033] | 1 |
| d1 tree_hard vs elephant-1 tree_hard | -0.044 [-0.081, -0.007] | 0.0308 |
| d1 tree_hard vs elephant-1 tree_v2 | -0.114 [-0.162, -0.066] | 6.97e-06 |
| d1 tree_hard vs mammoth-1 flat | -0.186 [-0.238, -0.135] | 1.17e-11 |
| d1 tree_hard vs mammoth-1 tree | -0.013 [-0.052, +0.026] | 0.586 |
| d1 tree_hard vs mammoth-1 tree_hard | -0.052 [-0.094, -0.011] | 0.0184 |
| d1 tree_hard vs mammoth-1 tree_v2 | -0.114 [-0.162, -0.066] | 8.23e-06 |
| d1 tree_hard vs scaledown-classify-1 flat | -0.033 [-0.087, +0.022] | 0.273 |
| d1 tree_hard vs scaledown-classify-1 tree | +0.096 [+0.055, +0.140] | 2.3e-05 |
| d1 tree_hard vs scaledown-classify-1 tree_hard | +0.135 [+0.085, +0.186] | 3.64e-07 |
| d1 tree_hard vs scaledown-classify-1 tree_v2 | +0.074 [+0.028, +0.122] | 0.00266 |
| d1 tree_hard vs gemini-2.5-flash paper_llm | -0.140 [-0.199, -0.083] | 5.06e-06 |
| d1 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.114 [-0.177, -0.050] | 0.000623 |
| d1 tree_hard vs gemini-3.8-flash paper_llm_low | -0.223 [-0.275, -0.172] | 7.6e-16 |
| d1 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.199 [-0.251, -0.146] | 1.22e-12 |
| d1 tree_v2 vs d1-ultra flat | -0.107 [-0.155, -0.059] | 1.91e-05 |
| d1 tree_v2 vs d1-ultra tree | +0.061 [+0.022, +0.105] | 0.00557 |
| d1 tree_v2 vs d1-ultra tree_hard | +0.007 [-0.039, +0.050] | 0.85 |
| d1 tree_v2 vs d1-ultra tree_v2 | -0.052 [-0.090, -0.017] | 0.00708 |
| d1 tree_v2 vs microsoft-decision-1 flat | -0.020 [-0.081, +0.041] | 0.569 |
| d1 tree_v2 vs microsoft-decision-1 tree | +0.148 [+0.094, +0.201] | 2.7e-07 |
| d1 tree_v2 vs microsoft-decision-1 tree_hard | +0.181 [+0.124, +0.238] | 2.49e-09 |
| d1 tree_v2 vs microsoft-decision-1 tree_v2 | -0.007 [-0.059, +0.046] | 0.868 |
| d1 tree_v2 vs elephant-1 flat | -0.085 [-0.129, -0.041] | 0.000206 |
| d1 tree_v2 vs elephant-1 tree | +0.092 [+0.048, +0.135] | 8.98e-05 |
| d1 tree_v2 vs elephant-1 tree_hard | +0.050 [+0.004, +0.096] | 0.0451 |
| d1 tree_v2 vs elephant-1 tree_v2 | -0.020 [-0.055, +0.015] | 0.321 |
| d1 tree_v2 vs mammoth-1 flat | -0.092 [-0.138, -0.048] | 0.000138 |
| d1 tree_v2 vs mammoth-1 tree | +0.081 [+0.039, +0.122] | 0.000158 |
| d1 tree_v2 vs mammoth-1 tree_hard | +0.041 [+0.002, +0.081] | 0.0558 |
| d1 tree_v2 vs mammoth-1 tree_v2 | -0.020 [-0.055, +0.015] | 0.321 |
| d1 tree_v2 vs scaledown-classify-1 flat | +0.061 [+0.009, +0.114] | 0.0261 |
| d1 tree_v2 vs scaledown-classify-1 tree | +0.190 [+0.144, +0.236] | 8.36e-15 |
| d1 tree_v2 vs scaledown-classify-1 tree_hard | +0.229 [+0.175, +0.284] | 3.51e-15 |
| d1 tree_v2 vs scaledown-classify-1 tree_v2 | +0.168 [+0.124, +0.214] | 1.22e-12 |
| d1 tree_v2 vs gemini-2.5-flash paper_llm | -0.046 [-0.100, +0.009] | 0.117 |
| d1 tree_v2 vs gemini-2.5-flash paper_llm_thinking | -0.020 [-0.079, +0.039] | 0.567 |
| d1 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.129 [-0.177, -0.081] | 5.96e-07 |
| d1 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.105 [-0.155, -0.055] | 6.11e-05 |
| d1-ultra flat vs d1-ultra tree | +0.168 [+0.116, +0.221] | 3.38e-09 |
| d1-ultra flat vs d1-ultra tree_hard | +0.114 [+0.066, +0.162] | 8.23e-06 |
| d1-ultra flat vs d1-ultra tree_v2 | +0.055 [+0.011, +0.098] | 0.0235 |
| d1-ultra flat vs microsoft-decision-1 flat | +0.087 [+0.037, +0.138] | 0.000763 |
| d1-ultra flat vs microsoft-decision-1 tree | +0.255 [+0.197, +0.314] | 2.37e-15 |
| d1-ultra flat vs microsoft-decision-1 tree_hard | +0.288 [+0.229, +0.347] | 1.21e-18 |
| d1-ultra flat vs microsoft-decision-1 tree_v2 | +0.100 [+0.048, +0.151] | 0.000237 |
| d1-ultra flat vs elephant-1 flat | +0.022 [-0.020, +0.063] | 0.348 |
| d1-ultra flat vs elephant-1 tree | +0.199 [+0.142, +0.255] | 8.32e-11 |
| d1-ultra flat vs elephant-1 tree_hard | +0.157 [+0.100, +0.214] | 1.87e-07 |
| d1-ultra flat vs elephant-1 tree_v2 | +0.087 [+0.037, +0.138] | 0.000995 |
| d1-ultra flat vs mammoth-1 flat | +0.015 [-0.015, +0.046] | 0.401 |
| d1-ultra flat vs mammoth-1 tree | +0.188 [+0.135, +0.242] | 4.67e-11 |
| d1-ultra flat vs mammoth-1 tree_hard | +0.148 [+0.103, +0.197] | 3.28e-09 |
| d1-ultra flat vs mammoth-1 tree_v2 | +0.087 [+0.041, +0.133] | 0.000464 |
| d1-ultra flat vs scaledown-classify-1 flat | +0.168 [+0.116, +0.221] | 1.3e-09 |
| d1-ultra flat vs scaledown-classify-1 tree | +0.297 [+0.240, +0.354] | 4.03e-21 |
| d1-ultra flat vs scaledown-classify-1 tree_hard | +0.336 [+0.277, +0.393] | 1.9e-25 |
| d1-ultra flat vs scaledown-classify-1 tree_v2 | +0.275 [+0.221, +0.330] | 1.22e-19 |
| d1-ultra flat vs gemini-2.5-flash paper_llm | +0.061 [+0.017, +0.105] | 0.0104 |
| d1-ultra flat vs gemini-2.5-flash paper_llm_thinking | +0.087 [+0.039, +0.135] | 0.000516 |
| d1-ultra flat vs gemini-3.8-flash paper_llm_low | -0.022 [-0.063, +0.020] | 0.353 |
| d1-ultra flat vs gemini-3.8-flash paper_llm_thinking | +0.002 [-0.039, +0.041] | 1 |
| d1-ultra tree vs d1-ultra tree_hard | -0.055 [-0.090, -0.020] | 0.00307 |
| d1-ultra tree vs d1-ultra tree_v2 | -0.114 [-0.149, -0.079] | 3.14e-09 |
| d1-ultra tree vs microsoft-decision-1 flat | -0.081 [-0.146, -0.020] | 0.0167 |
| d1-ultra tree vs microsoft-decision-1 tree | +0.087 [+0.041, +0.131] | 0.00033 |
| d1-ultra tree vs microsoft-decision-1 tree_hard | +0.120 [+0.070, +0.168] | 5.72e-06 |
| d1-ultra tree vs microsoft-decision-1 tree_v2 | -0.068 [-0.127, -0.011] | 0.0288 |
| d1-ultra tree vs elephant-1 flat | -0.146 [-0.192, -0.100] | 3.7e-09 |
| d1-ultra tree vs elephant-1 tree | +0.031 [-0.002, +0.063] | 0.0814 |
| d1-ultra tree vs elephant-1 tree_hard | -0.011 [-0.050, +0.026] | 0.649 |
| d1-ultra tree vs elephant-1 tree_v2 | -0.081 [-0.122, -0.041] | 0.000132 |
| d1-ultra tree vs mammoth-1 flat | -0.153 [-0.205, -0.103] | 2.98e-08 |
| d1-ultra tree vs mammoth-1 tree | +0.020 [-0.009, +0.048] | 0.222 |
| d1-ultra tree vs mammoth-1 tree_hard | -0.020 [-0.055, +0.015] | 0.342 |
| d1-ultra tree vs mammoth-1 tree_v2 | -0.081 [-0.122, -0.039] | 0.000219 |
| d1-ultra tree vs scaledown-classify-1 flat | +0.000 [-0.055, +0.055] | 1 |
| d1-ultra tree vs scaledown-classify-1 tree | +0.129 [+0.090, +0.168] | 1.53e-10 |
| d1-ultra tree vs scaledown-classify-1 tree_hard | +0.168 [+0.116, +0.218] | 5.95e-10 |
| d1-ultra tree vs scaledown-classify-1 tree_v2 | +0.107 [+0.066, +0.148] | 8.51e-07 |
| d1-ultra tree vs gemini-2.5-flash paper_llm | -0.107 [-0.164, -0.048] | 0.000553 |
| d1-ultra tree vs gemini-2.5-flash paper_llm_thinking | -0.081 [-0.144, -0.020] | 0.0167 |
| d1-ultra tree vs gemini-3.8-flash paper_llm_low | -0.190 [-0.242, -0.138] | 9.45e-12 |
| d1-ultra tree vs gemini-3.8-flash paper_llm_thinking | -0.166 [-0.221, -0.114] | 6.13e-09 |
| d1-ultra tree_hard vs d1-ultra tree_v2 | -0.059 [-0.100, -0.015] | 0.00863 |
| d1-ultra tree_hard vs microsoft-decision-1 flat | -0.026 [-0.083, +0.031] | 0.41 |
| d1-ultra tree_hard vs microsoft-decision-1 tree | +0.142 [+0.096, +0.188] | 4.66e-09 |
| d1-ultra tree_hard vs microsoft-decision-1 tree_hard | +0.175 [+0.127, +0.223] | 9.17e-12 |
| d1-ultra tree_hard vs microsoft-decision-1 tree_v2 | -0.013 [-0.070, +0.044] | 0.709 |
| d1-ultra tree_hard vs elephant-1 flat | -0.092 [-0.133, -0.050] | 3.89e-05 |
| d1-ultra tree_hard vs elephant-1 tree | +0.085 [+0.044, +0.129] | 0.000111 |
| d1-ultra tree_hard vs elephant-1 tree_hard | +0.044 [+0.002, +0.087] | 0.0544 |
| d1-ultra tree_hard vs elephant-1 tree_v2 | -0.026 [-0.072, +0.020] | 0.307 |
| d1-ultra tree_hard vs mammoth-1 flat | -0.098 [-0.144, -0.052] | 8.06e-05 |
| d1-ultra tree_hard vs mammoth-1 tree | +0.074 [+0.037, +0.114] | 0.000183 |
| d1-ultra tree_hard vs mammoth-1 tree_hard | +0.035 [+0.002, +0.070] | 0.0559 |
| d1-ultra tree_hard vs mammoth-1 tree_v2 | -0.026 [-0.070, +0.020] | 0.303 |
| d1-ultra tree_hard vs scaledown-classify-1 flat | +0.055 [+0.000, +0.109] | 0.0598 |
| d1-ultra tree_hard vs scaledown-classify-1 tree | +0.183 [+0.133, +0.234] | 3.21e-12 |
| d1-ultra tree_hard vs scaledown-classify-1 tree_hard | +0.223 [+0.170, +0.275] | 2.8e-15 |
| d1-ultra tree_hard vs scaledown-classify-1 tree_v2 | +0.162 [+0.109, +0.214] | 3.29e-09 |
| d1-ultra tree_hard vs gemini-2.5-flash paper_llm | -0.052 [-0.105, +0.000] | 0.0652 |
| d1-ultra tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.026 [-0.085, +0.033] | 0.422 |
| d1-ultra tree_hard vs gemini-3.8-flash paper_llm_low | -0.135 [-0.181, -0.092] | 1.22e-08 |
| d1-ultra tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.111 [-0.159, -0.066] | 8.29e-06 |
| d1-ultra tree_v2 vs microsoft-decision-1 flat | +0.033 [-0.026, +0.090] | 0.303 |
| d1-ultra tree_v2 vs microsoft-decision-1 tree | +0.201 [+0.144, +0.255] | 3.5e-11 |
| d1-ultra tree_v2 vs microsoft-decision-1 tree_hard | +0.234 [+0.175, +0.293] | 2.61e-13 |
| d1-ultra tree_v2 vs microsoft-decision-1 tree_v2 | +0.046 [-0.004, +0.096] | 0.0848 |
| d1-ultra tree_v2 vs elephant-1 flat | -0.033 [-0.074, +0.009] | 0.151 |
| d1-ultra tree_v2 vs elephant-1 tree | +0.144 [+0.096, +0.190] | 7.5e-09 |
| d1-ultra tree_v2 vs elephant-1 tree_hard | +0.103 [+0.052, +0.151] | 8.27e-05 |
| d1-ultra tree_v2 vs elephant-1 tree_v2 | +0.033 [-0.002, +0.068] | 0.0912 |
| d1-ultra tree_v2 vs mammoth-1 flat | -0.039 [-0.083, +0.004] | 0.0982 |
| d1-ultra tree_v2 vs mammoth-1 tree | +0.133 [+0.094, +0.173] | 4.39e-10 |
| d1-ultra tree_v2 vs mammoth-1 tree_hard | +0.094 [+0.052, +0.135] | 1.18e-05 |
| d1-ultra tree_v2 vs mammoth-1 tree_v2 | +0.033 [+0.002, +0.063] | 0.0489 |
| d1-ultra tree_v2 vs scaledown-classify-1 flat | +0.114 [+0.061, +0.164] | 2.63e-05 |
| d1-ultra tree_v2 vs scaledown-classify-1 tree | +0.242 [+0.194, +0.288] | 3.45e-21 |
| d1-ultra tree_v2 vs scaledown-classify-1 tree_hard | +0.282 [+0.223, +0.338] | 6.53e-19 |
| d1-ultra tree_v2 vs scaledown-classify-1 tree_v2 | +0.221 [+0.177, +0.264] | 1.61e-20 |
| d1-ultra tree_v2 vs gemini-2.5-flash paper_llm | +0.007 [-0.046, +0.059] | 0.87 |
| d1-ultra tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.033 [-0.024, +0.090] | 0.298 |
| d1-ultra tree_v2 vs gemini-3.8-flash paper_llm_low | -0.076 [-0.124, -0.028] | 0.00262 |
| d1-ultra tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.052 [-0.103, -0.002] | 0.0498 |
| microsoft-decision-1 flat vs microsoft-decision-1 tree | +0.168 [+0.111, +0.225] | 2.97e-08 |
| microsoft-decision-1 flat vs microsoft-decision-1 tree_hard | +0.201 [+0.148, +0.253] | 7.92e-13 |
| microsoft-decision-1 flat vs microsoft-decision-1 tree_v2 | +0.013 [-0.037, +0.063] | 0.679 |
| microsoft-decision-1 flat vs elephant-1 flat | -0.066 [-0.114, -0.015] | 0.0133 |
| microsoft-decision-1 flat vs elephant-1 tree | +0.111 [+0.046, +0.179] | 0.00142 |
| microsoft-decision-1 flat vs elephant-1 tree_hard | +0.070 [+0.007, +0.133] | 0.033 |
| microsoft-decision-1 flat vs elephant-1 tree_v2 | +0.000 [-0.059, +0.061] | 1 |
| microsoft-decision-1 flat vs mammoth-1 flat | -0.072 [-0.120, -0.024] | 0.00465 |
| microsoft-decision-1 flat vs mammoth-1 tree | +0.100 [+0.037, +0.166] | 0.00318 |
| microsoft-decision-1 flat vs mammoth-1 tree_hard | +0.061 [+0.002, +0.120] | 0.0547 |
| microsoft-decision-1 flat vs mammoth-1 tree_v2 | +0.000 [-0.057, +0.059] | 1 |
| microsoft-decision-1 flat vs scaledown-classify-1 flat | +0.081 [+0.022, +0.142] | 0.0105 |
| microsoft-decision-1 flat vs scaledown-classify-1 tree | +0.210 [+0.140, +0.282] | 1.61e-08 |
| microsoft-decision-1 flat vs scaledown-classify-1 tree_hard | +0.249 [+0.190, +0.310] | 1.51e-14 |
| microsoft-decision-1 flat vs scaledown-classify-1 tree_v2 | +0.188 [+0.120, +0.258] | 2.78e-07 |
| microsoft-decision-1 flat vs gemini-2.5-flash paper_llm | -0.026 [-0.072, +0.022] | 0.315 |
| microsoft-decision-1 flat vs gemini-2.5-flash paper_llm_thinking | +0.000 [-0.044, +0.046] | 1 |
| microsoft-decision-1 flat vs gemini-3.8-flash paper_llm_low | -0.109 [-0.155, -0.063] | 6.91e-06 |
| microsoft-decision-1 flat vs gemini-3.8-flash paper_llm_thinking | -0.085 [-0.131, -0.039] | 0.000556 |
| microsoft-decision-1 tree vs microsoft-decision-1 tree_hard | +0.033 [+0.011, +0.055] | 0.00592 |
| microsoft-decision-1 tree vs microsoft-decision-1 tree_v2 | -0.155 [-0.205, -0.107] | 2.25e-09 |
| microsoft-decision-1 tree vs elephant-1 flat | -0.234 [-0.286, -0.181] | 1.73e-16 |
| microsoft-decision-1 tree vs elephant-1 tree | -0.057 [-0.098, -0.015] | 0.00955 |
| microsoft-decision-1 tree vs elephant-1 tree_hard | -0.098 [-0.140, -0.057] | 5.46e-06 |
| microsoft-decision-1 tree vs elephant-1 tree_v2 | -0.168 [-0.221, -0.114] | 4.22e-09 |
| microsoft-decision-1 tree vs mammoth-1 flat | -0.240 [-0.299, -0.181] | 1.03e-13 |
| microsoft-decision-1 tree vs mammoth-1 tree | -0.068 [-0.116, -0.017] | 0.00956 |
| microsoft-decision-1 tree vs mammoth-1 tree_hard | -0.107 [-0.157, -0.055] | 9.18e-05 |
| microsoft-decision-1 tree vs mammoth-1 tree_v2 | -0.168 [-0.225, -0.109] | 5.77e-08 |
| microsoft-decision-1 tree vs scaledown-classify-1 flat | -0.087 [-0.144, -0.033] | 0.00267 |
| microsoft-decision-1 tree vs scaledown-classify-1 tree | +0.041 [-0.009, +0.094] | 0.137 |
| microsoft-decision-1 tree vs scaledown-classify-1 tree_hard | +0.081 [+0.033, +0.129] | 0.00143 |
| microsoft-decision-1 tree vs scaledown-classify-1 tree_v2 | +0.020 [-0.035, +0.076] | 0.543 |
| microsoft-decision-1 tree vs gemini-2.5-flash paper_llm | -0.194 [-0.251, -0.135] | 5.21e-10 |
| microsoft-decision-1 tree vs gemini-2.5-flash paper_llm_thinking | -0.168 [-0.227, -0.109] | 7.88e-08 |
| microsoft-decision-1 tree vs gemini-3.8-flash paper_llm_low | -0.277 [-0.332, -0.223] | 3.35e-21 |
| microsoft-decision-1 tree vs gemini-3.8-flash paper_llm_thinking | -0.253 [-0.308, -0.197] | 3.38e-17 |
| microsoft-decision-1 tree_hard vs microsoft-decision-1 tree_v2 | -0.188 [-0.240, -0.135] | 1.44e-11 |
| microsoft-decision-1 tree_hard vs elephant-1 flat | -0.266 [-0.321, -0.212] | 5.22e-19 |
| microsoft-decision-1 tree_hard vs elephant-1 tree | -0.090 [-0.135, -0.044] | 0.000244 |
| microsoft-decision-1 tree_hard vs elephant-1 tree_hard | -0.131 [-0.175, -0.085] | 2.09e-08 |
| microsoft-decision-1 tree_hard vs elephant-1 tree_v2 | -0.201 [-0.258, -0.144] | 4.47e-11 |
| microsoft-decision-1 tree_hard vs mammoth-1 flat | -0.273 [-0.332, -0.214] | 7.75e-17 |
| microsoft-decision-1 tree_hard vs mammoth-1 tree | -0.100 [-0.151, -0.048] | 0.000287 |
| microsoft-decision-1 tree_hard vs mammoth-1 tree_hard | -0.140 [-0.194, -0.085] | 1.19e-06 |
| microsoft-decision-1 tree_hard vs mammoth-1 tree_v2 | -0.201 [-0.260, -0.142] | 3.94e-10 |
| microsoft-decision-1 tree_hard vs scaledown-classify-1 flat | -0.120 [-0.177, -0.063] | 5.82e-05 |
| microsoft-decision-1 tree_hard vs scaledown-classify-1 tree | +0.009 [-0.046, +0.066] | 0.819 |
| microsoft-decision-1 tree_hard vs scaledown-classify-1 tree_hard | +0.048 [+0.000, +0.096] | 0.0589 |
| microsoft-decision-1 tree_hard vs scaledown-classify-1 tree_v2 | -0.013 [-0.072, +0.046] | 0.721 |
| microsoft-decision-1 tree_hard vs gemini-2.5-flash paper_llm | -0.227 [-0.284, -0.170] | 1.61e-13 |
| microsoft-decision-1 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.201 [-0.255, -0.146] | 2.11e-11 |
| microsoft-decision-1 tree_hard vs gemini-3.8-flash paper_llm_low | -0.310 [-0.362, -0.255] | 1.07e-25 |
| microsoft-decision-1 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.286 [-0.341, -0.231] | 1.34e-21 |
| microsoft-decision-1 tree_v2 vs elephant-1 flat | -0.079 [-0.131, -0.026] | 0.00491 |
| microsoft-decision-1 tree_v2 vs elephant-1 tree | +0.098 [+0.039, +0.159] | 0.00174 |
| microsoft-decision-1 tree_v2 vs elephant-1 tree_hard | +0.057 [+0.000, +0.116] | 0.0694 |
| microsoft-decision-1 tree_v2 vs elephant-1 tree_v2 | -0.013 [-0.061, +0.037] | 0.661 |
| microsoft-decision-1 tree_v2 vs mammoth-1 flat | -0.085 [-0.138, -0.033] | 0.00202 |
| microsoft-decision-1 tree_v2 vs mammoth-1 tree | +0.087 [+0.028, +0.148] | 0.00544 |
| microsoft-decision-1 tree_v2 vs mammoth-1 tree_hard | +0.048 [-0.009, +0.107] | 0.125 |
| microsoft-decision-1 tree_v2 vs mammoth-1 tree_v2 | -0.013 [-0.063, +0.039] | 0.683 |
| microsoft-decision-1 tree_v2 vs scaledown-classify-1 flat | +0.068 [+0.011, +0.122] | 0.0215 |
| microsoft-decision-1 tree_v2 vs scaledown-classify-1 tree | +0.197 [+0.135, +0.258] | 1.4e-09 |
| microsoft-decision-1 tree_v2 vs scaledown-classify-1 tree_hard | +0.236 [+0.177, +0.295] | 2.29e-13 |
| microsoft-decision-1 tree_v2 vs scaledown-classify-1 tree_v2 | +0.175 [+0.116, +0.234] | 2.12e-08 |
| microsoft-decision-1 tree_v2 vs gemini-2.5-flash paper_llm | -0.039 [-0.094, +0.015] | 0.179 |
| microsoft-decision-1 tree_v2 vs gemini-2.5-flash paper_llm_thinking | -0.013 [-0.066, +0.039] | 0.683 |
| microsoft-decision-1 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.122 [-0.175, -0.070] | 9.9e-06 |
| microsoft-decision-1 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.098 [-0.151, -0.044] | 0.000528 |
| elephant-1 flat vs elephant-1 tree | +0.177 [+0.127, +0.227] | 1.22e-11 |
| elephant-1 flat vs elephant-1 tree_hard | +0.135 [+0.087, +0.183] | 1.03e-07 |
| elephant-1 flat vs elephant-1 tree_v2 | +0.066 [+0.024, +0.105] | 0.00231 |
| elephant-1 flat vs mammoth-1 flat | -0.007 [-0.044, +0.028] | 0.813 |
| elephant-1 flat vs mammoth-1 tree | +0.166 [+0.118, +0.214] | 3.82e-11 |
| elephant-1 flat vs mammoth-1 tree_hard | +0.127 [+0.085, +0.170] | 1.34e-08 |
| elephant-1 flat vs mammoth-1 tree_v2 | +0.066 [+0.024, +0.107] | 0.00288 |
| elephant-1 flat vs scaledown-classify-1 flat | +0.146 [+0.092, +0.199] | 1.59e-07 |
| elephant-1 flat vs scaledown-classify-1 tree | +0.275 [+0.223, +0.330] | 3.16e-21 |
| elephant-1 flat vs scaledown-classify-1 tree_hard | +0.314 [+0.258, +0.369] | 5.63e-24 |
| elephant-1 flat vs scaledown-classify-1 tree_v2 | +0.253 [+0.203, +0.306] | 9.39e-20 |
| elephant-1 flat vs gemini-2.5-flash paper_llm | +0.039 [-0.009, +0.087] | 0.13 |
| elephant-1 flat vs gemini-2.5-flash paper_llm_thinking | +0.066 [+0.013, +0.118] | 0.0192 |
| elephant-1 flat vs gemini-3.8-flash paper_llm_low | -0.044 [-0.083, -0.004] | 0.0422 |
| elephant-1 flat vs gemini-3.8-flash paper_llm_thinking | -0.020 [-0.061, +0.022] | 0.402 |
| elephant-1 tree vs elephant-1 tree_hard | -0.041 [-0.072, -0.011] | 0.011 |
| elephant-1 tree vs elephant-1 tree_v2 | -0.111 [-0.148, -0.074] | 1.39e-08 |
| elephant-1 tree vs mammoth-1 flat | -0.183 [-0.238, -0.129] | 3.73e-10 |
| elephant-1 tree vs mammoth-1 tree | -0.011 [-0.041, +0.022] | 0.59 |
| elephant-1 tree vs mammoth-1 tree_hard | -0.050 [-0.090, -0.011] | 0.0178 |
| elephant-1 tree vs mammoth-1 tree_v2 | -0.111 [-0.157, -0.066] | 5.83e-06 |
| elephant-1 tree vs scaledown-classify-1 flat | -0.031 [-0.085, +0.024] | 0.313 |
| elephant-1 tree vs scaledown-classify-1 tree | +0.098 [+0.063, +0.133] | 6.27e-08 |
| elephant-1 tree vs scaledown-classify-1 tree_hard | +0.138 [+0.090, +0.186] | 8.82e-08 |
| elephant-1 tree vs scaledown-classify-1 tree_v2 | +0.076 [+0.037, +0.116] | 0.000266 |
| elephant-1 tree vs gemini-2.5-flash paper_llm | -0.138 [-0.197, -0.076] | 1.56e-05 |
| elephant-1 tree vs gemini-2.5-flash paper_llm_thinking | -0.111 [-0.177, -0.046] | 0.00142 |
| elephant-1 tree vs gemini-3.8-flash paper_llm_low | -0.221 [-0.277, -0.166] | 1.2e-13 |
| elephant-1 tree vs gemini-3.8-flash paper_llm_thinking | -0.197 [-0.253, -0.140] | 9.64e-11 |
| elephant-1 tree_hard vs elephant-1 tree_v2 | -0.070 [-0.114, -0.026] | 0.00268 |
| elephant-1 tree_hard vs mammoth-1 flat | -0.142 [-0.197, -0.087] | 8.57e-07 |
| elephant-1 tree_hard vs mammoth-1 tree | +0.031 [-0.007, +0.068] | 0.146 |
| elephant-1 tree_hard vs mammoth-1 tree_hard | -0.009 [-0.050, +0.033] | 0.76 |
| elephant-1 tree_hard vs mammoth-1 tree_v2 | -0.070 [-0.116, -0.022] | 0.00593 |
| elephant-1 tree_hard vs scaledown-classify-1 flat | +0.011 [-0.044, +0.066] | 0.754 |
| elephant-1 tree_hard vs scaledown-classify-1 tree | +0.140 [+0.096, +0.183] | 2.69e-09 |
| elephant-1 tree_hard vs scaledown-classify-1 tree_hard | +0.179 [+0.129, +0.231] | 1.58e-11 |
| elephant-1 tree_hard vs scaledown-classify-1 tree_v2 | +0.118 [+0.070, +0.166] | 4.17e-06 |
| elephant-1 tree_hard vs gemini-2.5-flash paper_llm | -0.096 [-0.153, -0.039] | 0.00146 |
| elephant-1 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.070 [-0.133, -0.007] | 0.0381 |
| elephant-1 tree_hard vs gemini-3.8-flash paper_llm_low | -0.179 [-0.234, -0.124] | 3.03e-10 |
| elephant-1 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.155 [-0.210, -0.098] | 1.37e-07 |
| elephant-1 tree_v2 vs mammoth-1 flat | -0.072 [-0.120, -0.026] | 0.00373 |
| elephant-1 tree_v2 vs mammoth-1 tree | +0.100 [+0.061, +0.140] | 9.2e-07 |
| elephant-1 tree_v2 vs mammoth-1 tree_hard | +0.061 [+0.020, +0.103] | 0.00508 |
| elephant-1 tree_v2 vs mammoth-1 tree_v2 | +0.000 [-0.031, +0.031] | 1 |
| elephant-1 tree_v2 vs scaledown-classify-1 flat | +0.081 [+0.028, +0.133] | 0.00326 |
| elephant-1 tree_v2 vs scaledown-classify-1 tree | +0.210 [+0.166, +0.255] | 6.38e-19 |
| elephant-1 tree_v2 vs scaledown-classify-1 tree_hard | +0.249 [+0.192, +0.306] | 8.53e-17 |
| elephant-1 tree_v2 vs scaledown-classify-1 tree_v2 | +0.188 [+0.146, +0.229] | 6.16e-18 |
| elephant-1 tree_v2 vs gemini-2.5-flash paper_llm | -0.026 [-0.081, +0.031] | 0.393 |
| elephant-1 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.000 [-0.059, +0.059] | 1 |
| elephant-1 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.109 [-0.159, -0.059] | 3.76e-05 |
| elephant-1 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.085 [-0.135, -0.035] | 0.00176 |
| mammoth-1 flat vs mammoth-1 tree | +0.172 [+0.122, +0.225] | 2.64e-10 |
| mammoth-1 flat vs mammoth-1 tree_hard | +0.133 [+0.090, +0.179] | 1.86e-08 |
| mammoth-1 flat vs mammoth-1 tree_v2 | +0.072 [+0.031, +0.116] | 0.00184 |
| mammoth-1 flat vs scaledown-classify-1 flat | +0.153 [+0.100, +0.205] | 4.5e-08 |
| mammoth-1 flat vs scaledown-classify-1 tree | +0.282 [+0.227, +0.338] | 7.33e-20 |
| mammoth-1 flat vs scaledown-classify-1 tree_hard | +0.321 [+0.262, +0.378] | 1.33e-22 |
| mammoth-1 flat vs scaledown-classify-1 tree_v2 | +0.260 [+0.207, +0.314] | 1.38e-18 |
| mammoth-1 flat vs gemini-2.5-flash paper_llm | +0.046 [+0.000, +0.092] | 0.0663 |
| mammoth-1 flat vs gemini-2.5-flash paper_llm_thinking | +0.072 [+0.022, +0.122] | 0.00724 |
| mammoth-1 flat vs gemini-3.8-flash paper_llm_low | -0.037 [-0.074, +0.000] | 0.0675 |
| mammoth-1 flat vs gemini-3.8-flash paper_llm_thinking | -0.013 [-0.052, +0.026] | 0.59 |
| mammoth-1 tree vs mammoth-1 tree_hard | -0.039 [-0.070, -0.011] | 0.0133 |
| mammoth-1 tree vs mammoth-1 tree_v2 | -0.100 [-0.135, -0.066] | 6.22e-08 |
| mammoth-1 tree vs scaledown-classify-1 flat | -0.020 [-0.072, +0.033] | 0.518 |
| mammoth-1 tree vs scaledown-classify-1 tree | +0.109 [+0.072, +0.146] | 8.58e-09 |
| mammoth-1 tree vs scaledown-classify-1 tree_hard | +0.148 [+0.096, +0.203] | 1.35e-07 |
| mammoth-1 tree vs scaledown-classify-1 tree_v2 | +0.087 [+0.048, +0.127] | 1.88e-05 |
| mammoth-1 tree vs gemini-2.5-flash paper_llm | -0.127 [-0.183, -0.070] | 3.11e-05 |
| mammoth-1 tree vs gemini-2.5-flash paper_llm_thinking | -0.100 [-0.166, -0.037] | 0.00305 |
| mammoth-1 tree vs gemini-3.8-flash paper_llm_low | -0.210 [-0.262, -0.159] | 2.98e-14 |
| mammoth-1 tree vs gemini-3.8-flash paper_llm_thinking | -0.186 [-0.240, -0.133] | 5.3e-11 |
| mammoth-1 tree_hard vs mammoth-1 tree_v2 | -0.061 [-0.096, -0.026] | 0.000914 |
| mammoth-1 tree_hard vs scaledown-classify-1 flat | +0.020 [-0.031, +0.072] | 0.51 |
| mammoth-1 tree_hard vs scaledown-classify-1 tree | +0.148 [+0.103, +0.194] | 4.56e-10 |
| mammoth-1 tree_hard vs scaledown-classify-1 tree_hard | +0.188 [+0.133, +0.245] | 1.72e-10 |
| mammoth-1 tree_hard vs scaledown-classify-1 tree_v2 | +0.127 [+0.081, +0.172] | 1.45e-07 |
| mammoth-1 tree_hard vs gemini-2.5-flash paper_llm | -0.087 [-0.140, -0.035] | 0.0017 |
| mammoth-1 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.061 [-0.120, +0.000] | 0.0584 |
| mammoth-1 tree_hard vs gemini-3.8-flash paper_llm_low | -0.170 [-0.216, -0.124] | 1.93e-12 |
| mammoth-1 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.146 [-0.197, -0.100] | 6.6e-09 |
| mammoth-1 tree_v2 vs scaledown-classify-1 flat | +0.081 [+0.031, +0.131] | 0.00249 |
| mammoth-1 tree_v2 vs scaledown-classify-1 tree | +0.210 [+0.164, +0.255] | 2.38e-17 |
| mammoth-1 tree_v2 vs scaledown-classify-1 tree_hard | +0.249 [+0.190, +0.308] | 2.34e-15 |
| mammoth-1 tree_v2 vs scaledown-classify-1 tree_v2 | +0.188 [+0.144, +0.231] | 6.78e-16 |
| mammoth-1 tree_v2 vs gemini-2.5-flash paper_llm | -0.026 [-0.079, +0.026] | 0.379 |
| mammoth-1 tree_v2 vs gemini-2.5-flash paper_llm_thinking | +0.000 [-0.059, +0.059] | 1 |
| mammoth-1 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.109 [-0.157, -0.061] | 1.87e-05 |
| mammoth-1 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.085 [-0.133, -0.037] | 0.000999 |
| scaledown-classify-1 flat vs scaledown-classify-1 tree | +0.129 [+0.072, +0.183] | 9.69e-06 |
| scaledown-classify-1 flat vs scaledown-classify-1 tree_hard | +0.168 [+0.111, +0.225] | 2.08e-08 |
| scaledown-classify-1 flat vs scaledown-classify-1 tree_v2 | +0.107 [+0.052, +0.162] | 0.000202 |
| scaledown-classify-1 flat vs gemini-2.5-flash paper_llm | -0.107 [-0.164, -0.050] | 0.000285 |
| scaledown-classify-1 flat vs gemini-2.5-flash paper_llm_thinking | -0.081 [-0.140, -0.024] | 0.00865 |
| scaledown-classify-1 flat vs gemini-3.8-flash paper_llm_low | -0.190 [-0.242, -0.138] | 1.29e-11 |
| scaledown-classify-1 flat vs gemini-3.8-flash paper_llm_thinking | -0.166 [-0.221, -0.111] | 7.59e-09 |
| scaledown-classify-1 tree vs scaledown-classify-1 tree_hard | +0.039 [-0.013, +0.090] | 0.162 |
| scaledown-classify-1 tree vs scaledown-classify-1 tree_v2 | -0.022 [-0.046, +0.002] | 0.0987 |
| scaledown-classify-1 tree vs gemini-2.5-flash paper_llm | -0.236 [-0.299, -0.172] | 2.1e-12 |
| scaledown-classify-1 tree vs gemini-2.5-flash paper_llm_thinking | -0.210 [-0.279, -0.142] | 9.9e-09 |
| scaledown-classify-1 tree vs gemini-3.8-flash paper_llm_low | -0.319 [-0.378, -0.260] | 5.05e-23 |
| scaledown-classify-1 tree vs gemini-3.8-flash paper_llm_thinking | -0.295 [-0.354, -0.236] | 9.32e-20 |
| scaledown-classify-1 tree_hard vs scaledown-classify-1 tree_v2 | -0.061 [-0.116, -0.004] | 0.0404 |
| scaledown-classify-1 tree_hard vs gemini-2.5-flash paper_llm | -0.275 [-0.334, -0.216] | 2.6e-18 |
| scaledown-classify-1 tree_hard vs gemini-2.5-flash paper_llm_thinking | -0.249 [-0.310, -0.188] | 6.07e-14 |
| scaledown-classify-1 tree_hard vs gemini-3.8-flash paper_llm_low | -0.358 [-0.415, -0.301] | 9.44e-29 |
| scaledown-classify-1 tree_hard vs gemini-3.8-flash paper_llm_thinking | -0.334 [-0.391, -0.275] | 3.16e-25 |
| scaledown-classify-1 tree_v2 vs gemini-2.5-flash paper_llm | -0.214 [-0.275, -0.153] | 8.3e-11 |
| scaledown-classify-1 tree_v2 vs gemini-2.5-flash paper_llm_thinking | -0.188 [-0.255, -0.122] | 1.32e-07 |
| scaledown-classify-1 tree_v2 vs gemini-3.8-flash paper_llm_low | -0.297 [-0.356, -0.240] | 4.03e-21 |
| scaledown-classify-1 tree_v2 vs gemini-3.8-flash paper_llm_thinking | -0.273 [-0.332, -0.216] | 4.11e-18 |
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

**pplx-decider-flash-v1.2 flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 119 | 19 | 2 | 18 | 3 |
| Comp | 36 | 65 | 4 | 9 | 1 |
| Opin | 19 | 33 | 59 | 1 | 3 |
| Outd | 21 | 6 | 0 | 35 | 0 |
| Misi | 4 | 0 | 0 | 1 | 0 |

**pplx-decider-flash-v1.2 tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 141 | 9 | 0 | 2 | 9 |
| Comp | 53 | 56 | 0 | 2 | 4 |
| Opin | 55 | 58 | 0 | 0 | 2 |
| Outd | 33 | 11 | 0 | 15 | 3 |
| Misi | 4 | 0 | 0 | 0 | 1 |

**pplx-decider-flash-v1.2 tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 123 | 10 | 1 | 11 | 16 |
| Comp | 45 | 63 | 0 | 3 | 4 |
| Opin | 39 | 61 | 5 | 0 | 10 |
| Outd | 23 | 7 | 0 | 27 | 5 |
| Misi | 4 | 0 | 0 | 0 | 1 |

**pplx-decider-flash-v1.2 tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 139 | 6 | 2 | 9 | 5 |
| Comp | 54 | 50 | 5 | 3 | 3 |
| Opin | 54 | 3 | 57 | 0 | 1 |
| Outd | 32 | 7 | 2 | 20 | 1 |
| Misi | 4 | 0 | 0 | 1 | 0 |

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

**d1-ultra flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 122 | 5 | 9 | 22 | 3 |
| Comp | 35 | 50 | 11 | 17 | 2 |
| Opin | 14 | 6 | 87 | 3 | 5 |
| Outd | 14 | 1 | 0 | 47 | 0 |
| Misi | 4 | 0 | 0 | 1 | 0 |

**d1-ultra tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 147 | 8 | 0 | 2 | 4 |
| Comp | 57 | 55 | 1 | 0 | 2 |
| Opin | 37 | 51 | 16 | 1 | 10 |
| Outd | 36 | 14 | 0 | 11 | 1 |
| Misi | 4 | 0 | 0 | 1 | 0 |

**d1-ultra tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 130 | 11 | 0 | 8 | 12 |
| Comp | 39 | 68 | 1 | 2 | 5 |
| Opin | 19 | 46 | 28 | 2 | 20 |
| Outd | 20 | 12 | 0 | 28 | 2 |
| Misi | 3 | 1 | 0 | 1 | 0 |

**d1-ultra tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 146 | 6 | 3 | 3 | 3 |
| Comp | 62 | 42 | 7 | 1 | 3 |
| Opin | 38 | 2 | 74 | 0 | 1 |
| Outd | 34 | 6 | 2 | 19 | 1 |
| Misi | 4 | 0 | 0 | 1 | 0 |

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

**elephant-1 flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 134 | 8 | 2 | 17 | 0 |
| Comp | 38 | 62 | 7 | 7 | 1 |
| Opin | 23 | 23 | 64 | 1 | 4 |
| Outd | 26 | 0 | 0 | 36 | 0 |
| Misi | 4 | 0 | 0 | 1 | 0 |

**elephant-1 tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 150 | 7 | 0 | 1 | 3 |
| Comp | 53 | 61 | 0 | 0 | 1 |
| Opin | 61 | 52 | 1 | 0 | 1 |
| Outd | 39 | 19 | 0 | 3 | 1 |
| Misi | 5 | 0 | 0 | 0 | 0 |

**elephant-1 tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 134 | 11 | 0 | 7 | 9 |
| Comp | 42 | 72 | 0 | 0 | 1 |
| Opin | 35 | 62 | 11 | 0 | 7 |
| Outd | 25 | 19 | 0 | 15 | 3 |
| Misi | 3 | 0 | 0 | 0 | 2 |

**elephant-1 tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 151 | 5 | 1 | 2 | 2 |
| Comp | 58 | 46 | 10 | 0 | 1 |
| Opin | 51 | 2 | 62 | 0 | 0 |
| Outd | 39 | 12 | 3 | 7 | 1 |
| Misi | 5 | 0 | 0 | 0 | 0 |

**mammoth-1 flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 127 | 0 | 7 | 20 | 7 |
| Comp | 39 | 45 | 9 | 17 | 5 |
| Opin | 20 | 3 | 83 | 0 | 9 |
| Outd | 18 | 0 | 0 | 44 | 0 |
| Misi | 4 | 0 | 0 | 1 | 0 |

**mammoth-1 tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 149 | 8 | 0 | 2 | 2 |
| Comp | 63 | 46 | 1 | 0 | 5 |
| Opin | 63 | 26 | 17 | 1 | 8 |
| Outd | 39 | 14 | 0 | 8 | 1 |
| Misi | 4 | 0 | 0 | 1 | 0 |

**mammoth-1 tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 137 | 7 | 1 | 7 | 9 |
| Comp | 55 | 47 | 1 | 6 | 6 |
| Opin | 39 | 22 | 32 | 2 | 20 |
| Outd | 24 | 10 | 0 | 22 | 6 |
| Misi | 4 | 0 | 0 | 1 | 0 |

**mammoth-1 tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 146 | 5 | 2 | 6 | 2 |
| Comp | 63 | 36 | 9 | 4 | 3 |
| Opin | 49 | 0 | 66 | 0 | 0 |
| Outd | 34 | 9 | 1 | 18 | 0 |
| Misi | 4 | 0 | 0 | 1 | 0 |

**scaledown-classify-1 flat**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 104 | 35 | 11 | 7 | 4 |
| Comp | 36 | 59 | 9 | 7 | 4 |
| Opin | 8 | 49 | 54 | 1 | 3 |
| Outd | 26 | 18 | 6 | 12 | 0 |
| Misi | 5 | 0 | 0 | 0 | 0 |

**scaledown-classify-1 tree**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 155 | 6 | 0 | 0 | 0 |
| Comp | 100 | 15 | 0 | 0 | 0 |
| Opin | 99 | 16 | 0 | 0 | 0 |
| Outd | 49 | 13 | 0 | 0 | 0 |
| Misi | 5 | 0 | 0 | 0 | 0 |

**scaledown-classify-1 tree_hard**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 72 | 75 | 3 | 8 | 3 |
| Comp | 41 | 66 | 1 | 5 | 2 |
| Opin | 33 | 67 | 10 | 3 | 2 |
| Outd | 10 | 48 | 0 | 4 | 0 |
| Misi | 0 | 5 | 0 | 0 | 0 |

**scaledown-classify-1 tree_v2**

| gold \ pred | NC | Comp | Opin | Outd | Misi |
|---|---|---|---|---|---|
| NC | 158 | 3 | 0 | 0 | 0 |
| Comp | 110 | 5 | 0 | 0 | 0 |
| Opin | 97 | 1 | 17 | 0 | 0 |
| Outd | 54 | 7 | 1 | 0 | 0 |
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
