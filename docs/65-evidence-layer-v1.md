# Evidence Layer v1

Status: minimal implementation layer

Date opened: 2026-05-05

## Purpose

Evidence Layer v1 gives this repo a small, auditable, metadata-safe bridge between controlled raw evidence and repo-visible candidate review artifacts.

It supports:

- deterministic evidence hashing;
- local controlled-store simulation;
- append-only audit logging with hash chaining;
- integrity-checked retrieval;
- metadata-only candidate stubs for reviewer workflow.

It does not authorize new Threads collection, crawler expansion, API access, model training, production detection, legal fraud determination, enforcement action, or raw evidence in git.

## Why Raw Data Is Not Stored In Git

Raw Threads evidence can contain personal data, handles, screenshots, URLs, session artifacts, or sensitive investigative context. Git is a poor custody store for that material because it replicates content, preserves deleted history, and makes access control hard to prove.

This repo remains metadata-only. The default `data/evidence_store/` path is only a simulated local controlled store for synthetic smoke tests and is ignored by git. Real raw evidence must stay in an approved outside-git controlled store. Use `EVIDENCE_STORE_DIR` to point the implementation at that location when a governed run authorizes it.

Repo-visible files should carry only:

- evidence ids;
- SHA-256 hashes;
- source category or non-sensitive source labels;
- signal-family metadata;
- candidate scores for review routing;
- aggregate or redacted audit summaries.

## Chain Of Custody

The ingestion path is:

```text
raw input
-> deterministic byte normalization
-> SHA-256 hash
-> UUID evidence_id
-> create-only controlled-store JSON record
-> append audit log entry with previous_hash
-> return evidence_id and hash
```

Each audit entry includes:

- `entity_id`;
- `action`;
- `actor`;
- `previous_hash`;
- non-sensitive `details`;
- `entry_hash`.

`entry_hash` is SHA-256 over canonical JSON for the audit entry excluding `entry_hash` itself. The next entry's `previous_hash` must match the prior entry's `entry_hash`. This detects entry edits, insertions, and reordering. A future version should anchor the latest hash outside the local machine if full tail-truncation detection is required.

Audit appends use an exclusive file lock around "read last hash, write next entry" so concurrent local writers cannot silently fork the chain.

## Reproducibility

Evidence hashes are computed over normalized bytes:

- text becomes UTF-8 bytes;
- binary input is hashed as bytes and stored as base64;
- JSON-like input is serialized as sorted-key canonical JSON before hashing.

Retrieval recomputes SHA-256 from stored content bytes before returning content. If the recomputed hash differs from the stored hash, retrieval fails.

Candidate stubs are reproducible because they store only:

- `evidence_ref.evidence_id`;
- `evidence_ref.sha256`;
- metadata-only features;
- a research triage score;
- `human_decision_required: true`.

## Reviewer Audit Path

Reviewers can audit a candidate without seeing raw content in git:

1. Open the candidate stub in `data/candidate_intake/`.
2. Confirm it contains `raw_content_included: false`.
3. Confirm `evidence_ref.evidence_id` and `evidence_ref.sha256`.
4. Run `python verify_chain.py` to verify the local audit chain.
5. In the controlled store only, retrieve evidence by id and recompute the hash.
6. Compare the recomputed hash to the candidate stub and audit-log hash.

The reviewer decision remains human-owned. Evidence Layer v1 supports custody and review routing; it does not decide whether an item is a scam.

## CLI Usage

Synthetic text ingest:

```bash
python ingest.py --input "synthetic smoke-test text; no real Threads content" --source threads
```

Verify the audit chain:

```bash
python verify_chain.py
```

Create a metadata-only candidate stub from Python:

```python
from src.evidence.ingestion import create_candidate_stub

create_candidate_stub(
    evidence_id="00000000-0000-0000-0000-000000000000",
    features={"signal_family": "synthetic_demo", "private_channel_migration": False},
    score=0.1,
)
```

## File Map

```text
src/evidence/hashing.py      SHA-256 hashing
src/evidence/storage.py      controlled-store read/write and integrity checks
src/evidence/audit.py        append-only JSONL hash chain
src/evidence/ingestion.py    ingest pipeline and candidate stub builder
schemas/                    v1 schema contracts
data/evidence_store/         ignored local controlled-store simulation
data/audit_logs/             ignored local audit-log simulation
```

## Boundary Rules

- Do not commit generated files from `data/evidence_store/`.
- Do not commit generated JSONL files from `data/audit_logs/`.
- Do not put raw text, URLs, handles, screenshots, or controlled-store paths into candidate stubs.
- Do not treat a candidate score as a final label.
- Do not use this layer for real collection unless the relevant governance record authorizes source, method, fields, storage, access, retention, redaction, and audit handling.
