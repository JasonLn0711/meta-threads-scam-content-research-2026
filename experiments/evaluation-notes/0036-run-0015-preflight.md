# Run 0015 Preflight

## Purpose

Record the repo-safe pre-execution readiness check for run 0015 after stakeholders approved all proposed evidence families with run-level limits.

This note contains no raw Threads content, item URLs, handles, screenshots, cookies, tokens, browser profiles, HAR files, raw visible text, raw storage paths, credential values, API responses, or sensitive investigative material.

## Run Scope

| Field | Value |
|---|---|
| Run ID | `CRAWL-THREADS-PILOT-V1-0015` |
| Target item range | `threads_pilot_v1_0018` through at most `threads_pilot_v1_0027` |
| Candidate review cap | 20 candidates |
| Selected item cap | 10 items |
| Item 0028 | blocked |
| Evidence scope | all proposed evidence families approved with run-level limits |

## Preflight Result

| Check | Result | Notes |
|---|---|---|
| Browser storage-state shape | ready | `cookies`, `origins`, cookie count, and origin count checks passed without printing values. |
| API dry-run readiness | not ready | Required API probe URL is missing or empty; do not use API path for run 0015. |
| Latest local aggregate strict validation | pass | 17 local records checked, 0 errors, 0 warnings. |
| Pilot preflight | pass | 21 OK, 0 WARN, 0 ERROR. |
| Controlled-store boundary | ready for browser path | Raw/session material remains outside git. |
| Second-review requirement | required before selected items count | Assign reviewer before counting any run 0015 selected item. |

## Decision

```text
browser_session_execution_ready_api_path_blocked
```

Run 0015 may proceed only through the approved browser/session path unless the API env is later completed and rechecked.

## Required Before Execution

- Use only the approved browser/session path for the next execution attempt.
- Keep raw screenshots, full OCR, full URLs, handles, replies, landing-page captures, redirect-chain details, profile details, cookies, browser/session material, API responses, and sensitive investigative notes outside git.
- Review at most 20 candidates.
- Select at most 10 items.
- Do not create item 0028 in this run.
- Build local redacted records only under ignored local files.
- Strict-validate every built record and the aggregate before any item counts.
- Second-review every selected item before it counts toward the pilot.
