# 能力迁移复核（CAPABILITY_MIGRATION_REVIEW）

> 生成时间：2026-11-17 14:42:36  
> 状态：**已执行**（2026-11-17，A2-07→CAP-01、A4-10→CAP-05 迁移落地）

## 背景

文件：`小学/数学/数与运算.yaml`

| ID | 仍在 knowledge_points | id_management | 已有 CAP |
|---|---|---|---|
| A2-07 数的大小比较 | 是（且 `type: cross_domain_capability`） | `reclassify` → cross_domain_capability | CAP-01 同名 |
| A4-10 运算方法选择 | 是（且 `type: cross_domain_capability`） | `reclassify` → cross_domain_capability | CAP-05 同名 |

二者已同时以 KP 与 CAP 双轨存在，定义高度重复，必须完成迁移并消除双绑。

---

## 1. A2-07 ↔ CAP-01

### A2-07 完整内容摘要

- **定义**：根据数的意义、计数单位和表示形式，判断两个或多个数之间的大小关系。
- **学习目标**：比较整数/小数/分数大小；选择比较方法；解释依据。
- **诊断维度**：integer_comparison / decimal_comparison / fraction_comparison / mixed_comparison / reasoning
- **prerequisites（KP）**：A2-01, A2-02, A2-03
- **curriculum_mapping**：stage_1 万以内比较；stage_2 小数分数初步比较；stage_3 综合应用
- **notes**：作为跨数域能力，不与具体数的表示概念并列。

### CAP-01 现况

- **name**：数的大小比较
- **description**：跨数域比较数的大小。（过简）
- **source_knowledge**：A2-01, A2-02, A2-03, A2-04
- **无** diagnostic_dimensions / learning_objectives 字段

### 结论

**实质重复。** CAP-01 应吸收 A2-07 的目标与诊断；A2-07 移出 knowledge_points。

### 迁移方案（字段级）

| 步骤 | 文件 | 位置 | 动作 |
|---|---|---|---|
| 1 | `小学/数学/数与运算.yaml` | `modules` 内 A2 模块 `knowledge_points` | **删除** A2-07 条目 |
| 2 | 同上 | `cross_domain_capabilities` 中 CAP-01 | **合并增强**：写入 description（用 A2-07 definition）、补充 `diagnostic_dimensions`（移植 A2-07 五维）、`source_knowledge` 保留并含 A2-01~A2-04、可增 `curriculum_notes` |
| 3 | 同上 | `id_management.legacy_id_handling` 中 A2-07 | `action: reclassified` / `canonical_capability_id: CAP-01` / `removed_from: knowledge_points` |
| 4 | 题库绑定 | primary_knowledge=A2-07 | 改为 capability_tags=`CAP-01`，并视题面挂具体数域 KP（如只比整数则 secondary A2-01） |

### 引用检查

| 引用方 | 文件 | 字段 | 现状 | 修订 |
|---|---|---|---|---|
| A5-02 | `初中/数学/数与运算.yaml` | prerequisites | 文本“小学数与运算：数的大小比较”；R2 曾改为 A2-07 | **禁止**改为 CAP-01 作前置。改为具体 KP：`A2-01`（必要）；可选 `A2-02`,`A2-03`。比较技能用 CAP-01 仅作能力标签，不进 prerequisites |
| A5-04 | 同上 | notes | “小学已有的数的大小比较作为前置” | 改为叙述性 notes，前置仍用 A5-01/A5-02/A5-03；能力侧 CAP-01 |
| 课标映射 CR-002 等 | 审计/题蓝图 | mapped KP | 含 A2-07 | 改为 CAP-01 + 相关数域 KP |
| 小学内部 KP | — | prerequisites | **无**其它 KP 依赖 A2-07 | — |

### 规则

> **不允许能力 ID（CAP-*）继续作为 prerequisite。**

A5-02 建议前置最终值：

```yaml
# 初中/数学/数与运算.yaml  A5-02.prerequisites
- A5-01
- A2-01
# 可选（若数轴题大量涉及小数/分数刻度）：
# - A2-02
# - A2-03
```

---

## 2. A4-10 ↔ CAP-05

### A4-10 摘要

- **定义**：根据数的特点、运算关系和问题要求，选择合理、简洁且正确的运算方法。
- **学习目标**：按算式选方法；使用运算律/性质；解释依据。
- **诊断**：method_selection / law_application / property_application / reasoning
- **prerequisites**：A4-01, A4-02, A4-03, A4-06, A4-07

### CAP-05 现况

- **name**：运算方法选择
- **description**：根据问题特点选择直接计算、运算律、运算性质或其他合适方法。
- **source_knowledge**：A3-01~04, A4-01~03, A4-06, A4-07
- **diagnostic_dimensions**：策略识别/选择/执行/解释（已有，与 A4-10 同义）

### 结论

**实质重复。** 以 CAP-05 为唯一能力 ID；A4-10 移出 knowledge_points；把 A4-10 更细的诊断命名可合并进 CAP-05（或保留 CAP-05 现维，在 notes 说明对应关系）。

### 迁移方案

| 步骤 | 文件 | 位置 | 动作 |
|---|---|---|---|
| 1 | `小学/数学/数与运算.yaml` | A4 模块 knowledge_points | **删除** A4-10 |
| 2 | 同上 | CAP-05 | 可选增强 description 吸收 A4-10 表述；source_knowledge 已覆盖 |
| 3 | id_management A4-10 | legacy | `canonical_capability_id: CAP-05` |
| 4 | 引用 | — | 当前无其它 KP 将 A4-10 列为 prerequisites；题库若有绑定则改 CAP-05 |

### 初中对照

`初中/数学/数与运算.yaml` 已有 `A-CAP-07 运算方法选择`，与 CAP-05 同层能力、不同学段命名空间——保持，不把 CAP-05 写入初中 prerequisites。

---

## 3. 迁移后统计影响（批准执行时）

| 项 | 变化 |
|---|---|
| 小学 KP 记录 | 100 → 98（再扣 A3-06 alias 后有效更少） |
| 能力 | CAP-01/CAP-05 成为正式比较/方法选择承载 |
| 前置图 | 去除一切指向 A2-07/A4-10/CAP-* 的 prerequisite 边 |

---

## 4. 验收标准

- [ ] knowledge_points 中无 A2-07、A4-10  
- [ ] CAP-01/CAP-05 含足够诊断信息  
- [ ] 全局 prerequisites 无 CAP-*、无 A2-07/A4-10  
- [ ] A5-02 前置为具体小学 KP ID  
- [ ] 课标映射中比较类要求改挂 CAP-01 + 数域 KP  
