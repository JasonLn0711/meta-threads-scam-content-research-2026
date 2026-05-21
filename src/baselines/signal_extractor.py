"""Extract structured rule signals from Threads research records."""

from __future__ import annotations

import re
from collections.abc import Iterable
from typing import Any

from .taxonomy import FIELD_LABELS, SIGNAL_DEFINITIONS
from .types import MatchedSignal, RuleConfig


VARIANT_FIELDS = {
    "text_only": {"post_text"},
    "text_reply": {"post_text", "reply_texts"},
    "text_ocr": {"post_text", "ocr_text"},
    "all": {
        "post_text",
        "reply_texts",
        "ocr_text",
        "external_links",
        "visible_contact_handles",
        "visible_platform_redirects",
        "screenshot_style",
    },
}


def normalize_text(value: Any) -> str:
    if isinstance(value, list):
        value = " ".join(str(item) for item in value)
    return " ".join(str(value or "").lower().split())


def aggregate_signals(record: dict[str, Any], variant: str, config: RuleConfig) -> list[MatchedSignal]:
    if variant not in VARIANT_FIELDS:
        raise ValueError(f"Unknown baseline variant {variant!r}")

    active_fields = VARIANT_FIELDS[variant]
    signals: list[MatchedSignal] = []

    if "post_text" in active_fields:
        signals.extend(extract_textual_lure_signals(record, "post_text", config))
        signals.extend(extract_redirect_signals(record, "post_text", config))
        signals.extend(extract_urgency_signals(record, "post_text", config))
        signals.extend(extract_testimonial_signals(record, "post_text", config))
        signals.extend(extract_pseudo_official_signals(record, "post_text", config))
        signals.extend(extract_payment_credential_signals(record, "post_text", config))

    if "reply_texts" in active_fields:
        before = len(signals)
        signals.extend(extract_textual_lure_signals(record, "reply_texts", config))
        signals.extend(extract_redirect_signals(record, "reply_texts", config))
        signals.extend(extract_urgency_signals(record, "reply_texts", config))
        signals.extend(extract_testimonial_signals(record, "reply_texts", config))
        signals.extend(extract_pseudo_official_signals(record, "reply_texts", config))
        signals.extend(extract_payment_credential_signals(record, "reply_texts", config))
        if len(signals) > before:
            signals.append(_meta_signal("REPLY_FUNNEL_PATTERN", "reply_texts", config))

    if "ocr_text" in active_fields:
        before = len(signals)
        signals.extend(extract_ocr_signals(record, config))
        if len(signals) > before:
            signals.append(_meta_signal("OCR_SUSPICIOUS_TEXT", "ocr_text", config))

    if "external_links" in active_fields:
        signals.extend(extract_structured_external_link_signals(record, config))

    if "visible_contact_handles" in active_fields:
        signals.extend(extract_structured_contact_signals(record, config))

    if "visible_platform_redirects" in active_fields:
        signals.extend(extract_structured_redirect_signals(record, config))

    if "screenshot_style" in active_fields:
        signals.extend(extract_screenshot_style_signals(record, config))

    return _dedupe_signals(signals)


def extract_textual_lure_signals(
    record: dict[str, Any],
    source_field: str,
    config: RuleConfig,
) -> list[MatchedSignal]:
    return _extract_pattern_signals(
        record,
        source_field,
        (
            "GUARANTEED_PROFIT",
            "LOW_EFFORT_HIGH_RETURN",
            "PAST_PERFORMANCE_PROFIT_PROOF",
            "HIGH_FEE_COURSE_FUNNEL",
            "STOCK_RESCUE_GROUP_FUNNEL",
            "INDIVIDUAL_STOCK_ADVICE_REPLY_FUNNEL",
            "MARKET_DIRECTION_HERDING_CHORUS",
            "INSTITUTIONAL_FLOW_AUTHORITY_LURE",
            "LIFESTYLE_TRUST_MARKET_REASSURANCE_FUNNEL",
            "BEGINNER_EASY_MONEY",
            "MENTOR_COPYTRADE_LANGUAGE",
        ),
        config,
    )


