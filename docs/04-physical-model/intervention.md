# Physical model: LearningIntervention

**Migration target:** `005_learning_intervention.sql`  
**Status:** Design recovered Ch25 / batch 20. V1 深度未决（U-013）。

## Tables

| Table | Role |
|---|---|
| `learning_intervention` | 干预头 |
| `intervention_revision` | 干预修订 |
| `intervention_goal` / `intervention_goal_revision` | 干预目标及版本 |
| `intervention_goal_link` | 目标关联 |
| `intervention_goal_progress` / `*_revision` | 干预内进展（不复用全局 GoalProgressState） |
| `intervention_stage` / `stage_revision` | 阶段 |
| `stage_goal` / `stage_goal_revision` | 阶段目标；钉 StageRevision + InterventionGoalRevision |
| `stage_goal_acceptance` / `acceptance_reference` | 阶段验收（PASSED/FAILED/INCONCLUSIVE/NOT_EVALUATED） |
| `stage_task` / `intervention_task` | 任务两层关联；可共享 LearningTask |
| `stage_dependency` | 阶段依赖；有效图无环 |
| `intervention_relation` | DEPENDS_ON / DERIVED_FROM / SUPPLEMENTS |
| `intervention_status_history` / `intervention_child_status_history` | 状态历史 |

## Key rules

- Intervention ≠ Workflow（D-014）
- 目标实质转向应结束旧 Intervention 并建新
- 阶段验收 ≠ 干预目标达成
- StageTask 必须校验 Stage↔Intervention 归属；`stage_goal_id` 校验 StageGoal 归属（G-11）
- StageDependency：INSERT **与** UPDATE 激活边都要环路检查（G-10）
- 共享 Task：同一次真实行为默认执行一次；延迟/迁移验证新建 Task+Response
- 父级终止不简单级联改子状态

## V1 recommendation

优先实现：Intervention + GoalRevision + Task links；Stage 图可延后（U-013）。

Validation: `NOT_RUN`
