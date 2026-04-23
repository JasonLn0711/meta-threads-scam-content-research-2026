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
rule_baseline_v1.py           Run the first transparent rule baseline
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

Run the v1 rule baseline:

```bash
python scripts/rule_baseline_v1.py data/interim/threads_pilot_v1_annotations.csv \
  --variant all \
  --output data/processed/threads_pilot_v1_rule_baseline_predictions.csv
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

Recommended baseline variants:

- `text_only`: use only `post_text`
- `text_reply`: use `post_text` plus `reply_texts`
- `text_ocr`: use `post_text` plus `ocr_text`
- `all`: use text, replies, OCR, visible links, handles, and redirects

`data/interim/` and `data/processed/` are ignored by git. Commit only aggregate experiment notes, not raw or sensitive outputs.
