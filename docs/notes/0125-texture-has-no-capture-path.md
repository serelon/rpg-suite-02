---
tags:
  - kind/observation
  - source/solorpg
  - source/conversation
  - theme/voice-and-register
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-24
---

# Texture has no capture path — the memory system selects for weight

**What it is.** A gap in the memory system (`rpg-tools` `memories` + the solorpg
post-process → memories pipeline — one system). It captures memories that carry **weight**
— consequential, resonant, emotionally/narratively load-bearing beats. But there's a whole
category it has no home for: **low-weight texture** — the *standing, memorable, minor*
details of a world. How a uniform looks. A dead-drop procedure. The brand of cigarettes a
contact smokes. Individually inconsequential; collectively, what makes a world feel
*lived-in* rather than merely tracked.

The diagnosis is precise: **it's a prompting gap, not a storage gap.** The schema could
hold these fine. But the extraction *prompt* asks "what mattered **most**?" — so texture
never gets surfaced. We prompt for the peaks; texture is the grain, and the grain falls
through.

**Two kinds of texture, same gap.** Not just *world* texture (how a uniform looks, a
dead-drop procedure) but **mechanical texture** — the *rendering contract* for a mechanical
object. A specific weapon has a mechanical layer (stats), but *"how this weapon should be
**written** when it's used"* is a distinct, capturable thing. Without it, the GM
re-improvises an interpretation every time the weapon appears → exactly the drift the system
exists to prevent. This is the **prose layer of [[0106-three-layer-character-record]]**
applied beyond characters: mechanical (stats) + semantic (interpretation contract) + prose
(how it reads). Leaving the prose layer to live-improv is the same failure mode as Tarot's
missing semantic layer ([[0105]]) — under-specified, so it decays into whatever the GM
guesses that session.

*Selection rule (owner):* mechanical texture is needed **in proportion to how invented the
thing is.** Contemporary/known objects (a Glock, a leather jacket) carry a stable shared
referent in the model — leave them as-is, the renders already converge. **Fantasy/sci-fi**
objects have *no external anchor*, so every appearance re-invents look-and-feel → drift.
The fictional-er the object, the more it needs a captured rendering contract. (Same logic
as [[0013]] name-the-default: where the model has no strong shared prior, you must supply
the anchor or it improvises one and wanders.)

**Where it comes from.** Confirmed against the live prompts:
- `solorpg/prompts/memory-extraction-guide.md` — *"Focus on what has weight/resonance"*;
  *"Memories should be selective, not comprehensive"*; substance floor *"usually 100+
  words."* Weight-selecting top to bottom.
- The `sensory` type **looks** like the home for this but isn't: it's for atmosphere that
  defines a place/moment *emotionally* (1–2 evocative paragraphs — "the silence of the
  frozen valley returns to her"). Texture facts aren't evocative *moments*; they're short,
  reusable, standing facts. Filtered out twice: once for weight, once for not-being-a-moment.

**Why it matters for next-gen.** Two distinct payoffs, both real:
1. **Richness** — texture is what lets the GM render a world densely and specifically
   instead of generically. It can be *just as load-bearing* as a plot beat — it's load
   bearing for *immersion* rather than for *plot*.
2. **Consistency** — once established, the uniform must look the same in session 30 as in
   session 3; the dead-drop procedure must not silently mutate. Texture that isn't captured
   can't be held stable, and uncaptured texture is exactly where drift hides.

So the axis the system is missing isn't fact-vs-feeling — it's **load-bearing-for-plot vs
load-bearing-for-world**. Both deserve capture; only the first has a path.

**Owner notes (2026-06-24).** Two clarifications that sharpen the gap:
- This isn't a *theoretical* gap — **memories are *supposed* to catch this texture and in
  practice aren't.** So [[0030]]'s "texture evicted to memories" isn't wrong in *intent*;
  the escape valve exists but **leaks** — the design says memories hold texture, the prompt
  doesn't actually pull it. A live failure, not a missing-by-design hole.
- The texture-bank link ([[0055]]) is **very close** — *"bigger chunks of the same thing."*
  The line between *memory* and *texture bank* is **expected to be blurry**, and that
  blur is itself a **design-time** question (flagged, not resolved here). Working
  distinction: **memory-texture = larger, more specific chunks**; texture-bank entries =
  smaller. Same substance, different granularity — likely one spectrum, not two artifacts.

**Open threads.**
- **[[0030-summary-as-compression]]**: the valve leaks (above) — reconcile at design time
  whether texture *is* a memory, a texture-bank entry, or a point on a shared granularity
  spectrum spanning both.
- **[[0055-register-anchor-banks]]** / **[[0107-prose-deprecation-doctrine]]** (keep prose
  where it's the *payload*: voice/appearance/texture): if memory-texture and texture-bank
  are the same substance at different sizes, the open question flips from *"same or
  sibling?"* to *"where's the granularity cut, and is it even a hard line?"* (Earlier guess
  — bank = how the world *sounds*, memory = how it *looks/works in small* — may be too
  clean; the blur suggests one continuum.)
- Does this want a **new memory type** (`texture`?), a **separate store**, or a **second
  extraction pass** that explicitly hunts the minor? (A weight-selecting pass and a
  texture-sweeping pass have opposite instincts — hard to do well in one prompt. Echoes the
  writer-never-does-bookkeeping split, [[0082]].)
- Capture is only half: texture also needs a **recall/injection** path (consistency only
  pays off if the established detail comes back at the right moment). Whose job — librarian
  ([[0075]]), JIT compiler, RAG index ([[0098]])?
- **[[0118-encoding-by-data-type]]** lens: is texture tacit (→ exemplar/prose) or factual
  (→ structured record)? A uniform's look might be *both* — a structured fact with a prose
  rendering.

**Verdict.** _(unevaluated — captured at the user's prompt; appraise with the
voice-register / memory-system cluster.)_
