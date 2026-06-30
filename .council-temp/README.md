# Council Workspace (Temporary)

This directory holds session-specific scratch files for AI council deliberations. It is **gitignored** — nothing here is permanent.

## Session structure

Each council session gets its own subdirectory. It holds one file per lens that ran, plus the synthesis:

```
session_YYYY-MM-DD_HH-MM-SS/
├── product-manager.md
├── ux-designer.md
├── technical-architect.md
├── business-strategist.md
└── synthesis.md
```

(Only the lenses that actually ran get a file. A two-lens session has two perspective files plus the synthesis.)

## Workflow

1. **Main agent** creates the session directory with the current timestamp.
2. **Main agent** spawns the chosen lenses, each pointing to its own file. They reason independently and never read each other's files.
3. Each lens writes its perspective to its file.
4. **Main agent** reads the perspective files and writes the verdict to `synthesis.md`.
5. The synthesis is promoted to `decisions/council/<NNN>-<slug>.md`. The session files are then discarded.

See `AGENTS.md` → Workflow 1 for the full procedure.

## Perspective file format

Each lens file follows this structure:

```markdown
# {Role} Perspective

**Request**: {topic}
**Time**: {UTC timestamp}

## Analysis
{reasoning from this lens}

## Recommendation
{concrete recommendation}

## Pre-mortem
{if this fails in 6 months, what is the most likely cause?}

## Questions/Concerns
{open questions, risks}

## Confidence
{1–10, and why — one sentence}
```

## Synthesis format

The synthesis is a **verdict doc, not a transcript**. Write it as if the per-agent files don't exist — because for the future reader, they don't. Target ≤300 words for the body (canonical tables / copy that downstream living docs will reuse are exempt).

```markdown
# Council: {short topic title}

**Date**: YYYY-MM-DD
**Lenses**: {comma-separated list of lenses that ran}
**Status**: Decided

## Decision
{1–3 sentence verdict. What we are doing.}

## Sequence
{Numbered actions in order. Omit this section if the decision is atomic.}

## Why
{2–4 sentences. Core reasoning. Not a re-telling of each lens.}

## Open Issues
{Optional. Only when something real is unresolved. Omit the section otherwise.}

## Action Items
- [ ] {concrete doc edit or build task}
```

**Rules**

- Omit any section that has no substance. "No contention" → drop the section. No open issues → drop the section. No sequence → drop the section.
- One line for lenses. Do not justify skipped lenses inside the permanent file — that belongs in the commit body.
- No process-citations inside the synthesis (e.g. `(deduplicated)`, `(no revision markers)`). The rules live in `AGENTS.md`; don't re-cite them here.
- Canonical tables and copy (pricing tables, plan-comparison tables, copy blocks that downstream living docs will reuse) are a legitimate exception to the word target — they are the source of truth, not deliberation residue.

---

**Note**: This directory is NOT committed to git. Session files are ephemeral and can be deleted after decisions are finalized.
