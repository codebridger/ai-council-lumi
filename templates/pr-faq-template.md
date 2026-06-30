# PR/FAQ — {Feature Name}

**Status**: Draft | Pending Council | Approved | Rejected | Shipped
**Author**: {name}
**Date**: {YYYY-MM-DD}
**Number**: PRFAQ-{NNN}
**Sequences after**: {PRFAQ-NNN or "none"} — features this one depends on shipping first

---

## Press Release

> Write this as if the feature has shipped. Past tense. Clear, specific, customer-facing. If you cannot write a compelling press release, you do not have a feature — you have an idea.

### Headline
{One or two sentences. The benefit, the target user, and the moment of use — not the feature.}

### Summary paragraph
{Two to four sentences. What did we ship, who is it for, what can they now do that they couldn't before, why does it matter?}

### The problem
{One paragraph describing the user pain in concrete terms. Use the user's own words where possible.}

### The solution
{One paragraph describing how the feature solves the problem. Focus on the experience, not the implementation. Cover the first-run moment in one or two sentences — where the user clicks, what they see, when they feel the value. Name what ships in Phase 1 vs. what's deferred to later phases.}

### Customer quote (optional)
> {Only include if you have a real quote from a real user with a date and a source. If using an aspirational/composite quote, mark it clearly as aspirational and replace with a real one before Phase 1 ships.}

---

## Engineering touchpoints

> Map each concrete piece of engineering work to the repo / area it touches. An engineer reading this should be able to tell in 10 seconds which parts of the system they need to open. Replace the column headers below with your real repos or areas (e.g. Frontend / Backend / Mobile). Keep rows at the level of one ownable piece of work, not one file. Mark "✓" where the piece touches that area; add a short note in parentheses if it helps (e.g. *✓ (caller)*).
>
> If the PR/FAQ introduces new UI / visual design, add one **Design**-scoped row whose deliverable is the design spec (mockups + interaction notes) for every UI surface the PR/FAQ introduces. Engineering rows that build that UI block on it.

| Piece | Area A | Area B | Area C |
|---|:---:|:---:|:---:|
| {short description of the engineering piece} | | | |
| ... | | | |

---

## Internal FAQ

> Anticipate hard internal questions. Answer with specifics, not hand-waves. If an answer reads as "we'll figure it out", that's a flag.

**Q: Who is this for, specifically?**
A:

**Q: How do we know this is a real problem and not a hypothesis?**
A: {Cite metrics, support tickets, interviews, or competitor signal. If you can't cite anything, that itself is the answer.}

**Q: What does success look like, and what would make us kill it?**
A: {Concrete 30-day and 90-day numbers tied to `docs/metrics/framework.md`, paired with the kill thresholds (the inverse of success). If a baseline is uninstrumented today, say so — and define when the baseline lands rather than picking a lift target against a missing number.}

**Q: Cost & resource exposure — be specific.**
A: {Name every line that costs money or compute (e.g. AI inference, third-party API calls, new infra), how often it runs, and which costs scale with free users vs. paying users. If the feature has no notable cost, say so.}

**Q: What does this trade off against on the roadmap?**
A: {What attention/sequencing does this displace? Which PR/FAQs sequence before or after?}

---

## External FAQ

> Only the questions that have a non-obvious answer specific to this feature. Skip the boilerplate (is it free? what platforms?) unless the answer is unusual.

**Q: What is this and how does it work?**
A:

**Q: How is this different from {nearest alternative or competitor}?**
A:

---

## Critic Pass

> Filled in by a critic subagent after the draft is complete. See `AGENTS.md` → Workflow 2.

{strongest objections, weakest claims, hand-wavy answers}

---

## Open Issues

> Things that still need work before this PR/FAQ can move from Draft to Approved. A stable section, not a changelog — fold items in or close them as they're resolved.

-
