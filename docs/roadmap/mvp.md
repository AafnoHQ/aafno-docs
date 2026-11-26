---
title: MVP
nav_order: 6
---

# MVP

The first release proves that a person can get better at Nepali on Aafno — speak more than they could, follow a short utterance, or read a sentence they could not read — using the method in [Methodology](../learning/methodology.md). It does not prove every future strand, and it does not depend on Tarka.

## Who the MVP is for

All three audiences in [Audience](../product/audience.md), in reduced form:

- A heritage-speech path that starts from production, not from the alphabet.
- A literacy path for people who already speak and need Devanagari.
- A beginner path with a short spoken core and script introduced alongside it.

Placement can be a concise self-check plus a few tasks (understand, produce, read a simple line). A perfect adaptive engine is not required. A wrong long course is the failure to avoid.

## What ships

**A validated starter curriculum.** A small set of units, written and accepted by native speakers, drawn from the [curriculum roadmap](../learning/curriculum-roadmap.md). The starter scope covers:

- A handful of high-use sentence frames.
- The grammar those frames require (word order, a first pass at pronouns and honorifics, a few postpositions, present-tense forms and negation, simple questions).
- Listening items for those same forms.
- Guided conversation turns that ask the learner to answer and to ask back.
- A script sequence that reaches reading and typing a simple sentence, usable on its own by the literacy pathway and in parallel by the others.

The MVP does not set a unit count before content review capacity is known. Each unit must have the outcome, prerequisites, activities, accepted answers, and QA record defined in [Curriculum](../learning/curriculum.md) and [Content QA](../learning/content-qa.md).

**Practice that matches the method.** For each unit, the learner hears a correct sentence, sees how it is built, rebuilds it, varies one slot, and uses it in a short exchange. Completion means they can understand and produce the form, and read it when the unit includes reading.

**Progress that respects the split.** Speaking progress and script progress are stored separately, as in [Data](../technical/database.md). The next unit follows prerequisites and obvious weaknesses (missed endings, missed letters).

**A custom web application**, built with TypeScript, Next.js and Tailwind CSS, that a learner can sign in to, take placement, study a unit, and see what to do next.

**This documentation**, published on GitHub Pages, kept aligned with what the MVP actually contains.

## What waits

- Native iOS and Android apps and offline synchronisation. The MVP is web-first. Device roles and future native work are described in [Architecture](../technical/architecture.md).

- Live AI conversation, speech scoring, and model-assisted curriculum drafts. These depend on provider approval and the validation in [AI integration](../technical/ai-integration.md).
- Handwriting instruction, if the first build can only support reading and typing.
- A large topic catalogue, dialect lessons, exam courses, and classrooms.
- A finished visual system. The MVP should look calm and readable, and follow [Visual identity](../design/visual-identity.md) — Aafno · आफ्नो, “Your language. Your roots. Your own.” — without inventing a second brand. Logo lockups and a licensed palette can land as soon as they exist; they do not block the first units.
- Payments and growth features.

## Feature backlog

These Step 3A proposals are available for future scope review. MVP commitments are listed under [What ships](#what-ships).

| Capability | Product requirement |
| --- | --- |
| Interactive sentence explorer | Inspect subjects, understood subjects, roles, case markers, predicates, agreement and contextual meaning. Link to canonical grammar and dictionary entries. Offer “Show understood subject” where appropriate and independent Devanagari, Romanisation and English controls. |
| Meaning-based construction discovery | Search by intentions such as expressing hunger or uncertainty, saying what one likes, reporting information and asking respectfully. Make grammatical terminology optional. |
| Grammatical meaning comparison explorer | Compare habitual and progressive, agent and experiencer, hearsay and discovery, and source-unspecified assertions and conjecture. Show shared content and explain how the change affects meaning and context. |
| Household language preferences | Prioritise validated examples and practice reflecting standard respectful forms, highest-honorific forms, both or unsure. Retain access to the full shared curriculum and validated variants. Use evidence and context for correctness. Avoid requiring caste, ethnicity or community disclosure. Onboarding design remains open. |
| Variant-aware references | Surface multiple validated alternatives, meanings, contexts, register, audio and canonical links across all three reference tools. Present reviewed full and contracted highest-honorific variants within the same register. |
| Moderated learner contributions | Take a Romanised expression, intended meaning, optional Devanagari, usage context, social relationship or register, and optional audio with appropriate consent. Queue for evidence and duplication checks, linguistic and native-speaker review, and approval or further research. Protect privacy and record consent and reuse rights before publication. |
| Information relay activities | Have a learner receive information from one speaker and convey it to another. Observe comprehension, meaning preservation, personal and temporal reference, agreement, register and source marking separately where demonstrated. |
| Progressive sentence builder | Build a core sentence, then add or remove time, place, frequency, manner or other optional information in reviewed frames. Use contextual feedback, canonical component annotations and links to vocabulary and conjugation. Reuse the sentence explorer annotations, support the three display controls, and record guided and independent evidence separately. A proposed [contextual noun phrase builder](../product/language-reference.md#noun-phrase-builder-extension) extends this activity. Proposed [adjective agreement explorer](../product/language-reference.md#adjective-agreement-explorer) and [progressive sentence modifier](../product/language-reference.md#progressive-sentence-modifier) extensions support reviewed agreement and adverbial scope comparisons. |
| Interactive pronoun reference | Future Grammar Library capability for searching reviewed person, number, register, case and possessive forms, agreement and household alternatives. Reuse canonical entries, examples, approved audio and variant-aware usage notes. A proposed [interactive reference explorer](../product/language-reference.md#reference-explorer-extension) extends this capability and the sentence explorer. |

## Content rule for the MVP

Every Nepali sentence, explanation, accepted answer, transcript, and audio file in the learner path has a native-speaker acceptance recorded against its version. Volume is whatever can be validated, not whatever can be generated. A short course that is right is the MVP. A long course that is unreviewed is a different product, and not this one.

## Acceptance criteria

The MVP is ready for learner testing when:

1. A new learner can sign in, complete placement, see a recommended pathway, and change that recommendation.
2. Each starter pathway opens only accepted curriculum content and has a usable first unit.
3. Every unit follows the core pattern: hear/read, understand construction, rebuild, vary, then use in an exchange.
4. Progress for speech and script is recorded independently; the next unit explains its prerequisite or review reason.
5. A learner can replay audio, view an answer or feedback result, and resume their latest progress.
6. No live provider call is necessary to complete placement, a unit, or the starter pathway.
7. A content issue can be reported to the review process and a corrected content version can replace the learner-facing one.

## Done

The MVP is done when a learner from each of the three starts can:

1. Land in a path that does not insult what they already know.
2. Finish the starter units.
3. Understand a short utterance that uses the taught forms.
4. Say a sentence in those forms that is not a line they memorised whole.
5. Read and type a simple Devanagari sentence if their path includes the script starter.

The exact MVP subset is selected during syllabus mapping. The comprehensive syllabus can cover later releases, and published units follow the native-speaker review gate.
