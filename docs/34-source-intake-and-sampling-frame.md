# Source Intake And Sampling Frame

## Purpose

This document defines how the project evaluates candidate sources before any real Threads item enters the pilot workflow.

The goal is to prevent the first real dataset from becoming source-skewed, privacy-heavy, or impossible to defend. This document does not authorize collection.

## Current State

As of `2026-04-23`:

- synthetic examples are approved for dry runs
- no real Threads item has been collected or committed
- the first real pilot is approved only for bounded `go_with_limits` launch preparation
- exact sensitive source, storage, access, retention, and redaction details still must be completed outside git before item 1
- immediate unlimited 500-item collection is rejected or paused
- the next valid real-data step is the first 10-15 item checkpoint inside the conditional 50-item pilot

## Source Intake Principle

Every real source candidate must be evaluated before collection.

The evaluation must answer:

- Is the source legally and operationally allowed?
- What fields may be retained?
- What privacy or redaction burden does it create?
- What evidence surfaces does it provide?
- What label buckets and content forms is it likely to cover?
- Would using it create source skew?
- Is it appropriate for the 50-item pilot, later expansion, or neither?

## Source Candidate Types

| Source type | Potential use | Main risk |
|---|---|---|
| `stakeholder_provided_case` | Operationally relevant examples and reported cases. | Sensitive investigative or personal data. |
| `manual_public_example` | Publicly visible examples collected manually under approved limits. | Platform/legal comfort, privacy, source URL handling. |
| `manual_public_comparator` | Non-scam and hard-negative comparator examples. | Overcollection of ordinary users. |
| `stakeholder_summary_only` | Pattern discovery without raw evidence. | May be too vague for annotation. |
| `api_authorized_sample` | Structured access if explicit API approval exists. | Scope and terms must be precise. |
| `researcher_synthetic` | Templates, calibration, tooling dry runs. | Not real evidence; cannot support real-world claims. |

Do not use scraping, browser automation, crawling, bulk export, landing-page crawling, or redirect-chain expansion unless a later recorded decision explicitly approves it.

## Intake Sequence

1. Create a source candidate ID.
2. Fill `templates/source_candidate_intake.md`.
3. Add the candidate to `governance/source-intake-register.md`.
4. Score privacy, redaction burden, evidence quality, source skew, and operational burden.
5. Decide whether the source is suitable for:
   - no use
   - planning only
   - calibration only
   - 50-item pilot
   - 100-200 item expansion
   - later 500-item expansion
6. If real evidence is proposed, complete `templates/data_authorization_request.md`.
7. If approved, add the source to `templates/source_sampling_frame_template.csv` before collection begins.

## Source Candidate ID

Use stable IDs that do not reveal sensitive source details:

```text
SRC-2026-04-001
SRC-2026-04-002
SRC-2026-05-001
```

Do not encode handles, URLs, stakeholder names, account names, or case identifiers in source IDs.

## Source Scoring

Use green/yellow/red ratings.

| Dimension | Green | Yellow | Red |
|---|---|---|---|
| Authorization clarity | Approved source and method are documented. | Approval likely but not complete. | Source or method unclear. |
| Privacy exposure | Low personal data; redaction easy. | Some personal data; redaction manageable. | Sensitive data or unclear redaction. |
| Evidence quality | Text/OCR/replies/links support annotation. | Evidence partial but reviewable. | Too incomplete or not reviewable. |
| Content-form coverage | Adds needed content forms. | Duplicates existing forms but usable. | Adds little beyond current sample. |
| Label-bucket value | Helps balance scam, non-scam, uncertain, or insufficient evidence. | Label value uncertain. | Likely to worsen imbalance. |
| Operational burden | Manual collection and review are feasible. | Requires careful handling or extra review. | Too slow or risky for phase 1. |
| Source skew risk | Complements other sources. | May dominate if unchecked. | Would make dataset misleading. |

Red authorization or red privacy means no real collection from that source.

## 50-Item Pilot Sampling Frame

The 50-item pilot is diagnostic, not a prevalence sample. Do not complete it in one uninterrupted pass; the first 10-15 items must be reviewed before continuation.

Target label buckets:

| Bucket | Target count |
|---|---:|
| likely scam or high-risk scam-like | 15 |
| likely non-scam comparator | 15 |
| uncertain or ambiguous | 10 |
| insufficient-evidence or low-context | 10 |

Target content-form coverage:

| Content form | Minimum target |
|---|---:|
| text-only | 8 |
| text plus image | 8 |
| reply/comment context | 10 |
| OCR-heavy or screenshot-style | 8 |
| visible link, handle, or redirection signal | 10 |

These content-form categories can overlap.

## Source Mix Guidance

If multiple real sources are approved, avoid letting one source type dominate the pilot.

Suggested pilot mix:

| Source type | Target range |
|---|---:|
| stakeholder-provided cases | 15-25 |
| manual public likely scam-like examples | 10-15 |
| manual public non-scam comparators | 10-15 |
| ambiguous or insufficient-evidence cases | 5-10 |

If only one real source is approved, the pilot may still proceed, but the pilot result summary must mark source skew as a limitation.

## Comparator Strategy

Non-scam comparators are required. They should include:

- ordinary conversation
- legitimate marketing
- legitimate financial education or investment discussion
- ordinary recruitment or job posts
- ordinary giveaways or promotions
- satire, politics, or celebrity content that is not scam-like

Do not collect broad ordinary-user content beyond approved and minimal comparator needs.

## Exclusion Rules

Exclude a candidate item or source when:

- collection authorization is unclear
- source includes sensitive material that cannot be redacted
- required fields cannot be retained
- source would require crawling, scraping, or bulk export
- source depends on unapproved account/profile/landing-page context
- raw evidence cannot be stored outside git
- annotators would need legal or investigative context not present in the item

Record exclusion reason in the collection log or source intake register.

## Source Skew Reporting

Every pilot summary must report:

- item counts by `source_type`
- item counts by `collection_method`
- item counts by source candidate ID, if safe
- label distribution by source type
- content-form distribution by source type
- limitations caused by source skew

Do not make prevalence claims from a diagnostic or source-skewed sample.

## Handoff To Collection

Before collection begins:

1. Candidate source is approved in `governance/source-intake-register.md`.
2. Authorization request is complete.
3. Source appears in `templates/source_sampling_frame_template.csv`.
4. Pilot work order names the approved source mix.
5. Collection log is ready.
6. Raw evidence storage and redaction rules are confirmed.

If any item is missing, do not collect real evidence.
