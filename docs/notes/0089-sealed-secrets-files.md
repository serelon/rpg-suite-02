---
tags:
  - kind/pattern
  - source/solorpg
  - theme/context-economy
  - theme/architecture
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-06
---

# Sealed secrets files — content hidden from the GM until the story earns it

**What it is.** Four dedicated secrets files exist (sweep + interview 2026-06-06):
`emberfall/branches/vekris/secrets/secret-0{1,2}.md` (sequential plot pivot: party wipe →
resurrection), `radiance/secrets/truth.md` (cosmology), `rust-and-ruin/branches/solace/
secrets/ashblind.md` (character nature in real violence). Shared, designed pattern:
dedicated `secrets/` folder; opening line **"DO NOT READ until [condition]"**; trigger
conditions mirrored in CLAUDE.md. Trigger styles vary: sequential chain (Vekris),
story-earned judgment ("you'll know when", Radiance), event-based (first real combat,
Solace).

**The audience is the GM model itself.** "we want to isolate the fact from it, to avoid
drift from foreshadowing. this is to create bigger plottwists :)" — same root mechanism as
[[0079-relational-anchoring-antipattern]]: whatever is in context shapes output, so a GM
that *knows* the twist telegraphs it. Context-exclusion as a **craft tool for surprise**,
the third member of the exclusion family (worldbuilding exclusion 0079, fresh-context
audit [[0052-evolution-vs-drift]], now sealed secrets). Extends
[[0071-fog-of-war-as-data-structure]]'s epistemics axis one level up: observed/actual
hides from the *player*; sealed files hide from the *GM*.

**Operational track record (proven):** the GM has **never opened one prematurely** —
the failure mode is the opposite: "sometimes i've had to prod it to open one it hasnt
opened on its own." Asymmetric, and the *good* asymmetry (over-caution beats leaks) —
also a rhyme with [[0060-jit-loading-retry]]'s not-reaching failure mode: models
under-read gated content.

**The railroad exception, scoped.** Vekris secret-01 pre-scripts a party wipe
("non-negotiable") in a system where railroads are seed-failure #1
([[0080-engineer-and-gardener]]). Resolution: "the railroad here only exists between
secret 1 and 2 — before then, it was a scenario seed, after that the session started for
real… for origin stories there are going to be mandatory beats. or the concept wont
happen." So: **mandatory beats are legitimate inside a sealed, bounded segment** (an
origin's load-bearing skeleton), and the seal is what makes them playable — the GM can't
foreshadow rails it can't see. Refines 0080's taxonomy — and the user refined it further: the real distinction is
**goalposting vs beat-by-beat planning**. Mandatory waypoints with open-ended play between
them are fine (sealed origin beats are exactly that); "unprompted session-planning… a
detailed beat-by-beat plan is the nono." Rails minimal, goalposts open.

**Why it matters for next-gen.** Completes the audience axis
([[0088-player-display-artifacts]]) with its missing quadrant: content hidden *from the
model*. The KB needs a **sealed flag** as a first-class treatment
([[0085-knowledge-entries-vs-tool-data]]): excluded from all consumers (compiler,
agentic reads, RAG — a sealed page must never be vector-indexed or keyword-triggered!),
with a declared unlock condition ([[0049-disposable-bootstrap-primer]]'s
lifespan-as-condition, mirrored: birth-condition instead of expiry). The prod-to-open
problem suggests the *unlock check* belongs in a hook ([[0082-live-hook-pipeline]]) or
prep-stage checklist, not the busy GM's judgment ([[0066-mandatory-presence-not-length]]).

**Open threads.** Who authors secrets — workshopped with the user present (so the user
knows; the seal protects only the GM) — and is there appetite for secrets sealed from
*both* (generated, never shown)? Should triggers be machine-checkable where possible
(event-based ones like "first real combat" could be hook-detected) vs judgment ones
("story earns it") staying human-prodded? Census gap: secrets/ folders were missed by the
type census — add to [[census-solorpg-data-types]].

**Verdict.** _(unevaluated.)_
