# Post-0076 Next Decision Memo

## Purpose

This memo gives reviewers and stakeholders a single repo-safe decision point after the approved checkpoint 0055 package and the local 0076 hard-negative addendum.

It does not authorize new collection. It contains no raw Threads URLs, handles, screenshots, raw post text, raw reply text, contact IDs, stock names, stock codes, price values, credentials, browser/session artifacts, or stakeholder case IDs.

## Current State

| Field | Value |
|---|---|
| Canonical approved package | checkpoint 0055 |
| Post-approval addendum | item 0076 hard-negative calibration |
| Current approved use | CIB/165-facing redacted evidence-system review |
| Current collection status | no new prospective tranche open |
| Default next action | report/checkpoint maintenance |

Checkpoint 0055 remains the canonical reviewed package. Item 0076 is useful because it tests false-positive pressure around anti-scam warning, victim-prevention, and scam-method vocabulary.

## Decision Needed

Choose exactly one path before opening new collection or promotion work.

| Option | Meaning | Choose if |
|---|---|---|
| `report_only_delivery` | Refine and deliver the checkpoint report package without new evidence collection. | The current 0055 plus 0076 package is enough for near-term CIB/165 review. |
| `targeted_confirmed_pointer_tranche` | Add a small set of stakeholder/CIB confirmed pointers through controlled capture, redaction, second review, and strict validation. | New scam/high-risk rule-family learning is needed. |
| `calibration_only_browser_tranche` | Use approved browser-session work only for hard negatives, uncertainty, insufficient-evidence, or false-positive calibration. | Reviewers need better boundary cases, not more alleged scam positives. |

## Recommendation

Select `report_only_delivery` unless a stakeholder has a concrete need for new scam/high-risk rule-family learning.

Reasoning:

- The repo already has a strict-valid approved checkpoint package.
- Browser-session expansion has produced useful calibration but has not justified unbounded collection.
- Confirmed pointers are more efficient when the goal is high-risk rule-family learning.
- The next high-value product is a readable CIB/165-facing evidence-system report, not a larger candidate bank.

## Required Gate If New Evidence Is Approved

Before any new item is promoted:

1. Record a new decision log entry with option, owner, date, cap, source type, and stop conditions.
2. Confirm the source path is approved.
3. Preserve raw evidence only in the controlled store.
4. Create redacted manual entry fields only after controlled review.
5. Run second review from a different reviewer perspective.
6. Build the manual record.
7. Run strict validation.
8. Record repo-safe aggregate results only.

## Stop Conditions

Stop if:

- the work starts depending on broad crawler expansion;
- raw Threads content, URLs, handles, screenshots, browser storage, or credentials are about to enter git;
- a candidate lacks item-level source linkage;
- reply/thread context is not review-ready but the item would be labeled anyway;
- the run starts becoming profile graph capture, private-message access, redirect crawling, model training, production detection, or legal determination.

## Output Of The Decision

The selected option should update:

- `docs/18-recommended-path-v1.md`
- this memo, if the recommendation changes
- `reports/threads-scam-content-research-v0.md`
- `reports/threads-scam-content-research-v0-executive-brief.md`
- a new decision-log entry
