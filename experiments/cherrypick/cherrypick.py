#!/usr/bin/env python3
"""cherrypick.py — resolve a dotted path into an Obsidian vault and extract sub-data.

Usage:
    python cherrypick.py <vault-root> <dotted.path>

Path grammar:
    folder.folder.page              -> whole page
    folder.folder.page.section      -> one '## Section' body (slug-matched)
    folder.folder.page.@meta        -> all frontmatter (as JSON)
    folder.folder.page.@meta.key    -> one frontmatter value (as JSON)

Stdlib only. Pages stay 100% Obsidian-compliant markdown.
"""
import json
import re
import sys
from pathlib import Path


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def parse_frontmatter(text: str):
    """Minimal YAML-subset parser: scalars, inline lists, block lists."""
    if not text.startswith("---"):
        return {}, text
    head, _, body = text[3:].partition("\n---")
    meta, key = {}, None
    for line in head.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if re.match(r"\s+- ", line) and key:
            meta.setdefault(key, []).append(_scalar(line.split("- ", 1)[1]))
        elif ":" in line:
            key, _, val = line.partition(":")
            key, val = key.strip(), val.strip()
            if val == "":
                meta[key] = []          # block list follows (or empty)
            elif val.startswith("[") and val.endswith("]"):
                meta[key] = [_scalar(v) for v in val[1:-1].split(",") if v.strip()]
            else:
                meta[key] = _scalar(val)
    return meta, body


def _scalar(v: str):
    v = v.strip().strip('"').strip("'")
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    if re.fullmatch(r"-?\d+\.\d+", v):
        return float(v)
    return v


def split_sections(body: str):
    """Map slugged '## Heading' -> section body (up to next ## or EOF)."""
    sections = {}
    for m in re.finditer(r"^## (.+?)\s*$\n(.*?)(?=^## |\Z)", body, re.M | re.S):
        sections[slug(m.group(1))] = m.group(2).strip()
    return sections


def resolve(root: Path, dotted: str) -> str:
    parts = dotted.split(".")
    # walk folders until a part matches a page file
    current, i = root, 0
    while i < len(parts):
        page = current / f"{parts[i]}.md"
        if page.is_file():
            break
        nxt = current / parts[i]
        if not nxt.is_dir():
            raise SystemExit(f"not found: no folder or page '{parts[i]}' in {current}")
        current, i = nxt, i + 1
    else:
        raise SystemExit(f"path '{dotted}' never reached a page")

    meta, body = parse_frontmatter(page.read_text(encoding="utf-8"))
    rest = parts[i + 1:]

    if not rest:                                   # whole page
        return body.strip()
    if rest[0] == "@meta":                         # frontmatter access
        if len(rest) == 1:
            return json.dumps(meta, indent=2)
        if rest[1] not in meta:
            raise SystemExit(f"no frontmatter key '{rest[1]}' in {page.name}")
        return json.dumps(meta[rest[1]])
    if rest[-1] == "@json":                        # fenced json block in a section
        sections = split_sections(body)
        target = slug(".".join(rest[:-1]))
        if target not in sections:
            raise SystemExit(f"no section '{target}' in {page.name}")
        m = re.search(r"```json\s*\n(.*?)\n```", sections[target], re.S)
        if not m:
            raise SystemExit(f"no json block in section '{target}'")
        return json.dumps(json.loads(m.group(1)), indent=2)
    target = slug(".".join(rest))                  # section access
    sections = split_sections(body)
    if target not in sections:
        raise SystemExit(
            f"no section '{rest[0]}' in {page.name}; have: {', '.join(sections)}")
    return sections[target]


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    print(resolve(Path(sys.argv[1]), sys.argv[2]))