def extract_redirect_signals(
    record: dict[str, Any],
    source_field: str,
    config: RuleConfig,
) -> list[MatchedSignal]:
    return _extract_pattern_signals(
        record,
        source_field,
        (
            "PRIVATE_REDIRECT",
            "IMPLICIT_DM_CONTACT_REQUEST",
            "COMMENT_CODE_LEAD_MAGNET",
            "STOCK_PICK_PLAYBOOK_KEYWORD_FUNNEL",
            "TRAPPED_POSITION_DM_PLAYBOOK_REPLY",
            "DARK_HORSE_STOCK_TARGET_PRICE_DM_FUNNEL",
            "CODED_ANIMAL_STOCK_LIMIT_UP_GROUP_FUNNEL",
            "MASS_STOCK_COMMAND_LIST_GROUP_FUNNEL",
            "TRADING_RULES_WEALTH_AUTHORITY_FOLLOW_GATE",
            "BRAND_PATENT_EXTREME_ROI_CONTACT_FUNNEL",
            "REPLY_IMPERSONATION_CONTACT_HIJACK",
            "CONTACT_HANDLE_PRESENT",
            "EXTERNAL_LINK_PRESENT",
        ),
        config,
    )


def extract_urgency_signals(
    record: dict[str, Any],
    source_field: str,
    config: RuleConfig,
) -> list[MatchedSignal]:
    return _extract_pattern_signals(record, source_field, ("URGENCY_PRESSURE",), config)


def extract_testimonial_signals(
    record: dict[str, Any],
    source_field: str,
    config: RuleConfig,
) -> list[MatchedSignal]:
    return _extract_pattern_signals(
        record,
        source_field,
        ("TESTIMONIAL_PATTERN", "SCREENSHOT_EVIDENCE"),
        config,
    )


def extract_pseudo_official_signals(
    record: dict[str, Any],
    source_field: str,
    config: RuleConfig,
) -> list[MatchedSignal]:
    return _extract_pattern_signals(
        record,
        source_field,
        ("PSEUDO_OFFICIAL_LANGUAGE", "CELEBRITY_ENDORSEMENT_PATTERN"),
        config,
    )


def extract_payment_credential_signals(
    record: dict[str, Any],
    source_field: str,
    config: RuleConfig,
) -> list[MatchedSignal]:
    return _extract_pattern_signals(record, source_field, ("PAYMENT_OR_CREDENTIAL_REQUEST",), config)


def extract_ocr_signals(record: dict[str, Any], config: RuleConfig) -> list[MatchedSignal]:
    signals: list[MatchedSignal] = []
    for signal_codes in (
        (
            "GUARANTEED_PROFIT",
            "LOW_EFFORT_HIGH_RETURN",
            "PAST_PERFORMANCE_PROFIT_PROOF",
            "HIGH_FEE_COURSE_FUNNEL",
            "STOCK_RESCUE_GROUP_FUNNEL",
            "INDIVIDUAL_STOCK_ADVICE_REPLY_FUNNEL",
            "MARKET_DIRECTION_HERDING_CHORUS",
            "INSTITUTIONAL_FLOW_AUTHORITY_LURE",
            "LIFESTYLE_TRUST_MARKET_REASSURANCE_FUNNEL",
            "BEGINNER_EASY_MONEY",
            "MENTOR_COPYTRADE_LANGUAGE",
        ),
        (
            "PRIVATE_REDIRECT",
            "IMPLICIT_DM_CONTACT_REQUEST",
            "COMMENT_CODE_LEAD_MAGNET",
            "STOCK_PICK_PLAYBOOK_KEYWORD_FUNNEL",
            "TRAPPED_POSITION_DM_PLAYBOOK_REPLY",
            "DARK_HORSE_STOCK_TARGET_PRICE_DM_FUNNEL",
            "CODED_ANIMAL_STOCK_LIMIT_UP_GROUP_FUNNEL",
            "MASS_STOCK_COMMAND_LIST_GROUP_FUNNEL",
            "TRADING_RULES_WEALTH_AUTHORITY_FOLLOW_GATE",
            "BRAND_PATENT_EXTREME_ROI_CONTACT_FUNNEL",
            "REPLY_IMPERSONATION_CONTACT_HIJACK",
            "CONTACT_HANDLE_PRESENT",
            "EXTERNAL_LINK_PRESENT",
        ),
        ("URGENCY_PRESSURE",),
        ("TESTIMONIAL_PATTERN", "SCREENSHOT_EVIDENCE"),
        ("PSEUDO_OFFICIAL_LANGUAGE", "CELEBRITY_ENDORSEMENT_PATTERN"),
        ("PAYMENT_OR_CREDENTIAL_REQUEST",),
    ):
        signals.extend(_extract_pattern_signals(record, "ocr_text", signal_codes, config))
    return signals


def extract_reply_funnel_signals(record: dict[str, Any], config: RuleConfig) -> list[MatchedSignal]:
    reply_signals = []
    reply_signals.extend(extract_redirect_signals(record, "reply_texts", config))
    reply_signals.extend(extract_payment_credential_signals(record, "reply_texts", config))
    if reply_signals:
        reply_signals.append(_meta_signal("REPLY_FUNNEL_PATTERN", "reply_texts", config))
    return _dedupe_signals(reply_signals)


