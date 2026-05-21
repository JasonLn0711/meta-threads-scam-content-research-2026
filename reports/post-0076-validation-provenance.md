# Post-0076 Validation Provenance

## Purpose

This note gives technical reviewers repo-safe provenance for the checkpoint 0055 package and the local 0076 hard-negative addendum.

It contains no raw Threads URLs, handles, screenshots, raw post text, raw reply text, contact IDs, stock names, stock codes, price values, credentials, browser/session artifacts, controlled-store paths, tokens, cookies, or stakeholder case IDs.

## Package Identity

| Field | Value |
|---|---|
| Package version | post-0076 report v0 reviewer package |
| Delivery status | `revise_before_delivery` |
| Selected path under revision | `report_only_delivery` |
| Canonical approved checkpoint | `threads_pilot_v1_0055` |
| Post-checkpoint addendum | local item `0076` hard-negative calibration |
| Base package commit reviewed | `21ed7b2` |

## Schema Contracts

| Schema | Purpose |
|---|---|
| `data-contracts/thread_item_schema_v1.json` | Thread item field and structural contract. |
| `data-contracts/labeling_schema_v1.json` | Label, risk, confidence, and review-state contract. |

## Validation Commands

The repo-safe command families used for the checkpoint summaries were:

| Command family | Purpose |
|---|---|
| `scripts/validate_thread_dataset.py --strict` | Strict schema and contract validation. |
| `scripts/audit_thread_dataset.py` | Dataset audit and warning-threshold review. |
| `scripts/run_rule_baseline.py --variant all` | Rule-baseline smoke-test metrics. |

The commands were run against the checkpoint 0055 aggregate and the local checkpoint 0076 aggregate. Raw/interim evidence files are not included in the reviewer ZIP.

## Checkpoint 0055 Results

| Measure | Value |
|---|---:|
| Total records | 55 |
| `scam` records | 17 |
| `non_scam` records | 23 |
| `uncertain` records | 9 |
| `insufficient_evidence` records | 6 |
| Strict validation errors | 0 |
| Strict validation warnings | 0 |
| Audit threshold flags | 0 |
| Raw evidence in git | no |

Baseline run name: `checkpoint-0055-option-a-run-0038-smoke-v1`

| Metric | Value |
|---|---:|
| Binary-evaluable items | 40 |
| Baseline precision | 0.708 |
| Baseline recall | 1.000 |
| Baseline F1 | 0.829 |
| Baseline false positives | 7 |
| Baseline false negatives | 0 |

These are smoke-test baseline metrics on the current binary-evaluable slice, not production performance estimates.

## Local Checkpoint 0076 Addendum Results

| Measure | Value |
|---|---:|
| Total records | 76 |
| `scam` records | 17 |
| `non_scam` records | 24 |
| `uncertain` records | 29 |
| `insufficient_evidence` records | 6 |
| `high` risk | 17 |
| `medium` risk | 13 |
| `low` risk | 46 |
| Strict validation errors | 0 |
| Strict validation warnings | 0 |
| Audit schema errors | 0 |
| Audit schema warnings | 0 |
| Raw evidence in git | no |

Baseline run name: `checkpoint-0076-hard-negative-smoke-v1`

| Metric | Value |
|---|---:|
| Baseline precision | 0.708 |
| Baseline recall | 1.000 |
| Baseline false positives | 7 |
| Baseline false negatives | 0 |

## Strict-Valid Caveat

"Strict-valid" means schema and validation checks passed. It does not mean the 76-record local aggregate replaces the approved 55-record checkpoint package or that every local record is reviewer-approved.

Only checkpoint 0055 is currently approved for CIB/165-facing checkpoint use. Item 0076 is a narrow local hard-negative addendum.

## Current Non-Authorizations

This provenance note does not authorize:

- item `0077`
- browser-session expansion
- crawler expansion
- confirmed-pointer intake
- embedding or model training
- production detector claims
- legal fraud determinations
- raw evidence in git
