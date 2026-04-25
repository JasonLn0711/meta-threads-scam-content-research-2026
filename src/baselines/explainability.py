"""Reviewer-friendly explanations for rule-baseline predictions."""

from __future__ import annotations

from .taxonomy import FIELD_LABELS
from .types import MatchedSignal, ScoreBreakdown


EXPLANATION_TEMPLATES = {
    "GUARANTEED_PROFIT": "Detected guaranteed-profit language in {source}.",
    "LOW_EFFORT_HIGH_RETURN": "Detected low-effort or high-return benefit language in {source}.",
    "PAST_PERFORMANCE_PROFIT_PROOF": "Detected past-performance profit-proof language in {source}.",
    "HIGH_FEE_COURSE_FUNNEL": "Detected high-fee course, academy, coaching, or membership funnel language in {source}.",
    "STOCK_RESCUE_GROUP_FUNNEL": "Detected stock-rescue group funnel language in {source}.",
    "INDIVIDUAL_STOCK_ADVICE_REPLY_FUNNEL": "Detected individualized stock-advice reply-funnel language in {source}.",
    "MARKET_DIRECTION_HERDING_CHORUS": "Detected market-direction herding chorus language in {source}.",
    "INSTITUTIONAL_FLOW_AUTHORITY_LURE": "Detected institutional-flow or macro-authority trading lure language in {source}.",
    "LIFESTYLE_TRUST_MARKET_REASSURANCE_FUNNEL": "Detected lifestyle-trust market-reassurance funnel language in {source}.",
    "BEGINNER_EASY_MONEY": "Detected beginner/no-experience earning language in {source}.",
    "MENTOR_COPYTRADE_LANGUAGE": "Detected mentor, signal-group, or copy-trade language in {source}.",
    "PRIVATE_REDIRECT": "Detected private-channel redirect language in {source}.",
    "IMPLICIT_DM_CONTACT_REQUEST": "Detected implicit DM/contact-request language in {source}.",
    "COMMENT_CODE_LEAD_MAGNET": "Detected comment-code or keyword lead-magnet language in {source}.",
    "STOCK_PICK_PLAYBOOK_KEYWORD_FUNNEL": "Detected stock-pick playbook or keyword-funnel language in {source}.",
    "TRAPPED_POSITION_DM_PLAYBOOK_REPLY": "Detected trapped-position DM playbook language in {source}.",
    "DARK_HORSE_STOCK_TARGET_PRICE_DM_FUNNEL": "Detected dark-horse stock target-price DM-funnel language in {source}.",
    "MASS_STOCK_COMMAND_LIST_GROUP_FUNNEL": "Detected mass stock-command list and daily-signal group funnel language in {source}.",
    "REPLY_IMPERSONATION_CONTACT_HIJACK": "Detected reply-based impersonation or contact-hijack language in {source}.",
    "CONTACT_HANDLE_PRESENT": "Detected visible contact-handle evidence in {source}.",
    "EXTERNAL_LINK_PRESENT": "Detected visible external-link evidence in {source}.",
    "URGENCY_PRESSURE": "Detected urgency or scarcity pressure in {source}.",
    "TESTIMONIAL_PATTERN": "Detected testimonial or proof-style language in {source}.",
    "SCREENSHOT_EVIDENCE": "Detected screenshot-style evidence or screenshot-as-proof framing.",
    "PSEUDO_OFFICIAL_LANGUAGE": "Detected pseudo-official or verification-style language in {source}.",
    "CELEBRITY_ENDORSEMENT_PATTERN": "Detected celebrity, expert, or endorsement framing in {source}.",
    "PAYMENT_OR_CREDENTIAL_REQUEST": "Detected payment, fee, credential, or personal-data request language in {source}.",
    "OCR_SUSPICIOUS_TEXT": "Suspicious wording was found in OCR text rather than only visible post text.",
    "REPLY_FUNNEL_PATTERN": "Suspicious funneling appeared in replies or comments.",
}


def build_explanations(
    signals: list[MatchedSignal],
    score: ScoreBreakdown,
    reason_codes: list[str],
) -> list[str]:
    explanations: list[str] = []
    first_by_reason: dict[str, MatchedSignal] = {}
    for signal in signals:
        first_by_reason.setdefault(signal.reason_code, signal)

    for reason_code in reason_codes:
        if reason_code == "MULTI_SIGNAL_CONVERGENCE":
            explanations.append(_convergence_explanation(score))
            continue
        signal = first_by_reason.get(reason_code)
        if not signal:
            continue
        template = EXPLANATION_TEMPLATES.get(reason_code)
        if not template:
            explanations.append(signal.description)
            continue
        explanations.append(
            template.format(source=FIELD_LABELS.get(signal.source_field, signal.source_field))
        )

    return explanations


def build_reviewer_note(risk_level: str, subtype_hint: str | None, score: ScoreBreakdown) -> str:
    if risk_level == "high":
        note = "High-risk queue candidate because multiple weighted rule signals co-occurred."
    elif risk_level == "medium":
        note = "Medium-risk rule output; review evidence before treating it as scam-like."
    else:
        note = "Low-risk rule output; no strong rule convergence was detected."

    if subtype_hint:
        note += f" Optional subtype hint: {subtype_hint}."
    if not score.high_guardrail_passed and score.total_score >= 9:
        note += " High-risk threshold was reached, but guardrails prevented high-risk assignment."
    return note


def _convergence_explanation(score: ScoreBreakdown) -> str:
    categories = sorted(score.category_counts)
    if categories:
        joined = " + ".join(categories)
        return f"Multiple independent suspicious signal families co-occurred: {joined}."
    return "Multiple suspicious signals co-occurred."
