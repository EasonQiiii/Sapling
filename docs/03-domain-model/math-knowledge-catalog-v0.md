# 数学知识目录 v0（搬运填充）

**决策：** D-029、D-030、D-031；U-012  
**状态：** 可种子化节点集（首闭环 + 常见小学/初中主题）；来源意图=义务教育数学课标内容领域组织  

## 学自 / 搬运 / 自研

| | 内容 |
|---|---|
| **学自** | 义务教育数学课程标准四大领域：数与代数、图形与几何、统计与概率、综合与实践；学段分小学/初中 |
| **搬运** | 领域→主题→要点树与稳定 Code；`curriculum_ref` 标注课标领域 |
| **自研** | 无。仅 UUID 种子与编码约定 |

编码：`MATH.<P|J>.<DOMAIN>.<TOPIC>.<LEAF>`  
种子：`database/seeds/math_knowledge_points_v0.sql`

### 小学 PRIMARY

| Code | Title | Parent | curriculum_ref |
|---|---|---|---|
| MATH.P.NA | 数与代数 | — | 课标·数与代数 |
| MATH.P.NA.INT | 整数与运算 | MATH.P.NA | 课标·数与代数 |
| MATH.P.NA.INT.ADD_SUB | 整数加减 | MATH.P.NA.INT | |
| MATH.P.NA.INT.MUL_DIV | 整数乘除 | MATH.P.NA.INT | |
| MATH.P.NA.FRAC | 分数 | MATH.P.NA | |
| MATH.P.NA.FRAC.MEANING | 分数意义 | MATH.P.NA.FRAC | |
| MATH.P.NA.FRAC.ADD_SAME | 同分母加减 | MATH.P.NA.FRAC | |
| MATH.P.NA.FRAC.ADD_DIFF | 异分母加减 | MATH.P.NA.FRAC | |
| MATH.P.NA.FRAC.MUL | 分数乘法 | MATH.P.NA.FRAC | |
| MATH.P.NA.FRAC.DIV | 分数除法 | MATH.P.NA.FRAC | |
| MATH.P.NA.DEC | 小数 | MATH.P.NA | |
| MATH.P.NA.DEC.MEANING | 小数意义 | MATH.P.NA.DEC | |
| MATH.P.NA.DEC.ADD | 小数加减 | MATH.P.NA.DEC | |
| MATH.P.NA.DEC.MUL_DIV | 小数乘除 | MATH.P.NA.DEC | |
| MATH.P.NA.PCT | 百分数 | MATH.P.NA | |
| MATH.P.NA.RATIO | 比和比例入门 | MATH.P.NA | |
| MATH.P.GEO | 图形与几何 | — | 课标·图形与几何 |
| MATH.P.GEO.SHAPE | 认识图形 | MATH.P.GEO | |
| MATH.P.GEO.LEN | 长度与周长 | MATH.P.GEO | |
| MATH.P.GEO.AREA | 面积 | MATH.P.GEO | |
| MATH.P.GEO.VOL | 体积与容积 | MATH.P.GEO | |
| MATH.P.GEO.ANGLE | 角 | MATH.P.GEO | |
| MATH.P.STAT | 统计与概率 | — | 课标·统计与概率 |
| MATH.P.STAT.CHART | 统计图表 | MATH.P.STAT | |
| MATH.P.STAT.AVG | 平均数 | MATH.P.STAT | |
| MATH.P.PRAC | 综合与实践 | — | 课标·综合与实践 |

### 初中 JUNIOR_SECONDARY

| Code | Title | Parent | curriculum_ref |
|---|---|---|---|
| MATH.J.NA | 数与式 | — | 课标·数与代数 |
| MATH.J.NA.RATIONAL | 有理数 | MATH.J.NA | |
| MATH.J.NA.EXPR | 整式 | MATH.J.NA | |
| MATH.J.NA.LINEAR | 方程 | MATH.J.NA | |
| MATH.J.NA.LINEAR.ONE | 一元一次方程 | MATH.J.NA.LINEAR | |
| MATH.J.NA.LINEAR.SYS | 二元一次方程组 | MATH.J.NA.LINEAR | |
| MATH.J.NA.INEQ | 不等式 | MATH.J.NA | |
| MATH.J.GEO | 图形与几何 | — | 课标·图形与几何 |
| MATH.J.GEO.LINE | 相交线与平行线 | MATH.J.GEO | |
| MATH.J.GEO.TRI | 三角形 | MATH.J.GEO | |
| MATH.J.GEO.QUAD | 四边形 | MATH.J.GEO | |
| MATH.J.GEO.CIRCLE | 圆 | MATH.J.GEO | |
| MATH.J.FUNC | 函数 | — | 课标·数与代数 |
| MATH.J.FUNC.LINEAR | 一次函数 | MATH.J.FUNC | |
| MATH.J.STAT | 统计与概率 | — | 课标·统计与概率 |
| MATH.J.STAT.DATA | 数据收集与整理 | MATH.J.STAT | |

其他科目仅 `SubjectCode` 占位，不建点。
