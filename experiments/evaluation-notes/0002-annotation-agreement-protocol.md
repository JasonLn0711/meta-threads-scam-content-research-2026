# Annotation Agreement Protocol

## Purpose

Measure whether annotators can apply the v1 guideline consistently enough to start the 50-item pilot.

## Inputs

- Two independent annotation files with the same `item_id` values.
- The v1 schema and annotation guideline.
- No raw screenshots or sensitive evidence in tracked files.

## Command

Prepare two blind annotator copies:

```bash
python scripts/prepare_calibration_files.py data/samples/thread_item_sample_batch.csv \
  --blind-output data/interim/calibration_blind.csv \
  --answer-key-output data/processed/calibration_answer_key.csv \
  --annotator-copy ann_01:data/interim/calibration_ann_01.csv \
  --annotator-copy ann_02:data/interim/calibration_ann_02.csv
```

After annotators complete their files:

```bash
python scripts/compare_annotation_passes.py \
  data/interim/calibration_ann_01.csv \
  data/interim/calibration_ann_02.csv \
  --name-a ann_01 \
  --name-b ann_02 \
  --output data/processed/calibration_agreement.md \
  --disagreements-csv data/processed/calibration_disagreements.csv
```

## Metrics To Review

- `scam_label` exact agreement and kappa
- `risk_level` exact agreement and kappa
- `evidence_sufficiency` exact agreement and kappa
- `scam_type` exact agreement and mean Jaccard
- `signal_tags` exact agreement and mean Jaccard
- item-level disagreement count

## Readiness Guidance

Proceed to the 50-item pilot when:

- primary label agreement is at least about 0.80 on the calibration set
- risk-level disagreements can be adjudicated with existing guidance
- subtype and signal-tag disagreements reveal small wording fixes rather than taxonomy failure

Pause and revise when:

- annotators repeatedly split between `scam` and `uncertain`
- `insufficient_evidence` is used as a substitute for low confidence
- finance, recruitment, giveaway, celebrity, or screenshot-only cases drive repeated disagreement
- annotators select many more tags than the evidence supports

## Output

Record:

- agreement report path
- disagreement CSV path
- adjudication notes
- guideline changes needed
- decision: proceed, recalibrate, revise guideline, or revise schema
