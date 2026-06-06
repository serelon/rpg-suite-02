---
tags:
  - kind/theme
  - theme/architecture
  - theme/single-source-of-truth
  - theme/context-economy
  - maturity/growing
  - verdict/adopt
created: 2026-06-06
appraised: 2026-06-06
synthesizes:
  - "[[0067-campaign-data-as-linked-vault]]"
  - "[[0068-multi-lens-data]]"
  - "[[0069-one-knowledge-base-many-presentation-layers]]"
  - "[[0072-schema-drift-tools-vs-hand-edited-json]]"
  - "[[0073-structured-mutation-beats-rewrite]]"
  - "[[0075-postprocessing-as-vault-librarian]]"
  - "[[0076-self-canonizing-hallucinations]]"
  - "[[0077-context-injection-vs-cache-economics]]"
  - "[[0082-live-hook-pipeline]]"
  - "[[0070-threads-tracker-design]]"
  - "[[0071-fog-of-war-as-data-structure]]"
---

# The Knowledge Base — canonical vault, lenses, librarians

> **Second synthesis doc — appraised 2026-06-06, verdict: adopt.** Thesis ratified by the
> user after point-by-point pushback (see Appraisal record at bottom). Cluster notes carry
> individual verdicts (0072 stays `undecided`). Headline standing work item: **KB
> structure needs a lot of thinking — data types, formats, templates — not just placement
> and linking.**

## The thesis (what we believe so far)

**All campaign data lives in one canonical, linked, structured-markdown vault. Everything
else — bundles, jsons, briefs, injected context — is a build product rendered from it by
swappable consumers. Writes go through librarians that mutate, never rewrite. Truth is
defended structurally — provenance, precedence, write-time validation — not by model
judgment.** Four moves that are one idea: *canonical shape, rendered views, operated
writes, defended truth.*

This is the sibling of [[modular-self-evolving-architecture]]: that theme says every
*concern* has one home; this one says every *fact* does — and works out what reading and
writing that home looks like.

## The disease: flat files, manual discipline, rewrite drift

- **All-or-nothing reads.** "flat data, flat files, flat everything. you either read
  everything or nothing. no way to see relations" ([[0067-campaign-data-as-linked-vault]]).
- **Multi-lens by hand.** The same entity maintained in 2–5 files at different fidelities
  — zero drift found, but only via sheer discipline ([[0068-multi-lens-data]]: the Eisrand
  walkers in 5+ places). Discipline doesn't scale; structure does.
- **Rewrite drift.** Artifacts that get *regenerated* (savefiles, summaries) bleed data
  and mutate canon; artifacts that get *operated on* (the threads tracker,
  [[0070-threads-tracker-design]]) stay trustworthy ([[0073-structured-mutation-beats-rewrite]]).
- **Silent schema drift.** aegis's live data went off-schema within weeks, invisibly even
  to its author — tools that tolerate divergence silently *hide* it
  ([[0072-schema-drift-tools-vs-hand-edited-json]]).
- **Self-canonizing hallucinations.** A checker reading a self-contaminated corpus
  confirms inventions — "was written in, so must be canon!"
  ([[0076-self-canonizing-hallucinations]]).

One disease, five faces: **the data has no shape that defends itself.**

## The cure, part 1 — canonical shape

- **The vault is canon; the build arrow inverts.** Linked, Obsidian-style,
  structured-markdown pages; "the jsons (or whatever next-gen thing we do) *builds* from
  the vault" (0067). E:\rpg compiled wiki *from* data; we compile data *from* the wiki.
- **Two trunks, one tree.** Play pages small and dispersed (existence line +
  play-relevant facts + links doing the work); design megadocs in their own trunk —
  linked, never auto-loaded. Zooms are mostly *link hops* (0068).
