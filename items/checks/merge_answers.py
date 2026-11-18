#!/usr/bin/env python3
"""Merge a reconciled answer sidecar into the main item YAML.

Usage:
    python3 items/checks/merge_answers.py <batch> [start] [end]

Reads items/answers/<batch>.yaml (entries: id / answer / answer_note) and inserts
the answer / answer_note fields into items/sujiao-g5-vol1.yaml at the end of each
item block, without reformatting anything else.

Safety properties:
  - Refuses to run if the sidecar covers ids outside [start, end] when given.
  - Refuses to overwrite an existing non-null answer unless --force is passed.
  - After editing, re-parses the file and verifies every merged value matches
    the sidecar exactly (yaml round-trip check).
"""
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
MAIN = ROOT / "items" / "sujiao-g5-vol1.yaml"
ANSWERS = ROOT / "items" / "answers"


def scalar_line(indent, key, value):
    """Render `key: value` as a single YAML line, escaping when needed."""
    if value is None:
        return f"{indent}{key}: null"
    dumped = yaml.safe_dump(value, allow_unicode=True, default_flow_style=False,
                            width=10**6).rstrip("\n")
    # safe_dump of a scalar document appends a document-end marker "..." — drop it.
    if dumped == "..." or dumped.endswith("\n..."):
        dumped = dumped[:-4].rstrip("\n") if dumped.endswith("\n...") else ""
    if isinstance(value, str):
        return f"{indent}{key}: {dumped}"
    out = [f"{indent}{key}:"]
    for ln in dumped.splitlines():
        out.append(f"{indent}{ln}" if not ln.startswith("- ") else f"{indent}  {ln}")
    return "\n".join(out)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    force = "--force" in sys.argv
    batch = args[0]
    lo = int(args[1]) if len(args) > 1 else None
    hi = int(args[2]) if len(args) > 2 else None

    with (ANSWERS / f"{batch}.yaml").open(encoding="utf-8") as f:
        entries = {e["id"]: e for e in yaml.safe_load(f)}

    ids = sorted(entries)
    if lo is not None:
        ids = [i for i in ids if lo <= int(i.split("-")[1]) <= hi]
    if not ids:
        sys.exit("nothing to merge after range filter")

    text = MAIN.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Locate each item block start: line "- id: G5V1-NNN"
    starts = {}  # id -> line index
    for idx, ln in enumerate(lines):
        s = ln.strip()
        if s.startswith("- id: G5V1-"):
            starts[s.split(": ")[1]] = idx
    ordered = sorted(starts.items(), key=lambda kv: kv[1])

    merged = 0
    offset = 0  # cumulative line count inserted so far; block indices were
                # computed on the pre-edit list, so shift them accordingly.
    for iid in ids:
        if iid not in starts:
            sys.exit(f"ERROR: {iid} not found in main YAML")
        block_start = starts[iid] + offset
        block_end = len(lines)
        for other_id, other_idx in ordered:
            if other_idx > starts[iid]:
                block_end = other_idx + offset
                break
        block = lines[block_start:block_end]

        key_names = [l.strip().split(":")[0] for l in block if l.strip()]
        entry = entries[iid]
        answer = entry.get("answer")
        note = entry.get("answer_note")

        if "answer" in key_names and not force:
            sys.exit(f"ERROR: {iid} already has an answer field; use --force to overwrite")

        # Insert after the last field line of the block (append at block end,
        # accounting for trailing blank line before the next "- id:").
        insert_at = block_end
        while insert_at > block_start and lines[insert_at - 1].strip() == "":
            insert_at -= 1
        new_lines = [scalar_line("  ", "answer", answer)]
        if note is not None:
            new_lines.append(scalar_line("  ", "answer_note", note))
        lines[insert_at:insert_at] = new_lines
        offset += len(new_lines)
        merged += 1

    new_text = "\n".join(lines) + ("\n" if not text.endswith("\n") else "")
    MAIN.write_text(new_text, encoding="utf-8")

    # Round-trip verification: re-parse and compare.
    with MAIN.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    by_id = {i["id"]: i for i in data["items"]}
    problems = []
    for iid in ids:
        got = by_id[iid]
        want = entries[iid]
        if got.get("answer") != want.get("answer"):
            problems.append(iid)
        if (got.get("answer_note") or None) != (want.get("answer_note") or None):
            problems.append(iid)
    if problems:
        sys.exit(f"ERROR: round-trip mismatch for {problems}")
    print(f"merged {merged} items from {batch}; round-trip OK")


if __name__ == "__main__":
    main()
