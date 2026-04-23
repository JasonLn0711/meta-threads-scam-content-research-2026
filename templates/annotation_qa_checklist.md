# Annotation QA Checklist

## Batch Identity

| Field | Value |
|---|---|
| Dataset ID |  |
| Collection batch ID |  |
| QA date |  |
| QA owner |  |
| Annotation file |  |
| Authorization reference |  |

## Pre-Annotation QA

| Check | Status | Notes |
|---|---|---|
| Data authorization completed for real evidence |  |  |
| Raw evidence storage outside git confirmed |  |  |
| Approved fields match annotation sheet fields |  |  |
| Collection batch ID filled |  |  |
| Required identity/provenance fields filled |  |  |
| Redaction notes present where needed |  |  |
| Screenshot snapshot statuses filled |  |  |
| Link snapshot statuses filled |  |  |
| OCR text privacy-reviewed where present |  |  |
| `has_image` agrees with `image_count` |  |  |
| `has_external_link` agrees with `external_links` |  |  |
| Missing evidence recorded where needed |  |  |

## Calibration QA

| Check | Status | Notes |
|---|---|---|
| Annotators read the guideline |  |  |
| Annotators read onboarding quickstart |  |  |
| Blind calibration completed |  |  |
| Agreement report generated |  |  |
| Primary-label disagreements reviewed |  |  |
| `scam` versus `uncertain` boundary understood |  |  |
| `uncertain` versus `insufficient_evidence` boundary understood |  |  |
| Guideline revisions logged if needed |  |  |

## In-Pass QA

Run after the first 10-15 pilot items.

| Check | Status | Notes |
|---|---|---|
| No blank primary labels |  |  |
| No blank risk levels |  |  |
| No blank evidence sufficiency values |  |  |
| No blank annotation confidence values |  |  |
| `signal_tags` uses `none` when no signal applies |  |  |
| High-risk `scam` items routed to second review |  |  |
| `uncertain` items routed to second review |  |  |
| Low-confidence items routed to second review |  |  |
| Notes are evidence-based |  |  |
| Notes avoid legal conclusions |  |  |
| No raw personal data pasted into notes |  |  |

## Post-Annotation QA

| Check | Status | Notes |
|---|---|---|
| Validation passes with zero errors |  |  |
| Audit report generated |  |  |
| Disagreement report generated where applicable |  |  |
| Adjudication completed for required items |  |  |
| `final_label` filled only for adjudicated items |  |  |
| `uncertain` rate reviewed |  |  |
| `insufficient_evidence` rate reviewed |  |  |
| Source skew reviewed |  |  |
| Content-form skew reviewed |  |  |
| Duplicate clusters reviewed |  |  |
| Signal-tag drift reviewed |  |  |

## Baseline Readiness QA

| Check | Status | Notes |
|---|---|---|
| Binary metric inclusion rule applied |  |  |
| `uncertain` excluded from binary metrics |  |  |
| `insufficient_evidence` excluded from binary metrics |  |  |
| High-confidence or adjudicated labels used for binary metrics |  |  |
| `post_text` or `ocr_text` present for baseline items |  |  |
| Evidence sufficiency is `sufficient` or `partial` for baseline items |  |  |
| Rule variant comparison generated |  |  |
| Error analysis owner assigned |  |  |

## QA Decision

Choose one:

- `proceed_to_annotation`
- `pause_for_collection_fix`
- `pause_for_guideline_revision`
- `proceed_to_baseline`
- `revise_before_expansion`

Decision:

```text

```

Required follow-up:

| Follow-up | Owner | Due date |
|---|---|---|
|  |  |  |

