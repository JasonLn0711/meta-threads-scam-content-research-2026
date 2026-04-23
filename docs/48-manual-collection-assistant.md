# Manual Collection Assistant

## Purpose

The manual collection assistant helps a collector turn manually supplied, approved fields into a schema-valid `thread_item_schema_v1` record.

It is a guardrail tool, not a collection engine.

It does not:

- fetch Threads pages
- scrape, crawl, or browse
- expand redirects
- capture landing pages
- inspect profiles or accounts
- authorize real collection

The assistant exists because the first pilot depends on consistent, privacy-minimized, schema-valid records after controlled launch details are complete outside git.

## Current Authorization Boundary

The current approved pilot method is manual only.

The assistant therefore uses:

```text
configs/manual_collection_assistant.yaml
```

The config explicitly keeps these disabled:

- network access
- scraping
- browser automation
- landing-page capture
- redirect expansion
- profile review

Changing a config flag is not authorization. A later governance record would be required before any automated mode could exist.

Low-speed automation is still automation. As of `2026-04-23`, the project has rejected or paused low-speed automated Threads/Meta collection without recorded legal approval, platform access conditions, stakeholder authorization, and approved scope.

## Input Shape

Prepare one local JSON object with manually entered fields.

Minimum practical fields:

```json
{
  "item_id": "threads-pilot-v1-0001",
  "source_type": "manual_public",
  "collection_method": "manual_capture",
  "authorization_status": "approved",
  "post_text": "Redacted manually captured post text.",
  "reply_texts": ["Selected relevant redacted reply."],
  "ocr_text": "",
  "image_count": 0,
  "privacy_redaction_notes": "Removed ordinary handles and unrelated personal details."
}
```

Use `data/samples/manual_collection_assistant_input_synthetic.json` for a synthetic smoke-test example.

## Command

Synthetic smoke test:

```bash
python scripts/build_manual_collection_record.py \
  data/samples/manual_collection_assistant_input_synthetic.json \
  --output experiments/evaluation-notes/outputs/synthetic-manual-collection-assistant/manual_record.json \
  --collection-log experiments/evaluation-notes/outputs/synthetic-manual-collection-assistant/collection_log.csv \
  --append-jsonl experiments/evaluation-notes/outputs/synthetic-manual-collection-assistant/manual_records.jsonl
```

Real pilot use after controlled launch details are complete outside git:

```bash
python scripts/build_manual_collection_record.py data/interim/manual_entry_0001.json \
  --ack-controlled-details \
  --output data/interim/manual_record_0001.json \
  --append-jsonl data/interim/threads_pilot_v1_annotations_seed.jsonl \
  --collection-log data/interim/threads_pilot_v1_collection_log.csv
```

`data/interim/` is ignored by git. Do not commit generated real records if they contain item-level evidence.

## 1-2 Item Rehearsal

Run a rehearsal before real volume begins. The rehearsal proves the collector can prepare approved local inputs, build a schema-valid record, append the local collection log, and pass redaction review without using unapproved context.

Use one or two local `data/interim/manual_entry_*.json` payloads prepared from approved manual or stakeholder-provided fields. The input JSON itself is local-only and must not contain raw personal data, full source URLs, unredacted contact handles, browser artifacts, credentials, or other forbidden fields.

Command for the first rehearsal record:

```bash
python scripts/build_manual_collection_record.py data/interim/manual_entry_0001.json \
  --ack-controlled-details \
  --output data/interim/manual_record_0001.json \
  --collection-log data/interim/threads_pilot_v1_collection_log.csv

python scripts/validate_thread_dataset.py data/interim/manual_record_0001.json --strict
```

Review `data/interim/manual_record_0001.json` and `data/interim/threads_pilot_v1_collection_log.csv` locally with `templates/manual_collection_rehearsal_checklist.md`.

Pass criteria:

- `governance_errors: 0`
- `schema_errors: 0`
- strict validation passes
- any governance warning is reviewed against the controlled launch record before continuation
- redaction notes explain links, handles, OCR, screenshots, or stakeholder context
- no unapproved fields or outside context are needed to make the record reviewable

Fail and pause if the collector reaches for profile review, landing-page content, redirect chains, broad comment history, raw handles, full URLs, or automation. If this happens, update governance or narrow the source before collecting more items.

## Outputs

The script can write:

| Output | Use |
|---|---|
| JSON record | One schema-valid `thread_item_schema_v1` object. |
| JSONL append | Local staging file for later validation/conversion. |
| collection log CSV row | Local collector workflow tracking. |
| action log JSONL | Local audit trail under ignored `data/interim/`. |

The action log intentionally does not store target URLs by default.

## Governance Checks

The assistant blocks:

- real records without `--ack-controlled-details`
- unsupported source types
- unsupported collection methods
- real records without `authorization_status: approved`
- full source URLs when config requires redacted or empty source references
- full snapshots when config disables `captured_full_approved`
- any config that enables scraping, automation, landing capture, redirect expansion, profile review, or network access

The assistant warns when:

- visible contact handles are not redacted or categorical
- links or handles exist but `privacy_redaction_notes` is blank

Warnings require review. Use `--allow-governance-warnings` only after confirming the warning is acceptable under the controlled launch record.

## Workflow Position

Use this assistant after:

1. Source and method authorization are complete.
2. Controlled launch details are complete outside git.
3. The local pilot workspace has been initialized.
4. The collector has manually captured only approved fields.

Then run:

```bash
python scripts/validate_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv --strict
```

or validate generated JSON/JSONL staging files before annotation handoff.

## Stop Conditions

Pause if the collector needs:

- unapproved source URLs
- profile/account context
- landing-page content
- redirect-chain context
- broad screenshot capture
- raw handles or personal identifiers
- automated collection

In those cases, revise governance and the controlled launch record before collecting more items.
