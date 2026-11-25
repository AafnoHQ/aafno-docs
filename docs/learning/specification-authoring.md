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

## Tracker sources and update process

| Field | Authority |
| --- | --- |
| ID, title and category | Active rows and category headings in the canonical catalogue |
| Specification path and authoring status | Canonical concept files and their identity sections |
| Batch membership, PR, structural review | `scripts/specification-status.json` batch records |
| Linguistic and native-speaker validation, mapping, publication | Draft defaults derived by QA. For any approved change, use a per-concept evidence-backed record in the same status file and update the corresponding specification identity. |
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

`--write` regenerates the progress tracker after source checks pass. The normal command detects stale generated output and exits with actionable errors for mandatory failures. Compare the active and original ID sets against the recorded approved baseline. A hash change requires an explicitly approved inventory change. Use the pull-request QA workflow for repeatable checks.

Check learning and linguistic quality during review. Automated QA checks Markdown structure, explicit and common heading anchors, selected link syntax and representation fields, draft status consistency and tracker freshness. It does not render Jekyll, verify external links or validate language, translations, educational completeness, appropriate social context or the full ownership model. Verify those separately where tooling and evidence permit.
