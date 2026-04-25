# Option A Run 0038 Result

## Purpose

Record the repo-safe result of the stakeholder-approved Option A limited browser-session tranche after checkpoint 0042.

This note contains no raw Threads content, full item URLs, raw handles, raw stock names, raw stock codes, brand names, price values, visible contact IDs, screenshots, raw reply text, credentials, browser artifacts, storage-state material, raw storage paths, or stakeholder case IDs.

## Result

| Field | Value |
|---|---|
| Run ID | `OPTION-A-THREADS-PILOT-V1-0046-0055-LIMITED-BROWSER-TRANCHE` |
| Run record | `governance/pilot-launch/threads_pilot_v1_2026-05_option_a_limited_browser_tranche_run_record_0038.md` |
| Source path | approved browser-session capture |
| Supplemental confirmed pointer used | no |
| Candidate review cap | 20 |
| Candidates reviewed | 20 |
| Selected item cap | 10 |
| Selected items | `0046-0055` |
| Strict validation | pass: 10 selected records and 55-record aggregate, 0 errors, 0 warnings |
| Second review | complete: fast different-angle review |
| Raw output | controlled store only |

## Second-Review Outcome

| Final label | Count |
|---|---:|
| `scam` | 0 |
| `non_scam` | 1 |
| `uncertain` | 4 |
| `insufficient_evidence` | 5 |

| Final risk | Count |
|---|---:|
| `high` | 0 |
| `medium` | 3 |
| `low` | 7 |

## Item-Level Repo-Safe Summary

| Item | Final label | Final risk | Repo-safe rationale |
|---|---|---|---|
| `0046` | `non_scam` | `low` | Anti-scam or concern-question false-positive pressure; private-message mechanics are discussed as a concern rather than used as a conversion path. |
| `0047` | `uncertain` | `medium` | Private-channel investment-group signal, but retained context is too thin for a scam label. |
| `0048` | `insufficient_evidence` | `low` | Fragmentary stock-audience wording. |
| `0049` | `insufficient_evidence` | `low` | Keyword-like stock fragment. |
| `0050` | `uncertain` | `low` | Vague stock reassurance, no retained payment/private-channel/reply proof. |
| `0051` | `insufficient_evidence` | `low` | Topic or hashtag-like fragment. |
| `0052` | `uncertain` | `medium` | Private group trading signal, but insufficient retained context for final scam label. |
| `0053` | `insufficient_evidence` | `low` | Negated or fragmentary market-scope text. |
| `0054` | `insufficient_evidence` | `low` | Negated or fragmentary intake-description text. |
| `0055` | `uncertain` | `medium` | Private-message action gate, but missing topic/reply context prevents a scam label. |

## Aggregate After Run 0038

| Metric | Value |
|---|---:|
| Total records | 55 |
| `scam` | 17 |
| `non_scam` | 23 |
| `uncertain` | 9 |
| `insufficient_evidence` | 6 |
| `high` risk | 17 |
| `medium` risk | 7 |
| `low` risk | 31 |
| Strict validation errors | 0 |
| Strict validation warnings | 0 |

## Baseline Smoke Result

```text
checkpoint-0055-option-a-run-0038-smoke-v1
```

| Metric | Value |
|---|---:|
| Binary metric items | 40 |
| Precision | 0.708 |
| Recall | 1.000 |
| F1 | 0.829 |
| False positives | 7 |
| False negatives | 0 |

## Interpretation

Run 0038 successfully executed the approved browser-session path within the stakeholder caps, but it did not add final scam/high-risk records.

The main value of the run is methodological:

- approved browser-session search can produce schema-valid and strict-valid records;
- short retained snippets still create substantial false-positive and uncertainty pressure;
- fast different-angle second review is necessary before counting any browser-session candidate;
- confirmed pointers remain higher-yield for final scam/high-risk rule-family learning.

## Decision Implication

Run 0038 exhausted both caps: 20 candidates reviewed and 10 selected items.

Do not continue this run. The next action should be either:

- synthesize the 55-record checkpoint and decide whether another tranche is justified; or
- wait for CIB/stakeholder confirmed pointers if the project needs more final scam/high-risk examples.