def extract_structured_external_link_signals(
    record: dict[str, Any],
    config: RuleConfig,
) -> list[MatchedSignal]:
    links = _as_list(record.get("external_links"))
    if not links and not record.get("has_external_link"):
        return []
    matched_text = links[0] if links else "has_external_link=true"
    return [_structured_signal("EXTERNAL_LINK_PRESENT", "external_links", matched_text, config)]


def extract_structured_contact_signals(
    record: dict[str, Any],
    config: RuleConfig,
) -> list[MatchedSignal]:
    handles = _as_list(record.get("visible_contact_handles"))
    if not handles:
        return []
    return [_structured_signal("CONTACT_HANDLE_PRESENT", "visible_contact_handles", handles[0], config)]


def extract_structured_redirect_signals(
    record: dict[str, Any],
    config: RuleConfig,
) -> list[MatchedSignal]:
    redirects = [value for value in _as_list(record.get("visible_platform_redirects")) if value != "none"]
    if not redirects:
        return []
    return [_structured_signal("PRIVATE_REDIRECT", "visible_platform_redirects", "|".join(redirects), config)]


def extract_screenshot_style_signals(
    record: dict[str, Any],
    config: RuleConfig,
) -> list[MatchedSignal]:
    style = str(record.get("screenshot_style") or "")
    if style not in {"screenshot_style", "screenshot_heavy"}:
        return []
    return [_structured_signal("SCREENSHOT_EVIDENCE", "screenshot_style", style, config)]


def _extract_pattern_signals(
    record: dict[str, Any],
    source_field: str,
    signal_codes: Iterable[str],
    config: RuleConfig,
) -> list[MatchedSignal]:
    values = _field_values(record, source_field)
    if not values:
        return []

    signals: list[MatchedSignal] = []
    for value in values:
        normalized = normalize_text(value)
        if not normalized:
            continue
        for signal_code in signal_codes:
            definition = SIGNAL_DEFINITIONS[signal_code]
            for pattern in definition.patterns:
                match = re.search(pattern, normalized, flags=re.IGNORECASE)
                if not match:
                    continue
                signals.append(
                    MatchedSignal(
                        signal_code=definition.signal_code,
                        reason_code=definition.reason_code,
                        category=definition.category,
                        source_field=source_field,
                        matched_pattern=pattern,
                        matched_text=match.group(0),
                        weight=_configured_weight(definition.signal_code, config),
                        description=definition.description,
                    )
                )
                break
    return signals


def _meta_signal(signal_code: str, source_field: str, config: RuleConfig) -> MatchedSignal:
    definition = SIGNAL_DEFINITIONS[signal_code]
    return MatchedSignal(
        signal_code=definition.signal_code,
        reason_code=definition.reason_code,
        category=definition.category,
        source_field=source_field,
        matched_pattern="<derived>",
        matched_text=f"Derived from suspicious signals in {FIELD_LABELS.get(source_field, source_field)}.",
        weight=_configured_weight(definition.signal_code, config),
        description=definition.description,
    )


def _structured_signal(
    signal_code: str,
    source_field: str,
    matched_text: str,
    config: RuleConfig,
) -> MatchedSignal:
    definition = SIGNAL_DEFINITIONS[signal_code]
    return MatchedSignal(
        signal_code=definition.signal_code,
        reason_code=definition.reason_code,
        category=definition.category,
        source_field=source_field,
        matched_pattern="<structured_field>",
        matched_text=matched_text,
        weight=_configured_weight(definition.signal_code, config),
        description=definition.description,
    )


def _configured_weight(signal_code: str, config: RuleConfig) -> float:
    return float(config.signal_weights.get(signal_code, SIGNAL_DEFINITIONS[signal_code].default_weight))


def _field_values(record: dict[str, Any], source_field: str) -> list[Any]:
    return _as_list(record.get(source_field))


def _as_list(value: Any) -> list[Any]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return [item for item in value if item not in ("", None)]
    return [value]


def _dedupe_signals(signals: list[MatchedSignal]) -> list[MatchedSignal]:
    seen: set[tuple[str, str, str, str]] = set()
    deduped: list[MatchedSignal] = []
    for signal in signals:
        key = (
            signal.signal_code,
            signal.source_field,
            signal.matched_pattern,
            normalize_text(signal.matched_text),
        )
        if key in seen:
            continue
        seen.add(key)
        deduped.append(signal)
    return deduped
