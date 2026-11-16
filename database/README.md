# Database

## 三层分离（D-020）

| 层 | 位置 | 作用 |
|---|---|---|
| 逻辑模型 | `docs/03-domain-model/` | 业务语义与关系 |
| 物理设计 | `docs/04-physical-model/` | 表/约束设计说明 |
| 可执行 SQL | `database/migrations/` | **唯一**结构执行来源 |

## V1 范围（D-025…D-032）

精简闭环 + Workflow 真表 + Finding→KI 自动归并（KC+Newman）+ 练习建议默认自动。  
LearningGoal、Policy 全量、Intervention Stage、Thinking/Habit/GoalProgress：**DEFERRED**。

## Migrations

| 文件 | 内容 | 空库结果 |
|---|---|---|
| 001_platform_identity.sql | identity | PASS（2026-11-15） |
| 002_learning_assessment.sql | catalog + task/question/response | PASS |
| 003_evidence_event.sql | evidence + event + outbox | PASS |
| 004_diagnosis_state.sql | diagnosis + KI + knowledge_state | PASS |
| 005_learning_intervention.sql | DEFERRED no-op | PASS（有意空） |
| 006_policy_methodology.sql | DEFERRED no-op | PASS（有意空） |
| 007_decision_workflow.sql | decision + workflow + 薄 intervention | PASS |
| 008_ai_execution_audit.sql | ai + audit 最小 | PASS |
| 009_cross_schema_constraints.sql | 索引子集 | PASS |

详情：[docs/06-validation/migration-validation.md](../docs/06-validation/migration-validation.md)

## Seeds

`seeds/math_knowledge_points_v0.sql` — **INVALID DRAFT（D-033）**：自编挂点，仅空库 smoke **PASS**；非正式标准知识体系。权威来源见决策 D-033 / `docs/03-domain-model/subject-and-catalog.md`。

## 本地重跑

```bash
# Postgres 16 + role/db flos / family_learning_os
export PGPASSWORD=flos
for f in database/migrations/00{1,2,3,4,5,6,7,8,9}_*.sql; do
  psql -h 127.0.0.1 -U flos -d family_learning_os -v ON_ERROR_STOP=1 -f "$f"
done
psql -h 127.0.0.1 -U flos -d family_learning_os -v ON_ERROR_STOP=1 -f database/seeds/math_knowledge_points_v0.sql
```
