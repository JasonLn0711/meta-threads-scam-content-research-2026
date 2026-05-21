# Checkpoint 0081 Executive Addendum

## Purpose

This addendum gives CIB/165-facing reviewers a short entry point into the CIB-approved 78-record research checkpoint.

It is a repo-safe summary. It contains no raw Threads URLs, handles, screenshots, raw post text, raw reply text, contact IDs, stock names, stock codes, price values, credentials, browser/session artifacts, exact controlled-store paths, or stakeholder case IDs.

## Bottom Line

Checkpoint `threads_pilot_v1_0081` is approved by CIB as a 78-record research checkpoint.

It is an evidence-system checkpoint, not a production detector, legal fraud determination, or prevalence estimate.

Current decision:

```text
use checkpoint 0081 as the current CIB-approved research checkpoint;
prepare reviewer-facing package/report addendum;
do not start item 0082 or broad collection from this approval.
```

## Key Numbers

| Measure | Value |
|---|---:|
| Total strict-valid records | 78 |
| `scam` records | 36 |
| `non_scam` records | 24 |
| `uncertain` records | 13 |
| `insufficient_evidence` records | 5 |
| `high` risk | 36 |
| `medium` risk | 11 |
| `low` risk | 31 |
| Binary metric items | 60 |
| Baseline precision | 0.829 |
| Baseline recall | 0.944 |
| Baseline F1 | 0.883 |
| Baseline false positives | 7 |
| Baseline false negatives | 2 |

The baseline numbers are smoke-test metrics on the current binary-evaluable slice. They are not production performance estimates.

## What Changed

Checkpoint 0081 adds:

- second-review adjudication of the existing ambiguous, insufficient, and medium-risk queue;
- local confirmed-pointer items `0080` and `0081`;
- stronger rule boundaries for reply/comment funnels, external-link funnels, profit proof, private-channel migration, and hard negatives;
- explicit preservation of `uncertain` and `insufficient_evidence` when context is too thin.

## Main Finding

CIB-confirmed pointers and careful second review produce more useful rule learning than broad browser-session searching by habit.

The repo can now distinguish more clearly between:

- confirmed scam-like investment or private-channel funnels;
- anti-scam warning hard negatives;
- high-risk trust-building starters that need more context;
- thin fragments that must remain `uncertain` or `insufficient_evidence`.

## What Reviewers Should Focus On

| Reviewer lens | Review question |
|---|---|
| Domain | Are the updated rule-family boundaries useful without exposing raw examples? |
| Legal/privacy | Is the package safe as a redacted CIB-approved research checkpoint? |
| Technical | Are validation, audit, baseline, and duplicate caveats clear enough? |
| Governance | Is it clear that checkpoint approval does not authorize item `0082` or broad expansion? |

## What This Checkpoint Does Not Claim

- It does not claim scam prevalence on Threads.
- It does not make legal fraud determinations.
- It does not authorize item `0082`.
- It does not authorize broad crawler or browser expansion.
- It does not authorize embedding or model training.
- It does not claim production detector readiness.
- It does not put raw evidence into git.

## Review Package

| Artifact | Purpose |
|---|---|
| `reports/checkpoint-0081-approved-package-index.md` | Canonical package index for the 78-record checkpoint. |
| `experiments/evaluation-notes/0089-checkpoint-0081-cib-approved-synthesis.md` | Detailed checkpoint synthesis. |
| `experiments/evaluation-notes/0088-existing-ambiguous-medium-second-review-synthesis.md` | Second-review synthesis behind the adjudication changes. |
| `decision-log/0105-approve-cib-78-record-checkpoint-synthesis.md` | CIB approval decision record. |
| `governance/pilot-launch/run_index.md` | Run, item, checkpoint, and gate index. |

## Next Step

Prepare a selected reviewer-facing package or report addendum around checkpoint 0081.

Do not open new collection unless a later decision records source, cap, evidence surface, controlled-store handling, redaction, second review, and strict-validation requirements.
