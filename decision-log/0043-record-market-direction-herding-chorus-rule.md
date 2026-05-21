# Decision 0043: Record Market-Direction Herding Chorus Rule

## Date

2026-04-25

## Status

Accepted

## Decision

Add `market_direction_herding_chorus` as a signal tag and `MARKET_DIRECTION_HERDING_CHORUS` as a baseline reason code.

This signal covers strong market-direction calls amplified by a reply/comment chorus of buying, adding, holding, refilling, or following behavior.

## Trigger

The project owner supplied a confirmed Threads scam pointer for item `0034`. The repo records only the repo-safe rule implication, not the raw URL, raw handle, raw post text, raw replies, screenshot, HTML, or source case ID.

The captured pattern is:

- strong full-position, no-retreat, bullish, buy-the-dip, or hold/add framing;
- dismissal of bearish or cautionary voices;
- multiple commenters echo buying, adding, refilling, holding, or following;
- the comment layer creates social proof and herd pressure.

## Rationale

Earlier rules covered individual stock advice, group funnels, and past-performance proof. Item `0034` shows a related but distinct social-pressure pattern: even without direct individual advice or visible group links, a strong direction call plus follower action chorus can make the thread function as a persuasion funnel.

For the CIB-authorized pilot, false negatives are more costly than explainable false positives at triage. The signal should be preserved when it converges with prediction-proof, guru authority, group/private context, or repeated user action-taking comments.

## Boundaries

- A bullish or bearish opinion alone is not automatically `scam`.
- A few ordinary agreement comments are not enough by themselves.
- Labeling must be based on a strong direction call plus visible action-taking chorus and surrounding funnel context.
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
