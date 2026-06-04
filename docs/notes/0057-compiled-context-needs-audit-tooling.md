---
tags:
  - kind/idea
  - source/new
  - theme/composition
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-04
---

# Compiled context needs audit tooling — dynamism's price is debuggability

**What it is.** (User, naming the big downside of [[0056-files-as-build-products]]:)
dynamically built files are **much harder to debug** than authored ones — when the playable
context is assembled from tagged sources, "what did the session actually see, and why?"
stops being answerable by reading a file. Likely answer: **(GUI) tools for review and
auditing the data** — inspect a build, trace an entry back to its source, see what a
tag-selection pulled in and what it excluded.

**Where it comes from.** User, morning workshop bounce (2026-06-04) — raised unprompted as
the cost side of the files-as-build-products idea.

**Why it matters for next-gen.** Every step toward compilation
([[0044-scenario-compiler]] → [[0056-files-as-build-products]]) trades inspectability for
power; the gates ([[0028-checkpointed-human-gates]], [[0052-evolution-vs-drift]]) only work
if a human can *see* what they're gating. Audit tooling is the gate infrastructure for a
compiled world. Note the existence proof already in hand: **reverse-mcp-rpg** — Claude
driving a live web dashboard — is exactly the delivery shape a build inspector could take.

**Open threads.** Minimum viable version is probably not GUI: a build *manifest* (what was
included, from where, selected by which tags) emitted with every artifact — diffable
([[0051-live-context-delta]]), greppable, and the data a GUI would later render. Does
audit-tooling itself become a module ([[0036-every-subsystem-is-a-module]])?

**Verdict.** _(unevaluated.)_
