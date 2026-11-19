#!/usr/bin/env python3
"""Author drafts for self-authored test items, batch S-B06 (3 KPs x 2 items).

Each entry: (kp, task, answer, thinking, answer_note or None).
ID range: G5V1-S229 … G5V1-S234.
Output: items/new/S-B06.yaml (drafts only; not merged into the bank yet).
"""
from pathlib import Path
import yaml

DRAFTS = [
    # ---- A2-02 小数的数位与位值 (已有 1 题，补 2)
    ("A2-02", "在 3.45 这个小数中，4 和 5 分别在哪一位上？它们各表示多少？这个数读作什么？",
     "4 在十分位上，表示 4 个十分之一，即 0.4；5 在百分位上，表示 5 个百分之一，即 0.05。3.45 读作三点四五。",
     "按步骤做",
     "完成标准：必须说明 4 在十分位、5 在百分位，且分别表示 0.4 和 0.05。"),
    ("A2-02", "一个小数：个位上是 2，十分位上是 6，百分位上是 8，其余各位都是 0。请写出这个数，并说明它由哪些计数单位组成。",
     "2.68。它由 2 个一、6 个十分之一和 8 个百分之一组成。",
     "还要说明理由", None),
    # ---- A3-02 减法的意义与运算 (已有 1 题，补 2)
    ("A3-02", "计算 15.6 − 7.8，并用加法检验结果。",
     "15.6 − 7.8 = 7.8。检验：7.8 + 7.8 = 15.6，差与减数相加等于被减数，结果正确。",
     "认出来就做", None),
    ("A3-02", "小红有 20.5 元，买了一支钢笔后还剩 12.8 元。这支钢笔多少元？为什么用减法计算？本题中减法表示的是哪一种意义（去掉一部分、比较两个数量的差，还是求一个加数）？",
     "20.5 − 12.8 = 7.7（元）。用减法是因为“原有的钱 − 买钢笔用去的钱 = 剩下的钱”，现在已知原有的钱和剩下的钱，求用去的钱，即已知和与一个加数求另一个加数，所以本题中减法表示的是“求一个加数”的意义。",
     "还要说明理由", None),
    # ---- A4-03 乘法分配律 (已有 1 题，补 2)
    ("A4-03", "用简便方法计算 25 × 44 时，小明写成 25 × 4 × 11，小红写成 25 × (40 + 4)。两个人的算法都正确吗？各用了什么运算律？请分别算出结果。",
     "都正确，结果都是 1100。小明：25 × 4 × 11 = 100 × 11 = 1100，把 44 拆成 4 × 11，用的是乘法结合律；小红：25 × (40 + 4) = 25 × 40 + 25 × 4 = 1000 + 100 = 1100，用的是乘法分配律。",
     "先选方法或先把情境翻译成数学关系", None),
    ("A4-03", "判断：“102 × 36 = 100 × 36 + 2 × 36”这个变形对不对？它依据什么运算律？为什么这样算简便？请算出结果。",
     "对。102 = 100 + 2，依据乘法分配律：(100 + 2) × 36 = 100 × 36 + 2 × 36 = 3600 + 72 = 3672。这样算简便是因为 100 × 36 可以直接写出 3600，把乘 102 化为乘整百数加乘 2。",
     "还要说明理由", None),
]

def build(start_num=229, batch="S-B06"):
    items = []
    for n, (kp, task, answer, thinking, note) in enumerate(DRAFTS, start=start_num):
        item = {
            "id": f"G5V1-S{n:03d}",
            "source": {"origin": "self", "note": f"自编测试题，依据 {kp}（覆盖补齐，第六批 S-B06 补充）"},
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
    out = Path(__file__).with_name("S-B06.yaml")
    items = build()
    out.write_text(yaml.safe_dump(items, allow_unicode=True, sort_keys=False, width=10**6), encoding="utf-8")
    print(f"wrote {len(items)} drafts -> {out}")
