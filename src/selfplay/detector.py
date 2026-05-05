"""Defensive detector used inside self-play simulations."""

from __future__ import annotations

from typing import Any

from src.concepts.matcher import match_concept
from src.evidence.storage import utc_now
from src.selfplay.logging import SELFPLAY_DETECTIONS_LOG, append_jsonl


DEFAULT_THRESHOLD = 0.58


def detect(
    simulated_data: dict[str, Any],
    concepts: list[dict[str, Any]],
    *,
    detector_state: dict[str, Any] | None = None,
    log: bool = False,
) -> dict[str, Any]:
    """Return a conservative concept detection result for abstract simulated data."""
    detector_state = detector_state or {}
    concept = _origin_concept(simulated_data, concepts)
    text = str(simulated_data.get("text", ""))
    match = match_concept(text, concepts)
    robustness = _clamp(float(detector_state.get("robustness", 0.35) or 0.35))
    difficulty = _clamp(float(simulated_data.get("difficulty", 0.0) or 0.0))
    alignment = _alignment_score(simulated_data, concept)
    matcher_confidence = float(match.get("confidence", 0.0) or 0.0)
    confidence = _clamp(
        0.3
        + (0.42 * robustness)
        + (0.2 * alignment)
        + (0.12 * matcher_confidence)
        - (0.24 * difficulty)
    )
    threshold = float(detector_state.get("threshold", DEFAULT_THRESHOLD) or DEFAULT_THRESHOLD)
    matched_concept = concept.get("concept_id") if concept and confidence >= threshold else match.get("matched_concept")
    is_scam_like = confidence >= max(0.35, threshold - 0.16)
    novelty = matched_concept is None and is_scam_like
    result = {
        "schema_version": "selfplay_detection_v1",
        "simulation_id": simulated_data.get("simulation_id"),
        "variant_id": simulated_data.get("variant_id"),
        "origin_concept_id": simulated_data.get("origin_concept_id"),
        "confidence": round(confidence, 6),
        "matched_concept": matched_concept,
        "novelty": bool(novelty),
        "is_scam_like": bool(is_scam_like),
        "detector_threshold": round(threshold, 6),
        "robustness": round(robustness, 6),
        "reasoning": _reason(confidence, threshold, novelty, concept),
        "created_at": utc_now(),
        "simulated": True,
        "raw_source_included": False,
    }
    if log:
        append_jsonl(SELFPLAY_DETECTIONS_LOG, result)
    return result


def _origin_concept(simulated_data: dict[str, Any], concepts: list[dict[str, Any]]) -> dict[str, Any]:
    origin_id = str(simulated_data.get("origin_concept_id") or "")
    for concept in concepts:
        if str(concept.get("concept_id")) == origin_id:
            return concept
    return {}


def _alignment_score(simulated_data: dict[str, Any], concept: dict[str, Any]) -> float:
    if not concept:
        return 0.15
    score = 0.25
    if simulated_data.get("origin_dominant_signal") == concept.get("dominant_signal"):
        score += 0.45
    if simulated_data.get("origin_concept_id") == concept.get("concept_id"):
        score += 0.3
    return _clamp(score)


def _reason(confidence: float, threshold: float, novelty: bool, concept: dict[str, Any]) -> str:
    if confidence >= threshold and concept:
        return "Matched the abstract variant back to its source concept."
    if novelty:
        return "Detected scam-like structure but kept the concept match conservative."
    return "Low-confidence abstract pattern; retain for robustness analysis."


def _clamp(value: float) -> float:
    return max(0.0, min(1.0, float(value)))
