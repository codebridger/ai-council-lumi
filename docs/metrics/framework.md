# Metrics Framework — Lumi

> Living doc. The few numbers we watch and what they mean. The council and PR/FAQs cite this doc when they set success and kill thresholds.

> TODO: most metrics below are not yet instrumented. Confirm the real definitions and wire them up.

## North-star metric
**Resolution rate** — the share of customer conversations the agent closes on its own, without a human. It best tracks the real value: fewer repetitive tickets for the store.

## Key metrics
- **Resolution rate** — conversations closed by the agent without a human. Current value: uninstrumented.
- **Time-to-first-value** — how fast a new store goes from sign-up to a live, answering agent. Current value: uninstrumented.
- **Free-to-paid conversion** — share of stores that start paying. Current value: uninstrumented.
- **Retention / churn** — stores that keep using Lumi month over month. Current value: uninstrumented.
- **Support hours saved per store** — a value proxy the store owner feels directly. Current value: uninstrumented.

## How we instrument
TODO: confirm. Likely from app events plus Firestore data, surfaced in a product analytics tool. Name an owner for the metrics.

## Guardrails
Metrics that must not get worse while we chase resolution rate:
- **Answer accuracy** — a high resolution rate is worthless if answers are wrong. Watch wrong-answer / escalation-after-answer rates.
- **Wrong tool actions** — refunds or returns taken in error must stay near zero.
- **Cost per conversation** — serverless and LLM spend must stay sane at small-shop scale.
