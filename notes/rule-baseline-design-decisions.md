# Rule Baseline Design Decisions

## Decisions

- Build the baseline as modular Python under `src/baselines/` instead of keeping all scoring logic in one script.
- Keep `scripts/rule_baseline_v1.py` as a compatibility wrapper for existing experiment docs.
- Put tunable weights, thresholds, bonuses, and subtype hints in `configs/baseline_rule_config.yaml`.
- Use conservative scoring: weak single signals can contribute evidence but cannot trigger high risk alone.
- Preserve stable, visible reason codes for reviewer worksheets and future triage packets.
- Keep synthetic samples clearly marked as `researcher_synthetic` and `synthetic_only`.
- Add a calibration workbench before real threshold tuning so changes are made from false-positive and false-negative review, not intuition.

## Rationale

The first trusted system should be explainable before it is clever. Rules are useful because reviewers can challenge them, identify missing evidence, and tune them after the first annotation batch.

## Non-Claims

This baseline does not prove scam intent, legal fraud, policy violation, or platform-scale detection capability. It is a research baseline for triage, scope learning, and evidence design.

## First Tuning Preference

Tune for high-risk precision first. False positives against legitimate finance, recruitment, health, creator, or promotional content are a serious research risk.

Use `precision_first` as the first alternative if the pilot high-risk queue feels noisy. Use `recall_probe` only to inspect missed cases.
