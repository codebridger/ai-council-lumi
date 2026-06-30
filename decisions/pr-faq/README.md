# PR/FAQs

Press-release-style feature pitches. Each PR/FAQ answers the question: *"Should we build this?"*

## How this directory works

- One file per feature pitch. Numbered sequentially: `001-<slug>.md`, `002-<slug>.md`, etc.
- Use the template in `templates/pr-faq-template.md`. Don't skip sections — empty sections are signal.
- A PR/FAQ is not "approved" until it has a Critic Pass and a Decision filled in. See `AGENTS.md` → Workflow 2 for the process.
- PR/FAQs are committed to git. They are part of the product memory, not ephemeral. Keep rejected ones — knowing what you said no to is as valuable as knowing what you said yes to.

## Lifecycle

```
Draft  →  Critic Pass  →  Decide
                            ├─→ Approved
                            ├─→ Rejected
                            └─→ Pending Council  →  Council Workflow  →  Approved / Rejected
```

If the Critic Pass surfaces real cross-functional trade-offs (pricing, positioning, infra cost, go-to-market), escalate to the council rather than deciding solo. The PR/FAQ becomes input context for the council session.

## Status field convention

Set the `Status` field in each doc to one of:

- `Draft` — being written
- `Pending Council` — escalated, council session in progress
- `Approved` — green-lit for the roadmap
- `Rejected` — passed on, with reasoning preserved for future reference
- `Shipped` — the feature is live; PR/FAQ now serves as historical context

## Index

<!-- New PR/FAQs are appended here as they're created. -->

_None yet._
