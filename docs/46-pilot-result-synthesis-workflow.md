# Pilot Result Synthesis Workflow

## Purpose

This workflow turns an annotated dataset plus local calibration outputs into aggregate-only decision artifacts.

It is the bridge between baseline evaluation and the project decision:

```text
expand_to_100_200 / revise_guideline_first / revise_schema_first / narrow_sources / pause
```

It does not authorize data collection, inspect raw screenshots, crawl links, or make platform-scale claims.

## Command

Synthetic tooling check:

```bash
python scripts/summarize_pilot_results.py data/samples/rule_baseline_eval_sample.json \
  --calibration-run-dir experiments/baselines/outputs/synthetic-calibration-smoke \
  --run-name synthetic-pilot-synthesis-smoke
```

Real pilot use after annotation, audit, and calibration:

```bash
python scripts/summarize_pilot_results.py data/interim/threads_pilot_v1_annotations.csv \
  --calibration-run-dir experiments/baselines/outputs/pilot-rule-calibration-v1 \
  --run-name pilot-v1-decision-draft \
  --governance-rating green \
  --privacy-rating green \
  --reviewer-burden-rating yellow
```

Generated outputs are local-only by default:

```text
experiments/evaluation-notes/outputs/<run-name>/
```

## Outputs

| File | Use |
|---|---|
| `pilot_synthesis_summary.json` | Machine-readable aggregate synthesis. |
| `pilot_result_summary_draft.md` | Draft filled summary for project-owner review. |
| `pilot_decision_memo_draft.md` | Draft decision memo that must be human-finalized. |

## Decision Heuristic

The script can draft a recommendation, but the project owner owns the final decision.

Rules:

- synthetic-only data produces `synthetic_dry_run_no_expansion_decision`
- red governance or privacy rating produces `pause`
- high `insufficient_evidence` rate suggests `revise_schema_first`
- high `uncertain` rate suggests `revise_guideline_first`
- baseline false positives suggest `revise_guideline_first` before expansion
- red reviewer burden suggests `narrow_sources`
- otherwise, the draft can recommend `expand_to_100_200`

## Human Review Required

Before committing any real pilot decision:

- confirm governance and privacy/redaction outcomes
- inspect false positives and false negatives
- check uncertain and insufficient-evidence rates
- confirm reviewer burden
- record final rationale in a decision-log entry
- commit only aggregate, non-sensitive summaries

## Claims Boundary

Allowed:

- "In this approved pilot slice..."
- "The calibration run changed risk decisions in..."
- "The pilot suggests guideline/schema revision..."

Not allowed:

- prevalence claims
- production accuracy claims
- legal fraud claims
- claims about uncollected Threads content
