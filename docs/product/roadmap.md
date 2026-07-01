# Roadmap — Lumi

> Living doc. The current plan of what ships next and why. Changing this doc is a council-level change (see `AGENTS.md` → "Editing rules for living docs"). Use **Phase 1 / Phase 2 / Phase 3** naming, not V1 / V2 / V3.

> TODO: this roadmap is a first draft from setup. Confirm the real phase plan and sequencing across the two product lines, then link each item to the PR/FAQ or council file that approved it.

Lumi runs two product tracks. They share a core (Firebase, Vue, Gemini, knowledge base), so work on one often helps the other.

## Track A — Lumi ChatBot (support widget)

### Now (in progress)
- Core agent: Gemini answers from your own knowledge base (grounded retrieval), embeddable widget, MCP bug reports, human handoff with Online/Away and email fallback.

### Next
- Deeper tool actions for e-commerce: order lookup, returns, shipping status through connected shop/payment/shipping systems.
- Multilingual quality pass for Baltic, Nordic, and CEE languages.

### Later
- Broader set of shop-platform connectors beyond the first ones.
- Analytics for store owners (what customers ask, what the agent resolves, where it hands off).

## Track B — Lumi Hireable Agents (AI employees)

### Now (in progress)
- Core agent that takes input from a channel, uses MCPs to do work, and delivers a result.
- **Task Board** — the default place agents and people work together by assigning tasks to each other.
- Isolated, queued runs within a time/token window. TODO: confirm the first job and buyer.

### Next
- More **collaboration environments**: connect Slack, ClickUp, Telegram, and other task managers/messengers.
- Subscription + top-up billing for the time/token window.

### Later
- A library of agent traits/tools so owners can shape what an agent can do.
- TODO: expand as the design firms up.

## Shipped
_Nothing logged yet._
