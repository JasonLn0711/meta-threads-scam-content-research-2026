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

## Recommended First Milestone

Within 4 weeks, produce:

1. A finalized phase-1 taxonomy and annotation guide.
2. A first manually reviewed dataset slice of 100 to 150 Threads-related items.
3. A rule-based text baseline.
4. An OCR and comment/link signal augmentation comparison.
5. An evaluation memo deciding whether to continue, add LLM-assisted review, or cut scope further.

Recommended first dataset slice:

- 100 to 150 manually reviewed examples.
- Include likely scam-like, likely non-scam, uncertain, and insufficient-evidence cases.
- Cover text-only posts, text plus image posts, comments/replies, OCR text, and visible redirection or link signals.

Recommended first experiment:

- Compare a text-only keyword/rule baseline against a text plus OCR plus comment/link-signal rule baseline.
- Evaluate not only precision, recall, and F1, but also reviewer burden, evidence completeness, explainability, and ambiguity handling.
