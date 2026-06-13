---
tags:
  - kind/design-note
  - source/solorpg
  - theme/architecture
  - theme/corpus-building
  - maturity/experimental
  - verdict/unevaluated
origin: ../solorpg/imports/IMPORT-DESIGN-BRIEF.md (the user's own pre-planning, authored in solorpg)
atomized-into: "0108, 0109, 0110, 0111, 0112 (+ confirmations folded into 0001, 0102, 0103)"
roadmap-candidate: true
created: 2026-06-13
---

> **Preserved primary source.** The user's own framework-agnostic pre-planning for the
> next-gen import pipeline — explicitly "a *consumer* of the coming toolchain refactor."
> One of multiple entrypoints to the future workflow → **roadmap candidate** (pre-planning,
> not a full plan; waits for a pipeline to slot into). Atomic patterns extracted into
> notes 0108–0112; companion data map is [[export-structure-map]]. Verbatim below.

# Export-Import Pipeline — Design Brief

**Status:** Research/planning only. No pipeline built. Deliberately framework-agnostic —
this is a *consumer* of the coming toolchain refactor, not an appendage to the current layout.
See `EXPORT-STRUCTURE-MAP.md` for the concrete data shapes this builds on.

**One-line:** Turn periodic Claude Desktop exports into (a) routed campaign material and
(b) a mineable semantic index + provenance graph over the whole creative corpus.

---

## Why this waits for the refactor

The load-bearing pieces — multi-label relationships, a provenance graph, UUID-keyed
incremental merge — are **data-model decisions**, and the refactor is where the data model
gets redrawn. Building them against the current `tools/` layout means rebuilding in months.
A semantic index + relationship graph over the corpus is plausibly a *native capability* the
refactored framework wants, not an import script. So: design now, build into the new frame.

---

## Hard constraints (these shape everything)

1. **Recurring, not one-shot.** This is dump #1. Future dumps are *superset snapshots*: the
   same UUIDs reappear, some conversations longer (chatting continued), plus new ones. The
   scaffold must treat re-import as the normal case, not an edge case.
2. **UUID is the stable spine.** Conversations, projects, docs all carry stable UUIDs. Every
   stage keys on UUID and **merges, never rebuilds**.
3. **Stream from the zip.** Full decompress of `conversations.json` is ~1.4 s; never unpack the
   529 MB to disk. One forward streaming pass is the unit of work. (DEFLATE is sequential — no
   cheap random access to conversation N; design around forward passes + a UUID→offset/shard
   index if random access is later needed.)
4. **Classification is multi-label & relational, not folder assignment.** A conversation can
   belong to two campaigns (crossover), be the ancestor of one (reboot seed), or be a meta-chat
   *about* a campaign. Output a *set of typed edges*, not one path.
5. **Lossy source for binaries.** `files[]` are bare references — image/map/binary bytes are NOT
   in the export. Only `attachments[].extracted_content` (text) survives. Accept text-only or
   source originals elsewhere.
6. **Don't add load before the refactor.** Today's artifact is this brief, not code.

---

## Data model (the durable core)

Keyed by conversation UUID. Per conversation, accumulate across dumps:

```
record {
  uuid                      # stable primary key
  name, created_at
  updated_at, msg_count     # change-detection: grew? → re-process
  last_processed_dump       # idempotency: skip if unchanged
  embedding_ref             # vector id (recomputed only on grow)
  routing: [ edge... ]      # typed relationships, below
  rulings: [ ... ]          # human decisions — durable, never re-adjudicated
}
```

### Relationship edge types (routing output)
- `belongs-to: <campaign>` — a play/session conversation of a known campaign
- `crossover-between: [<campaign>, <campaign>]` — sits genuinely between settings
  (e.g. the Sophie drop from Long Watch into Great Awakening)
- `seed-of: <campaign>/<branch>` — an orphan that became canon
  (e.g. "lone consciousness on an alien world" → Pale Horizon / Parniyan branch)
- `variant-of: <conversation-uuid>` — alternate attempts at the same thing
  (e.g. 3 failed Sophie-drops pointing at the 1 successful one)
- `about: <campaign>` — meta/planning/discussion *of* a campaign, not play
- `cluster: <discovered-label>` — unsupervised grouping (non-campaign or not-yet-a-campaign)
- `unrelated` — junk / out-of-scope (e.g. the meme thread — kept & labeled, not deleted)

Edges carry confidence + provenance-of-decision (heuristic / embedding / model / human).

---

## Two spines, one embedding pass

The same per-conversation embedding feeds both products.

### Spine A — Supervised routing (campaigns you have)
- Build labeled reference points from well-named sessions, project docs, `project_memories`
  blobs, and campaign `reference/` folders.
- **k-NN, NOT centroids.** Classify an orphan by its nearest *individual* labeled neighbours,
  majority-vote. Robust to tonal/arc/POV/model drift within long campaigns — an arc-3 orphan
  matches other arc-3 points even when arc-1 points are tonally distant. Averaging to a single
  centroid would blur exactly the campaigns that matter most.
- Top-2 neighbours from different campaigns → contested → emit `crossover-between` and/or
  escalate. The geometry honestly reporting "between two clouds" IS the crossover detector.

### Spine B — Unsupervised survey (the wilderness)
- Cluster the *un-routed* remainder with no labels. Out fall natural groupings: abandoned
  worldbuilding seams, the meme thread, magic-system tinkering scattered across unrelated chats.
- Each cluster = a candidate idea-seam to mine, or a campaign-you-forgot-you-had.
- This is arguably the higher-value half: the campaign sessions mostly already live in
  `solorpg`; the floating seeds are genuinely lost.

### Bonus capability (falls out for free)
A semantic index over 2 years of output → **concept retrieval**: "every time I sketched a
prison-dungeon dynamic," "anything with portable-consciousness before Pale Horizon." An
idea-recovery tool used for years, not a one-time import step.

---

## Tier pyramid (cost narrows hard at each step)

| Tier | Engine | Job | Sees |
|------|--------|-----|------|
| 1 | regex/heuristic on `name` | well-named sessions → `belongs-to` | the majority |
| 2 | `bge-m3` embed + k-NN | orphans; confident matches auto-route | the residue |
| 3 | local gemma (incl. 27B/a4b via litellm.localhost router) | read a sample, decide low-confidence/contested | a trickle |
| 4 | Claude | adjudicate crossovers, name new clusters, confirm seeds | a handful |

Local tier covers the bulk → saves tokens. The 27B on the router lifts tier-3 capability
(no longer "between haiku and sonnet"), so fewer escalations to Claude.
**Open:** what to embed per conversation — full doc (avg-pool, faithful, more compute) vs.
sample (first+last few human turns, cheap, usually enough to fingerprint). Default to sample
for triage; full-doc embed in reserve for muddy clusters.

Local models available (probed 2026-06-13): ollama `bge-m3`, `nomic-embed-text`,
`mxbai-embed-large` (embedding); `gemma4:e2b/e4b`, `mistral-nemo-gutenberg-12B`; plus a
27B/a4b gemma via `litellm.localhost` router.

---

## Incremental re-import (dump #2+)

On a new dump, diff against stored records by UUID:
- **new** UUID → embed + classify (full tier pyramid)
- **grew** (msg_count/updated_at advanced) → re-embed + re-check routing
- **unchanged** → skip entirely
Human `rulings` persist against the UUID and survive re-import — never re-adjudicate a
confirmed call. Dump #2 therefore costs a fraction of dump #1.

---

## Provenance graph (the secret history)

Beyond routing, the `seed-of` / `variant-of` / `crossover-between` edges reconstruct how
settings actually evolved: which floating oneshot seeded which canon branch, which failed
attempts orbit which success. Worth capturing as a first-class artifact — folder-routing alone
would discard it as residue.

---

## Open decisions (for Therese, at build time)

1. **Scope** — port all RPG material, or only campaigns already live in `solorpg`? (Affects how
   many reference clouds Spine A needs.)
2. **Binaries** — accept text-only, or hunt originals for image/map `files[]` references?
3. **Index home** — does the semantic index live in the refactored framework as a native
   capability, or as a sidecar store?
4. **Embed granularity** — sample vs. full-doc as the default (see tier table).
5. **Mining cadence** — is wilderness-survey a one-time sweep, or a standing tool you re-run as
   each dump adds material?
