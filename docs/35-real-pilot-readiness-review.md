# Real Pilot Readiness Review

## Purpose

Use this review before starting the first real 50-item Threads pilot.

This document is the integrated readiness gate. It does not replace the source intake, authorization request, sampling frame, go/no-go checklist, collection SOP, annotation QA plan, or baseline protocol. It brings those artifacts together so the project owner can make one defensible launch decision.

Default status: `not_ready`.

As of `2026-04-23`, the first real 50-item pilot has a `go_with_limits` launch packet under `governance/pilot-launch/`. Exact source, storage, access, retention, and redaction limits live in the outside-git controlled launch record. Item-level controlled pilot artifacts, if present, remain outside git; this repo should contain only non-sensitive launch records, aggregate notes, and decision artifacts.

## When To Use This Review

Complete this review after:

1. A candidate source has been proposed.
2. The source intake has been completed.
3. The sampling frame has been drafted.
4. The stakeholder authorization packet has been reviewed.
5. The stakeholder authorization decision record has been completed.
6. The authorization request has been reviewed.
7. Raw evidence storage, access, retention, and redaction rules are known.

Complete it before:

1. Collecting real Threads items.
2. Opening raw screenshots or stakeholder case materials for annotation.
3. Creating local files under `data/interim/` or `data/processed/` that contain real evidence.
4. Running baselines on real pilot data.
5. Preparing any 100-200 item dataset or 500-item expansion.

## Readiness Levels

| Level | Meaning | Allowed next action |
|---|---|---|
| `not_ready` | One or more required gates is missing, unclear, or unsafe. | Use only synthetic or fully redacted dry-run examples. |
| `ready_with_limits` | Required gates are satisfied, but collection must stay within specific limits. | Run only the approved limited pilot scope and stop at the first 10-15 item checkpoint. |
| `ready` | Required gates are satisfied with no unresolved launch blockers. | Start the approved pilot exactly as documented, beginning with the first 10-15 item checkpoint. |

Use `ready_with_limits` when approval is real but constrained, for example: one source type only, text-only capture, no screenshots, no stored URLs, no OCR retention, or a smaller batch than 50.

## Required Evidence Bundle

The readiness review should point to completed local artifacts. Do not paste raw evidence into this document.

| Area | Required artifact | Why it matters |
|---|---|---|
| Source intake | `templates/source_candidate_intake.md` completed copy | Defines what source is being used and why it is permitted. |
| Sampling | `templates/source_sampling_frame_template.csv` completed copy | Prevents opportunistic over-collection and source skew. |
| Stakeholder decision | `templates/stakeholder_authorization_decision_record.md` completed copy | Records approval, limits, blockers, and decision owner. |
| Authorization | `templates/data_authorization_request.md` completed copy | Records approved fields, handling, retention, and limits. |
| Governance record | `governance/source-intake-register.md` and `governance/pilot-authorization-register.md` | Creates durable decision memory. |
| Launch checklist | `docs/26-pilot-go-no-go-checklist.md` completed copy | Confirms operational gates. |
| Work order | `templates/pilot_batch_work_order.md` completed copy | Defines batch identity, roles, target counts, and stop conditions. |
| Collection SOP | `docs/23-collection-and-redaction-sop.md` | Confirms redaction and storage procedure. |
| Annotation onboarding | `docs/30-annotator-onboarding-quickstart.md` and `templates/annotator_onboarding_checklist.md` | Confirms annotators can apply labels consistently. |
| QA plan | `docs/31-annotation-quality-control-plan.md` and `templates/annotation_qa_checklist.md` | Confirms review, disagreement, and adjudication flow. |
| Baseline plan | `docs/08-baseline-strategy.md` and `docs/33-pilot-analysis-and-decision-framework.md` | Confirms evaluation will preserve uncertainty and not overclaim. |
| Mechanical preflight | `docs/40-pilot-preflight-verification.md` and `scripts/check_pilot_preflight.py` | Confirms repo and local workspace mechanics before item 1. |

## Review Gates

### Gate 1: Governance And Authorization

Readiness requires:

- approved source type
- approved collection fields
- approved collection method
- clear authorization status
- automation scope approved in writing; for this CIB pilot, API and automation are approved only under the controlled launch record and Decision 0018
- raw evidence storage location outside git
- access list for raw evidence
- retention rule
- redaction rule
- publication and demo restrictions

Current default finding: `ready_with_limits` only for the controlled run path recorded outside git; any unrecorded source, method, field, or storage change is `not_ready`.

### Gate 2: Source And Sampling

Readiness requires:

- source candidate reviewed before collection
- source sampling frame completed
- positive, negative, uncertain, and insufficient-evidence targets defined
- source skew risk noted
- duplicate handling defined
- exclusion reasons defined

The first pilot can target 50 items only conditionally. Start with the first 10-15 item checkpoint, then continue only if the checkpoint records `continue_to_50` or `continue_with_limits`.

