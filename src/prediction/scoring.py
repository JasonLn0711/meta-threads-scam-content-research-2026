"""Risk scoring for synthetic predictive simulations."""

from __future__ import annotations

import math
from typing import Any

from src.concepts.matcher import match_concept
from src.embedding.encoder import encode
from src.evidence.storage import utc_now
from src.prediction.logging import SIMULATION_SCORES_LOG, append_jsonl


def score_simulation(
    simulated_post: dict[str, Any],
    concept: dict[str, Any],
    *,
    log: bool = False,
) -> dict[str, Any]:
    """Score a simulated post using similarity, concept match, and novelty."""
    text = str(simulated_post.get("text", ""))
    similarity = _cosine(encode(text), encode(_concept_text(concept)))
    match = match_concept(text, [concept])
    concept_match_confidence = float(match.get("confidence", 0.0) or 0.0)
    novelty_score = 1.0 if match.get("is_novel") else max(0.0, 1.0 - concept_match_confidence)
    evasion_strength = float(simulated_post.get("evasion_strength", 0.0) or 0.0)
    risk_score = (
        (0.42 * similarity)
        + (0.28 * concept_match_confidence)
        + (0.18 * novelty_score)
        + (0.12 * evasion_strength)
    )
    result = {
        "schema_version": "simulation_risk_score_v1",
        "simulation_id": simulated_post.get("simulation_id"),
        "variant_id": simulated_post.get("variant_id"),
        "origin_concept_id": concept.get("concept_id"),
        "embedding_similarity": round(similarity, 6),
        "concept_match_confidence": round(concept_match_confidence, 6),
        "novelty_score": round(novelty_score, 6),
        "evasion_strength": round(evasion_strength, 6),
        "risk_score": round(max(0.0, min(1.0, risk_score)), 6),
        "matched_concept": match.get("matched_concept"),
        "is_novel": bool(match.get("is_novel")),
        "reasoning": _reason(similarity, concept_match_confidence, novelty_score, evasion_strength),
        "created_at": utc_now(),
        "simulated": True,
        "raw_source_included": False,
    }
    if log:
        append_jsonl(SIMULATION_SCORES_LOG, result)
    return result


def _concept_text(concept: dict[str, Any]) -> str:
    keywords = " ".join(str(keyword) for keyword in concept.get("keywords", []))
    return " ".join(
        [
            str(concept.get("concept_name", "")),
            str(concept.get("description", "")),
            str(concept.get("attack_pattern", "")),
            str(concept.get("psychological_hook", "")),
            keywords,
        ]
    )


def _cosine(left: list[float], right: list[float]) -> float:
    numerator = sum(a * b for a, b in zip(left, right))
    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))
    if left_norm == 0.0 or right_norm == 0.0:
        return 0.0
    return max(0.0, min(1.0, numerator / (left_norm * right_norm)))


def _reason(similarity: float, confidence: float, novelty: float, evasion: float) -> str:
    if novelty >= 0.7 and similarity >= 0.45:
        return "Semantically near the concept but likely to evade direct matching."
    if confidence >= 0.6 and evasion >= 0.5:
        return "Still matches the concept while softening obvious signals."
    return "Plausible low-to-medium priority simulation; keep as exploration seed."
