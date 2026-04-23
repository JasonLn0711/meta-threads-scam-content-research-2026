"""Config-driven scoring for rule-baseline signals."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

from .taxonomy import REASON_CODE_ORDER
from .types import MatchedSignal, RuleConfig, ScoreBreakdown


def load_rule_config(path: str | Path) -> RuleConfig:
    config_path = Path(path)
    data = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{config_path} must contain a YAML mapping")
    scoring = data.get("scoring", {})
    return RuleConfig(
        signal_weights={
            str(key): float(value)
            for key, value in data.get("signal_weights", {}).items()
        },
        thresholds=dict(scoring.get("thresholds", {})),
        combination_bonuses=list(scoring.get("combination_bonuses", [])),
        subtype_mappings=list(scoring.get("subtype_mappings", [])),
        reason_code_order=list(data.get("reason_code_order", REASON_CODE_ORDER)),
        max_signal_instances_per_code=int(scoring.get("max_signal_instances_per_code", 2)),
    )


def score_signals(signals: list[MatchedSignal], config: RuleConfig) -> ScoreBreakdown:
    signal_counts: Counter[str] = Counter()
    category_counts: Counter[str] = Counter()
    signal_scores: defaultdict[str, float] = defaultdict(float)
    base_score = 0.0

    for signal in signals:
        if signal_counts[signal.signal_code] >= config.max_signal_instances_per_code:
            continue
        signal_counts[signal.signal_code] += 1
        category_counts[signal.category] += 1
        signal_scores[signal.signal_code] += float(signal.weight)
        base_score += float(signal.weight)

    applied_bonuses = _apply_combination_bonuses(signals, config)
    bonus_score = sum(float(bonus["weight"]) for bonus in applied_bonuses)
    total_score = base_score + bonus_score
    high_guardrail_passed = _high_guardrail_passed(total_score, category_counts, config)

    return ScoreBreakdown(
        base_signal_score=base_score,
        bonus_score=bonus_score,
        total_score=total_score,
        category_counts=dict(category_counts),
        signal_scores=dict(signal_scores),
        applied_bonuses=applied_bonuses,
        high_guardrail_passed=high_guardrail_passed,
    )


def assign_risk_level(score: ScoreBreakdown, config: RuleConfig) -> str:
    medium_threshold = float(config.thresholds.get("medium_threshold", 5))
    high_threshold = float(config.thresholds.get("high_threshold", 9))

    if score.total_score >= high_threshold and score.high_guardrail_passed:
        return "high"
    if score.total_score >= medium_threshold:
        return "medium"
    return "low"


def assign_binary_prediction(risk_level: str, config: RuleConfig) -> str:
    policy = str(config.thresholds.get("binary_positive_policy", "medium_or_high"))
    if policy == "high_only":
        return "scam_like" if risk_level == "high" else "not_scam_like"
    if policy == "medium_or_high":
        return "scam_like" if risk_level in {"medium", "high"} else "not_scam_like"
    raise ValueError(f"Unsupported binary_positive_policy: {policy}")


def infer_subtype_hint(
    signals: list[MatchedSignal],
    score: ScoreBreakdown,
    config: RuleConfig,
) -> str | None:
    signal_codes = {signal.signal_code for signal in signals}
    categories = {signal.category for signal in signals}

    for mapping in config.subtype_mappings:
        min_score = float(mapping.get("min_total_score", 0))
        if score.total_score < min_score:
            continue
        required_all = set(mapping.get("required_all_signal_codes", []))
        if required_all and not required_all <= signal_codes:
            continue
        required_any = set(mapping.get("required_any_signal_codes", []))
        if required_any and not required_any & signal_codes:
            continue
        required_categories = set(mapping.get("required_any_categories", []))
        if required_categories and not required_categories & categories:
            continue
        return str(mapping["subtype"])
    return None


def reason_codes_from_score(
    signals: list[MatchedSignal],
    score: ScoreBreakdown,
    config: RuleConfig,
) -> list[str]:
    codes = {signal.reason_code for signal in signals}
    for bonus in score.applied_bonuses:
        reason_code = bonus.get("reason_code")
        if reason_code:
            codes.add(str(reason_code))
    return _ordered_codes(codes, config.reason_code_order)


def _apply_combination_bonuses(
    signals: list[MatchedSignal],
    config: RuleConfig,
) -> list[dict[str, Any]]:
    categories = {signal.category for signal in signals}
    signal_codes = {signal.signal_code for signal in signals}
    bonuses: list[dict[str, Any]] = []

    for bonus in config.combination_bonuses:
        required_categories = set(bonus.get("required_categories", []))
        required_signals = set(bonus.get("required_signal_codes", []))
        min_categories = int(bonus.get("min_categories", 0))

        if required_categories and not required_categories <= categories:
            continue
        if required_signals and not required_signals <= signal_codes:
            continue
        if min_categories and len(categories) < min_categories:
            continue

        bonuses.append(
            {
                "code": str(bonus["code"]),
                "reason_code": str(bonus.get("reason_code", "")),
                "weight": float(bonus.get("weight", 0)),
                "description": str(bonus.get("description", "")),
            }
        )
    return bonuses


def _high_guardrail_passed(
    total_score: float,
    category_counts: Counter[str],
    config: RuleConfig,
) -> bool:
    high_threshold = float(config.thresholds.get("high_threshold", 9))
    if total_score < high_threshold:
        return False
    min_categories = int(config.thresholds.get("high_min_categories", 2))
    return len(category_counts) >= min_categories


def _ordered_codes(codes: set[str], order: list[str]) -> list[str]:
    order_index = {code: index for index, code in enumerate(order)}
    return sorted(codes, key=lambda code: (order_index.get(code, 999), code))
