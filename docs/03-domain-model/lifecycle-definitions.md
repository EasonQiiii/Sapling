# 生命周期定义

| 对象 | 状态 / 规则 |
|---|---|
| LearningTask | 业务状态机（具体枚举待与 Workflow 对齐细化） |
| LearningResponse | IN_PROGRESS → SUBMITTED → PENDING_CONFIRMATION → CONFIRMED / CANCELLED；CONFIRMED≠正确 |
| Evidence | ACTIVE / WITHDRAWN / INVALIDATED / PENDING_DELETION / DELETED；内容不可覆盖 |
| Finding | 不可变；Validity 追加 VALID/SUPERSEDED/RETRACTED/UNCONFIRMED |
| KnowledgeIssue | OPEN / MONITORING / RESOLVED / CLOSED；摘要走 Revision |
| LearningIntervention | PLANNED / ACTIVE / PAUSED / COMPLETED / CANCELLED / CLOSED |
| WorkflowRun | 钉住 DefinitionVersion；状态历史 StatusRevision；不自动升版 |
| DecisionRecord | 独立 ID；状态与子对象状态独立 |
| PolicyPublication | 生效与版本分离；冲突规则未冻结（U-002） |

父级终止不简单级联改变子对象状态（干预域明确规则）。
