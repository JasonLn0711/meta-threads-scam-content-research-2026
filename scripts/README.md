# Scripts

Keep scripts minimal. This repo should not start with automation-heavy collection or model training code.

Acceptable early scripts:

- Schema validation
- CSV to JSONL conversion
- Simple keyword or pattern baseline
- OCR output normalization for approved local files
- Metric calculation from annotated outputs

Do not add automated Threads or Meta collection scripts without documented authorization in `governance/data-governance.md`.

## Current Scripts

```text
thread_dataset_utils.py       Shared local file parsing and validation helpers
validate_thread_dataset.py    Validate CSV/JSON/JSONL records against thread_item_schema_v1
convert_thread_dataset.py     Convert records between CSV, JSON, and JSONL
audit_thread_dataset.py       Produce a Markdown dataset audit summary
build_manual_collection_record.py Build one schema-valid record from manually supplied local fields
rule_baseline_v1.py           Run the first transparent rule baseline
run_rule_baseline.py          Run the modular rule baseline and write JSON/Markdown outputs
run_rule_calibration.py       Compare rule variants, threshold profiles, and export reviewer worksheet
summarize_pilot_results.py    Draft aggregate-only pilot result summary and decision memo
build_review_packets.py       Build local-only Markdown packets for item-level baseline review
compare_rule_variants.py      Compare text/reply/OCR/all rule baseline variants
compare_annotation_passes.py  Compare two annotator passes and export disagreements
prepare_calibration_files.py  Create blind calibration sheets and answer keys
init_pilot_workspace.py       Create empty local-only pilot files under ignored data/interim/
check_pilot_preflight.py      Check repo and local workspace readiness before item 1
```

## Example Usage

Validate a JSON sample:

```bash
python scripts/validate_thread_dataset.py templates/thread_item_sample_batch.json
```

Audit a first annotation CSV:

```bash
python scripts/audit_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv
```

Convert annotation CSV to JSONL:

```bash
python scripts/convert_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv \
  data/processed/threads_pilot_v1.jsonl \
  --validate
```

Build one manual collection record from a local JSON payload:

```bash
python scripts/build_manual_collection_record.py \
  data/samples/manual_collection_assistant_input_synthetic.json \
  --output experiments/evaluation-notes/outputs/synthetic-manual-collection-assistant/manual_record.json \
  --collection-log experiments/evaluation-notes/outputs/synthetic-manual-collection-assistant/collection_log.csv
```

Run the v1 rule baseline:

```bash
python scripts/rule_baseline_v1.py data/interim/threads_pilot_v1_annotations.csv \
  --variant all \
  --output data/processed/threads_pilot_v1_rule_baseline_predictions.csv
```

Run the modular baseline and write local JSON/Markdown outputs:

```bash
python scripts/run_rule_baseline.py data/samples/rule_baseline_eval_sample.json \
  --variant all \
  --run-name synthetic-eval-smoke
```

Run the calibration workbench:

```bash
python scripts/run_rule_calibration.py data/samples/rule_baseline_eval_sample.json \
  --run-name synthetic-calibration-smoke
```

Draft a pilot result synthesis:

```bash
python scripts/summarize_pilot_results.py data/samples/rule_baseline_eval_sample.json \
  --calibration-run-dir experiments/baselines/outputs/synthetic-calibration-smoke \
  --run-name synthetic-pilot-synthesis-smoke
```

Build local-only reviewer packets:

```bash
python scripts/build_review_packets.py data/samples/rule_baseline_eval_sample.json \
  --run-name synthetic-review-packets-smoke
```

Compare all v1 rule variants:

```bash
python scripts/compare_rule_variants.py data/processed/threads_pilot_v1.jsonl \
  > data/processed/threads_pilot_v1_rule_variant_comparison.md
```

Compare two annotation passes:

```bash
python scripts/compare_annotation_passes.py \
  data/interim/calibration_ann_01.csv \
  data/interim/calibration_ann_02.csv \
  --name-a ann_01 \
  --name-b ann_02 \
  --output data/processed/calibration_agreement.md \
  --disagreements-csv data/processed/calibration_disagreements.csv
```

Prepare blind calibration sheets:

```bash
python scripts/prepare_calibration_files.py data/samples/thread_item_sample_batch.csv \
  --blind-output data/interim/calibration_blind.csv \
  --answer-key-output data/processed/calibration_answer_key.csv \
  --annotator-copy ann_01:data/interim/calibration_ann_01.csv \
  --annotator-copy ann_02:data/interim/calibration_ann_02.csv
```

Preview local pilot workspace creation:

```bash
python scripts/init_pilot_workspace.py --dry-run
```

Initialize local pilot workspace files after controlled launch details are complete outside git:

```bash
python scripts/init_pilot_workspace.py --ack-controlled-details
```

Run repo-only pilot preflight checks:

```bash
python scripts/check_pilot_preflight.py
```

Run the item-1 preflight after controlled launch details and local workspace setup:

```bash
python scripts/check_pilot_preflight.py --before-item-1 --ack-controlled-details
```

## Governed Phase 1 Launch Sequence

These commands support manual governed operations only. They do not collect Threads data, scrape, crawl, browse, expand redirects, capture landing pages, inspect profiles, run live ingestion, or authorize any source.

Initialize the local workspace only after controlled launch details are complete outside git:

```bash
python scripts/init_pilot_workspace.py --ack-controlled-details
python scripts/check_pilot_preflight.py --before-item-1 --ack-controlled-details
```

Run the 1-2 item manual collection rehearsal from a manually prepared local input:

```bash
python scripts/build_manual_collection_record.py data/interim/manual_entry_0001.json \
  --ack-controlled-details \
  --output data/interim/manual_record_0001.json \
  --collection-log data/interim/threads_pilot_v1_collection_log.csv

python scripts/validate_thread_dataset.py data/interim/manual_record_0001.json --strict
```

Compare the 5-item annotator calibration passes:

```bash
python scripts/compare_annotation_passes.py \
  data/interim/calibration_ann_01.csv \
  data/interim/calibration_ann_02.csv \
  --name-a ann_01 \
  --name-b ann_02 \
  --output data/processed/calibration_agreement.md \
  --disagreements-csv data/processed/calibration_disagreements.csv
```

Run the first 10-15 item checkpoint audit after the local annotation CSV exists:

```bash
python scripts/validate_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv --strict
python scripts/audit_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv \
  > data/processed/threads_pilot_v1_checkpoint_audit.md
```

Do not continue to the rest of the 50-item pilot unless the checkpoint decision is `continue_to_50` or `continue_with_limits`.

Recommended baseline variants:

- `text_only`: use only `post_text`
- `text_reply`: use `post_text` plus `reply_texts`
- `text_ocr`: use `post_text` plus `ocr_text`
- `all`: use text, replies, OCR, visible links, handles, and redirects

`data/interim/` and `data/processed/` are ignored by git. Commit only aggregate experiment notes, not raw or sensitive outputs.
