# Initial Thinking

## Why The Project Narrowed To Threads

The earlier research direction considered scam-like advertising and ad-adjacent content across Meta platforms. Recent stakeholder discussion changed the practical priority: Threads appears to receive a high volume of scam-content reports, and therefore provides a sharper starting point for research.

Trying to cover all Meta platforms at once would create too much variation in formats, access paths, policies, evidence types, and review workflows. Threads-first scope gives the project a narrower research surface while still preserving operational relevance.

## What Changed After Stakeholder Discussion

The project is no longer framed as a broad Meta scam-ad detection effort. The new project centers on Threads-related scam or scam-like content, especially:

- Text posts
- Text plus image posts
- Replies and comments
- Visible redirection signals
- External links when present
- OCR text from attached images

Video-heavy and deepfake-heavy workstreams are deferred because they are expensive, annotation-heavy, and unlikely to be the fastest path to a defensible phase-1 result.

## Current Strategic Judgment

The strongest first move is to build a high-quality research scaffold:

- Define what counts as scam-like content for research purposes.
- Preserve uncertainty and evidence quality.
- Create annotation rules that reviewers can actually follow.
- Build a small, balanced sample.
- Compare simple baselines before reaching for heavy models.

The first useful output is not a production detector. It is a defensible decision package showing which signals are worth further investment under the NTD 1.8M budget constraint.

## What Was Set Up On 2026-04-23

The Threads-first repo was created as a sibling of both `planning-everything-track` and `meta-scam-ad-research-2026`.

Created today:

- README and AGENTS instructions.
- Project charter, problem framing, scope matrix, taxonomy, annotation guideline, data strategy, dataset schema, baseline strategy, experiment plan, evaluation framework, budget fit, system concept, risk register, decision memo, 4-week plan, stakeholder questions, recommended path, Codex workflow, repo-series naming, and repo-relationship docs.
- Machine-readable schema: `data-contracts/thread_item_schema_v1.json`.
- Templates: `templates/annotation_sheet_template.csv` and `templates/experiment_log_template.md`.
- Governance note: `governance/data-governance.md`.
- Experiment folders for baselines, modality studies, and evaluation notes.
- Decision record: `decision-log/0001-initial-threads-first-research-scaffold.md`.

## Repo Relationship Judgment

The repo connection should stay thin:

```text
planning-everything-track = priority / status / capacity / next action
meta-scam-ad-research-2026 = umbrella strategy / broad Meta scope / decision memory
meta-threads-scam-content-research-2026 = Threads execution / schema / annotation / experiments / evaluation
```

This avoids turning the work into a duplicated documentation pile. Use links and decision records, not submodules or sync scripts.

## Immediate Next Research Move

The next useful research move is not code. It is a CIB/165-facing Threads research report `v0` due `2026-04-30`.

The report is the right next artifact because it turns a stakeholder signal into a defensible research object:

- stakeholder report pressure is not a verified dataset
- scam-like content must preserve uncertainty and evidence quality
- the NTD 1.8M budget fits governed research, not full production detection
- real collection should wait for authorization and redaction rules
- the first experiment should compare evidence surfaces, not claim final truth

The report package created on `2026-04-23`:

- `reports/README.md`
- `reports/threads-scam-content-research-v0.md`
- `decision-log/0002-create-report-v0-deadline.md`
- `notes/2026-04-23-cib-165-report-v0-direction.md`

Planning was also updated so W18 contains named report blocks and a deadline checkpoint. Google Calendar creation was attempted but blocked by connector unsupported-tool errors, so the planning repo now contains an `.ics` import fallback.

After the report v0 package was assembled, the next research move became pilot authorization and synthetic workflow QA:

- 5 synthetic or redacted calibration items before real evidence.
- 50 authorized pilot items after authorization, go/no-go, and readiness-review gates.
- 100-200 first usable items after pilot review and any guideline/schema revisions.
- Balanced likely scam-like, likely non-scam, uncertain, and insufficient-evidence examples.
- Include text-only, text plus image/OCR, replies/comments, visible links, and redirection signals.
- First experiment: text-only keyword/rule baseline versus text plus OCR plus comments/link-signal baseline.

## Later Same-Day Status

By the next update on `2026-04-23`, the repo had these additional research assets:

- Report-v0 executive brief, review checklist, delivery plan, and feedback template.
- Stakeholder pilot kickoff, go/no-go checklist, and pilot-readiness decision record.
- Synthetic sample manifest.
- Synthetic dataset audit dry-run log.
- Synthetic rule-baseline dry-run log.
- Synthetic dry-run summary doc.
- Calibrated rule baseline after dry-run inspection.
- Authorized pilot execution plan, work-order template, result-summary template, authorization register, and pilot execution decision record.
- Annotator onboarding quickstart, annotation QA plan, QA checklist, onboarding checklist, and guideline revision log template.
- 500-item expansion plan and decision record rejecting unlimited immediate collection.
- Pilot analysis and decision framework, decision memo template, error review table, and decision-analysis protocol.
- Source intake and sampling-frame package for evaluating candidate sources before collection.
- Integrated real-pilot readiness review package tying source, governance, annotation, QA, and baseline gates together.
- Stakeholder authorization packet and decision-record template for turning the next approval meeting into a recorded source decision.
- Approved pilot launch packet with `go_with_limits` records under `governance/pilot-launch/`.

The main conclusion is that the repo is ready for stakeholder review and authorized pilot setup, but not for real Threads collection yet.

The synthetic dry run validated the local workflow:

- 5 synthetic CSV records validated with 0 errors and 0 warnings.
- 5 synthetic JSON records validated with 0 errors and 0 warnings.
- Conversion to JSONL worked.
- Audit correctly flagged synthetic-only source skew.
- Rule variants showed expected evidence-surface behavior on synthetic examples.

The dry-run metrics are not real-world performance claims. They only show the scripts and data contracts are coherent enough to use once authorized pilot data exists.

## Same-Day Git Checkpoints

Threads repo:

- `be5f2b5 docs: initialize Threads scam content research repo`
- `653e679 docs: align Threads taxonomy vocabulary`
- `ee3b2d5 templates: add pilot governance and annotation forms`
- `3f4d8ed data: add synthetic calibration sample sheets`
- `aa06301 scripts: add dataset QA and baseline tooling`
- `886c719 docs: add pilot runbooks and governance SOP`
- `a0f7851 experiments: add pilot audit and baseline protocols`
- `4deb071 docs: create CIB 165 Threads report v0 package`
- `bc05600 docs: add report v0 review package`
- `952ca09 docs: add pilot readiness gate`

Uncommitted same-day work at this note update:

- Synthetic sample manifest.
- Synthetic dry-run result docs.
- Synthetic audit and baseline experiment logs.
- Rule-baseline calibration from synthetic dry-run findings.

Planning repo:

- `13b60ea plan: record Threads research repo bridge`
- `67559f3 plan: update Threads research next action`
- `ca9c65d plan: schedule CIB 165 Threads report v0`
