# B01 对账记录（047–067）

日期：2026-11-18

## 流程

1. Author（独立 agent）：只读主 YAML 中 047–067 的 task/kp_main/source，产出 `items/answers/B01.yaml`。
2. 盲测输入：`items/answers/B01/blind.json`（由 `items/checks/export_blind.py` 导出，只含 id/task/figure）。
3. Verifier（独立 agent）：只读 blind.json，产出 `items/answers/B01/independent.json`。
4. 对比脚本：`items/checks/compare_answers.py B01 47 67` → MATCH 21，NUMERIC-MATCH 0，DIFF 0，MISSING 0。

## 裁决

两方独立作答在全部 21 题上结论一致：**均为开放或活动题**，`answer: null`，`answer_note` 写完成标准。无分歧项，无需逐题裁决。

依据：本批全部题目要么依赖真实班级/个人调查数据（047–051、056–057、064–067），要么数据在教材插图（第 22–23 页游泳人数、跳绳训练、篮球赛统计图）中而题库题干未转写（052–055、058–063）。题面与图形是唯一依据，题干无数据即不得编造。

## 上报人工的问题（ISSUES）

1. **G5V1-052–055、058–063（共 9 题）**：数值答案完全取决于教材插图的统计数据，但题库 `figure` 为 null、题干未转写数值。若希望这批题有确定数值答案，需人工核对教材插图后把数据补进 `task`/`figure`（属题面修改，超出本计划权限）。在补录之前，这 9 题按开放题处理是唯一不编造数据的选项。
2. **G5V1-050**：题干提到"男、女生的测试成绩"但未指明测试项目，answer_note 按泛化表述处理。
3. **计划偏差**：ANSWER_FILL_PLAN.md 预计 B01"多为数值结论"，实际 21 题全部无数据支撑。此偏差同样会影响 B06（141–144）等调查类批次之外的批次吗——待后续批次逐一验证，遇到同类情况按同一规则处理并记录。

## 合并

通过 `items/checks/merge_answers.py B01 47 67` 合并进 `items/sujiao-g5-vol1.yaml`，round-trip 校验通过；`python3 items/checks/validate_g5v1.py 67` 0 错误。
