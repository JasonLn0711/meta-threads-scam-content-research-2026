# Evaluation Note 0006: Manual Collection Assistant Smoke Test

## Hypothesis

A manual collection assistant can reduce schema and provenance errors without adding scraping, landing-page capture, redirect expansion, or other unapproved automation.

## Dataset Slice

Initial smoke test:

- `data/samples/manual_collection_assistant_input_synthetic.json`
- synthetic-only payload
- no real Threads evidence

## Method

```bash
python scripts/build_manual_collection_record.py \
  data/samples/manual_collection_assistant_input_synthetic.json \
  --output experiments/evaluation-notes/outputs/synthetic-manual-collection-assistant/manual_record.json \
  --collection-log experiments/evaluation-notes/outputs/synthetic-manual-collection-assistant/collection_log.csv \
  --append-jsonl experiments/evaluation-notes/outputs/synthetic-manual-collection-assistant/manual_records.jsonl
```

Then validate:

```bash
python scripts/validate_thread_dataset.py \
  experiments/evaluation-notes/outputs/synthetic-manual-collection-assistant/manual_record.json \
  --strict
```

## Expected Result

- governance errors: 0
- schema errors: 0
- schema warnings: 0
- generated record uses `authorization_status: synthetic_only`
- generated contact handles are redacted or categorical
- generated outputs stay under ignored local output paths

## Decision Use

If the smoke test passes, the assistant is ready for local manual pilot rehearsal after controlled launch details are complete.

This does not authorize real collection and does not permit automation.

## Commit Boundary

Commit this note, config, code, and synthetic input.

Do not commit generated real manual records, real collection logs, raw evidence, source URLs, personal handles, screenshots, browser artifacts, or item-level sensitive evidence.
