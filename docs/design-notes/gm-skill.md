---
tags:
  - kind/design-note
  - source/new
  - source/claude-desktop
  - theme/skill-authoring
  - theme/gm-craft
  - theme/context-economy
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
origin: inbox/gm-skill.zip
preserves:
  - "[[gm-skill-SKILL]]"
  - "[[gm-skill-RATIONALE]]"
atomized-into:
  - "[[0013-counter-training-name-the-default]]"
  - "[[0014-scope-stripping]]"
  - "[[0015-compounding-loops]]"
  - "[[0016-thinking-as-enforcement]]"
  - "[[0017-recap-as-verification]]"
  - "[[0018-layered-skill-architecture]]"
  - "[[0019-companion-rationale-as-anti-regression]]"
---

# GM Skill (Claude Desktop) — wrapper / index

> **Preserved artifact + its companion why-doc.** This wrapper carries vault metadata; the
> two source files are kept **verbatim, untouched**:
> - [[gm-skill-SKILL]] — the shipped Claude Desktop skill (the artifact).
> - [[gm-skill-RATIONALE]] — the companion design-rationale ("read before revising").

**What it is.** The user's current, working Claude Desktop GM skill: a personalized
solo-RPG game-mastering harness encoding a house style that *deliberately diverges* from
default GMing norms. It loads `rpg-tools` for mechanics and governs *craft and conducting*
(how to run a session). Status per the user: **"works fairly well."** → `maturity/proven`.

**Why it matters for next-gen.** Two layers of value:
1. **Meta / framework-level** — the skill is a case study in *authoring robust, counter-default
   behavior* under context pressure. Those techniques (counter-training, named failure-mode
   families, the thinking-block enforcement layer, layered skill/module/tool architecture)
   generalize far beyond GMing and are atomized below.
2. **GM-craft corpus** — the session-running detail (channels, transform, camera, pacing,
   authority split, scene headers, debrief ethics) is itself a reusable asset for the next-gen
   GM layer. *Not yet atomized* — it lives in the preserved [[gm-skill-SKILL]] and can be
   mined in a later craft-focused pass if a theme calls for it.

**Note on the companion doc.** RATIONALE.md is the concrete proof of the
*companion-why-doc-as-anti-regression* idea the user flagged — see
[[0019-companion-rationale-as-anti-regression]].

**Open threads.** Craft layer un-atomized (deliberate, batch discipline). Authority-split
(world vs. will), stop-on-a-live-wire (links to [[0009-jit-context-and-eviction]] — beats as
natural units), and scene-headers-as-anti-drift are strong candidates for the next pass.
