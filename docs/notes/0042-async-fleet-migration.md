---
tags:
  - kind/idea
  - source/new
  - theme/architecture
  - theme/self-evolution
  - theme/exceptions
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-03
---

# Async fleet migration — campaigns get up to spec independently, not in lockstep

**What it is.** The mechanism that makes self-evolution ([[0041-self-evolving-versioned-spec]])
practical: campaigns upgrade to the current canonical spec **asynchronously** — each on its own
schedule, **not** a forced lockstep migration of all 16+ campaigns on every spec bump. Each
campaign declares which **spec version** it's at; a defined *"refactor to this"* path brings
any campaign current when convenient (lazily, when it's next touched, or on demand).

**The crucial distinction it enables.** With a baseline spec, you can finally separate
**intentional** per-campaign variation (the campaign's [[0026-exceptions-are-features]]
*exception profile* — deltas it *means* to have) from **accidental** divergence (it simply
never got updated). Today there's no baseline, so *every* difference is ambiguous — you can't
tell a deliberate house-rule from stale convention. The spec is the shared floor; exceptions
are intentional deltas declared *on top* of it.

**Where it comes from.** User: "allow for campaigns to get up to spec asynchronically from each
other."

**Why it matters for next-gen.** Async migration is what keeps a self-evolving system from
collapsing under its own improvements — you must **never have to re-migrate the whole fleet on
every change** (a mass-rewrite requirement would itself be a
[[0031-beware-transient-constraint-architecture]]-class trap). It needs three things the vault
already points at: a versioned spec ([[0041]]), per-campaign spec-version tracking, and a
migration path (plausibly **agent-assisted** — read the campaign, diff against the current
spec, propose a refactor behind [[0028-checkpointed-human-gates]]). It's the fleet-scale face
of [[0036-every-subsystem-is-a-module]] (modules version; campaigns declare what they're built
against).

**Open threads.** How is a campaign's spec-version recorded (frontmatter? a manifest)? Is
migration eager or lazy (on next touch)? How does migration **preserve intentional exceptions**
([[0027-recurring-exception-taxonomy]]) without clobbering them — diff against *spec*, not
against other campaigns? Relationship between a campaign's spec-version and the versions of the
*modules* it uses. Could the same machinery migrate *modules* and *workflows*, not just
campaigns?
