---
title: Curriculum structure
parent: Learning
nav_order: 4
---

# Curriculum structure

This proposed structure turns the curriculum architecture into reusable, buildable content without deciding the detailed lesson order or grammar syllabus. A content item can serve multiple skills, but each delivery activity declares the skill evidence it collects.

## Strands and sub-strands

| Strand | Sub-strands / concept families | Shared content role |
| --- | --- | --- |
| Sound and pronunciation | Sound discrimination; intelligibility; stress/rhythm; sound–script links. | Audio, minimal contrasts after validation, and pronunciation-aware tasks support oral paths and literacy. |
| Devanagari literacy | Character and vowel recognition; syllable/word decoding; spelling; reading fluency; typing; handwriting/tracing when available. | Connects familiar spoken vocabulary to written forms; supports reading and writing evidence. |
| Grammar and meaning | Clause patterns; participant/reference choices; time/aspect/modality; negation/questions; relationships/connection; agreement and register-sensitive choices. | Supplies explainable choices for construction, comprehension, and productive feedback. |
| Sentence construction | Frames; substitution; transformation; expansion; repair. | Turns grammar and vocabulary into controlled productive evidence. |
| Vocabulary and lexical patterns | High-use words; topic sets; collocations; lexical relationships; register-marked expressions. | Supplies usable language across all strands and retrieval practice. |
| Listening comprehension | Word/sentence parsing; main idea; detail; intent; register cues; longer discourse. | Reuses approved text/audio at increasing support and complexity. |
| Conversation and interaction | Opening/responding; asking back; clarification; repair; requests; narratives; opinions; role-play. | Recombines approved patterns in ordinary situations and later bounded AI practice. |
| Cultural and register awareness | Honorific context; everyday/respectful/formal choices; family/regional/code-switched variation. | Adds contextual metadata to examples, tasks, and accepted answers. |

Concept-family labels are organising placeholders, not claims about a final grammatical taxonomy. Detailed Nepali forms, terminology, and sequence require validation.

## Dependency model

Dependencies are explicit links between concepts or units, not assumptions based on a learner's overall level.

```text
validated sound / meaning input
        ├── spoken vocabulary + basic pattern ──► listening / construction ──► interaction
        └── sound–script link ──► decoding ──► reading ──► typed writing
grammar explanation ───────────────────────────► controlled variation ─────► productive use
register metadata ─────────────────────────────► context-appropriate choices across pathways
```

Typical dependency rules:

- A productive task depends on comprehension of its target pattern plus enough vocabulary to vary it.
- A reading task depends on the relevant script decoding, not on oral proficiency beyond the text's language demand.
- A writing task depends on appropriate reading/spelling access and construction evidence; typing may precede handwriting.
- A register-sensitive task depends on the underlying pattern plus contextual explanation; it must not mark a legitimate labelled variant wrong.
- Review tasks depend on prior exposure but may cross strands to test retrieval in a new mode.

## Flexible entry and shared content

| Learner entry | Initial route | Shared item use |
| --- | --- | --- |
| Heritage speech | Listening check → production/grammar frames → interaction; add literacy at its own placement. | Familiar family situations can supply listening and conversation, while grammar tasks reveal the forms behind them. |
| Fluent speaker, new to script | Spoken self-check → sound–script links → decoding/reading/typing at known vocabulary. | The same approved sentence can be an oral known item, a reading prompt, and a typing task without reteaching its meaning. |
| Complete beginner | Sound + meaning + basic patterns → controlled listening/construction → parallel early script. | One approved frame can appear as audio, supported reading, construction, and a short exchange, with demand changed by activity. |

Shared content reduces duplication but does not erase assessment distinctions. One sentence may be reused across modalities, while completion, scaffolding, scoring, and the resulting skill update remain separate.

## Content object proposal for Base44

For later implementation, model a content concept separately from its rendered activities:

- **Concept:** strand/sub-strand, outcome, proficiency-band range, prerequisite links, register/variation metadata, and QA state.
- **Language asset:** validated text, Romanisation policy/display fields, English support, audio/transcript links, source/version, and review record.
- **Activity:** mode (listen, speak, read, write, construction, retrieval), prompt, scaffold, marking rule, accepted-variant policy, and evidence target.
- **Path rule:** eligible skills/bands, prerequisites, optional/review status, and a transparent reason it can be recommended.

This is a proposed modelling boundary, not a database schema. The application data design remains in [Data](../technical/database.md).

## Proposed build order

1. Define and validate a small starter concept map covering the MVP's approved oral patterns and independent script starter.
2. Attach unit contracts and activities that satisfy the methodology cycle for each concept.
3. Pilot placement tasks against the concept prerequisites and revise the maps where learners take unexpected routes.
4. Expand by concept family and proficiency band, keeping the same review record and dependency model.

Do not expand a topic catalogue or detailed tense/aspect list until native-speaker reviewers approve the concepts, terminology, examples, and sequencing. English tense labels may be useful learner-facing signposts, but they must not be used to force Nepali structures into an unsupported one-to-one scheme.

## Decisions and validation needs

**Proposed:** content reuse across modalities, explicit prerequisite links, and separate concept/asset/activity/path-rule records.

**Requires native-speaker validation:** all sub-strand definitions as applied to Nepali, dependency claims between actual forms, honorific/register metadata, accepted-variant policy, and each language asset.

**Open decisions:** the canonical content taxonomy; how variation tags appear to learners; which elements are required versus optional per band; handwriting scope; external-resource curation criteria; and the MVP concept map's exact boundaries.
