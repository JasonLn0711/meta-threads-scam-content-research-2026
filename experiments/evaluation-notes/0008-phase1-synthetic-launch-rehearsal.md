# Phase 1 Synthetic Launch Rehearsal

## Objective

Exercise the governed Phase 1 launch bridge end to end using synthetic-only inputs:

1. manual record building
2. strict validation
3. calibration file preparation
4. annotation-pass comparison
5. checkpoint-style dataset audit
6. rule baseline
7. rule calibration matrix
8. reviewer packets
9. pilot synthesis draft

This rehearsal does not collect real Threads data, does not inspect live content, does not authorize scraping or automation, and does not support a real expansion decision.

## Dataset Slice

| Input | Use |
|---|---|
| `data/samples/manual_collection_assistant_input_synthetic.json` | Synthetic manual-record rehearsal payload. |
| `data/samples/thread_item_sample_batch.csv` | Five-item synthetic calibration/checkpoint-style sample. |
| `data/samples/rule_baseline_eval_sample.json` | Six-item synthetic rule-baseline evaluation sample. |

All generated outputs were written under ignored local output folders:

```text
experiments/evaluation-notes/outputs/phase1-synthetic-launch-rehearsal/
experiments/evaluation-notes/outputs/phase1-synthetic-launch-rehearsal-packets/
experiments/evaluation-notes/outputs/phase1-synthetic-launch-rehearsal-synthesis/
experiments/baselines/outputs/phase1-synthetic-launch-rehearsal-baseline/
experiments/baselines/outputs/phase1-synthetic-launch-rehearsal-calibration/
```

## Commands Run

Manual record build:

```bash
python scripts/build_manual_collection_record.py \
  data/samples/manual_collection_assistant_input_synthetic.json \
  --output experiments/evaluation-notes/outputs/phase1-synthetic-launch-rehearsal/manual_record.json \
  --collection-log experiments/evaluation-notes/outputs/phase1-synthetic-launch-rehearsal/collection_log.csv \
  --append-jsonl experiments/evaluation-notes/outputs/phase1-synthetic-launch-rehearsal/manual_records.jsonl
```

Manual record validation:

```bash
python scripts/validate_thread_dataset.py \
  experiments/evaluation-notes/outputs/phase1-synthetic-launch-rehearsal/manual_record.json \
  --strict
```

Calibration file preparation:

```bash
python scripts/prepare_calibration_files.py data/samples/thread_item_sample_batch.csv \
  --blind-output experiments/evaluation-notes/outputs/phase1-synthetic-launch-rehearsal/calibration_blind.csv \
  --answer-key-output experiments/evaluation-notes/outputs/phase1-synthetic-launch-rehearsal/calibration_answer_key.csv \
  --annotator-copy ann_01:experiments/evaluation-notes/outputs/phase1-synthetic-launch-rehearsal/calibration_ann_01.csv \
  --annotator-copy ann_02:experiments/evaluation-notes/outputs/phase1-synthetic-launch-rehearsal/calibration_ann_02.csv
```

Synthetic agreement comparison:

```bash
python scripts/compare_annotation_passes.py \
  data/samples/thread_item_sample_batch.csv \
  data/samples/thread_item_sample_batch.csv \
  --name-a synthetic_ann_01 \
  --name-b synthetic_ann_02 \
  --output experiments/evaluation-notes/outputs/phase1-synthetic-launch-rehearsal/calibration_agreement.md \
  --disagreements-csv experiments/evaluation-notes/outputs/phase1-synthetic-launch-rehearsal/calibration_disagreements.csv
```

Checkpoint-style audit:

```bash
python scripts/audit_thread_dataset.py data/samples/thread_item_sample_batch.csv
```

Baseline and calibration:

