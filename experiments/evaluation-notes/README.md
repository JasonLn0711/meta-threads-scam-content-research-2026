# Evaluation Notes

Use this directory for metric summaries, reviewer burden analysis, error reviews, ambiguity notes, and phase-narrowing evidence.

## Current Protocols

| File | Purpose |
|---|---|
| `0001-pilot-error-analysis-template.md` | Error-analysis structure for false positives, false negatives, and uncertainty. |
| `0002-annotation-agreement-protocol.md` | Agreement and disagreement review protocol. |
| `0003-pilot-decision-analysis-protocol.md` | Protocol for turning pilot results into expand/revise/narrow/pause decision. |
| `0004-pilot-result-synthesis-workbench.md` | Aggregate-only synthesis workflow for result summary and decision memo drafts. |
| `0005-review-packet-workflow.md` | Local-only item packet workflow for baseline error and threshold review. |
| `0006-manual-collection-assistant-smoke.md` | Synthetic smoke test for manual-only record building and governance checks. |
| `0007-phase1-pilot-launch-readiness.md` | Operational readiness note for governed Phase 1 launch gates. |
| `0008-phase1-synthetic-launch-rehearsal.md` | Synthetic-only integrated rehearsal of manual build, validation, calibration, audit, baseline, packets, and synthesis. |
| `0009-first-10-15-real-pilot-start-note.md` | Repo-safe start note for the first governed 10-15 real-item checkpoint. |
| `0010-manual-rehearsal-intake-gate-check.md` | Repo-safe gate check proving pending manual rehearsal intake cannot generate a real record. |
| `0011-approved-placeholder-gate-check.md` | Repo-safe gate check proving approved manual rehearsal intake with unresolved placeholders cannot generate a real record. |
| `0012-synthetic-calibration-guideline-revision.md` | Repo-safe note recording calibration-driven guideline and answer-key revisions before real-item expansion. |
| `0013-controlled-rehearsal-boundary-watchlist.md` | Repo-safe watchlist for the first 1-2 controlled real rehearsal items after the calibration-driven guideline revision. |
| `0014-controlled-rehearsal-review-protocol.md` | Repo-safe bridge from the 1-2 item rehearsal to the first 10-15 item checkpoint decision. |
| `0015-controlled-crawler-rehearsal-run-0001.md` | Repo-safe result note for the first seed-1 controlled crawler rehearsal and its no-extractable-item stop condition. |
| `0016-controlled-browser-rehearsal-run-0002.md` | Repo-safe result note for the first browser-rendered rehearsal that produced one strict-valid local record. |
| `0017-first-10-item-checkpoint-start.md` | Repo-safe start note for the first 10-item checkpoint under run-0002 limits. |
| `0018-first-10-item-checkpoint-result.md` | Repo-safe aggregate result and `continue_with_limits` decision for the first 10-item checkpoint. |
| `0019-first-15-item-limited-extension-result.md` | Repo-safe aggregate result for the item 11-15 limited extension and source-strategy gate before item 16. |
| `0020-high-risk-case-finding-method-study.md` | Repo-safe method-study design for finding higher-risk cases without uncontrolled scraping or label leakage. |
| `0021-risk-probe-run-0005-result.md` | Repo-safe result note for the multi-term risk-probe run that returned no extractable item content. |
| `0022-risk-probe-run-0006-result.md` | Repo-safe result note for the normalized no-space risk-probe retry that also returned no extractable item content. |
| `0023-access-path-review-run-0007-result.md` | Repo-safe result note for the approved session/API access-path review before item 16. |
| `0024-access-path-preparation-run-0008-result.md` | Repo-safe result note for preparing browser storage-state and API/session-aware paths before item 16. |
| `0025-browser-session-run-0009-result.md` | Repo-safe result note for the approved browser-session run that produced strict-valid item 0016. |
| `0026-browser-session-limited-extension-run-0010-start.md` | Repo-safe start note for the item 0017-0020 limited extension with negation/risk-warning candidate filtering. |
| `0027-run-0010-method-review.md` | Repo-safe method review after all five run 0010 seeds failed to produce item 0017. |
| `0028-run-0011-method-revision-start.md` | Repo-safe start note for the item 0017 method-revision diagnostic run. |
| `0029-item-0017-second-review.md` | Repo-safe second-review note excluding item 0017 because retained visible text was only a query echo. |
| `0030-item-0017-evidence-path-study-start.md` | Repo-safe start note for deciding the next evidence path after text-only item 0017 methods failed. |
| `0031-evidence-path-study-decision.md` | Repo-safe evidence-path decision selecting run 0012 design boundaries. |
| `0032-run-0012-evidence-path-design-start.md` | Repo-safe start note for the design-only run 0012 scoped evidence-path boundaries. |
| `0033-run-0013-scoped-execution-start.md` | Repo-safe start note for the future single item 0017 scoped evidence execution attempt. |
| `0034-run-0013-method-review.md` | Repo-safe method review stopping the item 0017 extension for the current pilot tranche after the scoped evidence path found no reviewable candidate. |
| `0035-pilot-synthesis-after-item-0017-stop.md` | Repo-safe checkpoint addendum preparing stakeholder evidence-scope review after the accepted dataset remained at 16 records. |
| `0036-run-0015-preflight.md` | Repo-safe preflight showing run 0015 is ready for browser/session execution while the API path remains blocked. |
| `0037-run-0015-execution-result.md` | Repo-safe execution result for run 0015: 20 candidates reviewed, 6 local records built, strict-valid checkpoint 0023, second review pending. |
| `0038-run-0015-second-review.md` | Repo-safe second-review result for items 0018-0023, finalizing 4 non-scam false-positive pressure cases and 2 uncertain boundary cases. |
| `0039-checkpoint-0023-interpretation.md` | Repo-safe 23-record checkpoint interpretation closing run 0015 for collection and requiring a new run design before item 0024. |
| `0040-run-0016-reply-aware-recall-design.md` | Repo-safe design note opening run 0016 as a bounded reply/comment-aware recall run before item 0024. |
| `0041-run-0016-preflight.md` | Repo-safe preflight showing run 0016 is ready for browser/session execution while the API path remains blocked. |
| `0042-run-0016-execution-result.md` | Repo-safe execution result for run 0016: 20 candidates reviewed across all five families, 4 local records built, strict-valid checkpoint 0027, second review pending. |
| `0043-run-0016-second-review.md` | Repo-safe second-review result for items 0024-0027, finalizing 2 non-scam false-positive pressure cases and 2 uncertain boundary cases. |

Generated local synthesis and packet outputs belong under `experiments/evaluation-notes/outputs/`, which is ignored by git.
