# Decision 0034: Select API Or Targeted Exemplar Method Before Item 0028

## Date

2026-04-25

## Decision

Do not open item `0028` through another browser/session search-result collection run yet.

Before item `0028`, choose one of two higher-yield acquisition paths:

1. complete the approved API/session-aware path by supplying and validating `META_API_PROBE_URL`; or
2. obtain targeted redacted stakeholder/CIB exemplars or exemplar-like pointers for high-risk scam-like cases.

If neither path is ready, pause collection and prepare synthesis/reporting from the 27-record checkpoint.

## Context

Checkpoint `0027` contains 27 strict-valid local records, 26 non-excluded records, and 1 excluded method-review trace. The final-label view still has:

- 0 final `scam`;
- 21 final `non_scam`;
- 5 final `uncertain`;
- 0 final high-risk records.

Run 0016 improved method discipline by using per-family candidate caps, narrow reply/comment review, anti-scam camouflage handling, and CIB false-negative preference at triage. It still produced mainly false-positive pressure and uncertainty-boundary records.

The current approved browser/session search-result path is useful for calibration, but it has not found confirmed high-risk scam-like examples.

## Options Considered

| Option | Decision |
|---|---|
| Start item `0028` with the same browser/session risk-probe pattern | Rejected; likely to add more low/medium boundaries without solving high-risk acquisition. |
| Complete API/session-aware readiness before item `0028` | Accepted as preferred path if `META_API_PROBE_URL` can be supplied and dry-run passes. |
| Request targeted redacted stakeholder/CIB exemplars or pointers | Accepted as parallel or fallback path because known report-worthy examples can calibrate high-risk evidence standards. |
| Pause collection for synthesis/reporting if neither path is ready | Accepted as the safe fallback. |

## Rationale

CIB's stated preference is to avoid false negatives even when false positives rise. That preference argues for better access to known or stronger high-risk evidence, not simply more broad search-result candidates.

API/session-aware retrieval may expose richer item/reply/link context and reduce search-result truncation. Targeted redacted exemplars may provide the clearest high-risk calibration without broadening collection.

Both paths preserve the repo's boundaries: no raw sensitive material in git, no production detector claim, no legal fraud determination, and second review before counting.

## Consequences

- Item `0028` remains blocked until one of the selected paths is ready and recorded.
- The API path remains blocked until `META_API_PROBE_URL` is supplied in the controlled env and a dry-run/readiness check passes.
- Targeted exemplars must be redacted before entering git; raw/source case IDs remain in controlled storage or stakeholder systems.
- Another browser/session search run requires a new decision explaining why it is expected to reach higher-risk evidence.
- The project should begin preparing a checkpoint synthesis if neither acquisition path is immediately available.

## Follow-Up

Run one of these next:

```bash
python3 scripts/prepare_controlled_access_path.py --api-dry-run --require-ready
```

after adding an approved `META_API_PROBE_URL` to the controlled env, or create a targeted exemplar intake record that defines:

- source owner;
- redaction owner;
- allowed fields;
- raw storage boundary;
- item cap;
- second-review owner;
- strict-validation step.
