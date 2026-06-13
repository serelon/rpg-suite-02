---
tags:
  - kind/design-note
  - source/solorpg
  - theme/corpus-building
  - theme/architecture
  - maturity/proven
  - verdict/unevaluated
origin: ../solorpg/imports/EXPORT-STRUCTURE-MAP.md (the user's own census/mapping, authored in solorpg)
atomized-into: "feeds 0064 (measured); companion to [[import-design-brief]]"
created: 2026-06-13
---

> **Preserved primary source.** Empirical census + format map of a 2-year Claude Desktop
> export (1,201 conversations / 108,404 messages / 31 projects) — the measured grounding for
> [[0064-unharvested-archive]]. Companion to the design thinking in [[import-design-brief]].
> Verbatim below.

# Claude Desktop Export — Structure Map & Import Plan

Source: `imports/claude desktop export 2026-06-12.zip` (116 MB zipped, ~531 MB unzipped)
Account: Therese (`serelon@gmail.com`, account uuid `a4cd92fd-31c8-418b-8367-751412ff235e`)
Mapped: 2026-06-13

---

## 1. Top-level archive layout

| Member | Size | Type | Notes |
|--------|------|------|-------|
| `users.json` | 153 B | array[1] | Single account record |
| `memories.json` | 95 KB | array[1] | One object: account-level + per-project memory text |
| `projects/<uuid>.json` | 0.3–244 KB | object | 31 files — project metadata + knowledge docs |
| `conversations.json` | **529 MB** | array | **1,201 conversations, 108,404 messages** |

No binary blobs are stored. Image/PDF/file *bytes* are NOT in the export (see §5).

---

## 2. `users.json`
```json
[{"uuid","full_name","email_address","verified_phone_number"}]
```

## 3. `memories.json`  (single-element array → object)
```json
[{
  "conversations_memory": "<markdown blob — account-wide memory>",
  "project_memories": { "<project-uuid>": "<markdown blob>", ... },  // 16 entries
  "account_uuid": "..."
}]
```
- `project_memories` keys are **project UUIDs** matching `projects/<uuid>.json`.
- 16 of 31 projects have memory text; the other 15 do not.

## 4. `projects/<uuid>.json`
```json
{
  "uuid","name","description","is_private","is_starter_project",
  "prompt_template","created_at","updated_at",
  "creator": {"uuid","full_name"},
  "docs": [ {"uuid","filename","content","created_at"}, ... ]
}
```
- **31 projects**: 22 carry docs (250 docs total), 9 are empty stubs.
- `docs[].content` is full text (markdown/plain). This is project knowledge, not chat.
- Doc-count leaders: Threads of Berlin (44), Aetherpunk Academy (41), Storytelling (20),
  Throne of Stars (19), Writing Project A / Tarot Tales / Queen of Darkness (15 each).
- RPG-relevant projects present: The Long Watch (6), The Great Awakening (8),
  Buried Light (1), wuxia campaign (3), Threads of Berlin (44), Aurora, Solargene, etc.

## 5. `conversations.json`  (the 529 MB array)

Element schema:
```json
{
  "uuid","name","summary","created_at","updated_at",
  "account": {"uuid"},
  "chat_messages": [ {
      "uuid","text","sender",            // sender ∈ {human, assistant}
      "content": [ {                      // structured blocks; text lives here too
          "start_timestamp","stop_timestamp","flags","type","text","citations"
      } ],
      "created_at","updated_at",
      "attachments": [ {"file_name","file_size","file_type","extracted_content"} ],
      "files":       [ {"file_uuid","file_name"} ],
      "parent_message_uuid"
  } ]
}
```

Census (full streaming pass):
- **1,201 conversations**, **108,404 messages**
- Date range: **2024-05-14 → 2026-06-12** (~2 years)
- Per-conversation JSON size: min 247 B / median 129 KB / max **6.0 MB**
- Longest threads: "Unlikely noble sidestory concept" (1,706 msgs),
  "The Long Watch Session 60 - Michi" (1,023), "Lone consciousness on an alien world" (993),
  "Buried Light S01E01" (889), "Silence campaign session 04 briefing" (880).

### Critical format notes
- **`text` vs `content`:** Each message has a flat `text` field AND a `content[]` block list.
  For plain text they duplicate; `content[]` is the authoritative structured form (it carries
  block `type`, timestamps, citations). A robust importer should walk `content[]` and fall back
  to `text`.
- **`attachments[]` carry inline `extracted_content`** — the *text* of uploaded files is preserved
  (1,399 attachments total). Usable for import.
- **`files[]` are bare references** (`file_uuid` + `file_name` only, 1,774 total). The actual
  bytes (images, binaries, original uploads) are **absent from the export**. Anything that was a
  non-text upload is unrecoverable from this archive — only the filename survives.
- **No project linkage in conversations.** A conversation object has no `project_uuid`. Mapping a
  chat back to its project must be done heuristically (name match, date, memory cross-ref) or is
  not possible from the export alone.

---

## 6. Working files created during mapping

- `imports/extracted/` — `users.json`, `memories.json`, `projects/*` unzipped (~3 MB, safe to keep).
  `conversations.json` was deliberately NOT extracted (529 MB).

---

## 7. Import / processing plan

Goal: get this archive's RPG-relevant content into the `solorpg` pipeline without drowning in the
non-RPG bulk, and without ever loading the 529 MB file whole.

### Phase 0 — Index (cheap, do first)
Build a lightweight `conversations-index.json`: one row per conversation
`{uuid, name, created_at, updated_at, msg_count, byte_size, first_human_text[:200]}`.
Produced by one streaming pass (the §5 script is the basis). ~1,201 rows — fits in context, lets us
triage by name/date without re-reading the monster.

### Phase 1 — Classify & route
From the index, bucket conversations:
- **Campaign sessions** (existing `solorpg` campaigns: Long Watch, Great Awakening, Buried Light,
  wuxia, etc.) → candidates for the existing `session-postprocess` pipeline.
- **Dormant/unported campaigns** (Threads of Berlin, Aetherpunk Academy, Throne of Stars,
  Aurora, Solargene…) → revival/porting candidates (cf. Berlin workshop in MEMORY.md).
- **One-off / non-RPG** (LLM stuff, tooling chats) → archive, low priority.
Name-prefix patterns ("Long watch campaign session NN", "<Campaign> S01E01") make most of this
mechanical.

### Phase 2 — Per-conversation extraction
For each conversation worth keeping, stream-extract it to its own file
(`imports/conversations/<uuid>--<slug>.jsonl` or preprocessed markdown). Reuse
`tools/preprocess_export.py` shape (strip to human/assistant text, chunk ~20k tokens) so existing
session-postprocess tooling consumes it directly. NB: this export's per-message schema differs from
the `.jsonl` export format preprocess_export expects — a small adapter (content[]→text flattening)
is needed first. **Implement the adapter into the tool, don't one-off it** (per repo feedback).

### Phase 3 — Project docs
`projects/*.json` docs are already clean text. For ported campaigns, project docs + `project_memories`
blob = the worldbook/reference layer. Map each relevant project → its campaign folder's `reference/`.

### Phase 4 — Memories
`project_memories[uuid]` and `conversations_memory` are Claude-authored summaries — useful as
campaign "what Claude remembered" seeds, but they are prose blobs, not the structured memory JSON
the `memories.py` tool uses. Treat as source material for hand/agent extraction, not direct import.

### Open decisions (for Therese)
1. Scope: port everything RPG, or only the campaigns already live in `solorpg`?
2. Lost binaries: do any `files[]` references (images/maps) matter enough to hunt for originals
   elsewhere, or accept text-only?
3. Destination: new per-campaign `imports/` subfolders, or a single staging area first?
