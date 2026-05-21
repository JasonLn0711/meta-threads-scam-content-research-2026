"""Small deterministic embedding encoder for synthetic discovery experiments."""

from __future__ import annotations

import hashlib
import math
import re


EMBEDDING_DIM = 32
TOKEN_PATTERN = re.compile(r"[A-Za-z0-9_]+|[\u4e00-\u9fff]")


def encode(text: str, *, dim: int = EMBEDDING_DIM) -> list[float]:
    """Return a deterministic normalized vector for text."""
    if dim < 4:
        raise ValueError("embedding dim must be at least 4")

    vector = [0.0] * dim
    tokens = _tokens(text)
    for token in tokens:
        digest = hashlib.blake2b(token.encode("utf-8"), digest_size=8).digest()
        bucket = int.from_bytes(digest[:4], "big") % dim
        sign = 1.0 if digest[4] % 2 == 0 else -1.0
        vector[bucket] += sign

    norm = math.sqrt(sum(value * value for value in vector))
    if norm == 0:
        return vector
    return [round(value / norm, 8) for value in vector]


def detect_language(text: str) -> str:
    """Return a coarse language tag suitable for metadata-only routing."""
    cjk = sum(1 for char in text if "\u4e00" <= char <= "\u9fff")
    ascii_letters = sum(1 for char in text if char.isascii() and char.isalpha())
    if cjk and cjk >= ascii_letters:
        return "zh-Hant"
    if ascii_letters:
        return "en"
    return "unknown"


def cosine_similarity(left: list[float], right: list[float]) -> float:
    _check_same_dim(left, right)
    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    dot = sum(a * b for a, b in zip(left, right))
    return dot / (left_norm * right_norm)


def euclidean_distance(left: list[float], right: list[float]) -> float:
    _check_same_dim(left, right)
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(left, right)))


def _tokens(text: str) -> list[str]:
    normalized = text.lower()
    tokens = TOKEN_PATTERN.findall(normalized)
    if not tokens and normalized.strip():
        tokens = [normalized.strip()]
    bigrams = [f"{a}{b}" for a, b in zip(tokens, tokens[1:])]
    return tokens + bigrams


def _check_same_dim(left: list[float], right: list[float]) -> None:
    if len(left) != len(right):
        raise ValueError(f"dimension mismatch: {len(left)} != {len(right)}")
