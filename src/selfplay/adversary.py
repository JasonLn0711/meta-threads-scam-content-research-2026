"""Safe adversary simulator for defensive self-play."""

from __future__ import annotations

import hashlib
import json
from typing import Any

from src.evidence.storage import utc_now
from src.selfplay.logging import SELFPLAY_VARIANTS_LOG, append_jsonl


DISALLOWED_TERMS = (
    "telegram",
    "whatsapp",
    "payment link",
    "bank account",
    "wire transfer",
    "crypto wallet",
    "seed phrase",
    "send money",
    "deposit",
    "account number",
    "click here",
    "dm me",
)

VARIANT_LIBRARY: dict[str, list[dict[str, Any]]] = {
    "authority_impersonation": [
        {
            "variant_strategy": "Remove explicit expert identity and frame the lure as peer-to-peer market reflection.",
            "evasion_characteristic": "authority_signal_drop",
            "abstract_example": "Abstract sample: a generic post presents peer discussion around market notes, with no expert title, contact path, or transaction step.",
            "target_difficulty": 0.25,
            "search_query": "peer market notes cautious investment discussion",
        },
        {
            "variant_strategy": "Split authority cues across soft credibility hints instead of direct titles.",
            "evasion_characteristic": "distributed_authority_hint",
            "abstract_example": "Abstract sample: a generic post implies experience through vague background context, without naming credentials or telling readers what to do.",
            "target_difficulty": 0.62,
            "search_query": "experienced investor notes soft credibility",
        },
    ],
    "guaranteed_return": [
        {
            "variant_strategy": "Replace outcome certainty with vague stability language and uncertainty-preserving phrasing.",
            "evasion_characteristic": "guarantee_language_softening",
            "abstract_example": "Abstract sample: a generic post describes a cautious observation that sounds stable but avoids promised outcomes, numbers, or steps.",
            "target_difficulty": 0.3,
            "search_query": "stable approach cautious observation investing",
        },
        {
            "variant_strategy": "Move from direct outcome claims to story-shaped confidence signals.",
            "evasion_characteristic": "outcome_claim_indirection",
            "abstract_example": "Abstract sample: a generic post references a personal learning arc without specific returns, instructions, or a request to act.",
            "target_difficulty": 0.67,
            "search_query": "personal investing learning arc stable",
        },
    ],
    "off_platform_contact": [
        {
            "variant_strategy": "Remove named channels and express only a vague preference for lower-noise discussion.",
            "evasion_characteristic": "platform_reference_drop",
            "abstract_example": "Abstract sample: a generic post says public discussion can be noisy, while omitting platform names, handles, or contact steps.",
            "target_difficulty": 0.36,
            "search_query": "quiet discussion investing no public noise",
        },
        {
            "variant_strategy": "Reframe migration pressure as resource organization rather than a direct invitation.",
            "evasion_characteristic": "contact_purpose_reframing",
            "abstract_example": "Abstract sample: a generic post mentions organized notes as context only, with no delivery channel, signup instruction, or payment path.",
            "target_difficulty": 0.72,
            "search_query": "organized investing notes reference",
        },
    ],
    "urgency": [
        {
            "variant_strategy": "Replace countdown pressure with a broad timing-window narrative.",
            "evasion_characteristic": "urgency_softening",
            "abstract_example": "Abstract sample: a generic post talks about a broad observation window without deadlines, scarcity, or instructions.",
            "target_difficulty": 0.28,
            "search_query": "observation window investing discussion",
        },
        {
            "variant_strategy": "Hide time pressure inside routine planning language.",
            "evasion_characteristic": "routine_timing_camouflage",
            "abstract_example": "Abstract sample: a generic post frames timing as ordinary planning, without pressure words or action requests.",
            "target_difficulty": 0.64,
            "search_query": "routine planning market observation",
        },
    ],
    "hard_negative_warning": [
        {
            "variant_strategy": "Preserve warning intent as a boundary test for false-positive pressure.",
            "evasion_characteristic": "hard_negative_boundary",
            "abstract_example": "Abstract sample: a generic safety note reminds readers to treat investment claims cautiously and seek independent verification.",
            "target_difficulty": 0.1,
            "search_query": "investment safety warning independent verification",
        }
    ],
}


def generate_variant(
    concept: dict[str, Any],
    *,
    difficulty: float = 0.35,
    strategy_bias: str | None = None,
    log: bool = False,
) -> dict[str, Any]:
    """Generate one non-actionable adversarial variant for a concept."""
    difficulty = _clamp(difficulty)
    template = _select_template(concept, difficulty=difficulty, strategy_bias=strategy_bias)
    concept_id = str(concept.get("concept_id") or "unknown_concept")
    variant_id = _variant_id(concept_id, str(template["evasion_characteristic"]), difficulty)
    variant = {
        "schema_version": "selfplay_variant_v1",
        "variant_id": variant_id,
        "origin_concept_id": concept_id,
        "origin_concept_name": concept.get("concept_name"),
        "origin_dominant_signal": concept.get("dominant_signal"),
        "variant_strategy": template["variant_strategy"],
        "evasion_characteristic": template["evasion_characteristic"],
        "abstract_example": _sanitize_text(str(template["abstract_example"])),
        "search_query": template["search_query"],
        "difficulty": round(difficulty, 6),
        "abstraction_level": "high",
        "safety_constraints": [
            "abstract patterns only",
            "no real contact path",
            "no payment or transfer detail",
            "no step-by-step scam script",
            "human research use only",
        ],
        "non_actionable": True,
        "actionable_content_included": False,
        "simulated_only": True,
        "created_at": utc_now(),
        "raw_source_included": False,
    }
    if log:
        append_jsonl(SELFPLAY_VARIANTS_LOG, variant)
    return variant


def _select_template(
    concept: dict[str, Any],
    *,
    difficulty: float,
    strategy_bias: str | None,
) -> dict[str, Any]:
    signal = str(concept.get("dominant_signal") or "hard_negative_warning")
    templates = VARIANT_LIBRARY.get(signal, VARIANT_LIBRARY["hard_negative_warning"])
    if strategy_bias:
        biased = [template for template in templates if template["evasion_characteristic"] == strategy_bias]
        if biased:
            return biased[0]
    return min(templates, key=lambda template: abs(float(template["target_difficulty"]) - difficulty))


def _sanitize_text(text: str) -> str:
    lowered = text.lower()
    if any(term in lowered for term in DISALLOWED_TERMS):
        return (
            "Abstract sample: a generic pattern changes surface language while omitting contact, "
            "payment, platform, credential, and action details."
        )
    return text


def _variant_id(concept_id: str, evasion_characteristic: str, difficulty: float) -> str:
    material = json.dumps(
        {
            "concept_id": concept_id,
            "difficulty_bucket": round(difficulty, 1),
            "evasion_characteristic": evasion_characteristic,
        },
        ensure_ascii=False,
        sort_keys=True,
    )
    digest = hashlib.sha1(material.encode("utf-8")).hexdigest()[:12]
    return f"selfplay_variant_{digest}"


def _clamp(value: float) -> float:
    return max(0.0, min(1.0, float(value)))
