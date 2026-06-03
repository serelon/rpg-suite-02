---
tags:
  - kind/idea
  - source/new
  - source/cross
  - theme/frontend-agnostic
  - theme/portability
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-03
---

# Front-end agnostic core — play anywhere, one brain underneath

**What it is.** Aim for a **core** (rules, data, memory, workflows) that is independent of
any particular frontend, and can be factored into *any* of them over time. The primary
target is **Claude Desktop**, but the same core should let you play in **Claude Code**, the
**reverse-mcp client** ([[relevant-paths]] → reverse-mcp-rpg), or something like
**SillyTavern** — without forking the core per surface.

**Where it comes from.** User aspiration (poking at SillyTavern again — "completely
different suite," currently isolated — and asking: *what if it wasn't?*). Not from any one
repo, but it **rhymes with patterns already mined**: read-anywhere/write-canonical data
access ([[0002-read-anywhere-write-canonical]]) and the portable `.skill` bundle both exist
precisely to decouple tools from where they run.

**Why it matters for next-gen.** This is a potential **north-star constraint**, not just a
feature. If true, it reorders everything: the seven source "systems" become *frontends and
fragments over a shared core*, and the real design work is defining that core's boundary —
what's portable (rules/data/memory/workflow) vs. what's frontend-specific (UI, transport,
session framing). It turns "which system wins?" into "what's the core, and how does each
frontend bind to it?"

**Open threads.**
- What's the binding layer? MCP is the obvious candidate (reverse-mcp-rpg proves a live one
  works; `.skill` is the Claude Desktop one; `E:\rpg` used MCP servers too). Is MCP *the*
  seam, or one of several?
- SillyTavern is a different paradigm (character-card / chat-completion frontend). Does
  agnosticism really stretch that far, or is there a frontend class the core can't serve?
- Tension with everything-is-files and with reverse-mcp-rpg's live-UI axis — see the
  pending "is everything-is-files a principle or inertia?" question.
- Likely graduates into a `theme/frontend-agnostic` synthesis doc, then a `kind/decision`.
