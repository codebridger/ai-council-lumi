# Technical Architecture — Lumi

> Living doc. The current shape of the system at a high level. The *why* behind specific choices lives in `../../decisions/adr/`. Changing this doc is a council-level change (see `AGENTS.md` → "Editing rules for living docs").

## Overview
Lumi has two product lines that share a common core (Firebase, Vue, Gemini, and a knowledge base):

1. **Lumi ChatBot** — a Firebase-backed web app with an embeddable chat widget. A customer drops a one-line snippet into their site. When a shopper asks a question, the agent retrieves matching content from the customer's own knowledge base (embeddings in Firestore vector search), writes a grounded answer with Gemini, and can take action through connected tools. If the shopper needs a person, the conversation hands off to a live agent inbox; when no agent is Online, it falls back to an async email ticket.
2. **Lumi Hireable Agents** — hire AI agents that run real work. An agent takes input from any communication channel, uses MCPs to do the work, and delivers results to a destination. Agents and people coordinate through a **Task Board**, and agents can also work inside owner-connected channels (Slack, ClickUp, Telegram, etc.). Each agent run is isolated and runs through a queue within a time/token window. See the section below.

## Components — Lumi ChatBot
- **Embeddable widget** — Vue 3 + PrimeVue front end (TypeScript), loaded by a one-line JS snippet on the customer's site.
- **Agent dashboard / inbox** — Vue 3 + PrimeVue app where support staff read conversations, take over, and set Online/Away.
- **Backend** — Firebase Cloud Functions (serverless) handle retrieval, Gemini calls, tool actions, MCP bug reports, and handoff routing.
- **Retrieval layer** — customer docs are chunked, embedded, and stored in Firestore vector search; answers are grounded in retrieved content.
- **Tool/action layer** — function calls into connected shop, payment, and shipping systems (order lookup, returns, shipping status), plus MCP-based bug reporting.

## Components — Lumi Hireable Agents
The goal is a **simple architecture**. The main parts:

- **Agent** — the core worker. It takes input from any connected communication channel, uses MCPs to do the task, and delivers the result to a destination. What an agent can do depends on the characteristics and tools it is given.
- **Task Board** — the default collaboration environment. Agents and people work together here: either side defines a request as a task and assigns it to an agent or a person to do the next step. This is how work is handed back and forth.
- **Collaboration environments** — an agent can operate in more than one place. The Task Board is the default; owners can also connect other environments — Slack, ClickUp, Telegram, and other third-party task managers and messengers.
- **Isolated runner** — each agent run is isolated in its own runnable job/container.
- **Execution queue** — an owner can define as many agents as they want, but activities go through a **queue** and run **one by one** within the plan's limited **time and token window**. A **top-up** mechanism lets owners boost throughput when they hit the limit (see `../marketing/brand.md` → Pricing).

> **TODO — still brainstorm-level.** The concrete infrastructure (container runtime and orchestration, queue technology, how the Task Board is stored, trigger/scheduling model, isolation and security boundaries, and how much of the shared Gemini + knowledge-base core it reuses) is not settled yet. Firm these up as the design lands.

## Data
- **Cloud Firestore** — conversations, messages, agent status, customer/store config, and document embeddings (via vector search).
- **Firebase Auth** — accounts for staff using the dashboard.
- **Hireable Agents** — tasks, task assignments (to an agent or a person), agent definitions and tools, connected collaboration environments, and run/queue records. Exact stores TODO.

## Key integrations
- **Gemini** — answers and (likely) embeddings for the knowledge base.
- **MCP** — the agent files bug reports through MCP; MCP is also how tools/actions are wired.
- **Firebase Cloud Messaging (FCM)** — push notifications to agents when a handoff arrives.
- **Shop / payment / shipping systems** — the tools the ChatBot acts through. TODO: confirm the first connectors.
- **Collaboration channels** for Hireable Agents — Slack, ClickUp, Telegram, and other task managers/messengers an owner connects as agent environments.
- **Container runtime / orchestration + queue** for Hireable Agents — TODO: confirm the tech once chosen.

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
