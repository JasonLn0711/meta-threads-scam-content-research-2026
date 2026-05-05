"""Temporal concept tracking for synthetic dynamic intelligence."""

from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

from src.evidence.storage import REPO_ROOT, utc_now
from src.intelligence.yaml_store import write_yaml


CONCEPT_TIME_SERIES_PATH = REPO_ROOT / "data/concept_time_series.yaml"


def track_concept_over_time(
    concepts: list[dict[str, Any]],
    timestamps: list[dict[str, Any]] | dict[str, Any],
    *,
    output_path: Path = CONCEPT_TIME_SERIES_PATH,
) -> dict[str, Any]:
    """Compute frequency, scam rate, and growth by concept and time bucket."""
    concept_lookup = {str(concept.get("concept_id")): concept for concept in concepts if concept.get("concept_id")}
    events = _normalize_events(timestamps)
    grouped: dict[str, dict[str, list[dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    for event in events:
        concept_id = str(event.get("concept_id") or "")
        if not concept_id:
            continue
        period = str(event.get("period") or _week_bucket(str(event.get("timestamp", ""))))
        grouped[concept_id][period].append(event)

    series = []
    for concept_id, periods in sorted(grouped.items()):
        previous_frequency = 0
        rows = []
        for period, period_events in sorted(periods.items()):
            frequency = len(period_events)
            scam_count = sum(1 for event in period_events if event.get("decision") == "scam" or event.get("high_value"))
            reviewed_count = sum(1 for event in period_events if event.get("decision") in {"scam", "non_scam", "uncertain"})
            growth = _growth(previous_frequency, frequency)
            rows.append(
                {
                    "period": period,
                    "frequency": frequency,
                    "reviewed_count": reviewed_count,
                    "scam_count": scam_count,
                    "scam_rate": round(scam_count / reviewed_count, 6) if reviewed_count else 0.0,
                    "growth": growth,
                }
            )
            previous_frequency = frequency
        concept = concept_lookup.get(concept_id, {})
        series.append(
            {
                "concept_id": concept_id,
                "concept_name": concept.get("concept_name"),
                "dominant_signal": concept.get("dominant_signal"),
                "risk_level": concept.get("risk_level", "unknown"),
                "time_series": rows,
            }
        )

    payload = {
        "schema_version": "concept_time_series_v1",
        "generated_at": utc_now(),
        "concepts": series,
        "summary": _summary(series),
        "raw_content_included": False,
    }
    write_yaml(output_path, payload)
    return payload


def _normalize_events(timestamps: list[dict[str, Any]] | dict[str, Any]) -> list[dict[str, Any]]:
    if isinstance(timestamps, list):
        return [event for event in timestamps if isinstance(event, dict)]
    events: list[dict[str, Any]] = []
    for concept_id, values in timestamps.items():
        if isinstance(values, list):
            for value in values:
                if isinstance(value, dict):
                    event = dict(value)
                    event.setdefault("concept_id", concept_id)
                    events.append(event)
                else:
                    events.append({"concept_id": concept_id, "timestamp": str(value)})
        else:
            events.append({"concept_id": concept_id, "timestamp": str(values)})
    return events


def _week_bucket(timestamp: str) -> str:
    if not timestamp:
        return "unknown"
    try:
        parsed = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    except ValueError:
        return timestamp[:10] if len(timestamp) >= 10 else "unknown"
    year, week, _ = parsed.isocalendar()
    return f"{year}-W{week:02d}"


def _growth(previous: int, current: int) -> float:
    if previous == 0:
        return 1.0 if current > 0 else 0.0
    return round((current - previous) / previous, 6)


def _summary(series: list[dict[str, Any]]) -> dict[str, Any]:
    growing = []
    for concept in series:
        rows = concept.get("time_series", [])
        if rows and float(rows[-1].get("growth", 0.0) or 0.0) > 0:
            growing.append(
                {
                    "concept_id": concept.get("concept_id"),
                    "growth": rows[-1].get("growth"),
                    "frequency": rows[-1].get("frequency"),
                }
            )
    growing = sorted(growing, key=lambda row: (-float(row["growth"]), str(row["concept_id"])))[:5]
    return {
        "concept_count": len(series),
        "growing_concepts": growing,
    }
