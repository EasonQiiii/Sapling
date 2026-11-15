# Physical model: Diagnosis / LearningState

**Migration target:** `004_diagnosis_state.sql`  
**Status:** 表清单已恢复；Diagnosis 字段级原文部分缺失 → 对照 `entity-dictionary.md`（RECONSTRUCTED）。

## Diagnosis tables

| Table | Role |
|---|---|
| `diagnosis` | 一次诊断活动 |
| `diagnosis_subject` | 诊断主体（复合归属 G-07） |
| `diagnosis_evidence_link` | 诊断依据 |
| `finding` | 不可变判断 |
| `finding_validity` | 有效性追加 |
| `finding_evidence_link` | Finding 证据 |
| `finding_relation` / `diagnosis_relation` | 关系 |
| `knowledge_issue` | 长期问题头 |
| `knowledge_issue_revision` | 问题叙事修订（与逻辑字典对齐，建议纳入） |
| `finding_issue_link` | Finding ↔ Issue |

## State tables

| Table | Uniqueness |
|---|---|
| `knowledge_state` | child + knowledge_point |
| `thinking_state` | child + capability |
| `learning_habit_state` | child + habit_dimension |
| `goal_progress_state` | child + learning_goal |
| `state_revision` | 统一元数据（C-04）；按类型独立序列 |
| `state_revision_reference` | 类型化依据 |

## Key rules

- Finding 不可变；新诊断新 Finding；Validity 追加（D-010）
- KnowledgeIssue ≠ 单次 Finding（D-011）
- 头表 `current_revision_id` 指向当前修订
- OCC：`ExpectedCurrentRevisionID` 仅写参数，不进 revision/history 表（C-06 / D-012）
- Revision + 依据 + 指针 + Event/Outbox 原子提交（G-23）
- 依据失效 → 重新评价，不回滚历史
- 不强制所有状态更新先有 Diagnosis
- 知识目录 ontology 仍缺（U-012）

Validation: `NOT_RUN`
