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

## Item 0017 Build Result

| Check | Result |
|---|---|
| Controlled-store reviewability gate | pass |
| `manual_entry_0017.json` created | yes; local-only ignored file |
| `manual_record_0017.json` built | yes; local-only ignored file |
| Item 0017 strict validation | pass; 1 record, 0 errors, 0 warnings |
| 17-record aggregate strict validation | pass; 17 records, 0 errors, 0 warnings |
| Preliminary label / risk | `uncertain` / `medium` |
| Preliminary signal summary | private-channel redirect plus wallet/deposit action |
| Raw/session material in git | no |

## Next Required Action After Build

Second-review item 0017 before any move to item 0018. The review should confirm redaction, the preliminary label/risk, and whether the visible retained fields are sufficient under the current approved field allowlist.

## Second-Review Result

| Check | Result |
|---|---|
| Second-review decision | excluded |
| Final label / risk | `insufficient_evidence` / `low` |
| Evidence sufficiency | `not_reviewable` |
| Reason | retained visible text was only a query echo, not independent item content |
| Item 0017 strict validation after update | pass; 1 record, 0 errors, 0 warnings |
| 17-record aggregate strict validation after update | pass; 17 records, 0 errors, 0 warnings |

## Next Required Action After Second Review

Patch the diagnostic gate to reject exact-query and near-query echoes before any further item 0017 attempt. Do not treat the excluded item 0017 trace as permission to advance to item 0018.

## Query-Echo Filter Retry Result

| Check | Result |
|---|---|
| Seed retried | `RP-0011-01` |
| Query echoes excluded | 1 |
| Candidates reviewed after filter | 4 |
| Reviewable candidates after filter | 0 |
| `manual_entry_0017.json` recreated | no |
| Raw/session material in git | no |

## Next Required Action After Filter Retry

Run only the next revised diagnostic seed, `RP-0011-02`, with the query-echo filter still enabled. Do not create item 0017 unless a non-query-echo candidate passes the reviewability gate.

## Second Revised Diagnostic Result

| Check | Result |
|---|---|
| Seed attempted | `RP-0011-02` |
| Query echoes excluded | 0 |
| Candidates reviewed | 5 |
| Negation/risk-warning count | 0 |
| Single-signal candidates | 2 |
| Multi-signal candidates | 1 |
| Reviewable candidates | 0 |
| Signal-family metadata | `crypto_domain`: 2; `testimonial`: 1; `wallet_or_deposit`: 1 |
| `manual_entry_0017.json` recreated | no |
| Raw/session material in git | no |

## Next Required Action After Second Revised Diagnostic

Run only the next revised diagnostic seed, `RP-0011-03`, with the query-echo filter still enabled. Do not create item 0017 unless a non-query-echo candidate passes the reviewability gate.

## Third Revised Diagnostic Result

| Check | Result |
|---|---|
| Seed attempted | `RP-0011-03` |
| Query echoes excluded | 0 |
| Candidates reviewed | 5 |
| Negation/risk-warning count | 0 |
| Single-signal candidates | 0 |
| Multi-signal candidates | 0 |
| Reviewable candidates | 0 |
| Signal-family metadata | none detected |
| `manual_entry_0017.json` recreated | no |
| Raw/session material in git | no |

## Next Required Action After Third Revised Diagnostic

Run only the final revised diagnostic seed, `RP-0011-04`, with the query-echo filter still enabled. Do not create item 0017 unless a non-query-echo candidate passes the reviewability gate.

## Fourth Revised Diagnostic Result

| Check | Result |
|---|---|
| Seed attempted | `RP-0011-04` |
| Query echoes excluded | 0 |
| Candidates reviewed | 5 |
| Negation/risk-warning count | 0 |
| Single-signal candidates | 0 |
| Multi-signal candidates | 0 |
| Reviewable candidates | 0 |
| Signal-family metadata | none detected |
| `manual_entry_0017.json` recreated | no |
| Raw/session material in git | no |

## Run 0011 Outcome

Run 0011 tested the revised candidate-diagnostic design, added a query-echo filter, and attempted all four revised seeds. The only local item 0017 trace was excluded after second review because it was query echo only. After the filter patch, no revised seed produced a reviewable candidate.

## Next Required Action After Run 0011

Pause collection again for method decision. Do not advance to item 0018. The next decision should choose whether to change the evidence scope, change acquisition path, revise candidate extraction beyond visible search-result text, or stop the item 0017 extension.
