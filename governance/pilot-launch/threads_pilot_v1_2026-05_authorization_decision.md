# Stakeholder Authorization Decision Record: Threads Pilot v1

This record captures the project-owner message that the stakeholder outcome is approved. It intentionally excludes raw Threads content, screenshots, source URLs, handles, case IDs, credentials, and sensitive investigative details.

Follow-up owner confirmation: the project owner also approved the repo's requirement that exact source, storage, access, retention, and redaction limits must be written into the launch record before collection begins. Sensitive values should be recorded in the approved controlled location rather than in git.

## Decision Identity

| Field | Value |
|---|---|
| Decision ID | `AUTH-THREADS-PILOT-V1-2026-04-23` |
| Decision date | `2026-04-23` |
| Meeting or thread reference | Project-owner approval message in this repo session |
| Request owner | project owner |
| Decision owner | project owner / stakeholder owner |
| Governance/privacy reviewer | governance reviewer role, exact name outside git if sensitive |
| Proposed dataset or batch ID | `threads_pilot_v1_2026-05` |
| Source candidate ID | `SRC-REAL-PILOT-APPROVED-2026-04-23` |

## Decision Outcome

| Field | Value |
|---|---|
| Outcome | `approved` |
| Approved sample size | 50 pilot items |
| Approved collection window | after readiness sign-off through `2026-05-31`, unless stakeholder limits specify otherwise |
| Approved source type | stakeholder-provided cases and/or manually identified public examples under pilot limits |
| Approved collection method | manual only |
| Automation approved? | no |
| Can real collection begin now? | yes only after go/no-go, work order, readiness review, and controlled raw-storage/access confirmation |

## Approved Fields

| Field | Decision | Limit or note |
|---|---|---|
| `post_text` | `approved_with_redaction` | Store only approved visible text; redact unnecessary personal data. |
| `reply_texts` | `approved_with_redaction` | Selected relevant replies/comments only. |
| `ocr_text` | `approved_with_redaction` | Risk-relevant OCR text after privacy review. |
| `image_paths` or screenshot references | `approved_with_limits` | Redacted local references only; no raw screenshots in git. |
| `external_links` | `approved_with_limits` | Normalized domain or redacted visible-link reference; no crawling. |
| `visible_contact_handles` | `approved_with_redaction` | Category or redacted handle only. |
| `visible_platform_redirects` | `approved` | Platform/category labels allowed. |
| `source_url_if_stored` | `approved_with_limits` | Redacted source reference only in repo-visible files. |
| screenshot snapshot | `approved_with_limits` | Redacted snapshots outside git only. |
| link snapshot | `denied` | Do not crawl, expand, or capture landing pages in this pilot. |
| limited metadata notes | `approved_with_redaction` | Non-sensitive metadata notes only. |

## Storage, Access, And Retention

| Question | Decision |
|---|---|
| Raw evidence storage location outside git | approved controlled location outside git; exact path not recorded here |
| Redacted annotation file location | local-only `data/interim/` and `data/processed/`, ignored by git |
| Raw evidence access list | project owner, governance reviewer, collector, assigned reviewers only |
| Annotation file access list | project owner, annotation team, research engineer |
| Raw evidence retention period | pilot-only retention; review after pilot decision memo |
| Redacted/derived file retention period | retain through pilot analysis and decision memo |
| Deletion owner | project owner or delegated governance reviewer |
| Redaction owner | collector with governance reviewer QA |
| Review before sharing required? | yes |

## Screenshot, URL, Link, And OCR Rules

| Evidence type | Approved handling |
|---|---|
| Screenshots | redacted only, outside git |
| Source URLs | redacted reference only in repo-visible files |
| Visible external links | normalized domain or redacted reference only |
| Contact handles | category only or redacted handle |
| OCR text | risk-relevant excerpt only after privacy review |
| Replies/comments | selected relevant only |

## Sharing And Reporting

| Output | Decision |
|---|---|
| Internal aggregate metrics | allowed |
| Internal redacted examples | allowed after review |
| External aggregate metrics | later review required |
| External redacted examples | later review required |
| Synthetic derivatives | allowed if non-evidence and clearly marked |
| Model-assisted review on approved samples | later review required |

## Conditions And Blockers

| Condition or blocker | Owner | Due date | Required before collection? |
|---|---|---|---|
| Exact raw evidence storage location must be confirmed outside git | project owner | before first item | yes |
| Exact raw evidence access list must be confirmed outside git | governance reviewer | before first item | yes |
| Exact source, retention, and redaction limits must be recorded in controlled launch details | project owner / governance reviewer | before first item | yes |
| Collector and annotator pseudonymous IDs must be assigned | project owner | before annotation | yes |
| Redaction checklist must be applied to every screenshot, OCR, URL, and handle field | collector | during collection | yes |

## Required Follow-Up

| Follow-up | Owner | Due date | Completion evidence |
|---|---|---|---|
| Update `governance/source-intake-register.md` | research engineer | `2026-04-23` | register row updated |
| Update `governance/pilot-authorization-register.md` | research engineer | `2026-04-23` | register row updated |
| Complete `docs/26-pilot-go-no-go-checklist.md` copy | research engineer | `2026-04-23` | launch packet record |
| Complete `templates/pilot_batch_work_order.md` copy | research engineer | `2026-04-23` | launch packet record |
| Complete `templates/real_pilot_readiness_review.md` copy | research engineer | `2026-04-23` | launch packet record |

## Decision Rationale

- The project owner reported the stakeholder outcome as approved.
- The project owner approved the requirement to record exact source, storage, access, retention, and redaction limits before collection.
- The pilot remains bounded to 50 items and manual/stakeholder-provided evidence only.
- The approval is recorded as usable only under privacy-minimized, redacted, non-automated conditions.
- No real Threads evidence is stored in this record.

## Sign-Off

| Role | Name or ID | Decision | Date | Notes |
|---|---|---|---|---|
| Project owner | project owner | approve | `2026-04-23` | Outcome reported approved. |
| Stakeholder owner | stakeholder owner | approve | `2026-04-23` | Exact identity not recorded in repo. |
| Governance/privacy reviewer | governance reviewer role | approve_with_conditions | `2026-04-23` | Conditions preserve privacy and storage limits. |
| Research lead | research lead | approve_with_conditions | `2026-04-23` | Proceed to 50-item pilot only. |
