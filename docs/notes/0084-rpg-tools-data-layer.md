---
tags:
  - kind/pattern
  - source/rpg-tools
  - theme/architecture
  - theme/context-economy
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-06
---

# The rpg-tools data layer is a proto-KB — steal its primitives, not its plumbing

**What it is.** Census of rpg-tools (sweep 2026-06-06, preserved in [[census-rpg-tools]]):
the toolbox already implements, in miniature, several primitives the canonical vault
([[knowledge-base-canonical-vault]]) needs:

- **Tiered loading as schema** — `minimal` (essence ≤35 words, role, voice) / `full` /
  `sections{…}` on characters, locations, factions. This is [[0068-multi-lens-data]]'s
  zoom tiers already living *inside one record*, with CLI flags (`--depth`, `--section`)
  as the cherrypick contract.
- **Read-anywhere / write-canonical** — 8-path merged discovery, writes always to the
  canonical folder. The KB's "consumers read from anywhere, librarian writes to one place"
  in embryo. Caveat: paths 5–8 are Claude.ai-runtime mounts — transient-constraint
  material ([[0031-beware-transient-constraint-architecture]]).
- **Namespace resolution + inheritance** (namesets v2): `namespace:id`, bare-ref fallback,
  `extends` chains with circular detection, per-entry tags/weights. The most evolved type
  system in the stack — and a `hidden` flag (the metadata-smuggling spot the user
  mentioned, [[0072-schema-drift-tools-vs-hand-edited-json]]).
- **Link integrity exists in exactly one tool** — memories.py validates `connections{}`
  and warns on broken refs (no cascade, orphans flagged). The custodian's graph-health job
  ([[0075-postprocessing-as-vault-librarian]]) has precisely one working prototype.
- **Era/session parsers + modular calendars** — "~15000 BCE" and "Y3.D45" both sort;
  offset vs loose calendars per campaign config. Timeline-aware data is solved
  infrastructure, relevant to the per-era axis ([[0047-multi-axis-data-management]]).

**Census oddities worth flagging:**
- **factions.py carries a full economy submodule** (accounts, running costs, inventory,
  assets) — most elaborate schema in the toolbox; real-campaign usage unverified →
  built-never-used audit candidate ([[0050-built-never-used-inventory]]).
- **pool.py skips multi-path discovery** (cwd only) — the lone inconsistency.
- **Version skew is intent-shaped:** nameset-guide documents cross-campaign shared-world
  namespaces (valdran, caldworth, solramis) — a use case that never manifested; in
  practice namespaces are campaign-scoped. Docs describing aspiration as if it were
  practice.

**Why it matters for next-gen.** The KB design shouldn't start from zero: tiered records,
canonical-write discovery, namespace/extends, ref validation, and calendar parsing are
*proven primitives* — what gets replaced is the plumbing (per-type CLI silos, formats
defined in guides instead of enforceable schemas). The census also sharpens the
[[0083-data-type-census]] finding: rpg-tools types are exactly the low-variance ones.

**Open threads.** Does the minimal/full/sections record shape survive translation to
structured markdown pages, or do tiers become page sections ([[0068]])? Is nameset-v2's
namespace system the seed of cross-campaign reference (the campaign-isolation question the
theme deferred)? Verify factions.py economy usage in real campaigns.

**Verdict.** _(unevaluated.)_
