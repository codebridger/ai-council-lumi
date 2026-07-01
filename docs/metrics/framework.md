# Metrics Framework — Lumi

> Living doc. The few numbers we watch and what they mean. The council and PR/FAQs cite this doc when they set success and kill thresholds.

> TODO: most metrics below are not yet instrumented. Confirm the real definitions and wire them up.

## North-star metric
**ChatBot: resolution rate** — the share of customer conversations the agent closes on its own, without a human. It best tracks the real value: fewer repetitive tickets for the store.

**Hireable Agents: tasks completed** — the number of tasks agents finish and deliver. TODO: confirm the right north star for this line as it takes shape.

## Key metrics
**ChatBot**
- **Resolution rate** — conversations closed by the agent without a human. Current value: uninstrumented.
- **Time-to-first-value** — how fast a new store goes from sign-up to a live, answering agent. Current value: uninstrumented.
- **Support hours saved per store** — a value proxy the store owner feels directly. Current value: uninstrumented.

**Hireable Agents**
- **Tasks completed** — tasks agents finish and deliver. Current value: uninstrumented.
- **Agent runs and queue throughput** — how much work clears the queue inside the time/token window. Current value: uninstrumented.
- **Top-up rate** — how often owners top up when they hit the limit (a demand + monetization signal). Current value: uninstrumented.

**Both lines**
- **Free-to-paid conversion** — share of accounts that start paying. Current value: uninstrumented.
- **Retention / churn** — accounts that keep using Lumi month over month. Current value: uninstrumented.

## How we instrument
TODO: confirm. Likely from app events plus Firestore data, surfaced in a product analytics tool. Name an owner for the metrics.

## Guardrails
Metrics that must not get worse while we chase the north stars:
- **Answer accuracy** — a high resolution rate is worthless if answers are wrong. Watch wrong-answer / escalation-after-answer rates.
- **Wrong tool / agent actions** — refunds, returns, or agent actions taken in error must stay near zero.
- **Queue wait time** — agent work should not sit too long in the queue before it runs.
- **Cost per conversation / per agent run** — serverless, container, and LLM spend must stay sane.
