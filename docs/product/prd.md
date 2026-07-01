# Product Requirements — Lumi

> Living doc. This is the current state of the product, not a decision record. Edit it as decisions land. Changing this doc is a council-level change (see `AGENTS.md` → "Editing rules for living docs").

## Vision
Lumi gives any product an AI support agent that actually resolves customer questions. It answers from the company's own docs, takes action through connected tools, and hands off to a human when it matters — all embedded with one line of code. The first market focus is European online stores that are underserved by English- and Shopify-first support tools.

## Target users
- **Buyers**: founders and support leads at small and mid-size online stores.
- **First markets**: Baltic, Nordic, and Central/Eastern European regions, where strong non-English support and GDPR-safe handling matter most.
- **End users**: the store's own shoppers, who want quick, correct answers about orders, returns, and shipping in their own language.

## Problems we solve
- Repetitive support tickets eat a small team's time. Lumi resolves the common ones on its own.
- Existing tools answer weakly in non-English languages and lean on shallow FAQ replies.
- Store owners in the EU need support that is GDPR-safe by design, not bolted on.

## Core features
- **Embeddable widget** — one line of code drops the chat agent into any site.
- **Answers from your own docs** — retrieval over the store's docs and help content, so answers stay grounded.
- **Takes action through your tools** — the agent looks up an order, starts a return, or checks shipping through connected shop, payment, and shipping systems.
- **Human handoff** — a live agent inbox with Online/Away status; when everyone is Away, new handoffs fall back to an async email ticket.
- **Agent push notifications** — support staff get notified of new handoffs.

## Out of scope (for now)
- The horizontal "AI coworker" market (general internal task automation) — that fight is against far better-funded players. Lumi stays focused on e-commerce support.
- Voice support.
- Deep, enterprise-grade platform features aimed at large support orgs.

## Success metrics
See `../metrics/framework.md`. The headline number is **resolution rate** — the share of conversations the agent closes without a human.
