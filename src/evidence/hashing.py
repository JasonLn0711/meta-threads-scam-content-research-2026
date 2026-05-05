"""Deterministic hashing helpers for Evidence Layer v1."""

from __future__ import annotations

import hashlib


HashableContent = str | bytes | bytearray | memoryview


def content_to_bytes(content: HashableContent) -> bytes:
    """Return deterministic bytes for supported text or binary content."""
    if isinstance(content, str):
        return content.encode("utf-8")
    if isinstance(content, bytes):
        return content
    if isinstance(content, bytearray):
        return bytes(content)
    if isinstance(content, memoryview):
        return content.tobytes()
    raise TypeError(f"unsupported content type for hashing: {type(content).__name__}")


def compute_sha256(content: HashableContent) -> str:
    """Compute a SHA-256 digest as a lowercase hex string."""
    return hashlib.sha256(content_to_bytes(content)).hexdigest()
