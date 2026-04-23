# Dataset Schema

## Purpose

The first dataset version is organized around one unit: a `thread_item`. A `thread_item` preserves enough evidence for manual collection, human annotation, first baselines, future OCR augmentation, review workflow, and evidence audit without becoming a production platform model.

The authoritative machine-readable contract is:

```text
data-contracts/thread_item_schema_v1.json
```

The annotation vocabulary is:

```text
data-contracts/labeling_schema_v1.json
```

## Thread Item Definition

A `thread_item` may be a top-level post, reply/comment, text-only post, text plus image post, screenshot-style image post, or a collected post context that includes replies, OCR text, visible links, contact handles, and redirection signals.

The schema intentionally centers the content item rather than accounts, profiles, campaigns, or platform enforcement actions. Phase 1 is about evidence design and human triage, not actor attribution.

## Flat Field Contract

| Field | Type | Required | Purpose |
|---|---|---:|---|
| `item_id` | string | Yes | Stable internal ID with no personal data. |
| `schema_version` | string | Yes | Must be `thread_item_schema_v1`. |
| `source_platform` | enum | Yes | Phase-1 value is `threads`. |
| `source_type` | enum | Yes | `stakeholder_provided`, `manual_public`, `api_authorized`, `synthetic_redacted`, `researcher_synthetic`, or `other_approved`. |
| `collection_batch_id` | string | Yes | Batch ID such as `threads_pilot_v1_2026-05`. |
| `collection_timestamp` | datetime | Yes | ISO 8601 timestamp. |
| `collection_method` | enum | Yes | `stakeholder_provided`, `manual_capture`, `api_authorized`, `synthetic`, or `other`. |
| `authorization_status` | enum | Yes | `approved`, `pending`, `synthetic_only`, or `rejected`. |
| `post_text` | string | Yes | Captured or redacted post text; empty string if absent. |
| `reply_texts` | array[string] | Yes | Relevant replies/comments; empty array if absent. |
| `image_paths` | array[string] | Yes | Redacted image references or local placeholders. |
| `image_count` | integer | Yes | Number of images represented or known. |
| `has_image` | boolean | Yes | Whether image evidence exists. |
| `has_reply` | boolean | Yes | Whether reply/comment evidence exists. |
| `has_external_link` | boolean | Yes | Whether visible external link evidence exists. |
| `external_links` | array[string] | Yes | Visible, normalized, or redacted external links. |
| `visible_contact_handles` | array[string] | Yes | Visible contact handles or redacted handle evidence. |
| `visible_platform_redirects` | array[enum] | Yes | LINE, WhatsApp, Telegram, private group, external site, or `none`. |
| `ocr_text` | string | Yes | OCR text from image/screenshot evidence; empty string if absent. |
| `language` | string | Yes | Primary language code such as `en`, `zh-TW`, `mixed`, or `und`. |
| `screenshot_style` | enum | Yes | `none`, `screenshot_style`, `screenshot_heavy`, or `unknown`. |
| `scam_label` | enum | Yes | `scam`, `non_scam`, `uncertain`, or `insufficient_evidence`. |
| `scam_type` | array[enum] | Yes | One or more v1 subtypes, or `none`. |
| `risk_level` | enum | Yes | `high`, `medium`, or `low`. |
| `signal_tags` | array[enum] | Yes | Observable reason/signal tags, or `none`. |
| `evidence_sufficiency` | enum | Yes | `sufficient`, `partial`, `insufficient`, or `not_reviewable`. |
| `annotation_confidence` | enum | Yes | `high`, `medium`, or `low`. |
| `annotation_notes` | string | No | Short evidence-based note. |
| `annotator_id` | string | No | Pseudonymous first annotator. |
| `reviewer_id` | string | No | Pseudonymous second reviewer/adjudicator. |
| `review_status` | enum | Yes | `new`, `annotated`, `needs_second_review`, `adjudicated`, or `excluded`. |
| `adjudication_status` | enum | Yes | `not_needed`, `pending`, or `resolved`. |
| `disagreement_flag` | boolean | Yes | Whether annotators disagreed on label/risk/subtype. |
| `final_label` | enum/string | No | Final adjudicated label or blank until resolved. |
| `final_risk_level` | enum/string | No | Final adjudicated risk or blank until resolved. |
| `source_url_if_stored` | string | No | Store only if approved; otherwise blank or redacted reference. |
| `screenshot_snapshot_status` | enum | Yes | `not_applicable`, `not_captured`, `captured_redacted`, `captured_full_approved`, or `unavailable`. |
| `link_snapshot_status` | enum | Yes | Same status vocabulary for link/destination evidence. |
| `metadata_notes` | string | No | Non-sensitive notes about missing or available metadata. |
| `privacy_redaction_notes` | string | No | What personal/sensitive content was removed. |
| `dedupe_key` | string | No | Internal duplicate review key. |
| `near_duplicate_group_id` | string | No | Cluster ID for repeated text/OCR/link/handle/screenshot patterns. |
| `missing_evidence` | array[enum] | No | Missing evidence that would improve review. |
| `baseline_split` | enum | No | `unassigned`, `train`, `validation`, `test`, `audit_holdout`, or `excluded`. |

