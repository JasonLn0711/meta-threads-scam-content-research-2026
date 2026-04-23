# Experiment 0003: Rule Baseline Calibration Workbench

## Hypothesis

A calibration workbench that compares evidence variants and threshold profiles will make the first real pilot review safer and more useful than one-off script runs.

## Dataset Slice

Initial smoke test:

- `data/samples/rule_baseline_eval_sample.json`
- synthetic only
- 6 records
- no real Threads evidence

Future pilot use:

- `data/interim/threads_pilot_v1_annotations.csv`
- only after authorization and local workspace setup
- use high-confidence or adjudicated `scam`/`non_scam` records for binary metrics
- keep `uncertain` and `insufficient_evidence` in ambiguity review

## Method

Run:

```bash
python scripts/run_rule_calibration.py data/samples/rule_baseline_eval_sample.json \
  --run-name synthetic-calibration-smoke
```

The workbench compares:

- evidence variants: `text_only`, `text_reply`, `text_ocr`, `all`
- threshold profiles: `baseline`, `precision_first`, `recall_probe`, `redirect_strict`, `ocr_sensitive`

## Metrics

Report:

- precision, recall, F1
- false positives and false negatives
- triage exact agreement
- high/medium/low prediction counts
- changed decisions versus `baseline/text_only`

## Reviewer Artifact

Use `reviewer_worksheet.csv` to inspect:

- high-risk reason quality
- false-positive causes
- false-negative causes
- OCR-driven changes
- reply-driven changes
- threshold-sensitive medium-risk cases

## Decision

Use this workbench before changing default thresholds. The first tuning priority remains high-risk precision, not broad recall.
