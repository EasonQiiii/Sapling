# V1 完整主干提案（修订 · 待审）

**状态：** `PROPOSAL` — 按产品意见修订：V1 要更完善，不做过度裁剪。  
**前一版：** 曾建议大幅缓建 Policy / Stage / 三类 State；**已撤回该立场**。  
**日期：** 2026-11-15（修订）

---

## 1. 立场（已对齐你的方向）

- **同意：** V1 应是完整、可演进的主干，而不是「只够演示的最小玩具」。
- **不同意（已收回）：** 把 Thinking/Habit/GoalProgress、Intervention Stage、Policy、Methodology、Workflow 大体踢出 V1。
- **仍坚持：** 「更完善」≠「把未拍板的规则假装已定并写进不可逆 Migration」。完善 = **域表齐全 + 关键规则先冻结 + 空库可验收**。

一句话目标：

> V1 落地整条学习闭环的**完整领域主干**（含四类状态、干预阶段、策略与流程、决策与审计），并对齐纸质作业原则；未冻结规则先写成正式决策，再进 SQL。

---

## 2. V1 应包含的范围（完善主干）

### 2.1 必含领域（建议全部进 V1 Migration）

| 域 | V1 包含 | 说明 |
|---|---|---|
| Identity | Family / Person / Account / FamilyMember / Authorization 基础 | 含家庭隔离 |
| Learning / Assessment | Goal、Task、Question*、Response、关联 | 纸质闭环核心 |
| Evidence / Event | Evidence 谱系、Event、Outbox | 证据与可靠通知 |
| Diagnosis | Diagnosis、Finding、Validity、KnowledgeIssue(+Revision)、Links | 完整诊断链 |
| LearningState | **四类** State + StateRevision + References | 按原则完整建模 |
| Decision | Record、Candidate、Selection、Approval、StatusHistory、基础 Result | 先记录再执行 |
| Intervention | Intervention、Goal/Revision、Progress、**Stage 树**、Task 链接、Dependency、Acceptance | 完整干预模型 |
| Policy | Policy / Version / Publication / Relation | SYSTEM + FAMILY；规则见下 |
| Methodology | Methodology / Version / GuidanceStrategy | 无独立 GuidanceExecution（D-015） |
| Workflow | Definition/Version/Step/Transition/Run/StepRun/StatusHistory/PolicyReference | 真表，不靠「纯代码流水线」凑合 |
| AI / Audit | Execution Record/Input/Output/Tool + Audit | AI 非事实源 |

### 2.2 仍建议不进 V1 的（少而硬）

这些不是「偷懒砍功能」，而是基线里**未冻结或明确 V1 不做**的项：

| 项 | 原因 |
|---|---|
| Policy **TASK** 层（可选延后） | U-003 未定；先 SYSTEM+FAMILY 也可称完善主干 |
| PolicySimulation / PolicyEvaluation 产品化表 | 可 V1.1；不阻塞主闭环 |
| GuidanceExecution 独立表 | 已决策不做（D-015） |
| AIOutputAcceptance 全局表 | 已决策不做（D-016） |
| PolicyRegistry 重复实体 | 已决策不做（D-017） |
| Redis / 独立 MQ / 向量库 | 已决策不做（D-018） |
| OCR 引擎锁定某一开源实现 | 用适配层；样本验证后定（U-001） |

若你要求 **TASK 层 Policy 与 Simulation 也进 V1**，可以——但必须先冻结 U-002/U-003/U-004 的文字规则，再写表。

---

## 3. 「完善 V1」落库前必须先定的设计（不是缓建表，是补规则）

没有这些，表建得越全，返工越大：

| ID | 必须产出的冻结物 | 为什么 |
|---|---|---|
| U-001 | OCR 适配层接口 + 候选引擎评测计划 | 纸质闭环关键路径 |
| U-002 | Publication 范围/时间冲突规则（至少 FAMILY） | 否则 policy_publication 语义不稳 |
| U-006 | Workflow 图发布最小校验集 | 已有倾向，升为 D 即可 |
| U-007 | 旧 Run 不升版 | 基线已倾向，升为 D |
| U-011 | Finding→KI 归并：**规则 v0**（可半自动+人工确认） | 完善诊断链需要 |
| U-012 | 知识/能力/习惯目录 **v0 种子**（小学数学为主） | 四类 State 要挂得住 |
| U-014 | 隐私删除原则 v0 | Audit append-only 与删除冲突 |
| G-01…G-24 | 收口进 Migration 设计说明 | 完善物理模型的验收门禁 |

**Intervention Stage 全树：** 按你的要求 **进 V1**；同步把环路检查（G-10）与归属校验（G-11）写进物理说明与测试，而不是砍掉 Stage。

---

## 4. 建议 Migration 计划（完整主干）

保持原 001–009 拓扑，**不再把 005/006 标成 DEFERRED**：

| 顺序 | 文件 | V1 |
|---|---|---|
| 001 | platform_identity | 完整基础身份 |
| 002 | learning_assessment | Goal+Task+Question+Response |
| 003 | evidence_event | Evidence+Event+Outbox |
| 004 | diagnosis_state | Diagnosis+Finding+KI+**四类 State** |
| 005 | learning_intervention | **含 Stage 树** |
| 006 | policy_methodology | Policy（SYSTEM+FAMILY）+ Methodology；Simulation 表可空壳或 V1.1 |
| 007 | decision_workflow | Decision 完整主链 + Workflow 真表 |
| 008 | ai_execution_audit | 完整执行与审计 |
| 009 | cross_schema_constraints | G 清单跨 schema 收口 |

每批：空库执行 → 约束/并发/关键业务测试 → `docs/06-validation/` 只记 PASS/FAIL/NOT_RUN。

---

## 5. 与「过度裁剪版」的差异

| 主题 | 旧提案（已撤回） | 本修订（对齐你） |
|---|---|---|
| 四类 State | 只留 Knowledge | **四类都进 V1** |
| Intervention Stage | 缓建 | **进 V1** |
| Policy | 几乎不做 | **Version/Publication/Relation 进 V1** |
| Workflow | 可代码硬编码 | **真表进 V1** |
| Methodology | 枚举凑合 | **Version + GuidanceStrategy 进 V1** |
| 完善方式 | 靠砍范围 | **靠先冻规则再落全主干** |

---

## 6. 请你确认的点（比上版少，且偏完善向）

1. **确认：** V1 = 完整主干（上表 §2.1），接受「先冻 U/G 再写 SQL」，而不是先砍表。  
2. **TASK 层 Policy：** V1 要还是不要？（要 = 先写 U-003 规则）  
3. **PolicySimulation / Evaluation：** V1 要表，还是 V1.1？  
4. **Finding→KI：** 接受「规则 v0 + 可人工确认」作为完善诊断链的第一版吗？

你点头后，我会：把本提案要点写入 `decision-register`（新 D-xxx）、更新 `unresolved` 的 V1 姿态、按完整主干改 `database/README` 与 Migration 计划——**仍不会在规则冻结前塞假 PASS 的全量 DDL。**
