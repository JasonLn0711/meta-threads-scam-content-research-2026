"""Local collection log helpers for manual-only collection workflows."""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


COLLECTION_LOG_FIELDS = (
    "collection_batch_id",
    "item_id",
    "candidate_bucket",
    "collector_id",
    "collection_timestamp",
    "source_type",
    "collection_method",
    "authorization_status",
    "source_reference_allowed",
    "source_url_if_stored",
    "screenshot_snapshot_status",
    "link_snapshot_status",
    "post_text_captured",
    "reply_context_captured",
    "image_count",
    "ocr_needed",
    "external_link_visible",
    "contact_handle_visible",
    "visible_platform_redirects",
    "raw_storage_location",
    "redaction_required",
    "redaction_completed",
    "ready_for_annotation",
    "exclusion_reason",
    "collector_notes",
)


def collection_log_row(record: dict[str, Any], payload: dict[str, Any]) -> dict[str, str]:
    has_links = bool(record.get("external_links"))
    has_handles = bool(record.get("visible_contact_handles"))
    has_image = bool(record.get("has_image"))
    redaction_required = has_links or has_handles or has_image or bool(record.get("ocr_text"))
    return {
        "collection_batch_id": str(record.get("collection_batch_id") or ""),
        "item_id": str(record.get("item_id") or ""),
        "candidate_bucket": str(payload.get("candidate_bucket") or ""),
        "collector_id": str(payload.get("collector_id") or record.get("annotator_id") or ""),
        "collection_timestamp": str(record.get("collection_timestamp") or ""),
        "source_type": str(record.get("source_type") or ""),
        "collection_method": str(record.get("collection_method") or ""),
        "authorization_status": str(record.get("authorization_status") or ""),
        "source_reference_allowed": "yes" if record.get("source_url_if_stored") else "no",
        "source_url_if_stored": str(record.get("source_url_if_stored") or ""),
        "screenshot_snapshot_status": str(record.get("screenshot_snapshot_status") or ""),
        "link_snapshot_status": str(record.get("link_snapshot_status") or ""),
        "post_text_captured": "yes" if str(record.get("post_text") or "").strip() else "no",
        "reply_context_captured": "yes" if record.get("reply_texts") else "no",
        "image_count": str(record.get("image_count") or 0),
        "ocr_needed": "yes" if has_image and not record.get("ocr_text") else "no",
        "external_link_visible": "yes" if has_links else "no",
        "contact_handle_visible": "yes" if has_handles else "no",
        "visible_platform_redirects": "|".join(record.get("visible_platform_redirects") or []),
        "raw_storage_location": str(payload.get("raw_storage_location") or ""),
        "redaction_required": "yes" if redaction_required else "no",
        "redaction_completed": str(payload.get("redaction_completed") or ("yes" if record.get("privacy_redaction_notes") else "no")),
        "ready_for_annotation": str(payload.get("ready_for_annotation") or "no"),
        "exclusion_reason": str(payload.get("exclusion_reason") or ""),
        "collector_notes": str(payload.get("collector_notes") or ""),
    }


def append_collection_log(path: str | Path, row: dict[str, str]) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    write_header = not output_path.exists() or output_path.stat().st_size == 0
    with output_path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLLECTION_LOG_FIELDS)
        if write_header:
            writer.writeheader()
        writer.writerow({field: row.get(field, "") for field in COLLECTION_LOG_FIELDS})


def write_action_log(
    path: str | Path,
    *,
    mode: str,
    action_type: str,
    success: bool,
    item_id: str = "",
    target_url: str = "",
    message: str = "",
    include_target_url: bool = False,
) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "mode": mode,
        "action_type": action_type,
        "success": success,
        "item_id": item_id,
        "target_url": target_url if include_target_url else "[not_logged]",
        "message": message,
    }
    with output_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, sort_keys=True) + "\n")
