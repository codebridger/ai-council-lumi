# Brand & Positioning — Lumi

> Living doc. How we talk about the product and how we price it. Changing this doc is a council-level change (see `AGENTS.md` → "Editing rules for living docs").

## One-line pitch
Lumi gives your product an AI support agent that answers from your own docs, takes action through your tools, and hands off to a human when it matters — embedded with one line of code. It also lets you hire AI agents that run a whole job on their own.

Lumi has two product lines:
- **Lumi ChatBot** — an embeddable AI support widget (Gemini answers, your knowledge base, MCP bug reports, human handoff).
- **Lumi Hireable Agents** — "AI employees" you hire that run as isolated, runnable jobs in their own container.

## Positioning
**Lumi ChatBot.** For small and mid-size online stores — first in Baltic, Nordic, and Central/Eastern European markets — the ChatBot replaces slow, repetitive manual support and shallow FAQ bots. Unlike Gorgias (Shopify-native, weak in CEE languages) and Tidio (SMB-friendly but surface-level FAQ replies), it answers well in non-English languages, takes real action through connected tools instead of just replying, and is GDPR/EU-first by design.

**Lumi Hireable Agents.** For teams that want an AI that owns a whole job — a coworker, not a chatbot. It competes in the "AI employees" space (players like Viktor, Superpal, nexos.ai, Wonderful) on being simple, fast, and easy to hire, with EU-first data handling. TODO: sharpen this positioning once the design doc and first job are set.

## Voice & tone
Plain, clear, and helpful. Sound like a calm expert, not a hype machine.
- **Do**: use short sentences and common words; be concrete about what the agent does; respect the reader's time.
- **Don't**: over-promise, lean on buzzwords, or bury the point in jargon.

## Pricing
Keep this the single source of truth for price.

**Lumi Hireable Agents** — a usage-based subscription, shaped like Anthropic's and OpenAI's plans:
- You subscribe to a plan and can define as many agents as you want.
- Each plan gives a limited **time and token window** per period. Agent activity goes through a **queue** and runs one by one inside that window.
- When agents hit the limit, owners can **top up** to boost throughput and keep work moving.
- Exact plan tiers, prices, and window sizes: TODO.

**Lumi ChatBot** — pricing not set yet (TODO). It may reuse the same subscription + top-up shape or use a support-style model. Competitor models to weigh: subscription (Gorgias), per-conversation (Tidio, Decagon), per-resolution (Sierra). Small shops respond to simple pricing at small-shop scale.

## Key messages
1. **Resolves, not just replies** — Lumi takes action through your tools, it doesn't just answer FAQs.
2. **Grounded in your own docs** — answers come from your content, so they stay accurate.
3. **Speaks your customers' language** — strong support beyond English, built for European stores.
4. **GDPR-safe by design** — EU-first data handling from the start.
