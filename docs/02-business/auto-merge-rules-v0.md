# Finding → KnowledgeIssue 自动归并：推荐解法 v0

**状态：** 由设计侧调研后给出的**默认解法**（产品未自带方案；本文件即交付的推荐）  
**决策对齐：** D-028（必须自动）、D-004（AI 非事实）、D-030（搬运优先 + 反馈）  
**算法 ID：** `ki_merge.kc_newman.v0`

---

## 1. 结论（先看这个）

**推荐搬运并组合两套成熟体系，而不是自创「家庭学习归并理论」：**

| 层次 | 搬运自 | 在本系统中的角色 |
|---|---|---|
| **问题主键** | ITS 的 **Knowledge Component（KC）**（Cognitive Tutor / ASSISTments 一脉） | `KnowledgePoint` = KC；长期问题按「学习者 × 科目 × KC」聚合 |
| **错因分层** | **Newman Error Analysis**（阅读/理解/转换/过程/编码 + 粗心等） | Finding 上的 `error_class`；避免把「粗心」并进「概念未掌握」 |
| **归并动作** | 数据领域 **entity resolution** 的「匹配→挂接/新建」 | 确定性规则服务写 `FindingIssueLink`；无人点选闸门 |
| **多技能题** | **Conjunctive Knowledge Tracing** 的归咎思想（Koedinger 等） | 错题不默认惩罚/归并到题面涉及的全部 KC，只归并诊断给出的主责 KC |
| **模型角色** | 辅助打标（可选） | LLM **只产出** KC/Newman **候选**；落库必须过规则（D-004） |

**不推荐 v0：** 纯向量聚类乱并、纯 LLM「觉得像就并」、无 KC 只靠题面相似度。

---

## 2. 学自 / 搬运 / 自研

| | 内容 |
|---|---|
| **学自** | Cognitive Tutor / ASSISTments 的 KC 学生模型；Newman (1977/1983) 数学解题错误层级；BKT 及 Conjunctive KT 的多技能归咎；实体解析「同一真实对象多条观测」 |
| **搬运** | KI 身份 ≈ 开放的 `(learner, subject, knowledge_component)`；Finding 必须尽量带 KC + Newman class；匹配则挂接，否则新建；粗心类不与概念类强并 |
| **自研** | 映射到 Finding/KI/Link/Event；`ki_merge.kc_newman.v0` 版本与反馈指标；本产品纸质/证据约束下的输入门槛 |

---

## 3. 对象语义（对齐领域模型）

```text
Finding (不可变)
  ├── knowledge_point_id   ← KC（课标/目录节点）
  ├── error_class          ← Newman 映射枚举（见下）
  ├── confidence
  └── evidence links

KnowledgeIssue (长期)
  ├── learner + subject_code
  ├── primary_knowledge_point_id  ← 同一 KC
  ├── issue_kind             ← CONCEPTUAL | PROCESS | CARELESS | UNCLEAR …
  └── status OPEN/MONITORING/…

FindingIssueLink
  └── merge_algorithm_version = ki_merge.kc_newman.v0
```

### Newman → `error_class`（搬运映射）

| Newman 层级 | error_class（系统枚举） | 归并策略 |
|---|---|---|
| Reading / Comprehension | `LANGUAGE_OR_COMPREHENSION` | 可并同 KC 下同类；与纯计算过程分轨 |
| Transformation | `STRATEGY_TRANSFORM` | 同 KC 可并 |
| Process skills | `PROCESS_SKILL` | 同 KC 可并 |
| Encoding | `ENCODING` | 同 KC 可并；易与粗心混淆，靠置信度 |
| Carelessness | `CARELESS` | **默认不并入** CONCEPTUAL 类 KI；可建短生命周期 CARELESS 问题或仅记 Finding |
| Motivation / Question form | `OTHER` | 待观察 KI 或不建长期问题 |

---

