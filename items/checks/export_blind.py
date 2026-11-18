#!/usr/bin/env python3
"""Export blind-run input for a batch of G5V1 items.

Usage:
    python3 items/checks/export_blind.py <batch> <start> <end>
    e.g. python3 items/checks/export_blind.py B01 47 67

Writes items/answers/<batch>/blind.json containing ONLY id / task / figure.
Author drafts and original YAML answers must never be included.
"""
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
ITEMS = ROOT / "items" / "sujiao-g5-vol1.yaml"
OUT_DIR = ROOT / "items" / "answers"


def main():
    if len(sys.argv) != 4:
        sys.exit("usage: export_blind.py <batch> <start> <end>")
    batch, start, end = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])

    with ITEMS.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)

    picked = []
    for it in data["items"]:
        num = int(str(it["id"]).split("-")[1])
        if start <= num <= end:
            picked.append({"id": it["id"], "task": it["task"], "figure": it.get("figure")})

    if len(picked) != end - start + 1:
        sys.exit(f"expected {end - start + 1} items, found {len(picked)} in {start}-{end}")

    out_dir = OUT_DIR / batch
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "blind.json"
    with out.open("w", encoding="utf-8") as f:
        json.dump(picked, f, ensure_ascii=False, indent=2)
    print(f"wrote {out} ({len(picked)} items)")


if __name__ == "__main__":
    main()
