# 关系基数矩阵（摘要）

> 第16章完整矩阵与 ERD A–J Mermaid 原文未恢复（U-016）。下表为基线摘要，标 RECONSTRUCTED。

| 从 | 到 | 基数 | 约束要点 |
|---|---|---|---|
| Family | FamilyMember | 1:N | 复合唯一 (id, family_id, role) |
| Family | LearningTask | 1:N | 家庭隔离 |
| LearningGoal | LearningTask | M:N | GoalTaskLink；复合 FK 校验归属 |
| LearningTask | WorkflowRun | 1:N | 一 Run 一 Task |
| Question | QuestionVersion | 1:N | Version 不可变 |
| LearningTask | TaskQuestion | 1:N | 固定 QuestionVersion |
| TaskQuestion | LearningResponse | 1:N | 每次真实作答一行 |
| LearningResponse | Evidence | M:N | Link；OCR 校正不新建 Response |
| Diagnosis | Finding | 1:N | Finding 不可变 |
| Finding | KnowledgeIssue | M:N | FindingIssueLink |
| State 主体 | StateRevision | 1:N | CurrentRevisionID；OCC |
| DecisionRecord | DecisionCandidate | 1:N | Candidate 不可变 |
| DecisionRecord | DecisionCandidateSelection | 1:N | 选择历史权威 |
| DecisionApproval | DecisionCandidateSelection | N:1 | 固定 SelectionID |
| LearningIntervention | LearningTask | M:N | 可共享；独立评价 |
| Policy | PolicyVersion | 1:N | Version 不可变 |
| PolicyVersion | PolicyPublication | 1:N | 发布≠版本本身 |
| WorkflowDefinition | WorkflowDefinitionVersion | 1:N | Run 钉住 Version |

完整 ERD：待 `docs/diagrams/erd-overview.mmd` 重建。
