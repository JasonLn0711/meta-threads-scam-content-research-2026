# Batch Logs

This directory stores one durable run log for each v2 research batch.

Batch logs are required whether the batch succeeds, fails, blocks, produces no
candidate records, or changes no metrics. They are the system's memory of what
was actually tried.

Rules:

- record actual results only
- keep expected outcomes separate from observed outcomes
- include failure modes and blocked states
- include reviewer-burden metrics whenever available
- do not store raw Threads content, PII, URLs, handles, screenshots, browser
  artifacts, credentials, or controlled-store locators
- do not claim legal fraud, enforcement readiness, production detection, or
  platform-wide validity

Use `template.yaml` before starting a new batch and keep the final run log after
the batch closes.

Current v2 learning-loop logs:

- `batch_0004_run_log.yaml`
- `batch_0005_run_log.yaml`
- `batch_0006_run_log.yaml`
- `batch_0007_run_log.yaml`
