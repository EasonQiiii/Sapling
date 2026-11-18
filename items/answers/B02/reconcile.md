# B02 对账记录（068–074，综合与实践：绿色出行）

日期：2026-11-18

## 流程

1. Author：产出 `items/answers/B02.yaml`。
2. 盲测输入：`items/answers/B02/blind.json`（export_blind.py 导出）。
3. Verifier：只读 blind.json，产出 `items/answers/B02/independent.json`。
4. 对比：`compare_answers.py B02 68 74` → MATCH 7，DIFF 0。

## 裁决

两方独立作答在全部 7 题上结论一致：均为开放或活动题，`answer: null`，`answer_note` 写完成标准。无分歧项。

依据：
- 068、072、073、074 依赖个人真实情境或讨论倡议，无唯一结果（074 为绿色出行倡议书，计划 §5 明确保持 null）。
- 069、070、071 依赖教材第 27 页路线图 / 公交线路图 / 地铁线路图，题库题干未转写站点与线路数据，不得编造。

## 上报人工的问题（ISSUES）

与 B01 同类：**G5V1-069–071** 的数值型答案（坐几站、途经哪些站、换乘方案）取决于教材插图的线路图数据。若希望给出确定答案，需人工核对教材插图后把线路与站点数据补进 `task`/`figure`。补录前按开放题处理。

## 合并

`merge_answers.py B02 68 74` 合并，round-trip 通过；`validate_g5v1.py 74` 0 错误。
