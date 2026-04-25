# Pilot Synthesis After Item 0017 Stop

## Purpose

Record the repo-safe synthesis step after Decision 0029 stopped the item 0017 extension for the current pilot tranche.

This note is not a post-50 pilot decision memo. It is a checkpoint addendum that explains why the project should move to stakeholder evidence-scope review before any further collection.

## Inputs Reviewed

| Input | Status |
|---|---|
| First 10-item checkpoint result | reviewed |
| First 15-item limited extension result | reviewed |
| Item 0016 browser-session run result | reviewed |
| Item 0017 second review | reviewed |
| Run 0013 scoped execution result | reviewed |
| Decision 0029 | reviewed |
| Latest local aggregate validation | strict-valid; 17 local records including 1 excluded trace |

## Current Aggregate State

| Measure | Result |
|---|---|
| Accepted records | 16 |
| Excluded traces | 1 |
| Accepted `scam_label` mix | 15 `non_scam`, 1 `uncertain`, 0 `scam` |
| Accepted risk mix | 16 `low`, 0 `medium`, 0 `high` |
| Accepted evidence sufficiency | 16 `partial` |
| Accepted source type | 16 `manual_public` |
| Accepted collection method | 16 `manual_capture` |
| Accepted image/reply/external-link flags | all false |
| Raw evidence in git | no |

## Interpretation

The pipeline works for controlled, redacted, low-risk comparator and boundary items. It does not yet produce the high-risk, multi-signal examples needed for meaningful scam-like case analysis.

The current blocker is not tooling readiness. The blocker is that higher-risk signals likely require evidence outside the current retained fields: screenshots/OCR, narrow reply context, richer visible-link categorization, stakeholder-provided cases, or a separately approved link/redirect path.

## Synthesis Decision

```text
pause_collection_for_stakeholder_evidence_scope_review
```

This means:

- do not open item 0018 under the current method;
- do not force item 0017 from aggregate domain counts or query terms;
- do not treat the 16 accepted records as a high-risk discovery sample;
- use the current results to request a precise evidence-scope decision before further collection.

## Stakeholder Memo Prepared

The repo-safe stakeholder memo is:

```text
docs/51-stakeholder-evidence-expansion-memo.md
```

It summarizes:

- why accepted records remain at 16;
- why item 0017 was stopped;
- which evidence expansions may be needed for high-risk discovery;
- what raw-data controls and second-review gates are required before resuming collection.

## Next Gate

Before any future item 0017 retry or item 0018 attempt, create a new decision or run record that explicitly states:

- approved evidence families;
- raw storage location outside git;
- exact redaction requirements;
- candidate-review caps;
- stop conditions;
- second-review ownership;
- whether the result can count toward the 50-item pilot.
