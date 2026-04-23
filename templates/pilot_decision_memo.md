# Pilot Decision Memo

Use this template after the checkpoint-approved 50-item pilot is complete. Do not use it for the first 10-15 item checkpoint; use `templates/pilot_checkpoint_review.md` for that gate.

If `scripts/summarize_pilot_results.py` returns `first_checkpoint_review_required`, stop and complete the checkpoint review before preparing this memo.

## Memo Identity

| Field | Value |
|---|---|
| Memo ID |  |
| Date |  |
| Owner |  |
| Pilot dataset ID |  |
| Collection batch ID |  |
| Authorization reference |  |
| Memo stage | post_50_pilot |
| Decision requested | `expand_to_100_200` / `revise_guideline_first` / `revise_schema_first` / `narrow_sources` / `pause` |

## Executive Decision

Decision:

```text

```

One-paragraph rationale:

```text

```

## Inputs Reviewed

| Input | Reviewed? | Notes |
|---|---|---|
| First 10-15 item checkpoint review |  | Must show `continue_to_50` or `continue_with_limits`. |
| Data authorization request |  |  |
| Pilot work order |  |  |
| Annotation QA checklist |  |  |
| Dataset audit summary |  |  |
| Agreement/adjudication summary |  |  |
| Rule baseline comparison |  |  |
| Error analysis |  |  |
| Pilot result summary |  |  |
| Guideline revision log |  |  |

## Governance And Privacy Outcome

| Check | Result | Notes |
|---|---|---|
| Approved source followed |  |  |
| Approved fields followed |  |  |
| Raw evidence stayed outside git |  |  |
| Redaction consistent |  |  |
| Access and retention rules followed |  |  |
| Incident or near miss |  |  |

Expansion is blocked if governance or privacy outcome is red.

## Dataset And Evidence Summary

| Measure | Result | Interpretation |
|---|---|---|
| Total items |  |  |
| `scam` |  |  |
| `non_scam` |  |  |
| `uncertain` |  |  |
| `insufficient_evidence` |  |  |
| Source skew |  |  |
| Content-form skew |  |  |
| Missing required fields |  |  |
| Duplicate clusters |  |  |

## Annotation Quality

| Measure | Result | Interpretation |
|---|---|---|
| Primary-label agreement |  |  |
| Risk-level agreement |  |  |
| Evidence-sufficiency agreement |  |  |
| Items routed to second review |  |  |
| Items adjudicated |  |  |
| Top disagreement cause |  |  |
| Guideline changes needed |  |  |

## Baseline Summary

| Variant | Binary items | Precision | Recall | F1 | Main lesson |
|---|---:|---:|---:|---:|---|
| `text_only` |  |  |  |  |  |
| `text_reply` |  |  |  |  |  |
| `text_ocr` |  |  |  |  |  |
| `all` |  |  |  |  |  |

## Error Themes

| Theme | Evidence | Decision implication |
|---|---|---|
| OCR changed interpretation |  |  |
| replies/comments changed interpretation |  |  |
| link/redirection changed interpretation |  |  |
| false positives on legitimate content |  |  |
| false negatives from missing signals |  |  |
| ambiguous evidence or missing context |  |  |

## Reviewer Burden

| Measure | Result | Notes |
|---|---|---|
| Average annotation time per item |  |  |
| Average review/adjudication time |  |  |
| Fields reviewers found confusing |  |  |
| Workload blocker? |  |  |

## Decision Rubric

| Dimension | Rating | Notes |
|---|---|---|
| Governance | green / yellow / red |  |
| Privacy/redaction | green / yellow / red |  |
| Schema completeness | green / yellow / red |  |
| Label quality | green / yellow / red |  |
| Evidence sufficiency | green / yellow / red |  |
| Source/content skew | green / yellow / red |  |
| Baseline usefulness | green / yellow / red |  |
| Reviewer burden | green / yellow / red |  |

## Required Revisions

| Revision | File or process | Owner | Due date |
|---|---|---|---|
|  |  |  |  |

## Final Recommendation

Choose one:

- `expand_to_100_200`
- `revise_guideline_first`
- `revise_schema_first`
- `narrow_sources`
- `pause`

Do not choose `expand_to_100_200` if the checkpoint was skipped, if fewer than 50 pilot items were reviewed, or if governance/privacy outcome is red.

Recommendation:

```text

```

## Next Review

- Next review date:
- Required artifact before next review:
- Decision owner:
