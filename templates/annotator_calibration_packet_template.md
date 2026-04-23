# Annotator Calibration Packet Template

Use this template to prepare a local blind calibration packet before real pilot annotation. Keep committed copies free of raw Threads content, screenshots, full URLs, unredacted handles, personal data, stakeholder-sensitive details, and answer keys.

## Calibration Identity

| Field | Value |
|---|---|
| Calibration ID |  |
| Date prepared |  |
| Dataset or sample source | synthetic / redacted real / other approved |
| Guideline version | `docs/06-annotation-guideline-v1.md` |
| Schema version | `thread_item_schema_v1` |
| Calibration owner |  |
| Governance reviewer, if real redacted evidence is used |  |
| Expected completion date |  |

## Participants

| Role | ID | Notes |
|---|---|---|
| Annotator 1 |  |  |
| Annotator 2 or reviewer |  |  |
| Annotation lead or adjudicator |  |  |
| Research engineer |  | file preparation and comparison only |

## Required Reading

| Item | Required? | Complete? |
|---|---|---|
| `docs/06-annotation-guideline-v1.md` | yes |  |
| `docs/04-taxonomy.md` | yes |  |
| `docs/07-dataset-schema.md` | yes |  |
| `docs/23-collection-and-redaction-sop.md` | yes |  |
| `docs/24-annotator-training-and-calibration.md` | yes |  |

## Calibration Item Roster

List item IDs only. Do not include raw source identifiers or raw evidence in a committed packet.

| Item ID | Intended boundary stress | Evidence fields included | Notes |
|---|---|---|---|
|  | scam / uncertain / non_scam / insufficient_evidence |  |  |
|  | scam / uncertain / non_scam / insufficient_evidence |  |  |
|  | scam / uncertain / non_scam / insufficient_evidence |  |  |
|  | scam / uncertain / non_scam / insufficient_evidence |  |  |
|  | scam / uncertain / non_scam / insufficient_evidence |  |  |

## Permitted Evidence

| Evidence field | Included? | Limits |
|---|---|---|
| `post_text` | yes / no |  |
| `reply_texts` | yes / no |  |
| `ocr_text` | yes / no |  |
| `external_links` | yes / no |  |
| `visible_contact_handles` | yes / no |  |
| `visible_platform_redirects` | yes / no |  |
| `metadata_notes` | yes / no | non-sensitive only |

## Forbidden Context

Annotators must not use:

- profile or account research outside the packet
- landing-page visits or redirect-chain inspection
- browser automation, crawling, scraping, or bulk export
- source URLs, screenshots, or handles outside approved packet fields
- legal fraud determinations or accusation language

## Instructions To Annotators

- Annotate independently before discussion.
- Use only the evidence fields in the blind file.
- Preserve uncertainty when evidence is weak or incomplete.
- Explain labels with evidence references, not assumptions.
- Mark low-confidence and boundary cases clearly for adjudication.

## Disagreement Review Plan

| Review item | Owner | Due date | Notes |
|---|---|---|---|
| Compare completed blind files | research engineer |  |  |
| Review primary-label disagreements | annotation lead |  |  |
| Review `uncertain` versus `insufficient_evidence` cases | annotation lead |  |  |
| Identify guideline revision needs | adjudicator |  |  |
| Record non-sensitive themes | governance reviewer / annotation lead |  |  |

## Readiness Decision

Choose one:

- `ready_for_first_10_15_items`
- `ready_with_narrower_rules`
- `revise_guideline_and_repeat`
- `pause_annotation`

Decision:

```text

```

Non-sensitive rationale:

-
