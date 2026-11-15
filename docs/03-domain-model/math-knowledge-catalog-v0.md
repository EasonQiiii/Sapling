# 数学知识目录 v0（搬运骨架）

**决策：** D-029、D-030、D-031；U-012  
**状态：** 骨架 + 首批节点；完整课标树持续搬运填充  

## 学自 / 搬运 / 自研

| | 内容 |
|---|---|
| **学自** | 义务教育数学课程标准内容领域组织（数与代数 / 图形与几何 / 统计与概率 / 综合与实践）；教材章–节知识点 |
| **搬运** | 领域→主题→知识点树；稳定 `Code`；`CurriculumRef` 标注来源意图 |
| **自研** | 无教育内容发明；仅系统 ID 与种子格式 |

## Subject

`SubjectCode = MATH`（其他科目占位不建点）

## 树结构（v0 示例节点 — 服务首闭环，可增）

编码约定：`MATH.<stage>.<domain>.<topic>.<leaf>`

### 小学（PRIMARY）示例

| Code | Title | Parent |
|---|---|---|
| MATH.P.NA | 数与代数 | — |
| MATH.P.NA.FRAC | 分数 | MATH.P.NA |
| MATH.P.NA.FRAC.MEANING | 分数意义 | MATH.P.NA.FRAC |
| MATH.P.NA.FRAC.ADD_SAME | 同分母加减 | MATH.P.NA.FRAC |
| MATH.P.NA.FRAC.ADD_DIFF | 异分母加减 | MATH.P.NA.FRAC |
| MATH.P.NA.DEC | 小数 | MATH.P.NA |
| MATH.P.NA.DEC.ADD | 小数加减 | MATH.P.NA.DEC |
| MATH.P.NA.RATIO | 比和比例入门 | MATH.P.NA |
| MATH.P.GEO | 图形与几何 | — |
| MATH.P.GEO.AREA | 面积 | MATH.P.GEO |
| MATH.P.STAT | 统计与概率 | — |

### 初中（JUNIOR_SECONDARY）示例

| Code | Title | Parent |
|---|---|---|
| MATH.J.NA | 数与式 | — |
| MATH.J.NA.LINEAR | 一次方程 | MATH.J.NA |
| MATH.J.NA.LINEAR.ONE | 一元一次方程 | MATH.J.NA.LINEAR |
| MATH.J.GEO | 图形与几何 | — |
| MATH.J.GEO.TRI | 三角形 | MATH.J.GEO |
| MATH.J.FUNC | 函数萌芽 | — |
| MATH.J.FUNC.LINEAR | 一次函数入门 | MATH.J.FUNC |

> 正式填充时以课标官方条目为准批量导入；本表为可运行骨架，保证归并/State 有挂点。

## 种子文件目标

`database/seeds/math_knowledge_points_v0.sql`（Migration 可跑后落地；当前以本文为源）。
