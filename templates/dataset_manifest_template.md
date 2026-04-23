# Dataset Manifest

## Identity

- Dataset ID:
- Dataset version:
- Created date:
- Owner:
- Schema version: `thread_item_schema_v1`
- Annotation guideline version: `docs/06-annotation-guideline-v1.md`
- Labeling schema version: `labeling_schema_v1`

## Authorization

- Authorization basis:
- Data owner/source owner:
- Approval reference:
- Collection method:
- Retention rule:
- Sharing/publication restriction:

## Scope

- Platform: Threads
- Source types:
- Batch ID:
- Item count:
- Date range:
- Included content forms:
- Excluded content forms:

## Composition

| Label bucket | Count | Notes |
|---|---:|---|
| `scam` |  |  |
| `non_scam` |  |  |
| `uncertain` |  |  |
| `insufficient_evidence` |  |  |

## Evidence Fields Available

Mark each field as complete, partial, sparse, unavailable, or not applicable.

| Field | Status | Notes |
|---|---|---|
| `post_text` |  |  |
| `reply_texts` |  |  |
| `image_paths` |  |  |
| `ocr_text` |  |  |
| `external_links` |  |  |
| `visible_contact_handles` |  |  |
| `visible_platform_redirects` |  |  |
| `source_url_if_stored` |  |  |
| `screenshot_snapshot_status` |  |  |
| `link_snapshot_status` |  |  |

## Quality Notes

- Known biases:
- Source skew:
- Content-form skew:
- Duplicate handling:
- Redaction status:
- Annotation disagreement summary:
- Major missing evidence:

## Allowed Uses

- Human annotation QA:
- Dataset audit:
- Rule baseline:
- OCR/reply/link ablation:
- Publication/demo use:

## Disallowed Uses

- Automated collection:
- Production scoring:
- Legal determination:
- Public release of raw evidence:
- Any use outside approved governance scope:

## Baseline Readiness

- Ready for binary baseline:
- Ready for risk-triage baseline:
- Items excluded from baseline and why:
- Next revision needed:
