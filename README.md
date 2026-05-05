# Meta Threads Scam Content Research 2026

## First Principle

This repo studies how to discover enough review-worthy Threads investment-scam candidates with as little human review burden as possible, under strict governance, hard-negative protection, and aggregate-only reporting.

本 repo 研究的不是單純「找到詐騙」，而是如何在嚴格治理與誤判控制下，用盡可能少的人力，穩定找到足夠多值得審查的 Threads 投資詐騙候選。

## Problem Statement

This repository supports a Threads-first research program for studying scam or scam-like content on Meta Threads. From this point forward, the first-principle goal is:

> Build a scalable, stable, reviewable, and labor-efficient method for discovering enough review-worthy Threads investment-scam candidates with as little human review burden as possible.

This is not merely "find scam posts." The true operational goal is to use a small amount of human labor to find enough candidates worth reviewing.

The project asks:

> What bounded, reviewable candidate-discovery method produces enough review-worthy Threads investment-scam candidates while minimizing reviewer burden, preserving hard-negative boundaries, and keeping evidence handling governance-safe?

This is not a production detector and does not make legal determinations. It is a research scaffold for scalable candidate discovery, risk triage, evidence design, and early experimental comparison.

The current north-star note is [docs/61-labor-efficient-investment-scam-candidate-discovery-north-star.md](docs/61-labor-efficient-investment-scam-candidate-discovery-north-star.md). The Reviewer Assist Layer design is [docs/62-reviewer-assist-layer-design.md](docs/62-reviewer-assist-layer-design.md). The active context-gating policy is [docs/63-context-gating-policy.md](docs/63-context-gating-policy.md). The metadata-safe Evidence Layer v1 design is [docs/65-evidence-layer-v1.md](docs/65-evidence-layer-v1.md). The synthetic closed-loop discovery runner is [docs/66-closed-loop-discovery-v1.md](docs/66-closed-loop-discovery-v1.md). The advanced synthetic discovery layer is [docs/67-advanced-discovery-v2.md](docs/67-advanced-discovery-v2.md). The synthetic concept reasoning layer is [docs/68-concept-reasoning-layer-v1.md](docs/68-concept-reasoning-layer-v1.md). The synthetic dynamic intelligence layer is [docs/69-dynamic-intelligence-layer-v1.md](docs/69-dynamic-intelligence-layer-v1.md). The synthetic predictive simulation layer is [docs/70-predictive-simulation-layer-v1.md](docs/70-predictive-simulation-layer-v1.md). The defensive self-play layer is [docs/71-defensive-self-play-layer-v1.md](docs/71-defensive-self-play-layer-v1.md). The adaptive policy deployment loop is [docs/72-adaptive-policy-deployment-loop-v1.md](docs/72-adaptive-policy-deployment-loop-v1.md). The supporting discovery-method note is [docs/56-first-principle-investment-scam-discovery-method.md](docs/56-first-principle-investment-scam-discovery-method.md).

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
- Discovery-yield and reviewer-burden metrics, including average/median/p95 review time, candidates reviewed per hour, auto-fill and correction rates, full-thread-reading rate, second-review rate, disagreement rate, insufficient-evidence rate, review-worthy yield per source arm, and high-risk yield per reviewer hour
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
data/candidates/  v2 metadata-only candidate records; no raw Threads evidence
data/candidate_intake/ metadata-only manual-assisted fill worksheets
data/evidence_store/ ignored local simulated controlled store; no raw evidence in git
data/learning_state/ ignored local synthetic bandit state and metrics
data/concepts/ ignored local synthetic concept and reasoning logs
data/predictions/ ignored local synthetic predictive simulation logs
data/selfplay/ ignored local defensive self-play simulation logs
data/policy/ ignored local adaptive policy decision, feedback, evaluation, and state logs
data/concept_graph.yaml ignored local synthetic concept graph
data/concept_time_series.yaml ignored local synthetic concept time series
data/adversarial_patterns.yaml ignored local synthetic adversarial findings
meta-system/      v2 sparse schemas and human-reviewed feature evolution metadata
metrics/          v2 aggregate signal scores and reviewer-effort metrics
engine/           v2 metadata-only sparse, embedding, discrepancy, and feature engines
outputs/          whitelisted v2 structured metadata reports only
exploration/      metadata-only exploration tasks; no external access or raw content
scripts/          Minimal utilities only after experiments justify code
src/              Small support prototypes for evidence custody, v2 metadata, and synthetic discovery loops
decision-log/     Durable decisions and scope changes
```

Current code is support tooling only: decision `0135` adds a metadata-safe Evidence Layer v1, decision `0136` adds a synthetic closed-loop discovery runner for query-arm and reviewer-hour learning, decision `0137` adds an advanced synthetic layer with prompt-shaped query generation, deterministic embeddings, clustering, and contextual bandit learning, decision `0138` adds a synthetic concept reasoning layer for cluster-to-concept mapping and conservative novelty routing, decision `0139` adds a dynamic intelligence layer for concept graphs, temporal tracking, evolution edges, and adversarial heuristics, decision `0140` adds a predictive simulation layer for subtle concept mutation, simulated posts, risk scoring, and validation hooks, decision `0141` adds a defensive self-play layer for abstract adversary/detector robustness testing, and decision `0142` adds an adaptive policy deployment loop for shadow/assist/partial metadata routing and safe offline policy updates. These decisions do not authorize external collection, real LLM/API calls, raw evidence in git, final scam determinations, actionable scam content generation, enforcement, or production detection.

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

The immediate next step is no longer generic operational-readiness planning, final-gate package polishing, condition-signoff collection, Day 0 start, Day 1 intake-control setup, primary review for batch `0001`, second review for batch `0001`, generic source-arm selection, batch `0002` candidate surfacing, batch `0002` primary review, or batch `0002` second review. CIB/internal adoption is recorded as `accepted_with_conditions`, technical/governance review accepted the investment-scam discovery method design for next-decision planning, decision `0121` recorded final-gate response, Track A completed a zero-new-evidence dry run, decision `0122` records Track B start authorization after formal signoff, decision `0123` records Track B Day 0 operational start, decision `0124` records Day 1 source-arm intake start, decision `0125` records the first surfaced candidate batch, decision `0126` records primary review for 6 checkpoint-derived seed replay candidates, decision `0127` records second review with 6 final review outcomes, 0 disagreements, and 0 accepted strict-valid records, decision `0128` selects the hard-negative probe arm for batch `0002`, decision `0129` surfaces 10 hard-negative probe candidates, decision `0130` records primary review with 10 initial `non_scam` / `low` hard negatives, 0 hard-negative false positives, and 10 second-review requirements, and decision `0131` records second review with 10 final `non_scam` / `low` hard-negative outcomes, 0 disagreements, 0 hard-negative false positives, and 0 accepted strict-valid records. Decisions `0132` through `0134` move the active v2 layer from balanced source-arm comparison to context-gated reviewer-hour routing: Batch `0009` supports the policy with `high_value_candidates_per_hour: 64.285714` versus Batch `0008` at `21.492537`. The current action is to use that supported policy as the routing base for Reviewer Assist Layer labor-savings evaluation, not to continue hard-negative probing, generic source-arm selection, broad collection, model training, or sparse schema promotion by habit. Confirmed pointers remain a possible source only inside the approved Track B source-arm design or a later capped decision.

Decision 0115 realigns the repo around the first-principle discovery-method goal: future work should explain how it advances scalable, stable, and reviewable discovery of Threads investment-scam candidates. The forward-looking realignment record [decision-log/0129-realign-repo-to-labor-efficient-candidate-discovery.md](decision-log/0129-realign-repo-to-labor-efficient-candidate-discovery.md) adds the labor-efficiency correction: discovery yield and reviewer burden are joint success conditions, not primary and secondary goals. Package, governance, readiness, and shadow-pilot artifacts are support structures for that goal, not the final goal by themselves.

Decision 0116 opens the design-only method-test charter draft at [reports/checkpoint-0081-investment-scam-discovery-method-test-charter-draft.md](reports/checkpoint-0081-investment-scam-discovery-method-test-charter-draft.md) and the signal-family matrix at [docs/57-investment-scam-discovery-signal-family-matrix.md](docs/57-investment-scam-discovery-signal-family-matrix.md). Decision 0117 records technical/governance `approve_design_for_next_decision` for that design package. Decision 0118 opens a `draft_only` capped investment-scam discovery method-test decision with proposed source arms, caps, schema fields, reviewer workflow, hard-negative protections, metrics thresholds, stop rules, legal/privacy gates, controlled-store handling, and aggregate reporting requirements. From this point forward, the same method-test path should also evaluate whether AI/system support can reduce reading, summarization, signal extraction, schema filling, triage, hard-negative review, and repo-safe reporting burden without making final scam determinations. The forward-looking decision file [decision-log/0130-open-reviewer-assist-layer-design.md](decision-log/0130-open-reviewer-assist-layer-design.md) opens [docs/62-reviewer-assist-layer-design.md](docs/62-reviewer-assist-layer-design.md) as the design layer for that assistance without authorizing model training or production deployment.

Decision 0118 is not executable. Decision 0119 opens a review-only package for decision `0118` so technical/governance and legal/privacy reviewers can decide whether the capped method-test draft can proceed toward a future execution-gate review. Decision 0120 opens final execution authorization package preparation and splits the possible execution into Track A zero-new-evidence dry run and Track B capped live candidate-discovery method test.

Decision 0121 records the final gate reviewer response as `approve_track_a_now_track_b_after_conditions`. Track A start checklist is complete and the zero-new-evidence dry-run report is [reports/checkpoint-0081-track-a-zero-new-evidence-dry-run-report.md](reports/checkpoint-0081-track-a-zero-new-evidence-dry-run-report.md). Track B formal signoff is now recorded: legal/privacy status is `no_veto`, CIB/internal owner status is `accepted_boundary`, and the formal signoff summary is [reports/checkpoint-0081-track-b-formal-signoff-summary.md](reports/checkpoint-0081-track-b-formal-signoff-summary.md). Decision 0122 records that Track B may begin under locked caps and stop rules: [decision-log/0122-record-track-b-start-authorization-after-formal-signoff.md](decision-log/0122-record-track-b-start-authorization-after-formal-signoff.md). Decision 0123 records Day 0 operational start and run `0054`: [reports/checkpoint-0081-track-b-day-0-start-record.md](reports/checkpoint-0081-track-b-day-0-start-record.md). Decision 0124 records Day 1 source-arm intake start: [reports/checkpoint-0081-track-b-day-1-source-arm-intake-start.md](reports/checkpoint-0081-track-b-day-1-source-arm-intake-start.md). Decision 0125 records batch `0001`: [reports/checkpoint-0081-track-b-day-1-batch-0001-checkpoint-seed-replay.md](reports/checkpoint-0081-track-b-day-1-batch-0001-checkpoint-seed-replay.md). Decision 0126 records batch `0001` primary review: [reports/checkpoint-0081-track-b-day-1-batch-0001-primary-review.md](reports/checkpoint-0081-track-b-day-1-batch-0001-primary-review.md). Decision 0127 records batch `0001` second review: [reports/checkpoint-0081-track-b-day-1-batch-0001-second-review.md](reports/checkpoint-0081-track-b-day-1-batch-0001-second-review.md). Decisions 0128 and the historical Track B decision 0129 select and surface batch `0002` hard-negative probe candidates: [reports/checkpoint-0081-track-b-day-1-batch-0002-hard-negative-probe-candidates.md](reports/checkpoint-0081-track-b-day-1-batch-0002-hard-negative-probe-candidates.md). Decision 0130 records batch `0002` primary review: [reports/checkpoint-0081-track-b-day-1-batch-0002-primary-review.md](reports/checkpoint-0081-track-b-day-1-batch-0002-primary-review.md). Decision 0131 records batch `0002` second review: [reports/checkpoint-0081-track-b-day-1-batch-0002-second-review.md](reports/checkpoint-0081-track-b-day-1-batch-0002-second-review.md). From this point forward, Track B should be interpreted as testing candidate discovery yield, reviewer burden, hard-negative false-positive pressure, and feasibility of AI/system-assisted reviewer workflow. This is controlled execution under capped method-test conditions, not item `0082`, open-ended collection, crawler expansion, model training, production detection, legal fraud determination, public release, automated enforcement, or raw evidence in git.

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
- Evaluate not only precision, recall, and F1, but also average/median/p95 review time, candidates reviewed per hour, fields auto-filled, fields manually corrected, summary usefulness, full-original-thread-reading rate, second-review rate, reviewer disagreement rate, hard-negative false-positive pressure, insufficient-evidence rate, review-worthy yield per source arm, high-risk yield per reviewer hour, evidence completeness, explainability, and ambiguity handling.
