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

## jev-1.14.0 flat

| Perturbation | n | Acc. original → perturbed | Δ [95% CI] | McNemar p | Flip rate | TV | Outdated recall orig → pert | Outdated F1 orig → pert |
|---|---|---|---|---|---|---|---|---|
| rerun | 406 | 0.596 → 0.603 | +0.007 [-0.007, +0.022] | 0.508 | 0.030 | 0.028 | 0.764 → 0.782 | 0.613 → 0.637 |
| no_dates | 406 | 0.596 → 0.596 | +0.000 [-0.012, +0.012] | 1 | 0.030 | 0.029 | 0.764 → 0.764 | 0.613 → 0.618 |
| dates_in_code | 406 | 0.596 → 0.606 | +0.010 [-0.007, +0.027] | 0.388 | 0.037 | 0.032 | 0.764 → 0.800 | 0.613 → 0.629 |
| shuffle1 | 406 | 0.596 → 0.606 | +0.010 [-0.017, +0.037] | 0.597 | 0.113 | 0.089 | 0.764 → 0.818 | 0.613 → 0.647 |
| shuffle2 | 406 | 0.596 → 0.596 | +0.000 [-0.025, +0.025] | 1 | 0.103 | 0.094 | 0.764 → 0.800 | 0.613 → 0.652 |

Planted false source (n = 96 No-conflict queries; expected label Misinformation):

| | Original | Planted |
|---|---|---|
| Predicted Misinformation | 0.219 | 0.646 |
| Predicted any conflict (not No conflict) | 0.510 | 0.854 |
| Predicted Outdated | 0.208 | 0.167 |
| Mean P(Misinformation) | 0.247 | 0.598 |
| Mean P(No conflict) | 0.434 | 0.143 |

## pplx-decider-v1.2 flat

| Perturbation | n | Acc. original → perturbed | Δ [95% CI] | McNemar p | Flip rate | TV | Outdated recall orig → pert | Outdated F1 orig → pert |
|---|---|---|---|---|---|---|---|---|
| rerun | 406 | 0.667 → 0.667 | +0.000 [+0.000, +0.000] | 1 | 0.000 | 0.000 | 0.782 → 0.782 | 0.672 → 0.672 |
| no_dates | 406 | 0.667 → 0.672 | +0.005 [-0.007, +0.017] | 0.688 | 0.020 | 0.022 | 0.782 → 0.800 | 0.672 → 0.677 |
| dates_in_code | 406 | 0.667 → 0.675 | +0.007 [-0.007, +0.022] | 0.508 | 0.030 | 0.020 | 0.782 → 0.782 | 0.672 → 0.672 |
| shuffle1 | 406 | 0.667 → 0.667 | +0.000 [-0.025, +0.025] | 1 | 0.074 | 0.057 | 0.782 → 0.782 | 0.672 → 0.656 |
| shuffle2 | 406 | 0.667 → 0.667 | +0.000 [-0.025, +0.025] | 1 | 0.067 | 0.059 | 0.782 → 0.800 | 0.672 → 0.677 |

Planted false source (n = 96 No-conflict queries; expected label Misinformation):

| | Original | Planted |
|---|---|---|
| Predicted Misinformation | 0.031 | 0.500 |
| Predicted any conflict (not No conflict) | 0.240 | 0.708 |
| Predicted Outdated | 0.135 | 0.146 |
| Mean P(Misinformation) | 0.065 | 0.416 |
| Mean P(No conflict) | 0.671 | 0.298 |

## pplx-decider-flash-v1.2 flat

| Perturbation | n | Acc. original → perturbed | Δ [95% CI] | McNemar p | Flip rate | TV | Outdated recall orig → pert | Outdated F1 orig → pert |
|---|---|---|---|---|---|---|---|---|
| rerun | 406 | 0.618 → 0.618 | +0.000 [+0.000, +0.000] | 1 | 0.000 | 0.000 | 0.582 → 0.582 | 0.577 → 0.577 |
| no_dates | 406 | 0.618 → 0.618 | +0.000 [-0.017, +0.017] | 1 | 0.037 | 0.030 | 0.582 → 0.618 | 0.577 → 0.602 |
| dates_in_code | 406 | 0.618 → 0.623 | +0.005 [-0.012, +0.022] | 0.791 | 0.042 | 0.024 | 0.582 → 0.636 | 0.577 → 0.603 |
| shuffle1 | 406 | 0.618 → 0.628 | +0.010 [-0.017, +0.037] | 0.597 | 0.103 | 0.079 | 0.582 → 0.600 | 0.577 → 0.589 |
| shuffle2 | 406 | 0.618 → 0.621 | +0.002 [-0.027, +0.032] | 1 | 0.131 | 0.083 | 0.582 → 0.618 | 0.577 → 0.613 |

