# Pilot Batch Work Order: Threads Pilot v1

## Batch Identity

| Field | Value |
|---|---|
| Work order ID | `PWO-THREADS-PILOT-V1-2026-05` |
| Date opened | `2026-04-23` |
| Project owner | project owner |
| Collection batch ID | `threads_pilot_v1_2026-05` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Authorization request ID | `DREQ-THREADS-PILOT-V1-2026-04-23` |
| Stakeholder authorization ID | `AUTH-THREADS-PILOT-V1-2026-04-23` |
| Go/no-go decision | `go_with_limits` |

## Authorization Summary

| Question | Answer |
|---|---|
| Approved source type | stakeholder-provided cases and/or manually identified public examples under pilot limits |
| Approved collection method | manual, stakeholder-provided, API-authorized, and automation-assisted under controlled launch record |
| Approved sample size | 50 |
| Approved collection window | after readiness sign-off through `2026-05-31`, unless stakeholder limits specify otherwise |
| Raw storage location outside git | approved controlled location outside git; exact path not recorded here |
| Retention rule | pilot-only retention; review after pilot decision memo |
| Access list | role-limited access; exact names outside git if sensitive |
| Publication/demo restrictions | internal aggregate metrics only; no external examples without later approval |
| Controlled launch details | exact source, storage, access, retention, and redaction limits required before first item |

## Approved Fields

| Field | Status | Notes |
|---|---|---|
| `post_text` | approved_redacted | Remove unnecessary personal data. |
| `reply_texts` | approved_redacted | Selected relevant replies/comments only. |
| `image_paths` / screenshot reference | approved_redacted | Redacted references only; raw screenshots outside git. |
| `ocr_text` | approved_redacted | Risk-relevant OCR after privacy review. |
| `external_links` | approved_redacted | Normalized or redacted visible-link references only. |
| `visible_contact_handles` | approved_redacted | Category or redacted handle only. |
| `visible_platform_redirects` | approved | Platform/category labels allowed. |
| `source_url_if_stored` | approved_redacted | Redacted reference only in repo-visible files. |
| `screenshot_snapshot_status` | approved | Status only in annotation sheet. |
| `link_snapshot_status` | approved | Status should usually be `not_captured` or `not_applicable`. |
| `metadata_notes` | approved_redacted | Non-sensitive notes only. |
| `privacy_redaction_notes` | approved | Required when redaction occurs. |

## Target Composition

| Bucket | Target count | Actual count | Notes |
|---|---:|---:|---|
| likely scam or high-risk scam-like | 15 | 0 | positive-risk diagnostic bucket |
| likely non-scam comparator | 15 | 0 | false-positive calibration bucket |
| uncertain or ambiguous | 10 | 0 | guideline stress-test bucket |
| insufficient-evidence or low-context | 10 | 0 | evidence sufficiency bucket |
| total | 50 | 0 | not a prevalence estimate |

## Content-Form Targets

| Content form | Target | Actual | Notes |
|---|---:|---:|---|
| text-only | 10-15 | 0 | include benign and suspicious text-only cases |
| text plus image | 10-15 | 0 | use redacted screenshot references only |
| reply/comment context | 10-15 | 0 | selected relevant replies only |
| OCR-heavy image or screenshot | 5-10 | 0 | only if OCR privacy review passes |
| visible link or redirection signal | 10-15 | 0 | visible, API, redirect, or landing evidence allowed only under run records and redaction controls |

## Assigned Roles

| Role | Assigned ID | Name or team, if allowed | Notes |
|---|---|---|---|
| Project owner | `owner_01` | held outside git if sensitive | final pilot decision owner |
| Governance reviewer | `gov_01` | held outside git if sensitive | confirms storage, access, retention, redaction |
| Collector | `collector_01` | held outside git if sensitive | manual and stakeholder-provided collection |
| Automation operator | `auto_op_01` | held outside git if sensitive | API and automation runs under controlled launch record |
| Annotator 1 | `ann_01` | held outside git if sensitive | first-pass annotation |
| Annotator 2 or reviewer | `rev_01` | held outside git if sensitive | second review |
| Adjudicator | `adj_01` | held outside git if sensitive | final label decisions |
| Research engineer | `eng_01` | held outside git if sensitive | validation, audit, conversion, baseline |

## Local-Only Working Files

| File | Owner | Status |
|---|---|---|
| `data/interim/threads_pilot_v1_collection_log.csv` | `collector_01` | create locally after storage/access confirmation |
| `data/interim/threads_pilot_v1_annotations.csv` | `ann_01` | create locally after collection fields are ready |
| `data/processed/threads_pilot_v1.jsonl` | `eng_01` | generate locally after validation |
| `data/processed/threads_pilot_v1_audit.md` | `eng_01` | generate locally after JSONL conversion |
| `data/processed/threads_pilot_v1_rule_variant_comparison.md` | `eng_01` | generate locally after adjudication |
| `data/processed/threads_pilot_v1_agreement.md` | `eng_01` | generate locally after two-pass review |
| `data/processed/threads_pilot_v1_disagreements.csv` | `eng_01` | generate locally after comparison |

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

| Stop condition | Clear? | Notes |
|---|---|---|
| Authorization unclear | yes | Approval recorded, but conditions must stay visible. |
| Raw personal data entering git | yes | Stop immediately if this occurs. |
| Screenshot/link policy unclear | yes | Redacted repo-visible fields; raw and expanded link evidence outside git only. |
| Collector needs unapproved fields | yes | Stop and revise authorization. |
| Annotators need unapproved context | yes | Stop and revise scope. |
| Collection or automation exceeds run record | yes | Stop immediately and revise governance. |
| Redaction cannot be completed safely | yes | Exclude item or pause. |

## Work Order Decision

- Decision: `ready_to_collect`
- Decision owner: project owner
- Decision date: `2026-04-23`
- Limits or conditions:
  - Ready to collect only after exact raw storage location and access list are confirmed outside git.
  - Exact source, storage, access, retention, and redaction limits must be written into the controlled launch record before collection.
  - Collection may use manual, stakeholder-provided, API-authorized, or automation-assisted paths under the controlled launch record and remains limited to 50 items before checkpoint and decision review.
  - Commit only aggregate, non-sensitive notes and decision records.
- Next review date: after first 10-15 collected or annotated rows, whichever comes first.
