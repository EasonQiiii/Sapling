# Knowledge-Spine 全量知识体系审计报告

> **状态：已由 math.std.v1 冻结结论取代（2026-11-18）**  
> 权威冻结声明：[`../MATH_STD_V1_FREEZE.md`](../MATH_STD_V1_FREEZE.md)  
> 下文保留审计轨迹；**不要再把 2026-11-17 11:36 的 Round 1 FAIL 当作现行结论。**

## 现行结论（冻结时）

| 项目 | 结果 |
|---|---|
| 是否达到 v1 冻结标准 | **是**（允许 29 条已知 partial） |
| 正式 YAML `status` | 14/14 = `final` |
| ID 唯一性 | PASS（初中统计已 `J-` 前缀） |
| 前置引用 | PASS（纯 ID、可解析、CAP 不作前置） |
| 依赖循环 | PASS |
| 课标映射（Round 2.2） | accurate 173 / partial 29 / incorrect 0 / gap 0 / pending 0；header_only 22 |

覆盖率分母（不含 header_only）= **202**。

### Round 2 阻断项处置

| 原 Round 1 阻断 | 处置 |
|---|---|
| 小学/初中统计 `D1-*`/`D2-*` 冲突 | 初中改为 `J-D*` / `J-D-CAP-*` |
| 自然语言/歧义前置 | 已按 `PREREQUISITE_MIGRATION_PLAN` 规范化 |
| `A2-06`/`A3-06` 双 ID | `A3-06` → alias(`A2-06`) |
| `A2-07`/`A4-10` 能力混入 KP | 迁入 `CAP-01` / `CAP-05` |
| 二次根式缺口（CR-080） | 新增 `A5-13` → accurate |
| 代数推理待决（CR-090） | 新增 `B-CAP-05` → partial（政策接受） |
| 数感素养缺口（CR-013） | 新增 `CAP-07` → partial（政策接受） |

## 历史快照：Round 1（已作废）

- **审计时间**：2026-11-17 11:36:51  
- **执行原则（当时）**：只审计、不修改任何源 YAML  
- **当时结论**：尚未达到可投入生产的验收状态（ERROR / FAIL）  
- **当时规模**：YAML 14；抽取 KP 179（建议扣 A3-06 后 178）；重复 ID 组 12；文本前置 58  
- **问题清单快照**：见同目录 `ISSUES.md`（Round 1 生成，条目状态以 Round 2 落地与冻结声明为准）

### 当时验收条件对照（历史）

| 项目 | 当时结果 |
|---|---|
| YAML 解析 | PASS |
| ID 唯一性 | FAIL |
| 前置引用 | FAIL |
| 依赖循环 | PASS |
| 必需字段 | PASS |
| 课标映射 | WARNING |
| 跨学段衔接 | FAIL |

## 交付物索引

- `../MATH_STD_V1_FREEZE.md`（**现行冻结权威**）
- `ROUND2_DECISIONS.md`
- `CURRICULUM_MAPPING_REVIEW.md` / `round2_2_index.json`
- `ID_MIGRATION_PLAN.md` / `PREREQUISITE_MIGRATION_PLAN.md` / `CAPABILITY_MIGRATION_REVIEW.md`
- `B3_B7_PROGRESSION_REVIEW.md` / `B5_CURRICULUM_REVIEW.md` / `RADICAL_COVERAGE_PLAN.md`
- `ISSUES.md`（Round 1 问题快照；非现行阻塞清单）
