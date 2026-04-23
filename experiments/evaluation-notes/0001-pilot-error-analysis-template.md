# Pilot Error Analysis Template

## Dataset

- Dataset ID:
- Dataset version:
- Schema version:
- Annotation guideline version:
- Baseline run:
- Date:
- Reviewer:

## Baseline Summary

| Variant | Precision | Recall | F1 | Notes |
|---|---:|---:|---:|---|
| `text_only` |  |  |  |  |
| `text_reply` |  |  |  |  |
| `text_ocr` |  |  |  |  |
| `all` |  |  |  |  |

## False Positives

| Item ID | Variant | Gold label | Predicted risk | Why flagged | Likely fix |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Common false-positive categories:

- legitimate finance discussion
- aggressive but legal marketing
- legitimate recruitment/job post
- legitimate giveaway or promotion
- celebrity/news/politics context
- link/contact info used benignly

## False Negatives

| Item ID | Variant | Gold label | Predicted risk | Missed signal | Likely fix |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Common false-negative categories:

- decisive claim appears only in OCR
- decisive lure appears only in replies
- redirection signal is phrased indirectly
- scam subtype lacks rule coverage
- evidence was incomplete or low quality

## Uncertain And Insufficient Evidence

- Number of `uncertain` items:
- Number of `insufficient_evidence` items:
- Most common missing evidence:
- Should the guideline change:
- Should collection practice change:

## Decision

Choose one:

- Continue to 100-200 item batch
- Revise annotation guide first
- Revise schema first
- Collect more hard negatives
- Narrow taxonomy
- Stop or defer this baseline branch

## Next Action

- Owner:
- Due date:
- Required file updates:
