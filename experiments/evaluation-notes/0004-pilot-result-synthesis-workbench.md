# Evaluation Note 0004: Pilot Result Synthesis Workbench

## Hypothesis

An aggregate-only synthesis workbench can turn pilot dataset counts and calibration artifacts into a decision memo draft without exposing raw evidence.

## Dataset Slice

Initial smoke test:

- `data/samples/rule_baseline_eval_sample.json`
- synthetic-only records
- calibration run: `experiments/baselines/outputs/synthetic-calibration-smoke`

Future pilot input:

- `data/interim/threads_pilot_v1_annotations.csv`
- local-only calibration output directory
- governance, privacy, and reviewer-burden ratings supplied by the project owner

## Method

```bash
python scripts/summarize_pilot_results.py data/samples/rule_baseline_eval_sample.json \
  --calibration-run-dir experiments/baselines/outputs/synthetic-calibration-smoke \
  --run-name synthetic-pilot-synthesis-smoke
```

## Outputs

- `pilot_synthesis_summary.json`
- `pilot_result_summary_draft.md`
- `pilot_decision_memo_draft.md`

## Decision Use

The draft recommendation is a structured starting point, not an automatic decision.

The project owner must review:

- governance/privacy ratings
- false positives
- false negatives
- uncertain and insufficient-evidence rates
- reviewer burden
- required guideline or schema revisions

## Commit Boundary

Commit only aggregate, non-sensitive synthesis notes. Do not commit local raw evidence, source URLs, personal data, screenshots, or unredacted annotations.
