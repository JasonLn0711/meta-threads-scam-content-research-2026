# Item 0028 Full Thread Capture Run Record 0018

Do not add raw Threads content, screenshots, full item URLs, raw handles, stakeholder case IDs, credentials, cookies, tokens, browser profiles, HAR files, full HTML, exact raw storage paths, access-list details, or sensitive investigative notes to this file. Exact sensitive values remain in the approved controlled store.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `CAPTURE-THREADS-PILOT-V1-0028-FULL-THREAD` |
| Date | `2026-04-25` |
| Related item | `threads_pilot_v1_0028` |
| Related intake | `EXEMPLAR-THREADS-PILOT-V1-0017` |
| Related decision | `0035-record-cib-confirmed-implicit-dm-funnel-rule` |
| Operator | `AUTO-OP-01` |
| Purpose | preserve controlled raw post/reply evidence for one CIB-confirmed targeted exemplar |
| Access path | approved Playwright Chromium browser session |
| Raw output location | controlled store only |
| Repo-visible raw output | no |

## Authorization And Scope

| Check | Result |
|---|---|
| CIB authorization applies | yes |
| Item-specific source pointer approved | yes |
| Browser/session artifact approved | yes |
| Single-item limit | yes: item `0028` only |
| Broad search or crawler expansion | no |
| Private-message access | no |
| Profile graph capture | no |
| Landing-page or redirect-chain capture | no |
| Raw output in git | no |

## Captured Controlled Artifacts

| Artifact type | Status | Repo-safe detail |
|---|---|---|
| Source pointer | captured | controlled-store source reference exists |
| Browser-rendered body text | captured | controlled store only |
| Browser-rendered HTML | captured | SHA-256 recorded below |
| Screenshot | captured | controlled store only |
| Visible text blocks | captured | 134 blocks in accepted capture |
| `[dir='auto']` text blocks | captured | 54 blocks in accepted capture |
| Hrefs | captured | 39 hrefs in accepted capture |
| `article` selector extraction | not available | selector returned 0; body/visible text blocks and screenshot were used |

## Run Attempts

| Attempt | Result | Notes |
|---|---|---|
| Attempt 1 | partial | A broad button-expansion routine opened a post-activity modal. Raw artifact retained as partial/obscured controlled evidence only. |
| Attempt 2 | accepted | No broad clicking; overlay closed with Escape; page scrolled and visible thread text, HTML, hrefs, and screenshot were captured. |

## Accepted Capture Hashes

| Field | Value |
|---|---|
| HTML SHA-256 | `cf96a688461656d83b30ba26344afce5378415c2bdae5fe35d56455643bf83df` |
| Body-text SHA-256 | `6816b53340e8c750833d64b32c2e6712e2b896a0970d9f89a5b10a8c8fa17e8c` |

## Limitation

The accepted screenshot showed the browser-rendered page and visible reply thread. Threads also displayed that some newly added replies could not be shown. Therefore, this run preserves the full browser-rendered raw evidence that was accessible to the approved session at capture time, but it does not guarantee recovery of unavailable, hidden, deleted, private, or platform-restricted replies.

## Decision

Run 0018 satisfies the controlled raw evidence preservation step for item `0028`.

The repo may use redacted derived fields and the run/hash summary. Raw URL, raw handle, raw post text, raw replies, HTML, screenshots, and source-session details remain outside git.
