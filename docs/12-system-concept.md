# System Concept

## Concept

The phase-1 prototype should be a research workflow, not a production system. It should capture evidence, extract low-cost signals, assign review-oriented risk tiers, and log experiments.

## High-Level Flow

```mermaid
flowchart TD
    A[Approved or manual sample] --> B[Evidence capture]
    B --> C[Text normalization]
    B --> D[OCR extraction]
    B --> E[Visible link and redirection extraction]
    C --> F[Signal extraction]
    D --> F
    E --> F
    F --> G[Rule-based risk scoring]
    G --> H[Human review]
    H --> I[Annotated dataset]
    I --> J[Experiment log]
    J --> K[Narrowing decision memo]
```

## Evidence Capture

Capture only what is needed:

- Post text
- Relevant replies/comments
- Redacted image references
- OCR text
- Visible links or handles
- Collection timestamp
- Evidence snapshot status

Do not store sensitive raw material in git.

## Signal Extraction

Signals should be transparent:

- Profit or benefit promises
- Urgency
- Private-channel redirection
- Suspicious links
- Fake authority or endorsement
- Suspicious testimonials
- OCR-only claims
- Reply-only redirection

## Triage Scoring

```mermaid
flowchart LR
    A[Observed signals] --> B{Strong combination?}
    B -->|Profit plus redirection| C[High risk review]
    B -->|Fake endorsement plus link| C
    B -->|Some weak signals| D[Medium risk review]
    B -->|No clear signals| E[Low risk or benign]
    B -->|Missing evidence| F[Insufficient evidence]
```

Risk scoring should produce:

- Risk tier
- Observed signals
- Explainable reasons
- Evidence source
- Missing evidence
- Suggested review status

## Human Review Loop

```mermaid
flowchart TD
    A[Baseline output] --> B[Annotator review]
    B --> C{Agreement?}
    C -->|Yes| D[Resolved label]
    C -->|No| E[Second review]
    E --> F[Guideline update candidate]
    F --> G[Decision log if taxonomy changes]
```

## Experiment Logging

Each experiment should leave:

- Dataset version
- Schema version
- Annotation guideline version
- Method
- Cost
- Metrics
- Error analysis
- Decision implication

## What This Is Not

This is not:

- A production enforcement system.
- A fully automated detector.
- A broad Meta intelligence platform.
- A legal fraud determination engine.
- A deepfake detection system.
