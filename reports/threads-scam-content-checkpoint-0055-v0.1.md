# Threads Scam Content Checkpoint 0055 Report v0.1

## Report Identity

| Field | Value |
|---|---|
| Report | Threads scam-content checkpoint 0055 report v0.1 |
| Date | 2026-04-25 |
| Repo | `meta-threads-scam-content-research-2026` |
| Dataset checkpoint | `threads_pilot_v1_0055` |
| Records | 55 |
| Audience | CIB/165-facing review, research reviewers, investigators, professors, engineers |
| Status | Checkpoint report, not production detector, not legal determination |
| Decision request | `reports/checkpoint-0055-decision-request.md` |
| Review checklist | `reports/checkpoint-0055-review-checklist.md` |
| Primary synthesis | `experiments/evaluation-notes/0068-checkpoint-0055-synthesis.md` |
| Current decision | `C2`: keep collection paused and review/refine this report package |

## Executive Summary

The project has completed a 55-record checkpoint after two distinct phases:

- checkpoint 0042 established that confirmed-pointer intake can produce useful high-risk scam-like rule families and hard-negative boundaries;
- checkpoint 0055 tested a stakeholder-approved Option A browser-session tranche after that checkpoint.

The 55-record checkpoint is strict-valid and reviewable. It also gives a clear acquisition lesson: approved browser-session candidate search is operationally feasible, but in this tranche it mostly produced uncertainty, insufficient evidence, and false-positive pressure. Confirmed pointers remain the highest-yield path for final scam/high-risk rule learning.

Checkpoint decision:

```text
C2: keep collection paused and review/refine the 55-record checkpoint report
```

The project should not open another browser-session tranche by habit. Item `0056` is not authorized by the current decision. The immediate task is to review and refine this checkpoint package for CIB/165-facing use.

## What This Checkpoint Proves

| Claim | Status |
|---|---|
| The repo can maintain a strict-valid 55-record redacted aggregate | Supported |
| Controlled raw evidence can remain outside git while repo-safe review artifacts stay useful | Supported |
| Confirmed pointers are currently higher-yield than browser-session candidate search for scam/high-risk rule learning | Supported |
| Browser-session search can add useful false-positive and uncertainty calibration examples | Supported |
| Second review is necessary for thin, reply-context, link/contact, and low-confidence candidates | Supported |
| High-recall baseline posture can preserve zero false negatives on the current binary-evaluable slice | Supported |

## What This Checkpoint Does Not Prove

| Non-claim | Reason |
|---|---|
| Scam prevalence on Threads | Sources are confirmed-pointer and controlled candidate samples, not representative population samples. |
| Legal fraud determination | This is research triage and rule-family learning, not legal adjudication. |
| Production detector readiness | Dataset remains small, review-governed, and source-biased. |
| Broad crawler readiness | The latest tranche showed review burden before high-risk discovery value. |
| Embedding/model-training readiness | The dataset is still too small and biased for model artifacts without a later governance decision. |

## Aggregate Distribution

| Label / risk | Count |
|---|---:|
| `scam` | 17 |
| `non_scam` | 23 |
| `uncertain` | 9 |
| `insufficient_evidence` | 6 |
| `high` risk | 17 |
| `medium` risk | 7 |
| `low` risk | 31 |

Source mix:

| Source type | Count |
|---|---:|
| `manual_public` | 37 |
| `stakeholder_provided` | 18 |

Content shape:

| Content shape | Count |
|---|---:|
| `text_only` | 21 |
| `link_or_redirect` | 16 |
| `reply_context` | 14 |
| `text_image_post` | 4 |

## Delta Since Checkpoint 0042

| Metric | Checkpoint 0042 | Checkpoint 0055 | Delta |
|---|---:|---:|---:|
| Total records | 42 | 55 | +13 |
| `scam` | 14 | 17 | +3 |
| `non_scam` | 22 | 23 | +1 |
| `uncertain` | 5 | 9 | +4 |
| `insufficient_evidence` | 1 | 6 | +5 |
| `high` risk | 14 | 17 | +3 |
| `medium` risk | 4 | 7 | +3 |
| `low` risk | 24 | 31 | +7 |

