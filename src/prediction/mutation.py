"""Predictive concept mutation engine with a deterministic local policy."""

from __future__ import annotations

import hashlib
import json
from typing import Any

from src.evidence.storage import utc_now
from src.prediction.logging import PREDICTED_VARIANTS_LOG, append_jsonl


MUTATION_LIBRARY: dict[str, list[dict[str, Any]]] = {
    "authority_impersonation": [
        {
            "variant_name": "peer experience soft pitch",
            "modified_strategy": "Replace the expert persona with a casual peer sharing a recent experience.",
            "evasion_type": "authority_signal_drop",
            "example_text": "最近朋友介紹一個投資討論方式，沒有很誇張但看起來滿穩，有興趣可以一起交流看看。",
            "search_query": "朋友介紹 投資 交流 滿穩",
            "evasion_strength": 0.62,
        },
        {
            "variant_name": "anonymous note sharing",
            "modified_strategy": "Move from named teacher guidance to anonymous notes and discussion framing.",
            "evasion_type": "identity_obfuscation",
            "example_text": "整理了一些近期市場筆記，想找幾個人一起討論方向，不保證結果，單純交流。",
            "search_query": "市場筆記 一起討論 投資方向",
            "evasion_strength": 0.54,
        },
    ],
    "guaranteed_return": [
        {
            "variant_name": "soft stability language",
            "modified_strategy": "Replace guaranteed-profit language with mild stability and experience claims.",
            "evasion_type": "guarantee_language_softening",
            "example_text": "最近試到一個比較穩的配置想法，波動沒有想像中大，想找人交換心得。",
            "search_query": "比較穩 配置想法 交換心得",
            "evasion_strength": 0.66,
        },
        {
            "variant_name": "case-based confidence",
            "modified_strategy": "Use personal-case framing instead of explicit return guarantees.",
            "evasion_type": "outcome_claim_indirection",
            "example_text": "這陣子用同一套方法看盤，結果比以前穩一些，想聽聽大家怎麼判斷。",
            "search_query": "同一套方法 看盤 穩一些",
            "evasion_strength": 0.58,
        },
    ],
    "off_platform_contact": [
        {
            "variant_name": "low-friction discussion invite",
            "modified_strategy": "Avoid explicit platform names and ask for lightweight private discussion.",
            "evasion_type": "platform_reference_drop",
            "example_text": "公開留言容易漏訊息，想深入聊的可以用比較方便的方式交流，不急著做決定。",
            "search_query": "深入聊 方便的方式 交流 投資",
            "evasion_strength": 0.68,
        },
        {
            "variant_name": "resource request funnel",
            "modified_strategy": "Frame private migration as sending notes or a checklist rather than joining a group.",
            "evasion_type": "contact_purpose_reframing",
            "example_text": "我有整理一份觀察清單，想看的可以再跟我說，先當參考不要衝動。",
            "search_query": "觀察清單 想看 跟我說 投資",
            "evasion_strength": 0.57,
        },
    ],
    "urgency": [
        {
            "variant_name": "gentle window framing",
            "modified_strategy": "Replace countdown pressure with a soft timing window.",
            "evasion_type": "urgency_softening",
            "example_text": "這幾天可能有一個不錯的觀察窗口，想先把想法整理好再慢慢討論。",
            "search_query": "觀察窗口 想法 整理 討論",
            "evasion_strength": 0.52,
        }
    ],
    "hard_negative_warning": [
        {
            "variant_name": "warning camouflage check",
            "modified_strategy": "Use anti-scam wording as a calibration variant, not as a scam lure.",
            "evasion_type": "hard_negative_boundary_test",
            "example_text": "看到有人用投資群引導私下聯絡，大家要小心，不要只看收益說法。",
            "search_query": "投資群 私下聯絡 小心 收益說法",
            "evasion_strength": 0.2,
        }
    ],
}


def build_mutation_prompt(concept: dict[str, Any]) -> str:
    """Build the prompt an approved LLM mutation adapter would receive."""
    safe_context = {
        "concept_id": concept.get("concept_id"),
        "concept_name": concept.get("concept_name"),
        "description": concept.get("description"),
        "attack_pattern": concept.get("attack_pattern"),
        "psychological_hook": concept.get("psychological_hook"),
        "dominant_signal": concept.get("dominant_signal"),
        "risk_level": concept.get("risk_level"),
        "keywords": list(concept.get("keywords", []))[:10],
    }
    return (
        "Generate plausible, subtle scam-strategy mutations for research simulation.\n"
        "Avoid extreme or operationally instructive content; preserve uncertainty and synthetic tags.\n"
        "Output variant_name, modified_strategy, evasion_type, and example_text.\n"
        f"Metadata-only concept context:\n{json.dumps(safe_context, ensure_ascii=False, sort_keys=True)}"
    )


def mutate_concept(concept: dict[str, Any], *, count: int = 3, log: bool = False) -> list[dict[str, Any]]:
    """Generate metadata-linked predicted variants for a concept."""
    prompt = build_mutation_prompt(concept)
    signal = str(concept.get("dominant_signal") or "hard_negative_warning")
    templates = list(MUTATION_LIBRARY.get(signal, MUTATION_LIBRARY["hard_negative_warning"]))
    if signal != "hard_negative_warning":
        templates.append(MUTATION_LIBRARY["hard_negative_warning"][0])

    variants = [_variant_from_template(concept, template, prompt) for template in templates[: max(1, count)]]
    if log:
        for variant in variants:
            append_jsonl(PREDICTED_VARIANTS_LOG, variant)
    return variants


def _variant_from_template(concept: dict[str, Any], template: dict[str, Any], prompt: str) -> dict[str, Any]:
    concept_id = str(concept.get("concept_id") or "unknown_concept")
    variant_name = str(template["variant_name"])
    variant_id = _variant_id(concept_id, variant_name, str(template["evasion_type"]))
    return {
        "schema_version": "predicted_variant_v1",
        "variant_id": variant_id,
        "origin_concept_id": concept_id,
        "origin_concept_name": concept.get("concept_name"),
        "origin_dominant_signal": concept.get("dominant_signal"),
        "variant_name": variant_name,
        "modified_strategy": template["modified_strategy"],
        "evasion_type": template["evasion_type"],
        "evasion_strength": round(float(template.get("evasion_strength", 0.5)), 6),
        "example_text": template["example_text"],
        "search_query": template["search_query"],
        "created_at": utc_now(),
        "llm_prompt_hash": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
        "llm_backend": "local_mutation_policy_v1",
        "simulated_only": True,
        "raw_source_included": False,
    }


def _variant_id(concept_id: str, variant_name: str, evasion_type: str) -> str:
    material = json.dumps(
        {"concept_id": concept_id, "variant_name": variant_name, "evasion_type": evasion_type},
        ensure_ascii=False,
        sort_keys=True,
    )
    digest = hashlib.sha1(material.encode("utf-8")).hexdigest()[:12]
    return f"variant_{digest}"
