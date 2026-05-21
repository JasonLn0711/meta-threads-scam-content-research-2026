# Decision 0049: Record Stock-Pick Playbook Keyword Funnel Rule

## Date

2026-04-25

## Status

Accepted

## Decision

Add `stock_pick_playbook_keyword_funnel` as a signal tag and `STOCK_PICK_PLAYBOOK_KEYWORD_FUNNEL` as a baseline reason code.

This signal covers a named short-term stock-pick lure where the public post creates FOMO or strong outcome expectations, then a reply/action gate asks readers to follow, message, or send a numeric code/keyword to receive a complete operation script, playbook, or similar private follow-up.

## Trigger

The project owner supplied a confirmed Threads scam pointer for item `0037`. The repo records only the repo-safe rule implication, not the raw URL, raw handle, raw stock text, raw replies, screenshot, HTML, or source case ID.

## Rationale

Earlier rules covered comment-code lead magnets and individual stock advice. Item `0037` adds a narrower short-term stock-pick playbook funnel: the public post uses a named pick, recent winner comparisons, do-not-miss framing, close-eyes entry, and break-high certainty; the reply then offers a complete operation script through follow/message/code action.

This is useful because the suspicious conversion is not always a visible LINE link. The gate can be a numeric code or private message that delivers the next step later.

## Boundaries

- Do not label every named stock discussion as scam.
- Legitimate stock analysis can include entry timing and technical discussion.
- The signal requires convergence: named short-term pick plus FOMO/strong outcome language plus follow/message/code gate or private playbook offer.
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

Use this rule for future confirmed pointers where a public short-term stock-pick post gates the complete playbook behind follow/message/code action.
