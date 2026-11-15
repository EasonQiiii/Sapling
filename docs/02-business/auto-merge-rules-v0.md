# Finding → KnowledgeIssue 自动归并规则 v0

**决策：** D-028（必须自动）、D-030（搬运优先）、D-004（AI 非事实）  
**状态：** 算法规格 v0（可迭代）  

## 学自 / 搬运 / 自研

| | 内容 |
|---|---|
| **学自** | 教育测量/数学教育中的**错因与知识点归属**思路；数据领域**实体解析（entity resolution）**的「匹配→合并/新建」；知识追踪里「同一技能多次观测」 |
| **搬运** | 匹配键以 **知识点 ID + 错因类型** 为主；阈值：挂接已有开放 KI，否则新建；低置信不硬并，标 UNCONFIRMED/待观察 |
| **自研** | 本产品对象映射（Finding/KI/Link/Event）与**反馈指标**；不发明全新教育心理学理论 |

## 流水线位置

`批量诊断 → Finding（不可变）→ **自动归并服务** → FindingIssueLink →（可选）KI Revision 摘要更新 → Event`

无人点选闸门。家长不参与「是否合并」；抽检仅用于反馈训练/质检（≠ 上线闸门）。

## 匹配键（v0，可解释）

对每条 Finding（须已尽量带 `knowledge_point_id` 与 `finding_type` / 错因码）：

1. **硬键：** `learner_id + subject_code + knowledge_point_id + error_code`  
2. **候选 KI：** 同学习者、同科目、状态 ∈ {OPEN, MONITORING}，硬键匹配或同 knowledge_point 且错因相容  
3. **决策：**
   - 唯一高置信候选 → **挂接**（新建 FindingIssueLink）  
   - 无候选 → **新建** KnowledgeIssue + Revision + Link  
   - 多候选冲突或缺 knowledge_point → 新建「待观察」KI 或 Link 到 UNCONFIRMED 效力，**不**停等人工  

> v0 不做黑盒大模型「随便并」；模型若参与，只产出**候选与分数**，最终以规则服务落库（D-004）。

## 与成熟掌握度的关系

State 更新可在归并后触发；掌握度公式**优先简化搬运 BKT/mastery 计数思想**（对则升、错则降的可解释规则），细节见后续 State schema——此处只保证 KI 挂点正确。

## 反馈系统（自研部分强制）

| 信号 | 用途 |
|---|---|
| 延迟验证对错 | 错并/漏并代理指标 |
| KI 自动拆分/再挂接事件 | 归并版本迭代 |
| 抽检不一致率 | 版本发布门禁 |
| `merge_algorithm_version` | 写在 Event/Link 元数据 |

指标示例：错挂率、应并未并率、UNCONFIRMED 占比。不达标则回滚算法版本。

## 样例（数学，手写预期）

| 场景 | 期望 |
|---|---|
| 同分母加减连续 3 次同类错 | 挂同一 KI |
| 一次粗心计算、知识点不同 | 不与「概念未掌握」KI 强行合并 |
| OCR 未确认题 | 不进入归并输入 |

（完整样卷集后续放 `docs/06-validation/`。）

## 相关

- U-011（本文件关闭「要不要自动」，保留「算法迭代」）  
- `diagnosis-process.md`  