## 4. 自动归并算法（确定性）

对每条**允许进入归并**的 Finding（见 §5 门槛）：

### 4.1 候选集

同 `learner_id`、同 `subject_code`、状态 ∈ `{OPEN, MONITORING}` 的 KnowledgeIssue，且：

`issue.primary_knowledge_point_id == finding.knowledge_point_id`

### 4.2 决策表

| 条件 | 动作 |
|---|---|
| Finding 缺 `knowledge_point_id` 或 confidence 为 UNCONFIRMED 且无法标 KC | **不归并进概念 KI**；可建 `issue_kind=UNCLEAR` 待观察 KI，或只留 Finding + Event |
| `error_class == CARELESS` | **不挂接**开放 CONCEPTUAL KI；可选新建/挂接 `issue_kind=CARELESS`（短窗，易 CLOSED） |
| 恰好 1 个候选 KI，且 `issue_kind` 与 `error_class` 相容 | **挂接** FindingIssueLink |
| 0 个候选 | **新建** KI（kind 由 error_class 映射）+ Revision + Link |
| ≥2 个候选 | 选「最近活跃 + 同 kind」；仍冲突则新建 UNCLEAR 并 Event 标记 `merge_conflict`（**仍自动**，不停人） |

**相容（v0）：** CONCEPTUAL 类 ↔ STRATEGY_TRANSFORM / PROCESS_SKILL / LANGUAGE…；CARELESS 仅 ↔ CARELESS。

### 4.3 多 KC 题目（Conjunctive 归咎）

诊断阶段必须给出 **primary KC**（主责）。  
归并**只使用 primary**；禁止「一题错了把 Q 矩阵里所有 KC 各开/并一个 KI」。  
（学自 Conjunctive KT：错误时不应均匀归咎所有成分。）

### 4.4 LLM 的位置（可选加速，非权威）

```text
证据/作答 →（可选）LLM 建议 KC + Newman class + 置信度
         → 规则校验（目录内 KC、枚举合法）
         → 写 Finding
         → §4.2 确定性归并
```

LLM 建议被拒则降级 UNCLEAR / 人工 OCR 确认后的重诊断——**不是**人工点选归并。

---

## 5. 输入门槛（纸质闭环）

不得进入归并：

- OCR/作答未 CONFIRMED  
- 无 Evidence 链路的 Finding  
- 诊断失败产物  

---

## 6. 反馈系统（自研强制，D-030）

| 信号 | 用途 |
|---|---|
| 延迟验证：同 KC 再练对/错 | 代理「并错了/并对了」 |
| `merge_conflict` / 自动拆分 Event | 规则迭代 |
| CARELESS 误并入 CONCEPTUAL 的抽检率 | 发布门禁 |
| `ki_merge.kc_newman.v0` → v0.1… | 灰度对比错挂率、漏并率 |

**效用指标（不用 AI 时长）：** 错挂率、漏并率、UNCLEAR 占比、同 KI 上提示强度是否下降、延迟验证通过率。

不达标 → 回滚算法版本，保留 Finding 不可变与 Link 历史。

---

## 7. 为什么选这套（给产品方的说明）

1. 你们要的是**长期知识问题**，ITS 界成熟单元就是 **KC**，不是「某道题」。  
2. 数学纸质错题大量是**过程层级不同**（Newman）；不分层会把粗心和未掌握并成一团，干预会歪。  
3. 自动、可解释、可测：规则落库满足「不靠人点选」+ D-004。  
4. 反馈闭环让这只「搬运来的轮子」能变好，而不是一次性拍死。

---

## 8. 相关文档

- [reuse-and-feedback.md](../01-architecture/reuse-and-feedback.md)  
- [subject-and-catalog.md](../03-domain-model/subject-and-catalog.md)  
- [diagnosis-process.md](./diagnosis-process.md)  
- U-011：本推荐落地后，未决收窄为「评测集与阈值标定」  
