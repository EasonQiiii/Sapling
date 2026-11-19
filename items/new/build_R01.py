"""Replacement batch R01: 12 self-authored test items replacing the 12 items
that needed human proofreading (see ANSWER_FILL_PLAN.md section 8, third round).

Each entry: (replaced_id, kp_main, thinking, task, answer, answer_note or None)
IDs run G5V1-S061 ... S072 in the same order as REPLACED.
"""
from pathlib import Path
import yaml

ENTRIES = [
    ("G5V1-326", "B3-03", "还要说明理由",
     "等式 5 × x = 35 两边同时除以 5，得到 x = 7。这样变形对吗？说明依据。",
     "对。依据：等式两边同时除以同一个非零数（5），等式仍成立；验算 5 × 7 = 35 也正确。",
     None),
    ("G5V1-393", "D2-03", "先选方法或先把情境翻译成数学关系",
     "口袋里只有 3 个红球和 1 个白球（除颜色外完全相同）。闭眼摸一个，摸到哪种颜色的可能性大？说明理由。",
     "摸到红球的可能性大。红球有 3 个、白球只有 1 个，红球所占的份数多，摸到的机会就多。",
     None),
    ("G5V1-175", "A1-10", "按步骤做",
     "3.45 中的 4 在哪一位上？它表示几个什么计数单位？",
     "4 在十分位上，表示 4 个十分之一（即 0.4）。",
     None),
    ("G5V1-176", "A3-04", "按步骤做",
     "计算 4.8 ÷ 6，并用乘法验算。",
     "4.8 ÷ 6 = 0.8；验算：6 × 0.8 = 4.8，与被除数相同，计算正确。",
     None),
    ("G5V1-209", "A1-03", "还要说明理由",
     "不计算，判断 36、47、51 中哪些是 3 的倍数，并说明理由。",
     "36 和 51 是 3 的倍数：3+6=9、5+1=6，各位数字之和都是 3 的倍数；47 不是，4+7=11，不是 3 的倍数。",
     None),
    ("G5V1-212", "A1-02", "按步骤做",
     "写出 12 的全部因数。再判断 8 是不是 4 的倍数，并说明为什么。",
     "12 的因数有 1、2、3、4、6、12。8 是 4 的倍数，因为 8 ÷ 4 = 2，没有余数（8 = 4 × 2）。",
     None),
    ("G5V1-187", "D2-03", "还要说明理由",
     "袋子里装有红球和黄球。摸球 40 次，记录红球 31 次、黄球 9 次。能推测袋中哪种颜色的球可能更多吗？说明理由。",
     "可以推测红球可能更多。摸到红球的次数远多于黄球，说明红球所占比例较大；但摸的次数有限，只能说“可能”，不能确定球的具体数量。",
     None),
    ("G5V1-239", "A1-07", "还要说明理由",
     "观察等式：3 + 5 = 8、3 + 7 = 10、5 + 7 = 12。每个加数是什么数？等号右边的数是什么数？",
     "每个加数都是质数（3、5、7）；等号右边的数都是大于 2 的偶数（8、10、12）。",
     None),
    ("G5V1-277", "B1-02", "按步骤做",
     "甲乙两地公路长 280 千米，已经行驶了 x 千米。用含字母 x 的式子表示还剩多少千米；当 x 是 100 时，还剩多少千米？",
     "剩下的路程为 (280 − x) 千米；当 x = 100 时，280 − 100 = 180（千米）。",
     None),
    ("G5V1-303", "B1-04", "先选方法或先把情境翻译成数学关系",
     "剧院共有 500 个座位。设卖出票数为 a，剩下票数为 b，写出 a 与 b 的关系式；若卖出 200 张，剩下多少张？",
     "b = 500 − a；卖出 200 张时，剩下 500 − 200 = 300 张。",
     None),
    ("G5V1-104", "C1-10", "按步骤做",
     "比较大小，填“＞”“＜”或“＝”：5 平方千米 ○ 480 公顷；3 公顷 ○ 30000 平方米。",
     "5 平方千米 = 500 公顷，500 > 480，填“＞”；3 公顷 = 30000 平方米，填“＝”。",
     None),
    ("G5V1-129", "C1-08", "先选方法或先把情境翻译成数学关系",
     "一个平行四边形的底是 9 厘米，高是 4 厘米，它的面积是多少平方厘米？如果底增加到 12 厘米、高不变，面积增加了多少平方厘米？",
     "原来面积：9 × 4 = 36（平方厘米）；底变为 12 厘米后面积：12 × 4 = 48（平方厘米），增加 48 − 36 = 12（平方厘米）。",
     None),
]

ID_PREFIX = "G5V1-S"


def build():
    items = []
    for n, (old, kp, thinking, task, answer, note) in enumerate(ENTRIES, start=61):
        item = {
            "id": f"{ID_PREFIX}{n:03d}",
            "source": {"origin": "self", "note": f"自编替换题（R01），替换 {old}；原题需人工校对，已删除"},
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
    out = Path(__file__).with_name("R01.yaml")
    items = build()
    out.write_text(yaml.safe_dump(items, allow_unicode=True, sort_keys=False, width=10**6), encoding="utf-8")
    print(f"wrote {len(items)} replacements -> {out}")
