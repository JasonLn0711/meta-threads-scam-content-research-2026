"""Append-only hash-chained audit logging for Evidence Layer v1."""

from __future__ import annotations

import json
import os
import uuid
import fcntl
from pathlib import Path
from typing import Any

from .hashing import compute_sha256
from .storage import AUDIT_LOG_FILE, ensure_evidence_directories, utc_now


GENESIS_PREVIOUS_HASH = "0" * 64
AUDIT_SCHEMA_VERSION = "audit_log_v1"


def canonical_entry_bytes(entry: dict[str, Any]) -> bytes:
    material = {key: value for key, value in entry.items() if key != "entry_hash"}
    return json.dumps(material, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def compute_audit_entry_hash(entry: dict[str, Any]) -> str:
    return compute_sha256(canonical_entry_bytes(entry))


def append_audit_log(
    entity_id: str,
    action: str,
    actor: str,
    details: dict[str, Any] | None = None,
    *,
    log_path: Path = AUDIT_LOG_FILE,
) -> dict[str, Any]:
    """Append one audit entry with previous_hash and entry_hash."""
    ensure_evidence_directories()
    if log_path.exists() and (not log_path.is_file() or log_path.is_symlink()):
        raise ValueError(f"audit log path is not a regular file: {log_path}")
    log_path.parent.mkdir(parents=True, exist_ok=True)

    flags = os.O_RDWR | os.O_CREAT | os.O_APPEND
    fd = os.open(log_path, flags, 0o600)
    with os.fdopen(fd, "a+", encoding="utf-8") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        entry = {
            "schema_version": AUDIT_SCHEMA_VERSION,
            "log_id": str(uuid.uuid4()),
            "timestamp": utc_now(),
            "entity_id": entity_id,
            "action": action,
            "actor": actor,
            "previous_hash": last_entry_hash_from_handle(handle),
            "details": details or {},
        }
        entry["entry_hash"] = compute_audit_entry_hash(entry)
        line = json.dumps(entry, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
        handle.write(line)
        handle.flush()
        os.fsync(handle.fileno())
        fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        return entry


def last_entry_hash(log_path: Path = AUDIT_LOG_FILE) -> str:
    if not log_path.exists() or log_path.stat().st_size == 0:
        return GENESIS_PREVIOUS_HASH
    with log_path.open("r", encoding="utf-8") as handle:
        return last_entry_hash_from_handle(handle)


def last_entry_hash_from_handle(handle: Any) -> str:
    handle.seek(0)
    last_line = ""
    for line in handle:
        stripped = line.strip()
        if stripped:
            last_line = stripped
    if not last_line:
        return GENESIS_PREVIOUS_HASH
    entry = json.loads(last_line)
    entry_hash = entry.get("entry_hash")
    if not isinstance(entry_hash, str) or len(entry_hash) != 64:
        raise ValueError("last audit entry is missing a valid entry_hash")
    return entry_hash


def append_jsonl(path: Path, entry: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(entry, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    flags = os.O_WRONLY | os.O_CREAT | os.O_APPEND
    fd = os.open(path, flags, 0o600)
    with os.fdopen(fd, "a", encoding="utf-8") as handle:
        handle.write(line)
        handle.flush()
        os.fsync(handle.fileno())


def verify_chain(log_path: Path = AUDIT_LOG_FILE) -> dict[str, Any]:
    """Verify the JSONL audit hash chain and return a machine-readable result."""
    if not log_path.exists():
        return {
            "valid": True,
            "checked_entries": 0,
            "last_hash": GENESIS_PREVIOUS_HASH,
            "log_path": str(log_path),
            "errors": [],
        }

    errors: list[str] = []
    previous_hash = GENESIS_PREVIOUS_HASH
    checked_entries = 0

    with log_path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            stripped = line.strip()
            if not stripped:
                continue
            checked_entries += 1
            try:
                entry = json.loads(stripped)
            except json.JSONDecodeError as exc:
                errors.append(f"line {line_number}: invalid JSON: {exc}")
                break

            stored_previous = entry.get("previous_hash")
            if stored_previous != previous_hash:
                errors.append(
                    f"line {line_number}: previous_hash {stored_previous!r} does not match expected {previous_hash!r}"
                )

            stored_entry_hash = entry.get("entry_hash")
            computed_entry_hash = compute_audit_entry_hash(entry)
            if stored_entry_hash != computed_entry_hash:
                errors.append(
                    f"line {line_number}: entry_hash {stored_entry_hash!r} does not match computed {computed_entry_hash!r}"
                )

            previous_hash = stored_entry_hash if isinstance(stored_entry_hash, str) else ""

    return {
        "valid": not errors,
        "checked_entries": checked_entries,
        "last_hash": previous_hash if checked_entries else GENESIS_PREVIOUS_HASH,
        "log_path": str(log_path),
        "errors": errors,
    }
