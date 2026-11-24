# Aafno · आफ्नो

**Your language. Your roots. Your own.**

**आफ्नो भाषा, आफ्नै पहिचान।**  
Your language, your identity.

Aafno is a Nepali language-learning platform. It helps people reconnect with the language that’s theirs — to speak, understand, and read Nepali with confidence, not only recognise words.

This repository is the documentation for Aafno. It records product intent, learning design, technical direction, visual identity, and the path to a first release. The application itself is built separately.

## Purpose

Many people sit close to Nepali without being able to use it fully. Some understand family speech and freeze when it is their turn to answer. Some speak easily and cannot read or write Devanagari. Others are starting from the beginning.

Aafno is for that gap. Lessons are structured, grammar is taught rather than implied, and practice is meant to sound like conversation. Educational content is validated by native speakers before it is treated as curriculum.

## Who it is for

1. **Second-generation Nepalis** who understand spoken Nepali and struggle to speak it confidently.
2. **Nepali speakers** who communicate verbally and cannot read or write Devanagari.
3. **Complete beginners** who want to learn Nepali from scratch.

## How Aafno is different

Aafno is built around structured grammar, sentence construction, real conversational practice, listening comprehension, personalised learning, and native-speaker-validated content.

## Technology

| Area | Status |
| --- | --- |
| Application | Confirmed — custom TypeScript codebase, web first with Next.js and Tailwind CSS |
| Development | Confirmed — Claude Code as development agent, Cursor as IDE |
| Source and docs | Confirmed — GitHub source control and GitHub Pages for these docs |
| Backend and hosting | Proposed — Supabase PostgreSQL, Auth and Storage, server-side APIs and Edge Functions, and Vercel web hosting |
| Native mobile | Future direction — Expo / React Native for iOS and Android, with EAS for builds |
| Code organisation | Proposed — Turborepo monorepo with shared domain logic, types and API client |
| Product AI | Planned — Tarka, subject to quality, licensing, commercial and privacy validation |

See [Architecture](docs/technical/architecture.md) for the web and mobile responsibilities and the decisions still open.

## Documentation

| Section | What it covers |
| --- | --- |
| [Documentation home](docs/index.md) | Map of this repository |
| [Vision](docs/product/vision.md) | What Aafno is trying to achieve |
| [Audience](docs/product/audience.md) | The three starting audiences and what each needs |
| [What sets Aafno apart](docs/product/usps.md) | Product differences from typical language apps |
| [Language reference](docs/product/language-reference.md) | Grammar Library, Verb Conjugation Reference, and Nepali Dictionary |
| [Methodology](docs/learning/methodology.md) | How learning is designed |
| [Curriculum](docs/learning/curriculum.md) | Skill strands and pathways |
| [Proficiency framework](docs/learning/proficiency-framework.md) | CEFR-inspired skill descriptors and assessment principles |
| [Curriculum structure](docs/learning/curriculum-structure.md) | Reusable concepts, dependencies, and flexible learning routes |
| [Grammar syllabus](docs/learning/grammar-syllabus.md) | Phase 2A.1 master grammar inventory |
| [Grammar concept framework](docs/learning/grammar-concept-framework.md) | Phase 2A.2 step 1 template, [teaching depth](docs/learning/grammar-teaching-depth.md) and [present habitual worked example](docs/learning/concepts/present-habitual.md) |
| [Grammar catalogue](docs/learning/grammar-catalogue/index.md) | Phase 2A.2 Step 2 · 265 agreed concepts across 18 of 31 categories (58.1% category coverage) |
| [Content QA](docs/learning/content-qa.md) | How learner-facing Nepali is reviewed and released |
| [Architecture](docs/technical/architecture.md) | Platforms and how the pieces fit |
| [AI integration](docs/technical/ai-integration.md) | Planned use of Tarka and Nepali models |
| [Data](docs/technical/database.md) | Information the product needs to remember |
| [Visual identity](docs/design/visual-identity.md) | Brand direction |
| [Curriculum roadmap](docs/learning/curriculum-roadmap.md) | Five phases from product design to implementation requirements |
| [MVP](docs/roadmap/mvp.md) | First release |

## Brand

The name is **Aafno · आफ्नो**. The visual and verbal direction is refined Nepali modernism: contemporary, warm, and culturally rooted. It draws on Nepali architecture, traditional textiles, patterns, art, and Devanagari typography. The brand line is “Your language. Your roots. Your own.” The identity is described in [visual identity](docs/design/visual-identity.md).