```bash
python scripts/run_rule_baseline.py data/samples/rule_baseline_eval_sample.json \
  --variant all \
  --run-name phase1-synthetic-launch-rehearsal-baseline

python scripts/run_rule_calibration.py data/samples/rule_baseline_eval_sample.json \
  --run-name phase1-synthetic-launch-rehearsal-calibration
```

Reviewer packets and synthesis:

```bash
python scripts/build_review_packets.py data/samples/rule_baseline_eval_sample.json \
  --run-name phase1-synthetic-launch-rehearsal-packets

python scripts/summarize_pilot_results.py data/samples/rule_baseline_eval_sample.json \
  --calibration-run-dir experiments/baselines/outputs/phase1-synthetic-launch-rehearsal-calibration \
  --run-name phase1-synthetic-launch-rehearsal-synthesis \
  --governance-rating unknown \
  --privacy-rating unknown \
  --reviewer-burden-rating unknown
```

## Results

| Check | Result |
|---|---|
| Manual assistant governance errors | 0 |
| Manual assistant governance warnings | 0 |
| Manual assistant schema errors | 0 |
| Manual assistant schema warnings | 0 |
| Strict validation of generated manual record | 1 checked record, 0 errors, 0 warnings |
| Calibration blind records prepared | 5 |
| Calibration answer-key records prepared | 5 |
| Synthetic agreement comparison | 5 shared items, 0 disagreements |
| Synthetic sample audit | 5 items, 0 schema errors, 0 schema warnings |
| Baseline `all` run | 6 items; 5 binary metric items; precision 1.000, recall 1.000, F1 1.000 |
| Calibration matrix | 5 profiles x 4 variants = 20 summary rows |
| Calibration changed decisions | 46 changed risk decisions versus `baseline/text_only` |
| Reviewer packets | 6 local-only packets generated |
| Synthesis recommendation | `synthetic_dry_run_no_expansion_decision` |

Audit findings on the five-item synthetic sample were expected:

- all records are `researcher_synthetic`
- all records use `synthetic` collection
- the source and method skew is therefore total by design

Rule-calibration findings were also expected for the synthetic fixture:

- `baseline/text_only` had recall 0.250 on five binary metric items
- `baseline/text_reply` and `baseline/text_ocr` each raised recall to 0.750
- `baseline/all` reached precision 1.000, recall 1.000, and F1 1.000 on the tiny synthetic fixture
- this is tooling evidence only, not real-world performance evidence

## Interpretation

The integrated toolchain is mechanically ready for a governed Phase 1 launch after the human-controlled launch record is complete outside git.

What the rehearsal confirms:

- the manual assistant can produce a schema-valid record from a synthetic local payload
- calibration files can be prepared without modifying committed data
- agreement comparison can produce local disagreement artifacts
- audit output can surface label/evidence/source skew
- rule baseline, calibration, review packets, and synthesis can run on synthetic fixtures
- synthesis correctly refuses to make an expansion decision from synthetic-only data

What the rehearsal does not confirm:

- real source authorization
- real redaction quality
- real collection burden
- real annotator agreement
- real OCR/link/reply usefulness
- real baseline performance
- readiness to continue beyond 10-15 real items

## Decision Implication

The next major research blocker remains outside git: complete the controlled launch record with exact source, storage, access, retention, redaction, screenshot, OCR, URL/link, handle/contact, role-ID, permitted-field, forbidden-field, uncertainty, and signoff details.

After that, run:

```bash
python scripts/init_pilot_workspace.py --ack-controlled-details
python scripts/check_pilot_preflight.py --before-item-1 --ack-controlled-details
```

Then rehearse 1-2 real controlled records locally before any 10-15 item checkpoint.

Do not use this synthetic rehearsal to justify completing 50 items, expanding to 100-200, or making any Phase 2 decision.

## Commit Boundary

Commit this aggregate note and any docs that describe the rehearsal.

Do not commit generated local outputs if they contain item-level evidence in future real runs. For this synthetic run, outputs still remain ignored because the same paths will be used for local real-output patterns later.
