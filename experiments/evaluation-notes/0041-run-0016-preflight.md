# Run 0016 Preflight

## Purpose

Record the repo-safe pre-execution readiness check for `CRAWL-THREADS-PILOT-V1-0016`.

This note contains no raw Threads content, item URLs, handles, screenshots, cookies, tokens, browser storage state, API responses, raw output paths, or sensitive investigative material.

## Result

| Check | Result |
|---|---|
| Date | `2026-04-25` |
| Target item | `threads_pilot_v1_0024` |
| Browser/session path | ready |
| API/session-aware path | blocked |
| API blocker | `META_API_PROBE_URL` missing or empty |
| Checkpoint 0023 strict validation | pass; 23 checked, 0 errors, 0 warnings |
| Pilot preflight | pass; 21 OK, 0 WARN, 0 ERROR |
| Execution allowed now | browser/session only |

## Decision

```text
run_0016_browser_session_execution_ready_api_path_blocked
```

Run 0016 may execute only through the approved browser/session path unless the API path is later completed and rechecked.

## Required During Execution

- Keep total candidate reviews at or below 20.
- Keep per-family candidate reviews at or below 4.
- Select at most 4 items, `0024` through `0027`.
- Do not open item `0028`.
- Use the narrow reply/comment evidence lane only as authorized in the run record.
- Treat anti-scam wording plus investment/profit funnel signals as a recall-priority pattern.
- Keep raw/session/candidate artifacts outside git.
- Build only redacted local records, strict-validate them, and second-review selected items before counting.
