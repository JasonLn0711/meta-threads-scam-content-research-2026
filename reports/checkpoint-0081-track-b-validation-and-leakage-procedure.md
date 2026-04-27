# Checkpoint 0081 Track B Validation And Leakage Procedure

## Purpose

Define the Track B strict-validation output target and raw-evidence exclusion procedure.

This procedure resolves the local validation-output-target blocker. It does not authorize Track B execution and does not replace legal/privacy or CIB/internal owner signoff.

## Status

| Field | Value |
|---|---|
| Track | `track_b_capped_live_method_test` |
| Procedure status | `ready_for_track_b_day_1_after_day_0_start` |
| Track B execution authorized by this procedure | no; execution is authorized only by decision `0122` and bounded by decision `0123` Day 0 start |
| Legal/privacy signoff resolved by this procedure | no; formal signoff is recorded separately as `no_veto` |
| CIB/internal owner signoff resolved by this procedure | no; formal signoff is recorded separately as `accepted_boundary` |
| Local-only Track B workspace | `data/interim/track_b/` prepared and ignored |
| Item `0082` authorized | no |
| Raw evidence in git authorized | no |

## Local-Only Validation Targets

Track B strict-validation inputs and logs must remain local-only under ignored `data/interim/`.

| Artifact | Target |
|---|---|
| Track B strict-validation dataset | `data/interim/track_b/manual_records_track_b.jsonl` |
| Track B strict-validation log | `data/interim/track_b/validation_track_b_strict.txt` |
| Track B raw-evidence exclusion scan log | `data/interim/track_b/raw_evidence_exclusion_scan.txt` |
| Repo-safe aggregate report after Track B completes | `reports/checkpoint-0081-track-b-capped-live-method-test-aggregate-report.md` |

The `data/interim/track_b/` files are ignored working files. Do not force-add them to git.

## Strict Validation Command

Run only after Track B is authorized and a repo-safe local validation dataset exists:

```bash
mkdir -p data/interim/track_b
python3 scripts/validate_thread_dataset.py \
  data/interim/track_b/manual_records_track_b.jsonl \
  --strict \
  > data/interim/track_b/validation_track_b_strict.txt
```

Required pass condition:

```text
errors: 0
warnings: 0
```

If strict validation fails, Track B reporting pauses until the validation owner records the error class and the correction path in repo-safe form.

## Raw-Evidence Exclusion Procedure

Run this before any Track B repo-facing output is committed.

```bash
git diff --cached --name-only
git diff --cached --check

git ls-files data/raw data/interim data/processed evidence/raw evidence/private \
  | rg -v '(^data/(raw|interim|processed)/README\\.md$)' || true

rg -n -I \
  'https?://|threads\\.com|threads\\.net|@[A-Za-z0-9_.]{3,}|raw Threads URL|raw post text|raw reply text|raw OCR text|contact ID|cookie|token|storage_state|browser/session artifact|exact controlled-store path|stakeholder case ID|private recipient detail' \
  reports docs decision-log experiments governance data-contracts scripts \
  > data/interim/track_b/raw_evidence_exclusion_scan.txt
```

Expected interpretation:

- governance-boundary wording such as "do not include raw URLs" is allowed;
- JSON schema IDs such as `https://example.invalid/...` are allowed;
- real Threads URLs, handles, screenshots, raw post text, raw reply text, raw OCR text, contact IDs, credentials, cookies, tokens, browser/session artifacts, exact controlled-store paths, stakeholder case IDs, or private recipient details are not allowed in git-facing outputs.

Any real raw-evidence hit triggers immediate stop and cleanup review before commit.

## Commit Gate

Before committing a Track B repo-facing report, confirm:

```text
strict validation log exists locally
strict validation errors = 0
strict validation warnings = 0
raw-evidence exclusion scan reviewed
no data/interim Track B files staged
aggregate report contains no raw evidence
legal/privacy and CIB/internal signoff were already recorded
```

## Explicit Non-Authorizations

This procedure does not authorize:

- Track B activity outside decision `0122`, decision `0123`, locked caps, stop rules, validation, and aggregate-only reporting;
- item `0082`;
- open-ended collection;
- broad crawler/browser expansion;
- private-message access;
- account/profile graph capture;
- landing-page or redirect-chain capture;
- model or embedding training;
- production detector claims;
- legal fraud determinations;
- automated enforcement;
- public release;
- raw evidence in git.
