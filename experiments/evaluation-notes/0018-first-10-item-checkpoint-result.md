# First 10-Item Checkpoint Result

## Purpose

Record the repo-safe aggregate result of the first 10-item checkpoint.

This note contains no raw Threads content, item URLs, handles, screenshots, cookies, tokens, browser profiles, HAR files, raw visible text, raw storage paths, or sensitive investigative material.

## Checkpoint Scope

| Field | Value |
|---|---|
| Checkpoint ID | `CHK-THREADS-PILOT-V1-0010` |
| Date | `2026-04-24` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Local records reviewed | 10 |
| Run records | run 0002 and run 0003 |
| Collection path | browser-rendered, one item at a time |
| Candidate cap | at most 5 candidates per selected item |

## Validation Result

| Check | Result |
|---|---|
| Local records built | 10 |
| Checkpoint JSONL strict validation | pass |
| Strict-validation errors | 0 |
| Strict-validation warnings | 0 |
| Collection log rows | 10 item rows |
| Raw evidence stayed outside git | yes |
| Source URLs, handles, screenshots, and session artifacts in git | no |

## Aggregate Distribution

| Dimension | Count |
|---|---:|
| `scam` | 0 |
| `non_scam` | 9 |
| `uncertain` | 1 |
| `insufficient_evidence` | 0 |
| low risk | 10 |
| text-only | 10 |
| needs second review | 1 |
| visible links or redirection signals | 0 |
| OCR-relevant items | 0 |
| reply/comment context | 0 |

## Checkpoint Finding

The collection and redaction pipeline is working for text-only browser-rendered search-result items. Every local record built and strict-validated.

The checkpoint is not broad readiness evidence. The first 10 records are skewed toward low-risk, text-only, manual-public/manual-capture items. The run did not test higher-risk scam-like examples, screenshots, OCR, visible links, redirect handling, reply/comment context, landing pages, or profile context.

## Decision

```text
continue_with_limits
```

## Required Limits Before Item 16

- Continue one browser-rendered item at a time.
- Review at most 5 candidates per selected item.
- Strict-validate every local record before counting it.
- Keep raw visible text, screenshots, source URLs, handles, cookies, browser profiles, and session artifacts out of git.
- Do not capture profile graph, landing pages, redirect chains, broad comments, screenshots, or OCR unless a later run record explicitly authorizes the field.
- Treat source skew as a checkpoint finding; try to improve risk mix within approved query/source limits, but do not force risk mix by adding unapproved context.
- Route the `uncertain` item and any later low-confidence or high-risk item to second review.

## Follow-Up

Proceed only to the limited item 11-15 checkpoint extension or the next controlled tranche under the limits above. Do not complete the 50-item pilot until a later checkpoint decision records that the composition and evidence mix are adequate.
