# Contrast Scores

`latest.yaml` stores contrast-aware reviewer routing scores generated from
metadata-only candidate records.

This is not a classifier and not a legal or enforcement layer. It compares sparse
metadata lanes by value per reviewer effort so the next batch can prioritize
high-value source arms while routing context-cost candidates to slower review.

The current lanes are:

- `strong_source_priority`
- `guarantee_context_review`
- `result_display_context_review`
- `result_display_contrast_holdout`
- `other_metadata_review`
