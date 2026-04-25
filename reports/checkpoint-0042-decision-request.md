# Checkpoint 0042 Decision Request

## Purpose

Ask CIB/165-facing reviewers or internal stakeholders to make one concrete checkpoint decision after reviewing the 42-record evidence package.

This request contains no raw Threads URLs, handles, screenshots, raw post text, raw reply text, contact IDs, stock names, stock codes, price values, credentials, browser/session artifacts, or stakeholder case IDs.

## Decision Needed

Choose one path:

| Option | Decision | Meaning |
|---|---|---|
| A | Resume bounded confirmed-pointer intake | Continue collecting approved confirmed pointers one item at a time, with a fixed tranche size and next checkpoint boundary before item `0046` begins. |
| B | Keep collection paused and review/refine checkpoint report | Treat the 42-record checkpoint as the current deliverable and refine the report package before collecting more examples. |

Recommended decision:

```text
B: keep collection paused and review/refine checkpoint report
```

## Why This Decision Is Needed Now

The project has enough evidence-system material to review:

- 42 strict-valid records;
- 14 `scam` / high-risk records;
- 22 `non_scam` records;
- 5 `uncertain` records;
- 1 `insufficient_evidence` record;
- baseline recall `1.000`;
- false negatives `0`;
- false positives `6`;
- a hard-negative anti-scam warning boundary;
- a run index connecting run records, evaluation notes, decision logs, validation status, and baseline outcomes.

Continuing collection without review would increase item count but not answer the current first-principles question: whether the evidence system is reviewable, explainable, and bounded enough for stakeholder use.

## Evidence Package To Review

| Artifact | Purpose |
|---|---|
| `reports/threads-scam-content-checkpoint-0042-v0.1.md` | Main checkpoint report. |
| `reports/checkpoint-0042-review-checklist.md` | Self-review checklist and sign-off scaffold. |
| `experiments/evaluation-notes/0064-checkpoint-0042-synthesis.md` | Repo-safe synthesis of the 42-record aggregate. |
| `governance/pilot-launch/run_index.md` | Index connecting run records, items, decisions, labels, risks, and validation outcomes. |
| `decision-log/0058-select-checkpoint-report-v0-1-after-0042-synthesis.md` | Decision to pause collection by default and create checkpoint report v0.1. |

## Option A Requirements

If stakeholders choose Option A, the next run must define:

- exact next tranche size;
- whether item `0046` starts a new checkpoint tranche;
- allowed source type;
- whether only approved confirmed pointers are allowed;
- whether account-source or crawler paths remain paused;
- review cap and selected-item cap;
- strict-validation requirement;
- second-review requirement for all high-risk, uncertain, low-confidence, link/contact, reply-context, OCR, screenshot, or profile-context items;
- redaction and controlled-store boundaries.

Option A should not authorize broad crawler expansion, unrestricted profile review, landing-page capture, redirect-chain expansion, embedding/model training, or production detection.

## Option B Requirements

If stakeholders choose Option B, the next work should be:

- revise checkpoint report language for stakeholder clarity;
- fill stakeholder sign-off rows in `reports/checkpoint-0042-review-checklist.md`;
- decide whether the 42-record checkpoint is enough for a CIB/165-facing v0.1 package;
- decide what evidence family is still missing, if any;
- define the minimum additional tranche needed only if the report cannot answer stakeholder questions.

## Requested Response

| Field | Response |
|---|---|
| Selected option | `A` / `B` |
| Decision owner |  |
| Date |  |
| Required changes before sharing |  |
| If Option A, next tranche size |  |
| If Option A, allowed source path |  |
| If Option B, report reviewer(s) |  |
| Notes |  |
