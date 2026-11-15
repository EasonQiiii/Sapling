# Decision Register

已确认决策登记。每个决策有唯一 ID。变更时新增条目或移入 `superseded-decisions.md`，**不覆盖**历史正文。

**状态枚举：** `Accepted` | `Superseded` | `Amended`

| ID | 标题 | 状态 | 日期 | 摘要 |
|---|---|---|---|---|
| D-001 | 纸质优先，不改变正常学习行为 | Accepted | 2026-11-15 | 孩子在纸质作业上完成；不要求数字化重做 |
| D-002 | 原始作答必须保留 | Accepted | 2026-11-15 | AI 干预前作答不可覆盖；订正/重答/迁移验证分记录 |
| D-003 | 知识与思维分别建模 | Accepted | 2026-11-15 | Knowledge / Thinking（及 Habit、GoalProgress）独立状态 |
| D-004 | AI 输出不是业务事实 | Accepted | 2026-11-15 | 结论必须可追溯到 Evidence；Agent 非最终裁判 |
| D-005 | 不以 AI 使用频率作成长指标 | Accepted | 2026-11-15 | 时长/对话数/频率/任务数均非最终成功标准 |
| D-006 | AI 不替代家长共定目标 | Accepted | 2026-11-15 | AI 建议，不裁决成长目标 |
| D-007 | LearningTask ≠ WorkflowRun | Accepted | 2026-11-15 | 业务任务与流程实例分离；一 Run 执行一 Task |
| D-008 | Question / Version / TaskQuestion 分离 | Accepted | 2026-11-15 | TaskQuestion 固定 QuestionVersion |
| D-009 | OCR 校正 ≠ 新 LearningResponse | Accepted | 2026-11-15 | 仅孩子重新作答创建新 Response |
| D-010 | Finding 不可变 + Validity 追加 | Accepted | 2026-11-15 | 新诊断产生新 Finding；有效性追加记录 |
| D-011 | KnowledgeIssue ≠ 单次 Finding | Accepted | 2026-11-15 | 长期问题可关联多次 Finding/干预 |
| D-012 | State 更新 OCC + 原子提交 | Accepted | 2026-11-15 | ExpectedCurrentRevisionID 为并发参数；与 Event/Outbox 同事务 |
| D-013 | Decision 先记录再执行 | Accepted | 2026-11-15 | DecisionCandidateSelection 为选择权威；SelectedCandidateID 仅快照 |
| D-014 | Intervention ≠ Workflow | Accepted | 2026-11-15 | Learning Domain 管理 Intervention；Workflow 不直接管理 |
| D-015 | V1 不强制 GuidanceExecution 表 | Accepted | 2026-11-15 | 引导追溯靠 Event/Evidence/Response/AIExecution/WorkflowRun |
| D-016 | V1 不强制 AIOutputAcceptance 全局实体 | Accepted | 2026-11-15 | C-09 |
| D-017 | Policy Registry 不建重复实体 | Accepted | 2026-11-15 | C-10；Registry 为管理入口 |
| D-018 | PostgreSQL + 单实例多 schema | Accepted | 2026-11-15 | 大文件对象存储；V1 不强制 Redis/MQ/向量库 |
| D-019 | Event 用 Transactional Outbox | Accepted | 2026-11-15 | 允许重复发布；消费者幂等；不宣称 exactly-once |
| D-020 | 文档三层分离 | Accepted | 2026-11-15 | 逻辑模型 / 物理模型说明 / 可执行 Migration 分离；禁止聊天批次 SQL 直接拼最终稿 |
| D-021 | 未执行验证不得标 PASS | Accepted | 2026-11-15 | 测试结果仅 PASS/FAIL/NOT_RUN |
| D-022 | ExecutionRequestID 统一幂等身份 | Accepted | 2026-11-15 | C-03；不另设业务 IdempotencyKey |
| D-023 | RespondentReference 独立于 Task Owner | Accepted | 2026-11-15 | C-01 |
| D-024 | ResponseContent 不存大型原始材料 | Accepted | 2026-11-15 | C-02；结构化内容或引用 |

## 决策正文

### D-001 — 纸质优先

**上下文：** 小学作业以纸质为主。  
**决策：** 系统适配现有纸质行为；上传发生在完成后。  
**后果：** OCR/确认成为关键路径；产品不得要求双轨重做。

### D-004 — AI 输出不是业务事实

**上下文：** 模型输出易被误当真相。  
**决策：** Evidence / Event / DecisionRecord 等业务对象拥有事实；AIExecution 成功 ≠ 诊断正确或业务已接受。  
**后果：** 所有长期结论需证据链路。

### D-012 — State OCC

**上下文：** 并发更新 LearningState。  
**决策：** `ExpectedCurrentRevisionID` 仅为写接口并发参数，**不**作为 StateRevision 或 StatusHistory 的必需存储字段（C-06）。  
**后果：** 修订创建、依据、当前指针、Event/Outbox 原子提交；依据失效则重评，不回滚历史。

### D-020 — 三层文档/SQL 分离

**上下文：** 第30章多批聊天 SQL 易被误拼为最终稿。  
**决策：** 逻辑模型、物理模型说明、`database/migrations/` 可执行 SQL 三层分离。  
**后果：** 物理文档解释设计；Migration 才是执行源。

---

新增决策时：分配下一个 `D-xxx`，更新上表，并写简短正文。废止时将状态改为 `Superseded` 并移摘要到 `superseded-decisions.md`。
