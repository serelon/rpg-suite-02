---
tags:
  - kind/pattern
  - source/rpg-tools
  - source/aegis-tools
  - theme/data-access
  - theme/portability
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Read-anywhere, write-canonical data access

**What it is.** Tools *discover* data by searching many locations and merging everything
found; they *write* only to one canonical path. `rpg-tools` searches 7 locations and
merges; new items go to `{cwd}/{data_type}/{id}.json`, updates modify the original file in
place. `aegis-tools` does the same shape: checks `AEGIS_CAMPAIGN_ROOT` env var → `./data/`
(bundle mode) → `campaigns/aegis/` walking up → sibling `solorpg/campaigns/aegis/`.

**Where it comes from.** `rpg-tools/scripts/lib/discovery.py`; `aegis-tools/README.md`
("Tools auto-detect campaign data in these locations").

**Why it matters for next-gen.** This is what makes the same tool work unchanged in a
local vault *and* inside a portable Claude Desktop bundle — read flexibility decouples the
tool from where data physically lives. It's the quiet enabler of the whole bundle workflow.

**Open threads.** The merge-everything read is permissive — no single source of truth on
read, which could mask stale/conflicting copies. `old-erpg` went the opposite way: one
authoritative store (Qdrant + Wiki.js) with entity IDs. Trade-off worth a `kind/decision`
note later: convenience/portability vs. authoritative single store. Pairs with
[[0001-tiered-progressive-loading]].
