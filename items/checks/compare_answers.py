#!/usr/bin/env python3
"""Compare Author sidecar answers with Verifier independent answers.

Usage:
    python3 items/checks/compare_answers.py <batch> [start] [end]

Reads:
    items/answers/<batch>.yaml          Author sidecar (id / answer / answer_note)
    items/answers/<batch>/independent.json  Verifier blind output

For each id, classifies both entries as:
    - null   : open / activity item (answer_note carries the standard)
    - numeric: answer contains numbers -> compare the multiset of key numbers
    - text   : no numbers (or prose conclusion) -> flag for manual review if
               normalized texts differ materially

Output: a per-item verdict list (MATCH / NUMERIC-MATCH / DIFF / REVIEW) written to
stdout, plus a summary. DIFF items need adjudication in reconcile.md.

This script does NOT read the main YAML; the original answer there (if any) is not
part of the reconciliation for batches B01+.
"""
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
ANSWERS = ROOT / "items" / "answers"


def numbers_in(text):
    """Extract numbers (ints and decimals) from a string answer."""
    if not isinstance(text, str):
        return []
    return [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", text.replace("，", ","))]


def round_clean(xs, tol=1e-9):
    return sorted(round(x, 6) for x in xs)


def classify(entry):
    a = entry.get("answer")
    if a is None:
        return "null"
    if isinstance(a, str):
        nums = numbers_in(a)
        if nums:
            return "numeric"
        return "text"
    return "structured"


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: compare_answers.py <batch> [start] [end]")
    batch = sys.argv[1]
    lo = int(sys.argv[2]) if len(sys.argv) > 2 else None
    hi = int(sys.argv[3]) if len(sys.argv) > 3 else None

    sidecar_path = ANSWERS / f"{batch}.yaml"
    indep_path = ANSWERS / batch / "independent.json"

    with sidecar_path.open(encoding="utf-8") as f:
        sidecar = {e["id"]: e for e in yaml.safe_load(f)}
    with indep_path.open(encoding="utf-8") as f:
        indep = {e["id"]: e for e in json.load(f)}

    ids = sorted(set(sidecar) | set(indep))
    if lo is not None:
        ids = [i for i in ids if lo <= int(i.split("-")[1]) <= hi]

    counts = {"MATCH": 0, "NUMERIC-MATCH": 0, "DIFF": 0, "MISSING": 0}
    diffs = []
    for iid in ids:
        s = sidecar.get(iid)
        v = indep.get(iid)
        if s is None or v is None:
            counts["MISSING"] += 1
            print(f"MISSING {iid}: sidecar={'yes' if s else 'no'} independent={'yes' if v else 'no'}")
            continue
        cs, cv = classify(s), classify(v)
        if cs != cv:
            counts["DIFF"] += 1
            diffs.append((iid, f"class mismatch: author={cs} verifier={cv}"))
            print(f"DIFF    {iid}: class mismatch author={cs} verifier={cv}")
            continue
        if cs == "null":
            counts["MATCH"] += 1
            sn = (s.get("answer_note") or "").strip()
            vn = (v.get("answer_note") or "").strip()
            if not sn:
                print(f"REVIEW  {iid}: author answer_note empty for open item")
            continue
        if cs == "numeric":
            sn, vn = round_clean(numbers_in(s["answer"])), round_clean(numbers_in(v["answer"]))
            if sn == vn:
                counts["NUMERIC-MATCH"] += 1
            else:
                counts["DIFF"] += 1
                diffs.append((iid, f"numbers differ: author={sn} verifier={vn}"))
                print(f"DIFF    {iid}: numbers author={sn} verifier={vn}")
        else:  # text
            counts["DIFF"] += 1
            diffs.append((iid, "text answers differ (manual review)"))
            print(f"REVIEW  {iid}: text answer — compare manually")
            print(f"    author   : {str(s.get('answer'))[:120]}")
            print(f"    verifier : {str(v.get('answer'))[:120]}")

    print()
    print(f"summary: {counts}")
    if diffs:
        print(f"{len(diffs)} item(s) need adjudication:")
        for iid, why in diffs:
            print(f"  {iid}: {why}")


if __name__ == "__main__":
    main()
