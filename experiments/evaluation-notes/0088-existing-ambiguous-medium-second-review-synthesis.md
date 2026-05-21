# Existing Ambiguous And Medium-Risk Second Review Synthesis

## Purpose

Synthesize the repo-safe result of decision `0101`, which authorized second review of existing redacted records with `uncertain`, `insufficient_evidence`, or `medium` risk status.

This note contains no raw Threads URLs, handles, screenshots, raw post text, raw reply text, contact IDs, stock names, stock codes, price values, credentials, browser/session artifacts, exact controlled-store paths, or stakeholder case IDs.

## Scope

| Field | Value |
|---|---|
| Review work order | `governance/pilot-launch/threads_pilot_v1_2026-05_existing_ambiguous_medium_second_review_work_order_0050.md` |
| Review queue note | `experiments/evaluation-notes/0085-existing-ambiguous-medium-review-queue.md` |
| Related decision | `decision-log/0101-authorize-existing-ambiguous-medium-second-review.md` |
| Input rule | existing redacted records only |
| New evidence collection | none |
| Browser/crawler expansion | none |
| Legal fraud determination | none |
| Production detector claim | none |

## Final Local Aggregate State

After applying the item-level second-review updates and the already completed local confirmed-pointer items `0080` and `0081`, the local aggregate is:

| Metric | Value |
|---|---:|
| Local records | 78 |
| `scam` | 36 |
| `non_scam` | 24 |
| `uncertain` | 13 |
| `insufficient_evidence` | 5 |
| `high` risk | 36 |
| `medium` risk | 11 |
| `low` risk | 31 |
| Strict validation errors | 0 |
| Strict validation warnings | 0 |

Important caveat: this is a local adjudicated aggregate state. It does not automatically replace the prior approved CIB/165-facing checkpoint package. A separate checkpoint decision is required before presenting it as a new official checkpoint.

## Queue Completion

The 35-record second-review queue has been reviewed through item `threads_pilot_v1_0075`.

Outcome categories:

| Outcome | Items |
|---|---|
| Promoted to `scam` / `high` | `0012`, `0017`, `0020`, `0021`, `0025`, `0049`, `0050`, `0051`, `0052`, `0055`, `0056`, `0058`, `0062`, `0067`, `0068`, `0071`, `0075` |
| Kept `uncertain` with `medium` risk | `0027`, `0047`, `0057`, `0064`, `0065`, `0066`, `0069`, `0070`, `0072` |
| Kept `uncertain` with `low` risk | `0059`, `0060`, `0061`, `0063` |
| Kept or moved to `insufficient_evidence` / `medium` | `0073`, `0074` |
| Kept `insufficient_evidence` / `low` | `0048`, `0053`, `0054` |

Duplicate and near-duplicate traces remain counting-sensitive. Some items may preserve rule lessons while not becoming independent new selected examples for checkpoint claims.

## Rule Lessons

The review strengthened these feature-combination boundaries:

- CIB-confirmed escort or fake-dating starter patterns can be scam/high when the downstream pattern is explicitly confirmed and private-message migration is part of the risk.
- Crypto wallet plus private-channel migration is scam/high when CIB confirmation establishes the funnel.
- Earnings-sheet, testimonial, public stock-tip, named-stock reassurance, wealth-password, day-trading, private group, comment-plus-DM, and external-link cues become strong when they converge as a funnel.
- Coordinated comment-account reinforcement can create false social proof.
- Implausible third-party account, deposit, or exchange-account custody is a high-risk signal when paired with crypto/contact/link context.
- Profit-plus-social-good language is high risk when it presumes future investment gains and pairs with external-link, guarantee, unrealistic-benefit, or investment-lure signals.

The review also strengthened caution boundaries:

- Topic-only finance words, ordinary investment vocabulary, ordinary charity language, ordinary market-scope narrowing, and single-sentence fragments are not enough for scam labeling.
- Market-scope narrowing can be a trust-building starter, but it remains insufficient without conversion context.
- Negated sensitive-intake language can be anti-scam education or trust-softening; fuller context is required.
- Investment-experience and trading-psychology language can build authority, but it remains `uncertain` unless paired with private-message, community, stock-tip, reassurance, guarantee, contact, or other funnel mechanics.
- Anti-scam warning or scam-method vocabulary alone is not scam when the post is victim-prevention oriented and does not redirect readers into the author's own funnel.

## Validation

Commands run:

```text
.venv/bin/python scripts/build_manual_collection_record.py data/interim/manual_entry_0072.json --output data/interim/manual_record_0072.json --ack-controlled-details --allow-governance-warnings
.venv/bin/python scripts/build_manual_collection_record.py data/interim/manual_entry_0073.json --output data/interim/manual_record_0073.json --ack-controlled-details --allow-governance-warnings
.venv/bin/python scripts/build_manual_collection_record.py data/interim/manual_entry_0074.json --output data/interim/manual_record_0074.json --ack-controlled-details --allow-governance-warnings
.venv/bin/python scripts/build_manual_collection_record.py data/interim/manual_entry_0075.json --output data/interim/manual_record_0075.json --ack-controlled-details --allow-governance-warnings
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0081.jsonl --strict
```

Result:

| Check | Result |
|---|---:|
| `manual_record_0072.json` strict validation | pass |
| `manual_record_0073.json` strict validation | pass |
| `manual_record_0074.json` strict validation | pass |
| `manual_record_0075.json` strict validation | pass |
| 78-record local aggregate strict validation | pass |
| Aggregate errors | 0 |
| Aggregate warnings | 0 |

## Decision Implication

The next step is not automatic collection.

The repo now needs a checkpoint decision:

- either keep this as local second-review adjudication and continue only with explicitly approved single confirmed pointers;
- or create a new local checkpoint synthesis around the 78-record aggregate;
- or pause evidence work and revise the reviewer-facing report package to explain the adjudication changes.

Do not start item `0082`, broad crawler/browser expansion, embedding/model training, production detection, or legal fraud determination from this synthesis.
