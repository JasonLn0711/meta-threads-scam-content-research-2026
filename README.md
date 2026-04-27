# Meta Threads Scam Content Research 2026

## Problem Statement

This repository supports a Threads-first research program for studying scam or scam-like content on Meta Threads. The first-principle goal is to find a scalable, stable, and reviewable method for discovering Threads scam-post candidates at volume, starting with investment-scam content.

The project asks:

> What bounded, reviewable candidate-discovery method produces the highest useful yield for Threads investment-scam candidates while preserving hard-negative boundaries and acceptable reviewer burden?

This is not a production detector and does not make legal determinations. It is a research scaffold for scalable candidate discovery, risk triage, evidence design, and early experimental comparison.

The current first-principle method note is [docs/56-first-principle-investment-scam-discovery-method.md](docs/56-first-principle-investment-scam-discovery-method.md).

## Why Threads First

Recent stakeholder discussion suggests that Threads receives a high volume of scam-content reports. That makes Threads a better first research surface than trying to cover all Meta platforms at once.

Threads is also a practical first target because phase-1 evidence can start with:

- Text posts
- Text plus image posts
- Replies and comments
- Visible redirection language
- External links when present
- OCR text extracted from attached images

These surfaces are narrow enough for a budget-constrained research phase, but rich enough to test whether early signals are useful for human review.

## Research, Not Production Promise

The practical budget target is about NTD 1.8 million. That budget does not support a full-scale, platform-wide detection system, broad automated collection, heavy video pipelines, deepfake detection, or production deployment.

The first useful output should be a defensible research package that helps answer the scalable-discovery question:

- A stable dataset schema
- A scam-risk taxonomy
- An annotation guide
- A small reviewed sample
- Simple baselines
- A comparison of text, OCR, comment, and link signals
- Discovery-yield and reviewer-burden metrics
- Hard-negative protection for ordinary investment discussion and anti-scam warnings
- A decision memo on what to continue, cut, or defer

## Scope Summary

Included in phase 1:

- Threads investment-scam candidate discovery as the first focused domain
- Threads text posts
- Threads text plus image posts
- Replies and comments
- OCR text from attached images and screenshots
- Visible external links, handles, and redirection signals
- Human-review-oriented triage scoring

Deferred in phase 1:

- Long video analysis
- Heavy multimodal video pipelines
- Deepfake detection as a mainline workstream
- Full Meta cross-platform integration
- Fully automated production deployment

## Repo Map

```text
reports/         External-facing research reports and report index
docs/             Research framing, taxonomy, experiment plans, budget analysis
data-contracts/   Machine-readable dataset schema drafts
templates/        Annotation and experiment templates
notes/            Early thinking and meeting notes
governance/       Data handling, legal, platform, and privacy constraints
experiments/      Logs for baseline, modality, and evaluation experiments
data/             Placeholder only; no raw sensitive data should be committed
scripts/          Minimal utilities only after experiments justify code
src/              Reserved for small research prototype code
decision-log/     Durable decisions and scope changes
```

## Related Repos

This repo is the active Threads execution repo in a small research repo family.

| Repo | Role |
|---|---|
| `../planning-everything-track` | Control plane for priority, status, capacity, deadlines, and next actions. |
| `../meta-scam-ad-research-2026` | Umbrella strategy repo for broader Meta scam-risk research framing and scope decisions. |

Read `docs/21-repo-relationships.md` before copying content across repos or changing the boundary between Threads execution and umbrella strategy.

## Current Report Deliverable

The immediate deliverable is a CIB/165-facing initial research report:

- [reports/threads-scam-content-research-v0.md](reports/threads-scam-content-research-v0.md)
- [reports/threads-scam-content-research-v0-executive-brief.md](reports/threads-scam-content-research-v0-executive-brief.md)
- [reports/post-0076-next-decision-memo.md](reports/post-0076-next-decision-memo.md)
- [reports/report-v0-review-checklist.md](reports/report-v0-review-checklist.md)
- Target date: `2026-04-30`
- Status: research report v0, not a production detector or legal fraud determination

