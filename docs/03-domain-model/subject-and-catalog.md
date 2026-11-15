# 学段 · 科目 · 知识目录（P0）

**决策：** D-029（中小学全科，先数学）、D-030（搬运优先）  
**状态：** 设计规格 v0  

## 学自 / 搬运 / 自研

| | 内容 |
|---|---|
| **学自** | 中国义务教育/普通高中**课程标准**知识点组织方式；教材「章–节–知识点」树；学习资源元数据中「学科/学段」常见维度 |
| **搬运** | 用「学段 + 科目 + 知识点树」三层挂载；知识点稳定 ID + 展示名 + 课标/教材可选映射 |
| **自研** | 无。仅增加本系统对象上的引用字段与 Family 隔离；不发明新课标 |

## 逻辑维度（可扩展，禁止数学死结构）

| 字段/对象 | 含义 | 备注 |
|---|---|---|
| `SchoolStage` | 学段枚举 | 如 PRIMARY / JUNIOR_SECONDARY（可再加高中）；年级用 `grade_code` 可选细化 |
| `SubjectCode` | 科目 | `MATH` 先实装；`CHINESE` / `ENGLISH` / … 占位合法 |
| `KnowledgePoint` | 目录节点 | 稳定 ID；可有 parent 形成树；`subject_code` 必填 |
| `curriculum_ref` | 可选课标/教材引用 | 字符串或 URI；便于对齐课标，不强制单一教材 |

## 挂到哪些业务实体

| 实体 | 建议字段 | 原因 |
|---|---|---|
| LearningTask | `school_stage`, `subject_code`, 可选 `grade_code` | 作业属于哪科学段 |
| Question / QuestionVersion | `subject_code`；知识点经关联表 | 题可跨任务复用 |
| TaskQuestion | 可选覆盖知识点 | 任务内点题 |
| Finding | `knowledge_point_id`（可多点经 link） | 诊断落点 |
| KnowledgeIssue | `subject_code` + 主 `knowledge_point_id` | 长期问题归属 |
| KnowledgeState | 已有 `KnowledgePointRef` → 改为正式 FK/稳定 ID | 掌握度附着 |

## 数学 v0 内容策略

- **不自编**知识点全集：从课标/主流教材章节树**搬运**一版数学子集（先覆盖首条闭环样卷所需节点）。  
- 其他科目：目录允许空树 + 合法 `SubjectCode`，保证扩展时不改核心表语义。

## 反馈（若后续自研映射层）

课标映射若需自研对齐算法：记录映射版本、抽检一致率、错挂知识点后的 State/KI 纠正事件（仍遵守 D-030）。

## 相关

- U-012（目录内容填充）  
- `entity-dictionary.md` 后续补字段行  
