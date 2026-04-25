# Decision 0044: Record Poster Identity Context Capture Rule

## Date

2026-04-25

## Status

Accepted

## Decision

Add a generic poster identity/profile-context capture rule for confirmed Threads scam-pointer intake.

For each newly approved controlled capture, the collection process should record the top-level poster's Threads ID and narrow risk-relevant profile context in the controlled store when technically available and authorized. Repo-safe records may carry only a controlled-store reference, salted hash, redacted handle, status field, category signals, and redacted notes.

## Trigger

The project owner clarified that scam-post collection should also preserve the scam poster's Threads ID and related information while building the scam-post database and rule library.

## Rationale

Post and reply content are not enough for repeat-source research. Poster identity context supports:

- dedupe across repeated confirmed pointers;
- repeat-source and cluster review;
- profile-level funnel interpretation;
- future evidence-family research on coordinated or recurring scam-like behavior.

This must not collapse into broad account surveillance. The ID/profile context is evidence context, not a standalone scam label or legal finding.

## Boundaries

- Capture top-level poster context only unless a later run record explicitly authorizes broader scope.
- Do not capture follower/following graphs, unrelated user handles, broad profile history, profile photos, or unrelated personal data by default.
- Do not store raw Threads IDs, raw profile URLs, raw handles, screenshots, or profile raw output in git.
- `poster_identity_context` may support dedupe and escalation only when it reinforces post, reply, OCR, link, payment, credential, or private-channel evidence.
- Preserve uncertainty and do not infer criminal intent from account identity alone.

## Files Updated

- `docs/04-taxonomy.md`
- `docs/06-annotation-guideline-v1.md`
- `docs/30-annotator-onboarding-quickstart.md`
- `docs/51-stakeholder-evidence-expansion-memo.md`
- `data-contracts/labeling_schema_v1.json`
- `data-contracts/thread_item_schema_v1.json`
- `templates/annotation_sheet_template.csv`
- `templates/controlled_launch_details_template.md`
- `templates/thread_item_sample.json`
- `templates/thread_item_sample_batch.json`
- `src/data_collection/manual_record_builder.py`
- `governance/pilot-launch/threads_pilot_v1_2026-05_guideline_revision_log.md`

## Next Action

For the next confirmed pointer, fill `poster_threads_id_ref`, `poster_profile_context_status`, `poster_profile_signals`, and `poster_profile_notes` in the local/manual record after the controlled capture confirms the raw poster ID/profile context is preserved in the controlled store.
