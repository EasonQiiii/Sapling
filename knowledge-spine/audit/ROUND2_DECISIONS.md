# 第二轮裁决总览（ROUND2_DECISIONS）

> **Round 2.2 验收通过；裁决落地：2026-11-17 16:53:07**  
> **math.std.v1 已冻结（2026-11-18）**：见 [`../MATH_STD_V1_FREEZE.md`](../MATH_STD_V1_FREEZE.md)  
> 正式源 YAML：**已修改**（A5-13 / CAP-07 / B-CAP-05；其后 J- 前缀 / CAP 迁移 / 前置规范化 / B3·B5 亦已落地）

## 当前覆盖汇总

| 状态 | 条数 | 计入覆盖率 |
|---|---|---|
| accurate | 173 | 是 |
| partial | 29 | 是 |
| incorrect | 0 | 是 |
| gap | 0 | 是 |
| pending_review | 0 | 是 |
| header_only | 22 | 否 |
| 合计 | 224 | |

覆盖率分母（不含 header_only）= **202**；accurate = **173**。

## 3 条遗留项落地结果

| CR | 裁决 | 落地动作 | 终态 |
|---|---|---|---|
| CR-080 | 批准 A5-13 | 写入 `初中/数学/数与运算.yaml`，4 条核心 LO | `accurate` |
| CR-090 | CAP 代数推理 | 新增 `B-CAP-05`，applies_to→B6/B7 | `partial` |
| CR-013 | A1 簇 + CAP | 映射 A1-01/08/09；新增 `CAP-07` | `partial` |

## 仍待执行的 Round 2 计划（已全部落地 2026-11-17）
- J- 前缀统计 ID 迁移 ✅（ID_MIGRATION_PLAN）
- A3-06 alias ✅（ID_MIGRATION_PLAN）
- A2-07/A4-10 → CAP-01/CAP-05 迁移 ✅（CAPABILITY_MIGRATION_REVIEW）
- 前置引用规范化 ✅（PREREQUISITE_MIGRATION_PLAN）
- B3/B7、B5 等边界方案 ✅（B3_B7_PROGRESSION_REVIEW / B5_CURRICULUM_REVIEW）
- 详见既有 `ROUND2_*.md` / `CAPABILITY_MIGRATION_REVIEW.md` / `PREREQUISITE_MIGRATION_PLAN.md`
