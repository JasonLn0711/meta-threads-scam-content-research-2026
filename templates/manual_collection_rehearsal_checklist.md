# Controlled Collection Rehearsal Checklist

Use this checklist for the 1-2 item controlled rehearsal before real pilot volume begins. It applies to manual, stakeholder-provided, API-authorized, or automation-assisted collection under the controlled launch record. Keep completed versions local-only if they contain item-level evidence, source details, raw storage details, URLs, handles, automation run details, or sensitive operational notes.

## Rehearsal Identity

| Field | Value |
|---|---|
| Rehearsal ID |  |
| Dataset or batch ID | `threads_pilot_v1_2026-05` |
| Rehearsal date |  |
| Collection path | manual / stakeholder_provided / api_authorized / automation_assisted |
| Collector ID |  |
| Automation operator ID |  |
| Reviewer ID |  |
| Controlled launch details confirmed? | yes / no |
| Separate API/automation run record confirmed if needed? | yes / no / n/a |
| Input file reviewed |  |
| Output record reviewed |  |
| Collection log reviewed |  |

## Command Record

```bash
python scripts/build_manual_collection_record.py data/interim/manual_entry_0001.json \
  --ack-controlled-details \
  --output data/interim/manual_record_0001.json \
  --collection-log data/interim/threads_pilot_v1_collection_log.csv

python scripts/validate_thread_dataset.py data/interim/manual_record_0001.json --strict
```

If the rehearsal item came from API or automation-assisted capture, also confirm the separate controlled run record outside git before review.

## Pass/Fail Checks

| Check | Pass? | Notes |
|---|---|---|
| Controlled launch record exists outside git | yes / no |  |
| Input JSON uses only approved fields | yes / no |  |
| Item ID contains no source, handle, URL, or person name | yes / no |  |
| Source type and collection method are approved | yes / no |  |
| Collection path matches the controlled launch record | yes / no |  |
| Authorization status is correct | yes / no |  |
| Raw evidence storage is outside git | yes / no |  |
| Raw storage reference follows controlled policy | yes / no |  |
| API/automation run details stayed outside git | yes / no / n/a |  |
| Source URL handling follows controlled policy | yes / no |  |
| Visible links are normalized or redacted as approved | yes / no |  |
| Contact handles are omitted, categorical, or redacted as approved | yes / no |  |
| OCR text is risk-relevant and privacy-reviewed | yes / no / n/a |  |
| Screenshot status is filled and allowed | yes / no / n/a |  |
| Reply/comment context is selected and approved | yes / no / n/a |  |
| No profile/account/landing-page/redirect context was added beyond the approved run record | yes / no |  |
| `privacy_redaction_notes` explains redaction | yes / no |  |
| Collection burden is logged | yes / no |  |
| Exclusion reason is logged if needed | yes / no / n/a |  |
| Manual assistant governance errors are zero | yes / no |  |
| Manual assistant warnings were reviewed | yes / no / n/a |  |
| Strict schema validation passes | yes / no |  |
| No raw evidence or sensitive controlled details entered git | yes / no |  |

## Common Mistakes Found

| Mistake | Found? | Fix before continuing |
|---|---|---|
| Full source URL copied into local record | yes / no |  |
| Raw contact handle, phone, email, payment detail, or referral code retained | yes / no |  |
| OCR includes unrelated personal details | yes / no |  |
| Screenshot retained without approved status or redaction | yes / no |  |
| Collector used profile/account/landing-page/redirect context | yes / no |  |
| API or automation output retained raw in repo-visible locations | yes / no |  |
| Collection log missing burden or exclusion notes | yes / no |  |
| Schema field needed but unclear | yes / no |  |

## Boundary Review

Use this section to catch the disagreement patterns already seen in synthetic calibration before they spread into real pilot rows.

| Boundary question | Reviewed? | Notes |
|---|---|---|
| Readable finance discussion without a funnel stayed `non_scam` rather than being escalated from topic alone | yes / no / n/a |  |
| Decisive OCR evidence was allowed to remain `sufficient` when the missing context was only uncaptured destination/profile detail | yes / no / n/a |  |
| Generic verification wording was not treated as a credential-request tag without an explicit data ask | yes / no / n/a |  |
| Confidence was judged from likely agreement on the main label and reason, not exact subtype/tag overlap | yes / no / n/a |  |

## Schema Or Guideline Revision Signals

| Signal | Observed? | Owner |
|---|---|---|
| Approved evidence cannot fit current schema | yes / no |  |
| Required field is too ambiguous for collector | yes / no |  |
| Redaction rule conflicts with annotation need | yes / no |  |
| Collector needs unapproved context to make item reviewable | yes / no |  |
| Current guideline does not explain expected note format | yes / no |  |
| Current guideline does not explain the observed finance, OCR, or pseudo-official boundary pattern | yes / no |  |

## Rehearsal Decision

Choose one:

- `pass_ready_for_calibration_or_first_10_15`
- `pass_with_limits`
- `pause_for_redaction_fix`
- `pause_for_schema_or_guideline_fix`
- `pause_for_authorization_review`
- `stop_source_for_pilot`

Decision:

```text

```

Required follow-up before real item 1:

| Follow-up | Owner | Required before item 1? |
|---|---|---|
|  |  | yes / no |
