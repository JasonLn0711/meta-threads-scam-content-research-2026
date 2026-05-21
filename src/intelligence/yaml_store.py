"""Tiny deterministic YAML writer for metadata-only intelligence outputs."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def write_yaml(path: Path, payload: dict[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(to_yaml(payload) + "\n", encoding="utf-8")
    return path


def to_yaml(value: Any, *, indent: int = 0) -> str:
    lines = _render(value, indent)
    return "\n".join(lines)


def _render(value: Any, indent: int) -> list[str]:
    prefix = " " * indent
    if isinstance(value, dict):
        lines: list[str] = []
        for key in sorted(value.keys(), key=str):
            item = value[key]
            if _is_scalar(item):
                lines.append(f"{prefix}{key}: {_scalar(item)}")
            else:
                lines.append(f"{prefix}{key}:")
                lines.extend(_render(item, indent + 2))
        return lines or [f"{prefix}{{}}"]
    if isinstance(value, list):
        lines = []
        for item in value:
            if _is_scalar(item):
                lines.append(f"{prefix}- {_scalar(item)}")
            elif isinstance(item, dict):
                lines.append(f"{prefix}-")
                lines.extend(_render(item, indent + 2))
            else:
                lines.append(f"{prefix}-")
                lines.extend(_render(item, indent + 2))
        return lines or [f"{prefix}[]"]
    return [f"{prefix}{_scalar(value)}"]


def _is_scalar(value: Any) -> bool:
    return value is None or isinstance(value, (str, int, float, bool))


def _scalar(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if text == "" or any(char in text for char in ":#[]{}&*?|-<>=!%@\\\n"):
        return json.dumps(text, ensure_ascii=False)
    return text
