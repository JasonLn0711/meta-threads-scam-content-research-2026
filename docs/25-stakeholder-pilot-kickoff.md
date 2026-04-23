# Stakeholder Pilot Kickoff

## Purpose

This memo is the stakeholder-facing kickoff packet for the first Threads scam-content research pilot. It asks for a narrow approval: a governed, manually reviewed pilot dataset and annotation exercise, not automation, enforcement, or production detection.

## Current Position As Of 2026-04-23

The pilot kickoff is not the immediate deliverable. The immediate deliverable is the CIB/165-facing report:

```text
reports/threads-scam-content-research-v0.md
```

Target date: `2026-04-30`.

First-principles order:

1. Write the report v0 to define the problem, scope, dataset plan, annotation plan, baselines, evaluation, budget fit, and approval gates.
2. Use the report to align stakeholders on what counts as report-worthy Threads scam-like content.
3. Only then run this pilot kickoff to request permission for real examples and annotation.

Do not treat this pilot memo as authorization by itself.

## Request

Approve the project team to run a phase-1 pilot with:

- 5-item synthetic or redacted annotator calibration
- 50-item first pilot batch after calibration passes
- optional expansion to 100-200 items after pilot review
- manual or stakeholder-provided examples only
- no automated collection, scraping, browser automation, or landing-page crawling
- raw evidence stored outside git
- redacted/derived annotation files only in project working areas

## Why This Is The Right Next Step

The research scaffold is ready:

- v1 dataset schema exists
- v1 annotation guide exists
- governance and redaction SOP exists
- collection log and data authorization templates exist
- audit, validation, agreement, and baseline scripts exist
- calibration files and synthetic examples exist

The project now needs stakeholder approval for real examples and a clear evidence standard before the team annotates beyond synthetic data.

## Pilot Scope

Included:

- Threads text posts
- text plus image posts
- selected replies/comments
- OCR text from approved/redacted images
- visible external links
- visible contact handles and platform redirects
- human labels, risk levels, signal tags, and evidence sufficiency

Excluded:

- automated Threads or Meta collection
- account/profile crawling
- broad comment harvesting
- landing-page crawling or redirect expansion
- long video
- deepfake detection
- legal determinations
- production scoring or enforcement recommendations

## Approval Needed

Stakeholders should decide:

| Decision | Needed answer |
|---|---|
| Source approval | Can stakeholder-provided or manually identified examples be used? |
| Field approval | Which schema fields may be stored? |
| Screenshot policy | Can screenshots be retained, and must they be redacted? |
| URL policy | Can source URLs or visible links be stored, normalized, redacted, or omitted? |
| Retention | How long may raw and derived evidence be kept? |
| Access | Who may see raw evidence and annotation files? |
| Reporting | Can aggregate metrics and redacted examples be shown in memos? |
| Publication | Are any outputs limited to internal review? |

Use `docs/36-stakeholder-authorization-packet.md`, `templates/stakeholder_authorization_decision_record.md`, and `templates/data_authorization_request.md` to record the decision.

## First Pilot Design

Target 50 items:

| Bucket | Count |
|---|---:|
| likely scam or high-risk scam-like | 15 |
| likely non-scam comparator | 15 |
| uncertain or ambiguous | 10 |
| insufficient-evidence or low-context | 10 |

This is a diagnostic sample, not a prevalence estimate. It is designed to test annotation reliability, evidence quality, and baseline feasibility.

## Outputs After Pilot

The team will produce:

- dataset manifest
- annotation agreement report
- audit summary
- disagreement/adjudication summary
- rule baseline comparison
- error analysis
- recommendation: expand, revise guideline/schema, narrow scope, or pause

## Stop Conditions

Pause the pilot if:

- collection authorization is unclear
- redaction rules are unclear
- annotator calibration fails
- raw personal data enters tracked files
- `uncertain` or `insufficient_evidence` rates are too high
- the team needs evidence that phase 1 is not approved to collect

## Meeting Agenda

1. Confirm the project is research, not production detection.
2. Confirm allowed data sources and fields.
3. Confirm raw storage and redaction rules.
4. Confirm pilot sample composition.
5. Confirm who reviews and adjudicates annotations.
6. Confirm what outputs can be shared.
7. Record approval, limits, and next owner.

## Immediate Next Action

Complete `docs/36-stakeholder-authorization-packet.md` for the first real source. If the decision is `approved` or `approved_with_limits`, fill `templates/stakeholder_authorization_decision_record.md`, update the governance registers, then continue through `docs/26-pilot-go-no-go-checklist.md`, `templates/pilot_batch_work_order.md`, and `docs/35-real-pilot-readiness-review.md`.
