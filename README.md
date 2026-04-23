# Meta Threads Scam Content Research 2026

## Problem Statement

This repository supports a Threads-first research program for studying scam or scam-like content on Meta Threads. The goal is to define the problem carefully, structure evidence, annotate examples, build defensible early baselines, and progressively narrow toward a budget-fit research MVP.

The project asks:

> What is the most realistic, evidence-driven, budget-fit way to study and prototype scam-content triage on Threads, starting from text, images, replies, OCR text, and visible redirection signals?

This is not a production detector and does not make legal determinations. It is a research scaffold for risk triage, evidence design, and early experimental comparison.

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

The first useful output should be a defensible research package:

- A stable dataset schema
- A scam-risk taxonomy
- An annotation guide
- A small reviewed sample
- Simple baselines
- A comparison of text, OCR, comment, and link signals
- A decision memo on what to continue, cut, or defer

## Scope Summary

Included in phase 1:

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
- [reports/report-v0-review-checklist.md](reports/report-v0-review-checklist.md)
- Target date: `2026-04-30`
- Status: research report v0, not a production detector or legal fraud determination

This supersedes a concept-only stakeholder scoping memo as the next research artifact.

## Current Research Status

As of `2026-04-23`, the repo has moved from scaffold-only to approved pilot launch preparation:

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
- The first 10-15 item checkpoint protocol exists.
- A local-only pilot workspace initializer exists and has created ignored `data/interim/` working files after controlled launch confirmation.
- A repo-safe pilot preflight verifier exists and the before-item-1 check has passed with `ERROR: 0`.
- A synthetic-only integrated launch rehearsal has exercised manual build, validation, calibration, audit, baseline, reviewer packet, and synthesis tooling.
- The outside-git controlled launch record has been confirmed with final status `ready_for_first_10_15_items`.
- A non-sensitive controlled launch record now records CIB authorization for API access and all research-required automation under explicit run-record, storage, access, retention, and redaction controls.
- The consolidated research day note is [notes/2026-04-23-research-day-notes.md](notes/2026-04-23-research-day-notes.md).
- Item-level controlled pilot artifacts, if present, live only in the outside-git controlled store; no raw or controlled Threads evidence is committed to this repo.

The next blocker is operational practice, not tooling: continue the 1-2 item controlled rehearsal under the controlled limits, validate local records, review redaction quality, confirm calibration if annotators changed, and then collect only the first 10-15 items before the checkpoint. The rehearsal may use the intended manual, API, or automation path, but raw evidence, credentials, session artifacts, and sensitive item-level outputs must stay outside git. Do not complete the 50-item pilot until the checkpoint decision is `continue_to_50` or `continue_with_limits`.

The Phase 1 operational spine is [docs/29-authorized-pilot-execution-plan.md](docs/29-authorized-pilot-execution-plan.md). The current launch decision note is [notes/phase1-launch-decisions.md](notes/phase1-launch-decisions.md), and the launch readiness note is [experiments/evaluation-notes/0007-phase1-pilot-launch-readiness.md](experiments/evaluation-notes/0007-phase1-pilot-launch-readiness.md).

## Recommended First Milestone

By `2026-04-30`, produce the readable report v0 above. Within the following 4 weeks, produce:

1. A finalized phase-1 taxonomy and annotation guide.
2. Controlled launch details for exact source, storage, access, retention, and redaction limits.
3. Local-only working files initialized under ignored `data/interim/`, pilot preflight passed, 1-2 item manual collection rehearsal completed, 5-item calibration completed, then a 10-15 item checkpoint before completing the conditional 50-item pilot.
4. A rule-baseline comparison across text, OCR, replies, and visible link/redirection signals only after labels and evidence fields are stable enough.
5. A decision memo deciding whether to continue to 50, continue with limits, pause, revise the guideline, revise the schema, or narrow sources.
6. A 100-200 item first usable dataset only after pilot review and revisions justify expansion.

Recommended first dataset slice:

- 5 synthetic or redacted calibration items.
- 10-15 real checkpoint items before completing the conditional 50-item pilot.
- 100-200 manually reviewed examples only after pilot review justifies expansion.
- Include likely scam-like, likely non-scam, uncertain, and insufficient-evidence cases.
- Cover text-only posts, text plus image posts, comments/replies, OCR text, and visible redirection or link signals.

Recommended first experiment:

- Compare a text-only keyword/rule baseline against a text plus OCR plus comment/link-signal rule baseline.
- Evaluate not only precision, recall, and F1, but also reviewer burden, evidence completeness, explainability, and ambiguity handling.
