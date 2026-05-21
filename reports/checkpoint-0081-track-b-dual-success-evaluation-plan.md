# Checkpoint 0081 Track B Dual-Success Evaluation Plan

## 1. Purpose

Define how Track B should evaluate both candidate-discovery effectiveness and reviewer-labor efficiency.

Track B remains a capped live candidate-discovery method test under the existing locked caps, source arms, stop rules, validation boundary, raw-evidence exclusion rule, and aggregate-only reporting boundary. This plan does not change those caps or authorize any new source arm.

The updated north star is:

```text
Use a small amount of human labor to find enough review-worthy Threads investment-scam candidates.
```

Track B must therefore answer two questions:

1. Does the method surface enough review-worthy Threads investment-scam candidates?
2. Can the method operate with acceptable reviewer burden?

The second question is not secondary. It is required for the first question to matter operationally.

## 2. Updated Success Definition

Track B succeeds only if it produces useful evidence on both sides of the method:

- candidate-discovery effectiveness: whether source arms surface review-worthy candidates, high-risk candidates, final scam-label candidates, and useful hard negatives under capped conditions;
- reviewer-labor efficiency: whether those candidates can be reviewed, validated, second-reviewed, and summarized without excessive human reading, schema filling, hesitation, disagreement, or correction burden.

The research output is not just a count of candidates. It is a validated method and workflow for deciding which source arms and review steps are worth scaling.

## 3. Why Discovery Yield Alone Is Insufficient

Discovery yield alone can be misleading.

A method may surface many candidates but still fail if reviewers must manually read every full thread, inspect all reply context, interpret OCR, identify signal families, fill schema fields, resolve hard-negative uncertainty, and write repo-safe summaries one candidate at a time.

A method may also reduce reviewer effort but fail if it does not surface enough review-worthy candidates.

Track B must therefore measure yield and reviewer burden together. Candidate volume without labor efficiency is not operationally scalable; labor efficiency without enough review-worthy yield is not useful.

## 4. Candidate-Discovery Metrics

These metrics measure whether Track B source arms surface useful candidates under the locked caps.

| Metric | Definition | Aggregate reporting note |
|---|---|---|
| surfaced candidates | Count of candidates surfaced by source arm | Report by source arm and total |
| human-reviewed candidates | Count of surfaced candidates receiving human review | Report by source arm and total |
| accepted strict-valid records | Count promoted into strict-valid accepted records | Report aggregate only; local validation target stays outside git |
| review-worthy yield | Review-worthy candidates divided by surfaced or reviewed candidates | Define denominator explicitly |
| high-risk yield | Final high-risk candidates divided by reviewed candidates | Human-reviewed final outcome only |
| final scam-label yield | Final `scam` labels divided by reviewed candidates | Research label only, not legal finding |
| duplicate rate | Duplicate or near-duplicate candidates divided by surfaced candidates | Report by source arm when possible |
| insufficient-evidence rate | `insufficient_evidence` outcomes divided by reviewed candidates | Capture/evidence quality pressure |
| source-arm yield | Review-worthy and high-risk yield per source arm | Compare source arms under existing caps only |
| signal-family yield | Yield by signal family or signal-family combination | Use signal-family matrix categories |

## 5. Reviewer-Labor Metrics

These metrics measure how much human work Track B requires.

| Metric | Definition | Aggregate reporting note |
|---|---|---|
| average review time per candidate | Mean review duration in minutes | Use buckets if exact timestamps are not repo-safe |
| median review time | Median review duration in minutes | Use reviewed-candidate denominator |
| p95 review time | 95th percentile review duration | Shows long-tail burden |
| candidates reviewed per hour | Human-reviewed candidates divided by reviewer hours | Report by source arm when possible |
| second-review rate | Candidates requiring second review divided by reviewed candidates | Include reason categories |
| reviewer disagreement rate | Final disagreements divided by second-reviewed candidates | Human review quality pressure |
| percentage of candidates requiring full-thread reading | Candidates requiring full original-thread reading divided by reviewed candidates | Key Reviewer Assist Layer input |
| percentage of schema fields manually filled | Manually filled fields divided by fields needed for review | Estimates schema-prefill opportunity |
| reviewer hesitation reason | Repo-safe category for why the reviewer slowed down or hesitated | Aggregate categories only |

## 6. Joint Success Metrics

These metrics connect candidate yield to reviewer time.

