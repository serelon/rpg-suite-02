---
tags:
  - kind/idea
  - source/conversation
  - theme/architecture
  - maturity/speculative
  - verdict/unevaluated
created: 2026-06-06
---

# Spreadsheet semantics as a tool-data shape — tables, recalc, rendered views

**What it is.** Design sketch from the [[0086-faction-as-character-economy]] discussion
(2026-06-06): the economy module's real need is *spreadsheet semantics* — and the user's
challenge ("thats challenging to integrate in an agentic flow..") decomposes cleanly:

1. **Tabular, human-legible state → CSV.** Plain text: agents read/write natively, git
   diffs it, double-click-opens in Excel/LibreOffice, stdlib `csv`, zero deps. Mutations
   are [[0073-structured-mutation-beats-rewrite]]-shaped by nature: append row, patch
   cell, never regenerate.
2. **Derived values → a small recalc tool, not a formula engine.** Formulas live in
   *code* (`economy.py recalc` style — auditable, versioned, reviewable); data lives in
   *tables*. Deliberately better than in-cell formulas, which are invisible logic — the
   exact illegibility that mothballed the original module (0086's failure mode).
3. **Visualization → a generated HTML view.** "spreadsheets are also a great
   visualisation layer" (user) — served by a *render*: recalc emits an HTML report
   (tables/balances/charts, no deps). Precedent is established in-house: **cheatsheets
   are widespread across branches and there's a dedicated `cheatsheet` skill to generate
   them** (user correction — not just sophie's one-off). Generated-HTML-view-of-campaign-
   state is already a proven, skill-backed pattern; this extends it to mechanical state.
   [[0056-files-as-build-products]] again — the pretty view is a build
   product, never the source of truth. Unicorn-era: same render as a widget pane
   ([[0082-live-hook-pipeline]]).

**Three audiences, one canonical table:** agent edits CSV; human eyeballs HTML or opens
the CSV in LibreOffice; tool computes between them. xlsx rejected (breaks stdlib-only,
agent-clumsy).

**Known trade:** no live in-cell formulas when the human edits directly — accepted in
exchange for formulas-as-reviewable-code.

**Why it matters for next-gen.** Generalizes past faction economy: any "crunch matters"
campaign state (aegis's strategic resources, [[0083-data-type-census]]'s mechanical-state
genre) could be instances of one **campaign-spreadsheet tool-data type** — per
[[0085-knowledge-entries-vs-tool-data]], module-owned, output-snippets-only into context.
One capability, many templates, instead of a bespoke schema per mechanical subsystem.

**Open threads.** Does recalc run as a hook (0082) so the HTML view stays live during
play? Schema-per-template: who defines a new table's columns (the workshop? the module)?
Does aegis's strategic.json migrate to this shape if aegis ever revives? CSV's weakness
is nested data — where's the boundary between "this is a table" and "this is a JSON/page"?

**Verdict.** _(unevaluated.)_
