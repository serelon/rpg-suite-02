---
tags:
  - kind/pattern
  - source/solorpg
  - theme/composition
  - theme/docs-as-code
  - theme/packaging
  - theme/architecture
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Bundle templates — a working declarative composition system

**What it is.** `solorpg`'s `tools/bundle.py` assembles a session package **declaratively**
from layered JSON templates. The mechanisms (all real, in use):
- **Inheritance** — a template `extends` a parent (base → branch), forming a chain.
- **Multi-chain merge** — `templates: [...]` grafts *additional, orthogonal* chains alongside
  the `extends` chain (e.g. a branch pulls in a **subsetting** template:
  `"templates": ["../../bundles/caldworth.json"]`). This enables **swappable sub-settings
  without rigid single-parent ancestry** — composition by layering+grafting.
- **Declarative includes** — glob `src → dest` file selection (`characters/**/*.json` →
  `characters/`); content choice is *data*, not code.
- **Composable briefing** — named `briefing_blocks` (prose fragments) + `briefing_data`
  (params), assembled into `briefing.md`, with parameter expansion (`{session}`,
  `{pov_character}`).
- **Automatic reference-following** — include a character and `bundle.py` scans for and pulls
  in the characters/memories it references (`scan_available_entities`).

**Where it comes from.** `solorpg/tools/bundle.py` + real template
`campaigns/emberfall/branches/frieda/bundle-template.json`.

**Why it matters for next-gen.** (User: "synergizes with `0024` and `0036`.") This is the
**missing assembly layer** between *modules exist* ([[0024-pluggable-extension-modules]],
[[0036-every-subsystem-is-a-module]]) and *a running session* — a working prototype of
[[0010-docs-as-code-context-compiler]] for **content**. Two parts map directly onto the module
system: **multi-chain merge** is module-composition (assemble a session from independent
contributing chains — base + subsetting + branch + …, i.e. modules contributing templates),
and **reference-following** is the [[0036]] *refer-back* contract made operational — cross-
module dependencies resolved at build time, not copied. It partially answers
[[0034-outgrown-scaffold]]'s "declare a need, the system binds": you declare `extends`/
`include`, the builder resolves.

**Open threads.** It composes *content/data* — does the *same* mechanism compose **skills/
modules** ([[0037-rpg-tools-modularization]]'s open question)? Deep inheritance strains
(the-silence's 4–5 levels, [[0027-recurring-exception-taxonomy]]) — does multi-chain merge
scale or tangle? Is the template the seam where a **module registers what it contributes** to a
session? Relationship to rpg-tools' simpler `build-skill.sh` packaging.
