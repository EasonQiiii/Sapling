#!/usr/bin/env python3
"""Validate items/sujiao-g5-vol1.yaml against the frozen primary spine.

Checks:
  1. Item IDs are unique and follow G5V1-NNN (textbook) or G5V1-SNNN (self-authored test items).
  2. Every kp_main / kp_other ID exists in knowledge-spine/小学/数学/*.yaml.
  3. kp_main is not a CAP id (capabilities are not KP targets).
  4. thinking is one of the five allowed levels, or null exactly when kp_main is null.
  5. kp_main null => kp_reason present.
  6. figure / answer have a valid shape (type in points/heights/table, or null).
  7. Items are in textbook order (unit order, then page non-decreasing within a unit).
  8. Duplicate task text (warning only).
  9. If dd_main is present, it must be a diagnostic_dimensions key of kp_main
     (spine DD id when the facet has id; otherwise the exact Chinese string).
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
ITEMS = ROOT / "items" / "sujiao-g5-vol1.yaml"
SPINE_DIR = ROOT / "knowledge-spine" / "小学" / "数学"

THINKING_LEVELS = {
    "认出来就做",
    "按步骤做",
    "先选方法或先把情境翻译成数学关系",
    "还要说明理由",
    "自己把几个关系串起来",
}
FIGURE_TYPES = {"points", "heights", "table"}


def collect_spine_ids():
    """Return (kp_ids, cap_ids, retired_ids, kp_dd_keys).

    kp_dd_keys maps KP id -> set of allowed dd_main values:
      - DD object with id  -> the id string
      - DD plain string    -> the string itself
    retired_ids are legacy IDs listed under id_management.legacy_id_handling
    (e.g. A3-06 alias -> A2-06, A2-07 reclassified to CAP-01). They must not be
    used as KP targets.
    """
    kp_ids, cap_ids, retired_ids = set(), set(), set()
    kp_dd_keys = {}

    def walk(node):
        if isinstance(node, dict):
            _id = node.get("id")
            if isinstance(_id, str):
                if "CAP" in _id:
                    cap_ids.add(_id)
                elif re.fullmatch(r"[A-D]\d-\d{2}", _id) and (
                    "learning_objectives" in node or "definition" in node
                ):
                    # KP nodes carry a definition / learning_objectives body.
                    # Legacy_id_handling entries (id + action only) are not KPs.
                    kp_ids.add(_id)
                    keys = set()
                    for d in node.get("diagnostic_dimensions") or []:
                        if isinstance(d, dict) and isinstance(d.get("id"), str):
                            keys.add(d["id"])
                        elif isinstance(d, str):
                            keys.add(d)
                    kp_dd_keys[_id] = keys
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    for path in sorted(SPINE_DIR.glob("*.yaml")):
        with path.open(encoding="utf-8") as f:
            doc = yaml.safe_load(f)
        walk(doc)
        for entry in (doc.get("id_management", {}) or {}).get("legacy_id_handling", []) or []:
            # action "retain" = still a live KP id; anything else (alias, reclassified,
            # deprecated, merged, ...) must not be used as a KP target.
            if isinstance(entry, dict) and isinstance(entry.get("id"), str):
                if entry.get("action") != "retain":
                    retired_ids.add(entry["id"])
    return kp_ids, cap_ids, retired_ids, kp_dd_keys


def check_shape(label, obj, errors, item_id):
    # figure / answer may be null, a structured points/heights/table object,
    # or (answer only) a plain-text string per items/README.md.
    if obj is None:
        return
    if label == "answer" and isinstance(obj, str):
        return
    if not isinstance(obj, dict):
        errors.append(f"{item_id}: {label} is not a mapping, string, or null")
        return
    t = obj.get("type")
    if t is not None and t not in FIGURE_TYPES:
        errors.append(f"{item_id}: {label}.type={t!r} not in {sorted(FIGURE_TYPES)}")


def main():
    argv = sys.argv[1:]
    # Optional: only items up to this id number are expected to have answers filled.
    # While a fill campaign is in progress, pass the highest completed number
    # (e.g. `validate_g5v1.py 67`) so pending items do not trip check 6b.
    filled_through = None
    if argv and argv[0].isdigit():
        filled_through = int(argv[0])

    with ITEMS.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    items = data["items"]

    kp_ids, cap_ids, retired_ids, kp_dd_keys = collect_spine_ids()
    known = kp_ids
    errors, warnings = [], []
    dd_filled = 0

    seen = set()
    for it in items:
        iid = it.get("id")
        if not re.fullmatch(r"G5V1-(\d{3}|S\d{3})", str(iid)):
            errors.append(f"bad id format: {iid}")
        if iid in seen:
            errors.append(f"duplicate id: {iid}")
        seen.add(iid)

        kp_main = it.get("kp_main")
        kp_other = it.get("kp_other") or []
        thinking = it.get("thinking")
        dd_main = it.get("dd_main")

        # 2 & 3: KP references
        for kp in ([kp_main] if kp_main else []) + list(kp_other):
            if kp in cap_ids:
                errors.append(f"{iid}: references CAP id {kp} (not a KP target)")
            elif kp in retired_ids:
                errors.append(f"{iid}: references retired/legacy id {kp}")
            elif kp not in known:
                errors.append(f"{iid}: unknown KP id {kp}")

        # 4 & 5: thinking / kp_reason consistency
        if kp_main is None:
            if thinking is not None:
                errors.append(f"{iid}: kp_main is null but thinking={thinking!r}")
            if not it.get("kp_reason"):
                errors.append(f"{iid}: kp_main is null but kp_reason is missing")
            if dd_main is not None:
                errors.append(f"{iid}: kp_main is null but dd_main={dd_main!r}")
        else:
            if thinking not in THINKING_LEVELS:
                errors.append(f"{iid}: invalid thinking {thinking!r}")

        # 9: dd_main optional; when present must belong to kp_main's facets
        if dd_main is not None:
            dd_filled += 1
            if not isinstance(dd_main, str) or not dd_main.strip():
                errors.append(f"{iid}: dd_main must be a non-empty string")
            elif kp_main is not None:
                allowed = kp_dd_keys.get(kp_main) or set()
                if dd_main not in allowed:
                    errors.append(
                        f"{iid}: dd_main={dd_main!r} not in diagnostic_dimensions of {kp_main}"
                    )

        # 6: figure / answer shape
        check_shape("figure", it.get("figure"), errors, iid)
        check_shape("answer", it.get("answer"), errors, iid)

        # 6a: when both figure and answer are structured, their type must match.
        fig, ans = it.get("figure"), it.get("answer")
        if isinstance(fig, dict) and isinstance(ans, dict):
            ft, at = fig.get("type"), ans.get("type")
            if ft is not None and at is not None and ft != at:
                errors.append(f"{iid}: figure.type={ft!r} != answer.type={at!r}")

        # 6b: answer null => answer_note must be non-empty (for filled items only
        # while the fill campaign is in progress; unconditionally without the arg).
        suffix = str(iid).split("-")[1]
        is_self = suffix.startswith("S")
        num = 0 if is_self else int(suffix)
        if is_self or filled_through is None or num <= filled_through:
            if ans is None and not (it.get("answer_note") or "").strip():
                errors.append(f"{iid}: answer is null but answer_note is empty")

    # 7: textbook order
    unit_order = []
    prev_unit, prev_page = None, -1
    for it in items:
        src = it.get("source", {})
        if src.get("origin") == "self":
            continue  # self-authored test items have no textbook position
        unit = src.get("unit")
        page = src.get("page")
        if unit != prev_unit:
            if unit in unit_order:
                warnings.append(f"{it['id']}: unit {unit!r} reappears (non-contiguous)")
            unit_order.append(unit)
            prev_unit, prev_page = unit, -1
        if isinstance(page, int):
            if page < prev_page:
                warnings.append(f"{it['id']}: page {page} < previous page {prev_page} in {unit}")
            prev_page = page

    # 8: duplicate task text
    tasks = {}
    for it in items:
        tasks.setdefault(it.get("task", ""), []).append(it["id"])
    for task, ids in tasks.items():
        if len(ids) > 1:
            warnings.append(f"duplicate task text across {ids}")

    print(f"items: {len(items)}  unique ids: {len(seen)}")
    print(f"spine KP ids: {len(kp_ids)}  CAP ids: {len(cap_ids)}  retired: {len(retired_ids)}")
    print(f"dd_main filled: {dd_filled}")
    print(f"errors: {len(errors)}  warnings: {len(warnings)}")
    for e in errors:
        print("ERROR  ", e)
    for w in warnings:
        print("WARN   ", w)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
