# Controlled Crawler Rehearsal Run 0001

## Purpose

Record the repo-safe result of the first controlled low-speed crawler rehearsal before any first 10-15 item checkpoint begins.

This note contains no raw Threads content, item URLs, handles, screenshots, cookies, tokens, browser profiles, HAR files, raw headers, raw HTML, raw storage paths, or sensitive investigative material.

## Run Scope

| Field | Value |
|---|---|
| Run ID | `CRAWL-THREADS-PILOT-V1-0001` |
| Date | `2026-04-24` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Authorization basis | Decision 0018 and Decision 0022 |
| Run record | `governance/pilot-launch/threads_pilot_v1_2026-05_controlled_crawler_run_record_0001.md` |
| Seed set | Threads search seeds for `投資`, `賺錢`, `股票`, `虛擬貨幣`, and `加密貨幣` |
| Executed seed | Seed 1 only |
| Parallelism | 1 worker |
| Minimum delay | 30 seconds between fetches |
| Target item count | 1 selected controlled rehearsal item |

## Method Summary

1. Confirmed the controlled run record existed and limited run 0001 to seed 1.
2. Performed a static fetch of seed 1.
3. Observed a platform canonical redirect.
4. Waited at least 30 seconds.
5. Performed one static fetch of the canonical search page.
6. Reviewed only non-sensitive structural indicators from the returned HTML.
7. Stopped because no extractable candidate item was available.

## Non-Sensitive Observations

| Observation | Result |
|---|---|
| Initial seed response | 301 platform canonical redirect |
| Canonical search response | 200 HTML response |
| Page title | Threads search page |
| Login/captcha/403/429/platform warning observed | no |
| Session-related response artifact observed | yes; value kept outside git |
| Raw headers and HTML retained outside git | yes |
| Extractable post text fields found by static review | 0 |
| Candidate items reviewed | 0 |
| Selected items | 0 |
| Redacted item entered into `manual_entry_0001.json` | no |
| `manual_record_0001.json` built | no |
| Strict validation | not run because no record exists |

## Gate Result

The run did not produce one selected controlled rehearsal item. The project therefore cannot move to the first 10-15 item checkpoint.

The builder block is expected and correct: `data/interim/manual_entry_0001.json` is still an intake skeleton, so record build cannot proceed until an actual selected item is entered with approved redacted fields.

## Decision

```text
pause_for_collection_fix
```

## Rationale

- The controlled crawler path is authorized for this pilot, but run 0001 used only the narrow seed-1 static fetch path.
- Static search retrieval returned a dynamic search page shell with no extractable candidate item.
- No redacted item exists, so the project cannot assess redaction burden, schema fit, evidence sufficiency, annotation boundary behavior, or checkpoint readiness.
- Raw response data and session-related artifacts stayed outside git.
- The first 10-15 item checkpoint remains blocked until one selected rehearsal item is built, strict-validated, and reviewed.

## Next Action

Before any additional collection, update the controlled run path for exactly one of these options:

- test one reserve seed at the same low rate and the same stop conditions
- use the already authorized browser-rendered/API/session-aware path with explicit session, rendering, raw-output, and redaction controls

Do not start the first 10-15 item checkpoint until the aggregate rehearsal review records either `pass_ready_for_calibration_or_first_10_15` or `pass_with_limits`.
