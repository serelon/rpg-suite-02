---
tags:
  - kind/pattern
  - source/aegis-tools
  - theme/rules-engine
  - theme/architecture
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Event-bus orchestrator — a thin core, self-registering modules, time as events

**What it is.** The strategic layer's orchestrator is **"thin glue" with no game logic**:
advancing time walks day-by-day and **emits events** (`DAY_ADVANCED`, `WEEK_ENDED`,
`MONTH_ENDED`) onto a bus; subscribed modules (research, medical, manufacturing, recruitment…)
each handle the events they care about and return messages to display. Modules **self-register
by import side-effect** (`strategic/__init__.py` imports each submodule, whose import
subscribes its handlers). The core knows nothing about any specific module.

**Where it comes from.** `aegis-tools` — `modules/strategic/orchestrator.py` (real code) +
`lib/events.py` (`EventBus.subscribe/emit`), `modules/strategic/__init__.py`.

**Why it matters for next-gen.** A concrete **decoupling/extensibility mechanism** — exactly
the plug-in seam [[0018-layered-skill-architecture]] gestures at. New mechanics attach by
subscribing, not by editing the core; this is how a mechanics-module *binds* without the
craft layer knowing it exists. "Time as a stream of events that modules react to" is also a
clean model for advancing a living world between scenes (cf. `gm-skill`'s "advance background
plots"). Pub/sub keeps the core frontend-agnostic ([[0004-frontend-agnostic-core]]): emit
events, let any surface render the collected messages.

**Open threads.** Events here are *temporal* (day/week/month) — do narrative beats want the
same bus (cf. [[0009-jit-context-and-eviction]]: beats as boundaries)? Ordering/dependencies
between module handlers? Import-side-effect registration is implicit/magic — explicit
registry vs. convenience trade-off.
