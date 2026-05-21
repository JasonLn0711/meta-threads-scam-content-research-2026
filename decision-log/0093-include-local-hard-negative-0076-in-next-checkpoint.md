# Decision 0093: Include Local Hard Negative 0076 In Next Checkpoint

## Status

Accepted.

## Decision

Accept local item `0076` for inclusion in the next checkpoint synthesis as a strict-valid `non_scam` / `low` hard-negative calibration item.

This decision does not reopen broad collection and does not create a scam/high-risk expansion.

## Context

Run `0045` created a source-linked hard-negative candidate. Decision `0092` promoted it into local `manual_entry_0076` and `manual_record_0076`.

A local 76-record aggregate file was built by appending `manual_record_0076` to the existing 75-record local aggregate.

## Validation Result

Local aggregate:

- dataset: `manual_records_checkpoint_0076.jsonl`;
- records: 76;
- strict validation errors: 0;
- strict validation warnings: 0;
- audit schema errors: 0;
- audit schema warnings: 0.

Aggregate labels:

- `scam`: 17;
- `non_scam`: 24;
- `uncertain`: 29;
- `insufficient_evidence`: 6.

Aggregate risk:

- `high`: 17;
- `medium`: 13;
- `low`: 46.

Rule-baseline smoke result:

- precision: 0.708;
- recall: 1.000;
- false positives: 7;
- false negatives: 0.

## Rationale

Item `0076` improves false-positive pressure and anti-scam warning boundary coverage. It does not change the high-risk scam evidence count.

The item is useful because scam-method vocabulary and private-channel vocabulary appear in a victim-prevention context. The rule system should not treat that pattern as scam-like by default.

## Consequences

- Future checkpoint synthesis may use 76 records with item `0076` included.
- Item `0076` must be counted as `non_scam` / `low`.
- The local aggregate remains in ignored interim storage unless a separate data-publication decision changes that boundary.
- The next preferred research step remains targeted confirmed-pointer intake or report synthesis, not broad browser expansion.
