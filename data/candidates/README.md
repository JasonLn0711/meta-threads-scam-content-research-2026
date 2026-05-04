# Candidate Records v2

This directory stores metadata-only candidate records for the v2 dual-track research operating system.

Allowed content:

- Candidate alias IDs
- Batch IDs
- Sparse binary features
- Optional precomputed embedding vectors
- Human review decision metadata
- Review time and second-review flags

Forbidden content:

- Raw Threads post, reply, OCR, or profile text
- URLs, handles, personal identifiers, screenshots, browser exports, session artifacts, credentials, tokens, or controlled-store paths

Use `data-contracts/candidate_record_v2.schema.yaml` and `scripts/validate_candidate_v2.py` before running v2 reports.
