"""Triage-level metrics for high/medium/low baseline outputs."""

from __future__ import annotations

from collections import Counter
from typing import Any


RISK_LEVELS = ("high", "medium", "low")


def preferred_gold_risk(record: dict[str, Any]) -> str:
    return str(record.get("final_risk_level") or record.get("risk_level") or "")


def triage_metrics(records: list[dict[str, Any]], predictions: list[dict[str, Any]]) -> dict[str, Any]:
    confusion = {gold: {pred: 0 for pred in RISK_LEVELS} for gold in RISK_LEVELS}
    support: Counter[str] = Counter()
    exact = 0
    total = 0
    skipped: Counter[str] = Counter()

    for record, prediction in zip(records, predictions, strict=False):
        gold = preferred_gold_risk(record)
        pred = str(prediction.get("risk_level_pred") or "")
        if gold not in RISK_LEVELS or pred not in RISK_LEVELS:
            skipped[gold or "<blank>"] += 1
            continue
        confusion[gold][pred] += 1
        support[gold] += 1
        total += 1
        if gold == pred:
            exact += 1

    return {
        "triage_metric_items": total,
        "exact_agreement": round(exact / total, 6) if total else 0.0,
        "exact_matches": exact,
        "confusion": confusion,
        "per_class_support": dict(sorted(support.items())),
        "skipped_risk_counts": dict(sorted(skipped.items())),
    }
