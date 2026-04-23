# 500-Item Expansion Plan

## Purpose

This plan defines how the Threads scam-content research project can responsibly reach a 500-item real dataset.

It does not authorize immediate collection. It explicitly rejects "without limitations" collection. A 500-item dataset is possible only after source, method, fields, storage, access, redaction, retention, and review workflow are approved and recorded.

## Current Decision

As of `2026-04-23`, do not start a 500-item real Threads collection.

Reason:

- "all approved, without limitations" is not a valid governance state
- no source category has been specified
- no collection method has been specified
- no raw storage location has been specified
- no redaction policy for real screenshots, URLs, handles, OCR, and replies has been recorded
- no access list or retention period has been recorded
- no evidence exists yet that annotators can label real cases consistently
- the synthetic dry run validates tooling only, not real-world annotation or baseline quality

The correct path is staged expansion.

## Expansion Gates

| Gate | Required before moving forward | Decision |
|---|---|---|
| Synthetic dry run | validation, audit, conversion, and rule baseline succeed on safe sample | complete |
| Authorization gate | source, fields, storage, access, retention, redaction, and sharing limits recorded | pending |
| 50-item pilot | real pilot collected and annotated under approved limits | not started |
| Pilot QA | label agreement, audit, disagreement, and baseline review completed | not started |
| 100-200 item first usable batch | guideline/schema revised after pilot and expanded dataset annotated | not started |
| 500-item expansion | only after earlier gates show annotation, governance, and baseline workflow are stable | not approved |

## Why Not Jump Directly To 500

A 500-item real dataset would multiply the risks that the first pilot is designed to detect:

- incorrect or overbroad labels repeated hundreds of times
- privacy issues in screenshots, OCR text, links, handles, or replies
- source skew that makes baseline results misleading
- annotator drift across many items
- weak evidence being forced into binary labels
- raw evidence or personal data accidentally entering tracked files
- baseline metrics being treated as stronger than the evidence supports

The project should not scale a workflow until the workflow has passed a real pilot.

## Allowed 500-Item Path

The 500-item dataset can proceed only through these stages.

### Stage 1: Authorized 50-Item Pilot

Purpose:

- test real evidence handling
- test annotation consistency
- test redaction rules
- test audit and baseline scripts on real but controlled data

Required composition:

| Bucket | Target count |
|---|---:|
| likely scam or high-risk scam-like | 15 |
| likely non-scam comparator | 15 |
| uncertain or ambiguous | 10 |
| insufficient-evidence or low-context | 10 |

Exit requirement:

- strict validation passes
- QA checklist complete
- annotation disagreement summarized
- baseline variant comparison complete
- decision recorded: expand, revise, narrow, or pause

### Stage 2: 100-200 Item First Usable Batch

Purpose:

- test whether revised annotation rules remain stable
- create the first useful baseline-ready dataset slice
- stress-test source and content-form diversity

Recommended composition:

| Bucket | Target count |
|---|---:|
| `scam` or likely high-risk scam-like | 40-60 |
| `non_scam` comparators | 40-60 |
| `uncertain` | 20-40 |
| `insufficient_evidence` | 10-20 |

Exit requirement:

- enough high-confidence or adjudicated `scam` and `non_scam` items for baseline reporting
- uncertain and insufficient-evidence rates understood
- source skew understood
- false-positive and false-negative themes reviewed
- reviewer burden is acceptable

### Stage 3: 500-Item Expansion

Purpose:

- broaden subtype coverage
- improve baseline error analysis
- test robustness across source types and content forms
- prepare a stronger recommendation memo

Recommended composition:

| Bucket | Target count | Purpose |
|---|---:|---|
| `scam` or high-risk scam-like | 175 | Ensure enough positive examples across scam families. |
| `non_scam` comparators | 175 | Protect against false positives on legitimate content. |
| `uncertain` | 100 | Preserve ambiguity and discover guideline gaps. |
| `insufficient_evidence` | 50 | Measure evidence quality and collection failure modes. |
| total | 500 | Diagnostic research sample, not platform prevalence estimate. |

Recommended content-form targets:

| Content form | Target range |
|---|---:|
| text-only | 100-150 |
| text plus image | 100-150 |
| reply/comment context | 100-150 |
| OCR-heavy or screenshot-style | 75-125 |
| visible link, contact handle, or redirect signal | 100-175 |

These categories can overlap.

## Source Strategy

Use a mixed but governed strategy:

- stakeholder-provided cases, if approved
- manually identified public examples, if permitted
- API-authorized examples, if explicit API approval exists
- synthetic/redacted examples only for calibration and QA, not real metrics

Do not use:

- scraping
- browser automation
- bulk export
- profile/account crawling
- landing-page crawling
- redirect-chain expansion
- raw browser sessions, cookies, credentials, or exported profiles

## Annotation Staffing

Minimum staffing for 500 items:

| Role | Minimum |
|---|---:|
| collector | 1-2 |
| first-pass annotators | 2 |
| reviewers | 1-2 |
| adjudicator | 1 |
| research engineer | 1 |
| governance reviewer | 1 |

Recommended review routing:

- 100 percent of high-risk `scam` items
- 100 percent of `uncertain` items
- 100 percent of low-confidence items
- 100 percent of partial/insufficient/not-reviewable evidence cases
- at least 20 percent of `non_scam` comparators

## Batch Partitioning

Do not annotate 500 items as one undifferentiated file.

Recommended partitions:

```text
threads_500_v1_batch_01_pilot_50
threads_500_v1_batch_02_expand_150
threads_500_v1_batch_03_expand_150
threads_500_v1_batch_04_expand_150
```

Each partition should have:

- collection log
- annotation file
- audit output
- agreement/adjudication summary
- baseline variant comparison
- non-sensitive result summary

## Baseline Reporting For 500 Items

Binary precision/recall should include only:

- `scam` and `non_scam`
- high-confidence or adjudicated items
- `sufficient` or `partial` evidence
- nonempty `post_text` or `ocr_text`

Report separately:

- `uncertain`
- `insufficient_evidence`
- source skew
- content-form skew
- missing evidence
- reviewer burden
- false positives by benign category
- false negatives by missed evidence surface

## Stop Conditions

Pause before or during 500-item expansion if:

- authorization scope is unclear
- source, field, or storage limits are violated
- raw personal data enters tracked files
- screenshot/link/OCR redaction becomes inconsistent
- `uncertain` exceeds 30 percent without clear value
- `insufficient_evidence` exceeds 20 percent without collection fixes
- annotation disagreement clusters around the same label boundary
- reviewers cannot keep up with required second review
- baseline false positives dominate legitimate comparator categories

## Required Records Before 500 Begins

- completed authorization request
- updated `governance/pilot-authorization-register.md`
- completed pilot go/no-go checklist
- completed real-pilot readiness review for the pilot and expansion scope
- completed 500-item expansion work order
- approved raw storage plan outside git
- access and retention rule
- redaction procedure
- completed 50-item pilot summary
- completed pilot decision memo using `templates/pilot_decision_memo.md`
- decision log approving expansion beyond the pilot

## Decision

The project may plan for a 500-item expansion, but it must not collect 500 real items until the staged gates are completed.

The immediate next action remains stakeholder authorization for the first real 50-item pilot.
