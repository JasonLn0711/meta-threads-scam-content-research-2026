# Decision 0001: Initial Threads-First Research Scaffold

## Identity

- Date: 2026-04-23
- Status: accepted
- Owner: Jason

## Decision

Create `meta-threads-scam-content-research-2026` as the active phase-1 execution repo for Threads-related scam or scam-like content research.

The repo should be documentation-first, research-second, and code-third. Its first useful output is a defensible research scaffold, not a production detector.

## Context

The broader Meta scam-ad research opportunity was first captured in `../meta-scam-ad-research-2026`. Same-day stakeholder reasoning narrowed the active phase-1 surface to Threads because Threads appears to receive the highest immediate scam-content report pressure.

The NTD 1.8 million budget is better spent on careful problem definition, lawful data strategy, annotation, signal taxonomy, simple baselines, and human-review-oriented evaluation than on broad platform integration, heavy video analysis, deepfake detection, or production deployment.

## Scope Accepted For Phase 1

Include:

- Threads text posts.
- Text plus image posts.
- Replies and comments.
- OCR text from images and screenshots.
- Visible redirection signals.
- External links when present.
- Human-review-oriented risk triage and explainable reasons.

Defer:

- Long video.
- Heavy short-video pipelines.
- Deepfake detection as a mainline workstream.
- Full Meta cross-platform integration.
- Automated collection.
- Production deployment.
- Heavy model training.

## Rationale

Text, OCR, comments, and link/redirection signals are low-cost, reviewable, and likely to expose scam-like lures. They also support clear ablation experiments:

- Text-only versus text plus OCR.
- Post-only versus post plus comments.
- Rule-based versus LLM-assisted versus hybrid.
- Binary classification versus risk triage.
- With-link-signals versus without-link-signals.

This gives the research team a way to learn quickly and cut scope if the evidence does not justify further investment.

## Consequences

- This repo owns Threads-specific taxonomy, schema, annotation, experiments, evaluation, and recommended-path docs.
- The umbrella repo `../meta-scam-ad-research-2026` owns broader Meta scam-risk strategy and cross-platform decision memory.
- The planning repo `../planning-everything-track` owns priority, status, capacity, and next action.
- Relationship docs should be used instead of duplicated live artifacts.
- No automated Threads or Meta data collection is approved at initialization.

## Initial Deliverables Created

- README and AGENTS instructions.
- Docs `00` to `21`.
- `data-contracts/thread_item_schema_v1.json`.
- Annotation and experiment templates.
- Governance and data-handling notes.
- Notes and initial thinking.
- Experiments folder structure.
- Repo-series naming guidance.
- Cross-repo relationship document.

## Next Action

After the W17 must outputs are safe, prepare a Threads-first stakeholder scoping memo and define the first 100 to 150 item dataset slice.
