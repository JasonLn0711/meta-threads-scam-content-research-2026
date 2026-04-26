# Items 0077-0079 Full-Thread Capture Work Order 0049

Do not add raw Threads content, screenshots, full item URLs, raw handles, stakeholder case IDs, credentials, cookies, tokens, browser profiles, HAR files, full HTML, exact raw storage paths, access-list details, stock names, stock codes, price values, or sensitive investigative notes to this file. Exact sensitive values remain in the approved controlled store.

## Work Order Identity

| Field | Value |
|---|---|
| Work order ID | `CAPTURE-THREADS-PILOT-V1-0077-0079-FULL-THREAD` |
| Date | `2026-04-26` |
| Related decision | `0100-authorize-0077-0079-full-thread-capture-work-order` |
| Items | `threads_pilot_v1_0077`, `threads_pilot_v1_0078`, `threads_pilot_v1_0079` |
| Operator | `AUTO-OP-01` |
| Purpose | complete controlled full-thread/reply readiness for three preliminary confirmed pointers |
| Access path | controlled browser-rendered/session-aware path |
| Raw output location | controlled store only |
| Repo-visible raw output | no |

## Scope Controls

| Check | Requirement |
|---|---|
| Item cap | exactly `0077-0079` |
| New source discovery | no |
| Search-query run | no |
| Broad crawler expansion | no |
| Account/profile graph capture | no |
| Private-message access | no |
| Landing-page or redirect-chain capture | no |
| Raw output in git | no |

## Item Work Queue

| Item | Current rule family | Capture status | Reply/comment status | Promotion status |
|---|---|---|---|---|
| `0077` | `supply_chain_insider_stock_lure` | `capture_pending` | `reply_capture_pending` | manual entry blocked |
| `0078` | `hidden_stock_code_past_performance_lure` | `capture_pending` | `reply_capture_pending` | manual entry blocked |
| `0079` | `hidden_stock_code_past_performance_lure` + `comment_code_lead_magnet` | `capture_pending` | `reply_capture_pending` | manual entry blocked |

## Required Item-Level Fields After Capture

For each item, record repo-safe outcomes only:

- capture succeeded / failed / unavailable;
- top-level post captured in controlled store: yes/no;
- replies/comments captured in controlled store: yes/no/unavailable;
- controlled artifact hashes if available;
- redacted rule-family summary;
- second-review result;
- manual entry build decision;
- strict-validation result if a manual record is built.

## Manual Build Gate

Do not build `manual_entry_0077.json`, `manual_entry_0078.json`, or `manual_entry_0079.json` until:

1. controlled capture is complete or unavailability is documented;
2. reply/comment context is summarized in redacted form;
3. second review confirms label, risk, and evidence sufficiency;
4. raw evidence remains outside git;
5. repo-safe fields can pass strict validation.

## Current Status

Work order opened. No full-thread capture attempt is recorded here yet.
