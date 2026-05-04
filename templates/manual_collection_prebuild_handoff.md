# Manual Collection Prebuild Handoff

Use this handoff before building the first 1-2 controlled rehearsal records through the manual collection assistant. It is for the gap between a local `manual_entry_*.json` intake file and the generated schema record.

Keep completed copies local-only if they contain item-level evidence, source details, raw storage details, URLs, handles, or sensitive operational notes.

## Handoff Identity

| Field | Value |
|---|---|
| Handoff ID |  |
| Dataset or batch ID | `threads_pilot_v1_2026-05` |
| Local input file | `data/interim/manual_entry_0001.json` |
| Planned output file | `data/interim/manual_record_0001.json` |
| Handoff date |  |
| Collector or operator ID |  |
| Governance reviewer ID |  |
| Controlled launch details confirmed outside git? | yes / no |
| Controlled crawler or API run record required? | yes / no / n/a |
| Required run record completed before intake? | yes / no / n/a |

## Required Intake Fields

Complete these before running `scripts/build_manual_collection_record.py`.

| Field | Acceptable prebuild value | Ready? | Notes |
|---|---|---|---|
| `item_id` | Non-identifying stable ID; no source, handle, URL, person name, or case ID. | yes / no |  |
| `candidate_bucket` | One of: `likely_scam_or_high_risk_scam_like`, `likely_non_scam_comparator`, `uncertain_or_ambiguous`, `insufficient_evidence_or_low_context`. | yes / no |  |
| `collector_id` | Approved role ID only, such as `collector_01`. | yes / no |  |
| `source_type` | Approved value from the controlled launch record. | yes / no |  |
| `collection_method` | Approved schema value compatible with the manual assistant input, usually `manual_capture`; use a separate run record for API or automation-assisted acquisition. | yes / no |  |
| `authorization_status` | `approved` for real rehearsal records. | yes / no |  |
| `post_text` | Approved redacted visible text, or blank only with a missing-evidence note. | yes / no |  |
| `privacy_redaction_notes` | Explains what was removed, normalized, minimized, or omitted. | yes / no |  |
| `metadata_notes` | Non-sensitive operational note; no placeholder text. | yes / no |  |

## Optional Evidence Fields

Fill only when approved and necessary for review. Otherwise keep blank, empty, or `not_applicable`.

| Field | Rule | Ready? | Notes |
|---|---|---|---|
| `reply_texts` | Selected relevant redacted replies only; no broad thread dumps. | yes / no / n/a |  |
| `image_paths` | Redacted local references only; no raw screenshot path in git. | yes / no / n/a |  |
| `image_count` | Count represented images; use `0` when none. | yes / no / n/a |  |
| `ocr_text` | Privacy-reviewed OCR excerpt only; no unrelated personal details. | yes / no / n/a |  |
| `external_links` | Domain-only, normalized, redacted, or categorical link evidence only. | yes / no / n/a |  |
| `visible_contact_handles` | Redacted or categorical evidence only, such as `telegram:[redacted]`. | yes / no / n/a |  |
| `visible_platform_redirects` | Schema vocabulary only, or `none` if no redirect signal is captured. | yes / no / n/a |  |
| `source_url_if_stored` | Blank or redacted according to the controlled launch record. | yes / no / n/a |  |
| `screenshot_snapshot_status` | Approved schema status; usually `not_applicable` when no image evidence is represented. | yes / no / n/a |  |
| `link_snapshot_status` | Approved schema status; usually `not_applicable` when no link evidence is represented. | yes / no / n/a |  |

## Stop Checks

Pause before building if any answer is `yes`.

| Stop condition | Yes/No | Fix |
|---|---|---|
| Any field still contains `FILL_`, `REPLACE_`, or `PENDING_` |  | Replace with approved redacted value, or pause. |
| The collector needs profile/account context |  | Pause for authorization review. |
| The collector needs landing-page or redirect-chain context |  | Pause for authorization review. |
| The collector needs raw handles, full URLs, payment details, or referral codes |  | Redact, normalize, or pause. |
| OCR or screenshot evidence includes unrelated personal details |  | Redact or exclude the evidence. |
| Evidence cannot be made reviewable under approved fields |  | Mark not ready and record the exclusion reason locally. |
| The item requires unrecorded automation, scraping, crawling, browser export, or session data |  | Stop. Use a completed controlled run record before any redacted selected item enters this intake. |

## Prebuild Command Check

Before building, this local scan should return no matches for the target input file:

```bash
rg -n "FILL_|REPLACE_|PENDING_" data/interim/manual_entry_0001.json
```

Then run the builder:

```bash
.venv/bin/python scripts/build_manual_collection_record.py data/interim/manual_entry_0001.json \
  --ack-controlled-details \
  --output data/interim/manual_record_0001.json \
  --collection-log data/interim/threads_pilot_v1_collection_log.csv
```

If the builder reports any governance error, do not bypass it. Fix the intake or pause.

## Handoff Decision

Choose one:

- `ready_to_build_rehearsal_record`
- `pause_for_redaction_fix`
- `pause_for_collection_fix`
- `pause_for_authorization_review`
- `stop_item_for_pilot`

Decision:

```text

```

Required follow-up:

| Follow-up | Owner | Required before build? |
|---|---|---|
|  |  | yes / no |
