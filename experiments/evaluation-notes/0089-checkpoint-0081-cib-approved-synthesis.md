# Checkpoint 0081 CIB-Approved Synthesis

## Purpose

Synthesize the repo-safe 78-record checkpoint after CIB approval of the current local adjudicated aggregate.

This note contains no raw Threads URLs, handles, screenshots, raw post text, raw reply text, contact IDs, stock names, stock codes, price values, credentials, browser/session artifacts, exact controlled-store paths, or stakeholder case IDs.

## Checkpoint Status

| Field | Value |
|---|---|
| Checkpoint | `threads_pilot_v1_0081` |
| Dataset file | `data/interim/manual_records_checkpoint_0081.jsonl` |
| Records | 78 |
| Latest included item | `threads_pilot_v1_0081` |
| Status | CIB-approved research checkpoint |
| Related decision | `decision-log/0105-approve-cib-78-record-checkpoint-synthesis.md` |
| Second-review synthesis | `experiments/evaluation-notes/0088-existing-ambiguous-medium-second-review-synthesis.md` |
| Run index | `governance/pilot-launch/run_index.md` |

This checkpoint is a research evidence-system checkpoint. It is not a legal fraud determination, production detector, platform prevalence estimate, or authorization for new collection.

## What Changed Since Checkpoint 0055

Checkpoint 0055 was the prior CIB/165-facing package anchor. Checkpoint 0081 adds three categories of local work:

- local hard-negative item `0076`;
- second-review adjudication of existing ambiguous, insufficient, and medium-risk records;
- completed CIB/project-owner confirmed-pointer records `0080` and `0081`.

The most important conceptual shift is that the repo is no longer only collecting examples. It is now adjudicating whether the evidence system can distinguish:

- confirmed scam-like funnels;
- hard negatives and anti-scam warnings;
- high-risk starters that require more context;
- thin fragments that must remain uncertain or insufficient.

## Validation

Commands run:

```text
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0081.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0081.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0081.jsonl --variant all --run-name checkpoint-0081-cib-approved-smoke-v1 --output-dir experiments/baselines/outputs
```

Validation result:

| Check | Result |
|---|---:|
| Strict validation checked records | 78 |
| Strict validation errors | 0 |
| Strict validation warnings | 0 |
| Audit schema errors | 0 |
| Audit schema warnings | 0 |

## Aggregate Result

| Label | Count |
|---|---:|
| `scam` | 36 |
| `non_scam` | 24 |
| `uncertain` | 13 |
| `insufficient_evidence` | 5 |

| Risk | Count |
|---|---:|
| `high` | 36 |
| `medium` | 11 |
| `low` | 31 |

Evidence sufficiency:

| Evidence sufficiency | Count |
|---|---:|
| `sufficient` | 22 |
| `partial` | 45 |
| `insufficient` | 11 |

Source mix:

| Source type | Count |
|---|---:|
| `manual_public` | 60 |
| `stakeholder_provided` | 18 |

Content shape:

| Content shape | Count |
|---|---:|
| `link_or_redirect` | 37 |
| `text_only` | 20 |
| `reply_context` | 16 |
| `text_image_post` | 4 |
| `screenshot_ocr` | 1 |

## Delta Since Checkpoint 0055

| Metric | Checkpoint 0055 | Checkpoint 0081 | Delta |
|---|---:|---:|---:|
| Total records | 55 | 78 | +23 |
| `scam` | 17 | 36 | +19 |
| `non_scam` | 23 | 24 | +1 |
| `uncertain` | 9 | 13 | +4 |
| `insufficient_evidence` | 6 | 5 | -1 |
| `high` risk | 17 | 36 | +19 |
| `medium` risk | 7 | 11 | +4 |
| `low` risk | 31 | 31 | 0 |

Interpretation:

- Most new `scam` / `high` movement comes from CIB-confirmed or reviewer-adjudicated feature combinations, not from topic-only keyword matching.
- The remaining `uncertain` and `insufficient_evidence` records are useful because they preserve weak or incomplete evidence instead of forcing labels.
- Duplicate and near-duplicate traces remain important caveats for item-count interpretation.

## Baseline Smoke Result

Rule baseline run:

```text
checkpoint-0081-cib-approved-smoke-v1
```

| Metric | Value |
|---|---:|
| Binary metric items | 60 |
| Accuracy | 0.850 |
| Precision | 0.829 |
| Recall | 0.944 |
| F1 | 0.883 |
| False positives | 7 |
| False negatives | 2 |

These are smoke-test baseline metrics on the current binary-evaluable slice. They are not production performance estimates.

The two false negatives show that the current rule baseline still misses some scam/high cases after human adjudication. This supports keeping human review and rule revision in the loop.

Baseline triage support uses the evaluator's preferred gold risk field: `final_risk_level` when present, otherwise `risk_level`. The final aggregate table above reports the schema-level `risk_level` distribution. One duplicate/insufficient-evidence trace has `risk_level = medium` and `final_risk_level = low`, so the baseline triage support is `high 36`, `medium 10`, `low 32`, while the checkpoint aggregate distribution remains `high 36`, `medium 11`, `low 31`.

## Key Rule Lessons

Feature combinations that became stronger:

- profit proof plus external-link or private-channel funnel;
- comment-account reinforcement and social-proof orchestration;
- private-channel migration after investment, crypto, day-trading, stock-tip, or loss-rescue framing;
- public stock-tip or named-stock reassurance when tied to conversion context;
- profit-plus-social-good framing when paired with unrealistic-benefit or guarantee signals;
- reply-level contact hijack or anti-scam camouflage that still publishes a "safe" contact or group path.

Boundaries that must remain protected:

- anti-scam warning posts are hard negatives when they do not redirect readers into the author's own funnel;
- ordinary finance vocabulary, market-scope narrowing, trading psychology, or single-sentence fragments are not enough for scam labeling;
- external-link presence alone is not enough;
- near-duplicates should not be counted as independent new evidence without distinct context;
- strict-valid means schema and validation checks passed, not that every item is equally complete.

## Audit Notes

The audit still flags source and collection-method skew:

- `manual_public`: 60 of 78 records;
- `manual_capture`: 60 of 78 records.

This is expected for a governed early research checkpoint. It means the checkpoint is suitable for rule learning and evidence-system review, but not for prevalence claims or model training.

Additional evidence gaps remain:

- many records have empty reply context;
- OCR remains under-tested;
- contact and link fields are redacted or category-level in tracked artifacts;
- controlled-store evidence is not reproduced in git.

## Decision Implication

Checkpoint 0081 can now be used as the current CIB-approved research checkpoint.

Recommended next action:

```text
prepare a reviewer-facing checkpoint 0081 package or report addendum
```

Do not start item `0082`, broad crawler/browser expansion, embedding/model training, production detection, or legal fraud determination from this synthesis.
