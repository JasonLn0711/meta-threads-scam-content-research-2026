# First 10-15 Real Pilot Start Note

## Objective

Start the next governed research step: prepare the first real 10-15 Threads pilot items as a checkpoint, not as a full collection push.

This note is repo-safe. It does not contain raw Threads content, screenshots, source URLs, handles, case IDs, credentials, raw storage paths, access lists, or sensitive investigative details.

## Current Start Status

As of `2026-04-23`, the repo is mechanically ready for the next governed step, and an outside-git controlled workspace scaffold has been created. Real item collection remains blocked until the controlled launch record is completed and approved outside git.

Repo-safe checks run for this start note:

```bash
python scripts/check_pilot_preflight.py
python scripts/init_pilot_workspace.py --dry-run
```

Observed preflight result:

| Check | Result |
|---|---|
| Repo-only preflight | `OK: 14`, `WARN: 3`, `ERROR: 0` |
| Local workspace dry run | expected local-only files listed; no files written |
| Tracked raw/interim/processed/private evidence | none detected |
| Local raw files in repo-controlled raw/screenshot/browser/evidence folders | none detected |

Expected warnings:

- local workspace files are not initialized yet
- controlled launch details cannot be verified from this repo
- git worktree has local uncommitted or untracked changes

These warnings are acceptable before collection only if the project owner completes the outside-git controlled launch record, changes its final decision to `ready_for_rehearsal` or `ready_for_first_10_15_items`, and can explain local worktree state before item 1.

## Research Question For The Checkpoint

Can a bounded, manual-only, privacy-minimized first batch of 10-15 Threads items produce reviewable `thread_item_schema_v1` records without triggering governance, redaction, source-skew, or annotation-stability failures?

The checkpoint should answer:

- whether approved source categories can produce enough reviewable items
- whether redaction rules work for text, screenshots, OCR, URLs, handles, and replies
- whether collectors need unapproved profile, account, landing-page, redirect-chain, or automation context
- whether annotators can separate `scam`, `non_scam`, `uncertain`, and `insufficient_evidence`
- whether the first source mix is already too skewed or too low-context
- whether continuing to 50 items is justified, limited, paused, or stopped

## Non-Negotiable Preconditions

Do not create real local item files until all of these are true:

- controlled launch record is complete outside git
- exact source or source category is recorded in the controlled location
- exact raw storage location is recorded outside git
- exact access list is recorded outside git
- exact retention or deletion rule is recorded outside git
- exact redaction limits are recorded outside git
- screenshot, OCR, URL/link, handle/contact, and reply/comment policies are recorded
- collector, annotator, reviewer, adjudicator, and research engineer IDs are assigned
- item-1 preflight passes with `ERROR: 0`

After that, initialize local-only files:

```bash
python scripts/init_pilot_workspace.py --ack-controlled-details
python scripts/check_pilot_preflight.py --before-item-1 --ack-controlled-details
```

## First 10-15 Item Target Mix

The first checkpoint batch should be diagnostic, not representative. Do not force any bucket if doing so requires unapproved evidence.

| Bucket | Target count |
|---|---:|
| likely scam or high-risk scam-like | 3-5 |
| likely non-scam comparator | 3-5 |
| uncertain or ambiguous | 2-3 |
| insufficient-evidence or low-context | 1-3 |

Content-form coverage target:

| Content form | Target |
|---|---:|
| text-only | at least 2 |
| text plus image | at least 2 if approved |
| reply/comment context | at least 1-2 if approved |
| OCR-heavy or screenshot-style | at least 1 if approved |
| visible link, handle, or redirect signal | at least 2 if approved |

## Minimum Item Readiness Checks

Each real checkpoint item must satisfy these before annotation:

- `collection_batch_id` is present
- `authorization_status` is `approved`
- source type and collection method match the controlled record
- raw evidence stayed outside git
- source references are omitted, normalized, or redacted as approved
- screenshot status is filled when image/screenshot evidence exists
- link status is filled when visible links exist
- OCR text is privacy-reviewed when present
- handles are redacted or categorized when present
- `privacy_redaction_notes` explains links, handles, OCR, screenshots, or stakeholder context where relevant
- no profile/account/landing-page/redirect-chain context is required
- no automation, scraping, crawling, bulk export, browser profile, credential, or session artifact is involved

## Recommended Start Sequence

1. Project owner confirms the controlled launch record is complete outside git.
2. Research engineer initializes local-only workspace under ignored `data/interim/`.
3. Research engineer runs item-1 preflight and confirms `ERROR: 0`.
4. Collector prepares 1-2 manual rehearsal records using approved fields only.
5. Collector and governance reviewer apply the manual rehearsal checklist.
6. Annotation lead confirms calibration or reruns it if annotators changed.
7. Collector records only the first 10-15 candidate items.
8. Team pauses and completes `data/interim/threads_pilot_v1_checkpoint_review.md`.
9. Research engineer runs validation/audit only on approved local files.
10. Project owner records one checkpoint decision before any move toward 50.

## Local Commands After Real Local Files Exist

Use only after controlled details are complete and local files exist:

```bash
python scripts/validate_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv --strict
python scripts/audit_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv \
  > data/processed/threads_pilot_v1_checkpoint_audit.md
```

If only the collection log exists, run a manual collection checkpoint first and wait to validate the annotation CSV until schema-shaped rows exist.

## Stop Or Pause Conditions

Pause immediately if:

- any raw evidence enters git
- item-1 preflight reports any `ERROR`
- controlled launch details are incomplete or unclear
- collector needs profile/account/landing-page/redirect-chain context
- collection drifts toward automation or bulk export
- screenshots, URLs, handles, OCR, or replies cannot be redacted consistently
- source is not the one approved in the controlled launch record
- more than 30 percent of checkpoint items are not ready for annotation because evidence is missing or unsafe
- annotators repeatedly confuse `uncertain` and `insufficient_evidence`
- any raw identifiers appear in annotation notes

## Checkpoint Decision Values

The checkpoint must choose exactly one:

- `continue_to_50`
- `continue_with_limits`
- `pause_for_redaction_fix`
- `pause_for_collection_fix`
- `pause_for_guideline_fix`
- `pause_for_authorization_review`
- `stop_pilot`

Do not continue to 50 unless the decision is `continue_to_50` or `continue_with_limits`.

## Current Decision

Current decision: `controlled_workspace_scaffold_created_waiting_for_owner_completion`

Reason:

- repo-only preflight has no errors
- local workspace dry run is ready
- an outside-git controlled workspace scaffold exists
- real local files should not be created until the project owner/governance reviewer completes and confirms the outside-git controlled launch record
- no real Threads evidence has been collected or committed as part of this start note

## Commit Boundary

Commit only this aggregate start note and index updates.

Do not commit:

- real local workspace files under `data/interim/`
- raw evidence or screenshots
- source URLs, handles, case IDs, or stakeholder case material
- filled controlled launch records if they contain sensitive details
- checkpoint audit output with item-level real evidence
