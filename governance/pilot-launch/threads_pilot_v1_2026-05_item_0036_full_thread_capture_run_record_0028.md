# Item 0036 Full Thread Capture Run Record 0028

Do not add raw Threads content, screenshots, full item URLs, raw handles, stakeholder case IDs, credentials, cookies, tokens, browser profiles, HAR files, full HTML, exact raw storage paths, access-list details, contact handles, or sensitive investigative notes to this file. Exact sensitive values remain in the approved controlled store.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `CAPTURE-THREADS-PILOT-V1-0036-FULL-THREAD` |
| Date | `2026-04-25` |
| Related item | `threads_pilot_v1_0036` |
| Related decision | `0048-record-reply-impersonation-contact-hijack-rule` |
| Operator | `AUTO-OP-01` |
| Purpose | preserve controlled raw post/reply evidence for one confirmed scam pointer |
| Access path | approved Playwright Chromium browser session |
| Raw output location | controlled store only |
| Repo-visible raw output | no |

## Authorization And Scope

| Check | Result |
|---|---|
| CIB/project research authorization applies | yes |
| Item-specific source pointer approved | yes |
| Browser/session artifact approved | yes |
| Single-item limit | yes: item `0036` only |
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
| Visible text blocks | captured | 144 blocks |
| `[dir='auto']` text blocks | captured | 58 blocks |
| Hrefs | captured | 49 hrefs |
| `article` selector extraction | not available | selector returned 0; body/visible text blocks and screenshot were used |
| Poster identity/profile context | unavailable | source still preserved in controlled raw pointer; repo uses redacted controlled reference only if available |

## Accepted Capture Hashes

| Field | Value |
|---|---|
| HTML SHA-256 | `afb3da4851953cfeadb9847058850638232e6e6b88db47360bf0a9d68e627c37` |
| Body-text SHA-256 | `7d408ff0193b9025acf01201b9ea90835bb355deeb0d22dd094182d79f9f56f9` |

## Repo-Safe Style Families Observed

The controlled full-thread sample supports the `reply_impersonation_contact_hijack` rule and reinforces the importance of reply-level evidence.

Repo-safe style families observed:

- top-level trust-building and humble/no-benefit framing around stock sharing;
- follower gratitude and confidence-building replies;
- repeated reply-level contact/group redirection for daily lists or holdings viewpoints;
- official-contact or anti-scam camouflage claims around contact handles;
- attribution uncertainty: suspicious contact replies may be impersonation/hijack rather than the top-level poster's own reply.

## Limitation

The capture preserves the approved browser-rendered raw evidence visible to the approved session at capture time. Hidden, deleted, private, unavailable, or platform-restricted replies are not guaranteed to be preserved. Attribution of suspicious replies should remain explicit and cautious.

## Decision

Run 0028 satisfies the controlled raw evidence preservation step for item `0036`.

The repo may use redacted derived fields and the run/hash summary. Raw URL, raw handle, raw contact handles, raw post text, raw replies, HTML, screenshots, and source-session details remain outside git.
