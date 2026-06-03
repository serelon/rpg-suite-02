# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

`rpg-suite-02` is a **greenfield scaffolding repo for a next-generation RPG workflows/toolchain**. It is currently pre-code by design — no build, no tests yet. We are in the **research and speculation phase**: collecting ideas and patterns from existing RPG repos before any planning or building begins.

> **On the name:** the `-02` is a misnomer — this is really the 5th or 6th iteration of the user's RPG system, not the second. Don't read lineage into it. A rename may come later.

**Do not rush ahead.** The user has been explicit that this phase will last a while. Default to gathering, characterizing, and indexing patterns — not designing architecture or writing code — unless the user clearly signals a move into planning or implementation. When in doubt, surface options and ask rather than scaffolding prematurely.

The progression is: **research/speculation → planning → building.** Know which phase you're in before acting.

## Capturing research (where findings go)

This repo doubles as an **Obsidian vault** for organizing the research. The structure is intentionally disposable — **tags are the source of truth, folders are convenience** — because the best organizing pattern isn't known yet. See `docs/README.md` for the full conventions; the essentials:

- `relevant-paths.md` (root) — **living index**: the source repos + one line per note. Keep it current.
- `docs/notes/` — **atomic captures**, one idea/pattern/workflow/question per file (`NNNN-slug.md`), with hierarchical-tag frontmatter (`kind/`, `source/`, `theme/`, `maturity/`) and `[[wikilinks]]`. Start from `docs/notes/0000-note-template.md`.
- `docs/themes/` — **synthesis docs**, written only when a `theme/` tag earns enough notes to graduate.
- `ROADMAP.md` (root) — placeholder; the *last* artifact, populated only when proven/decided material exists to sequence.

- `inbox/` (root) — drag-and-drop queue for raw, unprocessed material. Not canonical; emptied as items are mined into notes.

**Workflow: mine → report → appraise → commit.** Mine patterns in *small batches* (~3–5), report them back, then **appraise together** before committing. Every note is born `verdict/unevaluated` and stays that way until we explicitly judge it (`adopt`/`adapt`/`reject`/`undecided`) — this gate is deliberate, to protect the good-vs-bad evaluation step from being skipped. Find un-reviewed notes via the `verdict/unevaluated` tag. Keep `maturity/` (proven *in its source*) distinct from `verdict/` (our call for next-gen).

Lifecycle: **capture → appraise → cluster (theme) → decide → sequence (roadmap).** When you discover a pattern in a source repo, write it as a note and index it — don't let it live only in chat. See `docs/README.md` for the full conventions.

## Source repos (the research material)

Four existing repos are the raw material. They are siblings/externals, not part of this repo. Each has its own `CLAUDE.md` worth reading in full when digging in.

| Path | Role | Status the user gave |
|------|------|----------------------|
| `../rpg-tools/` | Portable, dependency-free Python toolbox (dice, oracle, tarot, namegen, characters/locations/memories loaders). Packages into a Claude Desktop `.skill`. | "Half obsolete, half cutting edge, always used." |
| `../solorpg/` | The main vault: ~16 active solo campaigns, session import/export workflow, bundling, post-processing agents, skills. Embeds `rpg-tools` as a submodule. | "Data is *very* important; workflows key but having growing pains; lots needs refurbishing." |
| `../aegis-tools/` | A modular rules/tool engine — an RPG *system* (1940s XCOM-style tactical) expressed as CLI layers: `tactical.py`, `strategic.py`, `threads.py`, `intel.py`, `gm.py` over `lib/` + `modules/`. | "Rules engine in modular shape." |
| `E:\rpg` | Old, obsolete infra repo: Qdrant + Wiki.js + MCP, a 5-agent session-processing pipeline (parser → entity extraction → timeline → wiki → briefing). | "Obsolete, but has patterns I never transferred over." Mine for patterns, don't treat as live. |

There are "a few more bits 'o info here and there" the user will surface over time. **As new sources appear, index them** (the user explicitly expects this).

## How the source repos relate (the big picture)

These four are different cuts at the same problem — running rich, long-lived solo RPG campaigns with Claude — and the tension between them is the whole point of this research phase:

- **`rpg-tools`** is the stateless mechanics layer (read-anywhere/write-canonical data discovery, tiered/progressive loading to save context). Designed to be portable into both Claude Code and Claude Desktop.
- **`solorpg`** is where that toolbox is *used at scale* — and where the growing pains live: bundling sessions into portable zips, preprocessing JSONL exports, post-processing into summaries/savefiles/memories, multi-branch and non-linear (timeline-aware) campaigns.
- **`aegis-tools`** shows the opposite end: a real **rules engine** with enforced state mutation (`gm.py` deliberately bypasses the rules). It's the "system as code" pattern that `rpg-tools`/`solorpg` deliberately avoid.
- **`E:\rpg`** is the abandoned "heavyweight infrastructure" answer — vector DB + wiki + agent pipeline + entity-ID disambiguation + retcon/branch versioning. The patterns (multi-granularity chunking, campaign isolation, entity registries) are valuable; the Docker/MCP infra is not being carried forward as-is.

A core recurring principle across all of them: **campaign isolation** (separate worlds, no cross-contamination) and **context economy** (load the minimum needed during play). Expect the next-gen design to grapple with both.

## Working conventions

- **Source repos are read-only research material.** Don't edit `../rpg-tools/`, `../solorpg/`, `../aegis-tools/`, or `E:\rpg` while researching here unless the user asks.
- All four source repos are pure-Python, stdlib-only, JSON-for-persistence. That's a likely constraint for what's built here too — confirm before assuming otherwise.
- When capturing research, prefer durable notes/index files in this repo over ephemeral chat so findings survive across sessions.
- This repo is **not a git repository yet**. Don't assume git workflow until it's initialized.