## CSV-Friendly Version

The CSV version is for first-pass manual annotation in a spreadsheet. Arrays should be pipe-separated. Empty arrays should be blank or `none` depending on the field.

```csv
item_id,schema_version,source_platform,source_type,collection_batch_id,collection_timestamp,collection_method,authorization_status,post_text,reply_texts,image_paths,image_count,has_image,has_reply,has_external_link,external_links,visible_contact_handles,visible_platform_redirects,ocr_text,language,screenshot_style,scam_label,scam_type,risk_level,signal_tags,evidence_sufficiency,annotation_confidence,annotation_notes,annotator_id,reviewer_id,review_status,adjudication_status,disagreement_flag,final_label,final_risk_level,source_url_if_stored,screenshot_snapshot_status,link_snapshot_status,metadata_notes,privacy_redaction_notes,dedupe_key,near_duplicate_group_id,missing_evidence,baseline_split
```

Example pipe-separated values:

```text
private_channel_redirect|visible_external_link|testimonial_or_earnings_screenshot
```

CSV advantages:

- fast for manual collection and annotation
- easy for small teams to review
- simple import into spreadsheets
- good for the 50-item pilot

CSV limitations:

- arrays and nested evidence are lossy
- quoting and line breaks need discipline
- duplicate clusters and review lifecycle can become awkward
- flat text fields can encourage over-storing sensitive evidence

## JSON-Friendly Nested Version

The JSON schema is flat for easy validation and CSV parity, but pipeline code may transform records into this nested shape for readability:

```json
{
  "identity": {
    "item_id": "threads-v1-0001",
    "schema_version": "thread_item_schema_v1",
    "source_platform": "threads",
    "collection_batch_id": "threads_pilot_v1_2026-05"
  },
  "provenance": {
    "source_type": "manual_public",
    "collection_timestamp": "2026-05-01T10:00:00+08:00",
    "collection_method": "manual_capture",
    "authorization_status": "pending",
    "source_url_if_stored": "",
    "screenshot_snapshot_status": "captured_redacted",
    "link_snapshot_status": "not_captured"
  },
  "content": {
    "post_text": "Redacted example post text.",
    "reply_texts": ["Redacted example reply."],
    "image_paths": ["data/samples/redacted-placeholder-0001.png"],
    "image_count": 1,
    "has_image": true,
    "has_reply": true,
    "has_external_link": false,
    "external_links": [],
    "visible_contact_handles": ["telegram:[redacted]"],
    "visible_platform_redirects": ["telegram"],
    "ocr_text": "Example OCR text",
    "language": "en",
    "screenshot_style": "screenshot_style"
  },
  "annotation": {
    "scam_label": "scam",
    "scam_type": ["guaranteed_profit_claim", "redirect_to_private_chat"],
    "risk_level": "high",
    "signal_tags": ["guaranteed_or_risk_free_claim", "private_channel_redirect"],
    "evidence_sufficiency": "sufficient",
    "annotation_confidence": "high",
    "annotation_notes": "OCR shows guarantee and visible private-channel redirect."
  },
  "review": {
    "annotator_id": "ann_01",
    "reviewer_id": "",
    "review_status": "annotated",
    "adjudication_status": "not_needed",
    "disagreement_flag": false,
    "final_label": "",
    "final_risk_level": ""
  },
  "derived": {
    "dedupe_key": "synthetic:guarantee-telegram",
    "near_duplicate_group_id": "",
    "missing_evidence": ["link_snapshot_missing"],
    "baseline_split": "unassigned"
  }
}
```

JSON advantages:

- preserves evidence groups cleanly
- easier for OCR, baseline, audit, and review-packet scripts
- reduces confusion between source evidence, annotation, and adjudication
- better for future JSONL datasets

JSON limitations:

- less convenient for first-pass spreadsheet annotation
- requires transformation before manual review
- nested structures are harder to inspect quickly without tooling

## Practical Tradeoff

Use CSV for the first annotation sheet and JSON/JSONL for durable dataset exports. The JSON schema remains authoritative; the CSV template is a manual-entry view of the same fields.

For the 50-item pilot, keep one spreadsheet-style annotation file and one JSONL export generated from it after review. Do not manually maintain two independent versions.

## Baseline-Ready Slice

The first baseline-ready slice should include items where:

- `scam_label` is `scam` or `non_scam`
- `annotation_confidence` is `high` or the item has `review_status` of `adjudicated`
- `post_text` or `ocr_text` is nonempty
- `evidence_sufficiency` is `sufficient` or `partial`
- `baseline_split` is not `excluded`

Keep `uncertain` and `insufficient_evidence` records in the dataset, but report them separately from binary precision/recall metrics.
