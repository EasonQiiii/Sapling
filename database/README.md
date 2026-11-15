# Database

## 三层分离（D-020）

| 层 | 位置 | 作用 |
|---|---|---|
| 逻辑模型 | `docs/03-domain-model/` | 业务语义与关系 |
| 物理设计 | `docs/04-physical-model/` | 表/约束设计说明 |
| 可执行 SQL | `database/migrations/` | **唯一**结构执行来源 |

**禁止**把第30章各批聊天输出直接拼成最终 Migration。应先在物理模型文档收口 G-01…G-24，再写入本目录并在空库验证。

## Migrations（计划）

| 文件 | 内容 | 状态 |
|---|---|---|
| 001_platform_identity.sql | platform + identity | PLACEHOLDER |
| 002_learning_assessment.sql | learning + assessment | PLACEHOLDER |
| 003_evidence_event.sql | evidence + event + outbox | PLACEHOLDER |
| 004_diagnosis_state.sql | diagnosis + learning state | PLACEHOLDER |
| 005_learning_intervention.sql | intervention | PLACEHOLDER |
| 006_policy_methodology.sql | policy + methodology | PLACEHOLDER |
| 007_decision_workflow.sql | decision + workflow | PLACEHOLDER |
| 008_ai_execution_audit.sql | ai_execution + audit | PLACEHOLDER |
| 009_cross_schema_constraints.sql | 跨 schema FK/规则 | PLACEHOLDER |

所有文件当前为占位；**不可用于生产**。空库执行结果：`NOT_RUN`。

## Tests

`database/tests/*.sql` — 结构与业务验收脚本占位。结果写入 `docs/06-validation/`，枚举仅 `PASS` / `FAIL` / `NOT_RUN`（D-021）。

## Seeds

`seeds/development-seed.sql` — 开发数据；待 Migration 可执行后补充。
