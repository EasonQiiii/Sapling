# V1 精简切片提案（当前方向）

**状态：** `PROPOSAL` — 产品已口头倾向精简路线；待确认 4 点后写入 `decision-register` 为正式 `D-xxx`。  
**修订史：**  
1. 初版：精简切片  
2. 曾按「V1 更完善」改为完整主干  
3. **2026-11-15：改回精简路线（本版）**

---

## 1. 一句话目标

纸质数学作业 → 拍照上传 → 确认识别 → 有证据的诊断要点 → 家长确认后一条练习建议；不覆盖原始作答，不要求屏幕重做。

在此之前，不建 Policy 模拟/评价全套、Intervention Stage 全树、完整四类 State 并行落库等重型对象。

---

## 2. 为什么精简（当前共识方向）

| 问题 | 影响 |
|---|---|
| OCR 未选型（U-001） | 纸质闭环关键路径未通 |
| 知识目录缺失（U-012） | State / KI 难稳挂 |
| Finding→KI 归并未定（U-011） | 诊断后半段不宜过度自动化 |
| Intervention Stage 全树 | 首条闭环过重 |
| Policy 冲突规则未冻 | 过早落全表易锁死错误语义 |
| G-01…G-24 未收口 | 全量 DDL 易返工 |

完整领域设计仍保留在 `docs/03-*` / `04-*` / recovery-baseline，作为 **已讨论、V1 后置** 的资产，不是删除。

---

## 3. V1 必建

### Identity
`family`, `person`, `account`, `account_person_link`, `family_member`  
缓建：完整 `child_autonomy_profile` 修订树、复杂 `on_behalf_of`

### Learning / Assessment
`learning_task`（+ 简单状态或 Event）  
`question`, `question_version`, `task_question`  
`learning_response`（RespondentReference、Mode、SupportLevel）  
`learning_goal` + revision + `goal_task_link`：**可选**——见下方待确认第 2 点

### Evidence / Event
`evidence`, `evidence_relation`, `learning_response_evidence_link`  
`learning_event`, `transactional_outbox`  
缓建：大而全通用 `evidence_link`（先专用 link）

### Diagnosis（薄）
`diagnosis`, `diagnosis_subject`, `diagnosis_evidence_link`  
`finding`, `finding_validity`, `finding_evidence_link`  
`knowledge_issue`, `knowledge_issue_revision`, `finding_issue_link`  
首版 KI 归并允许人工确认

### State（最小）
仅 `knowledge_state` + `state_revision` + `state_revision_reference`  
**缓建：** Thinking / Habit / GoalProgress 头表（原则保留在文档，V1 不落）

### Decision / Intervention（极薄）
`decision_record`, `decision_candidate`, `decision_candidate_selection`, `decision_approval`  
`learning_intervention`, `intervention_goal`, `intervention_goal_revision`, `intervention_task`  
**无 Stage 树**

### Workflow / AI（务实）
Workflow：真表 **或** 代码固定流水线——见待确认第 3 点  
`ai_execution_record` + input/output；`audit_record`

---

## 4. V1 明确缓建

| 域 | 缓建 | 理由 |
|---|---|---|
| Policy | Publication 全冲突模型、Simulation、Evaluation、TASK 层 | 未冻结；SYSTEM 规则先用配置/常量 |
| Methodology | 复杂 GuidanceStrategy JSON、独立会话表 | 固定提示强度枚举即可（D-015） |
| Intervention | Stage / StageGoal / Dependency / Acceptance | 一条 Goal+Task 足够 |
| Decision | OutcomeEvaluation 网、大量 relation | Selection+Approval+简单 result |
| State | Thinking / Habit / GoalProgress | 先跑通知识状态 |
| Infra | Redis / MQ / 向量库 | D-018 |

---

## 5. Migration 顺序（仅切片）

```text
1. 001  identity
2. 002  task + question* + response（± goal）
3. 003  evidence + event + outbox
4. 004  diagnosis + finding + knowledge_issue + knowledge_state 最小
5. 007' decision 薄 + intervention 薄
6. 008' ai_execution + audit 最小
```

原 `005` 全 Intervention、`006` Policy/Methodology 全量：标 `DEFERRED`，文件可留空壳说明，不进 V1 验收门禁。

---

## 6. 落库前三刀

1. 本提案确认后 → 正式 `D-025`（V1 范围）  
2. 知识目录 v0（小学数学小种子）——关 U-012 的 V1 子集  
3. Finding→KI：V1 = 人工确认归并 ——关 U-011 的 V1 姿态  

OCR：适配层接口先定；不阻塞表结构起草，阻塞产品闭环验收。

---

## 7. 待你确认（精简版四点）

1. 是否正式确认：**V1 不做** Policy 全表、Intervention Stage 树、Thinking/Habit/GoalProgress？  
2. LearningGoal 首周：缓建只留 Task，还是极简 Goal 也建？  
3. Workflow：首版 **真表** 还是 **代码内固定流水线**（表后补）？  
4. KnowledgeIssue：接受 **人工归并** 吗？

确认后：写入 decision-register、更新 unresolved 的 V1 姿态、改 `database/README` Migration 计划。
