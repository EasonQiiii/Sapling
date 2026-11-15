# Physical model: Learning / Assessment

**Status:** Design recovered; SQL not fully integrated.  
**Migration target:** `002_learning_assessment.sql`

## Tables

- `learning_goal`, `learning_goal_revision`
- `learning_task`, `learning_task_status_history`
- `question`, `question_version`, `task_question`
- `learning_response`, `response_relation`, `learning_response_evidence_link`
- goal–task link table（复合 FK）

## Key rules

- UUID PK；TIMESTAMPTZ  
- Goal 稳定身份；Revision 不可变  
- Goal ↔ Task M:N；复合唯一/复合 FK（FamilyMember、LearningGoal）  
- TaskQuestion 固定 QuestionVersion  
- LearningResponse 不重复存 question_version_id；RespondentReference 独立  
- ResponseContent 不存大型原始材料  
- OCR 校正不新建 Response  
- ResponseStatus / ResponseMode / SupportLevel 枚举见逻辑字典  

## Batch-16 修订要点

整合进正式 CREATE，避免事后反复 ALTER。测试：`NOT_RUN`。
