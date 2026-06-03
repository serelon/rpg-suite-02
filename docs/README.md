# docs/ — capture & organization conventions

This folder is an **Obsidian vault**. Open the repo root as a vault and browse by the
tag pane and graph view. Everything here is plain, Obsidian-compatible Markdown.

The structure is deliberately disposable: **tags are the source of truth, folders are
convenience.** We don't yet know the best organizing pattern, so nothing here should be
expensive to reorganize. Re-slicing happens by retagging and querying, not by moving files.

## Layout

```
relevant-paths.md   # living index (repo root): source repos + every note
docs/
  notes/            # atomic captures — ONE idea/pattern/workflow/question per file
  themes/           # synthesis docs — written later, when a tag earns its keep
  README.md         # this file
ROADMAP.md          # placeholder; populated when notes mature (repo root)
```

## Notes

- One note = one thing. Keep them short. If a note sprouts a second idea, split it.
- Filename: `NNNN-kebab-slug.md`, zero-padded sequential number.
- Start from `notes/0000-note-template.md`.
- After writing a note, **add a row to `relevant-paths.md`**.
- Link liberally with `[[wikilinks]]` — a link to a note that doesn't exist yet is fine;
  it marks something worth capturing.

## Tag vocabulary

Tags are **hierarchical** (Obsidian nests them under `/` in the tag pane). Use these axes:

- `kind/` — `pattern` · `idea` · `workflow` · `question` · `decision`
- `source/` — `rpg-tools` · `solorpg` · `aegis-tools` · `old-erpg` · `tarot-tales` · `new` · `cross`
- `theme/` — free-growing (`theme/context-economy`, `theme/bundling`, …). Coin new ones freely.
- `maturity/` — how proven **in its source**: `seed` · `growing` · `proven` · `obsolete`
- `verdict/` — **our** judgment for next-gen: `unevaluated` · `adopt` · `adapt` · `reject` · `undecided`

A note typically carries one `kind/`, one or more `source/`, any number of `theme/`, one
`maturity/`, and one `verdict/`.

> **`maturity/` ≠ `verdict/`.** Maturity describes how battle-tested the pattern was *where
> it came from*; verdict is *our* call on whether to carry it forward. A pattern can be
> `maturity/proven` yet `verdict/reject` (proven, but not for where we're going). Keep them
> separate — conflating them is how good-vs-bad evaluation gets skipped.

## The capture → review gate

Every new note starts at **`verdict/unevaluated`**. That's the protection against rubber-
stamping: an unevaluated note is *captured, not blessed*. The review step is where we
actually decide good/bad, and a note isn't "done" until it leaves `unevaluated`.

To see what still owes a review, search the tag `verdict/unevaluated` (Obsidian tag pane,
or `grep -rl "verdict/unevaluated" docs/notes`). That list should be worked down, not let
to pile up.

## Workflow: mine → report → appraise → commit

1. **Mine** — pull patterns from a source into atomic notes, in **small batches** (~3–5,
   one source-area at a time). Descriptive only; tag `verdict/unevaluated`. Big sweeps get
   rubber-stamped — keep batches small so review keeps pace.
2. **Report** — surface the fresh batch back for review (the index makes this easy).
3. **Appraise** — the protected step. **Interview-first:** let the user think out loud and
   surface their read *before* any verdict is proposed — we won't always be in sync, and
   anchoring them early hides that. Only once they've processed does the assistant give its
   own verdict **plus honest pushback / constructive criticism** (this matters more as the
   system grows). Then assign each note a `verdict/` with a one-line *why*. `undecided` is a
   legitimate verdict; `unevaluated` is not a resting state. Capture disagreements as
   `kind/question` notes.
4. **Commit** — git-commit the batch once verdicts are recorded.

## Lifecycle: note → theme → roadmap

1. **Capture** — atomic note in `notes/`, tagged, `verdict/unevaluated`. Don't polish.
2. **Appraise** — assign a verdict (see workflow above). This is the good-vs-bad call.
3. **Cluster** — when several notes share a `theme/`, that theme is real. Promote it to a
   synthesis doc in `themes/` that pulls the thread together.
4. **Decide** — synthesis surfaces choices; capture them as `kind/decision` notes.
5. **Sequence** — adopted/adapted material and decisions feed `ROADMAP.md`. Roadmap is the
   *last* artifact, not the first. We are nowhere near it yet.
