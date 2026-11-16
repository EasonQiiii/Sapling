# Global conflict checklist G-01…G-24

物理模型整合验收清单（来自 Recovery Baseline §26.4）。全部收口前，Migration 不得宣称完成（U-015）。

| ID | 主题 | 主要落点 |
|---|---|---|
| G-01 | FamilyMember / LearningGoal 复合唯一键 | 001 / 002 |
| G-02 | GoalRevision 归属校验 | 002 |
| G-03 | Response 不重复存 QuestionVersionID | 002 |
| G-04 | EvidenceLink NULL 唯一性 | 003 |
| G-05 | Outbox 索引重复 | 003 |
| G-06 | 多态引用领域校验 | 多批 |
| G-07 | Finding / DiagnosisSubject 复合归属 | 004 |
| G-08 | StateRevision 多态主体与当前指针 | 004 |
| G-09 | InterventionGoalLink NULL 唯一性 | 005 |
| G-10 | StageDependency UPDATE 环路检查 | 005 |
| G-11 | StageTask / StageGoal 归属 | 005 |
| G-12 | PolicyPublication 时间与范围冲突 | 006 · U-002 |
| G-13 | PolicyRelation 双层冲突 | 006 · U-004 |
| G-14 | CandidateSelection 历史与快照 | 007 |
| G-15 | StepRun 固定流程版本 | 007 |
| G-16 | StepRun attempt_number 并发安全 | 007 |
| G-17 | WorkflowPolicyReference | 007 |
| G-18 | AIExecution status_revision | 008 |
| G-19 | Audit AuthorizationReference FK | 008 |
| G-20 | AIExecutionStepLink | 008 / 007 |
| G-21 | 隐私删除 | U-014 |
| G-22 | 复合外键字段顺序 | 009 |
| G-23 | 状态历史与 Event/Outbox 原子提交 | 003 / 004 |
| G-24 | 测试脚本字段与真实 Migration 对齐 | tests |

收口流程：物理文档标注 → Migration 整合 → 空库执行 → `docs/06-validation/` 记 PASS/FAIL。