This supersedes a concept-only stakeholder scoping memo as the next research artifact.

## Current Research Status

As of `2026-04-27`, the repo has moved from scaffold-only to a controlled, checkpointed pilot with a CIB-approved 78-record research checkpoint:

- The canonical entry point for checkpoint 0081 is [reports/checkpoint-0081-approved-package-index.md](reports/checkpoint-0081-approved-package-index.md).
- The short reviewer entry point is [reports/checkpoint-0081-executive-addendum.md](reports/checkpoint-0081-executive-addendum.md).
- The detailed synthesis is [experiments/evaluation-notes/0089-checkpoint-0081-cib-approved-synthesis.md](experiments/evaluation-notes/0089-checkpoint-0081-cib-approved-synthesis.md).
- Historical approved checkpoint 0055 remains available at [reports/checkpoint-0055-approved-package-index.md](reports/checkpoint-0055-approved-package-index.md).
- Dataset schema and labeling schema v1 exist.
- Annotation guideline, collection/redaction SOP, pilot runbook, annotator calibration, and go/no-go checklist exist.
- Report v0, executive brief, review checklist, and delivery plan exist.
- Synthetic sample, calibration sheets, and sample manifest exist.
- Validation, audit, conversion, annotation-agreement, and rule-baseline scripts exist.
- The synthetic dataset/audit/baseline dry run completed successfully.
- The authorized pilot execution plan, work-order template, result-summary template, and authorization register exist.
- The annotator onboarding and annotation QA package exists.
- A staged 500-item expansion plan exists, but immediate unlimited 500-item collection is rejected or paused.
- The post-pilot analysis and decision framework exists.
- The source intake and sampling-frame package exists.
- The integrated real-pilot readiness review package exists.
- The stakeholder authorization packet and decision-record template exist.
- The approved pilot launch packet exists under `governance/pilot-launch/`.
- The first real 50-item pilot is approved for `go_with_limits` launch preparation.
- A controlled rehearsal review template and protocol now exist to turn the first 1-2 rehearsal items into a repo-safe decision before the first 10-15 item checkpoint.
- The first 10-15 item checkpoint protocol exists.
- A local-only pilot workspace initializer exists and has created ignored `data/interim/` working files after controlled launch confirmation.
- A repo-safe pilot preflight verifier exists and the before-item-1 check has passed with `ERROR: 0`.
- A synthetic-only integrated launch rehearsal has exercised manual build, validation, calibration, audit, baseline, reviewer packet, and synthesis tooling.
- The outside-git controlled launch record has been confirmed with final status `ready_for_first_10_15_items`.
- A non-sensitive controlled launch record now records CIB authorization for API access and all research-required automation under explicit run-record, storage, access, retention, and redaction controls.
- The consolidated research day note is [notes/2026-04-23-research-day-notes.md](notes/2026-04-23-research-day-notes.md).
- Item-level controlled pilot artifacts, if present, live only in the outside-git controlled store; no raw or controlled Threads evidence is committed to this repo.
- The first 15 controlled local records have been collected under ignored `data/interim/`, built, strict-validated, and summarized in repo-safe aggregate notes.
- The first 15-item aggregate remains low-risk skewed: 14 `non_scam`, 1 adjudicated `uncertain`, 0 `scam`, and 0 medium/high-risk records.
- Risk-probe runs 0005 and 0006 tested domain plus signal-family seeds, but public unauthenticated browser-rendered search returned no extractable item content.
- Approved browser-session execution, scoped reply/link evidence runs, confirmed-pointer intake, account-source context, and a hard-negative anti-scam warning example have now produced a 42-record strict-valid checkpoint.
- The repo-safe run index is [governance/pilot-launch/run_index.md](governance/pilot-launch/run_index.md).
- The 42-record checkpoint synthesis is [experiments/evaluation-notes/0064-checkpoint-0042-synthesis.md](experiments/evaluation-notes/0064-checkpoint-0042-synthesis.md).
- Decision 0058 selects a temporary collection pause and starts the CIB/165-facing checkpoint report v0.1: [reports/threads-scam-content-checkpoint-0042-v0.1.md](reports/threads-scam-content-checkpoint-0042-v0.1.md).
- The stakeholder decision request is [reports/checkpoint-0042-decision-request.md](reports/checkpoint-0042-decision-request.md).
- The stakeholder handoff note is [reports/checkpoint-0042-stakeholder-handoff-note.md](reports/checkpoint-0042-stakeholder-handoff-note.md).
- The stakeholder decision record is [governance/pilot-launch/checkpoint_0042_stakeholder_decision_record.md](governance/pilot-launch/checkpoint_0042_stakeholder_decision_record.md).
- Decision 0059 selects Option A and opens a bounded prospective item `0046-0055` tranche: [governance/pilot-launch/threads_pilot_v1_2026-05_option_a_limited_browser_tranche_run_record_0038.md](governance/pilot-launch/threads_pilot_v1_2026-05_option_a_limited_browser_tranche_run_record_0038.md).
- Checkpoint `0042` contains 14 `scam` / high-risk records, 22 `non_scam`, 5 `uncertain`, and 1 `insufficient_evidence`.
- Option A run 0038 then selected items `0046-0055` from 20 browser-session candidates; after strict validation and second review, the 55-record aggregate contains 17 `scam`, 23 `non_scam`, 9 `uncertain`, and 6 `insufficient_evidence`.
- The 55-record checkpoint synthesis is [experiments/evaluation-notes/0068-checkpoint-0055-synthesis.md](experiments/evaluation-notes/0068-checkpoint-0055-synthesis.md).
- Decision 0061 selects the 55-record CIB/165-facing checkpoint report package: [reports/threads-scam-content-checkpoint-0055-v0.1.md](reports/threads-scam-content-checkpoint-0055-v0.1.md).
- Decision 0067 adds the approved package index: [reports/checkpoint-0055-approved-package-index.md](reports/checkpoint-0055-approved-package-index.md).
- The checkpoint 0042 baseline is high-recall research triage: precision 0.700, recall 1.000, F1 0.824, 6 false positives, and 0 false negatives.
- The 55-record baseline smoke result is precision 0.708, recall 1.000, F1 0.829, 7 false positives, and 0 false negatives.
- The hard-negative lesson is explicit: anti-scam warning content is not scam content unless the item itself introduces a conversion path.
- Local item `0076` extends this hard-negative lesson as `non_scam` / `low`; the 76-record local aggregate is strict-valid and does not add scam/high-risk evidence.
- Checkpoint `0081` is now CIB-approved as a 78-record research checkpoint: 36 `scam`, 24 `non_scam`, 13 `uncertain`, and 5 `insufficient_evidence`.
- The checkpoint 0081 baseline smoke result is precision 0.829, recall 0.944, F1 0.883, 7 false positives, and 2 false negatives on 60 binary-evaluable items.