| Bucket | Target |
|---|---:|
| likely scam or high-risk scam-like | 15 |
| likely non-scam comparator | 15 |
| uncertain or ambiguous | 10 |
| insufficient-evidence or low-context | 10 |

Do not expand to 100-200 items or 500 items until the 50-item pilot has been analyzed.

### Gate 3: Storage And Redaction

Readiness requires:

- raw screenshots, exports, and case packets stored outside git
- no credentials, browser profiles, raw personal data, or sensitive investigative files committed
- contact handles redacted or normalized according to the authorization request
- source URLs stored only if approved
- OCR text reviewed for unnecessary personal data
- screenshots reviewed before annotation and before any sharing
- collection log records redaction notes and missing evidence

If redaction cannot be performed consistently, the pilot remains `not_ready`.

### Gate 4: Annotation Operations

Readiness requires:

- annotator IDs assigned
- annotators have read the v1 guideline
- onboarding checklist completed
- 5-item calibration complete or scheduled before real annotation
- second-review routing rule understood
- adjudicator assigned
- disagreement log and adjudication template ready
- QA checkpoint after the first 10-15 real annotations

The pilot is not baseline-ready until high-risk, uncertain, low-confidence, and partial-evidence cases have received required review.

### Gate 5: Baseline And Evaluation

Readiness requires:

- validated annotation file format
- planned validation, conversion, audit, and baseline commands
- binary metric inclusion rule confirmed
- `uncertain` and `insufficient_evidence` retained for analysis rather than forced into binary labels
- error review table ready
- decision memo template ready

The first baseline-ready slice is:

- adjudicated or high-confidence items
- nonempty `post_text` or `ocr_text`
- clear `scam` or `non_scam` labels for binary metrics
- `uncertain` and `insufficient_evidence` reported separately

### Gate 6: Stop Conditions

The readiness review should confirm that the team will stop or pause if:

- authorization is unclear
- raw evidence enters tracked files
- collection or automation exceeds the controlled run record
- redaction is inconsistent
- source skew makes the batch uninformative
- annotators repeatedly disagree on label boundaries
- `uncertain` exceeds 30 percent without explanation
- `insufficient_evidence` exceeds 20 percent without a collection-quality fix
- baseline reporting would require overclaiming or collapsing uncertainty

## Current Readiness Assessment

| Area | Current status | Reason |
|---|---|---|
| Governance and authorization | `ready_with_limits` | Approval and launch packet recorded; exact controlled details required before first item. |
| Source and sampling | `ready_with_limits` | Source category and sampling frame recorded; exact sensitive source details stay outside git. |
| Storage and redaction | `ready_with_limits` | Storage category and redaction limits recorded; exact raw path/access list required outside git. |
| Annotation operations | `ready_with_limits` | Guideline, onboarding, QA, and templates exist; real annotation waits on approved evidence. |
| Baseline and evaluation | `ready_with_limits` | Scripts and protocols are dry-run tested on synthetic samples; real metrics wait on approved pilot data. |
| Overall launch decision | `go_with_limits` | Use `governance/pilot-launch/threads_pilot_v1_2026-05_readiness_review.md`; no collection before controlled details are complete. |

Before item 1, run:

```bash
python scripts/check_pilot_preflight.py --before-item-1 --ack-controlled-details
```

## Launch Decision Rule

The project owner may mark the pilot as `ready` only when every gate is satisfied and linked to a completed artifact.

The project owner may mark the pilot as `ready_with_limits` only when every unresolved issue is converted into an explicit launch limit.

Examples of acceptable limits:

- collect only text and manually entered OCR, no screenshots
- collect from stakeholder-provided cases only
- collect no source URLs
- collect 20 items before another review
- restrict annotation to two named reviewers
- store only redacted local CSV/JSONL, with raw evidence held by the authorized stakeholder

Examples of unacceptable unresolved issues:

- "approval assumed"
- "source public, so okay"
- "we will redact later"
- "raw screenshots in repo temporarily"
- "500 items because more data is better"
- "uncertain labels will be converted later"

## Owner Actions Before Real Collection

1. Complete a project-specific copy of `templates/real_pilot_readiness_review.md`.
2. Attach or link completed source intake, sampling frame, stakeholder authorization decision record, authorization request, go/no-go checklist, and pilot work order.
3. Record the source decision in `governance/source-intake-register.md`.
4. Record the pilot authorization decision in `governance/pilot-authorization-register.md`.
5. Confirm raw evidence storage outside git.
6. Confirm who may view raw evidence.
7. Confirm retention and deletion timing.
8. Confirm whether screenshots, URLs, contact handles, and OCR text may be stored.
9. If the final decision is `go` or `go_with_limits`, execute `docs/29-authorized-pilot-execution-plan.md`.

Until those actions are complete, continue with synthetic or fully redacted examples only.
