# Redacted Field Readiness Check

Historical note: this was a local pre-sync readiness note originally drafted before the repository was fast-forwarded to the current `origin/main` state on `2026-05-04`. It is retained as a repo-safe audit note, but the active evaluation-note sequence has since advanced beyond the first controlled rehearsal build.

## Objective

Identify the exact local-only intake fields that must be filled before the first approved rehearsal record can be generated for the first 10-15 item checkpoint.

This note is repo-safe. It does not contain raw Threads content, screenshots, source URLs, handles, case IDs, credentials, raw storage paths, access lists, or sensitive investigative details.

## Context

As of `2026-04-23`, the project owner has confirmed the outside-git controlled launch record with final status `ready_for_first_10_15_items`.

The current repo state has already verified three gates:

- before-item-1 preflight passed with `ERROR: 0`
- pending manual rehearsal intake cannot generate a real record
- approved manual rehearsal intake with unresolved placeholders cannot generate a real record

Controlled crawler rehearsal run 0001 later confirmed that no extractable candidate item was available from the first static seed path. The next research step is therefore confirming that an approved acquisition path can produce one selected item with redacted, non-placeholder fields under the controlled launch limits.

## Local-Only Intake Status

These files are under ignored `data/interim/` and must not be committed.

| Local file | Authorization status | Current readiness |
|---|---|---|
| `data/interim/manual_entry_0001.json` | `approved` | blocked by unresolved placeholder fields |
| `data/interim/manual_entry_0002.json` | `pending` | blocked by pending authorization and unresolved placeholder fields |

`manual_entry_0001.json` is still the first local intake target, but it is not ready because no selected item has been entered and placeholder markers remain unresolved.

## Required Replacements For Item 0001

Replace only with approved, redacted fields from the controlled launch scope. If the selected item is crawler-acquired, complete the controlled crawler run record first and enter only the redacted selected item into the local intake.

| Field | Required collector action |
|---|---|
| `candidate_bucket` | Replace with a non-sensitive bucket description such as `likely_scam_or_high_risk_scam_like`, `likely_non_scam_comparator`, `uncertain_or_ambiguous`, or `insufficient_evidence_or_low_context`. |
| `post_text` | Replace with approved redacted visible text, or leave blank only when no reviewable post text is approved and the missing evidence is reflected in notes. |
| `privacy_redaction_notes` | Describe what was minimized, removed, normalized, or omitted for privacy and governance reasons. |
| `metadata_notes` | Replace placeholder text with a non-sensitive operational note about the allowed evidence shape. |

Optional fields also need deliberate values when present:

| Field area | Rule |
|---|---|
| `reply_texts` | Include only selected relevant redacted replies approved for the pilot, or keep `[]`. |
| `ocr_text` | Include only privacy-reviewed OCR text, or keep blank. |
| `external_links` | Store only approved domain-only, normalized, redacted, or categorical link evidence. Do not store full tracking URLs unless later authorization allows it. |
| `visible_contact_handles` | Use redacted or categorical handle evidence only. |
| `visible_platform_redirects` | Use the schema vocabulary, or `none` when no redirect signal is captured. |
| `source_url_if_stored` | Keep blank or redacted as allowed by the controlled launch record. |
| `screenshot_snapshot_status` | Keep `not_applicable` when no approved image or screenshot evidence is represented. |
| `link_snapshot_status` | Keep `not_applicable` when no approved link evidence is represented. |

## Why This Check Matters

This check keeps the first real-item work inside the actual authorization boundary. An `approved` status by itself is not enough if the item still contains placeholders, unredacted text, full identifiers, or unsupported evidence.

It also protects the first 10-15 item checkpoint from a false start. A schema-valid record that was created from placeholders would look operationally successful while carrying no usable research evidence. A record created from over-broad evidence would be worse: it would blur the privacy, legal, and platform limits that the pilot is supposed to test.

## Current Decision

Current decision: `redacted_field_readiness_check_complete_waiting_for_selected_item`

Reason:

- controlled launch confirmation has been received outside git
- local-only manual rehearsal files exist under ignored `data/interim/`
- controlled crawler rehearsal run 0001 did not produce an extractable selected item
- `manual_entry_0001.json` still contains unresolved placeholder fields because no selected item is ready
- `manual_entry_0002.json` remains pending and cannot be used for a real build
- the manual assistant correctly blocks approved records that still contain placeholders
- no real Threads evidence has been collected, generated, or committed as part of this check

## Next Action

After an approved path produces one selected item, the collector should update `data/interim/manual_entry_0001.json` locally with approved, redacted, non-placeholder values for the required fields.

After that, run:

```bash
.venv/bin/python scripts/build_manual_collection_record.py data/interim/manual_entry_0001.json \
  --ack-controlled-details \
  --output data/interim/manual_record_0001.json \
  --collection-log data/interim/threads_pilot_v1_collection_log.csv

.venv/bin/python scripts/validate_thread_dataset.py data/interim/manual_record_0001.json --strict
```

Proceed to a second rehearsal item only if the first record passes governance review, schema validation, and the local manual collection checklist.

## Commit Boundary

Commit only this aggregate readiness note and index updates.

Do not commit:

- local-only files under `data/interim/`
- raw evidence or screenshots
- source URLs, handles, case IDs, or stakeholder case material
- filled controlled launch records if they contain sensitive details
- checkpoint outputs with item-level real evidence
