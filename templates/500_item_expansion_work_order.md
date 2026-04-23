# 500-Item Expansion Work Order

## Work Order Identity

| Field | Value |
|---|---|
| Work order ID |  |
| Date opened |  |
| Project owner |  |
| Dataset ID |  |
| Prior pilot dataset ID |  |
| Authorization request ID |  |
| Expansion decision record |  |
| Decision | `pending` / `approved_with_limits` / `rejected_or_paused` |

## Prerequisite Gates

| Gate | Complete? | Evidence or link |
|---|---|---|
| 50-item pilot completed |  |  |
| Pilot QA completed |  |  |
| Pilot result summary completed |  |  |
| Guideline revisions applied, if needed |  |  |
| Schema revisions applied, if needed |  |  |
| Authorization updated for 500 items |  |  |
| Raw storage capacity confirmed outside git |  |  |
| Annotator/reviewer capacity confirmed |  |  |
| Decision log authorizes expansion |  |  |

Do not proceed if any prerequisite is incomplete.

## Approved Scope

| Scope item | Approved value | Notes |
|---|---|---|
| Source type(s) |  |  |
| Collection method(s) |  |  |
| Collection window |  |  |
| Raw storage location |  |  |
| Access list |  |  |
| Retention rule |  |  |
| Screenshot policy |  |  |
| URL/link policy |  |  |
| Contact-handle policy |  |  |
| OCR policy |  |  |
| Publication/demo restrictions |  |  |

## Target Composition

| Label bucket | Target count | Actual count | Notes |
|---|---:|---:|---|
| `scam` or high-risk scam-like | 175 |  |  |
| `non_scam` comparators | 175 |  |  |
| `uncertain` | 100 |  |  |
| `insufficient_evidence` | 50 |  |  |
| total | 500 |  |  |

## Partition Plan

| Partition | Target count | Source mix | Status | Notes |
|---|---:|---|---|---|
| batch 01 pilot | 50 |  |  |  |
| batch 02 expansion | 150 |  |  |  |
| batch 03 expansion | 150 |  |  |  |
| batch 04 expansion | 150 |  |  |  |

## Staffing

| Role | Assigned ID(s) | Capacity confirmed? | Notes |
|---|---|---|---|
| collector |  |  |  |
| first-pass annotator |  |  |  |
| reviewer |  |  |  |
| adjudicator |  |  |  |
| research engineer |  |  |  |
| governance reviewer |  |  |  |

## Required Outputs

For each partition:

- collection log
- annotation file
- validation result
- audit summary
- agreement/adjudication summary
- rule baseline comparison
- non-sensitive result summary

Final 500-item package:

- dataset manifest
- aggregate audit summary
- aggregate annotation quality summary
- aggregate baseline comparison
- error analysis
- recommendation memo
- decision log for next phase

## Stop Conditions

| Stop condition | Owner | Response |
|---|---|---|
| authorization ambiguity |  | pause collection |
| raw data enters git |  | stop and remediate |
| redaction inconsistent |  | pause and retrain |
| source skew extreme |  | revise source mix |
| high disagreement |  | revise guideline |
| review capacity exceeded |  | pause expansion |
| baseline false positives dominate |  | revise rules/evaluation |

## Final Decision

- Decision: `approved_with_limits` / `rejected_or_paused` / `needs_revision`
- Decision owner:
- Decision date:
- Conditions:
- Next review date:

