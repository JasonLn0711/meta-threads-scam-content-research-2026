# Approved Pilot Launch Plan

## Purpose

This document records the post-approval launch plan for the first real Threads pilot.

The stakeholder outcome has been reported as approved. The repo therefore moves from approval preparation into controlled pilot launch preparation.

Launch status: `go_with_limits`.

No real Threads evidence has been collected or committed.

Owner follow-up approval: the project owner approved the repo's requirement that exact source, storage, access, retention, and redaction limits must be written into the launch record before collection. Sensitive values should be kept in the approved controlled location rather than this git repo.

## What Approval Means Here

Approval means the project may prepare and run the first 50-item pilot under explicit limits:

- 50 items maximum
- Threads-first only
- manual or stakeholder-provided examples only
- no scraping, crawling, browser automation, bulk export, landing-page crawling, redirect-chain capture, profile review, or production scoring
- raw evidence outside git
- redacted or derived annotation files only
- internal aggregate reporting only by default

Approval does not mean unlimited collection, production detection, public accusation, or legal fraud determination.

## Launch Packet

The non-sensitive launch records are in `governance/pilot-launch/`.

| Artifact | File |
|---|---|
| Source intake | `governance/pilot-launch/threads_pilot_v1_2026-05_source_intake.md` |
| Sampling frame | `governance/pilot-launch/threads_pilot_v1_2026-05_sampling_frame.csv` |
| Stakeholder authorization decision | `governance/pilot-launch/threads_pilot_v1_2026-05_authorization_decision.md` |
| Data authorization | `governance/pilot-launch/threads_pilot_v1_2026-05_data_authorization.md` |
| Go/no-go record | `governance/pilot-launch/threads_pilot_v1_2026-05_go_no_go.md` |
| Pilot work order | `governance/pilot-launch/threads_pilot_v1_2026-05_work_order.md` |
| Readiness review | `governance/pilot-launch/threads_pilot_v1_2026-05_readiness_review.md` |
| Local workspace instructions | `docs/39-local-pilot-workspace.md` |
| First checkpoint protocol | `docs/38-first-pilot-checkpoint-protocol.md` |
| First checkpoint template | `templates/pilot_checkpoint_review.md` |

## Launch Register Status

| Register | Status |
|---|---|
| `governance/source-intake-register.md` | `SRC-REAL-PILOT-APPROVED-2026-04-23` approved for the 50-item pilot under limits. |
| `governance/pilot-authorization-register.md` | `AUTH-THREADS-PILOT-V1-2026-04-23` approved with limits. |

## Launch Sequence

1. Complete the controlled launch record with exact source, storage, access, retention, and redaction limits. Use `templates/controlled_launch_details_template.md` only in the controlled location after filling it.
2. Confirm exact raw evidence storage outside git in a controlled location.
3. Confirm exact raw evidence access list outside git.
4. Assign collector, annotator, reviewer, adjudicator, and research engineer IDs.
5. Create local-only working files under ignored `data/interim/` using `scripts/init_pilot_workspace.py`.
6. Collect the first 10-15 items using the 15/15/10/10 diagnostic composition as a guide.
7. Run the first checkpoint with `docs/38-first-pilot-checkpoint-protocol.md` and `templates/pilot_checkpoint_review.md`.
8. Continue to 50 items only if the checkpoint decision is `continue_to_50` or `continue_with_limits`.
9. Apply redaction QA before annotation.
10. Validate the annotation CSV before annotation expands.
11. Run first-pass annotation.
12. Review all high-risk, uncertain, low-confidence, and partial-evidence cases.
13. Adjudicate disagreements.
14. Convert to JSONL locally after strict validation.
15. Run audit and rule-baseline comparison locally.
16. Produce a non-sensitive pilot result summary and decision memo.

## First Local Files To Create

Create these only after storage/access confirmation:

```bash
python scripts/init_pilot_workspace.py --dry-run
python scripts/init_pilot_workspace.py --ack-controlled-details
```

```text
data/interim/threads_pilot_v1_collection_log.csv
data/interim/threads_pilot_v1_annotations.csv
data/interim/threads_pilot_v1_annotation_pass_ann_01.csv
data/interim/threads_pilot_v1_annotation_pass_ann_02.csv
data/interim/threads_pilot_v1_checkpoint_review.md
data/interim/threads_pilot_v1_workspace_manifest.md
```

Create these only after validation and annotation:

```text
data/processed/threads_pilot_v1.jsonl
data/processed/threads_pilot_v1_audit.md
data/processed/threads_pilot_v1_rule_variant_comparison.md
data/processed/threads_pilot_v1_agreement.md
data/processed/threads_pilot_v1_disagreements.csv
```

These paths are ignored by git. Commit only aggregate, non-sensitive findings.

## First Review Checkpoint

Pause after the first 10-15 collected or annotated rows.

Use [38-first-pilot-checkpoint-protocol.md](38-first-pilot-checkpoint-protocol.md) and `templates/pilot_checkpoint_review.md`.

Review:

- whether redaction is consistent
- whether raw evidence stayed outside git
- whether the 15/15/10/10 composition is still feasible
- whether `uncertain` is becoming a catch-all
- whether screenshot/OCR/link handling is too burdensome
- whether annotators need unapproved context
- whether source skew is already too strong

If any issue is severe, pause the pilot and update the relevant governance, source, annotation, or schema document before continuing.

## Next Human Owner Action

Before first collection, the project owner must complete the controlled launch record with exact source, raw storage location, access list, retention/deletion rule, and redaction limits outside git. Use `templates/controlled_launch_details_template.md` as the blank structure, but keep the filled version out of git unless it is fully non-sensitive and explicitly approved. Then the collector can initialize local-only working files using [39-local-pilot-workspace.md](39-local-pilot-workspace.md) and begin the first 10-15 item collection checkpoint.
