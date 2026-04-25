# Account Source Capture Run Record 0025

Do not add raw Threads content, screenshots, full account URLs, raw handles, raw post URLs, stakeholder case IDs, credentials, cookies, tokens, browser profiles, HAR files, full HTML, exact raw storage paths, access-list details, follower/following graph data, or sensitive investigative notes to this file. Exact sensitive values remain in the approved controlled store.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `CAPTURE-THREADS-ACCOUNT-SOURCE-V1-0001` |
| Date | `2026-04-25` |
| Account sample ID | `threads_account_source_v1_0001` |
| Related decision | `0045-record-account-multi-post-style-cluster-rule` |
| Operator | `AUTO-OP-01` |
| Purpose | test controlled account-level multi-post style sampling for one CIB-detected investment scam account |
| Access path | approved Playwright Chromium browser session |
| Raw output location | controlled store only |
| Repo-visible raw output | no |

## Authorization And Scope

| Check | Result |
|---|---|
| CIB/project research authorization applies | yes |
| Account-specific source pointer approved | yes |
| Browser/session artifact approved | yes |
| Account sample limit | yes: one account source only |
| Candidate post cap | yes: 5 candidate post links |
| Broad search or crawler expansion | no |
| Private-message access | no |
| Follower/following graph capture | no |
| Landing-page or redirect-chain capture | no |
| Raw output in git | no |

## Captured Controlled Artifacts

| Artifact type | Status | Repo-safe detail |
|---|---|---|
| Account source pointer | captured | controlled-store source reference exists |
| Account identity/profile context | captured | controlled-store only; repo-safe records use redacted references and category signals |
| Browser-rendered body text | captured | controlled store only |
| Browser-rendered HTML | captured | SHA-256 recorded below |
| Screenshot | captured | controlled store only |
| Visible text blocks | captured | 139 blocks |
| `[dir='auto']` text blocks | captured | 64 blocks |
| Hrefs | captured | 27 hrefs |
| Candidate post links | captured | 5 links; raw URLs stored only in controlled store; hashes available in raw controlled artifact |

## Accepted Capture Hashes

| Field | Value |
|---|---|
| HTML SHA-256 | `eeabdd0ebafb218c38a7b72ba7561ca71b2f47822fecd6d3dfacf93b4384a6f9` |
| Body-text SHA-256 | `ce33d789563e39b193208e83f9377b878ab150d5b2e0b95a1bb7610555b315e3` |

## Repo-Safe Style Families Observed

The controlled account sample supports the `account_multi_post_style_cluster` method. The sampled account page showed multiple candidate posts with at least these redacted style families:

- profile-level free community / synchronized-operation / stock-question framing;
- past-performance and stock-picking proof language;
- strong market-direction and broad bullish framing;
- individualized operation language such as switching, buying, adding, holding, or continuing positions;
- follower/social-proof style engagement counts visible in the account feed.

These style families are candidate-selection context only. They do not automatically label every post under the account as `scam`.

## Limitation

The run captured only the browser-rendered account feed visible to the approved session at capture time. Hidden, deleted, private, unavailable, or platform-restricted posts/replies are not guaranteed to be preserved. Full-thread capture is still required before any individual candidate post becomes a dataset item.

## Decision

Run 0025 satisfies the first controlled account-level sampling rehearsal. The method is useful enough to keep as a candidate-generation path for CIB-detected accounts, subject to small caps and item-level validation.
