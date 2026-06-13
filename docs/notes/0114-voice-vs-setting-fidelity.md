---
tags:
  - kind/pattern
  - source/conversation
  - theme/voice-register
  - theme/corpus-building
  - theme/local-finetuning
  - maturity/seed
  - verdict/adapt
created: 2026-06-13
---

# Voice and setting-fidelity are two different error classes — and different layers fix them

**What it is.** "Sails on a starship" is **not** a voice failure. The model knows *how* to
write; it grabs the wrong furniture because its prior drags "ship + travel" toward
age-of-sail before it reaches your canon. That's a **default-association** error, distinct
from a prose/cadence error. The two come apart cleanly:
- **Voice** (cadence, beat structure, tone) — taught by demonstration.
- **Setting-fidelity / idiom** (how ships move, what jump-travel *feels* like) — a matter
  of which way the probability mass leans at a fork.

The payoff: reshaping defaults is something fine-tuning does **better** than teaching
voice — so the jump/starship register is a high-value target, arguably *more* than voice
work, because it fixes the thing prompting keeps failing to suppress. But it changes how
you build that slice: it must be **contrastive** — heavy on the exact scenes where the
cliché *would* fire, rendered in the correct idiom. You're not just showing good scenes;
you're showing the model the fork and which way to take it.

**Where it comes from.** Inbox conversation [[Claude-export-custom-lora]] (2026-06-13):
even Opus "ends up putting sails on starships at times." The user has 5–10 distinct combat
registers and fuzzier non-combat ones (jump travel, starship-as-place).

**Why it matters for next-gen.** The split is a **diagnostic axis that generalizes past
fine-tuning**: when output is wrong, ask *which error class* — voice or default-association
— because they route to different fixes (exemplars/register banks vs contrastive
anchors + a banned-furniture list). It also argues for **discovering registers, not
enumerating them**: tag each scene with a freeform "what kind of scene is this," cluster,
and let the taxonomy fall out of actual play (combat self-splits into its real 5–10
sub-types; cliché-dominated clusters flag the "sails" hotspots). That's the mechanized
register-discovery the sample-book grid ([[0006-sample-book-grid]]) and wilderness survey
([[0110-wilderness-survey-idea-recovery]]) gesture at.

**Open threads.** The contrastive slice is exactly where a distill/rewrite step
([[0113-distill-dont-imitate]]) **betrays you**: a blind rewrite launders the cliché
straight into training data (the strong model sails-on-starships too). For this register
the rewrite prompt needs canon + an explicit banned-metaphor list, and QC checks one thing
above all — *did it sail again?* This is [[0076-self-canonizing-hallucinations]] in a new
guise: a self-check needs an **external referent** (the banned list / a canon file), never
its own output. Boundary with [[0115-lora-idiom-lorebook-facts]]: idiom is shiftable;
exact facts are not — don't ask the default-shifting mechanism to memorize numbers.

**Verdict.** _(2026-06-13.)_ **adapt** — the durable, consumer-agnostic half is the
**register/scene-type categorization** (discover-by-clustering; the user's "10 flavors of
combat"), which is just [[0006-sample-book-grid]]'s scene-type×register axes *discovered
from actual play* rather than pre-named. That feeds the sample book and texture bank
([[0055-register-anchor-banks]]) whether or not a fine-tune ever happens. The
voice-vs-default-association split rides along as a useful **diagnostic axis** (which error
class → which fix). Lift it out of the LoRA framing when building.
