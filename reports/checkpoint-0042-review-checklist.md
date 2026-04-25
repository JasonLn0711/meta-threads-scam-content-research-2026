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
| Report scope is exactly the 42-record checkpoint ending at `threads_pilot_v1_0042` | `pass` | AUTO-OP-01 | Report identity and aggregate sections use checkpoint `0042` and 42 records. |
| Items `0043-0045` are treated as post-checkpoint work, not mixed into the 42-record claims | `pass` | AUTO-OP-01 | Run index and synthesis separate these as post-checkpoint work. |
| Report links or refers to `governance/pilot-launch/run_index.md` | `pass` | AUTO-OP-01 | Listed in next work items and report/checklist context. |
| Report links or refers to `experiments/evaluation-notes/0064-checkpoint-0042-synthesis.md` | `pass` | AUTO-OP-01 | Synthesis is the source checkpoint artifact. |
| Report states this is research triage, not production detection | `pass` | AUTO-OP-01 | Status and non-claim table say no production detector. |
| Report avoids legal fraud determinations | `pass` | AUTO-OP-01 | Report status and non-claim table say no legal determination. |

## 2. Aggregate Claims

| Check | Status | Owner | Notes |
|---|---|---|---|
| Record count is 42 | `pass` | AUTO-OP-01 | Matches checkpoint synthesis and audit output. |
| Label counts match checkpoint synthesis: 14 `scam`, 22 `non_scam`, 5 `uncertain`, 1 `insufficient_evidence` | `pass` | AUTO-OP-01 | Counts match synthesis. |
| Risk counts match checkpoint synthesis: 14 `high`, 4 `medium`, 24 `low` | `pass` | AUTO-OP-01 | Counts match synthesis. |
| Source mix is reported as 27 `manual_public`, 15 `stakeholder_provided` | `pass` | AUTO-OP-01 | Counts match synthesis. |
| Content-shape mix is reported as 16 `text_only`, 11 `link_or_redirect`, 11 `reply_context`, 4 `text_image_post` | `pass` | AUTO-OP-01 | Counts match synthesis. |
| The report avoids prevalence claims | `pass` | AUTO-OP-01 | Report explicitly lists prevalence as a non-claim. |

## 3. Baseline Interpretation

| Check | Status | Owner | Notes |
|---|---|---|---|
| Baseline run is named `checkpoint-0042-synthesis-smoke-v1` | `pass` | AUTO-OP-01 | Name appears in baseline section. |
| Metrics match synthesis: precision 0.700, recall 1.000, F1 0.824 | `pass` | AUTO-OP-01 | Metrics match synthesis. |
| False positives are listed as 6 | `pass` | AUTO-OP-01 | Listed in baseline table. |
| False negatives are listed as 0 | `pass` | AUTO-OP-01 | Listed in baseline table. |
| Baseline is described as a review-queue/triage baseline, not a final classifier | `pass` | AUTO-OP-01 | Interpretation states this directly. |
| False positives are treated as review burden, not ignored | `pass` | AUTO-OP-01 | Interpretation states false positives remain meaningful. |
| Recall priority is tied to CIB policy while preserving human review | `pass` | AUTO-OP-01 | Interpretation ties recall to CIB policy and review queue. |

## 4. Hard-Negative Boundary

| Check | Status | Owner | Notes |
|---|---|---|---|
| Anti-scam warning content is explicitly treated as a hard negative | `pass` | AUTO-OP-01 | Hard-negative section states this. |
| Report says warning/education/victim-prevention wording is not scam-like by itself | `pass` | AUTO-OP-01 | Hard-negative section states this boundary. |
| Report uses direction of persuasion, not isolated vocabulary, as the principle | `pass` | AUTO-OP-01 | Principle is quoted directly. |
| Report does not overgeneralize scam vocabulary into labels | `pass` | AUTO-OP-01 | Boundary is explicitly stated. |

## 5. Governance And Redaction

| Check | Status | Owner | Notes |
|---|---|---|---|
| No raw Threads URLs are present | `pass` | AUTO-OP-01 | Safety scan found no raw Threads URL patterns. |
| No raw handles or profile URLs are present | `pass` | AUTO-OP-01 | Safety scan found no raw handle/profile URL patterns. |
| No raw post text or raw reply text is present | `pass` | AUTO-OP-01 | Report uses aggregate and rule-family summaries only. |
| No screenshots, HTML, browser/session artifacts, cookies, tokens, or storage state are present | `pass` | AUTO-OP-01 | Report contains no raw artifact material. |
| No visible contact IDs are present | `pass` | AUTO-OP-01 | Safety scan found no controlled contact IDs. |
| No controlled-evidence stock names, stock codes, or price values are present | `pass` | AUTO-OP-01 | Safety scan found no controlled stock names/codes/price values. |
| Raw evidence is described as controlled-store-only | `pass` | AUTO-OP-01 | Governance boundaries state this. |
| Stakeholder case IDs and sensitive investigative notes are absent | `pass` | AUTO-OP-01 | Report uses no stakeholder case IDs or sensitive notes. |

## 6. Next-Decision Readiness

| Check | Status | Owner | Notes |
|---|---|---|---|
| Report presents Path A: resume bounded confirmed-pointer intake | `pass` | AUTO-OP-01 | Recommended Decision section includes Path A. |
| Report presents Path B: keep collection paused and review/refine checkpoint report | `pass` | AUTO-OP-01 | Recommended Decision section includes Path B. |
| Report recommends Path B first | `pass` | AUTO-OP-01 | Recommendation is explicit. |
| If Path A is chosen, the next tranche size must be fixed before item `0046` | `pass` | AUTO-OP-01 | Next work items state this. |
| Report rejects broad crawler expansion as the default next step | `pass` | AUTO-OP-01 | Non-claim and acquisition lesson reject broad crawler readiness/default expansion. |
| Report rejects embedding/model training from this checkpoint | `pass` | AUTO-OP-01 | Non-claim table rejects model-training readiness. |

## Final Sign-Off

| Role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Research owner | pending | `revise` / `approve` / `block` | pending | External sign-off still required. |
| Domain reviewer | pending | `revise` / `approve` / `block` | pending | External sign-off still required. |
| Legal/privacy reviewer | pending | `revise` / `approve` / `block` | pending | External sign-off still required. |
| Technical reviewer | pending | `revise` / `approve` / `block` | pending | External sign-off still required. |
| Stakeholder owner | pending | `revise` / `approve` / `block` | pending | External sign-off still required. |

## Blocker Log

| Blocker | Owner | Required fix | Due date | Resolved? |
|---|---|---|---|---|
| No internal self-review blocker found | AUTO-OP-01 | Send to human/stakeholder review for sign-off decision | before stakeholder use | no; sign-off pending |
