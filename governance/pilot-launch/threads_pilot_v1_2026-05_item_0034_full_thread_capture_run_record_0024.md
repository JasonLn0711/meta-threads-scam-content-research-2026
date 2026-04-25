# Item 0034 Full Thread Capture Run Record 0024

Do not add raw Threads content, screenshots, full item URLs, raw handles, stakeholder case IDs, credentials, cookies, tokens, browser profiles, HAR files, full HTML, exact raw storage paths, access-list details, or sensitive investigative notes to this file. Exact sensitive values remain in the approved controlled store.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `CAPTURE-THREADS-PILOT-V1-0034-FULL-THREAD` |
| Date | `2026-04-25` |
| Related item | `threads_pilot_v1_0034` |
| Related decision | `0036-adopt-confirmed-scam-pointer-intake-method` |
| Operator | `AUTO-OP-01` |
| Purpose | preserve controlled raw post/reply evidence and top-level poster context for one confirmed scam pointer |
| Access path | approved Playwright Chromium browser session |
| Raw output location | controlled store only |
| Repo-visible raw output | no |

## Authorization And Scope

| Check | Result |
|---|---|
| CIB/project research authorization applies | yes |
| Item-specific source pointer approved | yes |
| Browser/session artifact approved | yes |
| Single-item limit | yes: item `0034` only |
| Broad search or crawler expansion | no |
| Private-message access | no |
| Profile graph capture | no |
| Top-level poster ID/profile context | yes: controlled-store only; repo-safe redacted reference fields only |
| Landing-page or redirect-chain capture | no |
| Raw output in git | no |

## Captured Controlled Artifacts

| Artifact type | Status | Repo-safe detail |
|---|---|---|
| Source pointer | captured | controlled-store source reference exists |
| Top-level poster ID/profile context | captured | controlled-store only; repo-safe records use `poster_threads_id_ref` and category signals |
| Browser-rendered body text | captured | controlled store only |
| Browser-rendered HTML | captured | SHA-256 recorded below |
| Screenshot | captured | controlled store only |
| Visible text blocks | captured | 128 blocks |
| `[dir='auto']` text blocks | captured | 58 blocks |
| Hrefs | captured | 50 hrefs |
| `article` selector extraction | not available | selector returned 0; body/visible text blocks and screenshot were used |

## Accepted Capture Hashes

| Field | Value |
|---|---|
| HTML SHA-256 | `3440bd926445470660302770cc65d7b149e12a044b5bda2038ff94a9061bc60a` |
| Body-text SHA-256 | `f67bc7c4b920a0c61809a124f9f4b55fc4d2612b46808862dbf90f0251aa5500` |

## Limitation

The capture preserves the approved browser-rendered raw evidence visible to the approved session at capture time. Threads displayed that some newly added replies could not be shown, so unavailable, hidden, deleted, private, or platform-restricted replies are not guaranteed to be preserved.

## Decision

Run 0024 satisfies the controlled raw evidence preservation step for item `0034`.

The repo may use redacted derived fields, poster identity reference status/category fields, and the run/hash summary. Raw URL, raw handle, raw poster Threads ID, raw profile URL, raw post text, raw replies, HTML, screenshots, and source-session details remain outside git.
