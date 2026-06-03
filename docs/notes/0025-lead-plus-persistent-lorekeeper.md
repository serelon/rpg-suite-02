---
tags:
  - kind/pattern
  - source/solorpg
  - theme/agent-architecture
  - theme/workflow
  - theme/context-economy
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Lead + persistent Lorekeeper — separate the source-holder from the orchestrator

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

**Open threads.** Long sessions exceed one Lorekeeper's context → it splits into Early/Late
Lorekeepers (sharding the source). Who owns the routing? Cost of keeping agents alive vs.
reload. Does this generalize to play (a live Lorekeeper during a session, not just
postprocess)?