The next blocker is no longer basic access-path readiness, A/B checkpoint selection, run 0038 execution, checkpoint 0055 report drafting, C1/C2/C3 selection, reviewer approval, local item `0076` inclusion, or checkpoint 0081 synthesis approval. Raw evidence, credentials, session artifacts, and sensitive item-level outputs must stay outside git. Do not move to item `0082`, broad crawler expansion, embedding experiments, or model training until a later checkpoint decision records scope, source mix, content-form mix, evidence mix, and governance limits.

The immediate next step is no longer generic operational-readiness planning or final-gate package polishing. CIB/internal adoption is recorded as `accepted_with_conditions`, technical/governance review accepted the investment-scam discovery method design for next-decision planning, and decision `0121` now records final-gate response. The current action is controlled execution planning: complete the Track A start checklist, run the zero-new-evidence dry run after checklist completion, and keep Track B blocked until all hard conditions are green. Confirmed pointers remain a possible future source only inside the approved Track B source-arm design or a later capped decision.

Decision 0115 realigns the repo around the first-principle discovery-method goal: future work should explain how it advances scalable, stable, and reviewable discovery of Threads investment-scam candidates. Package, governance, readiness, and shadow-pilot artifacts are support structures for that goal, not the final goal by themselves.

Decision 0116 opens the design-only method-test charter draft at [reports/checkpoint-0081-investment-scam-discovery-method-test-charter-draft.md](reports/checkpoint-0081-investment-scam-discovery-method-test-charter-draft.md) and the signal-family matrix at [docs/57-investment-scam-discovery-signal-family-matrix.md](docs/57-investment-scam-discovery-signal-family-matrix.md). Decision 0117 records technical/governance `approve_design_for_next_decision` for that design package. Decision 0118 opens a `draft_only` capped investment-scam discovery method-test decision with proposed source arms, caps, schema fields, reviewer workflow, hard-negative protections, metrics thresholds, stop rules, legal/privacy gates, controlled-store handling, and aggregate reporting requirements.

