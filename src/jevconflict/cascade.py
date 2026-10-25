"""Confidence-gated cascade, computed offline from stored answers (protocol in NOTES.md).

Jev answers every query; the fraction f with the lowest Jev confidence is escalated to the LLM,
whose answer replaces Jev's. The threshold is a quantile of Jev's confidences, so it uses no
labels and the curve can be computed on the evaluation split itself.
"""

from __future__ import annotations

import numpy as np

from .metrics import mcnemar_exact, paired_bootstrap

HEADLINE = (0.25, 0.50)


def escalate_mask(conf: np.ndarray, f: float) -> np.ndarray:
    """True for the round(f * n) least confident queries (ties broken by query order)."""
    k = int(round(f * len(conf)))
    mask = np.zeros(len(conf), dtype=bool)
    mask[np.argsort(conf, kind="stable")[:k]] = True
    return mask


def auroc(score: np.ndarray, positive: np.ndarray) -> float:
    """P(score of a random positive > score of a random negative), ties counted half."""
    pos, neg = score[positive], score[~positive]
    if not len(pos) or not len(neg):
        return float("nan")
    greater = (pos[:, None] > neg[None, :]).mean()
    ties = (pos[:, None] == neg[None, :]).mean()
    return float(greater + 0.5 * ties)


def curve(cheap: list[dict], expensive: list[dict], fractions=None) -> list[dict]:
    """`cheap` and `expensive` are run records on the same queries, in the same order."""
    assert [r["id"] for r in cheap] == [r["id"] for r in expensive]
    fractions = np.round(np.arange(0, 1.0001, 0.05), 2) if fractions is None else fractions
    conf = np.array([max(r["probs"].values()) for r in cheap])
    ok_c = np.array([r["pred"] == r["label"] for r in cheap])
    ok_e = np.array([r["pred"] == r["label"] for r in expensive])
    usd_c = np.array([r["cost_usd"] or 0.0 for r in cheap])
    usd_e = np.array([r["cost_usd"] or 0.0 for r in expensive])
    lat_c = np.array([r["latency_s"] or 0.0 for r in cheap])
    lat_e = np.array([r["latency_s"] or 0.0 for r in expensive])
    rows = []
    for f in fractions:
        esc = escalate_mask(conf, f)
        ok = np.where(esc, ok_e, ok_c)
        rows.append({
            "f": float(f), "escalated": int(esc.sum()), "acc": float(ok.mean()),
            "acc_random": float((1 - esc.mean()) * ok_c.mean() + esc.mean() * ok_e.mean()),
            "usd_per_1k": 1000 * float((usd_c + esc * usd_e).mean()),
            "lat_mean": float((lat_c + esc * lat_e).mean()),
            "lat_p95": float(np.percentile(lat_c + esc * lat_e, 95)),
            "vs_expensive": paired_bootstrap(ok, ok_e), "p_vs_expensive": mcnemar_exact(ok, ok_e),
            "correct": ok,
        })
    return rows


def summary_stats(cheap: list[dict], expensive: list[dict]) -> dict:
    conf = np.array([max(r["probs"].values()) for r in cheap])
    ok_c = np.array([r["pred"] == r["label"] for r in cheap])
    ok_e = np.array([r["pred"] == r["label"] for r in expensive])
    return {"auroc": auroc(conf, ok_c), "acc_cheap": float(ok_c.mean()), "acc_expensive": float(ok_e.mean()),
            "usd_expensive": 1000 * float(np.mean([r["cost_usd"] or 0.0 for r in expensive])),
            "lat_expensive": float(np.mean([r["latency_s"] or 0.0 for r in expensive])),
            # Where escalation can help at all: Jev wrong and the LLM right.
            "jev_wrong_llm_right": int((~ok_c & ok_e).sum()), "jev_right_llm_wrong": int((ok_c & ~ok_e).sum())}
