# 核心实体字段字典（Chapter 15）

**状态：** `RECONSTRUCTED` 草稿（非原文恢复）  
**基础：** Recovery Baseline §§5–9 + C-01…C-10（已应用修复）  
**约定：** Field Name（PascalCase 逻辑名）· Logical Type · Required（REQUIRED / CONDITIONAL / OPTIONAL）· Description · Constraint  

**已修复：**  
1. `ExpectedCurrentRevisionID` 不入库，仅为 OCC 写参数（C-06）  
2. `LearningGoal` 不含 `GoalLevel`（属 §16 业务范围）  
3. `KnowledgeIssue` 使用 `CurrentRevisionID` + `KnowledgeIssueRevision`  
4. C-05…C-10 已覆盖（实体或明确“不建表”注释）  
5. D-029：补 `SchoolStage` / `SubjectCode` / `KnowledgePoint` 挂载  
6. D-026：LearningGoal 表 V1 缓建（字典保留供后置）  
7. D-031：Finding/KI 对齐 KC + Newman `ErrorClass`  
8. D-033：KnowledgePoint 属**标准知识体系**；`CurriculumRef` 锚定课标；个人掌握另表；依赖边候选/发布另模型

逻辑类型：ID, ENUM, STRING, TEXT, INTEGER, DECIMAL, BOOLEAN, DATETIME, DATE, JSON, REFERENCE, HASH, URI。

---

## LearningTask

| Field | Type | Required | Description | Constraint |
|---|---|---|---|---|
| LearningTaskID | ID | REQUIRED | 稳定任务身份 | PK |
| FamilyID | ID | REQUIRED | 所属家庭 | FK |
| LearnerFamilyMemberID | ID | REQUIRED | 学习者 | FK |
| SchoolStage | ENUM | REQUIRED | 学段 PRIMARY/JUNIOR_SECONDARY… | D-029 |
| SubjectCode | ENUM | REQUIRED | 科目；先 MATH | D-029；可扩展 |
| GradeCode | STRING | OPTIONAL | 年级细化 | |
| TaskType | ENUM | REQUIRED | 任务类型 | |
| TaskStatus | ENUM | REQUIRED | 任务状态 | 对齐 closed-loop-steps |
| TaskSource | ENUM | REQUIRED | 任务来源 | |
| Title | STRING | OPTIONAL | 标题 | |
| Description | TEXT | OPTIONAL | 说明 | |
| PlannedStartAt | DATETIME | OPTIONAL | 计划开始 | |
| DueAt | DATETIME | OPTIONAL | 截止 | |
| CompletedAt | DATETIME | CONDITIONAL | 完成时间 | 完成态必填 |
| CreatedAt | DATETIME | REQUIRED | 创建 | |
| UpdatedAt | DATETIME | REQUIRED | 更新 | |

## LearningGoal

| Field | Type | Required | Description | Constraint |
|---|---|---|---|---|
| LearningGoalID | ID | REQUIRED | 稳定目标身份 | UNIQUE(id, family, owner) |
| FamilyID | ID | REQUIRED | 家庭 | |
| OwnerFamilyMemberID | ID | REQUIRED | 所有者 | |
| CurrentRevisionID | ID | REQUIRED | 当前修订 | FK → LearningGoalRevision |
| GoalStatus | ENUM | REQUIRED | 状态 | |
| CreatedAt | DATETIME | REQUIRED | 创建 | |
| UpdatedAt | DATETIME | REQUIRED | 更新 | |

> 不含 GoalLevel（out of slice）。

## GoalTaskLink

| Field | Type | Required | Description | Constraint |
|---|---|---|---|---|
| GoalTaskLinkID | ID | REQUIRED | 关联 ID | PK |
| LearningGoalID | ID | REQUIRED | 目标 | 复合 FK |
| LearningTaskID | ID | REQUIRED | 任务 | 复合 FK |
| LinkStatus | ENUM | REQUIRED | 有效状态 | 保留历史 |
| CreatedAt | DATETIME | REQUIRED | 创建 | |

## WorkflowRun

| Field | Type | Required | Description | Constraint |
|---|---|---|---|---|
| WorkflowRunID | ID | REQUIRED | 流程实例 | PK |
| LearningTaskID | ID | REQUIRED | 业务任务 | 一 Run 一 Task |
| WorkflowDefinitionVersionID | ID | REQUIRED | 钉住的流程版本 | 不自动升级 |
| RunStatus | ENUM | REQUIRED | 运行状态 | |
| CurrentStepRunID | ID | OPTIONAL | 当前步骤 | |
| ExecutionRequestID | ID | REQUIRED | 幂等请求身份（C-03） | UNIQUE |
| StartedAt | DATETIME | OPTIONAL | 开始 | |
| CompletedAt | DATETIME | CONDITIONAL | 结束 | 终态 |
| CreatedAt | DATETIME | REQUIRED | 创建 | |
| UpdatedAt | DATETIME | REQUIRED | 更新 | |

## Question / QuestionVersion / TaskQuestion

**Question：** `QuestionID`, `SubjectCode` (REQUIRED), `CreatedAt`  
**QuestionVersion：** `QuestionVersionID`, `QuestionID`, `VersionNumber`, `StemContent`(JSON), `StandardAnswer`, `Rubric`, `CreatedAt`（不可变）  
**QuestionKnowledgeLink（建议）：** `QuestionID`/`QuestionVersionID` + `KnowledgePointID`（Q 矩阵一行；可多 KC）  
**TaskQuestion：** `TaskQuestionID`, `LearningTaskID`, `QuestionID`, `QuestionVersionID`（与 Question 复合一致）, `SequenceNo`, `CreatedAt`

## LearningResponse

| Field | Type | Required | Description | Constraint |
|---|---|---|---|---|
| LearningResponseID | ID | REQUIRED | 一次真实作答 | OCR 校正不新建 |
| LearningTaskID | ID | REQUIRED | 任务 | |
| TaskQuestionID | ID | REQUIRED | 任务题目 | |
| QuestionID | ID | REQUIRED | 题目身份 | **不**存 QuestionVersionID |
| RespondentReferenceType | ENUM | REQUIRED | 作答者类型（C-01） | |
| RespondentReferenceID | ID | REQUIRED | 作答者（C-01） | ≠ 必须等于 Task Owner |
| ResponseMode | ENUM | REQUIRED | INDEPENDENT / AI_ASSISTED / HUMAN_ASSISTED | |
| SupportLevel | ENUM | REQUIRED | NONE / HINT / GUIDED / DIRECT_INSTRUCTION | |
| ResponseStatus | ENUM | REQUIRED | … / CONFIRMED / CANCELLED | CONFIRMED≠正确 |
| ResponseContent | JSON | CONDITIONAL | 结构化内容或引用（C-02） | 无大文件 |
| ContentStorageRef | URI | CONDITIONAL | 外部内容 | |
| StartedAt / SubmittedAt / ConfirmedAt | DATETIME | CONDITIONAL | 时序字段 | CONFIRMED 时必填且有序 |
| CreatedAt / UpdatedAt | DATETIME | REQUIRED | 审计时间 | |

## Evidence（AnswerEvidence）

| Field | Type | Required | Description | Constraint |
|---|---|---|---|---|
| EvidenceID | ID | REQUIRED | 证据身份 | 内容不可覆盖 |
| FamilyID | ID | REQUIRED | 家庭隔离 | |
| EvidenceType | ENUM | REQUIRED | 类型 | |
| ContentStorageType | ENUM | REQUIRED | INLINE_JSON / OBJECT_STORAGE / EXTERNAL_URI / REFERENCE_ONLY | |
| ContentInline | JSON | CONDITIONAL | 内联 | |
| ContentURI | URI | CONDITIONAL | 外链 | |
| ContentHash | HASH | OPTIONAL | 完整性 | |
| EvidenceStatus | ENUM | REQUIRED | ACTIVE…DELETED | |
| CapturedAt | DATETIME | OPTIONAL | 采集时间 | |
| CreatedAt | DATETIME | REQUIRED | 记录时间 | |
| CreatedByActorType / CreatedByActorID | ENUM/ID | OPTIONAL | 创建者 | |

