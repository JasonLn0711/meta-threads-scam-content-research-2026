# Evaluation Note 0003: Pilot Decision Analysis Protocol

## Purpose

Use this protocol after the authorized 50-item pilot is annotated, audited, adjudicated, and run through baseline variants.

The output is a decision memo: expand to 100-200 items, revise the guideline, revise the schema, narrow sources, or pause.

## Inputs

- `templates/pilot_result_summary.md`
- `templates/pilot_decision_memo.md`
- `templates/baseline_error_review_table.csv`
- `templates/guideline_revision_log_template.md`
- `docs/33-pilot-analysis-and-decision-framework.md`
- local-only audit, agreement, adjudication, and baseline outputs under `data/processed/`

## Method

1. Confirm governance and privacy compliance.
2. Summarize dataset composition and source/content-form skew.
3. Summarize annotation agreement and adjudication themes.
4. Review uncertain and insufficient-evidence rates.
5. Compare baseline variants: `text_only`, `text_reply`, `text_ocr`, and `all`.
6. Fill the error review table for representative false positives and false negatives.
7. Identify whether OCR, replies, links, handles, or redirects changed decisions.
8. Assess reviewer burden and confusing fields.
9. Fill `templates/pilot_decision_memo.md`.
10. Record the final decision in `decision-log/`.

## Required Decision Logic

Pause if:

- governance or privacy rules were violated
- raw evidence entered tracked files
- required fields are missing or validation errors remain

Revise before expansion if:

- repeated disagreements show unclear label boundaries
- `uncertain` is above 30 percent without a clear research reason
- `insufficient_evidence` is above 20 percent without a collection fix
- false positives are dominated by legitimate content categories
- reviewers cannot manage the annotation burden

Expand to 100-200 if:

- governance and redaction held
- labels are usable after adjudication
- evidence fields are sufficiently complete
- baseline variants are interpretable
- the next research question is about breadth rather than fixing the workflow

## Output

Commit only non-sensitive aggregate notes:

- pilot decision memo
- summary of error themes
- guideline/schema revision recommendations
- decision-log entry

Do not commit raw annotation files, raw screenshots, source URLs, personal data, or sensitive stakeholder material.

