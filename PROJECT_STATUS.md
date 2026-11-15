# PROJECT_STATUS

**最后更新：** 2026-11-15 21:08（Asia/Shanghai）  
**项目状态：** 产品边界确认为中小学全科、先做数学（D-029）；V1 精简 D-025…D-028 已确认  
**当前分支目标：** 按闭环优先级推进（数学首闭环）；Migration 为落库手段而非第一步

## 已完成

- [x] Recovery Baseline 1.0 整理（历史设计恢复，非逐字聊天还原）
- [x] 产品定位、原则、模块架构、核心业务流程（设计层）
- [x] 逻辑领域模型主体与一致性审查结论（设计层）
- [x] 物理模型主体设计与 G-01…G-24 冲突清单（设计层）
- [x] 正式仓库目录结构（docs / database / deployment / delivery）
- [x] 重建 Chapter 15 字段字典草稿（`entity-dictionary.md`，标记 RECONSTRUCTED）
- [x] `docs/DOC_MAP.md` 整图导航 + 各物理模型节点补全
- [x] `docs/04-physical-model/global-conflicts.md`（G-01…G-24 地图）

## 进行中

- [ ] 按 D-025…D-028 精简范围起草可执行 PostgreSQL Migration（当前仍 PLACEHOLDER）
- [ ] U-011：自动归并算法 v0（不再争论人工/自动）
- [ ] U-012：知识目录 v0 种子

## 当前问题 / 阻塞

1. 第15～23批完整 PostgreSQL DDL 原文未完全恢复（尤其 Diagnosis 字段级、Policy SQL）。
2. 第16章 ERD 十个子图 Mermaid 原文缺失。
3. OCR 技术未最终选型。
4. PolicyPublication 范围/时间冲突等设计未冻结（见 unresolved-decisions）。
5. 无真实空库 Migration 执行记录；任何测试均为 `NOT_RUN`。

## 下一步（建议顺序）

1. 补全 / 标注 `RECONSTRUCTED` 的物理模型与 Migration。
2. 建立干净 PostgreSQL 环境，从空库执行 Migration。
3. 跑 FK / 唯一性 / CHECK / 触发器 / 并发 / E2E / 隐私测试，并写入 `docs/06-validation/`。
4. 仅在真实执行通过后更新冻结报告；未执行不得标 PASS。
5. 生成 `delivery/` 版本快照。

## 关键文档

| 文档 | 路径 |
|---|---|
| **整图导航** | `docs/DOC_MAP.md` |
| 恢复入口 | `docs/00-overview/recovery-baseline.md` |
| 决策登记 | `docs/05-decisions/decision-register.md` |
| 未决事项 | `docs/05-decisions/unresolved-decisions.md` |
| 逻辑模型 | `docs/03-domain-model/logical-data-model.md` |
| 字段字典 | `docs/03-domain-model/entity-dictionary.md` |
| G 清单 | `docs/04-physical-model/global-conflicts.md` |
| 已知限制 | `docs/07-delivery/known-limitations.md` |
