# 实体目录

| 领域 | 实体 |
|---|---|
| Identity | Family, Person, Account, FamilyMember, … |
| Learning | LearningGoal, LearningGoalRevision, LearningTask, GoalTaskLink, LearningIntervention, … |
| Assessment | Question, QuestionVersion, TaskQuestion, LearningResponse, ResponseRelation |
| Evidence/Event | Evidence, EvidenceSource, EvidenceRelation, EvidenceLink, LearningEvent, EventRelation, TransactionalOutbox |
| Diagnosis | Diagnosis, DiagnosisSubject, Finding, FindingValidity, KnowledgeIssue, FindingIssueLink, … |
| State | KnowledgeState, ThinkingState, LearningHabitState, GoalProgressState, StateRevision, StateRevisionReference |
| Decision | DecisionRecord, DecisionCandidate, DecisionCandidateSelection, DecisionApproval, DecisionStatusHistory, … |
| Policy | Policy, PolicyVersion, PolicyPublication, PolicyRelation, PolicySimulation, PolicyEvaluation, … |
| Workflow | WorkflowDefinition, WorkflowDefinitionVersion, WorkflowStepDefinition, WorkflowRun, WorkflowStepRun, *StatusHistory, WorkflowPolicyReference |
| Methodology | Methodology, MethodologyVersion, GuidanceStrategy |
| AI/Audit | AIExecutionRecord, AIExecutionInput/Output, AIToolExecution, AuditRecord, … |

完整字段见 [entity-dictionary.md](./entity-dictionary.md)（RECONSTRUCTED 草稿）。  
关系矩阵见 [relationship-matrix.md](./relationship-matrix.md)。
