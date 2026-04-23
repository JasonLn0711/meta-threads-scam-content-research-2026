"""Typed records for the modular rule baseline."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


VALID_VARIANTS = ("text_only", "text_reply", "text_ocr", "all")


@dataclass(frozen=True)
class ThreadItem:
    """Minimal wrapper around a schema-v1 record."""

    item_id: str
    record: dict[str, Any]

    @classmethod
    def from_record(cls, record: dict[str, Any]) -> "ThreadItem":
        return cls(item_id=str(record.get("item_id") or ""), record=record)


@dataclass(frozen=True)
class SignalDefinition:
    signal_code: str
    reason_code: str
    category: str
    description: str
    default_weight: float
    patterns: tuple[str, ...] = ()


@dataclass(frozen=True)
class MatchedSignal:
    signal_code: str
    reason_code: str
    category: str
    source_field: str
    matched_pattern: str
    matched_text: str
    weight: float
    description: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ScoreBreakdown:
    base_signal_score: float
    bonus_score: float
    total_score: float
    category_counts: dict[str, int] = field(default_factory=dict)
    signal_scores: dict[str, float] = field(default_factory=dict)
    applied_bonuses: list[dict[str, Any]] = field(default_factory=list)
    high_guardrail_passed: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "base_signal_score": round(self.base_signal_score, 3),
            "bonus_score": round(self.bonus_score, 3),
            "total_score": round(self.total_score, 3),
            "category_counts": dict(sorted(self.category_counts.items())),
            "signal_scores": {
                key: round(value, 3) for key, value in sorted(self.signal_scores.items())
            },
            "applied_bonuses": self.applied_bonuses,
            "high_guardrail_passed": self.high_guardrail_passed,
        }


@dataclass
class RuleConfig:
    signal_weights: dict[str, float]
    thresholds: dict[str, Any]
    combination_bonuses: list[dict[str, Any]]
    subtype_mappings: list[dict[str, Any]]
    reason_code_order: list[str]
    max_signal_instances_per_code: int = 2


@dataclass
class RulePrediction:
    item_id: str
    binary_pred: str
    risk_level_pred: str
    subtype_hint: str | None
    total_score: float
    reason_codes: list[str]
    explanations: list[str]
    score_breakdown: ScoreBreakdown
    matched_signals: list[MatchedSignal]
    reviewer_note: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "item_id": self.item_id,
            "binary_pred": self.binary_pred,
            "risk_level_pred": self.risk_level_pred,
            "subtype_hint": self.subtype_hint,
            "total_score": round(self.total_score, 3),
            "reason_codes": self.reason_codes,
            "explanations": self.explanations,
            "score_breakdown": self.score_breakdown.to_dict(),
            "matched_signals": [signal.to_dict() for signal in self.matched_signals],
            "reviewer_note": self.reviewer_note,
        }
