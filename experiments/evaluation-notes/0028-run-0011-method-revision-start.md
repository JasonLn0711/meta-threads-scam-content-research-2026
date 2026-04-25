# Run 0011 Method Revision Start

## Purpose

Record the repo-safe start condition for run 0011, a method-revision run required before any further item 0017 attempt.

This note contains no raw Threads content, item URLs, handles, screenshots, cookies, tokens, browser profiles, HAR files, raw visible text, raw storage paths, credential values, or sensitive investigative material.

## Start Condition

| Check | Result |
|---|---|
| Prior run | run 0010 completed with no selected item |
| Prior dataset state | 16 strict-valid local records |
| Item 0017 | not created |
| Main blocker | candidate-generation and evidence design, not access readiness |
| Required change | separate candidate diagnostics from item selection |
| Raw/session material in git | prohibited |

## Method Revision

Run 0011 changes the workflow from immediate selection to staged diagnostics:

1. Check access readiness.
2. Review up to 5 candidates for a revised seed.
3. Record only aggregate signal metadata.
4. Decide whether one candidate is reviewable under the current field allowlist.
5. Create at most one local item 0017 only if the reviewability gate passes.

## Revised First Seed

| Probe ID | Purpose | Query seed | Max candidates reviewed |
|---|---|---|---:|
| `RP-0011-01` | test private-channel plus wallet/deposit co-occurrence in crypto context | `加密貨幣錢包私訊LINE` | 5 |

## Decision

```text
open_run_0011_method_revision_but_execute_diagnostic_pass_only_first
```

## Required Before Execution

- Re-check approved browser storage-state readiness.
- Strict-validate the existing 16-record local aggregate.
- Confirm `manual_entry_0017.json` is absent.
- Run only `RP-0011-01` diagnostic pass first.
- Keep raw candidate text, URLs, handles, screenshots, cookies, and session material outside git.
- Do not advance to item 0018.

## First Diagnostic Result

| Check | Result |
|---|---|
| Seed attempted | `RP-0011-01` |
| Candidates reviewed | 5 |
| Negation/risk-warning count | 0 |
| Single-signal candidates | 2 |
| Multi-signal candidates | 1 |
| Reviewable candidates | 1 |
| Signal-family metadata | `crypto_domain`: 1; `private_channel`: 1; `wallet_or_deposit`: 3 |
| `manual_entry_0017.json` created | no |
| Raw/session material in git | no |

## Next Required Action

Review the controlled-store candidate outside git before building item 0017. Build `manual_entry_0017.json` only if the candidate can be reduced to approved redacted fields under the run 0011 field allowlist.
