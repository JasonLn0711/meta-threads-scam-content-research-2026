# Checkpoint 0042 Review Checklist

## Purpose

Use this checklist before sharing `reports/threads-scam-content-checkpoint-0042-v0.1.md` for CIB/165-facing checkpoint review.

The goal is to verify that the checkpoint package is reviewable, redacted, honest about limits, and ready to support a next-decision conversation.

## Review Status Legend

| Status | Meaning |
|---|---|
| `pass` | Ready as written. |
| `revise` | Needs an edit before checkpoint review. |
| `defer` | Valid issue, but not required for checkpoint v0.1. |
| `blocker` | Must be resolved before sharing the checkpoint package. |

## 1. Checkpoint Scope

| Check | Status | Owner | Notes |
|---|---|---|---|
| Report scope is exactly the 42-record checkpoint ending at `threads_pilot_v1_0042` |  |  |  |
| Items `0043-0045` are treated as post-checkpoint work, not mixed into the 42-record claims |  |  |  |
| Report links or refers to `governance/pilot-launch/run_index.md` |  |  |  |
| Report links or refers to `experiments/evaluation-notes/0064-checkpoint-0042-synthesis.md` |  |  |  |
| Report states this is research triage, not production detection |  |  |  |
| Report avoids legal fraud determinations |  |  |  |

## 2. Aggregate Claims

| Check | Status | Owner | Notes |
|---|---|---|---|
| Record count is 42 |  |  |  |
| Label counts match checkpoint synthesis: 14 `scam`, 22 `non_scam`, 5 `uncertain`, 1 `insufficient_evidence` |  |  |  |
| Risk counts match checkpoint synthesis: 14 `high`, 4 `medium`, 24 `low` |  |  |  |
| Source mix is reported as 27 `manual_public`, 15 `stakeholder_provided` |  |  |  |
| Content-shape mix is reported as 16 `text_only`, 11 `link_or_redirect`, 11 `reply_context`, 4 `text_image_post` |  |  |  |
| The report avoids prevalence claims |  |  |  |

## 3. Baseline Interpretation

| Check | Status | Owner | Notes |
|---|---|---|---|
| Baseline run is named `checkpoint-0042-synthesis-smoke-v1` |  |  |  |
| Metrics match synthesis: precision 0.700, recall 1.000, F1 0.824 |  |  |  |
| False positives are listed as 6 |  |  |  |
| False negatives are listed as 0 |  |  |  |
| Baseline is described as a review-queue/triage baseline, not a final classifier |  |  |  |
| False positives are treated as review burden, not ignored |  |  |  |
| Recall priority is tied to CIB policy while preserving human review |  |  |  |

## 4. Hard-Negative Boundary

| Check | Status | Owner | Notes |
|---|---|---|---|
| Anti-scam warning content is explicitly treated as a hard negative |  |  |  |
| Report says warning/education/victim-prevention wording is not scam-like by itself |  |  |  |
| Report uses direction of persuasion, not isolated vocabulary, as the principle |  |  |  |
| Report does not overgeneralize scam vocabulary into labels |  |  |  |

## 5. Governance And Redaction

| Check | Status | Owner | Notes |
|---|---|---|---|
| No raw Threads URLs are present |  |  |  |
| No raw handles or profile URLs are present |  |  |  |
| No raw post text or raw reply text is present |  |  |  |
| No screenshots, HTML, browser/session artifacts, cookies, tokens, or storage state are present |  |  |  |
| No visible contact IDs are present |  |  |  |
| No controlled-evidence stock names, stock codes, or price values are present |  |  |  |
| Raw evidence is described as controlled-store-only |  |  |  |
| Stakeholder case IDs and sensitive investigative notes are absent |  |  |  |

## 6. Next-Decision Readiness

| Check | Status | Owner | Notes |
|---|---|---|---|
| Report presents Path A: resume bounded confirmed-pointer intake |  |  |  |
| Report presents Path B: keep collection paused and review/refine checkpoint report |  |  |  |
| Report recommends Path B first |  |  |  |
| If Path A is chosen, the next tranche size must be fixed before item `0046` |  |  |  |
| Report rejects broad crawler expansion as the default next step |  |  |  |
| Report rejects embedding/model training from this checkpoint |  |  |  |

## Final Sign-Off

| Role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Research owner |  | `approve` / `revise` / `block` |  |  |
| Domain reviewer |  | `approve` / `revise` / `block` |  |  |
| Legal/privacy reviewer |  | `approve` / `revise` / `block` |  |  |
| Technical reviewer |  | `approve` / `revise` / `block` |  |  |
| Stakeholder owner |  | `approve` / `revise` / `block` |  |  |

## Blocker Log

| Blocker | Owner | Required fix | Due date | Resolved? |
|---|---|---|---|---|
|  |  |  |  |  |
