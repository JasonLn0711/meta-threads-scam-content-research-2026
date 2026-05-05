"""Evidence ingestion and metadata-only candidate stub creation."""

from __future__ import annotations

import json
import re
import uuid
from typing import Any

from .audit import append_audit_log
from .hashing import compute_sha256
from .storage import (
    REPO_ROOT,
    STUB_SCHEMA_VERSION,
    coerce_score,
    load_evidence_record,
    normalize_input,
    normalize_source_info,
    save_candidate_stub,
    store_evidence_record,
    utc_now,
    verify_evidence_integrity,
)


FORBIDDEN_STUB_KEYS = {
    "browser_export",
    "browser_profile",
    "content",
    "controlled_store_path",
    "cookie",
    "credential",
    "external_link",
    "external_links",
    "handle",
    "image_path",
    "image_paths",
    "ocr_text",
    "post_text",
    "profile_url",
    "raw_content",
    "raw_text",
    "raw_threads_content",
    "reply_text",
    "reply_texts",
    "screenshot",
    "screenshot_path",
    "session",
    "token",
    "url",
    "urls",
    "user_id",
    "username",
    "visible_contact_handles",
}
FORBIDDEN_STUB_PATTERN = re.compile(r"https?://|www\.|@[A-Za-z0-9_]{2,}|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def ingest_evidence(raw_input: Any, source_info: str | dict[str, Any], actor: str = "system") -> dict[str, str]:
    """Normalize, hash, store, and audit one controlled evidence item."""
    normalized_payload, content_bytes = normalize_input(raw_input)
    sha256_hash = compute_sha256(content_bytes)
    evidence_id = str(uuid.uuid4())
    normalized_source = normalize_source_info(source_info)

    store_evidence_record(
        evidence_id=evidence_id,
        normalized_payload=normalized_payload,
        sha256_hash=sha256_hash,
        source_info=normalized_source,
        actor=actor,
    )
    append_audit_log(
        evidence_id,
        "ingest",
        actor,
        details={
            "hash_algorithm": "sha256",
            "sha256": sha256_hash,
            "source_type": safe_source_type(normalized_source),
        },
    )
    return {"evidence_id": evidence_id, "sha256": sha256_hash}


def create_candidate_stub(evidence_id: str, features: dict[str, Any], score: int | float | str) -> dict[str, str]:
    """Create a metadata-only candidate stub linked to a controlled evidence hash."""
    validate_metadata_only_features(features)
    evidence_hash = verify_evidence_integrity(evidence_id)
    evidence_record = load_evidence_record(evidence_id)
    candidate_id = f"candidate_stub_{uuid.uuid4()}"
    stub = {
        "schema_version": STUB_SCHEMA_VERSION,
        "candidate_id": candidate_id,
        "created_at": utc_now(),
        "evidence_ref": {
            "evidence_id": evidence_id,
            "hash_algorithm": "sha256",
            "sha256": evidence_hash,
        },
        "evidence_hash": evidence_hash,
        "features": features,
        "score": coerce_score(score),
        "raw_content_included": False,
        "human_decision_required": True,
        "source_type": safe_source_type(evidence_record.get("source_info", {})),
    }
    path = save_candidate_stub(stub)
    try:
        relative_path = str(path.relative_to(REPO_ROOT))
    except ValueError:
        relative_path = str(path)
    append_audit_log(
        evidence_id,
        "candidate_stub_create",
        "system",
        details={
            "candidate_id": candidate_id,
            "candidate_path": relative_path,
            "raw_content_included": False,
        },
    )
    return {
        "candidate_id": candidate_id,
        "candidate_path": str(path),
        "evidence_id": evidence_id,
        "sha256": evidence_hash,
    }


def validate_metadata_only_features(features: dict[str, Any]) -> None:
    if not isinstance(features, dict):
        raise TypeError("features must be a dictionary")
    json.dumps(features, ensure_ascii=False, sort_keys=True)
    _walk_metadata_only(features)


def safe_source_type(source_info: dict[str, Any]) -> str:
    raw_value = str(source_info.get("source") or source_info.get("source_type") or "")
    if FORBIDDEN_STUB_PATTERN.search(raw_value):
        return "[redacted_source]"
    return raw_value


def _walk_metadata_only(value: Any, path: str = "features") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            key_text = str(key)
            normalized_key = key_text.lower()
            if normalized_key in FORBIDDEN_STUB_KEYS:
                raise ValueError(f"candidate stub feature {path}.{key_text} is forbidden metadata")
            _walk_metadata_only(child, f"{path}.{key_text}")
        return
    if isinstance(value, list):
        for index, child in enumerate(value):
            _walk_metadata_only(child, f"{path}[{index}]")
        return
    if isinstance(value, str) and FORBIDDEN_STUB_PATTERN.search(value):
        raise ValueError(f"candidate stub feature {path} appears to contain raw locator or contact data")
