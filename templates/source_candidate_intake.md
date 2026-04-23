# Source Candidate Intake

## Candidate Identity

| Field | Value |
|---|---|
| Source candidate ID |  |
| Date opened |  |
| Intake owner |  |
| Proposed source owner |  |
| Proposed use | planning / calibration / 50-item pilot / 100-200 expansion / 500 expansion |

Do not put sensitive source names, handles, URLs, or case IDs in this file unless the storage location is approved.

## Source Description

| Field | Value |
|---|---|
| Source type | `stakeholder_provided_case` / `manual_public_example` / `manual_public_comparator` / `stakeholder_summary_only` / `api_authorized_sample` / `researcher_synthetic` / other |
| Platform | Threads |
| Proposed collection method |  |
| Expected item count |  |
| Expected date range |  |
| Expected content forms | text / image / replies / OCR / links / handles / redirects / screenshots |
| Expected label buckets | likely scam / likely non-scam / uncertain / insufficient evidence |

## Authorization And Limits

| Question | Answer |
|---|---|
| Is source sharing approved? |  |
| Is manual collection approved? |  |
| Is API access approved? |  |
| Are screenshots approved? |  |
| Are source URLs approved? |  |
| Are visible links approved? |  |
| Are visible contact handles approved? |  |
| Is OCR approved? |  |
| Is raw storage outside git defined? |  |
| Is retention defined? |  |
| Is access defined? |  |

If any authorization answer is unclear, the source is not ready for real collection.

## Fields Requested

Mark each as `needed`, `optional`, `not_needed`, or `not_allowed`.

| Field | Status | Notes |
|---|---|---|
| `post_text` |  |  |
| `reply_texts` |  |  |
| `image_paths` / screenshot reference |  |  |
| `ocr_text` |  |  |
| `external_links` |  |  |
| `visible_contact_handles` |  |  |
| `visible_platform_redirects` |  |  |
| `source_url_if_stored` |  |  |
| `metadata_notes` |  |  |
| `privacy_redaction_notes` |  |  |

## Source Scoring

Use `green`, `yellow`, or `red`.

| Dimension | Rating | Notes |
|---|---|---|
| authorization clarity |  |  |
| privacy exposure |  |  |
| redaction burden |  |  |
| evidence quality |  |  |
| content-form coverage |  |  |
| label-bucket value |  |  |
| operational burden |  |  |
| source skew risk |  |  |

## Suitability Decision

Choose one:

- `reject`
- `planning_only`
- `calibration_only`
- `candidate_for_50_item_pilot`
- `candidate_for_100_200_expansion`
- `candidate_for_500_expansion`

Decision:

```text

```

Rationale:

```text

```

## Required Follow-Up

| Follow-up | Owner | Due date |
|---|---|---|
|  |  |  |

