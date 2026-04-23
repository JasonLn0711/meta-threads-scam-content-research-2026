"""Error-analysis helpers for the rule baseline."""

from __future__ import annotations

from collections import Counter
from typing import Any

from .metrics import NEGATIVE_LABEL, POSITIVE_LABEL, preferred_gold_label


def error_analysis(records: list[dict[str, Any]], predictions: list[dict[str, Any]]) -> dict[str, Any]:
    false_positives: list[dict[str, Any]] = []
    false_negatives: list[dict[str, Any]] = []
    medium_risk_ambiguity: list[str] = []
    subtype_misses: Counter[str] = Counter()

    for record, prediction in zip(records, predictions, strict=False):
        item_id = str(record.get("item_id") or prediction.get("item_id") or "")
        gold = preferred_gold_label(record)
        pred_positive = prediction.get("binary_pred") == "scam_like"

        if gold == NEGATIVE_LABEL and pred_positive:
            false_positives.append(_compact_case(record, prediction))
        if gold == POSITIVE_LABEL and not pred_positive:
            false_negatives.append(_compact_case(record, prediction))
            for subtype in record.get("scam_type", []) or []:
                if subtype != "none":
                    subtype_misses[str(subtype)] += 1
        if gold in {"uncertain", "insufficient_evidence"} and prediction.get("risk_level_pred") == "medium":
            medium_risk_ambiguity.append(item_id)

    return {
        "false_positive_count": len(false_positives),
        "false_negative_count": len(false_negatives),
        "false_positives": false_positives[:25],
        "false_negatives": false_negatives[:25],
        "medium_risk_ambiguity_count": len(medium_risk_ambiguity),
        "medium_risk_ambiguity_item_ids": medium_risk_ambiguity[:50],
        "subtype_specific_misses": dict(sorted(subtype_misses.items())),
    }


def _compact_case(record: dict[str, Any], prediction: dict[str, Any]) -> dict[str, Any]:
    return {
        "item_id": str(record.get("item_id") or prediction.get("item_id") or ""),
        "gold_label": preferred_gold_label(record),
        "gold_risk_level": str(record.get("final_risk_level") or record.get("risk_level") or ""),
        "pred_binary": prediction.get("binary_pred"),
        "pred_risk_level": prediction.get("risk_level_pred"),
        "subtype_hint": prediction.get("subtype_hint"),
        "reason_codes": prediction.get("reason_codes", []),
        "total_score": prediction.get("total_score"),
    }