| Metric group | Metric | Definition | Why it matters |
|---|---|---|---|
| Discovery effectiveness | surfaced candidates | Count of candidates surfaced | Measures source-arm activity under caps |
| Discovery effectiveness | human-reviewed candidates | Count receiving human review | Measures actual reviewer load |
| Discovery effectiveness | accepted strict-valid records | Count promoted into strict-valid accepted records | Measures usable evidence output |
| Discovery effectiveness | review-worthy yield | Review-worthy candidates / reviewed candidates | Measures candidate quality |
| Discovery effectiveness | high-risk yield | Final high-risk candidates / reviewed candidates | Measures priority-case output |
| Discovery effectiveness | final scam-label yield | Final `scam` labels / reviewed candidates | Measures research-label output |
| Discovery effectiveness | duplicate rate | Duplicate candidates / surfaced candidates | Measures wasted review pressure |
| Discovery effectiveness | insufficient-evidence rate | Insufficient-evidence outcomes / reviewed candidates | Measures context/capture quality |
| Discovery effectiveness | source-arm yield | Review-worthy or high-risk yield by source arm | Compares approved source arms |
| Discovery effectiveness | signal-family yield | Review-worthy or high-risk yield by signal family | Guides future signal-family focus |
| Reviewer labor | average review time per candidate | Mean review duration | Measures mean labor burden |
| Reviewer labor | median review time | Median review duration | Measures typical labor burden |
| Reviewer labor | p95 review time | 95th percentile review duration | Measures long-tail scaling risk |
| Reviewer labor | candidates reviewed per hour | Reviewed candidates / reviewer hours | Measures throughput |
| Reviewer labor | second-review rate | Second-review candidates / reviewed candidates | Measures ambiguity and complexity |
| Reviewer labor | reviewer disagreement rate | Disagreements / second-reviewed candidates | Measures review stability |
| Reviewer labor | percentage of candidates requiring full-thread reading | Full-thread reads / reviewed candidates | Measures residual reading burden |
| Reviewer labor | percentage of schema fields manually filled | Manual fields / needed fields | Measures schema-prefill opportunity |
| Reviewer labor | reviewer hesitation reason | Categorized reason for reviewer slowdown | Guides Reviewer Assist design |
| Joint metrics | review-worthy yield per reviewer hour | Review-worthy candidates / reviewer hours | Measures useful candidate output per labor hour |
| Joint metrics | high-risk yield per reviewer hour | High-risk candidates / reviewer hours | Measures priority output per labor hour |
| Joint metrics | false-positive pressure per reviewer hour | False-positive or over-prioritized candidates / reviewer hours | Measures review waste and trust pressure |
| Joint metrics | hard-negative false-positive pressure | Hard negatives incorrectly prioritized or overflagged / hard negatives reviewed | Protects ordinary/warning content |
| Joint metrics | accepted strict-valid records per reviewer hour | Accepted strict-valid records / reviewer hours | Measures usable record output per labor hour |
| Joint metrics | stopped-source-arm time saved | Estimated review time avoided after pausing low-yield/high-burden source arms | Measures stop-rule value |
| Joint metrics | duplicate-filter time saved | Estimated review time avoided through dedupe before full review | Measures dedupe value |

## 7. Failure Modes

Track B should flag failure when:

- a source arm surfaces candidates but review-worthy yield stays low;
- high-risk yield is low despite high surfaced volume;
- duplicate or insufficient-evidence rates consume reviewer time;
- average, median, or p95 review time is too high for operational scale;
- reviewers must read full original threads for most candidates;
- too many schema fields require manual filling;
- second-review or disagreement rates show unstable labels or guidance;
- hard-negative cases create recurring reviewer hesitation;
- hard-negative false-positive pressure rises;
- yield per reviewer hour is poor even when raw yield looks acceptable;
- stop rules fail to prevent wasted labor;
- any raw evidence leakage, scope drift, cap breach, model-training drift, production-detection claim, legal-fraud claim, or enforcement implication appears.

## 8. Required Reviewer Burden Fields

Track B review worksheets should include repo-safe burden fields separate from raw evidence.

Required fields:

| Field | Allowed shape | Purpose |
|---|---|---|
| `review_start_time_bucket` | date or coarse bucket, no exact personal schedule needed | Supports throughput and review-sequence analysis |
| `review_duration_minutes` | number or bucket | Measures human review burden |
| `full_thread_read_required` | yes / no / partial / not_available | Measures residual reading burden |
| `summary_would_have_helped` | yes / no / unclear / not_applicable | Identifies future summary-assist value |
| `schema_fields_auto_fillable` | list or count of field names/categories | Identifies schema-prefill opportunity |
| `reviewer_hesitation_reason` | controlled category plus repo-safe note | Identifies slowdown causes |
| `second_review_reason` | controlled category plus repo-safe note | Explains second-review load |
| `hard_negative_uncertainty_reason` | controlled category plus repo-safe note | Explains hard-negative ambiguity |
| `reviewer_burden_note` | short repo-safe note | Captures labor issues not covered above |

