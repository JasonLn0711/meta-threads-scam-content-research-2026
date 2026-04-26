# Existing Ambiguous And Medium-Risk Review Queue

## Purpose

Summarize the second-review queue for existing checkpoint 0076 records with `uncertain`, `insufficient_evidence`, or `medium` risk status.

This note is repo-safe. It does not include raw Threads URLs, handles, screenshots, raw post text, raw reply text, contact IDs, stock names, stock codes, price values, credentials, browser/session artifacts, exact controlled-store paths, or stakeholder case IDs.

## Queue Summary

| Measure | Count |
|---|---:|
| Checkpoint 0076 total records | 76 |
| `uncertain` records | 29 |
| `insufficient_evidence` records | 6 |
| `medium` risk records | 13 |
| Deduplicated review queue | 35 |

Queue file:

```text
data/interim/review_queue_checkpoint_0076_uncertain_insufficient_medium.csv
```

## Priority Rationale

This review is valuable because:

- `uncertain` items may hide false negatives if evidence actually supports scam/high-risk;
- `insufficient_evidence` items may need explicit controlled-context follow-up or should remain excluded;
- `medium` risk items often sit near the threshold between low-risk comparator and high-risk scam-like record;
- second review can improve the existing dataset without opening new collection.

## Review Buckets

| Bucket | Review question |
|---|---|
| `uncertain` + `medium` | Can existing evidence support promotion to `scam` / `high`, downgrade to `non_scam` / `low`, or should it stay uncertain? |
| `uncertain` + `low` | Is uncertainty caused by weak evidence, benign context, or missing context? |
| `insufficient_evidence` | Is there enough existing evidence to review, or should missing context remain blocking? |
| `medium` risk without high-confidence label | Should risk be adjusted after second review? |

## Guardrails

This review queue does not authorize:

- item `0080` or later;
- new source discovery;
- browser/crawler expansion;
- account/profile graph capture;
- landing-page or redirect-chain capture;
- private-message access;
- embedding or model training;
- production detection;
- legal fraud determinations;
- raw evidence in git.

## Next Step

Review queued items one by one using existing redacted records. Record item-level adjudication before changing labels, rebuilding records, or updating aggregate metrics.
