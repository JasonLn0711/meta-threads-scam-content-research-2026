# Pilot Result Summary

## Summary Identity

| Field | Value |
|---|---|
| Dataset ID |  |
| Collection batch ID |  |
| Summary date |  |
| Summary owner |  |
| Authorization reference |  |
| Schema version | `thread_item_schema_v1` |
| Annotation guideline | `docs/06-annotation-guideline-v1.md` |

## Governance Outcome

| Check | Result | Notes |
|---|---|---|
| Approved source followed |  |  |
| Approved fields followed |  |  |
| Raw evidence stayed outside git |  |  |
| Redaction completed |  |  |
| Retention/access restrictions followed |  |  |
| Any incident or near miss |  |  |

## Dataset Composition

| Label bucket | Count | Percentage | Notes |
|---|---:|---:|---|
| `scam` |  |  |  |
| `non_scam` |  |  |  |
| `uncertain` |  |  |  |
| `insufficient_evidence` |  |  |  |
| total |  |  |  |

## Content Forms

| Content form | Count | Notes |
|---|---:|---|
| text-only |  |  |
| text plus image |  |  |
| reply/comment context |  |  |
| OCR-heavy image or screenshot |  |  |
| visible link or redirection signal |  |  |

## Annotation Quality

| Measure | Result | Notes |
|---|---|---|
| Primary label agreement |  |  |
| Risk-level agreement |  |  |
| Evidence-sufficiency agreement |  |  |
| Items needing second review |  |  |
| Items adjudicated |  |  |
| Top disagreement cause |  |  |
| Guideline sections needing revision |  |  |

## Dataset Audit Findings

| Audit check | Result | Notes |
|---|---|---|
| Schema validation errors |  |  |
| Schema validation warnings |  |  |
| Missing required fields |  |  |
| Duplicate or near-duplicate clusters |  |  |
| Source skew |  |  |
| Content-form skew |  |  |
| Too many `uncertain` labels |  |  |
| Too many `insufficient_evidence` labels |  |  |
| Signal-tag drift |  |  |

## Baseline Results

| Variant | Binary items | Precision | Recall | F1 | High-risk predictions | Notes |
|---|---:|---:|---:|---:|---:|---|
| `text_only` |  |  |  |  |  |  |
| `text_reply` |  |  |  |  |  |  |
| `text_ocr` |  |  |  |  |  |  |
| `all` |  |  |  |  |  |  |

## Error Analysis Themes

| Theme | Example count | Implication |
|---|---:|---|
| OCR changed interpretation |  |  |
| replies/comments changed interpretation |  |  |
| link/redirect fields changed interpretation |  |  |
| false positives on legitimate content |  |  |
| false negatives from wording variation |  |  |
| evidence missing or not approved |  |  |

## Recommended Decision

Choose one:

- `expand_to_100_200`
- `revise_guideline_first`
- `revise_schema_first`
- `narrow_sources`
- `pause`

Rationale:

```text

```

## Required Follow-Up

| Follow-up | Owner | Due date | Notes |
|---|---|---|---|
|  |  |  |  |