**EvidenceRelation：** From/To EvidenceID + RelationType（含 CORRECTED_FROM 等）+ 禁自环、图无环（领域校验）。  
**LearningResponseEvidenceLink：** Response ↔ Evidence。  
**LearningEvent：** 业务事实；含 OccurredAt/RecordedAt/CorrelationID/CausationID/Payload；append-only；≠ Evidence。

## Diagnosis / Finding / KnowledgeIssue

**Diagnosis：** DiagnosisID, FamilyID, DiagnosisVersion, DiagnosedAt, InputContextRef, BasisSummary, DiagnosisStatus, CreatedAt（追加新诊断）。  
**DiagnosisSubject / DiagnosisEvidenceLink：** 主体与证据关联。  
**FindingValidity：** 追加有效性。  

### Finding（D-031）

| Field | Type | Required | Description | Constraint |
|---|---|---|---|---|
| FindingID | ID | REQUIRED | 不可变判断 | PK |
| DiagnosisID | ID | REQUIRED | 所属诊断 | FK |
| KnowledgePointID | ID | CONDITIONAL | 主责 KC | 归并强依赖；缺则 UNCLEAR |
| ErrorClass | ENUM | CONDITIONAL | Newman 映射类 | 见 auto-merge-rules-v0 |
| IsPrimaryBlame | BOOLEAN | OPTIONAL | 多 KC 题是否主责 | 默认 true |
| FindingType | ENUM | REQUIRED | 判断类型 | |
| Statement | TEXT | REQUIRED | 判断陈述 | |
| Confidence | ENUM | REQUIRED | 含 UNCONFIRMED | |
| CausalNotes | JSON | OPTIONAL | 共存/因果 | |
| CreatedAt | DATETIME | REQUIRED | 创建 | 不可变 |

### KnowledgeIssue（D-031）

| Field | Type | Required | Description | Constraint |
|---|---|---|---|---|
| KnowledgeIssueID | ID | REQUIRED | 长期问题 | ≠ 单次 Finding |
| FamilyID | ID | REQUIRED | 家庭 | |
| LearnerFamilyMemberID | ID | REQUIRED | 学习者 | |
| SubjectCode | ENUM | REQUIRED | 科目 | D-029 |
| PrimaryKnowledgePointID | ID | CONDITIONAL | 主 KC | 归并主键之一 |
| IssueKind | ENUM | REQUIRED | CONCEPTUAL/PROCESS/CARELESS/UNCLEAR… | 与 ErrorClass 相容 |
| Title | STRING | REQUIRED | 短标题 | |
| IssueStatus | ENUM | REQUIRED | OPEN…CLOSED | |
| CurrentRevisionID | ID | REQUIRED | 当前修订 | FK → KnowledgeIssueRevision |
| MergeAlgorithmVersion | STRING | OPTIONAL | 如 ki_merge.kc_newman.v0 | 反馈追溯 |
| OpenedAt / ResolvedAt | DATETIME | REQ / COND | 开闭时间 | |
| CreatedAt / UpdatedAt | DATETIME | REQUIRED | 审计 | |

### KnowledgeIssueRevision

| Field | Type | Required | Description | Constraint |
|---|---|---|---|---|
| KnowledgeIssueRevisionID | ID | REQUIRED | 不可变修订 | PK |
| KnowledgeIssueID | ID | REQUIRED | 父问题 | |
| RevisionNumber | INTEGER | REQUIRED | 展示序 | 非身份 |
| Summary | TEXT | REQUIRED | 叙事摘要 | 不可变 |
| Description | TEXT | OPTIONAL | 详述快照 | |
| StatusAtRevision | ENUM | OPTIONAL | 当时状态观察 | 不单独改头状态 |
| CreatedAt | DATETIME | REQUIRED | 创建 | |
| BasedOnFindingIDs | JSON | OPTIONAL | 参考 Finding | 权威在 Link |

## KnowledgePoint（标准知识体系节点，D-029 / D-033；首版内容 U-012）

