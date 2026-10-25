# Diagnostics on CONFLICTS, split `test`

Each perturbed run is compared with the same system's original run on the same queries. Flip rate = share of queries whose predicted type changed. TV = mean total-variation distance between probability vectors (probabilistic systems only). Protocol in NOTES.md.

## jev-1.13.0 flat

| Perturbation | n | Acc. original → perturbed | Δ [95% CI] | McNemar p | Flip rate | TV | Outdated recall orig → pert | Outdated F1 orig → pert |
|---|---|---|---|---|---|---|---|---|
| rerun | 406 | 0.618 → 0.613 | -0.005 [-0.017, +0.007] | 0.688 | 0.020 | 0.027 | 0.727 → 0.745 | 0.650 → 0.667 |
| no_dates | 406 | 0.618 → 0.608 | -0.010 [-0.025, +0.005] | 0.344 | 0.030 | 0.031 | 0.727 → 0.745 | 0.650 → 0.661 |
| dates_in_code | 406 | 0.618 → 0.621 | +0.002 [-0.012, +0.017] | 1 | 0.034 | 0.034 | 0.727 → 0.764 | 0.650 → 0.651 |
| shuffle1 | 406 | 0.618 → 0.633 | +0.015 [-0.012, +0.042] | 0.377 | 0.111 | 0.099 | 0.727 → 0.727 | 0.650 → 0.650 |
| shuffle2 | 406 | 0.618 → 0.621 | +0.002 [-0.027, +0.032] | 1 | 0.121 | 0.103 | 0.727 → 0.673 | 0.650 → 0.627 |

Planted false source (n = 96 No-conflict queries; expected label Misinformation):

| | Original | Planted |
|---|---|---|
| Predicted Misinformation | 0.177 | 0.667 |
| Predicted any conflict (not No conflict) | 0.417 | 0.854 |
| Predicted Outdated | 0.125 | 0.135 |
| Mean P(Misinformation) | 0.212 | 0.594 |
| Mean P(No conflict) | 0.487 | 0.170 |

## jev-1.13.0 tree

| Perturbation | n | Acc. original → perturbed | Δ [95% CI] | McNemar p | Flip rate | TV | Outdated recall orig → pert | Outdated F1 orig → pert |
|---|---|---|---|---|---|---|---|---|
| rerun | 406 | 0.473 → 0.473 | +0.000 [-0.010, +0.010] | 1 | 0.015 | 0.018 | 0.055 → 0.036 | 0.102 → 0.070 |
| no_dates | 406 | 0.473 → 0.466 | -0.007 [-0.017, +0.002] | 0.375 | 0.020 | 0.019 | 0.055 → 0.055 | 0.102 → 0.102 |
| dates_in_code | 406 | 0.473 → 0.470 | -0.002 [-0.012, +0.007] | 1 | 0.022 | 0.021 | 0.055 → 0.055 | 0.102 → 0.102 |
| shuffle1 | 406 | 0.473 → 0.463 | -0.010 [-0.032, +0.012] | 0.523 | 0.069 | 0.062 | 0.055 → 0.018 | 0.102 → 0.035 |
| shuffle2 | 406 | 0.473 → 0.451 | -0.022 [-0.042, -0.005] | 0.0352 | 0.064 | 0.060 | 0.055 → 0.036 | 0.102 → 0.070 |

Planted false source (n = 96 No-conflict queries; expected label Misinformation):

| | Original | Planted |
|---|---|---|
| Predicted Misinformation | 0.031 | 0.365 |
| Predicted any conflict (not No conflict) | 0.250 | 0.677 |
| Predicted Outdated | 0.010 | 0.010 |
| Mean P(Misinformation) | 0.109 | 0.250 |
| Mean P(No conflict) | 0.599 | 0.320 |

## jev-1.13.0 tree_v2

| Perturbation | n | Acc. original → perturbed | Δ [95% CI] | McNemar p | Flip rate | TV | Outdated recall orig → pert | Outdated F1 orig → pert |
|---|---|---|---|---|---|---|---|---|
| rerun | 406 | 0.635 → 0.633 | -0.002 [-0.015, +0.010] | 1 | 0.025 | 0.018 | 0.200 → 0.200 | 0.310 → 0.306 |
| no_dates | 406 | 0.635 → 0.635 | +0.000 [-0.012, +0.012] | 1 | 0.034 | 0.021 | 0.200 → 0.200 | 0.310 → 0.310 |
| dates_in_code | 406 | 0.635 → 0.638 | +0.002 [-0.012, +0.017] | 1 | 0.037 | 0.023 | 0.200 → 0.218 | 0.310 → 0.338 |
| shuffle1 | 406 | 0.635 → 0.621 | -0.015 [-0.039, +0.010] | 0.327 | 0.099 | 0.068 | 0.200 → 0.182 | 0.310 → 0.282 |
| shuffle2 | 406 | 0.635 → 0.613 | -0.022 [-0.047, +0.002] | 0.108 | 0.084 | 0.066 | 0.200 → 0.182 | 0.310 → 0.290 |

Planted false source (n = 96 No-conflict queries; expected label Misinformation):

| | Original | Planted |
|---|---|---|
| Predicted Misinformation | 0.021 | 0.198 |
| Predicted any conflict (not No conflict) | 0.250 | 0.677 |
| Predicted Outdated | 0.042 | 0.156 |
| Mean P(Misinformation) | 0.086 | 0.177 |
| Mean P(No conflict) | 0.599 | 0.320 |

## gemini-3.8-flash paper_llm_low

| Perturbation | n | Acc. original → perturbed | Δ [95% CI] | McNemar p | Flip rate | TV | Outdated recall orig → pert | Outdated F1 orig → pert |
|---|---|---|---|---|---|---|---|---|
| rerun | 406 | 0.700 → 0.712 | +0.012 [-0.005, +0.030] | 0.267 | 0.034 | – | 0.691 → 0.727 | 0.661 → 0.690 |
| no_dates | 406 | 0.700 → 0.692 | -0.007 [-0.022, +0.007] | 0.508 | 0.027 | – | 0.691 → 0.673 | 0.661 → 0.649 |
| dates_in_code | 406 | 0.700 → 0.692 | -0.007 [-0.027, +0.015] | 0.648 | 0.057 | – | 0.691 → 0.727 | 0.661 → 0.684 |
| shuffle1 | 406 | 0.700 → 0.695 | -0.005 [-0.030, +0.020] | 0.851 | 0.084 | – | 0.691 → 0.745 | 0.661 → 0.683 |
| shuffle2 | 406 | 0.700 → 0.672 | -0.027 [-0.054, +0.002] | 0.0895 | 0.103 | – | 0.691 → 0.709 | 0.661 → 0.655 |

Planted false source (n = 96 No-conflict queries; expected label Misinformation):

| | Original | Planted |
|---|---|---|
| Predicted Misinformation | 0.031 | 0.521 |
| Predicted any conflict (not No conflict) | 0.250 | 0.719 |
| Predicted Outdated | 0.125 | 0.135 |
