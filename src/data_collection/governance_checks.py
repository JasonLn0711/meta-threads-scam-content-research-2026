"""Governance checks for manual-only collection assistance.

These checks intentionally block scraping, crawling, browser automation,
landing-page capture, redirect expansion, and profile review. They validate
local records and config flags; they do not authorize collection.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


BLOCKED_FLAGS = (
    "network_access_allowed",
    "enable_scraping",
    "enable_browser_automation",
    "enable_landing_capture",
    "enable_redirect_expansion",
    "enable_profile_review",
)


@dataclass
class GovernanceResult:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors

    def extend(self, other: "GovernanceResult") -> None:
        self.errors.extend(other.errors)
        self.warnings.extend(other.warnings)


def load_manual_collection_config(path: str | Path) -> dict[str, Any]:
    config_path = Path(path)
    data = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{config_path} must contain a YAML mapping")
    return data


def check_config_boundary(config: dict[str, Any]) -> GovernanceResult:
    result = GovernanceResult()
    mode = str(config.get("collection_mode", "manual_only"))
    if mode != "manual_only":
        result.errors.append(f"collection_mode must be manual_only, got {mode!r}")

    for flag in BLOCKED_FLAGS:
        if bool(config.get(flag)):
            result.errors.append(f"{flag} must remain false for the current approved pilot")
    return result


def check_record_governance(
    record: dict[str, Any],
    config: dict[str, Any],
    *,
    ack_controlled_details: bool = False,
) -> GovernanceResult:
    result = check_config_boundary(config)
    source_type = str(record.get("source_type") or "")
    collection_method = str(record.get("collection_method") or "")
    authorization_status = str(record.get("authorization_status") or "")
    is_synthetic = authorization_status == "synthetic_only" or source_type in set(
        config.get("allowed_synthetic_source_types", [])
    )

    if is_synthetic:
        _check_synthetic_record(result, record, config, collection_method, authorization_status)
    else:
        _check_real_record(
            result,
            record,
            config,
            source_type,
            collection_method,
            authorization_status,
            ack_controlled_details=ack_controlled_details,
        )

    _check_privacy_minimization(result, record, config)
    return result


def _check_synthetic_record(
    result: GovernanceResult,
    record: dict[str, Any],
    config: dict[str, Any],
    collection_method: str,
    authorization_status: str,
) -> None:
    allowed_methods = set(config.get("allowed_synthetic_collection_methods", []))
    allowed_sources = set(config.get("allowed_synthetic_source_types", []))
    source_type = str(record.get("source_type") or "")
    if source_type not in allowed_sources:
        result.errors.append(f"synthetic item has unsupported source_type {source_type!r}")
    if collection_method not in allowed_methods:
        result.errors.append(f"synthetic item has unsupported collection_method {collection_method!r}")
    if authorization_status != "synthetic_only":
        result.errors.append("synthetic item must use authorization_status='synthetic_only'")


def _check_real_record(
    result: GovernanceResult,
    record: dict[str, Any],
    config: dict[str, Any],
    source_type: str,
    collection_method: str,
    authorization_status: str,
    *,
    ack_controlled_details: bool,
) -> None:
    if config.get("require_controlled_details_ack_for_real_items", True) and not ack_controlled_details:
        result.errors.append(
            "real manual items require --ack-controlled-details after the controlled launch record is complete"
        )

    if source_type not in set(config.get("allowed_real_source_types", [])):
        result.errors.append(f"real item has unsupported source_type {source_type!r}")
    if collection_method not in set(config.get("allowed_real_collection_methods", [])):
        result.errors.append(f"real item has unsupported collection_method {collection_method!r}")
    if authorization_status != "approved":
        result.errors.append("real manual items must use authorization_status='approved'")


def _check_privacy_minimization(
    result: GovernanceResult,
    record: dict[str, Any],
    config: dict[str, Any],
) -> None:
    privacy = config.get("privacy", {})
    source_url = str(record.get("source_url_if_stored") or "")
    external_links = list(record.get("external_links") or [])
    handles = list(record.get("visible_contact_handles") or [])
    redaction_notes = str(record.get("privacy_redaction_notes") or "").strip()

    if privacy.get("source_url_storage") == "redacted_or_empty" and _looks_like_full_url(source_url):
        result.errors.append("source_url_if_stored appears to contain a full URL; store a redacted reference or blank")

    if privacy.get("external_link_storage") == "domain_only":
        for value in external_links:
            if _looks_like_full_url(str(value)) and "/" in str(value).replace("://", "", 1):
                result.errors.append(f"external_links value should be domain-only or redacted, got {value!r}")

    if privacy.get("contact_handle_storage") == "redacted_only":
        for value in handles:
            lowered = str(value).lower()
            if "redacted" not in lowered and value:
                result.warnings.append(f"visible_contact_handles should be redacted or categorical, got {value!r}")

    if privacy.get("require_redaction_notes_for_links_or_handles") and (external_links or handles) and not redaction_notes:
        result.warnings.append("privacy_redaction_notes should explain link or handle minimization")

    if not privacy.get("allow_captured_full_snapshots", False):
        if record.get("screenshot_snapshot_status") == "captured_full_approved":
            result.errors.append("captured_full_approved screenshots are disabled in manual assistant config")
        if record.get("link_snapshot_status") == "captured_full_approved":
            result.errors.append("captured_full_approved link snapshots are disabled in manual assistant config")


def _looks_like_full_url(value: str) -> bool:
    lowered = value.lower().strip()
    return lowered.startswith("http://") or lowered.startswith("https://")
