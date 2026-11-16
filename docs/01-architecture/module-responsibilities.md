# 模块职责

## Decision Engine

综合上下文、学习状态、目标、历史证据、任务、依赖、权限，决定下一步；产出 `DecisionRecord`。含 Rule Engine（确定性）与 AI Reasoning（复杂推理），二者不可混同。三级权限：自动执行 / 建议待确认 / 需家长与孩子参与的授权决策。

## Workflow Engine

确定性流程：启动、节点执行、状态、分支、异常、暂停恢复、重试、调度。WorkflowDefinitionVersion 不可变；Run 固定版本，默认不自动升级。

## Methodology Engine

学习方法与引导：思维阶段、工具、提示方式与强度、引导适配。参与节点引导，但不可自行改变决策目标或业务状态。V1 不强制 `GuidanceExecution` 表（D-015）。

## Policy Engine

SYSTEM / FAMILY / TASK 策略层级；版本、发布、关系、模拟、评价。当前版本 ≠ 当前生效版本。多项未决见 `U-002`…`U-005`。

## Learning Domain

LearningGoal、LearningTask、LearningIntervention、InterventionGoal、InterventionStage 等业务对象生命周期。

## Diagnosis Capability

Diagnosis、Finding、KnowledgeIssue、诊断关系、Finding 有效性；基于证据判断。

## LDSM

统一持久化、关联、追溯、状态更新、Revision、查询。不是 Engine；不拥有/不创造业务事实，不自行判断领域状态。
