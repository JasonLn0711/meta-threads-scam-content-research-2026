# Controlled Crawler Acquisition Plan

## Purpose

Define the next acquisition path now that CIB and other units cannot provide redacted case examples and manual controlled sampling is not available.

This plan permits only a controlled low-speed crawler rehearsal under the existing CIB-authorized API and automation scope. It does not authorize open-ended scraping, evasion, bulk monitoring, production detection, or legal fraud determinations.

## Current Status

| Area | Status |
|---|---|
| CIB authorization | complete for current controlled pilot path |
| Redacted CIB case handoff | unavailable |
| Manual controlled sampling | unavailable |
| API / automation authorization | approved under Decision 0018 |
| Practical next acquisition path | controlled low-speed crawler rehearsal |
| First required output | one redacted, schema-valid `manual_record_0001.json` |
| First checkpoint status | blocked until one-item rehearsal review passes |

## Operating Principle

Low speed is a burden and risk control, not the whole authorization.

The crawler is allowed only because it is:

- tied to the CIB-approved research purpose
- run under a written run record
- limited to one rehearsal item at first
- field-limited
- redaction-first
- local-only for item-level outputs
- stopped before any checkpoint or scale-up decision

## One-Item Rehearsal Sequence

1. Fill a local or controlled copy of `templates/controlled_crawler_run_record.md`.
2. Confirm source category, operator, purpose, item limit, field allowlist, raw output location, and stop conditions.
3. Run only the lowest practical crawl needed to identify one candidate item.
4. Keep raw outputs, browser/session artifacts, credentials, tokens, screenshots, logs, and full source references outside git.
5. Redact the selected item into `data/interim/manual_entry_0001.json`.
6. Build the local record:

```bash
.venv/bin/python scripts/build_manual_collection_record.py data/interim/manual_entry_0001.json \
  --ack-controlled-details \
  --output data/interim/manual_record_0001.json \
  --collection-log data/interim/threads_pilot_v1_collection_log.csv
```

7. Strict-validate:

```bash
.venv/bin/python scripts/validate_thread_dataset.py data/interim/manual_record_0001.json --strict
```

8. Complete the local rehearsal checklist and aggregate review.
9. Decide whether the first 10-15 item checkpoint can begin.

## Default Rehearsal Limits

| Limit | Value |
|---|---|
| Rehearsal output | exactly 1 selected item |
| Candidate review cap | 5 candidates maximum |
| Runtime cap | 30 minutes maximum |
| Parallel workers | 1 |
| Minimum delay | 30 seconds between page/API/object fetches |
| Retries | at most 1 retry per failed fetch |
| Redirect or landing-page capture | only if stated in the run record |
| Profile/account context | only if stated in the run record |
| Broad comments/replies | not in the first rehearsal unless stated in the run record |
| Storage | raw outside git; redacted local-only under ignored `data/interim/` |

The run record may make these limits stricter. It must not make them broader without a later decision or owner approval.

## Allowed Fields For First Rehearsal

Use the existing `thread_item_schema_v1` fields only:

- `post_text`
- selected `reply_texts`
- `image_count`
- redacted `image_paths`
- privacy-reviewed `ocr_text`
- domain-only or redacted `external_links`
- categorical or redacted `visible_contact_handles`
- `visible_platform_redirects`
- `screenshot_snapshot_status`
- `link_snapshot_status`
- `metadata_notes`
- `privacy_redaction_notes`
- `missing_evidence`

Do not add new fields during the rehearsal. If the approved evidence does not fit the schema, pause and record a schema-revision candidate.

## Forbidden During First Rehearsal

- raw screenshots in git
- full source URLs in git
- raw handles in git
- credentials, tokens, cookies, browser profiles, HAR files, or session artifacts in git
- unrelated personal data
- follower/following graph capture
- broad account profiling
- unrelated Meta surfaces
- enforcement, public accusation, or legal conclusions
- expanding from one item into a batch without review

## Pass Criteria

The crawler rehearsal passes only if:

- one selected item is redacted into `manual_entry_0001.json`
- build produces `manual_record_0001.json`
- strict validation returns zero errors and zero warnings
- local collection log records the item
- redaction notes are clear
- raw evidence stayed outside git
- no stop condition was triggered
- the aggregate rehearsal review records `pass_ready_for_calibration_or_first_10_15` or `pass_with_limits`

## If The Rehearsal Fails

Pause before the first 10-15 item checkpoint and choose the appropriate outcome:

- `pause_for_redaction_fix`
- `pause_for_schema_or_guideline_fix`
- `pause_for_collection_fix`
- `pause_for_authorization_review`
- `stop_source_for_pilot`

Use `pause_for_authorization_review` only if the crawler needs evidence, access, source, or collection methods outside the controlled CIB-approved path.
