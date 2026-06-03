---
tags:
  - kind/idea
  - source/new
  - theme/context-economy
  - theme/composition
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-03
---

# Live context delta — patch a running session with a diff, never a reload

**What it is.** (User:) workshopping continues *while session 01 is already running* — the
bundle gets patched mid-session, sometimes with details that are literally in play at that
moment. The next-gen system must be able to hand the running session **just the delta** of
what changed in its context. "Reloading everything will be murder on the context window, so
just a diff."

**Scope boundary (important):** this is *intra-session* only. Between-session diffs are
already solved — bundle changes are tracked via git, including PRs that get reviewed
(see [[0035-surgical-git-staging]], [[0028-checkpointed-human-gates]]).

**Where it comes from.** User realization during a light workshop exchange (2026-06-03),
noticing their own habit of patching the bundle mid-session-01.

**Why it matters for next-gen.** If scenarios are compiled ([[0044-scenario-compiler]]),
the compiler can diff two builds and emit a delta as a first-class artifact — which makes
live patching cheap instead of context-murder. This also implies the live session is a
*subscriber* to its compiled context, not a one-shot consumer: a runtime channel, adjacent
to [[0045-runtime-composition-briefing-py]].

**Open threads.** Delta granularity — file, section, semantic? How does the running session
*receive* it (re-read a delta file? tool call? the runtime-composition path)? What happens
when the patch contradicts something already said in play — is that a canon event
([[0048-canon-precedence-and-naming-is-permission]])?

**Verdict.** _(unevaluated.)_
