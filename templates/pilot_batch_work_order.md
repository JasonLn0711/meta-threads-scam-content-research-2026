# Pilot Batch Work Order

## Batch Identity

| Field | Value |
|---|---|
| Work order ID |  |
| Date opened |  |
| Project owner |  |
| Collection batch ID |  |
| Dataset ID |  |
| Authorization request ID |  |
| Go/no-go decision | `go` / `go_with_limits` / `no_go` / `pending` |

## Authorization Summary

| Question | Answer |
|---|---|
| Approved source type |  |
| Approved collection method |  |
| Approved sample size |  |
| Approved collection window |  |
| Raw storage location outside git |  |
| Retention rule |  |
| Access list |  |
| Publication/demo restrictions |  |

## Approved Fields

Mark each field as `approved`, `approved_redacted`, `not_approved`, or `not_needed`.

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
| `screenshot_snapshot_status` |  |  |
| `link_snapshot_status` |  |  |
| `metadata_notes` |  |  |
| `privacy_redaction_notes` |  |  |

## Target Composition

| Bucket | Target count | Actual count | Notes |
|---|---:|---:|---|
| likely scam or high-risk scam-like | 15 |  |  |
| likely non-scam comparator | 15 |  |  |
| uncertain or ambiguous | 10 |  |  |
| insufficient-evidence or low-context | 10 |  |  |
| total | 50 |  |  |

## Content-Form Targets

| Content form | Target | Actual | Notes |
|---|---:|---:|---|
| text-only |  |  |  |
| text plus image |  |  |  |
| reply/comment context |  |  |  |
| OCR-heavy image or screenshot |  |  |  |
| visible link or redirection signal |  |  |  |

## Assigned Roles

| Role | Assigned ID | Name or team, if allowed | Notes |
|---|---|---|---|
| Project owner |  |  |  |
| Governance reviewer |  |  |  |
| Collector |  |  |  |
| Annotator 1 |  |  |  |
| Annotator 2 or reviewer |  |  |  |
| Adjudicator |  |  |  |
| Research engineer |  |  |  |

## Local-Only Working Files

| File | Owner | Status |
|---|---|---|
| `data/interim/threads_pilot_v1_collection_log.csv` |  |  |
| `data/interim/threads_pilot_v1_annotations.csv` |  |  |
| `data/processed/threads_pilot_v1.jsonl` |  |  |
| `data/processed/threads_pilot_v1_audit.md` |  |  |
| `data/processed/threads_pilot_v1_rule_variant_comparison.md` |  |  |
| `data/processed/threads_pilot_v1_agreement.md` |  |  |
| `data/processed/threads_pilot_v1_disagreements.csv` |  |  |

## Required Commands

```bash
python scripts/validate_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv --strict
python scripts/convert_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv \
  data/processed/threads_pilot_v1.jsonl \
  --validate
python scripts/audit_thread_dataset.py data/processed/threads_pilot_v1.jsonl \
  > data/processed/threads_pilot_v1_audit.md
python scripts/compare_rule_variants.py data/processed/threads_pilot_v1.jsonl \
  --output data/processed/threads_pilot_v1_rule_variant_comparison.md
```

## Stop Conditions

Check each before and during collection:

| Stop condition | Clear? | Notes |
|---|---|---|
| Authorization unclear |  |  |
| Raw personal data entering git |  |  |
| Screenshot/link policy unclear |  |  |
| Collector needs unapproved fields |  |  |
| Annotators need unapproved context |  |  |
| Collection drifting toward automation |  |  |
| Redaction cannot be completed safely |  |  |

## Work Order Decision

- Decision: `open` / `ready_to_collect` / `paused` / `closed`
- Decision owner:
- Decision date:
- Limits or conditions:
- Next review date:

