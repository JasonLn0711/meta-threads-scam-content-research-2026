# Pilot Go/No-Go Checklist

## Purpose

Use this checklist before moving from synthetic calibration to any real 50-item Threads pilot batch.

The default decision is no-go until each gate is explicitly satisfied.

## Gate 1: Governance

| Check | Status | Owner | Notes |
|---|---|---|---|
| Data authorization request completed |  |  |  |
| Approved source type recorded |  |  |  |
| Approved fields listed |  |  |  |
| Raw storage location outside git confirmed |  |  |  |
| Retention rule confirmed |  |  |  |
| Access list confirmed |  |  |  |
| Publication/demo restrictions confirmed |  |  |  |
| No automation required |  |  |  |

Go only if every governance check is complete.

## Gate 2: Collection And Redaction

| Check | Status | Owner | Notes |
|---|---|---|---|
| Collection batch ID assigned |  |  |  |
| Collection log ready |  |  |  |
| Redaction checklist ready |  |  |  |
| Screenshot policy understood |  |  |  |
| URL/link policy understood |  |  |  |
| Contact-handle redaction rule understood |  |  |  |
| OCR privacy review rule understood |  |  |  |
| Exclusion reasons defined |  |  |  |

Go only if the collector can explain what must not be stored.

## Gate 3: Annotator Calibration

| Check | Status | Owner | Notes |
|---|---|---|---|
| Annotators read guideline |  |  |  |
| 5-item blind calibration completed |  |  |  |
| Agreement report generated |  |  |  |
| Disagreements adjudicated |  |  |  |
| `scam` vs `uncertain` boundary understood |  |  |  |
| `uncertain` vs `insufficient_evidence` boundary understood |  |  |  |
| Guideline changes recorded if needed |  |  |  |

Suggested go threshold:

- `scam_label` agreement at least 0.80 on calibration
- no unresolved primary-label disagreements
- no repeated confusion on evidence sufficiency

## Gate 4: Annotation Operations

| Check | Status | Owner | Notes |
|---|---|---|---|
| Annotation file location under `data/interim/` confirmed |  |  |  |
| Pseudonymous annotator IDs assigned |  |  |  |
| Second-review routing rule understood |  |  |  |
| Adjudicator assigned |  |  |  |
| Dataset manifest draft started |  |  |  |
| Validation command tested |  |  |  |
| Audit command tested |  |  |  |

Go only if the team can run validation before annotation expands.

## Gate 5: Baseline Readiness

| Check | Status | Owner | Notes |
|---|---|---|---|
| Baseline protocol selected |  |  |  |
| Binary metric inclusion rule understood |  |  |  |
| `uncertain` items excluded from binary metrics |  |  |  |
| `insufficient_evidence` reported separately |  |  |  |
| Rule-variant comparison command tested |  |  |  |
| Error-analysis template ready |  |  |  |

Go only if evaluation will preserve uncertainty rather than forcing binary labels.

## Final Decision

- Decision: `go` / `no_go` / `go_with_limits`
- Decision owner:
- Decision date:
- Limits or conditions:
- First collection batch ID:
- Next review date:

## If No-Go

Record the blocker:

- governance approval missing
- source unclear
- redaction unclear
- annotator disagreement too high
- schema/guideline confusion
- operational capacity missing
- other

Then update the relevant doc or template before retrying the checklist.
