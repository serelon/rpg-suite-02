---
tags:
  - kind/pattern
  - source/rpg-tools
  - source/solorpg
  - theme/architecture
  - maturity/speculative
  - verdict/unevaluated
created: 2026-06-06
---

# Faction-as-character — and the economy module built for it (never deployed)

**What it is.** A campaign mode plus its purpose-built tool (interview 2026-06-06):

**Faction-as-character**: "where a faction and its fate and development is given as much
agency as a player character." Scope matters — it fits factions *at story scale*:
the **Delacroix** branch of the-long-watch (a 5-ship family clan of merchants with a
pirate backside — still in mothball, never converted to the new format) was the original
target; the **Askvargr** in rust-and-ruin would fit too. It is *not* for campaigns where
the faction is bigger than the story.

**The economy module** (factions.py: accounts, running costs, inventory, assets,
resources — the most elaborate schema in rpg-tools, [[0084-rpg-tools-data-layer]]) was
engineered for this mode and **never deployed**: the Delacroix never came out of mothball,
and by now the user has *forgotten how to use the tool*. Confirmed addition to the
built-never-used inventory ([[0050-built-never-used-inventory]]).

**Design intent, in the user's words:** for campaigns "where crunching the numbers rather
than yoloing it is important. it's our glorified spreadsheet. we could actually replace it
with a custom campaign spreadsheet if we had a spreadsheet tool." Cleanly **tool data**
in [[0085-knowledge-entries-vs-tool-data]] terms — module-owned mechanical state, GM sees
outputs, never raw tables. Possibly not even a bespoke module: a campaign-spreadsheet
*capability* that faction-economy is one template of.

**New failure mode named:** "some of the tools are too obfuscated for the user, hard to
read and audit. and thats a failure mode." Distinct from built-never-used's *why didn't
it deploy* — this is **illegibility as decay accelerant**: a tool the owner can't read
or audit stops being trusted, then stops being remembered. Sibling of
[[0057-compiled-context-needs-audit-tooling]] (auditability as first-class) and a design
requirement for next-gen tool data: **the human must be able to open and understand the
state file** — which the JSON economy schema arguably fails and a spreadsheet wouldn't.

**Why it matters for next-gen.** Faction-as-character is a real mode with two live
candidates waiting (Delacroix unmothball, Askvargr). The module question: does next-gen
carry a faction-economy module, or a generic **campaign-spreadsheet tool-data type** that
faction economy instantiates ([[0036-every-subsystem-a-module]] favors the latter)?
Either way: legible state files, or it dies in mothball again.

**Open threads.** Delacroix unmothball as a [[0043-campaigns-as-testbeds]] candidate —
the natural test campaign for faction-as-character in the new system? Does
faction-as-character need its own savefile/thread shapes (a faction has arcs, debts,
reputations — [[0070-threads-tracker-design]] for organizations)? Where's the line
between "crunch matters" and "yolo it" — is that a campaign-level flag the spec should
own?

**Verdict.** _(unevaluated.)_
