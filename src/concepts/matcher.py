"""Conservative concept matching for semantic reasoning simulations."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from src.concepts.builder import CONCEPTS_DIR
from src.embedding.encoder import detect_language
from src.evidence.storage import utc_now


MATCH_RESULTS_LOG = CONCEPTS_DIR / "match_results.jsonl"
REASONING_TRACE_LOG = CONCEPTS_DIR / "reasoning_trace.jsonl"
NEW_CLUSTER_POOL_LOG = CONCEPTS_DIR / "new_cluster_pool.jsonl"


def build_match_prompt(post: str, concepts: list[dict[str, Any]]) -> str:
    """Build the prompt an approved LLM matcher would receive."""
    safe_concepts = [
        {
            "concept_id": concept.get("concept_id"),
            "concept_name": concept.get("concept_name"),
            "description": concept.get("description"),
            "attack_pattern": concept.get("attack_pattern"),
            "risk_level": concept.get("risk_level"),
            "keywords": concept.get("keywords", [])[:8],
        }
        for concept in concepts[:12]
    ]
    return (
        "You are matching a social media post to known scam-behavior concepts.\n"
        "Prefer conservative matching; if evidence is weak, mark novel.\n"
        "Keep reasoning short and do not infer legal fraud.\n"
        f"Post hash: {_content_hash(post)}\n"
        f"Known concepts:\n{json.dumps(safe_concepts, ensure_ascii=False, sort_keys=True)}"
    )


def match_concept(
    post: str,
    concepts: list[dict[str, Any]],
    *,
    min_confidence: float = 0.52,
    log: bool = False,
) -> dict[str, Any]:
    """Match a post to a known concept, or conservatively mark it novel."""
    prompt = build_match_prompt(post, concepts)
    if not concepts:
        result = _novel_result(post, prompt, "no known concepts")
        if log:
            log_match_result(result)
        return result

    scored = sorted(
        [(_concept_score(post, concept), concept) for concept in concepts],
        key=lambda item: (-item[0], str(item[1].get("concept_id", ""))),
    )
    score, concept = max(scored, key=lambda item: item[0])
    related_concepts = _related_concepts(scored)
    is_novel = score < min_confidence or concept.get("risk_level") == "low" and _has_high_risk_language(post)
    if is_novel:
        result = _novel_result(post, prompt, "no conservative concept match")
        result["related_concepts"] = related_concepts
    else:
        result = {
            "schema_version": "concept_match_v1",
            "matched_concept": concept["concept_id"],
            "matched_concept_name": concept["concept_name"],
            "dominant_signal": concept.get("dominant_signal"),
            "confidence": round(score, 6),
            "reasoning": _short_reasoning(post, concept),
            "is_novel": False,
            "risk_level": concept.get("risk_level", "medium"),
            "language": detect_language(post),
            "post_hash": _content_hash(post),
            "llm_prompt_hash": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
            "llm_backend": "local_concept_match_policy_v1",
            "related_concepts": related_concepts,
            "raw_post_included": False,
        }
    if log:
        log_match_result(result)
    return result


def log_match_result(result: dict[str, Any], *, concepts_dir: Path = CONCEPTS_DIR) -> None:
    """Append match, reasoning, and novelty logs without raw content."""
    concepts_dir.mkdir(parents=True, exist_ok=True)
    _append_jsonl(concepts_dir / "match_results.jsonl", result)
    _append_jsonl(
        concepts_dir / "reasoning_trace.jsonl",
        {
            "schema_version": "reasoning_trace_v1",
            "timestamp": utc_now(),
            "matched_concept": result.get("matched_concept"),
            "confidence": result.get("confidence"),
            "reasoning": result.get("reasoning"),
            "is_novel": result.get("is_novel"),
            "post_hash": result.get("post_hash"),
            "raw_post_included": False,
        },
    )
    if result.get("is_novel"):
        _append_jsonl(
            concepts_dir / "new_cluster_pool.jsonl",
            {
                "schema_version": "new_cluster_pool_v1",
                "timestamp": utc_now(),
                "post_hash": result.get("post_hash"),
                "language": result.get("language"),
                "reason": result.get("reasoning"),
                "trigger_future_clustering": True,
                "raw_post_included": False,
            },
        )


def _concept_score(post: str, concept: dict[str, Any]) -> float:
    text = post.lower()
    keywords = [str(keyword).lower() for keyword in concept.get("keywords", [])]
    keyword_hits = sum(1 for keyword in keywords if keyword and keyword in text)
    keyword_score = min(0.4, keyword_hits * 0.1)
    signal_score = _signal_score(text, str(concept.get("dominant_signal", "")))
    risk_score = {"high": 0.12, "medium": 0.08, "low": 0.0}.get(str(concept.get("risk_level", "low")), 0.0)
    return max(0.0, min(0.95, keyword_score + signal_score + risk_score))


def _related_concepts(scored: list[tuple[float, dict[str, Any]]]) -> list[dict[str, Any]]:
    related = []
    for score, concept in scored:
        if score < 0.3:
            continue
        related.append(
            {
                "concept_id": concept.get("concept_id"),
                "concept_name": concept.get("concept_name"),
                "confidence": round(score, 6),
                "dominant_signal": concept.get("dominant_signal"),
            }
        )
    return related[:4]


def _signal_score(text: str, signal: str) -> float:
    checks = {
        "guaranteed_return": ("保證", "穩賺", "零風險", "保本", "翻倍", "收益"),
        "authority_impersonation": ("老師", "助理", "分析師", "專家", "官方", "帶單"),
        "off_platform_contact": ("line", "telegram", "whatsapp", "私訊", "dm", "加群", "群組", "社群"),
        "urgency": ("限時", "名額", "倒數", "最後", "立刻", "開盤"),
        "hard_negative_warning": ("反詐", "不要相信", "風險", "虧損", "金融教育"),
    }
    terms = checks.get(signal, ())
    hits = sum(1 for term in terms if term in text)
    return min(0.48, hits * 0.16)


def _short_reasoning(post: str, concept: dict[str, Any]) -> str:
    signal = str(concept.get("dominant_signal", ""))
    if signal == "off_platform_contact":
        return "Matches private-channel migration signals."
    if signal == "authority_impersonation":
        return "Matches expert or assistant authority framing."
    if signal == "guaranteed_return":
        return "Matches guaranteed-return investment framing."
    if signal == "urgency":
        return "Matches urgency pressure around investment action."
    return "Matches risk-warning hard-negative concept."


def _novel_result(post: str, prompt: str, reason: str) -> dict[str, Any]:
    return {
        "schema_version": "concept_match_v1",
        "matched_concept": None,
        "matched_concept_name": None,
        "dominant_signal": None,
        "confidence": 0.0,
        "reasoning": reason,
        "is_novel": True,
        "risk_level": "unknown",
        "language": detect_language(post),
        "post_hash": _content_hash(post),
        "llm_prompt_hash": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
        "llm_backend": "local_concept_match_policy_v1",
        "related_concepts": [],
        "raw_post_included": False,
    }


def _has_high_risk_language(post: str) -> bool:
    text = post.lower()
    return any(term in text for term in ("保證", "穩賺", "line", "私訊", "加群", "老師", "助理"))


def _content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _append_jsonl(path: Path, entry: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n")
