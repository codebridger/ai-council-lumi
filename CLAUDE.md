# CLAUDE.md — Claude Code pointer

**Read `AGENTS.md` in full before doing anything in this repo.** It is the single source of truth for the decision-making workflows (triage → depth → output; the council, PR/FAQ, and ADR procedures; records and history; the writing style; and the anti-patterns). Claude Code does not auto-load `AGENTS.md` yet, so treat this line as a hard instruction: open and follow `AGENTS.md` at the start of every session.

**Hard rule — code repos are read-only.** You may read this product's code repos to audit or answer questions, but you must never edit, commit, merge, or push code. Code gaps become tasks in the tracker (preview with the owner first) or doc updates. See `AGENTS.md` → "Code repos are read-only for AI agents". (Delete this rule if your repo has no separate code repos.)

Everything below is **only** the Claude-Code-specific way to run what `AGENTS.md` describes. It adds no new rules.

---

## First run — set up the repo

If the repo still has `<...>` placeholders (e.g. `<PRODUCT_NAME>`), it is a fresh template and not yet set up. Run the setup routine in `SETUP.md` (**Workflow 0**) before any council / PR/FAQ / ADR work — tell the user you'll initialize it first. Setup is a main-thread interview + bulk edit; no subagents needed.

## Spawning personas in Claude Code

- The council personas live in `agents/*.md` (canonical source). Read the relevant persona file **verbatim** into the subagent prompt — never paraphrase.
- Spawn each lens with the **Task** tool, `subagent_type: "general-purpose"`.
- **Run a tier in parallel:** put several Task calls in a **single message** so the lenses reason at the same time and independently. Do not call them one after another.
- Follow the subagent prompt template in `AGENTS.md` → Workflow 1 → step 4. Always paste the grounding pack inline and include the writing-style block.
- The **main thread** (you) reads the per-agent files in `.council-temp/session_<id>/` and writes the synthesis. Never ask a subagent to synthesize or to read another subagent's file.
- For the PR/FAQ critic pass (Workflow 2) and the ADR architect review (Workflow 3), spawn ONE `general-purpose` subagent with the prompt given in those workflows.

## Tracking

- Use **TodoWrite** to track the steps of any multi-step workflow.

## Persona edits

`agents/*.md` is canonical. If you change a persona, also update its Gemini-native mirror in `.gemini/agents/<role>.md` so all tools stay in sync.

## Writing style

Plain everyday English — in chat replies, in docs, and in every subagent prompt. Full rules are in `AGENTS.md` → "Writing style — the house style".
