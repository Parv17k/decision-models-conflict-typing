"""Classification quality, calibration, and paired significance tests (numpy only)."""

from __future__ import annotations

from math import comb

import numpy as np


def accuracy(y: list[str], pred: list[str]) -> float:
    return float(np.mean([a == b for a, b in zip(y, pred)]))


def per_class_f1(y: list[str], pred: list[str], labels: list[str]) -> dict[str, float]:
    out = {}
    for c in labels:
        tp = sum(a == c and b == c for a, b in zip(y, pred))
        fp = sum(a != c and b == c for a, b in zip(y, pred))
        fn = sum(a == c and b != c for a, b in zip(y, pred))
        out[c] = 2 * tp / (2 * tp + fp + fn) if tp + fp + fn else float("nan")
    return out


def macro_f1(y: list[str], pred: list[str], labels: list[str]) -> float:
    """Averaged over labels that occur in the gold labels."""
    f1 = per_class_f1(y, pred, labels)
    return float(np.mean([f1[c] for c in labels if c in set(y)]))


def confusion(y: list[str], pred: list[str], labels: list[str]) -> np.ndarray:
    """Predictions outside `labels` (unparsed answers) are left out of the matrix."""
    m = np.zeros((len(labels), len(labels)), dtype=int)
    for a, b in zip(y, pred):
        if b in labels:
            m[labels.index(a), labels.index(b)] += 1
    return m


def ece(conf: np.ndarray, correct: np.ndarray, bins: int = 10) -> float:
    """Top-label expected calibration error with equal-width bins."""
    edges = np.linspace(0, 1, bins + 1)
    idx = np.clip(np.digitize(conf, edges[1:-1]), 0, bins - 1)
    return float(sum(abs(conf[idx == b].mean() - correct[idx == b].mean()) * (idx == b).mean()
                     for b in range(bins) if (idx == b).any()))


def brier(P: np.ndarray, y_idx: np.ndarray) -> float:
    onehot = np.eye(P.shape[1])[y_idx]
    return float(((P - onehot) ** 2).sum(axis=1).mean())


def nll(P: np.ndarray, y_idx: np.ndarray, eps: float = 1e-4) -> float:
    return float(-np.log(np.clip(P[np.arange(len(y_idx)), y_idx], eps, 1)).mean())


def bootstrap_ci(x: np.ndarray, n: int = 10_000, seed: int = 0) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    means = x[rng.integers(0, len(x), (n, len(x)))].mean(axis=1)
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def paired_bootstrap(a: np.ndarray, b: np.ndarray, n: int = 10_000, seed: int = 0) -> dict:
    """Mean of a - b over queries, with a 95% interval from resampling queries."""
    lo, hi = bootstrap_ci(a.astype(float) - b.astype(float), n, seed)
    return {"diff": float(a.mean() - b.mean()), "lo": lo, "hi": hi}


def mcnemar_exact(a: np.ndarray, b: np.ndarray) -> float:
    """Two-sided exact McNemar p-value on per-query correctness."""
    n01, n10 = int((~a & b).sum()), int((a & ~b).sum())
    n = n01 + n10
    if n == 0:
        return 1.0
    k = min(n01, n10)
    return min(1.0, 2 * sum(comb(n, i) for i in range(k + 1)) / 2 ** n)
