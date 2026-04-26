# Existing Ambiguous And Medium-Risk Second Review Work Order 0050

Do not add raw Threads content, screenshots, full item URLs, raw handles, stakeholder case IDs, credentials, cookies, tokens, browser profiles, HAR files, full HTML, exact raw storage paths, access-list details, stock names, stock codes, price values, or sensitive investigative notes to this file.

## Work Order Identity

| Field | Value |
|---|---|
| Work order ID | `REVIEW-THREADS-PILOT-V1-0076-AMBIGUOUS-MEDIUM` |
| Date | `2026-04-26` |
| Related decision | `0101-authorize-existing-ambiguous-medium-second-review` |
| Dataset | `manual_records_checkpoint_0076.jsonl` |
| Review queue | `data/interim/review_queue_checkpoint_0076_uncertain_insufficient_medium.csv` |
| Queue size | 35 records |
| Operator | `AUTO-OP-01` |
| Purpose | second-review existing ambiguous, insufficient, and medium-risk records |
| Raw output location | not applicable; existing redacted records only |
| Repo-visible raw output | no |

## Queue Definition

Include any existing checkpoint 0076 record where:

- `scam_label == uncertain`; or
- `scam_label == insufficient_evidence`; or
- `risk_level == medium`.

## Review Lanes

| Lane | Items | Review goal |
|---|---:|---|
| `uncertain` | 29 | Decide whether evidence supports `scam`, `non_scam`, or remains mixed. |
| `insufficient_evidence` | 6 | Decide whether evidence remains not reviewable or can move to `uncertain`/another label. |
| `medium` risk | 13 | Decide whether risk should move to `high`, `low`, or remain `medium`. |
| Deduplicated queue | 35 | One row per item needing review. |

## Review Rules

For each item:

1. Use existing redacted record fields first.
2. Do not use raw source URLs, handles, screenshots, private messages, or external browsing.
3. Do not infer legal fraud.
4. Prefer `uncertain` when signals are mixed but evidence exists.
5. Prefer `insufficient_evidence` when decisive context is missing or not reviewable.
6. Promote to `scam` / `high` only when the existing evidence shows a review-worthy scam-like funnel or strong risk pattern.
7. Downgrade to `non_scam` / `low` only when the evidence is benign, warning/education, duplicate/excluded, or lacks scam-like persuasion.

## Output Fields

Each item-level review should record:

- item ID;
- prior label/risk;
- reviewer decision;
- final label/risk recommendation;
- evidence sufficiency recommendation;
- rule-family or signal rationale;
- whether controlled full-thread/reply capture is required;
- whether manual record rebuild is required.

## Current Status

Work order opened. No item-level adjudication has been recorded yet.
