# 2026-04-23 Research Day Notes

## Day Thesis

Today moved the Threads scam-content research project from a broad idea into a governed, executable research package.

The important shift was not "build more tooling." The important shift was defining what must be true before real Threads evidence can be collected, annotated, and used for baseline claims.

Current status: the repo is structurally ready for a bounded first pilot, but item 1 remains blocked until controlled launch details are completed outside git.

## First-Principles Frame

The project should be driven by first principles:

1. Research claims require evidence, provenance, and uncertainty.
2. Real platform content creates privacy, legal, and safety duties before it creates model opportunities.
3. A useful phase-1 result is a defensible human-review research package, not a production detector.
4. Annotation quality must come before model evaluation.
5. Small controlled batches reveal schema, redaction, source, and label failures faster than large collection.
6. Simple baselines are the right first test because they expose whether text, OCR, replies, and visible redirection signals carry useful evidence.
7. Scale is earned by passing gates; it is not granted by enthusiasm or availability of content.

From those principles, the current project design follows:

- Threads-first scope because stakeholder context points there and the evidence forms are tractable.
- Text, OCR, replies, and visible redirection signals are first-class because they are reviewable and budget-fit.
- Long video, deepfake detection, cross-platform integration, and automation are deferred because they are not required to answer the phase-1 question.
- A 50-item pilot comes before 100-200 items, and 100-200 comes before any governed 500-item expansion.
- Real evidence stays out of git.
- Suspicion is preserved as suspicion; the project does not make legal fraud determinations.

## What Was Built Today

The repo now contains the core phase-1 research package:

- Threads-first project framing, scope, and recommended path.
- Dataset schema v1 and labeling schema v1.
- Annotation guideline v1 and scam-risk taxonomy.
- Flat CSV and JSON-compatible data contracts.
- Annotation, adjudication, collection-log, redaction, and pilot-result templates.
- Synthetic/redacted sample records for dry-run use only.
- Data governance, collection/redaction SOP, pilot runbook, go/no-go checklist, and readiness review flow.
- CIB/165-facing report v0 package with executive brief, checklist, delivery plan, and feedback template.
- Synthetic workflow dry run and local experiment notes.
- Validation, audit, conversion, annotation agreement, calibration-file, rule-baseline, rule-variant comparison, local-workspace, and preflight scripts.
- Annotator onboarding and annotation QA package.
- Source intake and sampling-frame package.
- Stakeholder authorization packet, approval records, and approved launch packet under `governance/pilot-launch/`.
- First 10-15 item checkpoint protocol.
- Local-only pilot workspace initializer.
- Repo-safe item-1 preflight verifier.

## Key Decisions Recorded

The durable decision path now says:

- Start with Threads, not all Meta platforms.
- Treat the work as research triage, not production enforcement.
- Use text, image/OCR, replies, visible links, and redirection signals as phase-1 evidence surfaces.
- Use a four-label annotation set: `scam`, `non_scam`, `uncertain`, `insufficient_evidence`.
- Preserve risk level, evidence sufficiency, signal tags, confidence, review status, and final adjudicated labels.
- Reject immediate unlimited 500-item real collection.
- Use a staged path: synthetic dry run, 50-item governed pilot, 100-200 item first usable dataset, then possible 500-item expansion.
- Require controlled launch details outside git before real item 1.
- Require a 10-15 item checkpoint before completing the 50-item pilot.
- Require local preflight before item 1.

## Verification Snapshot

Current repo verification on `2026-04-23`:

- Git worktree: clean.
- Latest commit: `0f24e28 scripts: add pilot preflight verifier`.
- Repo-only preflight: `OK: 15`, `WARN: 2`, `ERROR: 0`.
- Expected warnings:
  - local workspace files are not initialized yet
  - controlled launch details cannot be verified from git
- `data/interim/` contains only `data/interim/README.md`.
- No real Threads evidence has been collected or committed.

The warning state is intentional. The repo is allowed to be mechanically ready while real collection remains blocked on controlled human approval details outside git.

## Current Blocker

The project is not blocked by schema, templates, scripts, or launch packet structure.

The project is blocked by the controlled launch record:

- exact source
- exact collection method
- exact raw storage location
- exact access list
- exact retention/deletion rule
- exact redaction limits
- exact treatment of screenshots, source URLs, external links, handles, OCR text, and replies/comments

Those values should remain outside git unless they are fully non-sensitive and explicitly approved for tracking.

## Next Research Move

The next research move is the first controlled 10-15 item pilot checkpoint.

Sequence:

1. Complete the controlled launch record outside git.
2. Assign collector, annotator, reviewer, adjudicator, and research engineer IDs.
3. Initialize local-only pilot files:

```bash
python scripts/init_pilot_workspace.py --ack-controlled-details
```

4. Run item-1 preflight:

```bash
python scripts/check_pilot_preflight.py --before-item-1 --ack-controlled-details
```

5. Collect only the first 10-15 real pilot items under approved limits.
6. Run the first checkpoint before continuing to 50.

## What Not To Do Next

Do not proceed directly to:

- 50 items without the 10-15 item checkpoint
- 100-200 items before pilot analysis
- 500 items before the staged expansion gates
- automated collection
- scraping, crawling, browser automation, profile review, redirect-chain capture, or landing-page crawling
- production scoring
- public claims about scam prevalence or platform rates

## Practical Lesson From Today

The repo now has enough structure to stop generating more abstract planning docs by default. The next learning has to come from a small, governed real-world contact with evidence.

That contact should be deliberately narrow, auditable, and reversible: first 10-15 items, checkpoint, then decide.
