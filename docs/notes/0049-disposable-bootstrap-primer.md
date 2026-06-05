---
tags:
  - kind/pattern
  - source/rpg-tools
  - theme/architecture
  - maturity/proven
  - verdict/adapt
created: 2026-06-03
---

# Disposable bootstrap — the session-01 primer is scaffolding that knows it will die

**What it is.** The campaign-zero bundle is three-tiered by *lifespan*: `setting-primer.md`
(permanent, reusable across campaigns), `campaign-primer.md` (permanent, this campaign),
`session-01-primer.md` (**disposable** — exists only to bootstrap play, consumed into real
data files after session 01). Scaffolding with a declared expiry.

**Where it comes from.** `rpg-tools/references/campaign-zero-guide.md` ("skeleton vs flesh"
philosophy: build the load-bearing bones, defer the flesh to discovery in play).

**Why it matters for next-gen.** Artifacts whose lifespan is declared at creation never
become stale authority — they can't be mistaken for canon because they're *expected* to be
superseded. Pairs with [[0048-canon-precedence-and-naming-is-permission]] (primers demote
from source to design-intent after play).

**Open threads.** I initially claimed this is "the antidote to [[0034-outgrown-scaffold]]" —
the user flagged that as a misreading of 0034; linkage dropped pending a re-read. Is
lifespan-tiering worth making explicit metadata on artifacts in the next-gen spec?

**Verdict.** **Adapt** (appraised 2026-06-05). Lifespan-tiering is right, but expiry is not
a hard date: session-0 primers legitimately survive past session 01 when an **origin story
takes multiple sessions**. So next-gen should declare lifespan as a *condition* ("dies when
the origin arc closes"), not an event count. Lifespan-as-metadata on artifacts: yes, carry
forward.