公共基准节点；**不是**个人知识地图。教材年级/章节属映射扩展，不替代 `CurriculumRef` 课标锚。

| Field | Type | Required | Description | Constraint |
|---|---|---|---|---|
| KnowledgePointID | ID | REQUIRED | KC 稳定身份 | PK |
| SubjectCode | ENUM | REQUIRED | 科目 | |
| SchoolStage | ENUM | OPTIONAL | 学段提示 | |
| ParentKnowledgePointID | ID | OPTIONAL | 树父节点 | |
| Code | STRING | REQUIRED | 稳定业务码 | UNIQUE(subject, code) |
| Title | STRING | REQUIRED | 展示名 | |
| CurriculumRef | STRING | REQUIRED* | 课标条目锚（D-033） | *发布版必填；草稿可空但不得当权威 |
| CatalogEdition | STRING | REQUIRED | 标准目录发布版本 | 与依赖边版本对齐 |

**KnowledgeDependency（候选/发布，D-033）：** `FromKnowledgePointID`, `ToKnowledgePointID`, `RelationStatus` (CANDIDATE|PUBLISHED|REJECTED), `EvidenceRef`, `SourceType`, `CatalogEdition`, 变更历史可回滚。  
**TextbookMapping（教学映射）：** 教材版别/册/章/节/年级 → KnowledgePointID；来源可含「中小学知识平台」下载教材。
| CreatedAt | DATETIME | REQUIRED | 创建 | |

## LearningState

**V1 只落** `KnowledgeState`（D-025）。Thinking/Habit/GoalProgress 字典保留、表缓建。  
KnowledgeState：`LearnerFamilyMemberID` + `KnowledgePointID` 唯一；`CurrentRevisionID`、`UpdatedAt`。

### StateRevision（C-04）

| Field | Type | Required | Description | Constraint |
|---|---|---|---|---|
| StateRevisionID | ID | REQUIRED | 不可变修订 | PK |
| StateType | ENUM | REQUIRED | 四类之一 | 独立序列 |
| StateSubjectID | ID | REQUIRED | 状态行 | 多态，领域校验 |
| RevisionNumber | INTEGER | REQUIRED | 单调序号 | |
| StateContent | JSON | REQUIRED | 类型化内容 | |
| CreatedAt | DATETIME | REQUIRED | 与依据/指针/Event/Outbox 原子 | |
| CreatedByEventID | ID | OPTIONAL | 触发事件 | |

**非字段：** `ExpectedCurrentRevisionID` — 仅 `submit_state_transition` 的 OCC 参数（C-06 / D-012）。

**StateRevisionReference：** ReferenceType/ID[/RevisionID] 作为固定依据。

---

## C-05…C-10

### Decision（C-05 / C-06）

- **DecisionRecord.SelectedCandidateID** — 当前快照 only  
- **DecisionCandidateSelection** — 选择历史权威  
- **DecisionApproval.SelectionID** — 必须指向 Selection，非快照字段  
- **DecisionStatusHistory** — 含 StatusRevision；**无** ExpectedRevision 列  

### PolicyRelation（C-07）

支持 Policy 级与 **PolicyVersion 级** 端点（From/To PolicyID 与 From/To PolicyVersionID）。双层冲突处理未冻结（U-004）。

### Workflow 状态历史（C-08）

`WorkflowRunStatusHistory` / `WorkflowStepRunStatusHistory` 统一：From/ToStatus + StatusRevision + ChangedAt。

### C-09 / C-10（不建表）

- **不**强制全局 `AIOutputAcceptance` 实体（D-016）。  
- **不**建重复 `PolicyRegistry` 表；Registry 为管理入口（D-017）。  

---

## 完整度

| 范围 | 状态 |
|---|---|
| §§5–9 主实体 | RECONSTRUCTED 可用审阅 |
| Platform/Identity 全字段 | 未完 |
| Intervention 全树 | 见物理模型；字典待扩 |
| 枚举全集 / JSON Schema | 未冻结（U-009/U-010） |

冻结前：对照 ERD、物理模型、Migration 做一致性验收；未执行 DB 测试不得 PASS。
