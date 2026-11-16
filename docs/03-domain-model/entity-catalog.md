# 实体目录

十大逻辑领域实体清单。字段细节见 [entity-dictionary.md](./entity-dictionary.md)。关系见 [relationship-matrix.md](./relationship-matrix.md)。

| 领域 | 实体 |
|---|---|
| Platform / Identity | Family, Person, Account, AccountPersonLink, FamilyMember, ChildAutonomyProfile, AutonomyProfileRevision, Authorization, AuthorizationReference, OnBehalfOf |
| Learning | LearningGoal, LearningGoalRevision, LearningTask, LearningTaskStatusHistory, GoalTaskLink, LearningIntervention, InterventionRevision, InterventionGoal, InterventionGoalRevision, InterventionGoalLink, InterventionGoalProgress, InterventionGoalProgressRevision, InterventionStage, StageRevision, StageGoal, StageGoalRevision, StageGoalAcceptance, AcceptanceReference, StageTask, InterventionTask, StageDependency, InterventionRelation, InterventionStatusHistory |
| Assessment | Question, QuestionVersion, TaskQuestion, LearningResponse, ResponseRelation, LearningResponseEvidenceLink |
| Evidence / Event | Evidence, EvidenceSource, EvidenceRelation, EvidenceLink, LearningEvent, EventRelation, EventEvidenceLink, TransactionalOutbox |
| Diagnosis | Diagnosis, DiagnosisSubject, DiagnosisEvidenceLink, Finding, FindingValidity, FindingEvidenceLink, FindingRelation, DiagnosisRelation, KnowledgeIssue, KnowledgeIssueRevision, FindingIssueLink |
| Learning State | KnowledgeState, ThinkingState, LearningHabitState, GoalProgressState, StateRevision, StateRevisionReference |
| Decision | DecisionRecord, DecisionContextReference, DecisionCandidate, DecisionCandidateSelection, DecisionApproval, DecisionRelation, DecisionTaskLink, DecisionInterventionLink, DecisionWorkflowLink, DecisionExecutionResult, DecisionExecutionRelation, DecisionOutcomeEvaluation, EvaluationReference, EvaluationRelation, DecisionStatusHistory |
| Policy | Policy, PolicyVersion, PolicyPublication, PolicyRelation, PolicySimulation, PolicyEvaluation, PolicyEvaluationTarget, PolicyEvaluationReference |
| Workflow / Methodology | WorkflowDefinition, WorkflowDefinitionVersion, WorkflowStepDefinition, WorkflowStepTransition, WorkflowRun, WorkflowStepRun, WorkflowRunStatusHistory, WorkflowStepRunStatusHistory, WorkflowPolicyReference, Methodology, MethodologyVersion, GuidanceStrategy |
| AI Execution / Audit | AIExecutionRecord, AIExecutionInput, AIExecutionOutput, AIToolExecution, ExecutionCorrelation, ExecutionCausation, ExecutionTraceReference, AuditRecord, AuditReference |

## 明确不建（已决策）

| 名称 | 决策 |
|---|---|
| GuidanceExecution（V1） | D-015 |
| AIOutputAcceptance（全局强制） | D-016 / C-09 |
| PolicyRegistry 重复实体 | D-017 / C-10 |

## 地图

返回 [`DOC_MAP.md`](../DOC_MAP.md)。
