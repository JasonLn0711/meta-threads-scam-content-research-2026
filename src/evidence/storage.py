"""Local controlled-store helpers for Evidence Layer v1."""

from __future__ import annotations

import base64
import json
import math
import os
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .hashing import compute_sha256, content_to_bytes


SCHEMA_VERSION = "evidence_store_v1"
STUB_SCHEMA_VERSION = "candidate_stub_v1"
REPO_ROOT = Path(__file__).resolve().parents[2]
EVIDENCE_STORE_DIR = Path(os.environ.get("EVIDENCE_STORE_DIR", REPO_ROOT / "data/evidence_store")).expanduser()
AUDIT_LOG_DIR = Path(os.environ.get("EVIDENCE_AUDIT_LOG_DIR", REPO_ROOT / "data/audit_logs")).expanduser()
AUDIT_LOG_FILE = AUDIT_LOG_DIR / "evidence_audit.jsonl"
CANDIDATE_INTAKE_DIR = Path(
    os.environ.get("EVIDENCE_CANDIDATE_INTAKE_DIR", REPO_ROOT / "data/candidate_intake")
).expanduser()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def ensure_evidence_directories() -> None:
    for directory in (EVIDENCE_STORE_DIR, AUDIT_LOG_DIR):
        directory.mkdir(parents=True, exist_ok=True)
        os.chmod(directory, 0o700)
    CANDIDATE_INTAKE_DIR.mkdir(parents=True, exist_ok=True)


def normalize_source_info(source_info: str | dict[str, Any] | None) -> dict[str, Any]:
    if source_info is None:
        return {}
    if isinstance(source_info, str):
        return {"source": source_info}
    if isinstance(source_info, dict):
        json.dumps(source_info, ensure_ascii=False, sort_keys=True)
        return dict(source_info)
    raise TypeError("source_info must be a string, dict, or None")


def normalize_input(raw_input: Any) -> tuple[dict[str, Any], bytes]:
    """Normalize supported input into a stored JSON payload plus hash bytes."""
    if isinstance(raw_input, str):
        content_bytes = raw_input.encode("utf-8")
        payload = {
            "content_type": "text",
            "content_encoding": "utf-8",
            "content": raw_input,
        }
    elif isinstance(raw_input, (bytes, bytearray, memoryview)):
        content_bytes = content_to_bytes(raw_input)
        payload = {
            "content_type": "binary",
            "content_encoding": "base64",
            "content": base64.b64encode(content_bytes).decode("ascii"),
        }
    elif isinstance(raw_input, (dict, list)):
        canonical = json.dumps(raw_input, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        content_bytes = canonical.encode("utf-8")
        payload = {
            "content_type": "json",
            "content_encoding": "utf-8",
            "content": canonical,
        }
    else:
        raise TypeError(f"unsupported evidence input type: {type(raw_input).__name__}")

    payload["byte_length"] = len(content_bytes)
    return payload, content_bytes


def validate_evidence_id(evidence_id: str) -> str:
    try:
        parsed = uuid.UUID(str(evidence_id))
    except ValueError as exc:
        raise ValueError(f"invalid evidence_id: {evidence_id!r}") from exc
    normalized = str(parsed)
    if normalized != str(evidence_id):
        raise ValueError(f"evidence_id must be canonical UUID form: {evidence_id!r}")
    return normalized


def evidence_path(evidence_id: str) -> Path:
    return EVIDENCE_STORE_DIR / f"{validate_evidence_id(evidence_id)}.json"


def store_evidence_record(
    *,
    evidence_id: str,
    normalized_payload: dict[str, Any],
    sha256_hash: str,
    source_info: dict[str, Any],
    actor: str,
) -> Path:
    ensure_evidence_directories()
    record = {
        "schema_version": SCHEMA_VERSION,
        "evidence_id": validate_evidence_id(evidence_id),
        "created_at": utc_now(),
        "actor": actor,
        "hash_algorithm": "sha256",
        "sha256": sha256_hash,
        "source_info": source_info,
        "storage_boundary": "local_controlled_store",
        **normalized_payload,
    }
    path = evidence_path(evidence_id)
    write_json_exclusive(path, record, mode=0o600)
    return path


def load_evidence_record(evidence_id: str) -> dict[str, Any]:
    path = evidence_path(evidence_id)
    if not path.exists():
        raise FileNotFoundError(f"evidence record not found: {path}")
    if not path.is_file() or path.is_symlink():
        raise ValueError(f"evidence record path is not a regular file: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"evidence record must be a JSON object: {path}")
    return data


def decode_evidence_content(record: dict[str, Any]) -> bytes:
    encoding = record.get("content_encoding")
    content = record.get("content")
    if encoding == "utf-8":
        if not isinstance(content, str):
            raise ValueError("utf-8 evidence content must be a string")
        return content.encode("utf-8")
    if encoding == "base64":
        if not isinstance(content, str):
            raise ValueError("base64 evidence content must be a string")
        return base64.b64decode(content.encode("ascii"), validate=True)
    raise ValueError(f"unsupported evidence content encoding: {encoding!r}")


def verify_evidence_integrity(evidence_id: str) -> str:
    record = load_evidence_record(evidence_id)
    content_bytes = decode_evidence_content(record)
    computed = compute_sha256(content_bytes)
    stored = record.get("sha256")
    if computed != stored:
        raise ValueError(
            f"evidence integrity failed for {evidence_id}: stored sha256 {stored!r} != recomputed {computed!r}"
        )
    return computed


def get_evidence(evidence_id: str) -> str | bytes | Any:
    """Return stored content only after SHA-256 integrity verification passes."""
    record = load_evidence_record(evidence_id)
    content_bytes = decode_evidence_content(record)
    computed = compute_sha256(content_bytes)
    if computed != record.get("sha256"):
        raise ValueError(f"evidence integrity failed for {evidence_id}")

    content_type = record.get("content_type")
    if content_type == "binary":
        return content_bytes
    if content_type == "json":
        return json.loads(content_bytes.decode("utf-8"))
    return content_bytes.decode("utf-8")


def save_candidate_stub(stub: dict[str, Any]) -> Path:
    ensure_evidence_directories()
    candidate_id = str(stub["candidate_id"])
    path = CANDIDATE_INTAKE_DIR / f"{candidate_id}.json"
    write_json_exclusive(path, stub, mode=0o600)
    return path


def coerce_score(score: int | float | str) -> float:
    value = float(score)
    if not math.isfinite(value):
        raise ValueError("score must be finite")
    return value


def write_json_exclusive(path: Path, data: dict[str, Any], *, mode: int = 0o600) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    fd = os.open(path, flags, mode)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
    except Exception:
        try:
            path.unlink(missing_ok=True)
        finally:
            raise
