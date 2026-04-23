# Repo Relationships

## First-Principles Axiom

This repo exists because Threads phase-1 research needs a sharper execution surface than the broader Meta scam-ad umbrella repo can provide.

The first principle is:

```text
One repo, one durable job.
```

This repo's durable job is to own Threads-specific scam-like content research execution: definitions, schema, annotation, experiments, evaluation, and phase-1 narrowing.

## Current Topology

```text
/home/jnln3799/every_on_git_ubuntu/
├── planning-everything-track/
│   └── data/projects/2026-04-meta-scam-ad-research.md
├── meta-scam-ad-research-2026/
│   ├── docs/19-repo-relationships.md
│   └── decision-log/0004-create-threads-first-child-repo.md
└── meta-threads-scam-content-research-2026/
    ├── docs/21-repo-relationships.md
    ├── docs/09-phase-1-experiment-plan.md
    ├── docs/18-recommended-path-v1.md
    └── data-contracts/thread_item_schema_v1.json
```

## Canonical Roles

| Repo | Role | This repo should expect from it |
|---|---|---|
| `../planning-everything-track` | Control plane | Current priority, deadline, next action, weekly status, and capacity tradeoff. |
| `../meta-scam-ad-research-2026` | Umbrella strategy repo | Broad Meta scam-risk framing, budget logic, cross-platform roadmap, and scope decisions. |
| `.` | Threads execution repo | Threads phase-1 research artifacts and experiment evidence. |

## What This Repo Owns

This repo owns:

- Threads scam-like content problem framing.
- Threads phase-1 scope and prioritization.
- Threads-specific taxonomy and annotation guideline.
- `thread_item_schema_v1`.
- Annotation sheet and experiment templates for Threads samples.
- Phase-1 experiment plan for text, OCR, comments/replies, links, and redirection signals.
- Baseline logs and evaluation notes for Threads work.
- Threads-specific risk register and decision memos.

## What This Repo Does Not Own

This repo does not own:

- Weekly planning, daily notes, capacity, or task status.
- Broad all-Meta strategy.
- Final cross-platform roadmap.
- Production deployment promises.
- Automated Meta collection authority.
- Raw sensitive evidence.
- Legal determinations of fraud.

## Link, Do Not Duplicate

Use links or short summaries across repos. Do not maintain two live copies of the same research artifact.

Examples:

| Need | Correct home |
|---|---|
| "What is the next action this week?" | `../planning-everything-track/data/projects/2026-04-meta-scam-ad-research.md` |
| "Why was Threads split into a child repo?" | `../meta-scam-ad-research-2026/decision-log/0004-create-threads-first-child-repo.md` |
| "What is the Threads phase-1 dataset schema?" | `data-contracts/thread_item_schema_v1.json` |
| "What did the OCR ablation show?" | `experiments/modality-studies/` |
| "Should the broader project add Instagram next?" | `../meta-scam-ad-research-2026/decision-log/` |

## Update Rules

| Event | Update here? | Also update |
|---|---:|---|
| Threads taxonomy changes | Yes | Umbrella only if it changes broad strategy |
| Threads schema changes | Yes | No, unless stakeholder-facing strategy changes |
| Threads experiment result | Yes | Planning short status; umbrella summary only if strategic |
| Budget or scope changes | Yes if phase 1 affected | Planning note and umbrella decision log |
| Weekly priority changes | No | Planning repo only |
| New data access authority | Yes if Threads-specific | Governance docs in both repos if broader |

## Milestone Reporting

At each phase-1 milestone:

1. Write the detailed experiment or evaluation artifact in this repo.
2. Summarize only the decision implication in the umbrella repo if it affects broader Meta strategy.
3. Update the planning project note with next action and current status.
4. Do not copy raw examples, screenshots, or sensitive evidence across repos.

## Current Active MVP

The active phase-1 MVP is a Threads scam-like content triage research package:

- Structured dataset.
- Annotation rules.
- Signal taxonomy.
- Rule-based risk scorer.
- OCR augmentation.
- Comment/reply context comparison.
- Visible link and redirection signal extraction.
- Optional LLM-assisted review explanation on approved redacted samples.
- Human-review-oriented evaluation.

This is not a production detector.
