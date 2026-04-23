"""Binary metrics for rule-baseline outputs."""

from __future__ import annotations

from collections import Counter
from typing import Any


POSITIVE_LABEL = "scam"
NEGATIVE_LABEL = "non_scam"


def preferred_gold_label(record: dict[str, Any]) -> str:
    return str(record.get("final_label") or record.get("scam_label") or "")


def binary_metrics(records: list[dict[str, Any]], predictions: list[dict[str, Any]]) -> dict[str, Any]:
    tp = tn = fp = fn = 0
    skipped: Counter[str] = Counter()

    for record, prediction in zip(records, predictions, strict=False):
        gold = preferred_gold_label(record)
        pred_positive = prediction.get("binary_pred") == "scam_like"
        if gold == POSITIVE_LABEL:
            if pred_positive:
                tp += 1
            else:
                fn += 1
        elif gold == NEGATIVE_LABEL:
            if pred_positive:
                fp += 1
            else:
                tn += 1
        else:
            skipped[gold or "<blank>"] += 1

    total = tp + tn + fp + fn
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = (2 * precision * recall / (precision + recall)) if precision + recall else 0.0
    accuracy = (tp + tn) / total if total else 0.0

    return {
        "binary_metric_items": total,
        "accuracy": round(accuracy, 6),
        "precision": round(precision, 6),
        "recall": round(recall, 6),
        "f1": round(f1, 6),
        "true_positive": tp,
        "true_negative": tn,
        "false_positive": fp,
        "false_negative": fn,
        "skipped_label_counts": dict(sorted(skipped.items())),
    }


def has_any_labels(records: list[dict[str, Any]]) -> bool:
    return any(preferred_gold_label(record) for record in records)
