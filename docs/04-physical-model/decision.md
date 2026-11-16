# Physical model: Decision

**Migration target:** `007_decision_workflow.sql`（与 workflow 同批）  
**Status:** Design recovered Ch24 / batch 22.

## Tables

| Table | Role |
|---|---|
| `decision_record` | 一次决策；独立 ID，不覆盖更新 |
| `decision_context_reference` | 决策上下文引用 |
| `decision_candidate` | 候选；属一个 Decision；不可变 |
| `decision_candidate_selection` | **选择历史权威**（C-05） |
| `decision_approval` | 审批；固定 `selection_id` |
| `decision_relation` | 决策间关系 |
| `decision_task_link` | 关联 LearningTask |
| `decision_intervention_link` | 关联 Intervention |
| `decision_workflow_link` | 关联 WorkflowRun |
| `decision_execution_result` | 执行结果（TARGET 事实 vs OVERALL 汇总） |
| `decision_execution_relation` | 执行结果关系 |
| `decision_outcome_evaluation` | 结果评价；每次独立 |
| `evaluation_reference` / `evaluation_relation` | 评价依据 |
| `decision_status_history` | 状态历史；`status_revision` |

## Key rules

- `selected_candidate_id` 仅当前快照；权威在 `decision_candidate_selection`（D-013 / C-05）
- Approval 固定 SelectionID，不钉快照字段
- `ExpectedRevision` 是写并发参数，**不是** history 列（C-06）
- EvaluationStatus 与 EvaluationConclusion 分离
- Decision 状态与子对象状态独立

## Open

- 复合 FK 字段顺序与唯一键对齐（G-14 / G-22）
- Validation: `NOT_RUN`
