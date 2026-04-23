# Annotator Calibration Packet Template

Use this packet for the 5-item calibration before real annotation volume begins. Keep completed packets local-only if they contain item-level real evidence, source details, URLs, handles, OCR text, screenshots, or sensitive notes.

## Calibration Identity

| Field | Value |
|---|---|
| Calibration ID |  |
| Dataset or batch ID | `threads_pilot_v1_2026-05` |
| Calibration date |  |
| Guideline version | `docs/06-annotation-guideline-v1.md` |
| Schema version | `thread_item_schema_v1` |
| Labeling schema version | `labeling_schema_v1` |
| Annotation lead |  |
| Adjudicator |  |
| Governance reviewer, if real redacted evidence is used |  |

## Participants

| Role | ID | Completed required reading? | Notes |
|---|---|---|---|
| Annotator 1 | `ann_01` | yes / no |  |
| Annotator 2 | `ann_02` | yes / no |  |
| Reviewer or adjudicator |  | yes / no |  |

## Required Reading

| Material | Confirmed? | Notes |
|---|---|---|
| `docs/06-annotation-guideline-v1.md` | yes / no |  |
| `docs/04-taxonomy.md` | yes / no |  |
| `docs/24-annotator-training-and-calibration.md` | yes / no |  |
| `docs/30-annotator-onboarding-quickstart.md` | yes / no |  |
| `data-contracts/labeling_schema_v1.json` | yes / no |  |

## Five Calibration Items

Do not include raw source identifiers in this table. Use item IDs or local packet references only.

| Item ID | Intended stress case | Evidence forms included | Notes |
|---|---|---|---|
|  | obvious scam/high-risk scam-like | text / image / OCR / reply / link / handle |  |
|  | likely benign comparator | text / image / OCR / reply / link / handle |  |
|  | uncertain or ambiguous | text / image / OCR / reply / link / handle |  |
|  | insufficient-evidence or low-context | text / image / OCR / reply / link / handle |  |
|  | OCR/reply/link/handle boundary case | text / image / OCR / reply / link / handle |  |

## Calibration Rules For Annotators

- Use only the evidence fields in the packet.
- Do not inspect live Threads pages, profiles, accounts, landing pages, redirect chains, or outside sources.
- Preserve uncertainty; do not force binary labels.
- Use `uncertain` for suspicious but incomplete or mixed evidence.
- Use `insufficient_evidence` when the capture cannot support a judgment.
- Avoid legal conclusions.
- Do not add raw personal data to notes.

## Files And Commands

Annotator files:

```text
data/interim/calibration_ann_01.csv
data/interim/calibration_ann_02.csv
```

Comparison command:

```bash
python scripts/compare_annotation_passes.py \
  data/interim/calibration_ann_01.csv \
  data/interim/calibration_ann_02.csv \
  --name-a ann_01 \
  --name-b ann_02 \
  --output data/processed/calibration_agreement.md \
  --disagreements-csv data/processed/calibration_disagreements.csv
```

## Qualitative Agreement Review

| Review question | Result | Notes |
|---|---|---|
| Primary-label disagreements are isolated and explainable | yes / no |  |
| `uncertain` and `insufficient_evidence` are used differently | yes / no |  |
| Risk-level differences do not break second-review routing | yes / no |  |
| Signal-tag differences do not hide decisive evidence | yes / no |  |
| OCR/reply/link evidence is handled consistently enough | yes / no |  |
| Notes are evidence-based and non-legal | yes / no |  |
| No annotator required unapproved outside context | yes / no |  |

## Disagreement Themes

| Theme | Item IDs | Guideline change needed? | Owner |
|---|---|---|---|
| scam vs uncertain |  | yes / no |  |
| uncertain vs insufficient_evidence |  | yes / no |  |
| risk level |  | yes / no |  |
| scam type |  | yes / no |  |
| signal tags |  | yes / no |  |
| OCR/reply/link interpretation |  | yes / no |  |
| note quality or overclaiming |  | yes / no |  |

## Calibration Decision

Choose one:

- `ready_for_first_10_15_annotation`
- `ready_with_limits`
- `revise_guideline_first`
- `revise_schema_first`
- `rerun_calibration`
- `pause`

Decision:

```text

```

Required follow-up:

| Follow-up | Owner | Required before first 10-15 item annotation? |
|---|---|---|
|  |  | yes / no |
