# Decision 0135: Add Evidence Layer v1

Date: 2026-05-05

Status: accepted as support tooling

## Decision

Add Evidence Layer v1 as a minimal metadata-safe custody layer for controlled raw evidence handling.

This decision adds:

- deterministic SHA-256 hashing;
- create-only local controlled-store simulation;
- append-only JSONL audit logging with hash chaining;
- integrity-checked retrieval;
- metadata-only candidate stub creation;
- schema contracts for evidence store records, candidate stubs, and audit logs.

## First-Principle Rationale

The repo's goal is to maximize review-worthy scam candidates per reviewer hour without losing governance, uncertainty, or hard-negative protection. That requires a clean separation between raw evidence custody and repo-visible research metadata.

Raw evidence cannot live in git. Reviewers still need reproducibility and auditability. Evidence Layer v1 provides the minimum custody mechanism needed to connect candidate records to raw evidence without exposing sensitive content in the repo.

## Scope Boundary

This decision does not authorize:

- external Threads or Meta data collection;
- crawler expansion;
- API access;
- raw evidence in git;
- legal fraud determinations;
- enforcement recommendations;
- production detection;
- model training.

The default `data/evidence_store/` and `data/audit_logs/` paths are local simulations for synthetic smoke tests and are ignored by git. A real run must point the layer to an approved controlled store only after the relevant governance authorization exists.

## Artifacts

- `docs/65-evidence-layer-v1.md`
- `src/evidence/hashing.py`
- `src/evidence/storage.py`
- `src/evidence/audit.py`
- `src/evidence/ingestion.py`
- `schemas/evidence_store_schema.yaml`
- `schemas/candidate_stub_schema.yaml`
- `schemas/audit_log_schema.yaml`
- `ingest.py`
- `verify_chain.py`
- `data/evidence_store/README.md`
- `data/audit_logs/README.md`

## Decision Implication

Future candidate records should prefer evidence references, hashes, and non-sensitive metadata over copied raw text or raw locators. Reviewers can verify custody through hash recomputation and audit-chain validation while final scam judgments remain human-owned.
