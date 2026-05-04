# Batch 0003 Dual-Track Metadata Dry Run

## Purpose

Exercise the v2 dual-track research operating system with synthetic metadata-only candidates.

This is not data collection, model training, scam classification automation, crawler expansion, or authorization for new Threads evidence. It tests whether the repo can compare explainable sparse structure against discovery-only embedding structure while preserving governance.

## Variants

| Variant | Role | Hypothesis | Measurement plan |
|---|---|---|---|
| A: sparse primary | Explainable decision-support layer | Sparse behavior features can rank signals by yield per reviewer effort. | Compute SVS by signal and batch; inspect sparse clusters. |
| B: embedding discovery | Discovery-only structure finder | Precomputed vectors can reveal pattern gaps without making decisions. | Compute nearest neighbors and embedding clusters with `discovery_only: true`. |
| C: discrepancy evolution | Human-in-the-loop feature evolution | Sparse/embedding disagreement can propose useful feature candidates without auto-changing the schema. | Detect `missed_pattern` and `over_generalization`; generate review queue entries only. |

## Guardrails

- No raw Threads content.
- No personal identifiers.
- No URLs, handles, screenshots, browser artifacts, credentials, tokens, or controlled-store paths.
- Embeddings are never used for final decisions.
- Sparse features remain the only decision-support layer.
- New features require human `accepted` status before schema promotion.

## Decision Implication

Continue with metadata-only v2 pipeline scaffolding if validation, clustering, discrepancy detection, and feature queue generation all run without raw-evidence leakage.
