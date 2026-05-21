# Batch 0004 Manual-Assisted Intake Protocol

## Purpose

Turn the 10 Batch 0004 candidate stubs into a safe manual-assisted metadata fill workflow.

This protocol does not create candidate records, invent labels, collect external content, or authorize new access. It only defines how a reviewer should fill structured metadata if authorized evidence is available through the existing governed workflow.

## Intake Artifact

- Intake worksheet: `data/candidate_intake/batch_0004_intake.yaml`
- Batch plan: `exploration/batches/batch_0004.yaml`
- Stub batch: `data/candidate_stubs/batch_0004.yaml`

## Fill Rules

For each intake entry, fill only:

- sparse feature observations: `0` or `1`;
- structured behavior notes at category level only;
- review decision metadata after human review;
- review time in seconds;
- whether second review is required;
- completion gates confirming raw evidence and PII were excluded from git.

Do not fill:

- raw post text;
- raw reply text;
- OCR text;
- URLs;
- handles;
- screenshots;
- browser/session artifacts;
- credentials or secret material;
- controlled-store locators;
- stakeholder case IDs;
- any personal identifiers.

## Conversion Rule

Only after an intake entry has `completion_gate` values satisfied and human review metadata completed should it be converted into `candidate_record_v2`.

Do not create `data/candidates/*.yaml` records with fake labels, fake confidence, fake review time, or assumed second-review status.

## After-Fill Commands

```bash
./.venv/bin/python scripts/validate_candidate_v2.py data/candidates
./.venv/bin/python scripts/run_v2_ros.py
./.venv/bin/python scripts/generate_feature_candidates_v1.py
./.venv/bin/python scripts/generate_exploration_tasks.py
```

## Learning Question

Does a 10-stub manual-assisted metadata pass confirm that `成果展示` and `保證收益` remain high-SVS signals, or does review burden / uncertainty collapse their value?
