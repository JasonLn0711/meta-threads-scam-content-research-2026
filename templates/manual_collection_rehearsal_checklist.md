# Manual Collection Rehearsal Checklist

Use this checklist for the 1-2 item manual collection rehearsal before the first 10-15 real pilot items. Keep this file free of raw Threads content, screenshots, full URLs, unredacted handles, personal data, browser artifacts, credentials, and sensitive controlled-launch details.

## Rehearsal Identity

| Field | Value |
|---|---|
| Rehearsal ID |  |
| Date |  |
| Collector ID |  |
| Reviewer ID |  |
| Controlled launch status | `ready_for_rehearsal` / `ready_for_first_10_15_items` |
| Rehearsal item count |  |
| Local-only record path(s) |  |
| Local collection log path |  |

## Controlled-Launch Prerequisites

| Check | Status | Notes |
|---|---|---|
| Filled controlled launch record exists outside git |  |  |
| Exact source/source category is approved |  |  |
| Exact storage and access limits are approved |  |  |
| Retention and deletion rules are approved |  |  |
| Redaction rules are approved |  |  |
| Screenshot, OCR, URL/link, and contact-handle policies are approved |  |  |
| Collector understands forbidden fields and contexts |  |  |
| No automation, crawling, scraping, redirect expansion, or landing-page capture is used |  |  |

## Manual Input Payload Review

| Check | Status | Notes |
|---|---|---|
| Input payload stayed under `data/interim/` or another approved local-only path |  |  |
| `item_id` is non-identifying |  |  |
| `source_type`, `collection_method`, and `authorization_status` are approved |  |  |
| Source URL is omitted, redacted, or represented as approved |  |  |
| Visible links use the approved representation |  |  |
| Contact handles are omitted, categorized, or redacted as approved |  |  |
| OCR text is minimized and privacy-reviewed |  |  |
| Reply/comment text is limited to approved evidence |  |  |
| No unapproved profile, account, landing-page, or redirect context is included |  |  |

## Generated Record QA

| Check | Status | Notes |
|---|---|---|
| `governance_errors: 0` |  |  |
| `schema_errors: 0` |  |  |
| Strict validation passes |  |  |
| Required schema fields are populated or intentionally blank |  |  |
| `screenshot_snapshot_status` is accurate |  |  |
| `link_snapshot_status` is accurate |  |  |
| `privacy_redaction_notes` explains minimized fields |  |  |
| `missing_evidence` explains unavailable approved evidence |  |  |
| Label fields remain preliminary when annotation has not started |  |  |

## Collection Log QA

| Check | Status | Notes |
|---|---|---|
| Collection log row was appended locally |  |  |
| Collection burden is recorded |  |  |
| Redaction burden is recorded |  |  |
| Exclusion reason is recorded if applicable |  |  |
| Ready-for-annotation value is justified |  |  |
| No raw or sensitive details are written into the log |  |  |

## Decision

Choose one:

- `rehearsal_passed`
- `revise_input_payload`
- `revise_redaction_rules`
- `revise_schema_or_template`
- `pause_for_governance_review`
- `stop_before_collection`

Decision:

```text

```

Required follow-up before item 1:

| Follow-up | Owner | Required before continuing? |
|---|---|---|
|  |  | yes / no |