Interpretation:

- Post-0042 confirmed pointers added three final scam/high-risk records.
- The Option A browser-session tranche added no final scam/high-risk records.
- The browser-session tranche mainly increased `uncertain` and `insufficient_evidence`, which is useful for calibration but weak for new scam-rule discovery.

## Baseline Result

Rule baseline run:

```text
checkpoint-0055-option-a-run-0038-smoke-v1
```

| Metric | Value |
|---|---:|
| Binary metric items | 40 |
| Precision | 0.708 |
| Recall | 1.000 |
| F1 | 0.829 |
| False positives | 7 |
| False negatives | 0 |

Interpretation:

- Recall remains the primary safety metric because stakeholder policy prefers avoiding false negatives.
- False positives increased from 6 to 7 and should be treated as reviewer workload, not as a harmless metric.
- The baseline remains a review-queue generator, not a final classifier.

## Rule-Family Lessons

The checkpoint continues to support the rule-library principle that scam-like labels should come from converging evidence families, not isolated keywords or topics.

Reusable evidence families remain strongest when they combine several of:

- investment or profit narrative;
- private-channel migration;
- contact or reply-to-DM funnel;
- link, redirect, wallet, deposit, or off-platform action;
- authority, course, group, or advisor framing;
- social proof, testimonial, past-performance, or urgency pressure;
- account-level pattern such as repeated style clusters or posting cadence;
- reply/comment context that changes the meaning of the post.

The 55-record checkpoint also reinforces a limit: thin browser snippets often do not contain enough evidence to label safely, even when they match a risk-probe query.

## Hard-Negative Boundary

The earlier hard-negative lesson still applies:

```text
label the direction of persuasion, not isolated scam vocabulary
```

Anti-scam warnings, victim-prevention posts, and concern-question posts can mention the same vocabulary as scam lures. They should not be labeled scam-like unless the item itself creates a new conversion path or persuasion funnel.

## Acquisition Lesson

Confirmed-pointer intake is still the best current path for final scam/high-risk learning.

Approved browser-session capture is useful for:

- testing candidate review flow;
- finding false-positive pressure;
- discovering uncertainty boundaries;
- proving second-review discipline;
- validating whether snippets are too thin for stable labels.

It is not currently the highest-yield method for adding new final scam/high-risk examples.

## Governance Boundaries

This report excludes:

- raw Threads URLs;
- raw handles or profile URLs;
- raw post text and raw reply text;
- screenshots and HTML;
- visible contact IDs;
- stock names, stock codes, and price values from controlled evidence;
- credentials, cookies, browser profiles, storage state, and tokens;
- stakeholder case IDs or sensitive investigative details.

Raw evidence remains in the approved controlled store. Git contains only redacted research records, hashes/counts, rule-family summaries, run indices, decision logs, and validation outcomes.

## Current Decision

Stakeholders selected `C2` on `2026-04-25`.

| Path | Status | Meaning |
|---|---|---|
| C1. Pause browser-session expansion and wait for confirmed pointers | Not selected now | Still the preferred future data path if reviewers request more final scam/high-risk examples. |
| C2. Use this as the current CIB/165-facing checkpoint package | Selected | Review and refine this 55-record report before any new collection. |
| C3. Open another browser-session tranche for calibration only | Not selected now | No browser-session tranche is currently authorized. |

The selected C2 path keeps collection paused. Any future C1 or C3 work requires a later decision record.

## Next Work Items

1. Review this report against `reports/checkpoint-0055-review-checklist.md`.
2. Fill remaining domain, legal/privacy, and technical review rows as reviewers respond.
3. Revise report language only for clarity, missing caveats, or stakeholder questions.
4. Keep item `0056` blocked unless a later decision records a new bounded collection scope.
