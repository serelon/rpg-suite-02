---
tags:
  - kind/idea
  - source/conversation
  - theme/architecture
  - theme/composition
  - maturity/speculative
  - verdict/unevaluated
created: 2026-06-06
---

# Live hook pipeline — event-driven agents around the writer

**What it is.** Extends [[0081-writer-planner-split]] (user, 2026-06-06): besides the
planner, **post-processing hooks during live play** — agents that run *after the writer*
each turn/beat: live data extraction, widget updating, etc. Orchestrated by a
**rules-based modular pipeline**: "run agent x at stage a whenever y has happened."

**The named risk and its counter-rule:** "there's of course a risk that we go over the top
with agents tho... but, optimize for tiny cheap ones for the often-run things, and to keep
the main agents free to focus on the story, not extra details."

**Why it matters for next-gen.** This is the missing *mechanism* for several adopted
threads:
- It's how **streamed librarianship** ([[0075-postprocessing-as-vault-librarian]]) would
  actually run — extraction hooks firing on events instead of one batch pass. The
  scene-boundary problem softens too: hooks can fire on *whatever* trigger ("y has
  happened"), not only scene breaks.
- It's [[0064-unharvested-archive]]'s tier-by-judgment again: often-run hooks = tiny cheap
  models; rare/heavy judgment = frontier. And [[0066-mandatory-presence-not-length]]'s
  attention economics: every detail-job moved to a hook is attention the writer keeps for
  prose.
- The rules-based trigger structure is [[0024-pluggable-extension-modules]] /
  [[0036-every-subsystem-a-module]] as an *event bus*: hooks are modules, triggers are
  declarative config.
- "Widget updating" implies Unicorn's UI has live state panes fed by hooks, not by the
  writer — the writer never does bookkeeping.

**Open threads.** What's the trigger vocabulary ("y has happened") — turn-complete,
entity-mentioned, state-changed, scene-break, explicit player beat? Hook failure handling:
a missed extraction is recoverable (batch sweep later, [[0075]]'s fallback), so hooks can
be best-effort — does that mean they *never* block the writer? Where does over-the-top
begin — is there a budget (hooks per turn / tokens per session) that keeps the pipeline
honest? Do hook outputs go through the same human gate as librarian mutations, or are
widget-level updates exempt (display vs canon)?

**Verdict.** _(unevaluated.)_
