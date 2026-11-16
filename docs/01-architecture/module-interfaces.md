# 模块接口（设计级）

> 以下为恢复基线中的接口清单；请求/响应 schema 尚未冻结（见 U-010 等）。

## LDSM 写入

- `append_learning_event`
- `append_learning_evidence`
- `append_learning_response`
- `append_diagnosis`
- `submit_state_transition`（含 OCC 参数 `ExpectedCurrentRevisionID`，不入库为修订字段）

## LDSM 查询

- `query_learning_state` / `query_state_history`
- `query_evidence_lineage` / `query_diagnosis_lineage` / `query_object_history`

## Learning Domain

- `manage_learning_goal` / `manage_learning_task`
- `manage_intervention` / `manage_intervention_plan` / `evaluate_intervention_progress`
- `request_execution` / `get_task` / `get_goal` / `get_learning_catalog`

## Workflow Engine

- `start_workflow` / `pause_workflow` / `resume_workflow` / `stop_workflow`
- `get_workflow_run` / `request_methodology` / `request_diagnosis`

## Methodology Engine

- `generate_guidance` / `adapt_guidance` / `evaluate_guidance_fit`

## Diagnosis Capability

- `get_diagnosis_context` / `create_diagnosis` / `reassess_diagnosis`
- `relate_findings` / `relate_diagnoses` / `append_diagnosis`

## Policy Engine

- `get_applicable_policies` / `validate_decision` / `validate_execution` / `validate_checkpoint`
- `publish_policy` / `simulate_policy`

## Decision Engine

- `evaluate_context` / `create_decision` / `revise_decision`
- `evaluate_decision_outcome` / `on_state_changed` / `on_workflow_result`
