# B15 对账记录（338–366，观察物体（三））

日期：2026-11-18

## 流程

1. Author：产出 `items/answers/B15.yaml`。
2. 盲测输入：`items/answers/B15/blind.json`。
3. Verifier：只读 blind.json，产出 `items/answers/B15/independent.json`。
4. 对比：`compare_answers.py B15 338 366` → MATCH 29，DIFF 0。

## 裁决

两方独立作答在全部 29 题上结论一致：观察物体题所需的物体摆放图或指定视图均在教材插图中、题库 figure 为 null 且题干未转写 → **全部按开放题处理**（answer: null，answer_note 按题型写完成标准：画视图、操作不变性理由、摆法要求、由视图反推等）。无分歧项。

## 上报人工的问题（ISSUES）

与 B03–B05 图依赖题同类：29 题若要给出确定答案（具体视图变化、摆法），需人工核对教材插图后把摆放数据补进 `figure`（属题面修改，超出本计划权限）。补录前开放处理是唯一不编造数据的选项。

## 合并

`merge_answers.py B15 338 366` 合并，round-trip 通过；`validate_g5v1.py 366` 0 错误。
