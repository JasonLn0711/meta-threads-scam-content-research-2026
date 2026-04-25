# Checkpoint 0027 Interpretation

## Purpose

Record the repo-safe aggregate interpretation after run 0016 completed second review for items `0024` through `0027`.

This note contains no raw Threads content, item URLs, handles, screenshots, cookies, tokens, browser profiles, HAR files, raw visible text, raw reply text, raw storage paths, or sensitive investigative material.

## Checkpoint Scope

| Field | Value |
|---|---|
| Checkpoint ID | `CHK-THREADS-PILOT-V1-0027` |
| Date | `2026-04-25` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Local records in checkpoint file | 27 |
| Non-excluded records | 26 |
| Excluded method-review traces | 1 |
| Latest run record | `CRAWL-THREADS-PILOT-V1-0016` |
| Collection path | approved browser/session path |
| Candidate cap in latest run | 20 candidates total; 4 per evidence family |
| Selected item cap in latest run | 4 items total |

## Validation Result

| Check | Result |
|---|---|
| Checkpoint JSONL strict validation | pass |
| Strict-validation errors | 0 |
| Strict-validation warnings | 0 |
| Pilot preflight after commit | pass; 21 OK, 0 WARN, 0 ERROR |
| Raw evidence stayed outside git | yes |
| Source URLs, handles, raw comments, screenshots, and session artifacts in git | no |

## Aggregate Distribution

| Dimension | Count |
|---|---:|
| Total strict-valid local records | 27 |
| Non-excluded records | 26 |
| Excluded method-review trace | 1 |
| Final `scam` | 0 |
| Final `non_scam` | 21 |
| Final `uncertain` | 5 |
| Final low risk | 22 |
| Final medium risk | 4 |
| Final high risk | 0 |
| Visible external-link signal | 10 |
| Private-channel redirect signal | 8 |
| Contact-handle signal | 7 |
| Payment/deposit signal | 1 |
| Guaranteed or risk-free claim signal | 2 |
| Unrealistic profit or benefit signal | 2 |
| Vague offer strong-benefit signal | 1 |

## Interpretation

Run 0016 improved the evidence-search method. The per-family cap prevented a single seed from consuming the whole candidate budget, and the reply-aware recall path surfaced more link, contact, private-channel, and payment/deposit signals than earlier runs.

The composition problem is still not solved. The checkpoint still has no final `scam` labels and no final high-risk records. The new value is mainly high-recall triage pressure, false-positive calibration, and medium-risk uncertainty boundaries.

This does not mean the method failed. It means the current browser/session search-result path is better at finding risk-relevant boundaries than confirmed high-risk scam-like examples. The next step should revise the acquisition strategy, not simply extend the same run.

Run 0016 cannot continue under its existing limits. It used all 20 candidate reviews, selected all 4 allowed items, and its target range stopped at item `0027`.

## Decision

```text
close_run_0016_for_collection_and_require_method_decision_before_item_0028
```

## Required Before Item 0028

- Open a new decision or run record before item `0028`.
- Decide whether the next step is another bounded collection run, a method review, stakeholder handoff, API-path completion, or a pause.
- Preserve per-family candidate caps if continuing collection.
- Keep narrow reply/comment evidence, anti-scam camouflage handling, and CIB false-negative preference in the next design.
- Add a concrete plan for reaching higher-risk evidence, not just more low/medium uncertainty boundaries.
- Keep query terms as candidate-finding hints only; do not convert seed terms into labels.
- Continue second-review routing for all `uncertain`, low-confidence, high-risk, anti-scam-camouflage, private-channel, link/redirect, OCR, screenshot, reply-context, or profile-context items.
- Keep raw/session/candidate artifacts outside git.