Decision 0118 is not executable. Decision 0119 opens a review-only package for decision `0118` so technical/governance and legal/privacy reviewers can decide whether the capped method-test draft can proceed toward a future execution-gate review. Decision 0120 opens final execution authorization package preparation and splits the possible execution into Track A zero-new-evidence dry run and Track B capped live candidate-discovery method test.

Decision 0121 records the final gate reviewer response as `approve_track_a_now_track_b_after_conditions`. Track A start checklist is complete and the zero-new-evidence dry-run report is [reports/checkpoint-0081-track-a-zero-new-evidence-dry-run-report.md](reports/checkpoint-0081-track-a-zero-new-evidence-dry-run-report.md). Track B is conditionally approved but remains blocked until [reports/checkpoint-0081-track-b-capped-live-method-test-condition-checklist.md](reports/checkpoint-0081-track-b-capped-live-method-test-condition-checklist.md) is fully green. Use [reports/checkpoint-0081-track-b-condition-response-request.md](reports/checkpoint-0081-track-b-condition-response-request.md) to collect repo-safe responses, then record accepted responses in [reports/checkpoint-0081-track-b-condition-resolution-tracker.md](reports/checkpoint-0081-track-b-condition-resolution-tracker.md). This is controlled execution planning, not item `0082`, open-ended collection, crawler expansion, model training, production detection, legal fraud determination, public release, automated enforcement, or raw evidence in git.

The Phase 1 operational spine is [docs/29-authorized-pilot-execution-plan.md](docs/29-authorized-pilot-execution-plan.md). The current launch decision note is [notes/phase1-launch-decisions.md](notes/phase1-launch-decisions.md), and the launch readiness note is [experiments/evaluation-notes/0007-phase1-pilot-launch-readiness.md](experiments/evaluation-notes/0007-phase1-pilot-launch-readiness.md).

## Recommended First Milestone

By `2026-04-30`, produce the readable report v0 above. Within the following 4 weeks, produce:

1. A finalized phase-1 taxonomy and annotation guide.
2. Controlled launch details for exact source, storage, access, retention, and redaction limits.
3. Local-only working files initialized under ignored `data/interim/`, pilot preflight passed, controlled browser-rendered rehearsal completed, 42 controlled records strict-validated, run index created, and checkpoint synthesis reviewed before further collection.
4. A rule-baseline comparison across text, OCR, replies, and visible link/redirection signals only after labels and evidence fields are stable enough.
5. A decision memo deciding whether to continue to 50, continue with limits, pause, revise the guideline, revise the schema, or narrow sources.
6. A 100-200 item first usable dataset only after pilot review and revisions justify expansion.

Recommended first dataset slice:

- 5 synthetic or redacted calibration items.
- 10-15 real checkpoint items before completing the conditional 50-item pilot; this lower-bound checkpoint is complete, but high-risk case-finding still needs a method study before item 16.
- 100-200 manually reviewed examples only after pilot review justifies expansion.
- Include likely scam-like, likely non-scam, uncertain, and insufficient-evidence cases.
- Cover text-only posts, text plus image posts, comments/replies, OCR text, and visible redirection or link signals.

Recommended first experiment:

- Compare a text-only keyword/rule baseline against a text plus OCR plus comment/link-signal rule baseline.
- Evaluate not only precision, recall, and F1, but also reviewer burden, evidence completeness, explainability, and ambiguity handling.
