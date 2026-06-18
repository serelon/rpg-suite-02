# Census: namesets — full inventory (agent sweep + tool ground-truth, 2026-06-15)

> Pass-two sweep of **every** nameset across the source repos, plus the namegen guide.
> Pass one ([[census-rpg-tools]], [[0084-rpg-tools-data-layer]], [[0085-knowledge-entries-vs-tool-data]])
> captured the **schema/system**; this captures the **inventory**, classified by *reusability*
> to feed the next-gen goal: **grow the core sets** by promoting campaign-buried building blocks.
>
> **This is a catalog, not a reorg proposal.** Reusability axes below are *observed properties*
> (real-world / era / species / genre / stratum / campaign-bound), not adopt/move verdicts. The
> actual core-vs-campaign reorganization is a later appraisal/decision step — born unevaluated.

## Method & ground truth

Authoritative source is the tool itself, run from the solorpg root so discovery sees
`campaigns/*/namesets/`:

```bash
python rpg-tools/scripts/namegen.py list --all            # grouped by namespace
python rpg-tools/scripts/namegen.py list --all --verbose   # + name/setting/desc/type/tags
```

**`namegen.py list` reports 193 namesets** — the count that matters. (151 *files* on disk:
30 core + 114 campaign + 6 examples + 1 shared; the file↔nameset gap is multi-nameset files
and the lumina-city generator stacks. Plus ~60 test fixtures under `rpg-tools/tests/`, **not**
inventoried here — they're validator fodder, not content.)

## Headline structural finding: the "core" is not a namespace, it's a polluted root

The 30 bundled defaults in `rpg-tools/tools/data/namesets/` carry **no namespace** → they land
in `(root)`. But so did **58 campaign-specific sets** whose authors never set a namespace. Result:
`(root)` holds **88 namesets**, only 30 of which are the intended shared core. The guide's
"Recommended Namespace Taxonomy" (era / species / genre / stratum / setting) **never manifested**
— confirmed live, not just in docs ([[census-rpg-tools]] flagged this; here it's quantified).

| Namespace | Count | What's actually in it |
|-----------|------:|-----------------------|
| `(root)` | 88 | **30 core defaults** + 58 campaign sets that defaulted to root (all aegis 1940s, all gladiators, solramis*, wasteland*, radiance civilians, era sets, wuxia, scottish-wartime, threadlight-spacer/colonies, heliodyne, kailani-names…) |
| `lumina-city` | 34 | handle/dj/doll/merc/street generator stacks (multi-nameset files) |
| `the-silence` | 18 | solramis*, eisrandi*, marennite*, narodnya*, etc. (invented cultures) |
| `longwatch` | 14 | *-evolved substrates + frontier/core-world/void-born aggregates |
| `asymptote` | 14 | corp-* org-name generators (corp-master-pool + 13) |
| `sutherlands-cairn` | 13 | moc-* houses + refugee strata + titles |
| `emberfall` | 10 | dwarves/elves/goblins/lizardfolk + invented cultures |
| `kailani` | 2 | ai-names, places (pale-horizon's set) |

Only **7 campaigns** adopted a namespace; ~9 dumped everything into root. So today there is no
clean boundary between "shared building block" and "campaign content" — both live in `(root)`.

---

## Inventory by reusability axis (observed property)

Axes are the guide's own dormant taxonomy. A set is a **core candidate** when its content is
real-world, era-generic, species-generic, or genre-archetypal — i.e. carries **no campaign-bound
invented proper nouns**. Campaign-bound = built around invented cultures/orgs/places.

### A. Already core — real-world cultural/geographic (30, in `tools/data/`)
The intended shared baseline. 21 leaf cultural sets + 9 aggregates.
- **Leaf (real cultures):** american, british, french, german, italian, spanish, polish,
  russian, ukrainian, chinese, japanese, korean, indian, pakistani, arabic, persian, turkish,
  nigerian, ethiopian, brazilian, mexican, vietnamese.
- **Aggregates:** `metropolitan-names` (20 sources — the `default` set), `names-western`,
  `names-african` (nigerian+ethiopian), `names-east-asian` (cn+jp+kr),
  `names-eastern-european` (ru+pl+uk), `names-latin-american`, `names-middle-eastern`,
  `names-south-asian`, `names-american` (as diverse aggregate).

### B. Era packs buried in campaigns — strongest core-candidate vein
Real-world historical names mis-filed under one campaign each. Map onto guide axis `era`.
- **1940s / WWII (13 sets, all in `aegis`, all in root):** names-american-1940s,
  -australian-1940s, -british-1940s, -canadian-1940s, -czech-1940s, -dutch-1940s,
  -french-1940s, -german-1940s, -italian-1940s, -japanese-1940s, -polish-1940s,
  -scandinavian-1940s, -soviet-1940s. (Plus `aegis-personnel`, a 13-source aggregate over them —
  *that* one is the campaign-flavored consumer.) An entire era pack hiding in a campaign.
- **Prehistoric (2, `the-eternal-witness`):** `ice-age-names` (paleolithic, 18–15k BCE),
  `early-neolithic-fertile-crescent` (~10–7k BCE). Era axis `bronze-age`/`paleolithic`.
- **Wartime Scottish (1, `timewalkers`):** `scottish-wartime`. Overlaps 1940s-British.
- **Historical Chinese (1, `where-mists-gather`):** `historical-chinese-names` — explicitly
  "historically plausible, common folk"; a generic historical-East-Asian leaf, not wuxia-bound.

### C. Species packs buried in `emberfall` — classic-fantasy core candidates
- `dwarves`, `elves`, `goblins`, `lizardfolk` — generic fantasy-species names. Map onto guide
  axis `species` (elven/dwarven/goblinoid/lizardfolk). Cross-setting reusable.
- *Campaign-bound siblings (NOT candidates):* arakessi, ibexin, korvathi, naimari,
  caldworth-city, humans-caldworth (invented Emberfall cultures/places).

### D. Genre-archetype packs (borderline — genre-core candidates)
Generic enough to reuse across settings of the same genre, but campaign-tinted.
- **Post-apoc (5, `rust-and-ruin`, root):** wasteland-commune, -trade, -wanderer, -warlord,
  wastelander. Archetype-named, not proper-noun-bound → genre axis `post-apoc`. (`askvargr` =
  the campaign's named free-company → campaign-bound.)
- **Modern civilian (5, `radiance`, root):** civilian-european/-japanese/-korean/-latinx-names
  + `civilian-names` aggregate. These are *near-duplicates of core leaves* (european≈western,
  japanese≈names-japanese) — redundancy worth flagging.
- **Sci-fi demographic substrates (`longwatch`):** african-/arabic-persian-/east-asian-/
  germanic-nordic-/pacific-oceanic-/slavic-/south-asian-evolved — real-world substrates
  *evolved* for far-future; frontier/core-world/void-born aggregates over them. Reusable as a
  sci-fi naming kit, but the "-evolved" styling is a setting choice.
- **Ancient-world by real culture (`blood-and-spectacle`, root):** gladiator-celtic, -germanic,
  -hellenic, -imperial(roman), -kemic(egyptian), -numidian, -thracian, -eastern(mesopotamian)
  are real ancient cultures (genre/era core candidates); gladiator-arena/-ludus/-patrician/
  -street/-katter are aggregates expressing arena social strata (campaign-shaped consumers).

### E. Generic utility
- `ultimate-cat-names-collection` (solorpg `tools/data/`, the only set in solorpg's own tools
  dir) — animal names, usable anywhere.

### F. Clearly campaign-bound (invented proper nouns — not core candidates)
- **the-silence (18):** solramis + 5 sub-variants, eisrandi + 4, marennite + 5, narodnya + 2,
  concordiate(+core), choir-of-stars, rathenmoor. The deepest `extends`/variant tree in the corpus.
- **lumina-city (34):** procedural *generator stacks* — handle-{dj,doll,merc,street,nouns},
  dj-{base,fused,single,stamp,suffix}, doll-{bright,edge,exotic,playful,soft},
  merc-{loan,noun,pair,the}, street-{loan,noun,nouns,pair,trait}, plus real ethnic leaves
  (malay, thai, indonesian, filipino, chinese-/indian-malaysian, asean-founding, luminan,
  minor-waves). The ethnic leaves are arguably core-adjacent; the handle generators are a
  *pattern* worth its own note (procedural-handle composition), not core content.
- **asymptote (14):** corp-* organization-name generators (megacorp, oligarch, pmc-*, sect,
  hyperscaler…) + corp-master-pool. Org-name *generators*, a distinct sub-genre from person-names.
- **sutherlands-cairn (13):** moc-* (Magistracy-of-Canopus-flavored) houses, refugee strata
  (african/hebrew/persian/sikh-punjabi/mixed), bishop-greek, highland, moc-titles.
- **threadlight (4):** heliodyne-general/-house (20- and 5-source aggregates), threadlight-spacer,
  threadlight-colonies. Setting-corp-bound.
- **kailani / pale-horizon (2):** ai-names, places.

---

## Trust / provenance column (owner walk + git, 2026-06-18)

Reusability ≠ usability. A set's *quality* (and even its true reusability) needs
**owner-validation** — git provenance is **blind to subagent content authorship** (the
`Co-Authored-By` trailer is the *orchestrator* model; names were often made by a delegated
**Haiku subagent**, so trailers say "Opus 4.5" on sets the owner knows are bad). Trust states:

| Set(s) | Origin (git) | Real provenance | Polished? | Trust (owner) |
|--------|--------------|-----------------|-----------|---------------|
| **core defaults** (30) | Jan/Apr 2026 | — | no | 🟢 **clean — owner's most-used set; the quality template** |
| **lumina-city** real-world leaves | May 2026 | Opus 4.7/4.8 | n/a | 🟢 clean (Opus, vouched) — SE-Asia leaves = the one real harvest |
| **rust-and-ruin** | — | Opus | n/a | 🟢 clean, but campaign-bound (leave) |
| **longwatch** substrates | Feb 2026 | Haiku subagent | yes (same-day) | 🔴 **"a mess"** — remediation didn't save it; write-off |
| **aegis 1940s** (13) | Dec 2025 | Haiku subagent | **never** | 🔴 suspect, unaudited — rebuild before promote |
| **emberfall** (incl. species) | Jan–Mar 2026 | — | no | ⛔ **setting-bound** (owner) — *not* core candidates despite generic-looking names |
| the-silence / sutherlands / asymptote / threadlight | — | mixed | no | setting-bound (leave) |

**Two corrections to this catalog's earlier inferences (§C, §A):**
- §C "species packs = core candidates" is **wrong** — emberfall's dwarves/elves/goblins/
  lizardfolk are setting-baked worldbuilding per the owner. The *demand* for generic species is
  real (see [[0119-core-namesets-by-demand]]); emberfall's *supply* is not the source.
- core (§A) is the **vouched** quality baseline, not merely "incumbent."

**Reusable audit tooling:** `polish_namesets.py`'s heuristics (dedup, English-word removal,
prefix/suffix-cluster trim, gibberish-block removal, length cap) *encode the Haiku failure
modes* — generalize them beyond their hardcoded longwatch paths for a corpus-wide audit.

**The pivot:** harvest is thin → grow-core is an **authoring** project, demand-driven and
supply-independent. Captured as [[0119-core-namesets-by-demand]].

## Patterns worth their own notes (flagged, not yet captured)

1. **Root-as-dumping-ground** — namespace discipline never adopted; 58/88 root sets are campaign
   content. The reorg's first lever: a real `core:` namespace vs explicit campaign namespaces.
2. **Era/species/genre veins map 1:1 onto the guide's dormant taxonomy** — the axes to grow the
   core into already exist on paper ([[census-rpg-tools]] version-skew); the content to fill them
   is already written, just mis-homed.
3. **Redundancy across the boundary** — radiance civilians ≈ core leaves; scottish-wartime ⊂
   1940s-british; gladiator real-culture leaves overlap potential ancient-era core. Promotion
   would need a dedupe pass.
4. **Generators ≠ namesets-of-people** — lumina handles, asymptote corps, specimen-designations
   are *procedural pattern* tools (random-pattern formats), a different sub-type from person-name
   rosters. Relevant to [[0087-spreadsheet-semantics-tool-data]] / tool-data typing.
5. **Aggregate = campaign-flavored consumer of reusable leaves** — recurring shape: real-world
   leaves stay generic, the per-campaign aggregate (aegis-personnel, gladiator-street,
   berlin-names, heliodyne-general, civilian-names) does the local demographic weighting. Clean
   seam for core(leaves)/campaign(aggregates) split.

## Cross-refs
[[census-rpg-tools]] · [[0084-rpg-tools-data-layer]] · [[0085-knowledge-entries-vs-tool-data]]
(namesets = tool data, complexity-is-free) · [[0013-counter-training-name-the-default]] (why
namegen exists) · [[0087-spreadsheet-semantics-tool-data]] (generator sub-type) ·
[[0083-data-type-census]] (namesets ~95% consistent, near-universal).
