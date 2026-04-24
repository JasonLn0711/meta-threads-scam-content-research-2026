# First 15-Item Limited Extension Result

## Purpose

Record the repo-safe aggregate result of the item 11-15 limited extension after the first 10-item checkpoint decision `continue_with_limits`.

This note contains no raw Threads content, item URLs, handles, screenshots, cookies, tokens, browser profiles, HAR files, raw visible text, raw storage paths, or sensitive investigative material.

## Extension Scope

| Field | Value |
|---|---|
| Checkpoint ID | `CHK-THREADS-PILOT-V1-0015` |
| Date | `2026-04-24` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Local records reviewed | 15 |
| New local records in extension | 5 |
| Run record | `CRAWL-THREADS-PILOT-V1-0004` |
| Collection path | browser-rendered, one item at a time |
| Candidate cap | at most 5 candidates per selected item |
| Delay | 30 seconds between page/object fetches |

## Validation Result

| Check | Result |
|---|---|
| Local records built | 15 total |
| 15-record JSONL strict validation | pass |
| 15-record CSV strict validation | pass |
| Strict-validation errors | 0 |
| Strict-validation warnings | 0 |
| Collection log rows | 15 item rows |
| Raw evidence stayed outside git | yes |
| Source URLs, handles, screenshots, and session artifacts in git | no |

## Second-Review Result

| Item class | Result |
|---|---|
| Prior checkpoint `uncertain` item | second-reviewed and adjudicated to final `non_scam` / `low` |
| New limited-extension boundary item | second-reviewed and adjudicated to final `uncertain` / `low` |
| Unresolved second-review items before item 16 | 0 |

## Aggregate Distribution

| Dimension | Count |
|---|---:|
| `scam` | 0 |
| `non_scam` | 14 |
| `uncertain` | 1 |
| `insufficient_evidence` | 0 |
| low risk | 15 |
| medium/high risk | 0 |
| text-only | 14 |
| visible private-message boundary | 1 |
| visible external links | 0 |
| OCR-relevant items | 0 |
| reply/comment context | 0 |

## Extension Finding

The collection, redaction, local build, strict validation, and second-review flow are working for the current browser-rendered text-first path.

The extension did not solve the composition problem. Topic-only search seeds continue to produce low-risk comparator or boundary content, not high-risk scam-like cases. The current sample cannot support high-risk baseline evaluation or a move to broad 50-item completion.

## Decision

```text
continue_with_limits
```

This means the project may continue only into source-strategy and risk-probe design work. It does not mean item 16 should start under the same topic-only seed method.

## Required Before Item 16

- Record a high-risk case-finding method study.
- Open a new run record if using risk-probe seeds, API/session-aware search, screenshots, OCR, replies, links, redirects, landing pages, or any new source/context.
- Keep one browser-rendered item at a time unless a later decision explicitly changes the limit.
- Review at most 5 candidates per selected item.
- Strict-validate every local record before counting it.
- Keep raw visible text, screenshots, source URLs, handles, cookies, browser profiles, and session artifacts out of git.
- Route all `uncertain`, low-confidence, and high-risk items to second review before the next gate.

## Follow-Up

Proceed to approved session/API risk-probe access review before item 16. The initial high-risk case-finding method study and public browser-rendered risk-probe runs did not produce extractable item content. Do not complete the 50-item pilot until a later checkpoint decision records that source mix, content-form mix, and evidence mix are adequate.
