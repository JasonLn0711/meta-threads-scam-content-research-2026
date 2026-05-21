# Decision 0048: Record Reply Impersonation Contact Hijack Rule

## Date

2026-04-25

## Status

Accepted

## Decision

Add `reply_impersonation_contact_hijack` as a signal tag and `REPLY_IMPERSONATION_CONTACT_HIJACK` as a baseline reason code.

This signal covers selected replies that appear to impersonate, certify, or ride on the poster's identity and redirect readers to LINE/contact/group paths, daily lists, holdings viewpoints, or similar investment follow-up channels.

## Trigger

The project owner supplied a confirmed Threads scam pointer for item `0036`. The repo records only the repo-safe rule implication, not the raw URL, raw handle, raw post text, raw replies, screenshot, HTML, contact handles, or source case ID.

## Rationale

The item shows an important thread-level scam risk: the top-level post uses humble/no-benefit/trust-building language, while the reply layer contains repeated contact/group redirection, official-contact or anti-scam claims, and LINE/contact paths. The suspicious conversion may be carried by replies rather than the top-level post.

This rule preserves attribution uncertainty. It does not assume the top-level poster authored every suspicious reply, but it records that the thread environment can expose readers to contact hijack or impersonation-based redirection.

## Boundaries

- Do not assume suspicious replies were written by the top-level poster unless controlled evidence shows that.
- A single unrelated spam reply may be insufficient by itself; repeated or prominent contact-hijack replies are stronger.
- Do not store raw contact handles, raw reply text, raw URLs, raw handles, screenshots, HTML, or source case IDs in git.
- The signal is strongest when paired with investment/profit framing, follower trust, anti-scam camouflage, daily list/holding-viewpoint offers, or repeated contact handles.

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

Use the rule for future confirmed pointers and controlled captures. Preserve attribution uncertainty whenever suspicious replies may be impersonation or hijack rather than the top-level poster's own reply.
