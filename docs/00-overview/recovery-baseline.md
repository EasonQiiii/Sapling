# Family Learning OS — 项目完整恢复档案

**文档版本：** Recovery Baseline 1.0  
**整理日期：** 2026-11-15  
**项目状态：** 暂停推进，保留历史设计成果  
**文档性质：** 基于现存项目记忆和历史摘要恢复，非完整聊天记录逐字还原  
**仓库位置：** 本文件为正式恢复入口；后续设计以分领域文档为准，本文件保留历史完整视图。

---

## 目录

1. 项目概述
2. 产品定位与设计原则
3. 总体系统架构
4. 核心业务流程
5. 核心领域模型
6. 学习任务与作业处理
7. OCR 与作答证据
8. Diagnosis 与 KnowledgeIssue
9. LearningState
10. Decision Engine
11. Policy Engine
12. Workflow Engine
13. Methodology Engine
14. LearningIntervention
15. LDSM 与跨模块协作
16. 家长、孩子与 AI 的角色边界
17. 逻辑数据模型设计规范
18. 第15章：核心实体字段字典
19. 第16章：逻辑 ERD 与关系约束
20. 第17章：逻辑模型一致性验收
21. 第18章：逻辑模型总表
22. 第19章：端到端业务链路验证
23. 第20章：物理设计准备
24. 第21～27章：物理模型
25. 第30章：物理模型修订与 PostgreSQL DDL
26. 第30章第24批：全局整合与验收
27. 已知问题与未决事项
28. 当前项目状态
29. 推荐后续工作
30. 历史资料恢复范围与限制

> **维护说明：** 分章详细内容已逐步拆分到 `docs/01-*`…`docs/07-*`。若与拆分文档冲突，以决策登记（`D-xxx`）和更新后的领域文档为准，并在本基线或 CHANGELOG 中记录变更。

---

## 1. 项目概述

### 1.1 项目名称

Family Learning OS — 家庭 AI 学习管家

面向小学阶段孩子，重点考虑小学四至六年级。

### 1.2 项目目标

帮助孩子形成可迁移的底层学习能力，而不是仅仅提高某次作业或考试成绩。

核心能力：独立学习、系统思维、批判性思考、创造力、自主探索、自我管理。

最终希望孩子离开 AI 后，仍然知道如何学习和解决问题。

### 1.3 核心学习闭环

发现问题 → 理解问题 → 拆解问题 → 探索解决 → 验证反思

AI 在其中扮演学习方法教练，而不是代替孩子完成任务的工具。

### 1.4 产品定位

系统应当：

- 适配孩子现有学习行为。
- 优先支持纸质作业。
- 通过长期证据了解孩子的知识掌握与思维能力。
- 根据孩子真实存在的问题安排学习干预。
- 随孩子成长逐步降低 AI 提示强度。
- 让孩子逐渐建立自主学习能力。

---

## 2. 产品设计原则

1. **不改变正常学习行为** — 孩子在纸质试卷或练习册上完成作业；不要求先在电脑/iPad 重做一遍。
2. **原始作答必须保留** — AI 干预前的原始作答必须保留；引导、订正、重答、迁移验证分开记录。
3. **知识与思维分别评价** — 分别建模、分别评价。
4. **长期结论必须有证据** — AI 判断不能直接成为最终业务事实。
5. **不以 AI 使用频率作为成长指标**
6. **AI 不替代家长** — 成长目标由家长和孩子共同制定。
7. **不追求一开始完美** — 优先完整、稳定、可演进的主干。

详见 [product-principles.md](./product-principles.md)。

---

## 3. 总体系统架构

最终模块：Decision Engine、Workflow Engine、Methodology Engine、Policy Engine、Learning Domain、Diagnosis Capability、LDSM。

**职责边界摘要：**

- Workflow 决定当前执行什么；Methodology 决定如何引导。
- Evidence 决定哪些结论有证据支持；Diagnosis 形成诊断判断。
- Decision 决定下一步做什么；Policy 限定允许做什么。
- Learning Domain 拥有学习业务对象；LDSM 负责持久化与状态更新机制，不拥有业务事实。

**特别强调：** 业务规则不依赖 Prompt，执行成功不依赖模型转述，Agent 不充当业务状态的最终裁判。

详见 `docs/01-architecture/`。

---

## 4. 核心业务流程

### Daily Learning Workflow

`CREATED → INGESTING → PARSING → NEEDS_CONFIRMATION → PLANNING → AWAITING_STUDENT_CONFIRMATION → COLLECTING_RESPONSES → BATCH_DIAGNOSING → LEARNING_PLAN_READY → INTERVENTION → REVIEWING → COMPLETED`

