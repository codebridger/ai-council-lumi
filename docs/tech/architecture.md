# Technical Architecture — Lumi

> Living doc. The current shape of the system at a high level. The *why* behind specific choices lives in `../../decisions/adr/`. Changing this doc is a council-level change (see `AGENTS.md` → "Editing rules for living docs").

## Overview
Lumi is a Firebase-backed web app with an embeddable chat widget. A customer drops a one-line snippet into their site to load the widget. When a shopper asks a question, the agent retrieves matching content from the store's own docs (stored as embeddings in Firestore vector search), writes a grounded answer with an LLM, and can take action through connected tools. If the shopper needs a person, the conversation hands off to a live agent inbox; when no agent is Online, it falls back to an async email ticket.

## Components
- **Embeddable widget** — Vue 3 + PrimeVue front end, loaded by a one-line JS snippet on the customer's site.
- **Agent dashboard / inbox** — Vue 3 + PrimeVue app where support staff read conversations, take over, and set Online/Away.
- **Backend** — Firebase Cloud Functions (serverless) handle retrieval, LLM calls, tool actions, and handoff routing.
- **Retrieval layer** — customer docs are chunked, embedded, and stored in Firestore vector search; answers are grounded in retrieved content.
- **Tool/action layer** — function calls into connected shop, payment, and shipping systems (order lookup, returns, shipping status).

## Data
- **Cloud Firestore** — conversations, messages, agent status, customer/store config, and document embeddings (via vector search).
- **Firebase Auth** — accounts for store staff using the dashboard.

## Key integrations
- **LLM provider** — answers and embeddings. TODO: confirm which provider(s).
- **Firebase Cloud Messaging (FCM)** — push notifications to agents when a handoff arrives.
- **Shop / payment / shipping systems** — the tools the agent acts through. TODO: confirm the first connectors.

## Constraints & non-functional needs
- **GDPR / EU compliance** is first-class: data residency and privacy shape the design, not an afterthought.
- **Multilingual quality** (Baltic, Nordic, CEE) — retrieval and answers must hold up outside English.
- **Latency** — the widget must answer quickly to feel live.
- **Cost** — serverless spend must stay sane at small-shop scale.

## Known risks & tech debt
- Grounded, accurate retrieval across many languages is hard to keep good.
- Tool actions that change state (refunds, returns) need guardrails so the agent does not act wrongly.
- Handoff routing must be reliable when agents are Away (the email fallback is the safety net).
- TODO: confirm scaling assumptions and any single points of failure in the Firebase setup.
