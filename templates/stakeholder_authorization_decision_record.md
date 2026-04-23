# Stakeholder Authorization Decision Record

Use this template to record the outcome of a stakeholder approval meeting or written approval thread. Do not include raw Threads content, screenshots, personal data, source URLs, credentials, case packets, or sensitive investigative details.

## Decision Identity

| Field | Value |
|---|---|
| Decision ID |  |
| Decision date |  |
| Meeting or thread reference |  |
| Request owner |  |
| Decision owner |  |
| Governance/privacy reviewer |  |
| Proposed dataset or batch ID |  |
| Source candidate ID |  |

## Decision Outcome

| Field | Value |
|---|---|
| Outcome | `approved` / `approved_with_limits` / `revise_request` / `rejected_or_paused` |
| Approved sample size |  |
| Approved collection window |  |
| Approved source type |  |
| Approved collection method |  |
| Automation approved? | no / yes with written limits |
| Can real collection begin now? | no / yes after go-no-go and readiness review |

## Approved Fields

Use `approved`, `approved_with_redaction`, `approved_with_limits`, `denied`, `pending`, or `not_needed`.

| Field | Decision | Limit or note |
|---|---|---|
| `post_text` |  |  |
| `reply_texts` |  |  |
| `ocr_text` |  |  |
| `image_paths` or screenshot references |  |  |
| `external_links` |  |  |
| `visible_contact_handles` |  |  |
| `visible_platform_redirects` |  |  |
| `source_url_if_stored` |  |  |
| screenshot snapshot |  |  |
| link snapshot |  |  |
| limited metadata notes |  |  |

## Storage, Access, And Retention

| Question | Decision |
|---|---|
| Raw evidence storage location outside git |  |
| Redacted annotation file location |  |
| Raw evidence access list |  |
| Annotation file access list |  |
| Raw evidence retention period |  |
| Redacted/derived file retention period |  |
| Deletion owner |  |
| Redaction owner |  |
| Review before sharing required? | yes / no |

## Screenshot, URL, Link, And OCR Rules

| Evidence type | Approved handling |
|---|---|
| Screenshots | not allowed / redacted only / full approved |
| Source URLs | not stored / redacted reference only / full approved |
| Visible external links | not stored / normalized domain only / redacted reference / full approved |
| Contact handles | category only / redacted handle / full handle approved |
| OCR text | not allowed / risk-relevant excerpt only / full OCR approved |
| Replies/comments | none / selected relevant only / broader thread context approved |

## Sharing And Reporting

| Output | Decision |
|---|---|
| Internal aggregate metrics | allowed / not allowed / limited |
| Internal redacted examples | allowed / not allowed / limited |
| External aggregate metrics | allowed / not allowed / limited |
| External redacted examples | allowed / not allowed / limited |
| Synthetic derivatives | allowed / not allowed / limited |
| Model-assisted review on approved samples | allowed / not allowed / later review required |

## Conditions And Blockers

| Condition or blocker | Owner | Due date | Required before collection? |
|---|---|---|---|
|  |  |  | yes / no |

## Required Follow-Up

| Follow-up | Owner | Due date | Completion evidence |
|---|---|---|---|
| Update `governance/source-intake-register.md` |  |  |  |
| Update `governance/pilot-authorization-register.md` |  |  |  |
| Complete `docs/26-pilot-go-no-go-checklist.md` |  |  |  |
| Complete `templates/pilot_batch_work_order.md` |  |  |  |
| Complete `templates/real_pilot_readiness_review.md` |  |  |  |

## Decision Rationale

Summarize why the decision was made. Keep this non-sensitive and evidence-handling focused.

- 

## Sign-Off

| Role | Name or ID | Decision | Date | Notes |
|---|---|---|---|---|
| Project owner |  | approve / revise / reject |  |  |
| Stakeholder owner |  | approve / revise / reject |  |  |
| Governance/privacy reviewer |  | approve / revise / reject |  |  |
| Research lead |  | approve / revise / reject |  |  |
