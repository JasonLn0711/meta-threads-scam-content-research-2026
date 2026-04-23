# Collection And Redaction SOP

## Purpose

This SOP defines how to prepare the first Threads dataset batch without violating the project boundary. It covers manual/stakeholder/API/automation-assisted collection, evidence minimization, redaction, local storage, collection logging, and handoff to annotation.

For the CIB-authorized pilot, API access and all research-required automation are authorized only through `governance/pilot-launch/threads_pilot_v1_2026-05_controlled_launch_record.md` and Decision 0018. This SOP does not authorize unscope automation or production use.

## Preconditions

Before collecting any real item:

- Complete source candidate intake in `templates/source_candidate_intake.md`.
- Record the source candidate in `governance/source-intake-register.md`.
- Build the source sampling frame with `templates/source_sampling_frame_template.csv`.
- Complete `docs/36-stakeholder-authorization-packet.md`.
- Complete `templates/stakeholder_authorization_decision_record.md`.
- Confirm the source is allowed under `governance/data-governance.md`.
- Complete or link `templates/data_authorization_request.md`.
- Decide where raw evidence will live outside git.
- Confirm who may see raw evidence.
- Confirm retention and deletion expectations.
- Confirm whether source URLs may be stored, redacted, normalized, or omitted.
- Assign a `collection_batch_id`.
- Assign pseudonymous collector and annotator IDs.
- Complete `templates/real_pilot_readiness_review.md` using `docs/35-real-pilot-readiness-review.md`.
- Complete `templates/pilot_batch_work_order.md` when preparing the 50-item pilot.

If any precondition is unresolved, use only synthetic examples.

## Approved Phase-1 Collection Modes

| Mode | Allowed when | Notes |
|---|---|---|
| Synthetic dry run | Always allowed | No real Threads evidence. |
| Stakeholder-provided cases | Sharing, retention, redaction, and use are approved | Preserve stakeholder report reference only if allowed. |
| Manual public examples | Legal/platform comfort is documented | Governed by the controlled launch record. |
| API-authorized examples | API approval is recorded | Approved for the CIB pilot under run-record controls. |
| Automation-assisted examples | CIB automation authorization and run record exist | Raw outputs, credentials, session artifacts, and logs stay outside git. |

Not approved by this SOP unless explicitly run-scoped under the CIB controlled launch record:

- scraping
- browser automation
- bulk export
- account/profile crawling
- landing-page crawling
- redirect-chain capture
- raw browser profiles, cookies, or credentials

## Minimal Evidence To Record

Record only what is needed for the v1 schema:

- post text, if visible and allowed
- selected relevant replies/comments, if visible and allowed
- image count and redacted local image reference, if needed
- OCR text relevant to risk signals
- visible external link text or normalized/redacted URL, if allowed
- visible contact handle category or redacted handle, if allowed
- visible platform redirects such as LINE, WhatsApp, Telegram, private group, or external site
- screenshot and link snapshot status
- collection method, timestamp, authorization status, and redaction notes

Do not collect profile history, follower/following lists, unrelated comments, unrelated personal names, or broad account metadata unless a later governance decision approves it.

## Item ID And Batch Naming

Recommended batch IDs:

```text
threads_dry_run_v1_2026-04
threads_pilot_v1_2026-05
threads_sample_v1_2026-05
```

Recommended item IDs:

```text
threads-pilot-v1-0001
threads-pilot-v1-0002
```

Do not encode names, handles, URLs, or source identities in `item_id`.

## Collection Log

Use `templates/collection_log_template.csv` while collecting. The collection log is local-only unless it is fully de-identified and approved.

The collection log records:

- candidate bucket
- collector ID
- source type
- authorization status
- whether raw evidence exists outside git
- whether redaction is complete
- whether the item is ready for annotation
- why any candidate was excluded

## Redaction Rules

Use `templates/redaction_checklist.md` before annotation and before any aggregate sharing.

Default redaction posture:

- Remove or mask ordinary user handles unless needed and approved.
- Remove unrelated names, faces, profile photos, personal messages, and comments.
- Replace contact handles with category and redacted value, such as `telegram:[redacted]`.
- Prefer normalized domains over full tracking URLs when possible.
- Remove tracking parameters unless the full URL is approved and analytically necessary.
- Keep OCR text only when it supports risk assessment or evidence audit.
- Do not include raw screenshots in git.

## Screenshot And Image Handling

Set `screenshot_snapshot_status`:

- `not_applicable`: no image/screenshot evidence.
- `not_captured`: image exists but was not captured.
- `captured_redacted`: redacted snapshot exists outside git or in approved storage.
- `captured_full_approved`: full snapshot exists and approval is recorded.
- `unavailable`: image could not be accessed or retained.

For the first pilot, prefer `captured_redacted` or `not_captured` over storing sensitive full screenshots.

## Link Handling

Set `link_snapshot_status`:

- `not_applicable`: no visible link.
- `not_captured`: link visible but destination was not captured.
- `captured_redacted`: link text/domain or safe screenshot is retained in redacted form.
- `captured_full_approved`: full destination evidence is retained with approval.
- `unavailable`: link could not be accessed or retained.

Redirect and landing evidence may be captured only when approved in the CIB run record. Otherwise, retain visible link text or domain as the signal.

## OCR Handling

OCR is allowed only on approved local/redacted images or stakeholder-provided images under the approved use. OCR text should be reviewed for personal data before entering annotation files.

When OCR is low quality, record:

- `ocr_text` as the readable portion only, or blank if not usable
- `missing_evidence`: `ocr_missing_or_low_quality`
- `metadata_notes`: short OCR quality note

## Collection QA Before Annotation

Before a record enters annotation:

- validate required identity/provenance fields
- confirm no raw personal data was copied into tracked files
- confirm `has_image`, `image_count`, and `image_paths` are consistent
- confirm `has_external_link` and `external_links` are consistent
- confirm redaction notes are present when redaction occurred
- confirm uncertain storage decisions are described in `metadata_notes`

Use:

```bash
python scripts/validate_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv
```

The optional manual collection assistant can help structure one manually supplied local JSON payload into a schema-valid record and collection-log row:

```bash
python scripts/build_manual_collection_record.py data/interim/manual_entry_0001.json \
  --ack-controlled-details \
  --output data/interim/manual_record_0001.json \
  --collection-log data/interim/threads_pilot_v1_collection_log.csv
```

This assistant does not collect data, fetch URLs, crawl pages, run OCR, or authorize any source. It only structures fields the collector has already captured under the controlled launch limits. Use separate run records for API or automation-assisted capture.

## Controlled Collection Rehearsal

Before the first 10-15 item checkpoint, run a 1-2 item rehearsal using only approved, controlled-launch fields. The objective is to test whether the team can turn manual, stakeholder-provided, API, or automation-assisted evidence into redacted, schema-valid local records without exceeding the controlled run record.

Use rehearsal records to catch operational mistakes, not to make pilot findings. A good rehearsal record:

- has a non-identifying `item_id`
- uses only an approved `source_type`, `collection_method`, and `authorization_status`
- stores raw evidence only in the approved outside-git location
- uses approved redacted or minimized forms for source URLs, visible links, contact handles, OCR text, screenshots, and replies
- fills `screenshot_snapshot_status`, `link_snapshot_status`, `privacy_redaction_notes`, and `missing_evidence` where relevant
- records collection burden and exclusion reasons in the local collection log

Run:

```bash
python scripts/build_manual_collection_record.py data/interim/manual_entry_0001.json \
  --ack-controlled-details \
  --output data/interim/manual_record_0001.json \
  --collection-log data/interim/threads_pilot_v1_collection_log.csv

python scripts/validate_thread_dataset.py data/interim/manual_record_0001.json --strict
```

Use `templates/manual_collection_rehearsal_checklist.md` for the human review.

Common rehearsal mistakes to catch:

- copying raw source URLs when only redacted references are approved
- storing contact handles, phone numbers, emails, payment details, or referral codes in raw form
- recording full OCR text that includes unrelated personal details
- including reply, profile, redirect, or landing context because it seems useful rather than because it is approved in the run record
- leaving screenshot/link status blank
- failing to log collection burden or exclusion reason
- treating warnings from the manual assistant as acceptable without governance review

Rehearsal passes only when:

- validation returns zero errors and zero strict warnings
- the collection-log row uses only approved fields
- redaction quality passes reviewer inspection
- no raw evidence or sensitive controlled detail is in git
- the collector can explain what was excluded and why

Rehearsal fails and collection pauses if:

- the collector or automation operator needs unapproved profile/account/landing-page/redirect context
- approved fields are too ambiguous to populate consistently
- redaction cannot be done reliably
- schema fields are missing, confusing, or too burdensome for the approved evidence
- any item requires automation or live platform ingestion outside the CIB controlled launch record

If the schema appears wrong during rehearsal, do not improvise new fields in local files. Record the issue as a schema-revision candidate and update `data-contracts/thread_item_schema_v1.json`, templates, and annotation guidance only after project-owner review.

The full post-authorization execution sequence is in `docs/29-authorized-pilot-execution-plan.md`.

## Stop Conditions

Pause collection if:

- the team is unsure whether a collection method is allowed
- raw screenshots or personal data are being copied into git
- source URLs include sensitive tracking or personal information and no redaction rule exists
- annotators need context that is not approved to collect
- stakeholder evidence has unclear retention or sharing restrictions
- collection or automation is drifting beyond the controlled run record

## Handoff To Annotation

After collection QA:

1. Move only the redacted/local annotation file into `data/interim/`.
2. Validate the file.
3. Annotate according to `docs/06-annotation-guideline-v1.md`.
4. Use `docs/22-annotation-pilot-runbook.md` for dry run and pilot execution.
5. Convert to JSONL only after validation.

No raw evidence should be committed at any stage.
