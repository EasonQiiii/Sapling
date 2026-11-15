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
| D-025 | V1 精简范围 | Accepted | 2026-11-15 | 见正文；完整域模型文档保留为后置资产 |
| D-026 | V1 缓建 LearningGoal | Accepted | 2026-11-15 | 首期只建 Task 闭环 |
| D-027 | V1 Workflow 使用真表 | Accepted | 2026-11-15 | 不用纯代码流水线冒充 |
| D-028 | Finding→KnowledgeIssue 自动归并 | Accepted | 2026-11-15 | 不依赖人工点选归并；规则算法仍可迭代 |
| D-029 | 产品范围为中小学全科，先做数学 | Accepted | 2026-11-15 | 纠正基线「仅小学四至六年级」的表述 |
| D-030 | 搬运成熟体系；自研必须带反馈 | Accepted | 2026-11-15 | 不做无来源发明；自研轮子可观测可迭代 |

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

### D-025 — V1 精简范围

**上下文：** 完整领域模型已设计，但未冻结项多，全量落库风险高；产品确认先走精简闭环。  
**决策（V1 不做 / 缓建）：**
- Policy 全表（Publication 冲突全套、Simulation、Evaluation、TASK 层）
- Intervention Stage 树（Stage/Dependency/Acceptance 等）
- ThinkingState / LearningHabitState / GoalProgressState（仅落 KnowledgeState）
- LearningGoal（见 D-026）

**V1 仍做：** Identity 基础、Task/Question/Response、Evidence/Event/Outbox、Diagnosis/Finding/KnowledgeIssue、KnowledgeState、薄 Decision+薄 Intervention、Workflow 真表、AIExecution+Audit 最小集。  
**后果：** `005`/`006` 全量标 DEFERRED；完整设计保留在 docs，不删除。

### D-026 — V1 缓建 LearningGoal

**决策：** 首期不建 Goal 及 GoalTaskLink；学习闭环以 LearningTask 为主。  
**后果：** Migration `002` 不含 goal 表；日后加 Goal 不破坏 Task 身份。

### D-027 — V1 Workflow 真表

**决策：** WorkflowDefinition/Version/Step/Run/StepRun/StatusHistory 等进 V1，不用「仅代码固定流水线、无表」。  
**后果：** 纳入 `007_decision_workflow.sql` 精简所需子集。

### D-028 — Finding→KnowledgeIssue 自动归并

**上下文：** 产品目标是系统自动形成长期知识问题，不依赖家长/老师点选归并。历史恢复文档写了「可归并到 KnowledgeIssue」，但**没有**写明必须人工确认；「先人工」曾是错误的精简默认，已纠正。  
**决策：** V1 **自动**将 Finding 归并/挂接到 KnowledgeIssue（创建或关联），不把人工点选当作必经步骤。  
**约束（与 D-004 并存）：**
- 归并是系统流程产出的业务事实，须写入 `finding_issue_link`（及必要 Event），可追溯到 Diagnosis/Finding/Evidence。
- 原始模型输出仍不是事实；须经 Diagnosis/归并服务落库后才生效。
- 置信不足可标 UNCONFIRMED / 新建待观察 Issue，而不是改回「等人点选才能并」。
- 归并**算法与阈值细则**仍可迭代（原 U-011 收窄为规则规格，不再争论要不要自动）。

**后果：** 诊断流水线默认自动归并；家长参与点在成长目标等（D-006），不在 KI 归并闸门。

### D-029 — 中小学全科，先做数学

**上下文：** Recovery Baseline 写「小学、重点四至六年级」，易被读成最终边界。  
**决策：** 产品服务**中小学**、**所有科目**；实施上**先打通数学闭环**，再扩展其他学科。  
**后果：**
- 领域模型（Task/Question/Evidence/Diagnosis/State/KI 等）不得写成「仅数学专用」死结构；科目/学段应为可扩展维度。
- V1 内容与评测样本可以只做数学；知识目录 v0 先数学，但预留多科目挂载（U-012）。
- 文档中凡「仅小学四至六年级」的表述，以本决策为准作边界更正。

### D-030 — 搬运成熟体系；自研必须带反馈

**上下文：** 教育、知识追踪、OCR、辅导流程等领域已有成熟体系；从零发明易脆弱且不可演进。  
**决策：**
1. 算法与关键设计**优先学习并适配**现有成熟体系（课标目录、BKT/掌握度、ITS 辅导、开源 OCR、FSM/BPMN 等）。  
2. 默认角色是**搬运工 + 适配器**，不是「家庭学习专用理论」发明家。  
3. 仅当硬约束无法被现成体系覆盖时才自研。  
4. 凡自研，必须具备版本、输入输出追溯、效用信号、指标与回滚，形成反馈系统，使轮子越用越成熟。  
5. 设计文档必须标明：学自何处 / 搬运了什么 / 自研了什么。

**后果：** P0/P1 设计稿无「学自」栏视为不合格；实现以适配层接入第三方/标准，避免锁死单一自研算法。  
**细则：** `docs/01-architecture/reuse-and-feedback.md`。

---

新增决策时：分配下一个 `D-xxx`，更新上表，并写简短正文。废止时将状态改为 `Superseded` 并移摘要到 `superseded-decisions.md`。
