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

The manual collection assistant remains manual-only. The broader CIB pilot now has separate API and automation authorization in `governance/pilot-launch/threads_pilot_v1_2026-05_controlled_launch_record.md`; this assistant is only for manually supplied local fields.

The assistant therefore uses:

```text
configs/manual_collection_assistant.yaml
```

Install the local script dependency before using the assistant:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

The config explicitly keeps these disabled:

- network access
- scraping
- browser automation
- landing-page capture
- redirect expansion
- profile review

Changing a config flag is not authorization for this assistant. API or automation work must use the controlled launch record and a separate run record.

Low-speed automation is still automation. Decision 0016 still rejects unscope low-speed automation; Decision 0018 records the separate CIB-authorized API and automation scope for this pilot.

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

Use one or two local `data/interim/manual_entry_*.json` payloads prepared from approved manual fields, stakeholder-provided fields, or a redacted selected item produced under a completed controlled run record. The input JSON itself is local-only and must not contain raw personal data, full source URLs, unredacted contact handles, browser artifacts, credentials, or other forbidden fields.

Before running the builder on a real rehearsal input, complete a local copy of:

```text
templates/manual_collection_prebuild_handoff.md
```

This handoff is for the collector and governance reviewer to confirm that the local intake has no placeholders, raw identifiers, unapproved context, full URLs, raw handles, or unsupported evidence fields.

Command for the first rehearsal record:

```bash
.venv/bin/python scripts/build_manual_collection_record.py data/interim/manual_entry_0001.json \
  --ack-controlled-details \
  --output data/interim/manual_record_0001.json \
  --collection-log data/interim/threads_pilot_v1_collection_log.csv

.venv/bin/python scripts/validate_thread_dataset.py data/interim/manual_record_0001.json --strict
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
- real records that still contain unresolved placeholder markers such as `FILL_`, `REPLACE_`, or `PENDING_`
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
