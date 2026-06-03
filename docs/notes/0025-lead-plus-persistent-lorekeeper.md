---
tags:
  - kind/pattern
  - source/solorpg
  - theme/agent-architecture
  - theme/workflow
  - theme/context-economy
  - maturity/obsolete
  - verdict/unevaluated
created: 2026-06-03
---

# Lead + persistent Lorekeeper — separate the source-holder from the orchestrator

> **⚠️ OBSOLETE (per user).** This whole multi-agent split existed *only* to fit session
> data into a **165k** context window. Once the window grew to **1M**, fitting all the
> session data in a single context became trivial, and **the v2 team split was obsoleted**.
> (The single-agent **session-postprocess (v1)** skill remains the constantly-used workhorse —
> it was *this multi-agent topology*, not postprocessing itself, that died.) Kept as a case
> study, not a recommendation — it's the worked example behind
> [[0031-beware-transient-constraint-architecture]]. The *residual* question (does the
> source-holder ⟂ orchestrator role-split have value *independent* of the context limit?) is
> the only live part — see Open threads.

**What it is.** The v2 postprocess workflow splits roles across two agents: a **Lorekeeper**
that reads *all* raw session chunks into context and **stays alive**, and a **Lead** that
handles user interaction, validation, filesystem checks, and git. The Lead never works from a
lossy extraction report — it **asks the Lorekeeper**, which answers from the raw source at
full fidelity, and drafts content (summaries, memories, savefiles) directly from it. The
Lorekeeper **persists after postprocess** so session-prep can reuse the loaded context.

**Where it comes from.** `solorpg` `.claude/skills/session-postprocess-v2`. Explicitly
contrasts v1 (single subagent reads, returns a report, dies → Lead works from a lossy
summary) — the v2 table calls out "full fidelity" as the win.

**Why it matters for next-gen.** A clean **agent-architecture pattern**: keep the
expensive-to-load raw context in a *living* specialist, and let a thin orchestrator query it,
rather than collapsing source → report → work (which loses fidelity at the first hop). The
"don't pre-summarize what you'll need to ask follow-ups about" principle is general. Pairs
with the `gm-skill` Lead/tools split ([[0018-layered-skill-architecture]]) and the
reader/drafter division of labor. Persistence-for-reuse is a context-economy win
([[0009-jit-context-and-eviction]]: load once, serve many).

**Open threads (the only live ones).** Strip away the context-fitting motive: does the
**source-holder ⟂ orchestrator** separation still earn its keep — for *parallelism*, for a
*clean role/permission boundary*, or for *persistence-for-reuse* across prep — even when all
the data fits in one window? Or is single-context now strictly simpler and better? That's the
verdict-time question. (The Early/Late sharding and routing concerns are dead with 1M.)
