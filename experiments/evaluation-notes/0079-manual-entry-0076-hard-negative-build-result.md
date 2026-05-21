# Manual Entry 0076 Hard-Negative Build Result

## Summary

Run `0045` second review promoted one source-linked candidate into local `manual_entry_0076` as a redacted `non_scam` / `low` hard-negative calibration item.

This is not a scam/high-risk expansion. It records a negative boundary: scam-method vocabulary and private-channel vocabulary can appear in anti-scam warning or victim-prevention context.

## Scope

| Field | Value |
|---|---|
| Source run | `0045` |
| Source candidate role | source-linkage-ready hard negative |
| Manual entry | `data/interim/manual_entry_0076.json` |
| Manual record | `data/interim/manual_record_0076.json` |
| Label | `non_scam` |
| Risk | `low` |
| Evidence sufficiency | `sufficient` |
| Confidence | `high` |
| Raw output | controlled store only |

## Validation

`manual_record_0076.json` strict validation result:

- checked records: 1;
- errors: 0;
- warnings: 0.

The record was built with:

```text
scripts/build_manual_collection_record.py
```

Governance and schema result:

- governance errors: 0;
- governance warnings: 0;
- schema errors: 0;
- schema warnings: 0.

## Interpretation

The selected item is useful because it protects the rule system from over-triggering on anti-scam education, victim-warning, or scam-method description posts.

The item contains redacted evidence pattern fields only. Raw Threads URL, raw handle, raw post text, raw replies, screenshots, browser/session artifacts, and exact controlled-store paths remain outside tracked docs.

## Decision Implication

`manual_entry_0076` exists locally as a strict-valid redacted hard-negative item.

Do not treat this as a new scam/high-risk case. If a later checkpoint synthesis includes item `0076`, it should be counted as `non_scam` / `low` and used for false-positive pressure and hard-negative calibration.
