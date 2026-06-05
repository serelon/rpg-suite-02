---
tags:
  - kind/pattern
  - source/solorpg
  - theme/architecture
  - theme/context-economy
  - theme/single-source-of-truth
  - maturity/proven
  - verdict/unevaluated
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

**Open threads.** Can a brief actually be *generated* from a full spec, or does a good
brief contain editorial judgment (what matters at the table) that must be authored — i.e.
is the lens a render or a curated view with its own source-of-truth slice? The Lodestone
brief has loadout percentages the full ref barely surfaces — lens-specific *content*, not
just compression. Maybe: canonical page holds all facts, each lens declares which facts +
what framing it takes (selection authored once, rendering automatic).

**Verdict.** _(unevaluated.)_
