"""Metadata-only candidate builder for closed-loop discovery runs."""

from __future__ import annotations

import json
import uuid
from pathlib import Path
from typing import Any

from src.evidence.hashing import compute_sha256
from src.evidence.storage import CANDIDATE_INTAKE_DIR, utc_now


KEYWORDS = {
    "guaranteed_return": ("保證獲利", "保證收益", "穩賺", "零風險", "保本獲利", "翻倍", "guaranteed return"),
    "impersonation": ("老師", "助理", "分析師", "專家", "官方", "投資顧問", "mentor", "analyst"),
    "off_platform_contact": ("LINE", "Telegram", "WhatsApp", "私訊", "DM", "加群", "群組", "社群"),
    "urgency": ("限時", "名額", "倒數", "最後", "今天", "立刻", "盤前", "開盤前"),
    "hard_negative_warning": ("反詐", "不要相信", "風險", "虧損", "自行研究", "金融教育", "沒有邀請"),
}


def create_candidate(
    evidence_id: str,
    raw_text: str,
    *,
    query_id: str = "",
    source_item_id: str = "",
    evidence_hash: str | None = None,
) -> dict[str, Any]:
    """Build a candidate without storing raw content in the candidate record."""
    features = extract_features(raw_text)
    return {
        "schema_version": "closed_loop_candidate_v1",
        "candidate_id": f"candidate_{uuid.uuid4()}",
        "created_at": utc_now(),
        "query_id": query_id,
        "source_item_id": source_item_id,
        "evidence_ref": {
            "evidence_id": evidence_id,
            "hash_algorithm": "sha256",
            "sha256": evidence_hash or compute_sha256(raw_text),
        },
        "features": features,
        "score": 0.0,
        "raw_content_included": False,
        "human_decision_required": True,
    }


def extract_features(raw_text: str) -> dict[str, Any]:
    """Extract simple keyword features for ranking only, not final labeling."""
    normalized = raw_text.lower()
    features: dict[str, Any] = {}
    for feature_name, keywords in KEYWORDS.items():
        matched = [keyword for keyword in keywords if keyword.lower() in normalized]
        features[feature_name] = bool(matched)
        features[f"{feature_name}_matches"] = matched[:3]
    features["feature_count"] = sum(
        1 for key, value in features.items() if key in KEYWORDS and key != "hard_negative_warning" and value
    )
    return features


def write_candidate_batch(
    candidates: list[dict[str, Any]],
    *,
    round_number: int,
    output_dir: Path = CANDIDATE_INTAKE_DIR,
) -> Path:
    """Persist selected metadata-only candidates as JSONL."""
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"closed_loop_round_{round_number:04d}_candidates.jsonl"
    with path.open("w", encoding="utf-8") as handle:
        for candidate in candidates:
            handle.write(json.dumps(candidate, ensure_ascii=False, sort_keys=True) + "\n")
    return path
