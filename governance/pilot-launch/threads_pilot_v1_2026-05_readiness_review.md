# Real Pilot Readiness Review: Threads Pilot v1

## Review Identity

| Field | Value |
|---|---|
| Review ID | `RPR-THREADS-PILOT-V1-2026-04-23` |
| Review date | `2026-04-23` |
| Project owner | `owner_01` |
| Governance reviewer | `gov_01` |
| Collection lead | `collector_01` |
| Annotation lead | `ann_01` / `rev_01` |
| Proposed collection batch ID | `threads_pilot_v1_2026-05` |
| Proposed source name or category | stakeholder-provided, manual public, API-authorized, and CIB-authorized automation-assisted examples under pilot limits |
| Proposed readiness decision | `ready_with_limits` |

## Evidence Bundle

| Required artifact | Completed? | Link or location | Notes |
|---|---|---|---|
| Source candidate intake | yes | `threads_pilot_v1_2026-05_source_intake.md` | Non-sensitive source category only. |
| Source sampling frame | yes | `threads_pilot_v1_2026-05_sampling_frame.csv` | Diagnostic 15/15/10/10 composition. |
| Stakeholder authorization decision record | yes | `threads_pilot_v1_2026-05_authorization_decision.md` | Approval recorded from project-owner message. |
| Data authorization request | yes | `threads_pilot_v1_2026-05_data_authorization.md` | Approved with privacy limits. |
| Source intake register entry | yes | `governance/source-intake-register.md` | Updated in repo. |
| Pilot authorization register entry | yes | `governance/pilot-authorization-register.md` | Updated in repo. |
| Go/no-go checklist | yes | `threads_pilot_v1_2026-05_go_no_go.md` | `go_with_limits`. |
| Pilot batch work order | yes | `threads_pilot_v1_2026-05_work_order.md` | `ready_to_collect` after local controlled setup. |
| Raw storage plan | limited | controlled location outside git | Exact path must remain outside git and be confirmed before first item. |
| Controlled launch details | limited | outside git controlled launch record | Owner approved requirement; exact source/storage/access/retention/redaction values required before first item. |
| Redaction checklist or rule | yes | `templates/redaction_checklist.md` | Apply before annotation/sharing. |
| Annotator onboarding checklist | scheduled | `templates/annotator_onboarding_checklist.md` | Complete before annotation starts. |
| Annotation QA checklist | yes | `templates/annotation_qa_checklist.md` | Use after first 10-15 rows. |
| Baseline/evaluation protocol | yes | `docs/08-baseline-strategy.md`; `docs/33-pilot-analysis-and-decision-framework.md` | Preserve uncertainty. |
| Mechanical preflight | pending before item 1 | `docs/40-pilot-preflight-verification.md`; `scripts/check_pilot_preflight.py` | Run after local workspace setup. |

## Gate Review

| Gate | Status | Blocker or limit | Owner | Evidence link |
|---|---|---|---|---|
| Governance and authorization | `ready_with_limits` | exact sensitive source details and raw path outside git | `owner_01` / `gov_01` | launch records |
| Source and sampling | `ready_with_limits` | diagnostic sample, not prevalence estimate | `owner_01` | sampling frame |
| Storage and redaction | `ready_with_limits` | raw evidence outside git; redaction required | `gov_01` / `collector_01` | data authorization |
| Annotation operations | `ready_with_limits` | assign annotator IDs and complete onboarding before annotation | `ann_01` | work order |
| Baseline and evaluation | `ready_with_limits` | run only after validation/adjudication | `eng_01` | baseline docs |
| Stop conditions | `ready_with_limits` | stop if raw data enters git, automation exceeds run record, credentials/session artifacts enter git, or redaction fails | all roles | work order |

## Approved Pilot Limits

| Limit area | Approved limit | Reason | Review date |
|---|---|---|---|
| Source type | stakeholder-provided cases and/or manual public examples | approved pilot sources only | `2026-04-23` |
| Collection method | manual, stakeholder-provided, API-authorized, and automation-assisted | CIB API and automation authorization recorded | `2026-04-23` |
| Batch size | 50 items | diagnostic pilot | `2026-04-23` |
| Screenshots | redacted only, outside git | privacy minimization | `2026-04-23` |
| Source URLs | redacted reference only in repo-visible files | avoid sensitive URL retention | `2026-04-23` |
| External links | normalized/redacted repo-visible references; raw or expanded evidence outside git | redirect and landing capture allowed only under run records | `2026-04-23` |
| Contact handles | category or redacted handle only | reduce personal data | `2026-04-23` |
| OCR text | risk-relevant excerpt after privacy review | avoid unnecessary personal data | `2026-04-23` |
| Replies/comments | selected relevant only | reduce overcollection | `2026-04-23` |
| Raw evidence access | named roles only | limit exposure | `2026-04-23` |
| Retention | pilot-only; review after decision memo | minimize storage | `2026-04-23` |
| Sharing/publication | internal aggregate metrics only by default | avoid public exposure | `2026-04-23` |

## Launch Decision

| Field | Value |
|---|---|
| Final decision | `go_with_limits` |
| Decision owner | project owner |
| Decision date | `2026-04-23` |
| First allowed collection date | after exact raw storage location and access list are confirmed outside git |
| Required next review date | after first 10-15 collected or annotated rows |
| Conditions that must be met before collection | confirm exact storage/access/API credential/automation log locations outside git; assign pseudonymous IDs; pass item-1 preflight; apply redaction checklist; run API/automation only with run records |

## Decision Rationale

- Stakeholder outcome was reported as approved by the project owner.
- Project owner approved the requirement to write exact source, storage, access, retention, and redaction limits into the controlled launch record before collection.
- The pilot is limited to 50 items before checkpoint and decision review; manual, stakeholder-provided, API-authorized, and CIB-authorized automation-assisted collection paths are approved under the controlled launch record.
- The launch packet preserves the repo boundary: no raw evidence, screenshots, full sensitive URLs, handles, or case material in git.
- The pilot remains diagnostic and cannot be used for prevalence or production claims.

## Unresolved Risks

| Risk | Severity | Mitigation | Owner |
|---|---|---|---|
| Exact source details may be sensitive | medium | keep source identifiers outside git | project owner |
| Raw storage path not recorded in repo | medium | confirm in controlled location before first item | governance reviewer |
| Controlled launch details may remain incomplete | high | do not collect until exact source, storage, access, retention, and redaction limits are recorded | project owner |
| Redaction burden may be higher than expected | medium | QA after first 10-15 rows; pause if failures repeat | collector / reviewer |
| `uncertain` may absorb too many cases | medium | monitor label distribution and revise guideline after pilot | annotation lead |

## Sign-Off

| Role | Name or ID | Sign-off date | Notes |
|---|---|---|---|
| Project owner | `owner_01` | `2026-04-23` | Approval outcome recorded. |
| Governance reviewer | `gov_01` | `2026-04-23` | Approved with privacy/storage limits. |
| Collection lead | `collector_01` | pending before first item | Manual-only collection. |
| Annotation lead | `ann_01` / `rev_01` | pending before annotation | Complete onboarding before annotation. |
