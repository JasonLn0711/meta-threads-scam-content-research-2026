#!/usr/bin/env python3
"""Run the first transparent Threads scam-content rule baseline."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Any

from thread_dataset_utils import load_records, record_text


TAG_PATTERNS: dict[str, list[str]] = {
    "guaranteed_or_risk_free_claim": [
        r"\bguaranteed\b",
        r"\brisk[- ]?free\b",
        r"\bno loss\b",
        r"\bfixed roi\b",
        r"\bguaranteed return\b",
        r"\bdaily profit\b",
    ],
    "unrealistic_profit_or_benefit": [
        r"\bturn\s+\$?\d+.*\binto\s+\$?\d+",
        r"\b\d+%.*\b(day|week|month)\b",
        r"\bsteady daily profit\b",
        r"\bmake .*profit\b",
        r"\bpassive income\b",
    ],
    "private_channel_redirect": [
        r"\bdm\b",
        r"\bdirect message\b",
        r"\bprivate group\b",
        r"\bjoin (the )?group\b",
        r"\bmessage the assistant\b",
        r"\btelegram\b",
        r"\bwhatsapp\b",
        r"\bline\b",
    ],
    "urgency_or_scarcity": [
        r"\blimited\b",
        r"\blast chance\b",
        r"\btoday only\b",
        r"\bfew spots\b",
        r"\bfirst\s+\d+\s+(members|people|spots|users)\b",
        r"\blimited seats\b",
        r"\bact now\b",
        r"\bdeadline\b",
    ],
    "testimonial_or_earnings_screenshot": [
        r"\btestimonial\b",
        r"\bproof\b",
        r"\bmember results\b",
        r"\bmember screenshots\b",
        r"\bearnings screenshot\b",
        r"\bprofit screenshot\b",
    ],
    "pseudo_official_language": [
        r"\bofficial\b",
        r"\bverification\b",
        r"\bverify your account\b",
        r"\bsupport account\b",
        r"\breward notice\b",
        r"\bsubsidy\b",
    ],
    "payment_deposit_or_fee_request": [
        r"\bdeposit\b",
        r"\bfee\b",
        r"\brelease fee\b",
        r"\bwallet transfer\b",
        r"\bshipping fee\b",
        r"\bpay\b",
    ],
    "credential_or_personal_data_request": [
        r"\blogin\b",
        r"\bpassword\b",
        r"\bverify your account\b",
        r"\bbank info\b",
        r"\bpersonal information\b",
        r"\bid number\b",
    ],
    "medical_cure_or_miracle_claim": [
        r"\bmiracle\b",
        r"\bcure\b",
        r"\btreatment\b",
        r"\bdoctor\b",
        r"\bsupplement\b",
    ],
    "giveaway_reward_or_prize_claim": [
        r"\bprize\b",
        r"\breward\b",
        r"\bgrant\b",
        r"\bgiveaway\b",
        r"\blottery\b",
        r"\bbonus\b",
    ],
    "recruitment_or_easy_income_claim": [
        r"\bremote work\b",
        r"\btask work\b",
        r"\beasy income\b",
        r"\bside hustle\b",
        r"\bno experience needed\b",
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Dataset file: .csv, .json, or .jsonl")
    parser.add_argument(
        "--variant",
        choices=["text_only", "text_reply", "text_ocr", "all"],
        default="all",
        help="Evidence fields to use",
    )
    parser.add_argument("--output", type=Path, help="Optional prediction CSV path")
    args = parser.parse_args()

    records = load_records(args.input)
    predictions = [predict_record(record, args.variant) for record in records]

    if args.output:
        write_predictions(args.output, predictions)
    else:
        write_predictions_to_handle(sys.stdout, predictions)

    print_metrics(records, predictions, args.variant, args.output)
    return 0


def predict_record(record: dict[str, Any], variant: str) -> dict[str, str]:
    text = evidence_text(record, variant)
    matched_tags = match_tags(text)

    if variant == "all":
        if record.get("external_links"):
            matched_tags.add("visible_external_link")
        if record.get("visible_contact_handles"):
            matched_tags.add("contact_handle_visible")
        redirects = [value for value in record.get("visible_platform_redirects", []) if value != "none"]
        if redirects:
            matched_tags.add("private_channel_redirect")

    risk = risk_from_tags(matched_tags)
    label = "scam" if risk == "high" else "uncertain" if risk == "medium" else "non_scam"
    reasons = reasons_from_tags(matched_tags)

    return {
        "item_id": str(record.get("item_id", "")),
        "baseline_variant": variant,
        "predicted_label": label,
        "predicted_risk_level": risk,
        "matched_signal_tags": "|".join(sorted(matched_tags)) if matched_tags else "none",
        "baseline_reasons": " ".join(reasons) if reasons else "No baseline risk pattern matched.",
        "gold_label": str(record.get("final_label") or record.get("scam_label") or ""),
        "gold_risk_level": str(record.get("final_risk_level") or record.get("risk_level") or ""),
    }


def evidence_text(record: dict[str, Any], variant: str) -> str:
    fields = ["post_text"]
    if variant in {"text_reply", "all"}:
        fields.append("reply_texts")
    if variant in {"text_ocr", "all"}:
        fields.append("ocr_text")
    if variant == "all":
        fields.extend(["external_links", "visible_contact_handles", "visible_platform_redirects"])
    return record_text(record, tuple(fields)).lower()


def match_tags(text: str) -> set[str]:
    matched: set[str] = set()
    for tag, patterns in TAG_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, text, flags=re.IGNORECASE):
                matched.add(tag)
                break
    return matched


def risk_from_tags(tags: set[str]) -> str:
    severe = {
        "payment_deposit_or_fee_request",
        "credential_or_personal_data_request",
    }
    redirect = {
        "private_channel_redirect",
        "contact_handle_visible",
        "visible_external_link",
    }
    benefit = {
        "guaranteed_or_risk_free_claim",
        "unrealistic_profit_or_benefit",
        "giveaway_reward_or_prize_claim",
        "recruitment_or_easy_income_claim",
        "medical_cure_or_miracle_claim",
    }
    proof_or_authority = {
        "testimonial_or_earnings_screenshot",
        "pseudo_official_language",
    }

    if tags & severe and (tags & benefit or tags & redirect or tags & proof_or_authority):
        return "high"
    if tags & {"guaranteed_or_risk_free_claim"} and tags & {"unrealistic_profit_or_benefit"}:
        return "high"
    if tags & {"guaranteed_or_risk_free_claim"} and (tags & redirect or tags & proof_or_authority):
        return "high"
    if tags & redirect and tags & proof_or_authority and tags & {"urgency_or_scarcity"}:
        return "high"
    if tags & benefit and tags & redirect and tags & {"urgency_or_scarcity", "testimonial_or_earnings_screenshot"}:
        return "high"
    if len(tags) >= 2:
        return "medium"
    return "low"


def reasons_from_tags(tags: set[str]) -> list[str]:
    labels = {
        "guaranteed_or_risk_free_claim": "Matched guarantee or risk-free language.",
        "unrealistic_profit_or_benefit": "Matched unusually strong benefit language.",
        "private_channel_redirect": "Matched private-channel or off-platform redirection.",
        "visible_external_link": "Visible external link evidence is present.",
        "contact_handle_visible": "Visible contact handle evidence is present.",
        "urgency_or_scarcity": "Matched urgency or scarcity language.",
        "testimonial_or_earnings_screenshot": "Matched testimonial or proof-style language.",
        "pseudo_official_language": "Matched official-looking or verification language.",
        "payment_deposit_or_fee_request": "Matched payment, deposit, or fee request language.",
        "credential_or_personal_data_request": "Matched credential or personal-data request language.",
        "medical_cure_or_miracle_claim": "Matched medical cure or miracle language.",
        "giveaway_reward_or_prize_claim": "Matched giveaway, reward, or prize language.",
        "recruitment_or_easy_income_claim": "Matched recruitment or easy-income language.",
    }
    return [labels[tag] for tag in sorted(tags) if tag in labels]


def write_predictions(path: Path, predictions: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        write_predictions_to_handle(handle, predictions)


def write_predictions_to_handle(handle: Any, predictions: list[dict[str, str]]) -> None:
    fieldnames = [
        "item_id",
        "baseline_variant",
        "predicted_label",
        "predicted_risk_level",
        "matched_signal_tags",
        "baseline_reasons",
        "gold_label",
        "gold_risk_level",
    ]
    writer = csv.DictWriter(handle, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(predictions)


def print_metrics(records: list[dict[str, Any]], predictions: list[dict[str, str]], variant: str, output: Path | None) -> None:
    gold_pairs = [
        (prediction["gold_label"], prediction["predicted_label"])
        for prediction in predictions
        if prediction["gold_label"] in {"scam", "non_scam"}
    ]
    scam_gold = sum(1 for gold, _ in gold_pairs if gold == "scam")
    scam_pred = sum(1 for _, pred in gold_pairs if pred == "scam")
    true_positive = sum(1 for gold, pred in gold_pairs if gold == "scam" and pred == "scam")
    false_positive = sum(1 for gold, pred in gold_pairs if gold == "non_scam" and pred == "scam")
    false_negative = sum(1 for gold, pred in gold_pairs if gold == "scam" and pred != "scam")

    precision = true_positive / scam_pred if scam_pred else 0.0
    recall = true_positive / scam_gold if scam_gold else 0.0
    f1 = (2 * precision * recall / (precision + recall)) if precision + recall else 0.0

    stream = sys.stderr if output is None else sys.stdout
    print("", file=stream)
    print(f"baseline_variant: {variant}", file=stream)
    print(f"items: {len(records)}", file=stream)
    print(f"binary_metric_items: {len(gold_pairs)}", file=stream)
    print(f"true_positive: {true_positive}", file=stream)
    print(f"false_positive: {false_positive}", file=stream)
    print(f"false_negative: {false_negative}", file=stream)
    print(f"precision: {precision:.3f}", file=stream)
    print(f"recall: {recall:.3f}", file=stream)
    print(f"f1: {f1:.3f}", file=stream)
    if output:
        print(f"predictions_written: {output}", file=stream)


if __name__ == "__main__":
    raise SystemExit(main())
