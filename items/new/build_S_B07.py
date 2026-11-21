#!/usr/bin/env python3
"""Author drafts for self-authored test items, batch S-B07 (diagnostic-gap fill).

Scope: only KPs whose existing items cannot yet attribute a missing facet.
Each entry: (kp, task, answer, thinking, answer_note or None).
ID range: G5V1-S235 … G5V1-S240.
Output: items/new/S-B07.yaml (drafts only; not merged into the bank yet).

Also documents the in-place rewrite of G5V1-S158 (B5-07) question ③ —
that rewrite is applied to the main bank separately, not as a new ID.
"""
from pathlib import Path
import yaml

DRAFTS = [
    # ---- B1-01 字母表示数的意义 · generality（现有 S076 仅覆盖情境代入）
    ("B1-01",
     "一支铅笔 a 元。买 6 支要用多少元？用含字母 a 的式子表示。再分别算出 a = 2 和 a = 3 时各要多少元。",
     "6a 元。当 a = 2 时要 12 元；当 a = 3 时要 18 元。",
     "按步骤做",
     "完成标准：写出 6a（或 a×6）；并给出代入 2、3 的两个结果。"),
    # ---- B2-01 总量与分量关系 · unknown_part（现有题均为由分量求总量）
    ("B2-01",
     "图书馆有故事书 248 本，其中童话书 96 本，其余都是科幻书。科幻书有多少本？",
     "248 − 96 = 152（本）。",
     "按步骤做",
     None),
    # ---- B2-02 相差关系 · smaller_quantity（现有题均为求较大量）
    ("B2-02",
     "姐姐身高 148 厘米，比妹妹高 12 厘米。妹妹身高多少厘米？",
     "148 − 12 = 136（厘米）。",
     "认出来就做",
     None),
    # ---- B4-03 比与除法、分数的关系 · 除数与分母限制（现有 S124 仅覆盖对应转换）
    ("B4-03",
     "下面三个比，哪些可以写成除法算式和分数？请写出能写的除法算式和分数，并说明不能写的原因：① 4:5；② 7:0；③ 9:12。",
     "① 4÷5，分数 4/5。② 不能写：后项是 0，除数和分母都不能为 0。③ 9÷12，分数 9/12。",
     "还要说明理由",
     "完成标准：①③ 写出除法与分数；② 明确指出后项为 0 因而不能写。"),
    # ---- B5-02 正比例的意义 · 比值不恒定则不成正比例（现有题均为比值一定）
    ("B5-02",
     "两组量的对应情况是：x 取 2、3、4 时，y 分别是 6、12、10。y 与 x 成正比例吗？请写出各组的比值 y÷x，并说明判断依据。",
     "不成正比例。各组比值：6÷2=3，12÷3=4，10÷4=2.5，比值不恒定，所以不成正比例。",
     "还要说明理由",
     "判据只能是比值是否一定；不得以同向变化作依据。"),
    # ---- B5-05 反比例的意义 · 乘积不恒定则不成反比例（现有题均为乘积一定）
    ("B5-05",
     "两组量的对应情况是：x 取 2、3、4 时，y 分别是 12、10、6。y 与 x 成反比例吗？请写出各组的乘积 xy，并说明判断依据。",
     "不成反比例。各组乘积：2×12=24，3×10=30，4×6=24，乘积不恒定，所以不成反比例。",
     "还要说明理由",
     "判据只能是乘积是否一定；不得以反向变化作依据。"),
]

# In-place rewrite for G5V1-S158 question ③ (not a new ID).
S158_REWRITE = {
    "task": (
        "下列每组量成什么比例关系？请逐一判断并说明依据："
        "① 单价一定时，总价与数量；"
        "② 总价一定时，单价与数量；"
        "③ 两组量的对应情况是：x 取 2、3、5 时，y 分别是 8、15、20。"
    ),
    "answer": (
        "① 成正比例：总价 ÷ 数量 = 单价（一定）。"
        "② 成反比例：单价 × 数量 = 总价（一定）。"
        "③ 不成比例：各组比值 8÷2=4、15÷3=5、20÷5=4，乘积 2×8=16、3×15=45、5×20=100，"
        "比值与乘积都不恒定。"
    ),
}


def build(start_num=235, batch="S-B07"):
    items = []
    for n, (kp, task, answer, thinking, note) in enumerate(DRAFTS, start=start_num):
        item = {
            "id": f"G5V1-S{n:03d}",
            "source": {
                "origin": "self",
                "note": f"自编测试题，依据 {kp}（诊断缺口补齐，第七批 S-B07）",
            },
            "task": task,
            "kp_main": kp,
            "kp_other": [],
            "thinking": thinking,
            "figure": None,
            "answer": answer,
        }
        if note:
            item["answer_note"] = note
        items.append(item)
    return items


if __name__ == "__main__":
    out = Path(__file__).with_name("S-B07.yaml")
    items = build()
    out.write_text(
        yaml.safe_dump(items, allow_unicode=True, sort_keys=False, width=10**6),
        encoding="utf-8",
    )
    print(f"wrote {len(items)} drafts -> {out}")
    print("S158 rewrite (apply separately):")
    print("  task:", S158_REWRITE["task"])
    print("  answer:", S158_REWRITE["answer"])
