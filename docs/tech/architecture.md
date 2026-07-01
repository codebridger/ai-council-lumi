# Technical Architecture — Lumi

> Living doc. The current shape of the system at a high level. The *why* behind specific choices lives in `../../decisions/adr/`. Changing this doc is a council-level change (see `AGENTS.md` → "Editing rules for living docs").

## Overview
Lumi has two product lines that share a common core (Firebase, Vue, Gemini, and a knowledge base):

1. **Lumi ChatBot** — a Firebase-backed web app with an embeddable chat widget. A customer drops a one-line snippet into their site. When a shopper asks a question, the agent retrieves matching content from the customer's own knowledge base (embeddings in Firestore vector search), writes a grounded answer with Gemini, and can take action through connected tools. If the shopper needs a person, the conversation hands off to a live agent inbox; when no agent is Online, it falls back to an async email ticket.
2. **Lumi Hireable Agents** — an "AI employee" you hire that runs as an isolated, runnable job in its own container. See the section below. The detailed architecture lives in the internal design doc (TODO — see "Hireable Agent" below).

## Components — Lumi ChatBot
- **Embeddable widget** — Vue 3 + PrimeVue front end (TypeScript), loaded by a one-line JS snippet on the customer's site.
- **Agent dashboard / inbox** — Vue 3 + PrimeVue app where support staff read conversations, take over, and set Online/Away.
- **Backend** — Firebase Cloud Functions (serverless) handle retrieval, Gemini calls, tool actions, MCP bug reports, and handoff routing.
- **Retrieval layer** — customer docs are chunked, embedded, and stored in Firestore vector search; answers are grounded in retrieved content.
- **Tool/action layer** — function calls into connected shop, payment, and shipping systems (order lookup, returns, shipping status), plus MCP-based bug reporting.

## Hireable Agent (isolated job/container)
The Hireable Agent runs as an isolated, runnable job — each hired agent gets its own container rather than living inside the shared web app. The stated goal is a **simple architecture**.

> **TODO — needs the internal design doc.** The full architecture (job/container model, how jobs are triggered and scheduled, orchestration, inputs/outputs, isolation and security boundaries, and how it reuses the shared Gemini + knowledge-base core) lives in the team's ClickUp design doc, which is not yet accessible to this repo. Paste it in and this section gets filled properly — the notes above are the only confirmed facts so far.

## Data
- **Cloud Firestore** — conversations, messages, agent status, customer/store config, and document embeddings (via vector search).
- **Firebase Auth** — accounts for staff using the dashboard.
- Hireable Agent data model: TODO (from the design doc).

## Key integrations
- **Gemini** — answers and (likely) embeddings for the knowledge base.
- **MCP** — the agent files bug reports through MCP; MCP is also how tools/actions are wired.
- **Firebase Cloud Messaging (FCM)** — push notifications to agents when a handoff arrives.
- **Shop / payment / shipping systems** — the tools the ChatBot acts through. TODO: confirm the first connectors.
- **Container runtime / orchestration** for Hireable Agents — TODO: confirm from the design doc.

## Constraints & non-functional needs
- **GDPR / EU compliance** is first-class: data residency and privacy shape the design, not an afterthought.
- **Multilingual quality** (Baltic, Nordic, CEE) — retrieval and answers must hold up outside English.
- **Latency** — the widget must answer quickly to feel live.
- **Cost** — serverless spend must stay sane at small-shop scale; per-job container cost must stay sane for Hireable Agents.
- **Isolation** — each Hireable Agent job must run isolated from others (security and blast-radius).

## Known risks & tech debt
- Grounded, accurate retrieval across many languages is hard to keep good.
- Tool actions that change state (refunds, returns) need guardrails so the agent does not act wrongly.
- Handoff routing must be reliable when agents are Away (the email fallback is the safety net).
- Two product lines on one small team risks split focus — keep the shared core truly shared.
- TODO: confirm scaling assumptions, container orchestration choice, and single points of failure once the Hireable Agent design doc is in hand.
