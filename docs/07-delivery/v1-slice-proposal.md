# V1 精简切片（已确认方向）

**状态：** 产品已确认精简四点 + 产品边界；见 `D-025`…`D-029`。  
**本文**保留执行清单；细节以 decision-register 为准。

**产品边界（D-029）：** 中小学**全科**；本切片用**数学**打通第一条闭环。模型须可扩展到其他科目，不得写成数学专用死结构。

## 已确认

| # | 结论 | 决策 |
|---|---|---|
| 1 | V1 不做 Policy 全表、Stage 树、Thinking/Habit/GoalProgress | D-025 |
| 2 | LearningGoal **缓建** | D-026 |
| 3 | Workflow **真表** | D-027 |
| 4 | Finding→KI **自动归并**（不靠人点选） | D-028 |
| 5 | 中小学全科，先做数学 | D-029 |

## 关于第 4 点与文档

- 基线/诊断文档写了 KnowledgeIssue **可以**聚合多个 Finding，**没有**写「必须人工确认归并」。  
- 「先人工」来自精简提案的错误默认，不是产品原文。  
- 现已用 D-028 写死：自动归并；U-011 只剩**算法规格**，不再争论要不要人。

## V1 Migration 计划

| 文件 | V1 |
|---|---|
| 001_platform_identity.sql | 做 |
| 002_learning_assessment.sql | 做（**不含** goal） |
| 003_evidence_event.sql | 做 |
| 004_diagnosis_state.sql | 做（Diagnosis/Finding/KI + **仅** KnowledgeState；自动归并链路） |
| 005_learning_intervention.sql | **DEFERRED** 全 Stage；另见薄 Intervention 可并入 007' 或小文件 |
| 006_policy_methodology.sql | **DEFERRED** |
| 007_decision_workflow.sql | 做（薄 Decision + **Workflow 真表** + 薄 Intervention） |
| 008_ai_execution_audit.sql | 做（最小） |
| 009_cross_schema_constraints.sql | 做（V1 表子集） |

完整域模型文档保留，不删除。
