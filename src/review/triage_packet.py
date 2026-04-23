"""Build local-only Markdown triage packets from records and predictions."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from src.baselines.risk_scoring import load_rule_config
from src.baselines.rule_based import predict_batch
from src.baselines.types import VALID_VARIANTS
from src.evaluation.metrics import preferred_gold_label
from src.evaluation.triage_metrics import preferred_gold_risk


def build_packets(
    records: list[dict[str, Any]],
    *,
    output_dir: str | Path,
    predictions: list[dict[str, Any]] | None = None,
    config_path: str | Path = "configs/baseline_rule_config.yaml",
    variant: str = "all",
    max_text_chars: int = 900,
) -> dict[str, Any]:
    if variant not in VALID_VARIANTS:
        raise ValueError(f"variant must be one of {', '.join(VALID_VARIANTS)}")
    if predictions is None:
        config = load_rule_config(config_path)
        predictions = predict_batch(records, config=config, variant=variant)
    else:
        predictions = align_predictions(records, predictions)

    out = Path(output_dir)
    packet_dir = out / "packets"
    packet_dir.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, Any]] = []
    for record, prediction in sorted(
        zip(records, predictions, strict=False),
        key=lambda pair: _sort_key(pair[0], pair[1]),
    ):
        item_id = str(record.get("item_id") or prediction.get("item_id") or "unknown")
        filename = f"{safe_filename(item_id)}.md"
        packet_path = packet_dir / filename
        packet_path.write_text(
            "\n".join(render_packet(record, prediction, max_text_chars=max_text_chars)).rstrip() + "\n",
            encoding="utf-8",
        )
        rows.append(index_row(record, prediction, packet_path))

    write_index_csv(out / "review_packet_index.csv", rows)
    write_manifest(out / "packet_manifest.json", rows, variant)
    (out / "index.md").write_text(
        "\n".join(render_index(rows, variant)).rstrip() + "\n",
        encoding="utf-8",
    )
    return {
        "output_dir": str(out),
        "packet_count": len(rows),
        "index_path": str(out / "index.md"),
        "csv_index_path": str(out / "review_packet_index.csv"),
        "manifest_path": str(out / "packet_manifest.json"),
    }


def load_predictions(path: str | Path) -> list[dict[str, Any]]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"{path} must contain a JSON prediction list")
    return data


def align_predictions(
    records: list[dict[str, Any]],
    predictions: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    if len(records) != len(predictions):
        raise ValueError(
            f"record count ({len(records)}) does not match prediction count ({len(predictions)})"
        )

    prediction_by_item_id: dict[str, dict[str, Any]] = {}
    for prediction in predictions:
        item_id = str(prediction.get("item_id") or "")
        if not item_id:
            return predictions
        if item_id in prediction_by_item_id:
            raise ValueError(f"duplicate prediction item_id: {item_id}")
        prediction_by_item_id[item_id] = prediction

    aligned: list[dict[str, Any]] = []
    missing: list[str] = []
    for record in records:
        item_id = str(record.get("item_id") or "")
        prediction = prediction_by_item_id.get(item_id)
        if prediction is None:
            missing.append(item_id or "<blank>")
            continue
        aligned.append(prediction)
    if missing:
        raise ValueError("missing predictions for item_id(s): " + ", ".join(missing[:10]))
    return aligned


def render_packet(
    record: dict[str, Any],
    prediction: dict[str, Any],
    *,
    max_text_chars: int,
) -> list[str]:
    item_id = str(record.get("item_id") or prediction.get("item_id") or "")
    lines = [
        f"# Review Packet: `{item_id}`",
        "",
        "## Safety Boundary",
        "",
        "This packet is for research triage. It is not a legal finding, platform enforcement decision, or production detector output.",
        "",
        "## Source And Labels",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| `source_type` | `{record.get('source_type', '')}` |",
        f"| `authorization_status` | `{record.get('authorization_status', '')}` |",
        f"| `collection_batch_id` | `{record.get('collection_batch_id', '')}` |",
        f"| Gold label | `{preferred_gold_label(record)}` |",
        f"| Gold risk | `{preferred_gold_risk(record)}` |",
        f"| Evidence sufficiency | `{record.get('evidence_sufficiency', '')}` |",
        f"| Annotation confidence | `{record.get('annotation_confidence', '')}` |",
        "",
        "## Baseline Triage",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Binary prediction | `{prediction.get('binary_pred', '')}` |",
        f"| Risk prediction | `{prediction.get('risk_level_pred', '')}` |",
        f"| Subtype hint | `{prediction.get('subtype_hint') or ''}` |",
        f"| Total score | `{prediction.get('total_score', '')}` |",
        f"| Reason codes | `{', '.join(prediction.get('reason_codes', []))}` |",
        "",
        "## Reviewer-Facing Explanation",
        "",
    ]
    explanations = prediction.get("explanations", [])
    if explanations:
        lines.extend(f"- {explanation}" for explanation in explanations)
    else:
        lines.append("- No baseline risk pattern matched.")

    lines.extend(
        [
            "",
            "## Evidence Fields",
            "",
            "### Post Text",
            "",
            fenced_excerpt(record.get("post_text"), max_text_chars),
            "",
            "### Reply Texts",
            "",
            fenced_excerpt(record.get("reply_texts"), max_text_chars),
            "",
            "### OCR Text",
            "",
            fenced_excerpt(record.get("ocr_text"), max_text_chars),
            "",
            "### Links, Handles, Redirects",
            "",
            f"- External links: `{pipe_join(record.get('external_links'))}`",
            f"- Visible contact handles: `{pipe_join(record.get('visible_contact_handles'))}`",
            f"- Visible platform redirects: `{pipe_join(record.get('visible_platform_redirects'))}`",
            f"- Screenshot style: `{record.get('screenshot_style', '')}`",
            f"- Missing evidence: `{pipe_join(record.get('missing_evidence'))}`",
            "",
            "## Matched Signals",
            "",
        ]
    )
    lines.extend(render_signal_table(prediction.get("matched_signals", [])))
    lines.extend(
        [
            "",
            "## Score Breakdown",
            "",
            fenced_json(prediction.get("score_breakdown", {})),
            "",
            "## Reviewer Decision",
            "",
            "- Final label:",
            "- Final risk:",
            "- Agree with baseline? yes / no / partial",
            "- Reviewer notes:",
            "- Missing evidence that would change decision:",
            "- Guideline/schema feedback:",
        ]
    )
    return lines


def render_index(rows: list[dict[str, Any]], variant: str) -> list[str]:
    lines = [
        "# Review Packet Index",
        "",
        f"- Baseline variant: `{variant}`",
        f"- Packets: {len(rows)}",
        "",
        "| Item | Priority | Gold | Predicted | Score | Reasons | Packet |",
        "|---|---|---|---|---:|---|---|",
    ]
    for row in rows:
        lines.append(
            "| `{item_id}` | `{review_priority}` | `{gold_label}/{gold_risk_level}` | `{pred_binary}/{pred_risk_level}` | {total_score} | `{reason_codes}` | [{packet_file}]({packet_rel_path}) |".format(
                **row
            )
        )
    return lines


def index_row(record: dict[str, Any], prediction: dict[str, Any], packet_path: Path) -> dict[str, Any]:
    return {
        "item_id": str(record.get("item_id") or prediction.get("item_id") or ""),
        "gold_label": preferred_gold_label(record),
        "gold_risk_level": preferred_gold_risk(record),
        "pred_binary": str(prediction.get("binary_pred") or ""),
        "pred_risk_level": str(prediction.get("risk_level_pred") or ""),
        "total_score": prediction.get("total_score", ""),
        "reason_codes": ", ".join(prediction.get("reason_codes", [])),
        "review_priority": review_priority(record, prediction),
        "packet_path": str(packet_path),
        "packet_rel_path": f"packets/{packet_path.name}",
        "packet_file": packet_path.name,
    }


def review_priority(record: dict[str, Any], prediction: dict[str, Any]) -> str:
    gold = preferred_gold_label(record)
    pred = prediction.get("binary_pred")
    risk = prediction.get("risk_level_pred")
    if gold == "non_scam" and pred == "scam_like":
        return "01_false_positive_review"
    if gold == "scam" and pred != "scam_like":
        return "02_false_negative_review"
    if gold in {"uncertain", "insufficient_evidence"}:
        return "03_ambiguity_review"
    if risk == "high":
        return "04_high_risk_reason_check"
    if risk == "medium":
        return "05_medium_risk_threshold_check"
    return "06_spot_check"


def write_index_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "item_id",
        "gold_label",
        "gold_risk_level",
        "pred_binary",
        "pred_risk_level",
        "total_score",
        "reason_codes",
        "review_priority",
        "packet_path",
        "packet_rel_path",
        "packet_file",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_manifest(path: Path, rows: list[dict[str, Any]], variant: str) -> None:
    review_priority_counts = Counter(row["review_priority"] for row in rows)
    path.write_text(
        json.dumps(
            {
                "variant": variant,
                "packet_count": len(rows),
                "review_priority_counts": dict(review_priority_counts),
                "packets": rows,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )


def render_signal_table(signals: list[dict[str, Any]]) -> list[str]:
    if not signals:
        return ["No matched signals."]
    lines = [
        "| Signal | Source | Weight | Matched text |",
        "|---|---|---:|---|",
    ]
    for signal in signals:
        lines.append(
            "| `{}` | `{}` | {} | `{}` |".format(
                signal.get("signal_code", ""),
                signal.get("source_field", ""),
                signal.get("weight", ""),
                clean_cell(str(signal.get("matched_text", "")))[:140],
            )
        )
    return lines


def fenced_excerpt(value: Any, max_text_chars: int) -> str:
    text = pipe_join(value)
    if not text:
        text = "<empty>"
    if len(text) > max_text_chars:
        text = text[: max_text_chars - 18].rstrip() + " ... [truncated]"
    return f"```text\n{text}\n```"


def fenced_json(value: Any) -> str:
    return "```json\n" + json.dumps(value, indent=2, sort_keys=True) + "\n```"


def pipe_join(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return " | ".join(str(item) for item in value if item not in ("", None))
    return str(value)


def safe_filename(value: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._")
    return safe or "unknown"


def clean_cell(value: str) -> str:
    return " ".join(value.replace("|", "/").split())


def _sort_key(record: dict[str, Any], prediction: dict[str, Any]) -> tuple[str, float, str]:
    score = float(prediction.get("total_score") or 0)
    return (review_priority(record, prediction), -score, str(record.get("item_id") or ""))
