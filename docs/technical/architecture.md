---
title: Architecture
parent: Technical
nav_order: 1
---

# Architecture

Aafno’s technical shape is intentionally small at the start. The learning product runs on Base44. This repository holds the documentation and is published with GitHub Pages. Day-to-day writing and editing happen in Cursor. Source control is GitHub.

```text
Learners
   │
   ▼
Base44 application        ← lessons, practice, learner progress
   │
   ├── Content (validated Nepali)
   ├── Learner profile and pathway
   └── Practice records

Tarka (planned)           ← Nepali language and speech models,
                             after licensing and validation
   │
   └── called by the application only for approved tasks

GitHub
   ├── Application source (separate repository)
   └── aafno-docs (this repository)
          │
          └── GitHub Pages
```

## Application

The product learners touch is a Base44 application. It is responsible for accounts, the learning experience, progress, and any later calls to AI. This documentation repository does not contain that application.

Base44 is the platform choice. Detailed service boundaries inside Base44 should be written down when the app repository exists, next to the code they describe. Until then, this page states responsibilities, not a folder layout we do not have.

At minimum, the application separates these responsibilities even if Base44 implements them together:

- **Learning delivery:** resolve an eligible unit, render its activities, and use only accepted content.
- **Assessment and progress:** store independent listening, speaking, reading, writing, and grammar results; derive a transparent next step.
- **Content administration:** draft, review, accept, revise, and retire curriculum without exposing drafts to learners.
- **Optional AI gateway:** make approved provider calls from the server side, apply task-specific constraints, and record the provider and version used.

Client screens must not hold provider keys or decide whether unreviewed content is publishable.

## Documentation

Human-facing product and engineering notes live here, under `docs/`. GitHub Pages serves them. The [repository README](https://github.com/AafnoHQ/aafno-docs) is the front door for anyone landing on the repository.

Pages in this repo are Markdown. They are the source of truth for intent. If the app disagrees with a page, either the app is unfinished or the page is out of date — and the change should be explicit in a commit, not silent.

## AI

AI is a planned dependency, not part of the current core. The provider in view is Tarka. Models must be Nepali-specialised language and speech models, and they are in scope only with commercial licensing and validation. The rules for what they may do are in [AI integration](ai-integration.md).

The curriculum must be teachable without an unvalidated model in the loop. Core lessons, validated audio, and progress tracking do not wait on Tarka.

## Data

What the application needs to remember is described in [Data](database.md). The store is part of the Base44 application. This repo does not host learner data.

## Delivery rules

- A learner can only receive content whose status is accepted.
- A learner's pathway can combine different starting bands by skill and strand; it is not one global level.
- Core lesson delivery, placement, and progress continue when an AI provider is unavailable.
- Content updates are versioned so an attempt remains attributable to the material the learner actually saw.
- Application secrets, provider agreements, and learner data stay outside GitHub and documentation builds.

## Environments and source control

- Development happens locally in Cursor.
- Version control is Git on GitHub.
- Documentation changes land in this repository (`AafnoHQ/aafno-docs`).
- Application code lands in its own repository when that project is created.

There is no production deployment described here beyond GitHub Pages for docs and whatever Base44 provides for the app. Secrets, keys, and model credentials do not belong in this repository.

## What is decided

| Decision | Status |
| --- | --- |
| Application platform is Base44 | Decided |
| Docs live in GitHub and are hosted on GitHub Pages | Decided |
| Editing environment is Cursor | Decided |
| AI provider is Tarka | Planned |
| Nepali language and speech models | Planned, subject to commercial licensing and validation |
| Internal schema and service layout | Not yet specified |
| Content review workflow | Defined; reviewer operations remain open |
| AI gateway and provider failover | Required boundary; implementation not yet specified |
