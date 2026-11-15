# Physical model: AI Execution / Audit

**Migration target:** `008_ai_execution_audit.sql`  
**Status:** Design recovered Ch27 / batch 23.

## AI Execution tables

| Table | Role |
|---|---|
| `ai_execution_record` | 一次模型/Agent 执行 |
| `ai_execution_input` | 输入内容/引用；核心内容不可覆盖 |
| `ai_execution_output` | 输出内容/引用；内容不可覆盖，允许状态更新 |
| `ai_tool_execution` | 工具调用；call number 锁 Record 后分配 |
| `execution_correlation` / `execution_causation` | 相关/因果；append-only；必须区分 |
| `execution_trace_reference` | 外部 Trace（如 OTel）引用 |

### AIExecutionRecord fields (logical)

`execution_type`, `execution_status`, Agent/Provider/Model, Prompt Config Version, `execution_request_id`, `correlation_id`, `causation_id`, `started_at`, `completed_at`, error, metadata, **`status_revision`**（正式 CREATE 直接包含，避免事后 ALTER）。

## Audit tables

| Table | Role |
|---|---|
| `audit_record` | 操作审计；append-only |
| `audit_reference` | 审计对象/依据引用 |

Audit 字段语义：操作者、授权依据、对象、类型、结果、请求引用、时间、关联信息。

## Hard boundaries (D-004)

- Audit / AIExecution **不能**替代 LearningEvent、Evidence、DecisionRecord
- AI 输出是候选，不自动成为业务事实
- AIExecution 成功 ≠ 诊断正确 / 决策合理 / 业务已接受
- **不**强制全局 `ai_output_acceptance` 表（C-09 / D-016）
- `AIExecutionStepLink` 复用 Workflow 关联机制（G-20）
- Audit ↔ AuthorizationReference 需真 FK（G-19）

Validation: `NOT_RUN`
