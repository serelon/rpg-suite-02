---
tags:
  - kind/pattern
  - source/new
  - source/claude-desktop
  - theme/context-economy
  - theme/skill-authoring
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Recap as verification, not "previously on…"

**What it is.** Reframe the session-opening recap from a courtesy retelling (for the player)
into a **verification step**: state current understanding back *compactly* to confirm it
survived the memory/context pipeline (compaction, summarization) intact, then flag anything
thin, missing, or contradictory. Source of truth is the freshly-packed **briefing**, checked
against what survived in context, checked against the player's sense. Crucially, **the gaps
the recap surfaces are the primary input to tuning** — recap is the diagnostic that *aims*
the calibration, not a separate step.

**Where it comes from.** [[gm-skill-SKILL]] §"Recap as verification";
[[gm-skill-RATIONALE]] §"Recap as verification" (called the key reframe of prep).

**Why it matters for next-gen.** Context drift across compaction is a *named, recurring*
risk the user has actually hit — and this is a cheap, general mitigation: a deliberate
**state-reconstruction-and-confirm checkpoint** at resume time. Applies to any long-running,
compaction-exposed session, not just GMing. Strongly ties the `theme/context-economy` thread
to a concrete ritual; complements [[0011-identity-pinned-state-evicted]] (what *should* have
survived) and [[0009-jit-context-and-eviction]] (why things vanish).

**Open threads.** Can verification be partly automated (diff briefing vs. in-context state)
rather than relying on the model to notice its own gaps? What's the durable "source of truth"
the recap checks against in the next-gen design — the briefing, a state file, both?
