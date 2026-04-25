# Checkpoint 0023 Interpretation

## Purpose

Record the repo-safe aggregate interpretation after run 0015 completed second review for items `0018` through `0023`.

This note contains no raw Threads content, item URLs, handles, screenshots, cookies, tokens, browser profiles, HAR files, raw visible text, raw storage paths, or sensitive investigative material.

## Checkpoint Scope

| Field | Value |
|---|---|
| Checkpoint ID | `CHK-THREADS-PILOT-V1-0023` |
| Date | `2026-04-25` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Local records in checkpoint file | 23 |
| Non-excluded records | 22 |
| Excluded method-review traces | 1 |
| Latest run record | `CRAWL-THREADS-PILOT-V1-0015` |
| Collection path | approved browser/session path |
| Candidate cap in latest run | 20 candidates total |
| Selected item cap in latest run | 10 items total |

## Validation Result

| Check | Result |
|---|---|
| Checkpoint JSONL strict validation | pass |
| Strict-validation errors | 0 |
| Strict-validation warnings | 0 |
| Pilot preflight after commit | pass; 21 OK, 0 WARN, 0 ERROR |
| Raw evidence stayed outside git | yes |
| Source URLs, handles, screenshots, and session artifacts in git | no |

## Aggregate Distribution

| Dimension | Count |
|---|---:|
| Total strict-valid local records | 23 |
| Non-excluded records | 22 |
| Excluded method-review trace | 1 |
| Final `scam` | 0 |
| Final `non_scam` | 19 |
| Final `uncertain` | 3 |
| Final low risk | 20 |
| Final medium risk | 2 |
| Final high risk | 0 |
| Visible external-link signal | 6 |
| Private-channel redirect signal | 4 |
| Contact-handle signal | 3 |
| Guaranteed or risk-free claim signal | 2 |
| Unrealistic profit or benefit signal | 2 |

## Interpretation

The pipeline is now stronger than the first 15-item checkpoint because it has exercised approved browser/session access, redacted link/category evidence, private-channel/contact signals, and second review for a richer evidence set.

The composition problem is not solved. The checkpoint still has no final `scam` labels and no final high-risk records. Most new value came from false-positive pressure cases and uncertainty-boundary cases, which are useful for calibration but not enough for high-risk scam-like evaluation.

Run 0015 cannot simply continue under the existing limits. It reviewed all 20 allowed candidates. Even though only 6 of the 10 selected-item slots were used, the candidate-review cap is already exhausted.

The next design must not evaluate only the top-level post. The project owner recorded that CIB policy treats comments/replies as important evidence because scam websites, scam links, LINE or other messaging-app links, add-friend links, and private-channel migration can appear in the comment area even when the post itself looks benign.

The next design must also reflect the CIB preference to avoid false negatives even at the cost of higher false positives. In this repo, that means high-recall triage and second-review routing, not legal accusation or production enforcement.

## Decision

```text
close_run_0015_for_collection_and_require_new_run_design_before_item_0024
```

## Required Before Item 0024

- Open a new run record or decision that explicitly defines the next candidate cap.
- Preserve the selected-item cap separately from the candidate-review cap.
- Rebalance the risk-probe seed matrix so one seed cannot consume the full candidate-review budget before later seed families are tested.
- Include a bounded, approved reply/comment evidence lane for candidate review when the run record allows it.
- Treat reply/comment links, add-friend instructions, private-channel migration, wallet/deposit instructions, and suspicious domains as high-priority recall signals.
- Keep query terms as candidate-finding hints only; do not convert seed terms into labels.
- Continue second-review routing for all `uncertain`, low-confidence, high-risk, negation-heavy, private-channel, link/redirect, OCR, screenshot, reply-context, or profile-context items.
- Keep raw/session/candidate artifacts outside git.
