# Product Requirements — Lumi

> Living doc. This is the current state of the product, not a decision record. Edit it as decisions land. Changing this doc is a council-level change (see `AGENTS.md` → "Editing rules for living docs").

## Vision
Lumi is an AI support and "AI employee" platform. It ships as two product lines that share the same core — a Firebase + Vue app, Gemini for answers, a knowledge base grounded in your own content, tool actions, and human handoff:

1. **Lumi ChatBot** — an embeddable AI support widget you add with one line of code. It answers from your own docs, takes action through your tools, files bug reports over MCP, and hands off to a human when it matters.
2. **Lumi Hireable Agents ("AI employees")** — an AI agent you "hire" that runs as an isolated, runnable job in its own container. This is the horizontal-coworker direction: an agent that does a defined job on its own, not just a chat widget on a page.

Both lines are active. The ChatBot is the near-term wedge into European e-commerce; the Hireable Agent opens the wider "AI employees" market.

## Target users
**Lumi ChatBot**
- **Buyers**: founders and support leads at small and mid-size online stores.
- **First markets**: Baltic, Nordic, and Central/Eastern European regions, where strong non-English support and GDPR-safe handling matter most.
- **End users**: the store's own shoppers, who want quick, correct answers about orders, returns, and shipping in their own language.

**Lumi Hireable Agents**
- **Buyers**: teams that want to "hire" an AI agent to own a repeatable job (a coworker, not a chatbot). TODO: sharpen the first target job and buyer from the internal design doc.

## Problems we solve
- Repetitive support tickets eat a small team's time. The ChatBot resolves the common ones on its own.
- Existing support tools answer weakly in non-English languages and lean on shallow FAQ replies.
- Teams want AI that does a whole job on its own, not another tool a person has to babysit — the Hireable Agent runs the job as an isolated container.
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
- **Hire an agent** — pick an agent to own a defined job.
- **Runs as an isolated job/container** — each hired agent runs in its own isolated, runnable container. TODO: fill in the full feature set from the internal design doc.

## Out of scope (for now)
- Voice support.
- Deep, enterprise-grade platform features aimed at large support orgs.
- TODO: confirm what is explicitly out of scope for the Hireable Agent line.

## Success metrics
See `../metrics/framework.md`. For the ChatBot the headline number is **resolution rate** — the share of conversations the agent closes without a human. Hireable Agent metrics are still to be defined (TODO).
