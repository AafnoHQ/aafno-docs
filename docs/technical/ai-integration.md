---
title: AI integration
parent: Technical
nav_order: 2
---

# AI integration

AI is planned, not switched on. The intended provider is Tarka. The intended models are Nepali-specialised language models and Nepali-specialised speech models. Neither is approved for the product until two conditions are met: a commercial licence that allows this use, and a validation pass that shows the model is fit for teaching Nepali.

Until both are true, Aafno teaches with human-authored, native-speaker-validated material.

## Why the bar is this high

A language app repeats its mistakes into someone’s speech. A fluent-sounding error about honorifics, agreement, or spelling becomes a habit. General-purpose models are not assumed to know Nepali well enough to teach it. Specialisation is required, and specialisation still has to be checked on Aafno’s own lesson types.

## What AI is for, once approved

Approved models may support practice. They do not silently become the curriculum.

Language models, when licensed and validated, may:

- Continue a conversation inside a lesson’s allowed forms and situation.
- Propose additional example sentences for a frame a reviewer has already accepted.
- Comment on a learner’s written sentence against a known grammar point.
- Help personalise review by ranking which validated items the learner should see next.

Speech models, when licensed and validated, may:

- Provide listening audio from validated text, if native-speaker review accepts the audio.
- Score or comment on pronunciation for sounds and forms the lesson is actually teaching.
- Accept spoken answers in conversation practice.

## What AI is not for

- Publishing an explanation, sentence, or audio file as curriculum without native-speaker validation.
- Inventing grammar rules.
- Replacing placement with an opaque score the learner cannot understand.
- Sending learner speech or writing to a provider we do not have a licence and a data agreement for.
- Pretending a model is a native speaker.

Drafts are allowed. A draft is labelled as a draft in the content workflow and stays out of the learner’s path until review.

## Validation

Validation is a recorded check, not a vibe. For a model under consideration, reviewers who are native speakers of Nepali assess it on tasks Aafno actually uses:

- Grammatical accuracy on the forms in the early curriculum.
- Honorifics in context.
- Naturalness of example sentences (not only correctness).
- For speech: intelligibility, and whether the model’s pronunciation is acceptable as a model for learners.
- Failure behaviour: the model should be able to stay inside a lesson brief, and should refuse to bluff when a form is outside it.

A model that is impressive in open chat and unreliable on honorifics does not pass.

Results of those checks belong with the decision to adopt a model. They are not written here in advance.

## Personalisation

Personalisation may use model help to choose the next validated item. The items themselves remain from the validated set. The rules for pathway and placement are in [Curriculum](../learning/curriculum.md) and stay legible without a model: comprehension, production, and script are assessed separately.

## Privacy and licensing

Learner audio and free-text answers are personal data. They go to Tarka, or to any later provider, only under a commercial agreement that covers this product, with the retention and training terms known and acceptable. Licensing is a gate, not a footnote. If the licence is unclear, the integration does not ship.

Keys and credentials live in the application’s secret store. They are not committed to this documentation repository or to source.

## Build order

1. Teach the MVP with validated, non-model content. See [MVP](../roadmap/mvp.md).
2. Confirm licence terms with Tarka for the specific Nepali language and speech models.
3. Run the validation set. Record pass or fail by task.
4. Enable one task at a time, starting with the lowest risk: for example, drafting extra examples for human review, before live conversation.
5. Keep a path that still works if the provider is unavailable. A lesson does not hard-depend on a live model for its core explanation.
