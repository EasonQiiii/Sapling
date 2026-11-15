# Database

## 三层分离（D-020）

| 层 | 位置 | 作用 |
|---|---|---|
| 逻辑模型 | `docs/03-domain-model/` | 业务语义与关系 |
| 物理设计 | `docs/04-physical-model/` | 表/约束设计说明 |
| 可执行 SQL | `database/migrations/` | **唯一**结构执行来源 |

**禁止**把第30章各批聊天输出直接拼成最终 Migration。

## V1 范围（D-025…D-028）

精简闭环 + Workflow 真表 + Finding→KI **自动**归并。  
LearningGoal、Policy 全量、Intervention Stage 树、Thinking/Habit/GoalProgress：**DEFERRED**。

## Migrations（计划）

| 文件 | 内容 | V1 状态 |
|---|---|---|
| 001_platform_identity.sql | platform + identity | 计划内 · **draft SQL written** · 空库 NOT_RUN |
| 002_learning_assessment.sql | catalog + task/question/response（**无 goal**） | 计划内 · **draft SQL written** · 空库 NOT_RUN |
| 003_evidence_event.sql | evidence + event + outbox | 计划内 · PLACEHOLDER |
| 004_diagnosis_state.sql | diagnosis + finding + KI + knowledge_state only | 计划内 · PLACEHOLDER |
| 005_learning_intervention.sql | 全 Stage 树 | **DEFERRED** |
| 006_policy_methodology.sql | policy + methodology 全量 | **DEFERRED** |
| 007_decision_workflow.sql | 薄 decision + workflow 真表 + 薄 intervention | 计划内 · PLACEHOLDER |
| 008_ai_execution_audit.sql | ai_execution + audit 最小 | 计划内 · PLACEHOLDER |
| 009_cross_schema_constraints.sql | 跨 schema（V1 子集） | 计划内 · PLACEHOLDER |

所有计划内文件当前仍为占位；**不可用于生产**。空库执行：`NOT_RUN`。

## Tests

结果写入 `docs/06-validation/`，仅 `PASS` / `FAIL` / `NOT_RUN`（D-021）。

## Seeds

`seeds/development-seed.sql` — 待可执行 Migration 后补充（含知识目录 v0 种子，关 U-012）。
