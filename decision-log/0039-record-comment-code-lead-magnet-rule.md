# Decision 0039: Record Comment-Code Lead Magnet Rule

## Date

2026-04-25

## Status

Accepted

## Decision

Add `comment_code_lead_magnet` as a signal tag and `COMMENT_CODE_LEAD_MAGNET` as a baseline reason code.

This signal covers replies or comments that ask readers to follow, comment, reply with a code, use a keyword, or otherwise trigger a free stock pick, list, method, quota, or benefit.

## Trigger

The project owner supplied a confirmed Threads scam pointer for item `0030`. The repo records only the repo-safe rule implication, not the raw URL, raw handle, raw post text, raw replies, screenshot, HTML, or source case ID.

The captured pattern is:

- public-figure or authority shock framing;
- named stock or brand references used as financial credibility bait;
- strong upside or target-price style language;
- the author's reply/comment contains the conversion signal through a code, keyword, follow, or free-receive instruction;
- selected reply context includes skepticism or scam-warning language.

## Rationale

Earlier rules covered explicit private redirects, implicit DM requests, and high-fee course funnels. Item `0030` adds a different conversion style: the public surface can look like ordinary finance discussion or engagement bait, while the author's reply converts attention into a lead magnet through a code/keyword instruction.

For the CIB-authorized pilot, false negatives are more costly than explainable false positives at triage. The signal should be preserved when it converges with investment/profit framing, fake authority, target-price claims, named stock picks, or suspicious reply context.

## Boundaries

- A code, keyword, or comment prompt alone is not automatically a `scam` label.
- Ordinary polls, jokes, creator engagement prompts, or harmless newsletters are not automatically scam-like.
- Labeling must be based on the whole collected `thread_item`.
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
