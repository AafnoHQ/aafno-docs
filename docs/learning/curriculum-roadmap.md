---
title: Curriculum roadmap
parent: Learning
nav_order: 6
---

# Curriculum roadmap

Aafno develops the curriculum in five phases. Discuss and agree each phase and each Phase 2 stage, document its outcome, and review it before proceeding. Record any applicable native-speaker validation still due at each review.

## Phase 1 — Product and learning design

Complete from a product design perspective, pending applicable native-speaker validation. The [curriculum architecture](curriculum.md), [proficiency framework](proficiency-framework.md) and [curriculum structure](curriculum-structure.md) record the decisions. These include independent listening, speaking, grammar, reading and writing profiles, parallel Devanagari literacy, Devanagari, Romanisation and English visible by default with independent controls, and separate records for lesson completion and demonstrated mastery.

## Phase 2 — Master syllabus {#phase-2--master-syllabus}

Phase 2 develops the master syllabus across the following stages.

| Stage | Scope |
| --- | --- |
| 2A — Grammar and language | Master grammar inventory, concept specification, provisional progression and grammar dependencies. |
| 2B — Devanagari literacy | Literacy progression across recognition, decoding, reading and writing. |
| 2C — Vocabulary | Vocabulary and lexical patterns, including their role in using the language across strands. |
| 2D — Listening, conversation and pronunciation | Receptive and interactive skills, speech intelligibility and pronunciation development. |
| 2E — Integrated syllabus | Map the strands to Aafno’s CEFR-inspired A1–C2 bands, reconcile prerequisites across strands and select the MVP subset. |

Register and variation run through every stage. Document how everyday, respectful and formal speech, regional and family usage, and code-switching affect examples and accepted responses. Validate claims about Nepali forms, terminology, naturalness, usage and sequencing where applicable.

### Phase 2A — Grammar and language

| Step | Deliverable | Status |
| --- | --- | --- |
| 2A.1 | [Master Nepali grammar inventory](grammar-syllabus.md) | Product scope approved. Linguistic and native-speaker validation pending. |
| 2A.2 | Concept specification and teaching depth | Step 1 reviewed and merged. Step 2 covers all 31 categories. Five reconciliation batches approved and merged. Step 3A merged. Step 3B Batch 1 merged. Batch 2 merged. Batch 3 merged. Batch 4 awaits product-owner review. Later batches, Step 3C and Step 4 are planned. |
| 2A.3 | Provisional A1–C2 grammar progression | Planned. Map when forms are introduced, developed and demonstrated. |
| 2A.4 | Grammar prerequisites and dependencies | Planned. Identify the grammar knowledge and evidence that later concepts depend on. |

#### Phase 2A.2 — Concept specification and teaching depth {#phase-2a2-concept-specification-and-teaching-depth}

1. **Document the specification template, teaching depth and one worked example.** The [grammar concept framework](grammar-concept-framework.md), [teaching depth guide](grammar-teaching-depth.md) and [present habitual example](concepts/present-habitual.md) were reviewed and merged. The linguistic examples remain drafts.
2. **Review and merge the reconciled master concept catalogue.** All five batches have structural approval. The [grammar catalogue](grammar-catalogue/index.md) contains 500 planned learner targets across 31 categories. The [reconciliation records](grammar-catalogue/reconciliation.md) preserve all 527 original IDs and outcomes. The Step 2 implementation was merged in PR #8. Linguistic and native-speaker validation remains pending.
3. **Author grammar concept specifications.**
   - **Step 3A — Pilot consolidation.** The product owner approved seven pilot directions. The [seven canonical drafts](concepts/index.md#step-3a-pilots), framework and supporting requirements were reviewed and merged in [PR #9](https://github.com/AafnoHQ/aafno-docs/pull/9). Linguistic and native-speaker validation remains open.
   - **Step 3B — Remaining specifications.** The approved [first batch](specification-batches.md#step-3b-batch-1) covers sentence structure and personal pronouns and is merged. The [second batch](specification-batches.md#step-3b-batch-2) covers the remaining pronouns and all noun targets and is merged. The [third batch](specification-batches.md#step-3b-batch-3) covers adjectives and adverbs and is merged. The [fourth batch](specification-batches.md#step-3b-batch-4) covers numbers, quantities and determiners and completes the authoring of all 55 Grammar Foundations specifications. Batch 4 awaits product-owner review. The [tracker](specification-progress.md) derives the number remaining. Continue after explicit approval, using the [authoring workflow](specification-authoring.md) and adaptive batch sizes.
   - **Step 3C — Cross-category consistency.** After authoring, check canonical ownership and conflicting rules, duplicate evidence, prerequisites, terminology, highest-honorific and variant coverage, teaching depth, language representations and validation completeness. Submit proposed catalogue changes for approval.
4. **Review the full set.** Check coverage, consistency, teaching depth, [Highest honorific (Ati Uchcha Aadar)](highest-honorific.md), reference integration and [Content QA](content-qa.md).

The [authoring guide](specification-authoring.md) defines drafting, validation, progress tracking, decision escalation, QA and PR review.

Phase 2A.3 progression and Phase 2A.4 dependency mapping follow this work.

Integrated mapping across all strands and MVP selection remain in Phase 2E.

## Phase 3 — Lessons and activities

Turn mapped concepts into unit contracts, lessons, activities and review items. Specify the context, target evidence, scaffolding, and accepted variants. Prepare teaching assets for native-speaker review.

## Phase 4 — Assessment and personalisation

Design placement, assessment evidence and mastery criteria by skill. Define how the evidence supports prerequisites, progression and explainable recommendations, then review those rules against representative learner pathways.

## Phase 5 — Application implementation requirements

Translate the reviewed learning and assessment design into application requirements for delivery, content review, data, progress and supported devices. Review the implementation requirements before building the application.

## Syllabus, release scope and publication

- **Master syllabus** — the comprehensive map of what Aafno intends to teach across skills and proficiency bands, with dependencies and variation recorded.
- **MVP subset** — the limited selection from that map that supports the three starter pathways in the [MVP](../roadmap/mvp.md). Selection happens in stage 2E.
- **Published curriculum** — the learner-facing versions of units and assets that have passed native-speaker review and acceptance under [Content QA](content-qa.md). Syllabus agreement and selection for a release are separate from publication approval.
