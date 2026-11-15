# Physical model: Workflow

**Migration target:** `007_decision_workflow.sql`  
**Status:** Design recovered Ch26 / batch 22.

## Tables

| Table | Role |
|---|---|
| `workflow_definition` | 流程稳定身份 |
| `workflow_definition_version` | 不可变流程版本 |
| `workflow_step_definition` | 版本内步骤定义 |
| `workflow_step_transition` | 同版本内转移 |
| `workflow_run` | 执行实例；钉住 DefinitionVersion |
| `workflow_step_run` | 步骤执行；可多次 attempt |
| `workflow_run_status_history` | Run 状态历史（C-08） |
| `workflow_step_run_status_history` | Step 状态历史（C-08） |
| `workflow_policy_reference` | 钉住的 PolicyVersion + role/mode |

## Node types

`START` · `END` · `ACTION` · `DECISION` · `HUMAN` · `WAIT` · `TOOL` · `SUB_WORKFLOW`

## Key rules

- Transition 的 source/target 必须同 DefinitionVersion
- 旧 Run 默认不自动升版（倾向 U-007 → 待升为 D）
- `execution_request_id` 在 Run 上唯一（C-03）
- `attempt_number`：V1 锁定 WorkflowRun 行后分配（G-16）
- StepRun 必须属于 Run 的 DefinitionVersion（G-15）
- PolicyReference roles：`EXECUTION_BASELINE` / `SAFETY_CONSTRAINT` / `AUTHORIZATION_CONSTRAINT` / `TASK_CONSTRAINT`
- ValidationMode：`PINNED_VERSION` vs `REVALIDATE_CURRENT`（安全/授权高风险检查点重验）

## Publish checks（最小集，U-006 未完全冻结）

节点完整、START/END、可达性、分支完整、有退出条件的环允许。

## Open

- 检查点结果是否独立建表（U-008）
- Validation: `NOT_RUN`
