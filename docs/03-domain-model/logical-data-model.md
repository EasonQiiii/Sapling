# 逻辑数据模型

**地位：** 领域与核心关系的设计事实来源之一（与 entity-dictionary、decision-register 并列）。  
**来源：** Recovery Baseline §§5–9、§17–18；字段级原文部分缺失处已 RECONSTRUCTED。

## 规范

| 主题 | 规则 |
|---|---|
| 稳定 ID | 每业务对象全局 ID |
| Revision | 独立 Revision ID；VersionNumber 仅展示；CurrentRevisionID 指当前 |
| 非 Revision 化 | 非所有对象都需；Diagnosis 追加新诊断 |
| 关联 | 有业务意义的关联有独立 ID；历史固定必要版本 |
| 多态 | 优先专用关联+真 FK；通用才 target_type/id[/revision_id] |
| 唯一性 | 每种关联独立定义；不能统一按双方 ID 唯一 |

## 核心关系

- LearningGoal ↔ LearningTask：**多对多**（GoalTaskLink）  
- WorkflowRun → LearningTask：**多对一**；Run 固定 DefinitionVersion  
- TaskQuestion → QuestionVersion：**固定引用**；且 QuestionID 一致  
- LearningResponse → TaskQuestion；**不**重复存 QuestionVersionID  
- Evidence 内容不可变；校正用 EvidenceRelation（如 CORRECTED_FROM）  
- LearningEvent ≠ Evidence  
- Diagnosis 1→N Finding；Finding N↔N KnowledgeIssue（FindingIssueLink）  
- 四类 State 各自 CurrentRevisionID → StateRevision；依据在 StateRevisionReference  
- DecisionCandidateSelection 为选择权威；SelectedCandidateID 为快照（D-013）  
- LearningIntervention 独立于 Workflow（D-014）  

## C-01…C-10（字段字典修订）

| ID | 修订 |
|---|---|
| C-01 | LearningResponse 增加 RespondentReference |
| C-02 | ResponseContent 结构化或引用，不存大型原始材料 |
| C-03 | ExecutionRequestID 统一幂等身份 |
| C-04 | 四类 StateRevision 统一元数据 |
| C-05 | DecisionCandidateSelection 权威；SelectedCandidateID 快照 |
| C-06 | ExpectedRevision 是并发参数，非 StatusHistory 必需字段 |
| C-07 | PolicyRelation 支持具体 PolicyVersion |
| C-08 | WorkflowRun/StepRun 状态历史统一规范 |
| C-09 | 不强制全局 AIOutputAcceptance 实体 |
| C-10 | Policy Registry 不建重复实体 |

已应用到 [entity-dictionary.md](./entity-dictionary.md)。逻辑模型冻结前须合并上述修订（基线结论）。

## 明确不在本文件的内容

- 可执行 DDL → `database/migrations/`  
- 物理表注释与约束说明 → `docs/04-physical-model/`  
