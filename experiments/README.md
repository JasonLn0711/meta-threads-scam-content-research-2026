# Experiments

Experiments must be narrow, documented, and decision-oriented.

Use:

- `baselines/` for keyword, rule, classifier, and LLM-assisted baseline logs.
- `modality-studies/` for text versus OCR, comments, image text, and link-signal comparisons.
- `evaluation-notes/` for error analysis, reviewer burden studies, and metric summaries.

Current dry-run artifacts:

- `dataset-audit/0002-synthetic-sample-audit-dry-run.md`
- `baselines/0002-synthetic-rule-baseline-dry-run.md`

Each experiment must state:

- Hypothesis
- Dataset slice
- Method
- Cost
- Result
- Failure modes
- Decision implication

Do not add code-heavy experiments until the taxonomy, schema, annotation guide, and first sample are stable enough to support comparison.
