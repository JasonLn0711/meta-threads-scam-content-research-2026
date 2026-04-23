"""Main orchestration API for the modular rule baseline."""

from __future__ import annotations

from typing import Any

from .explainability import build_explanations, build_reviewer_note
from .risk_scoring import (
    assign_binary_prediction,
    assign_risk_level,
    infer_subtype_hint,
    reason_codes_from_score,
    score_signals,
)
from .signal_extractor import aggregate_signals
from .types import RuleConfig, RulePrediction, VALID_VARIANTS


def predict_item(record: dict[str, Any], config: RuleConfig, variant: str = "all") -> dict[str, Any]:
    if variant not in VALID_VARIANTS:
        raise ValueError(f"variant must be one of {', '.join(VALID_VARIANTS)}")

    matched_signals = aggregate_signals(record, variant, config)
    score = score_signals(matched_signals, config)
    risk_level = assign_risk_level(score, config)
    binary_pred = assign_binary_prediction(risk_level, config)
    subtype_hint = infer_subtype_hint(matched_signals, score, config)
    reason_codes = reason_codes_from_score(matched_signals, score, config)
    explanations = build_explanations(matched_signals, score, reason_codes)
    reviewer_note = build_reviewer_note(risk_level, subtype_hint, score)

    prediction = RulePrediction(
        item_id=str(record.get("item_id") or ""),
        binary_pred=binary_pred,
        risk_level_pred=risk_level,
        subtype_hint=subtype_hint,
        total_score=score.total_score,
        reason_codes=reason_codes,
        explanations=explanations,
        score_breakdown=score,
        matched_signals=matched_signals,
        reviewer_note=reviewer_note,
    )
    return prediction.to_dict()


def predict_batch(
    records: list[dict[str, Any]],
    config: RuleConfig,
    variant: str = "all",
) -> list[dict[str, Any]]:
    return [predict_item(record, config=config, variant=variant) for record in records]
