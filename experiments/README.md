# Experiments

Experiments must be narrow, documented, and decision-oriented.

Use:

- `baselines/` for keyword and rule baseline logs.
- `modality-studies/` for text versus OCR, comments, image text, and link-signal comparisons.
- `evaluation-notes/` for error analysis, reviewer burden studies, and metric summaries.

Current dry-run artifacts:

- `dataset-audit/0002-synthetic-sample-audit-dry-run.md`
- `baselines/0002-synthetic-rule-baseline-dry-run.md`

Current v2 routing-learning artifacts:

- `batch_variants/0006-contrast-aware-routing-validation.md`
- `batch_variants/0006-post-review-routing-result.md`
- `batch_variants/0007-result-display-context-split.md`
- `evaluation-notes/0102-v2-batch-0006-routing-validation-result.md`

Each experiment must state:

- Hypothesis
- Dataset slice
- Method
- Cost
- Result
- Failure modes
- Decision implication

Do not add code-heavy experiments until the taxonomy, schema, annotation guide, and first sample are stable enough to support comparison.
