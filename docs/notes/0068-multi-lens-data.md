---
tags:
  - kind/pattern
  - source/solorpg
  - theme/architecture
  - theme/context-economy
  - theme/single-source-of-truth
  - maturity/proven
  - verdict/adopt
created: 2026-06-05
---

# Multi-lens data — the same entity at several fidelities, for different readers

**What it is.** Across rust-and-ruin, the-silence (Lodestone), and pale-horizon, engineering
entities are deliberately described in **multiple files at different fidelity/goal** — the
user's "multiple lenses of the same data." The standard pair: a **full spec** (~80–1000
lines: design intent, failure modes, author lens) plus a **brief** (~20–40% the size:
stat-block + tactics, GM-at-table lens). Examples: Fenris / Old Grudge / Redhowl
(`rust-and-ruin/reference/vehicles/*.md` + `*-reference.md` + a `fleet.md` roster line),
Matau / Tala Moana / Nereid & Fenrir sleeves (`pale-horizon/.../ship-*.md` + `*-brief.md`).

**The maximal case — Lodestone's Eisrand walkers exist in 5+ places:**
1. `eisrand-walkers.md` — 1008-line full technical spec
2. `eisrand-walkers-gm.md` — 296-line GM brief (loadout tables, damage zones)
3. `eisrand.md` — faction doc: the walkers' *strategic* role in war doctrine
4. `characters/bruno.json` — character lens: "cables, ports, connectors, the things that
   go wrong on a siege walker between deployments"
5. `locations/weissdorn.json` — location lens: walker collars as fortress hardpoints
   …plus play-session prose (Greta's fire-control math).

**Key empirical finding: zero mechanical drift between copies.** Crew counts, depth
ratings, traverse rates all agree across lenses — but only by **manual discipline**. The
lenses differ in *aperture*, never in fact: full ref emphasizes failure modes, brief
emphasizes capability, faction doc emphasizes strategy, character/location data emphasize
lived experience.

**Where it comes from.** Explore-agent sweep of the three campaigns (2026-06-05), prompted
by the user mid-0067-discussion: "handling multiple lenses of the same data… the data
exists in *3* places. because it's different fidelity/goal in them."

**Why it matters for next-gen.** This is the killer app for the canonical vault
([[0067-campaign-data-as-linked-vault]]) + compiler ([[0044-scenario-compiler]]): one
canonical entity page, with the lenses as **build products at different fidelities** —
GM brief, faction summary, character-relationship snippet, location embed are *renders*,
not siblings. Drift becomes structurally impossible instead of discipline-dependent.
Also feeds [[0063-portable-bundles-constraint]] (thin bundle takes the brief lens, fat
bundle maybe both) and [[0056-files-as-build-products]] (lenses are the cleanest example
yet of files-as-renders).

**The user's framing (2026-06-05): "same document, different zooms."** The three variants
have distinct jobs: full doc = *everything* designed, "for revisiting the design in the
future" (archive zoom); brief = what play needs (table zoom); primer line = "you just want
to know the thing exists" (existence zoom). Not summaries of each other — the same document
at three magnifications.

**Next-gen direction (user):** for the vault ([[0067-campaign-data-as-linked-vault]]),
collapse the variants into **one file with multiple blocks, pulled selectively by whatever
wants the data**. Zoom tiers as *structure within the canonical page* — e.g. an
existence-line block, a table/GM block, a full-design block — and each consumer (compiler,
primer build, JIT mid-session read) pulls at its own depth. This answers 0067's cherrypick
contract: the structured-md sections are zoom tiers. It is also rpg-tools' tiered/progressive
loading philosophy relocated *inside* the document.

**Revised shape (same session): two trunks, one tree.** The one-file-many-blocks idea was
walked back — "a good wikidesign has the data dispersed, not monoliths, and i just pushed
for megamonoliths." Resolution: **play data lives in one trunk of the tree, design data in
a different trunk — same tree, separate, linked.** Entity pages stay small and dispersed
(existence line + play-relevant facts + links doing the heavy lifting); the full
everything-doc is demoted to a linked **design artifact** in its own trunk, reachable from
the page but never loaded by accident. Zooms thus become mostly **link hops** rather than
blocks-in-a-file: shallow read = the entity page, deep read = follow the design-doc link.
Context-economy win: a JIT "what's a Schreiter" read never touches a 1008-line file.

**Open threads.** Where exactly is the play/design cut for a given entity — does the GM-brief
zoom live on the entity page or as a third artifact? Are shallower tiers authored or derived
(the Lodestone brief has content the full doc barely surfaces — loadout percentages —
suggesting authored)? How do JSON-lens embeds (character/location relationships to an
entity) reference the page vs the design doc? And does the design trunk get its own
lifecycle rules ([[0049-disposable-bootstrap-primer]]-style lifespan metadata)?

**Verdict.** **Adopt** (appraised 2026-06-06). The pattern is proven (zero drift across
5+ hand-maintained lenses), and the next-gen shape is settled: two trunks, one tree —
play pages small and dispersed, design docs linked but never auto-loaded, zooms as link
hops. Open: where the GM-brief zoom lives, authored-vs-derived tiers.
