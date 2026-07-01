# Product Requirements — Lumi

> Living doc. This is the current state of the product, not a decision record. Edit it as decisions land. Changing this doc is a council-level change (see `AGENTS.md` → "Editing rules for living docs").

## Vision
Lumi is an AI support and "AI employee" platform. It ships as two product lines that share the same core — a Firebase + Vue app, Gemini for answers, a knowledge base grounded in your own content, tool actions, and human handoff:

1. **Lumi ChatBot** — an embeddable AI support widget you add with one line of code. It answers from your own docs, takes action through your tools, files bug reports over MCP, and hands off to a human when it matters.
2. **Lumi Hireable Agents ("AI employees")** — hire AI agents that own real work. An agent takes input from any communication channel, uses MCPs to do the work, and delivers the result to a destination. Agents and people coordinate through a **Task Board**: either side can define a request as a task and assign it to an agent or a person for the next step. Agents can also work inside other collaboration environments the owner connects (Slack, ClickUp, Telegram, other task managers and messengers). Each agent run is isolated (its own runnable job/container).

Both lines are active. The ChatBot is the near-term wedge into European e-commerce; the Hireable Agents line opens the wider "AI employees" market.

## Target users
**Lumi ChatBot**
- **Buyers**: founders and support leads at small and mid-size online stores.
- **First markets**: Baltic, Nordic, and Central/Eastern European regions, where strong non-English support and GDPR-safe handling matter most.
- **End users**: the store's own shoppers, who want quick, correct answers about orders, returns, and shipping in their own language.

**Lumi Hireable Agents**
- **Buyers**: teams and owners who want to hire AI agents to run real work and hand it back and forth with their people. TODO: sharpen the first target job and buyer.

## Problems we solve
- Repetitive support tickets eat a small team's time. The ChatBot resolves the common ones on its own.
- Existing support tools answer weakly in non-English languages and lean on shallow FAQ replies.
- Teams want AI that does whole jobs and hands work back and forth with people — not another tool someone has to babysit. Lumi's agents run the work and coordinate with people through a shared Task Board.
- EU teams need AI that is GDPR-safe by design, not bolted on.

## Core features
**Lumi ChatBot**
- **Embeddable widget** — one line of code drops the chat agent into any site.
- **Gemini answers from your own docs** — retrieval over your knowledge base, so answers stay grounded.
- **Takes action through your tools** — look up an order, start a return, check shipping through connected shop, payment, and shipping systems.
- **MCP bug reports** — the agent can file bug reports through MCP when a shopper hits a real problem.
- **Human handoff** — a live agent inbox with Online/Away status; when everyone is Away, new handoffs fall back to an async email ticket.
- **Agent push notifications** — support staff get notified of new handoffs.

**Lumi Hireable Agents**
- **Agents** — an agent takes input from any channel, uses MCPs to do the task, and delivers the result to a destination. What it can do depends on the tools and traits it is given.
- **Task Board** — the default place agents and people work together. Either side creates a task and assigns it to an agent or a person for the next step.
- **Collaboration environments** — beyond the Task Board, agents can work in owner-connected channels: Slack, ClickUp, Telegram, and other task managers and messengers.
- **Isolated runs** — each agent run is isolated in its own runnable job/container.
- **Queued execution** — agent runs go through a queue and run within the plan's time and token window (see `../marketing/brand.md` → Pricing).

## Out of scope (for now)
- Voice support.
- Deep, enterprise-grade platform features aimed at large support orgs.
- TODO: confirm what is explicitly out of scope for the Hireable Agent line.

## Success metrics
See `../metrics/framework.md`. For the ChatBot the headline number is **resolution rate** — the share of conversations the agent closes without a human. For Hireable Agents it is **tasks completed** (with agent-run throughput and top-up rate as supporting numbers). Both are still to be instrumented (TODO).
