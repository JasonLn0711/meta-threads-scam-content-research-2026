# Confirmed Pointer 0079 Preliminary Rule Result

## Purpose

Record the repo-safe preliminary rule learning from one stakeholder-supplied confirmed scam pointer.

This note does not include raw Threads URLs, handles, screenshots, raw post text, raw reply text, contact IDs, stock names, stock codes, price values, credentials, browser/session artifacts, exact controlled-store paths, or stakeholder case IDs.

## Result

| Field | Value |
|---|---|
| Related decision | `decision-log/0099-authorize-single-confirmed-pointer-0079-intake.md` |
| Related run record | `governance/pilot-launch/threads_pilot_v1_2026-05_item_0079_confirmed_pointer_intake_run_record_0048.md` |
| Prospective item | `threads_pilot_v1_0079` |
| Current status | preliminary rule extracted; full reply capture pending |
| Manual entry built | no |
| Manual record built | no |
| Strict validation | not applicable yet |

## Preliminary Signal Family

Primary:

- `hidden_stock_code_past_performance_lure`

Co-signal:

- `comment_code_lead_magnet`

Definition:

```text
Past buy/sell or stock-pick performance proof is used to establish trading authority, then the post teases an unnamed next stock, hidden code, or "number" as a high-value opportunity and asks readers to comment a keyword/phrase so the poster can share details individually.
```

## Observable Pattern Summary

The top-level post-level pattern combines:

- prior stock-pick or buy/sell performance proof;
- a hidden next-stock/code teaser;
- catalyst, technical, or market-structure claims;
- urgent value framing;
- a public comment-keyword gate for individualized follow-up.

This pattern is stronger than a generic stock-pick post because the public thread itself creates a lead magnet: readers are instructed to comment a keyword/phrase, after which details are promised individually.

## Reply/Comment Status

Reply/comment analysis is not complete. Static public metadata did not provide reliable full reply capture.

Required next step before item promotion:

- controlled browser-rendered/session-aware full-thread capture;
- redacted reply/comment summary;
- second review;
- manual entry/record build only if the capture is sufficient;
- strict validation if a manual record is built.

## Decision Implication

Do not add a broader schema tag yet. Use the existing `hidden_stock_code_past_performance_lure` plus `comment_code_lead_magnet` combination and update annotation guidance to mention keyword-gated variants.

Do not treat this preliminary result as a completed item `0079` record.
