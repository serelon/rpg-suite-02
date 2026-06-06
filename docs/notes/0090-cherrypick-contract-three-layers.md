---
tags:
  - kind/decision
  - source/new
  - theme/architecture
  - theme/single-source-of-truth
  - theme/context-economy
  - maturity/seed
  - verdict/adopt
created: 2026-06-06
appraised: 2026-06-06
---

# The cherrypick contract — three layers, one Obsidian page (T7 resolved: go)

**What it is.** The KB theme doc's biggest open gate — *"can tools extract targeted
sub-data from vault pages while staying Obsidian-compliant?"* ([[knowledge-base-canonical-vault]]
soft list; tension T7 in [[STATE-OF-RESEARCH]]) — answered by working prototype
(`experiments/cherrypick/`, 2026-06-06). A ~100-line stdlib resolver addresses
`folder.folder.page.section` paths into a vanilla Obsidian page and extracts:

- `…page.section` → one `##` section body (slug-matched)
- `…page.@meta` / `…page.@meta.key` → frontmatter as typed JSON
- `…page.section.@json` → a fenced ```json block, parsed

**The contract — three layers per page, all vanilla Obsidian:**

| Layer | Holds | Obsidian sees | Tool gets |
|---|---|---|---|
| frontmatter | edges + hot scalars | Properties, graph edges, rename-refactor | typed JSON |
| ```json blocks | deep nested mechanical data | rendered code block | `json.loads`, full fidelity |
| `##` sections | freeform prose, zoom tiers | normal markdown | addressable text |

Rule of thumb: **relations/identity → frontmatter (Obsidian-alive); mechanical depth →
json block (tool-alive, Obsidian-inert); meaning → prose.** The user's framing: json/xml
blocks "reserve the .md stuff to freeform data." XML rejected absent a specific need —
JSON wins on stdlib ergonomics and prev-gen continuity.

**Edges-as-datastructs upgraded.** Obsidian Properties (~1.4+) support real internal
links in frontmatter — resolving, rename-refactoring, graph-visible. The PoC demonstrates
`operators: ["[[ragna]]", "[[freyke]]"]` extracting as clean JSON. User skepticism →
verify-in-vault → live evidence. (Caveat: wikilinks *inside* code blocks stay dead to
Obsidian — relations don't belong in json blocks.)

**Why it matters for next-gen.** With the cherrypick condition satisfied, Obsidian-compat
is **go** — the vault-is-canon thesis loses its biggest structural risk. The binding
constraint shifts to template discipline: stable frontmatter keys + a controlled section
vocabulary per page-type (section renames break addresses), which is exactly the
[[0085-knowledge-entries-vs-tool-data]] type-system work.

**Open threads.** Nested `###` addressing; frontmatter nesting rules ("flat-ish" spec?);
pretty-print/formatting polish; does the dotted-path grammar become the KB contract
surface ([[0069-one-knowledge-base-many-presentation-layers]]'s open question)? Obsidian
*plugins* as an extension lead (user, esp. for [[0087-spreadsheet-semantics-tool-data]]
rendering).

**Verdict.** adopt — prototype passed first try; contract ratified in review session
2026-06-06. The PoC artifact is the citation.
