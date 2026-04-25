# Account Source Capture Run Record 0026

Do not add raw Threads content, screenshots, full account URLs, raw handles, raw post URLs, stakeholder case IDs, credentials, cookies, tokens, browser profiles, HAR files, full HTML, exact raw storage paths, access-list details, follower/following graph data, or sensitive investigative notes to this file. Exact sensitive values remain in the approved controlled store.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `CAPTURE-THREADS-ACCOUNT-SOURCE-V1-0002` |
| Date | `2026-04-25` |
| Account sample ID | `threads_account_source_v1_0002` |
| Related decision | `0045-record-account-multi-post-style-cluster-rule` |
| Operator | `AUTO-OP-01` |
| Purpose | test controlled account-level multi-post style sampling for one additional CIB-detected investment scam account |
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
| Visible text blocks | captured | 98 blocks |
| `[dir='auto']` text blocks | captured | 48 blocks |
| Hrefs | captured | 23 hrefs |
| Candidate post links | captured | 5 links; raw URLs stored only in controlled store; hashes available in raw controlled artifact |

## Accepted Capture Hashes

| Field | Value |
|---|---|
| HTML SHA-256 | `37324794ea575cdd895c2c0005cb760c52d940df5e62bf9ea4acef74239aa932` |
| Body-text SHA-256 | `0186139b78797fa9efcb49719243f6a91c2ed196454dfa66b86dbfddaea3146c` |

## Repo-Safe Style Families Observed

The controlled account sample supports the `account_multi_post_style_cluster` method. The sampled account page showed multiple candidate posts with at least these redacted style families:

- profile-level anti-scam / no-group / no-active-invitation disclaimer framing;
- unusually large profit proof and social-benefit framing tied to prior calls;
- group-like follower recognition and public gratitude around people who followed the call;
- strong belief / hold-tight / continue-accumulating operation language;
- market-sector keyword clustering around Taiwan stocks and trading.

These style families are candidate-selection context only. They do not automatically label every post under the account as `scam`.

## Limitation

The run captured only the browser-rendered account feed visible to the approved session at capture time. Hidden, deleted, private, unavailable, or platform-restricted posts/replies are not guaranteed to be preserved. Full-thread capture is still required before any individual candidate post becomes a dataset item.

## Decision

Run 0026 confirms that the account-level multi-post style cluster method generalizes beyond the first account sample. The next useful action is to choose one candidate post from this account for normal full-thread capture if the project wants to add it as an item-level record.