Planted false source (n = 96 No-conflict queries; expected label Misinformation):

| | Original | Planted |
|---|---|---|
| Predicted Misinformation | 0.010 | 0.250 |
| Predicted any conflict (not No conflict) | 0.250 | 0.573 |
| Predicted Outdated | 0.135 | 0.188 |
| Mean P(Misinformation) | 0.086 | 0.259 |
| Mean P(No conflict) | 0.628 | 0.397 |

## gpt-6-luna-decisions flat

| Perturbation | n | Acc. original → perturbed | Δ [95% CI] | McNemar p | Flip rate | TV | Outdated recall orig → pert | Outdated F1 orig → pert |
|---|---|---|---|---|---|---|---|---|
| rerun | 406 | 0.663 → 0.663 | +0.000 [+0.000, +0.000] | 1 | 0.000 | 0.000 | 0.727 → 0.727 | 0.727 → 0.727 |
| no_dates | 406 | 0.663 → 0.658 | -0.005 [-0.030, +0.020] | 0.845 | 0.071 | 0.076 | 0.727 → 0.745 | 0.727 → 0.739 |
| dates_in_code | 406 | 0.663 → 0.663 | +0.000 [-0.025, +0.025] | 1 | 0.071 | 0.071 | 0.727 → 0.745 | 0.727 → 0.719 |
| shuffle1 | 406 | 0.663 → 0.616 | -0.047 [-0.081, -0.012] | 0.011 | 0.155 | 0.145 | 0.727 → 0.673 | 0.727 → 0.673 |
| shuffle2 | 406 | 0.663 → 0.606 | -0.057 [-0.094, -0.020] | 0.00592 | 0.202 | 0.144 | 0.727 → 0.673 | 0.727 → 0.661 |

Planted false source (n = 96 No-conflict queries; expected label Misinformation):

| | Original | Planted |
|---|---|---|
| Predicted Misinformation | 0.010 | 0.240 |
| Predicted any conflict (not No conflict) | 0.229 | 0.531 |
| Predicted Outdated | 0.104 | 0.167 |
| Mean P(Misinformation) | 0.040 | 0.230 |
| Mean P(No conflict) | 0.612 | 0.384 |

## d1 flat

| Perturbation | n | Acc. original → perturbed | Δ [95% CI] | McNemar p | Flip rate | TV | Outdated recall orig → pert | Outdated F1 orig → pert |
|---|---|---|---|---|---|---|---|---|
| rerun | 406 | 0.626 → 0.635 | +0.010 [-0.017, +0.037] | 0.597 | 0.094 | 0.070 | 0.818 → 0.855 | 0.662 → 0.671 |
| no_dates | 406 | 0.626 → 0.623 | -0.002 [-0.025, +0.020] | 1 | 0.054 | 0.047 | 0.818 → 0.818 | 0.662 → 0.638 |
| dates_in_code | 406 | 0.626 → 0.621 | -0.005 [-0.027, +0.017] | 0.832 | 0.069 | 0.050 | 0.818 → 0.891 | 0.662 → 0.658 |
| shuffle1 | 406 | 0.626 → 0.628 | +0.002 [-0.032, +0.037] | 1 | 0.163 | 0.100 | 0.818 → 0.855 | 0.662 → 0.648 |
| shuffle2 | 406 | 0.626 → 0.648 | +0.022 [-0.012, +0.057] | 0.253 | 0.148 | 0.107 | 0.818 → 0.855 | 0.662 → 0.686 |

Planted false source (n = 96 No-conflict queries; expected label Misinformation):

| | Original | Planted |
|---|---|---|
| Predicted Misinformation | 0.052 | 0.302 |
| Predicted any conflict (not No conflict) | 0.354 | 0.646 |
| Predicted Outdated | 0.208 | 0.302 |
| Mean P(Misinformation) | 0.076 | 0.318 |
| Mean P(No conflict) | 0.564 | 0.311 |

