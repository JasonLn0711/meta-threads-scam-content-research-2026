# Decision 0054: Record Anti-Scam Warning Hard-Negative Boundary

## Date

2026-04-25

## Status

Accepted

## Decision

Record anti-scam warning posts as hard-negative calibration examples when they describe scam methods to warn potential victims and do not introduce a new conversion path.

This is not a new scam signal. It is a boundary rule for avoiding false positives when warning, education, victim-prevention, or commentary posts contain scam vocabulary.

## Trigger

The project owner supplied a Threads pointer for item `0042` and explicitly identified it as a warning to potential victims, not a scam post. The repo records only the repo-safe boundary implication, not the raw URL, raw handle, raw post text, raw replies, screenshot, HTML, or source case ID.

## Rationale

Anti-scam warnings can contain many words that also appear in scams: promised returns, stock groups, teachers, foreign-market trading, pump-and-dump mechanics, victim-loss stories, or private-group references. First principles: label the direction of persuasion, not isolated keywords. A warning that tells readers not to join, not to trust, and not to chase the offer should be treated differently from a post that asks readers to join, pay, DM, open an account, or follow a private method.

## Boundaries

- Use `non_scam` when the visible thread is warning, educating, or discussing victim-prevention and does not introduce a new offer.
- Do not turn quoted scam mechanics into active scam evidence by themselves.
- Escalate to `uncertain` if the warning post also promotes the author's own group, safe teacher, paid course, affiliate path, private contact, or replacement investment method.
- Do not store raw URLs, raw handles, raw post text, raw reply text, screenshots, HTML, stock names, contact handles, or source case IDs in git.

## Files Updated

- `docs/06-annotation-guideline-v1.md`
- `docs/43-reason-codes-and-thresholds.md`
- `governance/pilot-launch/threads_pilot_v1_2026-05_item_0042_full_thread_capture_run_record_0034.md`
- `experiments/evaluation-notes/0063-confirmed-non-scam-warning-0042-result.md`

## Next Action

Use item `0042` as a hard negative when checking whether future rule changes over-trigger on anti-scam warnings, victim reports, or educational commentary.
