---
tags:
  - kind/pattern
  - source/new
  - source/claude-desktop
  - source/solorpg
  - theme/architecture
  - theme/frontend-agnostic
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Layered separation: craft skill ⟂ mechanics module ⟂ tools ⟂ bundle data

**What it is.** The GM stack is deliberately split into independent layers, each owning one
concern:
- **Craft skill** ([[gm-skill]]) — *how to run a session* (conducting, voice, pacing). No
  mechanics, no campaign data.
- **Mechanics module** — resolution rules (when to roll, attempts vs. declared, crunch
  visibility). *Per-campaign, optional,* loaded from the bundle in prep — deliberately **not**
  in the craft skill, so resolution rules stay the bundle's to set.
- **Tools** (`rpg-tools`) — dice, names, oracles, character/state loading. Pure mechanism.
- **Bundle data** — the campaign's briefing, characters, modifiers, calibration.

The craft skill explicitly *defers* to tools and *conditionally loads* the module — "this
skill governs craft and conducting, not how to roll."

**Where it comes from.** [[gm-skill-SKILL]] §"Mechanics" + §"Invocation/Prep";
[[gm-skill-RATIONALE]] §"Play: mechanics". Echoes `solorpg`'s skill/agent/bundle split.

**Why it matters for next-gen.** A clean **separation-of-concerns spine** that keeps the
craft layer portable and campaign-agnostic while crunch lives in swappable modules. Directly
serves [[0004-frontend-agnostic-core]] (craft is frontend-portable; mechanics/data bind
per-context) and the docs-as-code compiler view ([[0010-docs-as-code-context-compiler]]) —
layers as composable build inputs. The "default tool must not flip narrative-first into
roll-first" guard (how-not-whether) is a sharp interface rule between craft and mechanics.

**Open threads.** Where exactly is the craft/mechanics seam for a *heavy-crunch* campaign
(e.g. `aegis-tools`' full rules engine as a "module")? Can a rules engine plug in as just
another module behind this interface? Is there a fifth layer (memory/knowledge) that wants
the same treatment?
