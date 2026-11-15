# V1 切片提案（待审 · 未采纳）

**状态：** `PROPOSAL` — 不是已确认决策。采纳后应写入 `decision-register.md` 并分配 `D-xxx`。  
**日期：** 2026-11-15  
**立场：** 文档地图已齐 ≠ 设计可全量落库。先收窄一条可验证闭环，再写 Migration。

---

## 1. 一句话目标

让一个四年级–六年级孩子：**纸质做完数学作业 → 拍照上传 → 确认识别 → 得到有证据的诊断要点 → 家长确认后有一条练习建议**；全程不覆盖原始作答，也不要求屏幕重做。

做到这一点之前，不建 Policy 模拟、Intervention Stage 图、完整 Decision 候选历史等重型对象。

---

## 2. 为什么现在不该全量落库

| 问题 | 影响 |
|---|---|
| OCR 未选型（U-001） | 纸质闭环关键路径未通 |
| 知识目录缺失（U-012） | KnowledgeState / KnowledgeIssue 无处稳挂 |
| Finding→KI 归并未定（U-011） | 诊断后半段自动化无规则 |
| Intervention 全树过重（U-013） | 实现量远超首条闭环 |
| Policy 冲突规则未冻（U-002…） | 过早落表只会锁住未定语义 |
| G-01…G-24 未收口 | 全量 DDL 必返工 |
| 字段字典 / ERD 为重建或缺失 | 全量建表依据不足 |

---

## 3. V1 必建（建议）

只服务「上传 → 确认 → 诊断 → 一条建议 → 状态一点更新」。

### 3.1 Identity / 租户

| 表/对象 | 原因 |
|---|---|
| `family` | 租户隔离 |
| `person` | 自然人 |
| `account` + `account_person_link` | 登录 |
| `family_member` | 家长/孩子角色 |

**缓建：** `child_autonomy_profile` 全修订树、复杂 `on_behalf_of`（可用最小授权字段或后期补）。

### 3.2 Learning / Assessment

| 表/对象 | 原因 |
|---|---|
| `learning_task` + 简单状态历史（或先 Event） | 作业任务 |
| `question` / `question_version` / `task_question` | 题目钉版本 |
| `learning_response` | 真实作答；含 RespondentReference、Mode、SupportLevel |
| `learning_goal` + `learning_goal_revision` + `goal_task_link` | 可先**极简**：一个家庭目标即可；若首周只要任务也可 Goal 再后移 |

### 3.3 Evidence / Event

| 表/对象 | 原因 |
|---|---|
| `evidence` + `evidence_relation` | 原图 / OCR / 校正谱系 |
| `learning_response_evidence_link` | 作答↔证据 |
| `learning_event` + `transactional_outbox` | 事实通知与可靠发布 |

**缓建：** 通用 `evidence_link` 大而全多态；先专用 link 表。

### 3.4 Diagnosis（薄）

| 表/对象 | 原因 |
|---|---|
| `diagnosis` + `diagnosis_subject` + `diagnosis_evidence_link` | 一次批诊断 |
| `finding` + `finding_validity` + `finding_evidence_link` | 不可变判断 + 有效性 |
| `knowledge_issue` + `knowledge_issue_revision` + `finding_issue_link` | 长期问题；**首版允许人工归并**（U-011 自动化后置） |

### 3.5 State（最小）

| 表/对象 | 原因 |
|---|---|
| `knowledge_state` + `state_revision` + `state_revision_reference` | 先只做知识掌握一类 |

**缓建：** Thinking / Habit / GoalProgress 三套头表（原则保留，V1 不落）。

### 3.6 Decision / Intervention（极薄）

| 表/对象 | 原因 |
|---|---|
| `decision_record` + `decision_candidate` + `decision_candidate_selection` | 至少保留「先记录再执行」；可先无复杂 evaluation 网 |
| `decision_approval` | 家长确认 |
| `learning_intervention` + `intervention_goal` + `intervention_goal_revision` + `intervention_task` | **无 Stage 树** |

### 3.7 Workflow / AI（务实最小）

| 表/对象 | 原因 |
|---|---|
| `workflow_definition` / `version` / `step_*` / `workflow_run` / `workflow_step_run` + 状态历史 | 若首版可用「硬编码作业流水线」也行；若坚持 Engine，只钉一个 Daily Learning 定义 |
| `ai_execution_record` + input/output | OCR/诊断调用可追溯 |
| `audit_record` | 关键写操作审计 |

---

## 4. V1 缓建（明确不进首迁）

| 域 | 缓建内容 | 理由 |
|---|---|---|
| Policy | Publication 冲突全套、Simulation、Evaluation、TASK 层 | 未冻结；用代码常量/配置文件先顶 SYSTEM 规则 |
| Methodology | GuidanceStrategy 复杂 JSON、独立会话 | V1 用固定提示强度枚举即可（D-015） |
| Intervention | Stage / StageGoal / Dependency / Acceptance 全树 | U-013；一条 Goal+Task 足够 |
| Decision | OutcomeEvaluation 网、大量 relation | 先 Selection + Approval + 简单 result |
| State | Thinking / Habit / GoalProgress | 先证明知识状态链路 |
| Identity | 完整自主权修订产品 | 隐私矩阵未定 |
| Infra | Redis / MQ / 向量库 | 已定 V1 不做（D-018） |

---

## 5. 建议落库顺序（仅 V1 切片）

```text
1. 001  identity（family/person/account/member）
2. 002  learning_task + question* + learning_response
3. 003  evidence + event + outbox
4. 004  diagnosis + finding + knowledge_issue（+ knowledge_state 最小）
5. 007' decision 薄切片 + intervention 薄切片
6. 008' ai_execution + audit 最小
```

原计划的 `005` 全 Intervention、`006` Policy/Methodology 全量：**移出 V1 Migration**，或留空文件并在 README 标 `DEFERRED`。

每批必须：空库执行 → FK/唯一/CHECK → 记入 `docs/06-validation/`（仅 PASS/FAIL/NOT_RUN）。

---

## 6. 设计上建议先改的三刀（落库前）

1. **写死 V1 范围决策**（本提案若采纳 → D-025）：必建/缓建表生效。  
2. **知识目录 v0**：四年级–六年级数学知识点一小表或种子枚举（关 U-012 的 V1 子集）。  
3. **Finding→KI**：V1 = 人工确认归并；自动化规则进 V2（关 U-011 的 V1 姿态）。

OCR：不阻塞「表结构切片」起草，但**阻塞产品闭环验收**；适配层接口先定，引擎可换（U-001）。

---

## 7. 我怎么看「完善度」

| 层 | 判断 |
|---|---|
| 产品原则 / 模块边界 | 够好，宜冻结 |
| 端到端业务故事 | 清楚，宜作验收脚本骨架 |
| 全量逻辑/物理模型 | **过完整、未收口**，不宜当 V1 建表清单 |
| 工程就绪 | **未就绪** |

**结论：** 先审本提案 → 采纳后改决策登记与 Migration 计划 → 再落库。不是「设计没问题了所以落库」。

---

## 8. 请你拍板的问题

1. 是否同意 **V1 不做** Policy 全表、Intervention Stage 树、Thinking/Habit/GoalProgress 状态？  
2. LearningGoal 首周是否也缓建，只保留 Task？  
3. Workflow Engine 首版是 **真表** 还是 **代码内固定流水线**（表后补）？  
4. KnowledgeIssue 首版是否接受 **人工归并**？  

你回复这四点后，再把提案转成正式 `D-xxx` 并改 `database/migrations` 计划。
