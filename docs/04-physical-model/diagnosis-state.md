# Physical model: Diagnosis / LearningState

**Migration target:** `004_diagnosis_state.sql`  
**注意：** Diagnosis 字段级原文恢复不完整 — 实现前对照 `entity-dictionary.md` 并标 RECONSTRUCTED。

## Diagnosis tables

`diagnosis`, `diagnosis_subject`, `diagnosis_evidence_link`, `finding`, `finding_validity`, `finding_evidence_link`, `finding_relation`, `diagnosis_relation`, `knowledge_issue`, `finding_issue_link`（+ knowledge_issue_revision 建议纳入，与逻辑字典一致）

## State tables

`knowledge_state`, `thinking_state`, `learning_habit_state`, `goal_progress_state`, `state_revision`, `state_revision_reference`

## Key rules

- Finding 不可变；Validity 追加  
- State 主体唯一性按类型  
- OCC：ExpectedCurrentRevisionID 为参数，不进 history/revision 表  
- Revision + 依据 + 指针 + Event/Outbox 原子提交  
