---
title: Data
parent: Technical
nav_order: 3
---

# Data

Aafno needs a durable record of who is learning, what they have been taught, and what they can do. The store lives with the Base44 application. This page names the information. It is not a schema: tables, field names, and indexes are chosen in the application repository when the data model is designed.

No learner data is stored in this documentation repository.

## Learner

Enough identity to run an account, and a profile that placement can update.

- Account identity, as provided by the application platform.
- Preferred writing system for interface chrome where we support a choice. Lesson Nepali stays in Devanagari once the learner is on the script strand; glosses may be in English.
- Pathway: heritage speech, literacy, beginner, or a combination (speech pathway plus script strand).
- Starting band within each active strand, from placement.
- Consent flags relevant to optional AI processing, left unset until [AI integration](ai-integration.md) is real.

## Curriculum content

The teaching material, separated from any one learner.

- Units and their strand (sound, script, grammar, construction, listening, conversation, vocabulary).
- Validated Nepali: explanations, sentences, prompts, and accepted answers.
- Audio references for listening items, once recorded or accepted.
- The grammar point and sentence frames a unit is responsible for.
- Content version and validation state: draft, in review, accepted, returned, or retired; who accepted it and when.
- Prerequisite links between units, so a pathway can order them.
- The unit contract: target skill, outcome, grammar point, sentence frames, accepted answers or marking rule, and register notes.

Draft AI output, if it is stored at all, is stored as draft content. It is not linked as a unit a learner can open.

## Progress

What this learner has done with that content.

- Units started, completed, and revisited. Completion follows the definition in [Curriculum](../learning/curriculum.md): understand, produce, and read when reading is in scope.
- Item-level results where they change review: correct, incorrect, or hesitant, with the form being practised.
- Script strand progress, independent of speaking progress.
- Placement results, kept so a later reassessment can be compared.

Progress is about forms and tasks. It is not a single global percentage that hides a strong listener who cannot yet speak.

## Practice artefacts

Spoken and written attempts, kept only as far as the product needs them for feedback, review, and support.

- The prompt the learner was answering.
- A reference to the audio or text they produced.
- The feedback shown, and whether it was rule-based or, later, from an approved model.
- Retention limits. Audio is not kept forever by default. Exact durations are a product decision before launch; the default intention is to keep what review and debugging need, and to delete the rest.

If a practice event is sent to Tarka, that fact is recorded with the event, under the agreement described in [AI integration](ai-integration.md), together with the provider capability and version used. Do not store a raw audio or text artefact merely because an event exists; keep the minimum needed for the agreed feedback, support, and deletion process.

## Personalisation inputs

Derived from progress, not from a second hidden profile.

- Forms with repeated production errors.
- Forms the learner can recognise and cannot produce. This distinction matters for heritage learners.
- Script items that are slow or wrong.
- The next eligible units, computed from prerequisites and those weaknesses.

A person should be able to understand why the next lesson appeared. “The model felt like it” is not an explanation we store as the only reason.

## Required relationships

The implementation may choose different table names, but it needs to preserve these relationships:

- One learner has independent skill and strand placements, progress records, and consent states.
- One unit has prerequisites and many versioned content items; only accepted versions are deliverable.
- One attempt belongs to one learner, activity, and content version, and can create a review signal.
- One QA record belongs to one content version and records the reviewer decision.
- One optional AI event belongs to one attempt and identifies the approved task and provider version.

This is the minimum needed to support personalisation, audit a learner-facing correction, and withdraw a content version safely.

## What we do not need yet

The first data model does not need social graphs, public profiles, class rosters, or a content marketplace. Those can be added when a real feature needs them. Payments, if Base44 or a store handles them, stay at the platform boundary rather than being reinvented in our tables.

## Care

Nepali learning data is ordinary personal data and should be treated as such: access limited to the application, exports and deletion available when the platform account requires them, and no production dumps in this repo, in tickets, or in prompts. Example sentences in the docs are teaching material, not learner data. Exact retention durations, deletion timing, account recovery, and roles with access to support artefacts are open decisions before launch.
