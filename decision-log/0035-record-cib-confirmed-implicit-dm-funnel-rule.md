# Decision 0035: Record CIB-Confirmed Implicit DM Funnel Rule

## Date

2026-04-25

## Status

Accepted

## Decision

Add an explicit signal for `implicit_dm_contact_request`.

This signal covers a scam-like item that asks users to private-message the poster or another account to receive details, while public contact details such as LINE links, external URLs, scam sites, or contact handles are absent from the visible post or selected replies.

## Trigger

The project owner provided a CIB-confirmed Threads scam-case pointer. The repo records only the repo-safe rule implication, not the raw URL, raw handle, screenshots, full content, or source case ID.

The reported pattern is:

- investment or profit-related content may be wrapped inside another story or ordinary-looking post;
- the visible post or selected replies may not directly show LINE, Telegram, WhatsApp, external scam links, scam websites, or contact handles;
- the post or replies may ask other users to private-message the poster;
- the scam contact route may then be delivered only inside private chat.

## Rationale

Earlier rules already covered visible private-channel redirects and visible contact handles. This exemplar shows a more evolved funnel: the public surface can avoid obvious contact artifacts while still using a DM request as the conversion step.

For the CIB-authorized pilot, false negatives are more costly than explainable false positives at triage. Therefore, the annotation guideline and baseline should preserve this signal and route it to review when it appears with investment/profit framing or other scam-like evidence.

## Boundaries

- A DM request alone is not automatically a `scam` label.
- Labeling must still be based on visible approved evidence in the `thread_item`.
- Legitimate creators also ask for DMs, so second review is required when this signal materially affects the label.
- Do not store raw URLs, raw handles, screenshots, raw reply text, or source case IDs in git.
- Do not claim legal fraud determination from this rule.

## Files Updated

- `docs/04-taxonomy.md`
- `docs/06-annotation-guideline-v1.md`
- `data-contracts/labeling_schema_v1.json`
- `data-contracts/thread_item_schema_v1.json`
- `docs/43-reason-codes-and-thresholds.md`
- `src/baselines/taxonomy.py`
- `src/baselines/signal_extractor.py`
- `src/baselines/explainability.py`
- `configs/baseline_rule_config.yaml`
- `governance/pilot-launch/threads_pilot_v1_2026-05_guideline_revision_log.md`

## Next Action

Use this rule in the next targeted exemplar or item `0028` review only after the approved redacted fields are entered, built, strict-validated, and second-reviewed.
