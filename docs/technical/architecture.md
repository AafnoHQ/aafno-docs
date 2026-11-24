---
title: Architecture
parent: Technical
nav_order: 1
---

# Architecture

## Confirmed direction

Aafno will have a custom TypeScript codebase. The first release is a web application built with Next.js and Tailwind CSS. Claude Code is the development agent and Cursor is the IDE. AI-assisted changes still need human review and testing for correctness, accessibility and security. Development tooling does not determine code quality or how quickly native apps can be delivered.

GitHub holds the application source in a separate repository. This repository contains the product and engineering documentation, published with GitHub Pages.

Web and future native clients share a backend, learner accounts, versioned curriculum and progress. The backend owns authorisation, official assessment, progression, content publication and approved calls to AI providers.

## Proposed stack

| Responsibility | Proposal |
| --- | --- |
| Database, identity and media | Supabase PostgreSQL, Auth and Storage |
| Backend operations | Server-side APIs and Supabase Edge Functions where appropriate |
| Web hosting | Vercel |
| Shared application code | Turborepo monorepo with shared domain logic, types and an API client |
| Future iOS and Android apps | Expo / React Native with EAS for builds and distribution workflows |

The service split and monorepo layout remain open. Share curriculum and learning rules, typed contracts and API access where useful. Each client can use an interface suited to its device. Shared packages do not give a client authority over assessment or publication.

## Web and native mobile

Desktop web is the main setting for deep grammar study, sustained reading and structured lessons. Future mobile apps are intended for quick review, flashcards, listening, voice practice and touch handwriting. The same account and progress should let a learner move between devices.

Expo is the preferred future direction because React Native gives us a separate mobile interface for touch, recording and playback, and local storage. Capacitor would package a web interface with access to native capabilities through plugins. That approach could reuse more web UI, while Expo better fits a mobile experience designed around those interactions. Both approaches require device testing and native integration work. Native release timing and scope are open, and the [MVP](../roadmap/mvp.md) ships on the web.

Future offline practice needs decisions about what to download, how to queue attempts, and how to reconcile concurrent changes on reconnect. Preserve distinct attempts, handle retries without counting them twice, and define how outdated content and conflicting preference changes are resolved. The backend validates synced evidence before updating official progress.

Before a native release, design microphone permissions and denied-permission flows, audio recording and playback across interruptions, and offline storage of downloaded or recorded media. Plan real-device testing and app store testing and submissions for both platforms.

## Backend responsibilities

- **Learning delivery:** resolve eligible units, serve accepted content versions, and keep attempts tied to the material the learner saw.
- **Assessment and progress:** validate evidence on the server, track listening, speaking, reading, writing and grammar independently, and explain the next step. Keep completion and demonstrated mastery separate.
- **Content administration:** restrict review and publication to authorised roles. Native-speaker acceptance is required before a curriculum version reaches learners.
- **Optional AI gateway:** call approved providers on the server through a provider abstraction and keep secrets server-side. Tarka is planned subject to quality, licensing, commercial and privacy validation. Core lessons, placement and progress work without it. See [AI integration](ai-integration.md).

See [Data](database.md) for the records and relationships the application needs. Service boundaries, schema and migrations, security and RLS policies, storage access, and privacy and retention rules still need design. Keep application secrets and learner data outside source control and documentation builds.