Suggested controlled values for hesitation and second-review categories:

- `reply_context_needed`;
- `ocr_unclear`;
- `signal_family_ambiguous`;
- `hard_negative_possible`;
- `duplicate_or_near_duplicate`;
- `source_context_thin`;
- `schema_field_unclear`;
- `evidence_sufficiency_unclear`;
- `privacy_or_redaction_boundary`;
- `other_repo_safe`.

Do not record raw post text, raw reply text, raw OCR, raw URLs, handles, screenshots, contact IDs, controlled-store paths, credentials, browser/session artifacts, or stakeholder case IDs in these fields.

## 9. Aggregate Reporting Format

Track B aggregate reporting should include the following tables.

### Source-Arm Summary

| Source arm | Surfaced | Human-reviewed | Accepted strict-valid | Review-worthy yield | High-risk yield | Final scam-label yield | Duplicate rate | Insufficient-evidence rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| checkpoint-derived seed replay |  |  |  |  |  |  |  |  |
| reviewer-supplied candidates |  |  |  |  |  |  |  |  |
| approved browser-session risk-probe matrix |  |  |  |  |  |  |  |  |
| reply/comment funnel cue candidates |  |  |  |  |  |  |  |  |
| OCR/image-cue candidates |  |  |  |  |  |  |  |  |
| hard-negative probe arm |  |  |  |  |  |  |  |  |

### Reviewer-Labor Summary

| Source arm | Avg review min | Median review min | P95 review min | Reviewed per hour | Full-thread read % | Manual schema field % | Second-review rate | Disagreement rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| checkpoint-derived seed replay |  |  |  |  |  |  |  |  |
| reviewer-supplied candidates |  |  |  |  |  |  |  |  |
| approved browser-session risk-probe matrix |  |  |  |  |  |  |  |  |
| reply/comment funnel cue candidates |  |  |  |  |  |  |  |  |
| OCR/image-cue candidates |  |  |  |  |  |  |  |  |
| hard-negative probe arm |  |  |  |  |  |  |  |  |

### Joint Outcome Summary

| Source arm | Review-worthy per reviewer hour | High-risk per reviewer hour | Strict-valid per reviewer hour | FP pressure per reviewer hour | Hard-negative FP pressure | Stopped-source-arm time saved | Duplicate-filter time saved |
|---|---:|---:|---:|---:|---:|---:|---:|
| checkpoint-derived seed replay |  |  |  |  |  |  |  |
| reviewer-supplied candidates |  |  |  |  |  |  |  |
| approved browser-session risk-probe matrix |  |  |  |  |  |  |  |
| reply/comment funnel cue candidates |  |  |  |  |  |  |  |
| OCR/image-cue candidates |  |  |  |  |  |  |  |
| hard-negative probe arm |  |  |  |  |  |  |  |

### Reviewer Assist Inputs

| Burden pattern | Count | Source arms affected | Future assist implication |
|---|---:|---|---|
| full-thread reading required |  |  | summary-assisted review |
| OCR uncertainty |  |  | OCR/image cue extraction QA |
| schema fields manually filled |  |  | schema prefill design |
| signal-family hesitation |  |  | signal extraction assistance |
| hard-negative hesitation |  |  | hard-negative checker design |
| duplicate review waste |  |  | dedupe filter design |

## 10. Relationship To Future Reviewer Assist Layer

Track B should produce the evidence needed to design and evaluate the Reviewer Assist Layer in [../docs/62-reviewer-assist-layer-design.md](../docs/62-reviewer-assist-layer-design.md).

Track B should not merely ask:

```text
Did we find candidates?
```

It must also ask:

```text
Which reviewer tasks consumed the most time?
Which fields could be prefilled?
Which signal families were easiest to summarize?
Which hard-negative cases caused reviewer hesitation?
Which source arms produced the best yield per reviewer hour?
```

The answers should guide future reviewer-assist design:

- summary-assisted review for source arms with high full-thread-reading burden;
- schema prefill for fields frequently filled manually and corrected predictably;
- signal-family extraction assistance for repeated visible cues;
- hard-negative checker improvements for hesitation-heavy or false-positive-prone cases;
- priority ranking only where yield per reviewer hour is high and hard-negative pressure is controlled.

This plan does not authorize implementation of a UI, API, model training flow, production detector, legal-fraud workflow, enforcement workflow, public release, new source arm, or raw evidence in git.

