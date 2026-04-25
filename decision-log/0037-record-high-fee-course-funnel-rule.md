# Decision 0037: Record High-Fee Course Funnel Rule

## Date

2026-04-25

## Status

Accepted

## Decision

Add `high_fee_course_or_membership_funnel` as a signal tag and `HIGH_FEE_COURSE_FUNNEL` as a baseline reason code.

This signal covers a high-fee course, academy, coaching, membership, or trading-education funnel tied to financial outcomes.

## Trigger

The project owner supplied a confirmed Threads scam pointer for item `0029`. The repo records only the repo-safe rule implication, not the raw URL, raw handle, raw post text, raw replies, screenshot, HTML, or source case ID.

The reported and captured pattern is:

- trading or financial-education brand narrative;
- high-fee course, membership, academy, or coaching funnel;
- selected reply/comment context surfaces guarantee/profit, fee, or legitimacy disputes;
- the top-level post may use defensive or legitimacy framing rather than an obvious scam claim.

## Rationale

Earlier rules covered guaranteed outcomes, private-channel migration, testimonial proof, and reply-only lures. Item `0029` adds another repeatable family: a high-fee trading or financial-education funnel where the risk becomes clear through the combination of post content, images, and reply-context disputes.

## Boundaries

- A paid course is not automatically a `scam` label.
- An expensive course is not automatically a `scam` label.
- The signal becomes review-worthy when paired with financial outcome claims, guarantee/profit disputes, private contact, payment structure, testimonial proof, fake authority, or other scam-like evidence.
- Do not claim legal fraud determination from this rule.
- Do not store raw URLs, raw handles, screenshots, raw post text, raw reply text, or source case IDs in git.

## Files Updated

- `docs/04-taxonomy.md`
- `docs/06-annotation-guideline-v1.md`
- `docs/30-annotator-onboarding-quickstart.md`
- `data-contracts/labeling_schema_v1.json`
- `data-contracts/thread_item_schema_v1.json`
- `docs/43-reason-codes-and-thresholds.md`
- `src/baselines/taxonomy.py`
- `src/baselines/signal_extractor.py`
- `src/baselines/explainability.py`
- `configs/baseline_rule_config.yaml`
- `governance/pilot-launch/threads_pilot_v1_2026-05_guideline_revision_log.md`

## Next Action

Use the rule for future confirmed pointers and controlled captures, but keep second review required when this signal materially affects a `scam` or `high` label.
