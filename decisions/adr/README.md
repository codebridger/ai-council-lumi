# Architecture Decision Records (ADRs)

Permanent records of *why* we made each significant technical or architectural choice.

## How this directory works

- One file per decision. Numbered sequentially: `001-<slug>.md`, `002-<slug>.md`, etc.
- Use the template in `templates/adr-template.md`. The "Alternatives Considered" section is the single most important part — without it, an ADR is just a memo.
- ADRs are committed to git and **never edited after acceptance**. To change a decision, write a new ADR with `Supersedes ADR-NNN` and update the old ADR's status to `Superseded by ADR-NNN`.
- ADRs are written by the Technical Architect (or whoever is making the call), then reviewed by the Technical Architect persona subagent. See `AGENTS.md` → Workflow 3.

## When to write an ADR

Write one when:

- A future engineer (including future-you, in 18 months) would benefit from understanding *why* a choice was made.
- There were multiple valid options and you picked one.
- The decision touches infrastructure, data, security, third-party integrations, or anything that's hard to reverse later.

Don't write one for:

- Routine implementation choices (which helper function, which file naming convention).
- Decisions already documented in `docs/tech/architecture.md` at a higher level.

## Status field convention

- `Proposed` — being drafted, not yet adopted
- `Accepted` — current truth; engineering should follow this
- `Rejected` — option was considered formally and turned down
- `Superseded by ADR-NNN` — replaced by a newer decision; kept for history

## Index

<!-- New ADRs are appended here as they're created. -->

_None yet._
