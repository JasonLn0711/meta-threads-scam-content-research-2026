"""Generate tagged synthetic posts from predicted concept variants."""

from __future__ import annotations

import hashlib
import json
from typing import Any

from src.evidence.storage import utc_now
from src.prediction.logging import SIMULATED_POSTS_LOG, append_jsonl


def generate_simulated_posts(variants: list[dict[str, Any]], *, log: bool = False) -> list[dict[str, Any]]:
    """Create plausible, tagged synthetic posts from predicted variants."""
    posts = [_post_from_variant(variant) for variant in variants]
    if log:
        for post in posts:
            append_jsonl(SIMULATED_POSTS_LOG, post)
    return posts


def _post_from_variant(variant: dict[str, Any]) -> dict[str, Any]:
    text = _realistic_text(str(variant.get("example_text", "")), str(variant.get("evasion_type", "")))
    simulation_id = _simulation_id(str(variant.get("variant_id", "")), text)
    return {
        "schema_version": "simulated_post_v1",
        "simulation_id": simulation_id,
        "variant_id": variant.get("variant_id"),
        "origin_concept_id": variant.get("origin_concept_id"),
        "origin_concept_name": variant.get("origin_concept_name"),
        "origin_dominant_signal": variant.get("origin_dominant_signal"),
        "evasion_type": variant.get("evasion_type"),
        "evasion_strength": variant.get("evasion_strength", 0.0),
        "text": text,
        "search_query": variant.get("search_query"),
        "candidate_type": "simulated",
        "source": "predictive_layer",
        "tag": "simulated_prediction",
        "created_at": utc_now(),
        "simulated": True,
        "raw_source_included": False,
    }


def _realistic_text(example_text: str, evasion_type: str) -> str:
    if not example_text:
        return "最近看到一個投資討論方式，想先整理想法再交流。"
    if evasion_type == "hard_negative_boundary_test":
        return example_text
    if "投資" not in example_text and "市場" not in example_text:
        return f"{example_text} 投資上還是先觀察就好。"
    return example_text


def _simulation_id(variant_id: str, text: str) -> str:
    material = json.dumps({"variant_id": variant_id, "text": text}, ensure_ascii=False, sort_keys=True)
    digest = hashlib.sha1(material.encode("utf-8")).hexdigest()[:12]
    return f"simulation_{digest}"
