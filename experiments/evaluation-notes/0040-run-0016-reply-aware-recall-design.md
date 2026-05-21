# Run 0016 Reply-Aware Recall Design

## Purpose

Record the repo-safe design note for `CRAWL-THREADS-PILOT-V1-0016`, the next bounded run before item `0024`.

This note contains no raw Threads content, item URLs, handles, screenshots, cookies, tokens, browser profiles, HAR files, raw visible text, raw storage paths, or sensitive investigative material.

## Design Change

Run 0016 changes the evidence strategy from post-first candidate review to reply-aware recall triage.

The reason is practical: scam-like evidence can appear in comments rather than the top-level post, including suspicious websites, scam links, LINE or other messaging-app links, add-friend links, wallet/deposit instructions, and private-channel migration.

The design also implements the CIB policy preference that false negatives are more costly than explainable false positives at the triage stage.

The design treats anti-scam wording as ambiguous when it appears together with an investment/profit funnel. Repeated claims such as hating or warning against scams do not lower risk by themselves if the same item or selected replies direct people toward investment paths, profit claims, links, messaging apps, add-friend flows, or contact handles.

## Limits

| Limit | Value |
|---|---|
| Total candidates reviewed | at most 20 |
| Per-family candidates reviewed | at most 4 |
| Selected items | at most 4 |
| Target items | `0024` through `0027` |
| Item `0028` | blocked |
| Reply/comment window | at most 3 selected relevant replies/comments per candidate |
| Raw/session material | controlled store only |
| Second review | required before selected items count |

## Evidence Families

| Family | Role |
|---|---|
| reply/comment private-channel or add-friend signal | catch comment-only migration paths |
| reply/comment wallet, deposit, or transfer signal | catch payment-risk paths |
| reply/comment contact handle or messaging-app migration | catch off-platform conversion |
| guarantee plus link/contact/comment signal | catch high-recall financial lures |
| earnings/proof screenshot plus link/contact/comment signal | catch testimonial-proof lures |
| anti-scam wording plus investment/profit funnel | catch camouflage patterns that could otherwise become false negatives |

## Decision

```text
open_run_0016_reply_aware_recall_design_before_item_0024
```

This design opens a preflight-ready run record. It does not start collection by itself.

## Required Before Execution

- Confirm approved browser/session or API/session-aware access readiness.
- Confirm checkpoint 0023 strict validation.
- Confirm controlled store is ready for raw reply/link/session artifacts.
- Execute with per-family candidate caps so no one seed consumes the entire run.
- Keep query terms as candidate-finding hints only.
- Build local records only after redaction.
- Strict-validate each local record and the aggregate.
- Second-review all selected items before counting.
