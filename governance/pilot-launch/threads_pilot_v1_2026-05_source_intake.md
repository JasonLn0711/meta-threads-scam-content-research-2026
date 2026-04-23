# Source Candidate Intake: Threads Pilot v1

## Candidate Identity

| Field | Value |
|---|---|
| Source candidate ID | `SRC-REAL-PILOT-APPROVED-2026-04-23` |
| Date opened | `2026-04-23` |
| Intake owner | project owner |
| Proposed source owner | stakeholder-approved source owner, exact identity held outside git |
| Proposed use | 50-item pilot |

Do not add raw source names, handles, URLs, case IDs, or investigative details to this file.

## Source Description

| Field | Value |
|---|---|
| Source type | `stakeholder_provided_case` and/or `manual_public_example` under approval limits |
| Platform | Threads |
| Proposed collection method | manual collection only |
| Expected item count | 50 |
| Expected date range | from launch readiness sign-off through `2026-05-31`, unless stakeholder limits specify a shorter window |
| Expected content forms | text / image / replies / OCR / links / handles / redirects / screenshots where approved |
| Expected label buckets | likely scam / likely non-scam / uncertain / insufficient evidence |

## Authorization And Limits

| Question | Answer |
|---|---|
| Is source sharing approved? | approved for pilot under stakeholder authorization limits |
| Is manual collection approved? | yes |
| Is API access approved? | no |
| Are screenshots approved? | redacted snapshots only, outside git, unless controlled approval allows fuller retention |
| Are source URLs approved? | redacted reference or normalized domain only in repo-visible files |
| Are visible links approved? | normalized or redacted visible-link evidence only; no crawling |
| Are visible contact handles approved? | category or redacted handle only |
| Is OCR approved? | risk-relevant OCR text allowed after privacy review |
| Is raw storage outside git defined? | yes at controlled-location category level; exact path must remain outside git |
| Is retention defined? | pilot-only retention, review after pilot decision |
| Is access defined? | named roles only; exact names held outside git if sensitive |

## Fields Requested

| Field | Status | Notes |
|---|---|---|
| `post_text` | needed | Redact unnecessary personal data. |
| `reply_texts` | optional | Selected relevant replies only. |
| `image_paths` / screenshot reference | optional | Redacted local reference only; no raw screenshots in git. |
| `ocr_text` | optional | Risk-relevant OCR text after privacy review. |
| `external_links` | optional | Normalized or redacted visible-link references. |
| `visible_contact_handles` | optional | Category or redacted handle only. |
| `visible_platform_redirects` | needed | Use platform/category labels where possible. |
| `source_url_if_stored` | optional | Redacted reference only unless separately approved. |
| `metadata_notes` | needed | Non-sensitive notes only. |
| `privacy_redaction_notes` | needed | Required whenever redaction occurs. |

## Source Scoring

| Dimension | Rating | Notes |
|---|---|---|
| authorization clarity | yellow | Stakeholder outcome approved; exact sensitive details are intentionally outside git. |
| privacy exposure | yellow | Real user-facing content may include personal identifiers. |
| redaction burden | yellow | Screenshots, handles, OCR, and links require review. |
| evidence quality | green | Expected to support first pilot annotation. |
| content-form coverage | green | Covers text, images/OCR, replies, and link/redirection signals where approved. |
| label-bucket value | green | Sampling frame includes positive, comparator, uncertain, and low-context buckets. |
| operational burden | yellow | Manual collection and review only. |
| source skew risk | yellow | Pilot is diagnostic, not prevalence sampling. |

## Suitability Decision

Decision:

```text
candidate_for_50_item_pilot
```

Rationale:

```text
The project owner reports stakeholder approval. The source is suitable for a 50-item diagnostic pilot under manual-only, privacy-minimized, redacted, non-automated limits.
```

## Required Follow-Up

| Follow-up | Owner | Due date |
|---|---|---|
| Confirm exact raw evidence storage outside git in controlled location | project owner | before first real item |
| Confirm access list in controlled location | governance reviewer | before first real item |
| Confirm collector and annotator pseudonymous IDs | project owner | before annotation |
| Review first 10-15 pilot rows for redaction and label drift | annotation lead | during pilot |
