# Threads Scam Content Research v0 Executive Brief

## Brief Identity

| Field | Value |
|---|---|
| Report package | Threads scam-content research v0 |
| Target delivery date | 2026-04-30 |
| Audience | CIB/165-facing review, anti-fraud research planning, investigators, professors, and engineers |
| Status | Review brief for stakeholder decision. No production promise. No real-data result claim. |
| Primary report | `reports/threads-scam-content-research-v0.md` |

## Bottom Line

The next useful research step is a governed Threads-only pilot, not a production detector.

Approve a small, manually reviewed phase-1 pilot only after source authorization, redaction rules, access rules, retention rules, controlled launch details, and annotator calibration are recorded. The recommended path is:

1. Complete controlled launch details outside git and initialize the local workspace.
2. Rehearse 1-2 manually prepared records and run a 5-item annotation calibration.
3. Collect only the first 10-15 real items for checkpoint review.
4. Continue to the conditional 50-item pilot only if the checkpoint permits it.
5. Use the pilot to revise the annotation guide, data schema, and baseline rules.
6. Expand to 100-200 items only after the pilot shows that labels, evidence fields, and review workflow are stable enough.

This keeps the project useful under budget while avoiding unsupported claims about legal fraud, automated enforcement, or platform-scale detection.

## Why Threads First

Threads is the recommended first surface because stakeholder discussion suggests high scam-content report pressure there, and the first evidence surfaces are realistic to inspect:

- post text
- selected replies and comments
- text in images or screenshots through OCR
- visible links and domains
- visible contact handles
- redirection language to private channels or external platforms

This is narrower and more defensible than a Meta-wide scam-ad system. It also avoids making long video, deepfake detection, account graph analysis, or production automation prerequisites for the first research result.

## What The v0 Package Provides

The repo now supports a first research pilot through:

- a `thread_item` dataset schema
- a human annotation guideline
- a label vocabulary for `scam`, `non_scam`, `uncertain`, and `insufficient_evidence`
- governance, collection, and redaction templates
- pilot runbooks and go/no-go checks
- controlled launch, local workspace, preflight, rehearsal, and first-checkpoint operating docs
- synthetic calibration samples
- local validation, audit, agreement, conversion, and rule-baseline scripts
- an initial report tying scope, evidence, budget, governance, annotation, and baseline experiments together

The package is intentionally documentation-first and tooling-light.

## Decision Requested

Stakeholders should decide whether the project may proceed to the first real pilot batch and under what limits.

| Decision area | Needed answer |
|---|---|
| Source | Which first source is approved: stakeholder-provided cases, manually identified public examples, or another approved source? |
| Fields | Which fields may be stored for annotation and audit? |
| Screenshots | Can screenshots be retained, and must they be redacted before annotation? |
| URLs and links | Can source URLs, visible links, domains, or redacted references be stored? |
| Raw evidence | Where may raw evidence live outside git, who may access it, and when must it be deleted? |
| Reporting | Can aggregate metrics and redacted examples appear in internal memos? |
| Pilot decision | Is the first pilot `go`, `go_with_limits`, or `no_go`? |

Use `docs/36-stakeholder-authorization-packet.md`, `templates/stakeholder_authorization_decision_record.md`, `templates/data_authorization_request.md`, `docs/26-pilot-go-no-go-checklist.md`, `docs/35-real-pilot-readiness-review.md`, `docs/37-approved-pilot-launch-plan.md`, `docs/39-local-pilot-workspace.md`, and `docs/40-pilot-preflight-verification.md` before any real evidence is collected.

## What This Work Will Not Do

The v0 package does not authorize:

- automated Threads collection or scraping
- account or profile crawling
- landing-page crawling or redirect expansion
- production scoring
- enforcement actions
- legal fraud determinations
- unredacted sensitive data in git
- broad Meta cross-platform integration
- heavy video or deepfake detection as phase-1 mainline work

## First Pilot Design

The recommended 50-item pilot is diagnostic, not a prevalence estimate. It must not be completed in one uninterrupted pass: the first 10-15 items are a checkpoint gate for governance, redaction, evidence quality, annotation consistency, and source skew.

| Bucket | Target count | Purpose |
|---|---:|---|
| likely `scam` or high-risk scam-like | 15 | Test positive signal coverage. |
| likely `non_scam` comparator | 15 | Check false-positive risk. |
| likely `uncertain` | 10 | Stress-test ambiguity rules. |
| likely `insufficient_evidence` | 10 | Test evidence-quality and collection rules. |

Continue past 10-15 items only after the checkpoint decision is `continue_to_50` or `continue_with_limits`.

The first baseline-ready slice should use high-confidence or adjudicated items with nonempty `post_text` or `ocr_text`, clear `scam` or `non_scam` labels, and sufficient evidence. `uncertain` and `insufficient_evidence` items should be retained for ambiguity and evidence-quality analysis, but excluded from binary precision/recall.

## Key Risks To Watch

| Risk | Mitigation |
|---|---|
| Annotators over-label aggressive marketing or finance content as scam | Require observable evidence and use `uncertain` when mixed signals remain unresolved. |
| `uncertain` becomes a catch-all | Separate mixed evidence from missing evidence; use `insufficient_evidence` when review cannot proceed. |
| Screenshots or links introduce privacy risk | Redact before annotation where required and keep raw evidence outside git. |
| The dataset skews toward only obvious lures | Include non-scam comparators and ambiguous cases from the start. |
| The report is read as a production promise | Repeat that phase 1 is research, triage, and evidence design only. |

## Next Seven Days

By 2026-04-30:

1. Complete report-v0 review using `reports/report-v0-review-checklist.md`.
2. Collect reviewer comments with `templates/report_review_feedback.md`.
3. Resolve scope, legal/privacy, and evidence-language comments before delivery.
4. Record that the stakeholder outcome is approved with bounded launch limits.
5. Complete the controlled launch record with exact source, storage, access, retention, redaction, screenshot, OCR, URL/link, handle/contact, role-ID, permitted-field, forbidden-field, uncertainty, and signoff details before real collection.
6. Initialize the local workspace, pass item-1 preflight, rehearse 1-2 records, run 5-item calibration, and prepare the first 10-15 item checkpoint.
