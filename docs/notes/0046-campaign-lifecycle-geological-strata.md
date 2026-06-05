---
tags:
  - kind/pattern
  - source/rpg-tools
  - source/solorpg
  - theme/architecture
  - theme/single-source-of-truth
  - maturity/proven
  - verdict/adopt
created: 2026-06-03
---

# Campaign-setup is geological strata — four lifecycle homes built in different eras

**What it is.** Campaign setup has no single home because it accreted across eras, not
because it was decomposed: *pre-play design* (`campaign-zero-guide.md`, rpg-tools — predates
the entire solorpg repo), *exploration* (workshop skill, solorpg), *formalization*
(campaign-setup skill's six-phase post-session-01 pipeline, solorpg), *ongoing state*
(`campaign.py`/`log.py` + campaign-state-guide, rpg-tools — which campaign-setup never even
mentions). Mining found **no copy-paste drift between them — they evolved independently from
shared intent**, which is worse than drift: there is no canonical source to drift *from*.

**Two corrections from the user (do not re-impose a pipeline):**
1. The path to session 01 is **asynchronous, not staged**. Seeds are heterogeneous — a
   setting, a character, a vibe, or most recently *refactoring a failed project from
   elsewhere*. "Stages" was an analyst's imposition on what is really opportunistic flow.
2. Workshop is now often the **entrypoint** ("just chat about a seed") — but it's freeform
   while everything downstream is linear. That seam is unresolved by design: "we need to
   figure that out in the future."

**Where it comes from.** Cross-repo mine of `solorpg/.claude/skills/{campaign-setup,workshop}/`
and `rpg-tools/references/{campaign-zero-guide,campaign-state-guide}.md` (2026-06-03).

**Why it matters for next-gen.** Direct fuel for [[0041-self-evolving-versioned-spec]]: the
spec must own the campaign lifecycle as *one concern*, while honoring that entry into it is
asynchronous and seed-heterogeneous — an intake funnel, not a pipeline. The
freeform-workshop → linear-workflow seam is a design problem to solve, not paper over.

**Open threads.** What does "one concern, many doors" look like concretely? Does workshop
stay a separate mode that *hands off*, or does the lifecycle module absorb a freeform mode?
Compare [[0026-exceptions-are-features]]. See [[0050-built-never-used-inventory]] for the
untested stratum.

**Verdict.** **Adopt** (appraised 2026-06-05). Lifecycle is one concern, many doors — and the
user's design call: **one entrypoint per platform** (Claude Code, Claude Desktop, future
frontends), each sharing the *same checkboxes, secondary skills, and end format*, all
importing cleanly into the database. The core lesson — imperative for next-gen — is that
those shared parts must be **one spec artifact the entrypoints reference**, never parallel
copies built from "shared intent": independent copies is exactly how the four strata formed.
Entrypoint flavors: workshop = "vague vibe" door; session-0-guide = "barest minimum to play"
door. Streamlining both into the shared spec is the design task.