## d1-ultra flat

| Perturbation | n | Acc. original → perturbed | Δ [95% CI] | McNemar p | Flip rate | TV | Outdated recall orig → pert | Outdated F1 orig → pert |
|---|---|---|---|---|---|---|---|---|
| rerun | 406 | 0.670 → 0.677 | +0.007 [-0.015, +0.030] | 0.648 | 0.052 | 0.046 | 0.764 → 0.782 | 0.627 → 0.652 |
| no_dates | 406 | 0.670 → 0.680 | +0.010 [-0.010, +0.030] | 0.454 | 0.044 | 0.036 | 0.764 → 0.782 | 0.627 → 0.662 |
| dates_in_code | 406 | 0.670 → 0.670 | +0.000 [-0.017, +0.020] | 1 | 0.044 | 0.032 | 0.764 → 0.800 | 0.627 → 0.652 |
| shuffle1 | 406 | 0.670 → 0.687 | +0.017 [-0.007, +0.042] | 0.248 | 0.074 | 0.061 | 0.764 → 0.800 | 0.627 → 0.672 |
| shuffle2 | 406 | 0.670 → 0.692 | +0.022 [-0.002, +0.049] | 0.122 | 0.074 | 0.066 | 0.764 → 0.818 | 0.627 → 0.672 |

Planted false source (n = 96 No-conflict queries; expected label Misinformation):

| | Original | Planted |
|---|---|---|
| Predicted Misinformation | 0.021 | 0.417 |
| Predicted any conflict (not No conflict) | 0.219 | 0.604 |
| Predicted Outdated | 0.156 | 0.167 |
| Mean P(Misinformation) | 0.079 | 0.326 |
| Mean P(No conflict) | 0.637 | 0.401 |

## microsoft-decision-1 flat

| Perturbation | n | Acc. original → perturbed | Δ [95% CI] | McNemar p | Flip rate | TV | Outdated recall orig → pert | Outdated F1 orig → pert |
|---|---|---|---|---|---|---|---|---|
| rerun | 406 | 0.581 → 0.586 | +0.005 [-0.007, +0.017] | 0.688 | 0.015 | 0.025 | 0.691 → 0.709 | 0.594 → 0.605 |
| no_dates | 406 | 0.581 → 0.574 | -0.007 [-0.025, +0.010] | 0.581 | 0.052 | 0.043 | 0.691 → 0.673 | 0.594 → 0.569 |
| dates_in_code | 406 | 0.581 → 0.579 | -0.002 [-0.020, +0.015] | 1 | 0.049 | 0.036 | 0.691 → 0.691 | 0.594 → 0.580 |
| shuffle1 | 406 | 0.581 → 0.584 | +0.002 [-0.030, +0.034] | 1 | 0.163 | 0.126 | 0.691 → 0.691 | 0.594 → 0.594 |
| shuffle2 | 406 | 0.581 → 0.589 | +0.007 [-0.027, +0.042] | 0.775 | 0.182 | 0.132 | 0.691 → 0.618 | 0.594 → 0.557 |

Planted false source (n = 96 No-conflict queries; expected label Misinformation):

| | Original | Planted |
|---|---|---|
| Predicted Misinformation | 0.167 | 0.469 |
| Predicted any conflict (not No conflict) | 0.583 | 0.854 |
| Predicted Outdated | 0.198 | 0.240 |
| Mean P(Misinformation) | 0.184 | 0.477 |
| Mean P(No conflict) | 0.426 | 0.162 |

## elephant-1 flat

| Perturbation | n | Acc. original → perturbed | Δ [95% CI] | McNemar p | Flip rate | TV | Outdated recall orig → pert | Outdated F1 orig → pert |
|---|---|---|---|---|---|---|---|---|
| rerun | 406 | 0.653 → 0.653 | +0.000 [+0.000, +0.000] | 1 | 0.000 | 0.000 | 0.564 → 0.564 | 0.585 → 0.585 |
| no_dates | 406 | 0.653 → 0.658 | +0.005 [-0.015, +0.025] | 0.804 | 0.042 | 0.022 | 0.564 → 0.655 | 0.585 → 0.632 |
| dates_in_code | 406 | 0.653 → 0.660 | +0.007 [-0.007, +0.025] | 0.549 | 0.030 | 0.021 | 0.564 → 0.582 | 0.585 → 0.604 |
| shuffle1 | 406 | 0.653 → 0.645 | -0.007 [-0.030, +0.015] | 0.678 | 0.074 | 0.055 | 0.564 → 0.600 | 0.585 → 0.589 |
| shuffle2 | 406 | 0.653 → 0.643 | -0.010 [-0.030, +0.010] | 0.481 | 0.071 | 0.056 | 0.564 → 0.582 | 0.585 → 0.593 |

