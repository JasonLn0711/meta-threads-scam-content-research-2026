# Data Governance

## Governing Principle

This project studies scam-like content on Threads through lawful, proportionate, and evidence-preserving research methods. Data access constraints are part of the research design.

## Collection Boundary

Do not automate collection from Threads or any Meta surface unless all of the following are true:

1. The collection method is legally approved.
2. Platform access conditions are documented.
3. Stakeholder or institutional authorization is recorded.
4. The approved scope is written in this file or in a linked decision record.
5. The fields collected are limited to what the experiment requires.

Semi-manual collection, stakeholder-provided samples, and documented public examples may be used for early planning if privacy and platform constraints are respected.

"Without limitations" is not an acceptable authorization state. Every real collection must define source, method, fields, storage, access, retention, redaction, and sharing limits.

On `2026-04-23`, a scope-change request proposed accepting low-speed automated Threads/Meta collection without legal approval, platform access conditions, stakeholder authorization, or approved scope. That request is not adopted in this repo. Low speed does not remove the need for authorization, platform-condition review, field limits, storage limits, access limits, retention limits, redaction rules, and auditability.

## Prohibited Repository Contents

Do not commit:

- Raw personal data
- Credentials, tokens, cookies, session files, or browser profiles
- Screenshots containing unnecessary personal information
- Sensitive investigative material
- Unredacted stakeholder case material
- Automated scraping outputs without recorded authorization

Use `data/README.md` to describe datasets without storing sensitive raw data in git.

## Evidence Handling

Each research item should preserve:

- What was observed
- Where it came from at a non-sensitive level
- Which signals were present
- Who reviewed it
- How confident the reviewer was
- What evidence is missing
- Whether the evidence snapshot is complete, redacted, partial, or unavailable

The project must preserve uncertainty. Labels such as `scam`, `uncertain`, and `insufficient_evidence` are research labels, not legal conclusions.

## Privacy Minimization

Prefer derived fields over raw personal content when possible. Store enough evidence to support auditability, but avoid retaining unnecessary personal identifiers.

Examples:

- Store normalized domain category rather than full tracking URL when full URL is not needed.
- Store OCR text relevant to risk signals rather than complete image text when irrelevant personal details appear.
- Store redacted screenshots outside git only when needed for reviewer audit.

## Current Authorization Status

As of `2026-04-23`, the first real 50-item Threads pilot is approved for bounded launch preparation under `go_with_limits`.

Phase-1 work should assume:

- Manual or stakeholder-provided sample collection only.
- Exact source, storage, access, retention, and redaction limits must be written into the controlled launch record before the first item.
- No crawler, scraper, browser automation, bulk collection pipeline, redirect expansion, landing-page capture, profile review, or production scoring.

## Authorization Levels

| Level | Meaning | Allowed use |
|---|---|---|
| `synthetic_only` | No real Threads evidence is involved. | Templates, dry runs, script smoke tests. |
| `pending` | A real source is proposed but approval is not complete. | Planning and manifest drafting only. |
| `approved_manual` | Manual collection or stakeholder-provided cases are approved for stated fields and retention. | 5-item dry run or 50-item pilot within the approved scope. |
| `approved_api` | Approved API access is documented for stated fields and volume. | API-based collection within explicit scope. |
| `rejected_or_paused` | Source or method is not approved. | Do not collect or use. |

## Phase-1 Manual Pilot Preconditions

Before any real Threads item enters `data/interim/` or annotation workflow:

- source candidate intake is completed
- source sampling frame is completed
- stakeholder authorization decision record is completed
- data owner or source category is identified
- collection method is manual or stakeholder-provided
- allowed fields are listed
- raw storage location is outside git
- redaction expectation is clear
- retention rule is known
- publication/demo restrictions are known
- `templates/stakeholder_authorization_decision_record.md` has been completed
- `templates/data_authorization_request.md` has been completed or linked from a governance decision
- `templates/real_pilot_readiness_review.md` has been completed with `go` or `go_with_limits`

## Collection Method Status

| Method | Current status | Notes |
|---|---|---|
| Synthetic examples | Allowed | Use only for templates and tooling tests. |
| Stakeholder-provided examples | Approved with limits for the 50-item pilot | Exact source, storage, access, retention, and redaction limits required before first item. |
| Manual public examples | Approved with limits for the 50-item pilot | Manual-only, privacy-minimized, no automation. |
| API-authorized collection | Not currently approved | Must be recorded before use. |
| Low-speed automated Threads/Meta collection | Rejected or paused | Rate limiting alone is not authorization; requires the same written approval and scope controls as any automated collection. |
| Browser automation, scraping, crawling, bulk export | Not approved | Do not add scripts or outputs for this. |
| Landing-page crawling or redirect-chain capture | Not approved | Visible links may be recorded if permitted; do not crawl destinations. |
| Unlimited 500-item collection | Rejected or paused | Use `docs/32-500-item-expansion-plan.md`; no collection without staged authorization. |

## Governance Records To Use

- Source intake plan: `docs/34-source-intake-and-sampling-frame.md`
- Source candidate intake template: `templates/source_candidate_intake.md`
- Source sampling frame template: `templates/source_sampling_frame_template.csv`
- Source intake register: `governance/source-intake-register.md`
- Stakeholder authorization packet: `docs/36-stakeholder-authorization-packet.md`
- Stakeholder authorization decision record: `templates/stakeholder_authorization_decision_record.md`
- Collection and redaction SOP: `docs/23-collection-and-redaction-sop.md`
- Authorization request template: `templates/data_authorization_request.md`
- Authorization register: `governance/pilot-authorization-register.md`
- Real-pilot readiness review: `docs/35-real-pilot-readiness-review.md`
- Real-pilot readiness template: `templates/real_pilot_readiness_review.md`
- Pilot execution plan: `docs/29-authorized-pilot-execution-plan.md`
- 500-item expansion plan: `docs/32-500-item-expansion-plan.md`
- Pilot batch work order: `templates/pilot_batch_work_order.md`
- 500-item expansion work order: `templates/500_item_expansion_work_order.md`
- Collection log template: `templates/collection_log_template.csv`
- Redaction checklist: `templates/redaction_checklist.md`
- Dataset manifest: `templates/dataset_manifest_template.md`
- Pilot result summary: `templates/pilot_result_summary.md`
