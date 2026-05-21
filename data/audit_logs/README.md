# Audit Logs

This directory stores local Evidence Layer v1 JSONL audit logs for smoke tests.

Generated audit logs are ignored by git because they can contain sensitive custody metadata. Keep repo-visible reports aggregate or redacted.

For real evidence operations, use an approved outside-git audit-log location and point `EVIDENCE_AUDIT_LOG_DIR` to that location.
