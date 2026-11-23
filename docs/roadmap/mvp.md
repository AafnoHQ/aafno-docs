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

**A validated starter curriculum.** A small set of units, written and accepted by native speakers, covering:

- A handful of high-use sentence frames.
- The grammar those frames require (word order, a first pass at pronouns and honorifics, a few postpositions, present-tense forms and negation, simple questions).
- Listening items for those same forms.
- Guided conversation turns that ask the learner to answer and to ask back.
- A script sequence that reaches reading and typing a simple sentence, usable on its own by the literacy pathway and in parallel by the others.

The MVP does not set a unit count before content review capacity is known. Each unit must have the outcome, prerequisites, activities, accepted answers, and QA record defined in [Curriculum](../learning/curriculum.md) and [Content QA](../learning/content-qa.md).

**Practice that matches the method.** For each unit, the learner hears a correct sentence, sees how it is built, rebuilds it, varies one slot, and uses it in a short exchange. Completion means they can understand and produce the form, and read it when the unit includes reading.

**Progress that respects the split.** Speaking progress and script progress are stored separately, as in [Data](../technical/database.md). The next unit follows prerequisites and obvious weaknesses (missed endings, missed letters).

**An application on Base44** that a learner can sign in to, take placement, study a unit, and see what to do next.

**This documentation**, published on GitHub Pages, kept aligned with what the MVP actually contains.

## What waits

- Live AI conversation, speech scoring, and model-written curriculum. Those wait for Tarka licensing and the validation in [AI integration](../technical/ai-integration.md).
- Handwriting instruction, if the first build can only support reading and typing.
- A large topic catalogue, dialect lessons, exam courses, and classrooms.
- A finished visual system. The MVP should look calm and readable, and follow [Visual identity](../design/visual-identity.md) — Aafno · आफ्नो, “Your language. Your roots. Your own.” — without inventing a second brand. Logo lockups and a licensed palette can land as soon as they exist; they do not block the first units.
- Payments and growth features that the platform does not already provide.

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

That is the demonstration. Broader grammar and approved AI practice are the next roadmap, written when this one is true.
