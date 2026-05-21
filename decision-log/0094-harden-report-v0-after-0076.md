# Decision 0094: Harden Report v0 After 0076

## Date

2026-04-26

## Status

accepted

## Context

Checkpoint 0055 is the current approved CIB/165-facing package. Local item 0076 was later accepted as a strict-valid hard-negative calibration addendum:

```text
non_scam / low
```

The report v0 package still carried some earlier 42-record and initial-pilot framing. That framing could make stakeholders think the repo's next step is more collection by default.

## Decision

Harden the report v0 package around the current state:

- checkpoint 0055 is the canonical approved package;
- item 0076 is a narrow hard-negative addendum;
- broad crawler or browser expansion is not the default next step;
- future collection requires a new decision record, caps, controlled preservation, redaction, second review, strict validation, and repo-safe reporting;
- stakeholders should choose one bounded post-0076 path before new collection.

## Post-0076 Options

| Option | Meaning |
|---|---|
| `report_only_delivery` | Refine and deliver the checkpoint report package without new evidence collection. |
| `targeted_confirmed_pointer_tranche` | Add approved stakeholder/CIB pointers for new scam/high-risk rule-family learning. |
| `calibration_only_browser_tranche` | Use browser-session work only for hard negatives, uncertainty, insufficient-evidence, or false-positive calibration. |

## Rationale

The repo has enough evidence-system material to be reviewed. The highest-value next product is a clear CIB/165-facing report and decision memo, not another candidate bank.

Browser-session runs can be useful, but only when their purpose is explicit and capped. Confirmed pointers remain the better source when the goal is final scam/high-risk rule-family learning.

## Updated Artifacts

- `reports/threads-scam-content-research-v0.md`
- `reports/threads-scam-content-research-v0-executive-brief.md`
- `reports/post-0076-next-decision-memo.md`
- `reports/report-v0-review-checklist.md`
- `reports/checkpoint-0055-approved-package-index.md`
- `docs/27-report-v0-delivery-plan.md`
- `docs/18-recommended-path-v1.md`
- `README.md`

## Non-Claims

This decision does not authorize:

- new item collection;
- broad crawler expansion;
- embedding or model training;
- profile graph capture;
- private-message access;
- raw evidence in git;
- production detection;
- legal fraud determinations.
