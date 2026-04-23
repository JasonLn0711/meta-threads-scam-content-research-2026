# Collection And Redaction SOP

## Purpose

This SOP defines how to prepare the first Threads dataset batch without violating the project boundary. It covers manual/stakeholder collection, evidence minimization, redaction, local storage, collection logging, and handoff to annotation.

This document does not authorize automated collection. It is an operating procedure for approved manual or stakeholder-provided evidence only.

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
| Manual public examples | Legal/platform comfort is documented | Manual recording only; no automation. |
| API-authorized examples | API approval is recorded | Not currently approved by default. |

Not approved by this SOP:

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

Do not crawl links, expand redirects, visit suspicious destinations, or capture landing pages unless approved. Visible link text can still be useful as a signal.

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

This assistant does not collect data, fetch URLs, crawl pages, run OCR, or authorize any source. It only structures fields the collector has already captured under the controlled launch limits.

The full post-authorization execution sequence is in `docs/29-authorized-pilot-execution-plan.md`.

## Stop Conditions

Pause collection if:

- the team is unsure whether a collection method is allowed
- raw screenshots or personal data are being copied into git
- source URLs include sensitive tracking or personal information and no redaction rule exists
- annotators need context that is not approved to collect
- stakeholder evidence has unclear retention or sharing restrictions
- collection is drifting toward automation

## Handoff To Annotation

After collection QA:

1. Move only the redacted/local annotation file into `data/interim/`.
2. Validate the file.
3. Annotate according to `docs/06-annotation-guideline-v1.md`.
4. Use `docs/22-annotation-pilot-runbook.md` for dry run and pilot execution.
5. Convert to JSONL only after validation.

No raw evidence should be committed at any stage.
