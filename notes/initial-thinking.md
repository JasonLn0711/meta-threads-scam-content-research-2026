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

After the report v0 is assembled, the next research move is the first dataset-slice design:

- 100 to 150 manually reviewed Threads-related items.
- Balanced likely scam-like, likely non-scam, uncertain, and insufficient-evidence examples.
- Include text-only, text plus image/OCR, replies/comments, visible links, and redirection signals.
- First experiment: text-only keyword/rule baseline versus text plus OCR plus comments/link-signal baseline.

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

Planning repo:

- `13b60ea plan: record Threads research repo bridge`
- `67559f3 plan: update Threads research next action`
- `ca9c65d plan: schedule CIB 165 Threads report v0`
