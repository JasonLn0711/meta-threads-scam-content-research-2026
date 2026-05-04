# Candidate Intake

This directory stores metadata-only intake worksheets for manual-assisted exploration batches.

Intake worksheets are not evidence records and not final candidate records. They exist to guide safe manual metadata fill before a completed item is converted into `candidate_record_v2`.

Do not include raw Threads content, PII, raw URLs, handles, screenshots, browser artifacts, credentials, or controlled-store locators.

## Active Intake Packets

- Batch 0005 contrast intake: `data/candidate_intake/batch_0005_intake.yaml`
- Batch 0005 reviewer packet: `data/candidate_intake/batch_0005_reviewer_packet.md`
- Batch 0005 conversion report: `data/candidate_intake/batch_0005_conversion_report.yaml`
- Batch 0006 routing intake: `data/candidate_intake/batch_0006_intake.yaml`
- Batch 0006 reviewer packet: `data/candidate_intake/batch_0006_reviewer_packet.md`
- Batch 0006 conversion report: `data/candidate_intake/batch_0006_conversion_report.yaml`
- Batch 0007 context-split intake: `data/candidate_intake/batch_0007_intake.yaml`
- Batch 0007 reviewer packet: `data/candidate_intake/batch_0007_reviewer_packet.md`
- Batch 0007 conversion report: `data/candidate_intake/batch_0007_conversion_report.yaml`

Batch 0005 has completed manual-assisted metadata review and conversion. Its
conversion report shows no blocked entries, and its metadata-only candidate
records are stored under `data/candidates/batch_0005/`.

Batch 0006 has completed manual-assisted metadata review and conversion. Its
conversion report shows no blocked entries, and its metadata-only candidate
records are stored under `data/candidates/batch_0006/`.

Batch 0006 is a routing-validation batch, not a collection expansion. It should
be read together with `metrics/batch_logs/batch_0006_run_log.yaml` and
`experiments/batch_variants/0006-post-review-routing-result.md`.

Batch 0007 is planned and pending manual-assisted metadata review. It tests
whether the broad `result_display_context_review` slow lane can be split into
lower-cost and higher-cost result-display sub-lanes. Do not write candidate
records from it until every completion gate is true and the conversion report
shows no blocked entries.
