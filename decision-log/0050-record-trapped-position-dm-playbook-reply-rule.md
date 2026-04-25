# Decision 0050: Record Trapped-Position DM Playbook Reply Rule

## Date

2026-04-25

## Status

Accepted

## Decision

Add `trapped_position_dm_playbook_reply` as a signal tag and `TRAPPED_POSITION_DM_PLAYBOOK_REPLY` as a baseline reason code.

This signal covers reply-level trapped-position or loss-anxiety cues that are moved into DM/private playbook guidance instead of transparent public explanation.

## Trigger

The project owner supplied a confirmed Threads scam pointer for item `0038`. The repo records only the repo-safe rule implication, not the raw URL, raw handle, raw stock text, raw replies, screenshot, HTML, or source case ID.

## Rationale

Item `0038` reinforces the short-term stock-pick playbook funnel and adds a reply-level conversion point: when a commenter expresses being trapped or needing help with a position, the author moves the answer to private message with a detailed operation playbook. This turns loss anxiety into a private persuasion path.

## Boundaries

- Do not label every reply to an investment question as scam-like.
- Legitimate creators may answer stock questions publicly.
- The signal requires a loss/trapped/help cue plus movement into private message, private guidance, or detailed playbook.
- It is strongest when paired with short-term stock-pick FOMO, prior-performance proof, private-channel migration, stock-rescue language, or operation-playbook offers.
- Do not store raw URLs, raw handles, raw stock text, raw reply text, screenshots, HTML, or source case IDs in git.

## Files Updated

- `docs/04-taxonomy.md`
- `docs/06-annotation-guideline-v1.md`
- `docs/30-annotator-onboarding-quickstart.md`
- `docs/43-reason-codes-and-thresholds.md`
- `data-contracts/labeling_schema_v1.json`
- `data-contracts/thread_item_schema_v1.json`
- `src/baselines/taxonomy.py`
- `src/baselines/signal_extractor.py`
- `src/baselines/explainability.py`
- `configs/baseline_rule_config.yaml`
- `governance/pilot-launch/threads_pilot_v1_2026-05_guideline_revision_log.md`

## Next Action

Use this rule for future confirmed pointers where loss anxiety or trapped-position help becomes a private-message or operation-playbook conversion point.