实际产品时序：孩子先完成纸质作业，之后上传照片，系统才进入 OCR 和统一诊断。不能要求 OCR 前后重复完成同一份数字作业。

详见 `docs/02-business/`。

---

## 5–9. 核心领域摘要

基础对象包括：Family、Person、Account、FamilyMember、LearningGoal、LearningTask、WorkflowRun、Question / QuestionVersion / TaskQuestion、LearningResponse、Evidence、LearningEvent、Diagnosis、Finding、KnowledgeIssue、LearningState、DecisionRecord、LearningIntervention。

关键规则：

- LearningTask ≠ WorkflowRun；一个 WorkflowRun 只执行一个 LearningTask。
- TaskQuestion 固定引用 QuestionVersion；LearningResponse 每次真实作答独立记录。
- OCR 校正不创建新 LearningResponse；孩子重新作答才创建。
- Finding 不可变；有效性通过 FindingValidity 追加；KnowledgeIssue ≠ 单次 Finding。
- LearningState 四类：Knowledge / Thinking / Habit / GoalProgress；Revision + OCC；依据失效则重新评价，不回滚历史。

详见 `docs/03-domain-model/`。

---

## 10–15. Engine 与协作摘要

Decision / Policy / Workflow / Methodology / LearningIntervention / LDSM 的职责、对象与接口见 `docs/01-architecture/` 与对应业务/领域文档。

未决项统一见 [unresolved-decisions.md](../05-decisions/unresolved-decisions.md)。

---

## 16. 家长、孩子与 AI 的角色边界

家长可查看任务、结果、知识问题、引导记录与重要事件；默认不逐字展示普通对话。安全例外需触发条件、范围与审计。AI 是工具不是人；不以 AI 使用频率作为成长指标；目标四级：Vision → Growth → Milestone → Action。

详见 [parent-child-ai-boundaries.md](../02-business/parent-child-ai-boundaries.md)。

---

## 17–22. 逻辑模型与验收摘要

- 稳定 ID、Revision、关联实体、多态引用规范。
- 第15章字段字典：规范 + C-01…C-10；完整逐实体表在恢复时缺失，仓库内提供 RECONSTRUCTED 草稿见 [entity-dictionary.md](../03-domain-model/entity-dictionary.md)。
- 第16章 ERD A–J：结论已完成，Mermaid 原文未恢复（不伪造）。
- 第17章一致性验收：设计审查完成；冻结前须合并 C-01…C-10。
- 第19章 E2E：五年级数学作业设计层通过；非数据库执行测试。

---

## 23–26. 物理模型与 DDL 摘要

- 推荐 PostgreSQL；大文件对象存储；V1 不强制 Redis / 独立 MQ / 独立向量库。
- 重要 Event 用 Transactional Outbox；单实例多 schema。
- 第21～27章：各域表清单与规则已恢复；部分字段级 SQL 缺失。
- 第30章分批修订结论已恢复；**不是已执行成功的 Migration**。
- Schema：platform, identity, learning, assessment, evidence, diagnosis, decision, policy, workflow, methodology, ai_execution, audit。
- 全局冲突清单 G-01…G-24 见物理模型总览与 unresolved。

**三层分离（正式约定）：**

1. `docs/03-domain-model/` — 逻辑模型  
2. `docs/04-physical-model/` — 物理设计说明  
3. `database/migrations/` — 可执行 SQL（不得由聊天批次直接拼接冒充最终稿）

---

## 27–30. 状态、后续与恢复限制

见 [PROJECT_STATUS.md](../../PROJECT_STATUS.md)、[known-limitations.md](../07-delivery/known-limitations.md)、[unresolved-decisions.md](../05-decisions/unresolved-decisions.md)。

### 未完整恢复的内容

- 全部历史对话逐字原文
- 第15～23批所有完整 PostgreSQL DDL
- 所有测试脚本原文
- 每个实体完整字段字典原文（已提供 RECONSTRUCTED 草稿）
- 第16章十个子图完整 Mermaid 原文
- 实际数据库执行日志
- 完整 Docker Compose 与部署文件原文

**因此本档案是 Recovery Baseline，不是已通过数据库执行验收的最终 V1 交付物。**

---

## 最终说明（系统原则）

1. 以孩子长期自主成长为目标。  
2. 保留真实学习行为和原始证据。  
3. 知识、思维、习惯和目标进展分别建模。  
4. 诊断必须有证据。  
5. Decision、Workflow、Methodology、Policy 各司其职。  
6. LearningIntervention 独立于 Workflow。  
7. LDSM 负责统一数据和状态管理，但不成为业务裁判。  
8. AI 是能力组件，不是系统事实来源。  
9. 所有重要判断必须可追溯。  
10. 系统逐渐培养孩子离开 AI 也能独立学习的能力。
