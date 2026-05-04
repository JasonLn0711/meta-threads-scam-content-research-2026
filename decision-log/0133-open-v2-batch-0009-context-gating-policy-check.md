# Decision 0133 - Open V2 Batch 0009 Context-Gating Policy Check

Date: 2026-05-05

## Status

Accepted as a planned metadata-only v2 batch.

## Decision

Open Batch 0009 as a capped prospective check of the Batch 0008 context-gating
policy.

The batch uses a policy-weighted allocation:

```text
strong_source_priority: 8
result_display_clean_holdout: 2
result_display_low_context_transition: 1
result_display_thread_required: 1
```

## Rationale

Batch 0008 showed that balanced comparison was no longer the right default.

The system learned:

- `strong_source_priority` has the strongest reviewer-hour value;
- `成果展示` alone is not a priority positive-yield source;
- low-context result display belongs in boundary triage;
- thread-required result display belongs in capped slow diagnostics;
- clean result-display holdout protects hard-negative calibration.

Batch 0009 therefore tests whether the policy improves reviewer-hour allocation
when it controls the next batch.

## Evidence

- `docs/63-context-gating-policy.md`
- `experiments/evaluation-notes/0104-v2-batch-0008-reviewer-hour-value-result.md`
- `metrics/batch_logs/batch_0008_run_log.yaml`
- `metrics/contrast_scores/latest.yaml`
- `metrics/signal_scores/latest_ranking.yaml`
- `outputs/research_candidates/RC_0007.md`

## Scope

This decision creates only metadata-only planning, stubs, intake, reviewer
packet, dry-run conversion, and planned run-log artifacts.

It does not authorize:

- external data access;
- raw Threads content storage;
- PII storage;
- URLs, handles, screenshots, browser artifacts, or controlled-store locators in
  git;
- sparse schema auto-promotion;
- model training;
- production detection;
- legal fraud determination;
- enforcement, takedown, or public-warning actions.

## Next Action

Fill Batch 0009 with human-reviewed structured metadata only. Conversion must
remain blocked until every completion gate passes.
