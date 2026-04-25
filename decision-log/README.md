# Decision Log

Use this directory for durable decisions that change scope, data handling, labels, experiment direction, budget assumptions, or prototype boundaries.

Decision records should include:

- Date
- Decision
- Context
- Options considered
- Rationale
- Consequences
- Follow-up owner or next review point

Do not silently expand the project into production detection, automated collection, or heavy ML work. Record the decision first.

## Index

| Date | Decision | Record |
|---|---|---|
| 2026-04-23 | Created the Threads-first phase-1 research scaffold and accepted text/OCR/comments/link-signal triage as the initial research MVP direction | `0001-initial-threads-first-research-scaffold.md` |
| 2026-04-23 | Created an April 30 CIB/165-facing Threads report v0 deadline and report package | `0002-create-report-v0-deadline.md` |
| 2026-04-23 | Added a pilot readiness and authorization gate before any real Threads examples are collected or annotated | `0003-pilot-readiness-and-authorization-gate.md` |
| 2026-04-23 | Ran a synthetic workflow dry run before any real pilot data collection | `0004-run-synthetic-workflow-dry-run-before-real-pilot.md` |
| 2026-04-23 | Prepared a post-authorization pilot execution package without starting real collection | `0005-prepare-authorized-pilot-execution-package.md` |
| 2026-04-23 | Added annotator onboarding and annotation QA gates before baseline-ready labels | `0006-add-annotation-onboarding-and-qa-gate.md` |
| 2026-04-23 | Rejected unlimited immediate 500-item collection and replaced it with a staged expansion plan | `0007-reject-unlimited-500-item-collection.md` |
| 2026-04-23 | Added a pilot analysis decision framework before expansion beyond the first real pilot | `0008-add-pilot-analysis-decision-framework.md` |
| 2026-04-23 | Added a source intake and sampling-frame gate before real source collection | `0009-add-source-intake-sampling-frame.md` |
| 2026-04-23 | Added an integrated real-pilot readiness review before any real 50-item pilot begins | `0010-add-real-pilot-readiness-review.md` |
| 2026-04-23 | Added a stakeholder authorization packet and decision record before real source approval | `0011-add-stakeholder-authorization-packet.md` |
| 2026-04-23 | Recorded approved pilot launch preparation with `go_with_limits` launch records | `0012-record-approved-pilot-launch-prep.md` |
| 2026-04-23 | Added a required first 10-15 item checkpoint before completing the 50-item pilot | `0013-add-first-pilot-checkpoint-protocol.md` |
| 2026-04-23 | Added a local pilot workspace initializer for ignored `data/interim/` working files | `0014-add-local-pilot-workspace-initializer.md` |
| 2026-04-23 | Added a mechanical pilot preflight verifier before item 1 | `0015-add-pilot-preflight-verification.md` |
| 2026-04-23 | Rejected low-speed automated Threads/Meta collection without recorded legal/platform/stakeholder scope | `0016-reject-low-speed-automation-without-scope.md` |
| 2026-04-23 | Recorded the integrated synthetic launch rehearsal while keeping real collection blocked until controlled launch details are complete | `0017-record-integrated-synthetic-launch-rehearsal.md` |
| 2026-04-23 | Recorded CIB authorization for API access and all research-required automation under a controlled launch record | `0018-record-cib-api-and-automation-authorization.md` |
| 2026-04-23 | Corrected controlled-store status so real controlled pilot artifacts are not mislabeled as examples or synthetic files | `0019-correct-controlled-store-artifact-status.md` |
| 2026-04-23 | Added a repo-safe controlled rehearsal review bridge before the first 10-15 item checkpoint | `0020-add-controlled-rehearsal-review-bridge.md` |
| 2026-04-24 | Recorded CIB-approved rehearsal intake readiness while keeping the first checkpoint blocked until one controlled item is built and strict-validated | `0021-record-cib-approved-rehearsal-intake-ready.md` |
| 2026-04-24 | Accepted a controlled low-speed crawler as the next practical acquisition path under the existing CIB-authorized automation scope | `0022-record-controlled-low-speed-crawler-path.md` |
| 2026-04-24 | Required a controlled risk-probe method before item 16 after the first 15 records yielded no high-risk examples | `0023-require-risk-probe-method-before-item-16.md` |
| 2026-04-24 | Required approved session/API risk-probe access after public browser-rendered risk probes returned no extractable item content | `0024-require-approved-session-or-api-risk-probe-access.md` |
| 2026-04-25 | Prepared controlled browser storage-state and API/session-aware access paths while keeping secrets and raw output outside git | `0025-prepare-controlled-session-api-access-path.md` |
| 2026-04-25 | Required method revision after run 0010 exhausted all five item 0017 seeds without selecting a safe redacted item | `0026-require-method-revision-after-run-0010.md` |
| 2026-04-25 | Paused the text-only item 0017 extension and required a scoped evidence-path study before any further item 0017 attempt | `0027-pause-text-only-item-0017-extension.md` |
| 2026-04-25 | Selected a scoped evidence-path study using domain-only link/redirect-category evidence plus narrow reply-context feasibility before any further item 0017 attempt | `0028-select-scoped-evidence-path-study.md` |
| 2026-04-25 | Stopped the item 0017 extension for the current pilot tranche after run 0013 produced no reviewable candidate under the scoped evidence-path boundaries | `0029-stop-item-0017-extension-after-run-0013.md` |
| 2026-04-25 | Required a stakeholder evidence-scope review gate before any item 0017 retry, item 0018 attempt, or high-risk evidence-expansion collection run | `0030-require-stakeholder-evidence-scope-review.md` |
| 2026-04-25 | Recorded stakeholder approval for all proposed evidence families while preserving run-level limits and raw-data boundaries before item 0018 | `0031-record-stakeholder-evidence-expansion-approval.md` |
| 2026-04-25 | Closed run 0015 for collection after its candidate-review cap was exhausted and required a new bounded run design before item 0024 | `0032-close-run-0015-and-require-new-run-design.md` |
| 2026-04-25 | Closed run 0016 for collection after item 0027 and required a method decision before item 0028 | `0033-close-run-0016-and-require-method-decision-before-item-0028.md` |
| 2026-04-25 | Selected API/session-aware readiness or targeted redacted exemplars as the required method before item 0028 | `0034-select-api-or-targeted-exemplar-method-before-item-0028.md` |
| 2026-04-25 | Paused collection by default and selected checkpoint report v0.1 after the 42-record synthesis | `0058-select-checkpoint-report-v0-1-after-0042-synthesis.md` |
| 2026-04-25 | Selected Option A: limited approved-browser-session tranche for prospective items 0046-0055 | `0059-select-option-a-limited-browser-tranche-after-checkpoint-0042.md` |
| 2026-04-25 | Closed Option A run 0038 after it reached 20 reviewed candidates and 10 selected items | `0060-close-option-a-run-0038-after-caps.md` |
| 2026-04-25 | Selected the 55-record CIB/165-facing checkpoint report package and blocked item 0056 until a new decision is recorded | `0061-select-checkpoint-0055-report-package.md` |
| 2026-04-25 | Selected C2: keep collection paused and review/refine the 55-record checkpoint report package | `0062-select-c2-checkpoint-0055-report-review.md` |
| 2026-04-25 | Refined the checkpoint 0055 report language after C2 so reviewers see report review as the active path | `0063-refine-checkpoint-0055-report-after-c2.md` |
| 2026-04-25 | Added role-specific checkpoint 0055 review questions for the selected C2 report-review path | `0064-add-checkpoint-0055-review-questions.md` |
| 2026-04-25 | Added a short checkpoint 0055 executive addendum for CIB/165-facing C2 review | `0065-add-checkpoint-0055-executive-addendum.md` |
| 2026-04-25 | Recorded that all reviewer roles approved the checkpoint 0055 package under C2 | `0066-record-checkpoint-0055-reviewer-approval.md` |
| 2026-04-25 | Added the canonical approved-package index for checkpoint 0055 delivery and handoff | `0067-add-checkpoint-0055-approved-package-index.md` |
| 2026-04-25 | Aligned the README and recommended path so the approved checkpoint 0055 package index is the main entry point | `0068-align-readme-and-recommended-path-to-approved-package.md` |
