# Pilot Go/No-Go Record: Threads Pilot v1

## Purpose

This is the filled go/no-go record for the first approved 50-item Threads pilot.

Decision: `go_with_limits`.

No real Threads evidence is stored in this record.

## Gate 1: Governance

| Check | Status | Owner | Notes |
|---|---|---|---|
| Stakeholder authorization decision record completed | pass | project owner | `AUTH-THREADS-PILOT-V1-2026-04-23` |
| Data authorization request completed | pass | project owner | `DREQ-THREADS-PILOT-V1-2026-04-23` |
| Source candidate intake completed | pass | project owner | `SRC-REAL-PILOT-APPROVED-2026-04-23` |
| Source sampling frame completed | pass | project owner | 15/15/10/10 diagnostic frame |
| Approved source type recorded | pass | governance reviewer | stakeholder/manual public/API-authorized/CIB automation source category |
| Approved fields listed | pass | governance reviewer | field limits recorded in data authorization |
| Raw storage location outside git confirmed | limited | project owner | controlled-location category approved; exact path outside git before first item |
| Retention rule confirmed | limited | governance reviewer | pilot-only retention; review after decision memo |
| Access list confirmed | limited | governance reviewer | roles listed; exact names outside git if sensitive |
| Exact source/storage/access/retention/redaction launch details approved | limited | project owner | owner approved requirement; controlled details must be filled before first item |
| Publication/demo restrictions confirmed | pass | project owner | no external examples without later approval |
| API and automation authorization recorded | pass | research engineer | CIB-authorized under controlled launch record |

## Gate 2: Collection And Redaction

| Check | Status | Owner | Notes |
|---|---|---|---|
| Collection batch ID assigned | pass | project owner | `threads_pilot_v1_2026-05` |
| Collection log ready | pass | research engineer | use local-only copy under `data/interim/` |
| Redaction checklist ready | pass | collector | use `templates/redaction_checklist.md` |
| Screenshot policy understood | pass | collector | redacted only, outside git |
| URL/link policy understood | pass | collector | normalized/redacted visible-link references only |
| Contact-handle redaction rule understood | pass | collector | category or redacted handle only |
| OCR privacy review rule understood | pass | collector | risk-relevant OCR after privacy review |
| Exclusion reasons defined | pass | collector | unsafe-to-redact, unapproved field, duplicate, unavailable evidence |

## Gate 3: Annotator Calibration

| Check | Status | Owner | Notes |
|---|---|---|---|
| Annotators read guideline | scheduled | annotation lead | required before annotation |
| Annotators read onboarding quickstart | scheduled | annotation lead | required before annotation |
| Annotator onboarding checklists completed | scheduled | annotation lead | required before annotation |
| 5-item blind calibration completed | pass | research engineer | synthetic calibration files exist |
| Agreement report generated | pass | research engineer | synthetic workflow validated; repeat if annotator team changes |
| Disagreements adjudicated | scheduled | adjudicator | synthetic revision note exists; real pilot disagreements still require adjudication |
| `scam` vs `uncertain` boundary understood | scheduled | annotation lead | confirm in onboarding with `docs/06` and watchlist `0013` |
| `uncertain` vs `insufficient_evidence` boundary understood | scheduled | annotation lead | confirm in onboarding with `docs/06` |
| Finance-without-funnel boundary understood | scheduled | annotation lead | confirm before real rehearsal review |
| OCR sufficiency boundary understood | scheduled | annotation lead | confirm before real rehearsal review |
| Generic verification wording tag boundary understood | scheduled | annotation lead | confirm before real rehearsal review |
| Guideline changes recorded if needed | pass | annotation lead | launch-packet revision log plus `0012-synthetic-calibration-guideline-revision.md` recorded |
| Annotation QA checklist ready | pass | annotation lead | template updated with current boundary checks |

## Gate 4: Annotation Operations

| Check | Status | Owner | Notes |
|---|---|---|---|
| Annotation file location under `data/interim/` confirmed | pass | research engineer | local-only ignored path |
| Pseudonymous annotator IDs assigned | limited | project owner | assign before annotation begins |
| Second-review routing rule understood | pass | annotation lead | all high-risk, uncertain, low-confidence, and partial-evidence cases |
| Adjudicator assigned | limited | project owner | assign before annotation begins |
| Pilot batch work order completed | pass | project owner | launch packet work order |
| Dataset manifest draft started | scheduled | research engineer | create after collection starts |
| Validation command tested | pass | research engineer | synthetic strict validation passes |
| Audit command tested | pass | research engineer | synthetic dry run completed |

## Gate 5: Baseline Readiness

| Check | Status | Owner | Notes |
|---|---|---|---|
| Baseline protocol selected | pass | research engineer | rule variants from `docs/08-baseline-strategy.md` |
| Binary metric inclusion rule understood | pass | research engineer | clear `scam` vs `non_scam` only |
| `uncertain` items excluded from binary metrics | pass | research engineer | report separately |
| `insufficient_evidence` reported separately | pass | research engineer | report separately |
| Rule-variant comparison command tested | pass | research engineer | synthetic dry run completed |
| Error-analysis template ready | pass | research engineer | baseline error table exists |

## Final Decision

- Decision: `go_with_limits`
- Decision owner: project owner
- Decision date: `2026-04-23`
- Limits or conditions:
  - 50 pilot items maximum.
  - Manual, stakeholder-provided, API-authorized, and CIB-authorized automation-assisted examples are allowed under the controlled launch record.
  - Production scoring, public accusation, and legal fraud determination remain out of scope.
  - Exact raw evidence storage path and access list must be confirmed outside git before first item.
  - Exact source, storage, access, retention, and redaction limits must be written into the controlled launch record before first item.
  - Raw evidence, screenshots, full sensitive URLs, handles, and stakeholder case details must not be committed.
  - Redaction checklist must be applied before annotation and sharing.
- First collection batch ID: `threads_pilot_v1_2026-05`
- Next review date: after first 10-15 collected or annotated rows, whichever comes first.