- **Relations are first-class.** Links are the edges; bidirectional auto-reverse at write
  time so half-links are impossible (0070's proven trick). Knowledge-scoping can be
  structural too — observed/actual blocks rather than model judgment
  ([[0071-fog-of-war-as-data-structure]]).
- **Pages carry consumer hints in the data itself** — volatility/placement metadata
  (0077), trigger keywords validated against the session corpus (0069), zoom-tier blocks
  (0068): "the rules for where to inject data must start with the data itself."

## The cure, part 2 — rendered views

- **One KB, many presentation layers** ([[0069-one-knowledge-base-many-presentation-layers]]):
  the bundle compiler (portable monolith + bundled db — today's pattern, kept), the
  agentic explorer (JIT link-following; initiative prompting is the named blocker), and
  keyword-RAG injection. Consumers are modules over a stable data contract; cache
  economics, RAG quality, and agentic skill are *era variables* and live consumer-side
  ([[0031-beware-transient-constraint-architecture]]).
- **Retrieval is layered: exact → graph → vector.** Names/aliases by exact match, related
  things by walking edges, vector search only as fuzzy-recall fallback (it's bad at exact
  things, its chunking is the real design problem, and its index lies when stale).

## The cure, part 3 — operated writes

- **Post-processing is the librarian** ([[0075-postprocessing-as-vault-librarian]]): the
  KB's write path. It updates pages, adds session pages, links entities — via mutations.
- **Structured mutation is a hard rule** (0073, adopted as such): append, transition,
  patch — *"unless specifically audited, never change the wording or data context of
  files; only datastructs."* Wording changes are an explicit audited pass, never a side
  effect.
- **Hooks may stream it** ([[0082-live-hook-pipeline]]): tiny cheap agents firing on
  events ("run agent x at stage a whenever y has happened") do live extraction so the
  main agents keep their attention on the story; batch sweep remains the fallback, so
  hooks are best-effort and never block.
- **A custodian probably joins the librarian** (0075, shape undecided): graph health,
  archiving, contradiction-surfacing, format flags, exception-hunting — cold-eyed,
  periodic, and **propose-never-commit**: "always talk to the human before doing changes."

## The cure, part 4 — defended truth

- **Provenance ("receipts").** Claims carry source pointers; *unsourced* is what a checker
  hunts, not confirms (0076). Granularity is the open tuning problem — section-level is
  the starting guess.
- **Check downstairs, never the mirror.** Verify against the layer below (summary →
  transcript, page → session source); never a document against itself or its siblings.
  In-play checkers point *down* the precedence stack
  ([[0048-canon-precedence-and-naming-is-permission]]) — the freshest text is the least
  authoritative.
- **Validation at write time** — whitelists and loud errors kept aegis's guarded fields
  clean (0070/0071); silent tolerance hid drift for the system's whole life (0072).
  *Stance pending 0072's cause-unknown investigation.*

## Why it's one idea

A canonical shape makes rendered views possible (you can only compile lenses from a single
truth); rendered views make operated writes *sufficient* (nobody hand-maintains five
copies, so mutations on one page propagate); operated writes make defended truth *cheap*
(provenance and precedence survive because nothing rewrites them away). Take out any leg
and you're back to manual discipline — which the Eisrand walkers prove is possible and the
rest of the corpus proves is the exception.

## What's still soft (carry forward)

- **The KB contract surface** — files+links only, or a shared query/index primitive that
  compiler and RAG both use? (0069)
- **The cherrypick contract** — frontmatter vs section schema; who enforces page structure;
  fixed zoom-tier vocabulary or per-type? (0067/0068)
- **Custodian shape & cadence**; scene-boundary detection for streaming (genuinely
  unsolved); hook trigger vocabulary and budget. (0075/0082)
- **Provenance granularity** (0076); **0072's cause** (hand edits, tool versions, or
  metadata smuggling?) gates the validate-loudly stance.
- **Migration path** — today's canonical JSONs become build products; in what order, and
  what happens to in-flight campaigns ([[0042-async-fleet-migration]] presumably)?
- **Campaign isolation** — per-campaign vaults assumed but not designed; cross-campaign
  reference (settings shared by branches/subsettings) needs a story.

## Appraisal record (2026-06-06)

**Assistant's pushback and the user's responses:**

1. *"The vault is a markdown database, and markdown is a bad database."* — Acknowledged:
   "'markdown database' is not ideal, but having it obsidian compatible is. i'm not sure
   how much wiggle room we have there." The existing JSON database is "fairly nice,
   tooling wise, but hard for the user to browse." Alternative noted but **not sold on**:
   a JSON/NoSQL db fronted by a custom Project-Unicorn interface. Human-browsability is
   the binding constraint; the cherrypick contract must stay small.
2. *"The librarian is a bottleneck by design."* — Agreed. Current librarian flow is
   post-session with a big audit step. A live/parallel librarian "would need a way to
   loop back non-audited things early, and defer the audit abit. maybe...idk" — open.
   **Important boundary drawn:** widget/state-level writes *aren't the librarian process
   at all* and aren't constrained the same way — "a widget could just read the latest
   post and be like 'yeah, heres some garbage i just made up' and that destroys nothing."
   Ephemeral display ≠ canon writes. (Plus: tool calls with **widget sidecards** — fancy
   graphical dice rolls inline — folded into [[0082-live-hook-pipeline]].)
3. *"Auto-reverse links conflict with structured mutation."* — "needs thinking about."
   Open; leading candidate: edges as datastructs (frontmatter), never in prose, which
   0073's rule already permits mutating.
4. *"Campaign isolation is hand-waved."* — Confirmed deferred: "we'll have to do a fair
   bit of thinking about this later." Broadened by the user into the **biggest named
   design-work item of the theme: KB structure needs *a lot* of thinking — not just where
   to put data and how to link it, but data types, formats, templates.**

**Status:** thesis engaged point-by-point, no leg rejected; **ratified — adopt**
(2026-06-06). Soft list stands as design work.