Planted false source (n = 96 No-conflict queries; expected label Misinformation):

| | Original | Planted |
|---|---|---|
| Predicted Misinformation | 0.000 | 0.115 |
| Predicted any conflict (not No conflict) | 0.167 | 0.406 |
| Predicted Outdated | 0.115 | 0.229 |
| Mean P(Misinformation) | 0.056 | 0.172 |
| Mean P(No conflict) | 0.654 | 0.462 |

## mammoth-1 flat

| Perturbation | n | Acc. original → perturbed | Δ [95% CI] | McNemar p | Flip rate | TV | Outdated recall orig → pert | Outdated F1 orig → pert |
|---|---|---|---|---|---|---|---|---|
| rerun | 406 | 0.658 → 0.658 | +0.000 [+0.000, +0.000] | 1 | 0.000 | 0.000 | 0.727 → 0.727 | 0.625 → 0.625 |
| no_dates | 406 | 0.658 → 0.655 | -0.002 [-0.017, +0.012] | 1 | 0.025 | 0.023 | 0.727 → 0.709 | 0.625 → 0.619 |
| dates_in_code | 406 | 0.658 → 0.655 | -0.002 [-0.015, +0.010] | 1 | 0.022 | 0.019 | 0.727 → 0.727 | 0.625 → 0.615 |
| shuffle1 | 406 | 0.658 → 0.670 | +0.012 [-0.005, +0.030] | 0.267 | 0.042 | 0.045 | 0.727 → 0.709 | 0.625 → 0.624 |
| shuffle2 | 406 | 0.658 → 0.680 | +0.022 [+0.000, +0.047] | 0.0931 | 0.067 | 0.051 | 0.727 → 0.782 | 0.625 → 0.667 |

Planted false source (n = 96 No-conflict queries; expected label Misinformation):

| | Original | Planted |
|---|---|---|
| Predicted Misinformation | 0.052 | 0.396 |
| Predicted any conflict (not No conflict) | 0.188 | 0.615 |
| Predicted Outdated | 0.115 | 0.198 |
| Mean P(Misinformation) | 0.108 | 0.351 |
| Mean P(No conflict) | 0.653 | 0.377 |

## scaledown-classify-1 flat

| Perturbation | n | Acc. original → perturbed | Δ [95% CI] | McNemar p | Flip rate | TV | Outdated recall orig → pert | Outdated F1 orig → pert |
|---|---|---|---|---|---|---|---|---|
| rerun | 406 | 0.500 → 0.493 | -0.007 [-0.032, +0.017] | 0.69 | 0.084 | 0.046 | 0.200 → 0.218 | 0.275 → 0.296 |
| no_dates | 406 | 0.500 → 0.475 | -0.025 [-0.062, +0.015] | 0.253 | 0.224 | 0.114 | 0.200 → 0.255 | 0.275 → 0.322 |
| dates_in_code | 406 | 0.500 → 0.485 | -0.015 [-0.052, +0.022] | 0.519 | 0.227 | 0.114 | 0.200 → 0.127 | 0.275 → 0.182 |
| shuffle1 | 406 | 0.500 → 0.470 | -0.030 [-0.081, +0.022] | 0.315 | 0.426 | 0.206 | 0.200 → 0.164 | 0.275 → 0.209 |
| shuffle2 | 406 | 0.500 → 0.510 | +0.010 [-0.042, +0.062] | 0.781 | 0.416 | 0.209 | 0.200 → 0.200 | 0.275 → 0.278 |

Planted false source (n = 96 No-conflict queries; expected label Misinformation):

| | Original | Planted |
|---|---|---|
| Predicted Misinformation | 0.021 | 0.073 |
| Predicted any conflict (not No conflict) | 0.271 | 0.469 |
| Predicted Outdated | 0.052 | 0.146 |
| Mean P(Misinformation) | 0.092 | 0.144 |
| Mean P(No conflict) | 0.519 | 0.366 |

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
