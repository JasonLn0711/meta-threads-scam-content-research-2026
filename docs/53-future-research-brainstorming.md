# Future Research Brainstorming

This note records research ideas for later evaluation. It does not authorize immediate collection, modeling, profile review, graph analysis, private-message access, user targeting, or production detection.

## Idea 1: Embedding-Based Scam Spectrum

When the confirmed scam-pointer dataset becomes large enough, test whether an embedding model can help map a "scam spectrum" across Threads scam-like content.

Possible uses:

- cluster similar scam narratives;
- compare new confirmed pointers against known scam families;
- find boundary cases between benign finance content, aggressive marketing, and scam-like funnels;
- support reviewer triage with nearest-neighbor examples;
- discover emerging variants that keyword rules miss.

Important boundaries:

- embeddings are research aids, not legal determinations;
- embedding similarity is not proof that an item is a scam;
- the first version should run on redacted or controlled-store-governed text only;
- do not use embeddings to publicly accuse accounts or automate enforcement;
- require a later decision record before model-assisted review becomes part of the active workflow.

Minimum prerequisites:

- enough confirmed and non-scam comparator examples;
- stable labels and second-review outcomes;
- documented redaction rules for text used in embeddings;
- evaluation against false positives and false negatives;
- stakeholder approval for model-assisted analysis.

## Idea 2: Potential Exposure Or Victim-Risk Dataset

For confirmed scam posts, later research may study users who reshared, quoted, replied to, liked, or otherwise amplified the post as a possible exposure population.

This should not be called a confirmed victim database without independent evidence. A safer research framing is:

- potential exposure dataset;
- possible victim-risk contact graph;
- scam-post interaction audience;
- reshare/reply exposure cohort.

Possible uses:

- understand whether scam posts spread through reshares or reply chains;
- estimate audience exposure around confirmed scam pointers;
- prioritize prevention messaging or outreach design;
- study which interaction patterns correlate with higher exposure risk.

Important boundaries:

- a resharer is not automatically a victim;
- a commenter is not automatically a victim;
- do not store raw user identifiers in git;
- do not infer victim status from interaction alone;
- do not contact users, deanonymize users, or build profile graphs without explicit later approval;
- store any raw interaction graph only in the controlled store with stricter access and retention rules.

Minimum prerequisites:

- explicit CIB/stakeholder approval for interaction-level data;
- data-governance update for user identifiers and possible victim-risk labeling;
- retention and deletion plan;
- redaction and pseudonymization method;
- ethics/legal review of any outreach or victim-risk interpretation;
- decision record distinguishing exposure, suspected victimization, and confirmed victimization.

## Current Status

Both ideas are brainstorming only. They should be revisited after the confirmed scam-pointer dataset has enough examples and after the current rule-library workflow stabilizes.
