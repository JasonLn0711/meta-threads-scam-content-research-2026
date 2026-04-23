# Controlled Rehearsal Work Order: Threads Pilot v1

## Rehearsal Identity

| Field | Value |
|---|---|
| Work order ID | `CRWO-THREADS-PILOT-V1-2026-04-23` |
| Date opened | `2026-04-23` |
| Project owner | `owner_01` |
| Governance reviewer | `gov_01` |
| Collection lead | `collector_01` |
| Automation operator | `auto_op_01` |
| Research engineer | `eng_01` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Collection batch ID | `threads_pilot_v1_2026-05` |
| Controlled launch record | `CTRL-THREADS-PILOT-V1-CIB-2026-04-23` |
| Maximum rehearsal item count | 2 |
| Allowed collection paths | manual / stakeholder_provided / api_authorized / automation_assisted |

## Purpose

Run the first 1-2 controlled real rehearsal items before any broader real pilot accumulation.

This work order exists to prove that the team can:

- convert approved evidence into redacted local records
- keep raw evidence, session artifacts, and run details outside git
- apply the revised finance, OCR-sufficiency, and pseudo-official tag boundaries consistently
- decide whether the first 10-15 item checkpoint may begin

This work order does not authorize expansion beyond the 1-2 rehearsal items by itself.

## Required Inputs

| Input | Status | Notes |
|---|---|---|
| Controlled launch details completed outside git | required | exact source, storage, access, retention, and redaction values stay outside git |
| Local workspace initialized | required | `data/interim/` and related ignored files already exist |
| Item-1 preflight passed | required | `scripts/check_pilot_preflight.py --before-item-1 --ack-controlled-details` must report `ERROR: 0` |
| Controlled source path selected | required per item | manual, stakeholder-provided, API, or automation path must match launch record |
| Separate API/automation run record | required if applicable | exact run details stay outside git |
| Rehearsal checklist | required | use `templates/manual_collection_rehearsal_checklist.md` locally |
| Boundary watchlist | required | use `experiments/evaluation-notes/0013-controlled-rehearsal-boundary-watchlist.md` during review |

## Allowed Evidence Handling

| Area | Requirement |
|---|---|
| Raw evidence | outside git only |
| Source URLs | redacted or normalized repo-visible form only |
| Visible links | redacted or normalized repo-visible form only |
| Handles/contact info | category or redacted handle only |
| OCR text | risk-relevant, privacy-reviewed excerpt only |
| Screenshots | redacted references only in repo-visible files; raw screenshots outside git |
| API credentials, cookies, tokens, session artifacts, automation logs | outside git only |
| Landing-page, profile, or redirect context | allowed only when the controlled run record explicitly permits it |

## Local-Only Files For The Rehearsal

| File | Owner | Notes |
|---|---|---|
| `data/interim/manual_entry_0001.json` | `collector_01` | replace with approved local payload for item 1 |
| `data/interim/manual_record_0001.json` | `collector_01` / `eng_01` | built local record for item 1 |
| `data/interim/manual_entry_0002.json` | `collector_01` | optional second rehearsal item |
| `data/interim/manual_record_0002.json` | `collector_01` / `eng_01` | optional second rehearsal item |
| `data/interim/threads_pilot_v1_collection_log.csv` | `collector_01` | required operational log |
| local copy of `templates/manual_collection_rehearsal_checklist.md` | `collector_01` / `gov_01` | completed locally only |

## Commands

For each rehearsal item:

```bash
python scripts/build_manual_collection_record.py data/interim/manual_entry_0001.json \
  --ack-controlled-details \
  --output data/interim/manual_record_0001.json \
  --collection-log data/interim/threads_pilot_v1_collection_log.csv

python scripts/validate_thread_dataset.py data/interim/manual_record_0001.json --strict
```

If the evidence was captured through API or automation, record the separate controlled run identifier in the local checklist before the record-build step.

## Boundary Watch Items

During review, confirm all of the following:

1. readable finance discussion without a funnel stays `non_scam`
2. decisive OCR can remain `sufficient` evidence even when destination/profile detail was not captured
3. generic verification wording does not create `credential_or_personal_data_request` without an explicit data ask
4. confidence tracks likely agreement on the primary label and reason, not perfect subtype/tag overlap

## Pass Criteria

The controlled rehearsal passes only when:

- no raw evidence, credentials, session artifacts, or run-record details enter git
- governance errors are zero
- strict validation reports zero errors and zero warnings
- redaction quality passes reviewer inspection
- the local collection log reflects burden and exclusion notes correctly
- the team can explain any missing evidence without asking for unapproved context
- none of the boundary watch items fail repeatedly

## Pause Conditions

Pause the rehearsal and do not start the first 10-15 item checkpoint if:

- any raw evidence or sensitive run artifact enters git
- API or automation collection exceeds the controlled run record
- profile, landing-page, or redirect context is needed but not approved
- source URLs, handles, OCR, or screenshots cannot be redacted consistently
- the collector cannot map approved evidence into the current schema reliably
- the same boundary watch item fails on both rehearsal items

## Decision Output

Record one outcome after the rehearsal review:

- `pass_ready_for_calibration_or_first_10_15`
- `pass_with_limits`
- `pause_for_redaction_fix`
- `pause_for_schema_or_guideline_fix`
- `pause_for_authorization_review`
- `stop_source_for_pilot`

Record the repo-safe rehearsal readout with `templates/controlled_rehearsal_review.md` and `experiments/evaluation-notes/0014-controlled-rehearsal-review-protocol.md`.

If the result is `pass_ready_for_calibration_or_first_10_15` or `pass_with_limits`, rerun calibration only if the annotator team changed; otherwise the next repo-side gate is `docs/38-first-pilot-checkpoint-protocol.md` with `templates/pilot_checkpoint_review.md`.
