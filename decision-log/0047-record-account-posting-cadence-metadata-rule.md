# Decision 0047: Record Account Posting Cadence Metadata Rule

## Date

2026-04-25

## Status

Accepted

## Decision

Add `account_posting_cadence_metadata` as an account-level context signal and controlled sampling rule.

For CIB-detected or otherwise approved scam accounts, the project may record repo-safe posting cadence and feed-density metadata during controlled account sampling. This includes aggregate candidate-post count, visible time-bucket distribution, recent-marker count, and a short density note.

## Trigger

The project owner noted that when the source is a scam account, posting frequency and other account metadata may be useful and asked whether it should become a rule.

## Rationale

Cadence metadata can help prioritize which approved accounts and candidate posts deserve full-thread capture next. Some scam-like accounts may post many related investment lures in a short period, repeat the same stock/sector themes, or maintain high interaction density across several recent posts.

This is especially useful when paired with `account_multi_post_style_cluster`, because the account-level sample can reveal both content-style variety and posting density without needing broad search.

## Boundaries

- Cadence is prioritization context, not a standalone scam label.
- Record only aggregate counts, time buckets, candidate density notes, and controlled-store references in repo-safe files.
- Do not run continuous monitoring unless a later decision explicitly approves it.
- Do not capture follower/following graphs, broad account history, profile photos, or unrelated personal data by default.
- Each selected post still needs item-level full-thread capture, redacted manual entry, strict validation, and second review.

## Files Updated

- `docs/04-taxonomy.md`
- `docs/06-annotation-guideline-v1.md`
- `docs/30-annotator-onboarding-quickstart.md`
- `docs/51-stakeholder-evidence-expansion-memo.md`
- `templates/controlled_launch_details_template.md`
- `data-contracts/labeling_schema_v1.json`
- `data-contracts/thread_item_schema_v1.json`
- `governance/pilot-launch/threads_pilot_v1_2026-05_guideline_revision_log.md`

## Controlled Store Tooling

The outside-git controlled account capture helper now records `account_cadence_metadata` in raw controlled output, including candidate-post count, visible time-marker count, recent-marker count, time-bucket counts, and a density note.
