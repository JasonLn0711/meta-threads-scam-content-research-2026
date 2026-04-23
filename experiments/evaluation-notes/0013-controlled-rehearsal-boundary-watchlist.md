# Controlled Rehearsal Boundary Watchlist

## Objective

Turn the latest synthetic calibration lessons into a short watchlist for the first 1-2 controlled real rehearsal items.

This note is repo-safe. It does not contain raw evidence, URLs, handles, screenshots, credentials, or run-record details.

## Why This Exists

The pilot already has:

- a controlled launch record
- local workspace and preflight checks
- a synthetic rehearsal path
- revised annotation guidance after synthetic calibration

The next failure risk is simpler and more human: the first real rehearsal item may still be collected or annotated with the old mental model unless the known disagreement patterns are named up front.

## Watchlist

### 1. Finance topic is not enough for `uncertain`

Ask:

- Does the item actually show a funnel, guaranteed benefit, redirect, fee, fake authority, or other concrete suspicious signal?
- Or is it just readable finance discussion, recordkeeping, or opinion?

Default:

- readable finance discussion without a conversion step stays `non_scam`

Escalate only when:

- the item visibly asks the reader to join, DM, pay, trust special access, or follow a secret method

## 2. Missing destination capture is not an automatic evidence downgrade

Ask:

- Is the decisive lure already visible in captured text, OCR, replies, or visible handles/links?
- Is the missing context only uncaptured destination/profile detail?

Default:

- keep `evidence_sufficiency` at `sufficient` when the captured evidence already supports the core label

Record instead:

- missing destination, source identity, or profile context in `missing_evidence`

## 3. Generic verification wording is not automatically a credential request

Ask:

- Does the item explicitly request login, identity, bank, account, or other personal details?
- Or does it only use official-looking verification language?

Default:

- keep `pseudo_official_language` when that is what is visible

Add `credential_or_personal_data_request` only when:

- the item explicitly asks for credentials or personal/account details

## Rehearsal Decision Use

During the first 1-2 controlled real rehearsal items:

- apply `templates/manual_collection_rehearsal_checklist.md`
- record whether any of the above boundary questions caused confusion
- treat repeated confusion as a blocker before the first 10-15 item checkpoint

## If Any Watchlist Item Fails

Do not improvise from memory in local files.

Instead:

1. pause the rehearsal item at review
2. note the issue in the local checklist
3. decide whether the fix belongs in:
   - collection/redaction handling
   - annotation guidance
   - schema/template wording
   - controlled launch authorization scope
