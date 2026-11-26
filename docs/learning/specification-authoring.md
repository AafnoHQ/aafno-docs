---
title: Specification authoring
parent: Learning
nav_exclude: true
---

# Specification authoring

Step 3B turns active catalogue targets into reviewable specifications, grouped by grammatical family. Use catalogue order by default and group related concepts where comparison improves coverage. Authorship order is independent of learner progression. Complex batches usually have 5–8 concepts, standard batches 10–15, and mature, closely related batches 15–20. Select scope with product-owner approval.

## Drafting and review workflow

1. Start from current main. Confirm the approved batch scope, and read catalogue rows, reconciliation, traceability, the related pilots and the [decision register](curriculum-decisions.md). Identify canonical owners before drafting.
2. Use all 15 sections and seven conventions in the [framework](grammar-concept-framework.md#reusable-specification). Follow the [seven pilots](concepts/index.md#step-3a-pilots) as the quality benchmark. Include formation, meaningful distinctions, exceptions, contrastive and natural examples, feedback, prerequisites, activities and independent evidence to the depth the target requires.
3. Use local observable outcomes, map each to the four teaching depths, and specify what is assessed independently. Shared examples and activities can elicit evidence for multiple targets when the task observes each one separately. See [teaching depth](grammar-teaching-depth.md) and [variant-aware assessment](proficiency-framework.md#variant-aware-assessment).
4. Record contextual meaning, participants, agreement, register, polarity, time and aspect, source, audio and review status where applicable. Use Devanagari, Romanisation and English for applicable material, including examples in corrections and assessments. Keep provisional forms or missing representations visible in the validation register instead of supplying unsupported material.
5. Keep new material in draft. Distinguish illustrative examples, reported usage, attestation, linguistic review, native-speaker review, approved versions and publication eligibility. Record each question under the concept’s Content validation section and link relevant shared [research themes](specification-research.md).
6. Update the batch record, concept navigation and catalogue links. Check the same outcome, constraints and canonical ownership across reused examples. Regenerate the [progress tracker](specification-progress.md) and run [QA](#qa).
7. Open a dedicated PR from current main. Include concept IDs and paths, outcome and section counts, ownership boundaries, catalogue and traceability integrity, progress, commands and results, unresolved evidence and product decisions, any pilot changes and incomplete checks. Stop for product-owner review before starting another batch.

Routine drafting uses approved conventions. Log linguistic uncertainties as research, and flag suspected duplicate concepts for Step 3C or explicit review. Escalate changes to canonical ownership, curriculum-wide rules, catalogue scope, assessment design and new product commitments. If material uncertainty prevents coherent drafting, request a decision. Formal progression, curriculum-wide dependencies, MVP selection and lesson authoring belong to later [roadmap phases](curriculum-roadmap.md).

## Educational completeness review

For each specification, a reviewer must compare the full catalogue target with the draft’s coverage and use the approved pilots as the quality benchmark. Section count, tracker generation and successful structural QA do not establish educational completeness. There is no word-count target. Document omissions or unresolved coverage before approving the batch.

- Walk through at least the representative construction or analysis step by step. Review meaningful variants, contrasting examples, contextual limits and rule ownership. Keep plausible provisional teaching analysis separate from claims that need evidence.
- Keep independently assessable targets in separate activity prototypes. For each prototype, state the learner prompt, expected response, assessment target, feedback with a meaningful retry, and draft validation status. When prototypes reuse an example, specify which response earns evidence for each target. Keep provisional grammatical analyses outside scoring until they are validated.
- Review actual learner prompts, expected responses, corrections and meaningful retries. Check whether independent tasks elicit each outcome and distinguish adjacent targets, and whether flexible application requires a concept-specific decision or transfer.
- Review required, helpful, co-taught and extension prerequisites where applicable. Check that substantive research questions identify evidence needed, context, scope and the reviewer decision to record.
- Manually review Devanagari, Romanisation and English in worked models, prose, dialogue, tables, corrections and activity prototypes. QA checks structured contextual tables, so other formats need manual inspection. Record any missing representation as a research gap.
- Before awarding any approval, open the linked evidence and confirm reviewer authority, the concept and reviewed version, the exact decision, and its applicability and reuse or publication scope. An existing link alone does not establish approval.

### Pre-PR assessment audit

Make a second pass through sections 12 and 13 of every new specification before requesting review.

1. Compare each prompt and expected response with its stated local outcome. Identify the observable response and check that it requires recognition, interpretation, selection or production as claimed.
2. Record independent evidence separately even when prompts share a scene. Hide model answers for unaided production. If wording or examples are supplied as a scaffold, record the response as guided practice.
3. Check that feedback explains a plausible mistake and asks the learner to apply the distinction in a meaningful retry. Record acceptable contextual alternatives and take unresolved analyses out of scoring until reviewed.
4. Check the canonical boundary. Separate adjective class from applying agreement, noun gender and plurality from adjective selection, and recognising a construction from producing it. For adverbs distinguish recognition, attachment and scope; keep tense, habitual aspect, numeral formation, information source and noun quantity separate. Check event-order interpretation separately from sequencing production.
5. Record the audit findings in the PR alongside outstanding validation limitations. Automated structural QA supports this review.

**Language evidence and scaffolding.** Require an observable response to Nepali wording, or an actual Nepali production response, for representative recognition, interpretation and production tasks. English-only conceptual reasoning can prepare the learner for a task. It cannot establish Nepali grammatical mastery by itself. Hide any gloss, prompt wording, visual label or key that supplies the grammatical distinction or answer being assessed. Keep vocabulary, translations, diagrams and number keys available for supporting knowledge when they do not disclose the target. Check each meaningful constituent skill of an outcome and give it concrete evidence, even when more than one independently scored sub-task is needed.

**Outcome coverage.** In the pre-PR audit, cross-check sections 2, 11, 12 and 13. Every local outcome needs its own concrete representative prompt or separately scored sub-task in section 12, linked to observable evidence, expected responses, ownership, meaningful retry and validation limitations. Record a coverage matrix in the review. Supply values, vocabulary, clocks, proportions or totals when arithmetic and number recall are supporting knowledge. Keep the target wording hidden in production. Flag and fix uncovered or misaligned outcomes before review.

**Recognition, interpretation, production and transfer.** A recognition response identifies the relevant form or structure. An interpretation response explains the meaning or relationship in the supplied context. A production response requires learner-generated language with the target hidden. Where the catalogue requires transfer, provide a genuinely unfamiliar example within an established class or construction, supply the supporting vocabulary, forms or stem as needed, and hide the expected output. Score transfer independently of recognising the model or reciting a memorised paradigm. Record where class membership, register or construction remains uncertain. Keep Phase 2C vocabulary recall outside grammatical scoring unless separately assessed.

## Tracker sources and update process

| Field | Authority |
| --- | --- |
| ID, title and category | Active rows and category headings in the canonical catalogue |
| Specification path and authoring status | Canonical concept files and their identity sections |
| Batch membership, PR, structural review | `scripts/specification-status.json` batch records |
| Linguistic and native-speaker validation, mapping, publication | Draft defaults derived by QA. For any approved change, use a per-concept evidence-backed record in the same status file with a repository-relative Markdown path and anchor for each approval and update the corresponding specification identity. |
| Related decisions and research | Batch register and concept validation sections |
| Totals and status presentation | Generated tracker |

Adjust batch data only when the scope or review status is approved. A concept outside a recorded batch is unassigned. Authoring status is independent of the catalogue’s planned status. A validated or mapped status requires the respective decision record, and publication eligibility requires reviewed linguistic and native-speaker evidence.

## QA

Run from the repository root with Python 3.10 or later.

```sh
python3 scripts/specification_qa.py --write
python3 scripts/specification_qa.py
python3 -m unittest discover -s scripts -p 'test_*.py'
```

`--write` regenerates the progress tracker after source checks pass. The normal command detects stale generated output and exits with actionable errors for mandatory failures. Compare active and original ID sets, active learning outcomes and reconciliation destinations against the recorded approved baseline. An approved change to those records is required before updating a fingerprint. QA checks that approval evidence paths and anchors resolve. The reviewer verifies the decision’s content and applicability. Use the pull-request QA workflow for repeatable checks.

Check learning and linguistic quality during review. Automated QA checks Markdown structure, explicit and common heading anchors, selected link syntax and representation fields, draft status consistency and tracker freshness. It does not render Jekyll, verify external links or validate language, translations, educational completeness, appropriate social context or the full ownership model. Verify those separately where tooling and evidence permit.
