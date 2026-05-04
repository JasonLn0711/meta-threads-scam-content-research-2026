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
prepare_controlled_access_path.py Prepare approved browser/API access paths without exposing secrets
validate_candidate_v2.py      Validate metadata-only v2 candidate YAML records
run_v2_ros.py                 Run sparse, embedding, discrepancy, and feature-queue v2 reports
run_contrast_aware_scoring.py Run contrast-aware sparse reviewer-routing scores
promote_sparse_features_v2.py Promote only human-accepted v2 feature candidates into a schema copy
generate_feature_candidates_v1.py Generate ranked feature hypotheses from valid missed-pattern discrepancy groups
generate_exploration_tasks.py Generate safe exploration tasks and metadata-only candidate stubs
build_exploration_batch.py Build a small metadata-only exploration batch from selected tasks
build_candidate_intake_v2.py Build Batch 0004 metadata-only manual-assisted intake worksheet
validate_candidate_intake_v2.py Validate a metadata-only candidate intake worksheet
convert_candidate_intake_v2.py Report on or convert completed intake entries into candidate_record_v2 files
```

## Local Python Setup

Some scripts read YAML config files under `configs/` and require `PyYAML`.

Recommended local setup:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Then run governed pilot tooling with `.venv/bin/python`:

```bash
.venv/bin/python scripts/check_pilot_preflight.py --before-item-1 --ack-controlled-details
```

## Example Usage

Validate a JSON sample:

```bash
.venv/bin/python scripts/validate_thread_dataset.py templates/thread_item_sample_batch.json
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

Run the v2 metadata-only dual-track research operating system:

```bash
python scripts/validate_candidate_v2.py data/candidates
python scripts/run_v2_ros.py
```

The v2 runner reads only structured candidate metadata and writes sparse ranking,
contrast-aware routing, sparse clusters, embedding-discovery clusters,
discrepancy reports, and feature-review proposals. It does not collect Threads
data, inspect profiles, crawl, train embeddings, make final scam decisions, or
promote new sparse features without human review.

Run contrast-aware reviewer routing by itself:

```bash
python scripts/run_contrast_aware_scoring.py
```

This writes `metrics/contrast_scores/latest.yaml` and treats contrast lanes as
reviewer-effort routing hypotheses, not labels.

After a human edits `meta-system/feature_review_queue/latest.yaml` and marks selected items `accepted`, write the active v2 schema:

```bash
python scripts/promote_sparse_features_v2.py
```

Pending and rejected feature candidates are ignored.

Generate feature hypotheses from the current discrepancy report without promotion:

```bash
python scripts/generate_feature_candidates_v1.py
```

This writes `meta-system/feature_candidates/auto_generated_v1.yaml` and filters to `missed_pattern` groups with at least three candidates.

Generate safe exploration tasks and metadata-only candidate stubs:

```bash
python scripts/generate_exploration_tasks.py
```

This writes `exploration/tasks/latest.yaml` and `data/candidate_stubs/latest.yaml`. It does not access external systems, store raw content, or authorize collection.

Build Batch 0004 from the top two low-coverage high-SVS exploration tasks:

```bash
python scripts/build_exploration_batch.py
```

This writes `exploration/batches/batch_0004.yaml` and `data/candidate_stubs/batch_0004.yaml`.

Build the Batch 0004 candidate intake worksheet:

```bash
python scripts/build_candidate_intake_v2.py
```

This writes `data/candidate_intake/batch_0004_intake.yaml`. It does not fabricate candidate records or labels.

Validate the Batch 0004 candidate intake worksheet:

```bash
python scripts/validate_candidate_intake_v2.py data/candidate_intake/batch_0004_intake.yaml --expected-count 10
```

Build the Batch 0004 conversion gate report:

```bash
python scripts/convert_candidate_intake_v2.py
```

This writes `data/candidate_intake/batch_0004_conversion_report.yaml`. It only writes candidate records when entries pass every completion gate and `--write-candidates` is explicitly provided.

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

## Controlled Access Path Preparation

Run 0008 prepares the next approved access path after run 0007 found governance material but no loadable browser session artifact and no ready API/session-aware client. These commands do not collect Threads items and do not print secrets.

Initialize the controlled-store slots and templates:

```bash
python scripts/prepare_controlled_access_path.py --init-controlled-store
```

After the approved browser-rendered session is exported outside git, import and validate it:

```bash
python scripts/prepare_controlled_access_path.py \
  --import-storage-state /path/to/approved/storage_state.json \
  --check-storage-state \
  --require-ready
```

Check API/session-aware credential readiness without printing token values:

```bash
python scripts/prepare_controlled_access_path.py --check-api-env
```

Dry-run the API probe readiness without a network request:

```bash
python scripts/prepare_controlled_access_path.py --api-dry-run
```

Execute the approved API probe only after the run record authorizes it and `META_API_PROBE_URL` plus `META_API_ACCESS_TOKEN` are set in the outside-git controlled env file:

```bash
python scripts/prepare_controlled_access_path.py --execute-api-probe
```

Raw API output and automation logs are written only to the outside-git controlled store. Do not copy them into `data/interim/`, `data/processed/`, or git.

## Governed Phase 1 Launch Sequence

These commands support manual governed operations only. They do not collect Threads data, scrape, crawl, browse, expand redirects, capture landing pages, inspect profiles, run live ingestion, or authorize any source.

Initialize the local workspace only after controlled launch details are complete outside git:

```bash
.venv/bin/python scripts/init_pilot_workspace.py --ack-controlled-details
.venv/bin/python scripts/check_pilot_preflight.py --before-item-1 --ack-controlled-details
```

Run the 1-2 item manual collection rehearsal from a manually prepared local input:

```bash
.venv/bin/python scripts/build_manual_collection_record.py data/interim/manual_entry_0001.json \
  --ack-controlled-details \
  --output data/interim/manual_record_0001.json \
  --collection-log data/interim/threads_pilot_v1_collection_log.csv

.venv/bin/python scripts/validate_thread_dataset.py data/interim/manual_record_0001.json --strict
```

The manual input must not contain unresolved placeholder markers such as `FILL_`, `REPLACE_`, or `PENDING_`. The assistant blocks real records with those markers even when `authorization_status` is `approved`.

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

Do not use `summarize_pilot_results.py` to make the first checkpoint decision. If it is run on fewer than 50 non-synthetic items, it should return `first_checkpoint_review_required`; complete `templates/pilot_checkpoint_review.md` instead.

Draft the post-50 pilot synthesis only after the checkpoint-approved 50-item pilot is annotated, audited, and reviewed:

```bash
python scripts/summarize_pilot_results.py data/interim/threads_pilot_v1_annotations.csv \
  --calibration-run-dir experiments/baselines/outputs/pilot-rule-calibration-v1 \
  --run-name pilot-v1-decision-draft \
  --governance-rating green \
  --privacy-rating green \
  --reviewer-burden-rating yellow
```

Recommended baseline variants:

- `text_only`: use only `post_text`
- `text_reply`: use `post_text` plus `reply_texts`
- `text_ocr`: use `post_text` plus `ocr_text`
- `all`: use text, replies, OCR, visible links, handles, and redirects

`data/interim/` and `data/processed/` are ignored by git. Commit only aggregate experiment notes, not raw or sensitive outputs.
