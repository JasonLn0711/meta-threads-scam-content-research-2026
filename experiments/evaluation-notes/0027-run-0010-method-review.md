# Run 0010 Method Review

## Purpose

Record the repo-safe method review after run 0010 attempted all five planned browser-session risk-probe seeds for item 0017 and selected no safe redacted item.

This note contains no raw Threads content, item URLs, handles, screenshots, cookies, tokens, browser profiles, HAR files, raw visible text, raw storage paths, credential values, or sensitive investigative material.

## Run Summary

| Check | Result |
|---|---|
| Access path | approved browser storage-state/session-aware path |
| Target item | `threads_pilot_v1_0017` |
| Seeds attempted | 5 |
| Candidates reviewed | 25 total; 5 per seed |
| Selected item 0017 | no |
| `manual_entry_0017.json` created | no |
| Raw/session material in git | no |
| Stop condition | method-review gate after seed matrix exhausted |

## Aggregate Candidate Diagnostics

Controlled-store raw files were reviewed only for aggregate metadata. No raw candidate text is copied here.

| Seed | Candidates reviewed | Negation/risk-warning count | Selectable by current rule | Visible signal-family metadata |
|---|---:|---:|---:|---|
| `RP-0010-01` | 5 | 0 | 0 | none detected |
| `RP-0010-02` | 5 | 0 | 0 | `guaranteed_outcome`: 2 |
| `RP-0010-03` | 5 | 0 | 0 | none detected |
| `RP-0010-04` | 5 | 0 | 0 | `wallet_or_deposit`: 1 |
| `RP-0010-05` | 5 | 0 | 0 | `private_channel`: 1 |

## Interpretation

Run 0010 did not fail because the approved browser session was unavailable. It failed because the current seed matrix and selection rule produced single-signal or no-signal candidates, while the run required a safe, reviewable item with stronger visible evidence before creating item 0017.

The negation filter did not block the run. The more important bottleneck is low co-occurrence of signal families in the retained candidate text.

## Method Issues

| Issue | Evidence | Decision implication |
|---|---|---|
| Low multi-signal yield | No seed produced a candidate selectable by the current rule. | Do not keep retrying the same matrix. |
| Signal families appear separately | Some seeds surfaced isolated `guaranteed_outcome`, `wallet_or_deposit`, or `private_channel` metadata. | Combine terms more deliberately or relax into a staged candidate-review design. |
| Text-only visible search results may be too narrow | No selected item after 25 candidates despite approved session access. | Consider whether replies, image/OCR, links, or profile context are required, but do not collect them without a new run record. |
| Current rule may be too strict for discovery | Single-signal candidates are rejected before local record creation. | Add a diagnostic-candidate stage before deciding whether an item is reviewable. |

## Decision

```text
pause_item_0017_collection_and_open_method_revision_before_run_0011
```

## Recommended Next Method

Open a new run record before any further item 0017 attempt. The new run should be a method-revision run, not a direct continuation of run 0010.

Required changes:

- Separate candidate diagnostics from item selection.
- Allow a repo-safe aggregate diagnostic pass over up to 5 candidates per seed before item creation.
- Use seed pairs that intentionally combine two visible signal families, such as private-channel plus deposit, private-channel plus testimonial, or urgency plus wallet/deposit.
- Keep query terms as retrieval hints only; they still cannot become labels.
- Keep raw candidate text, URLs, handles, screenshots, cookies, and session material outside git.
- Do not add replies, screenshots/OCR, landing pages, redirects, or profile context unless the new run record explicitly authorizes those fields.

## Blocked Actions

- Do not advance to item 0018.
- Do not create `manual_entry_0017.json` from query terms alone.
- Do not rerun the same five run 0010 seeds without a method change.
- Do not expand to the full 50-item pilot from this result.

## Next Allowed Action

Create run 0011 as a method-revision run for item 0017. It should validate the revised candidate-diagnostic design first, then attempt at most one item 0017 only if a candidate is reviewable under the approved field allowlist.
