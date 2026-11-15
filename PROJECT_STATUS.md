# PROJECT_STATUS

**最后更新：** 2026-11-15 21:15（Asia/Shanghai）  
**项目状态：** D-030 搬运优先已立；P0 四份规格初稿已写（学自/搬运/自研分栏）  
**当前分支目标：** 按闭环推进 P1 教练性规格；实现时继续搬运成熟体系

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

- [x] D-030 + reuse-and-feedback 原则
- [x] P0：`subject-and-catalog.md` / `auto-merge-rules-v0.md` / `closed-loop-steps.md` / `ocr-human-boundary.md`
- [ ] P1：薄干预/决策权限/验证（须标明学自 ITS/间隔复习等）
- [ ] U-012：数学目录内容从课标/教材树搬运填充
- [ ] 其后：精简 Migration / 原型（PLACEHOLDER 直至可执行）

## 当前问题 / 阻塞

1. **闭环规格不足**（守卫/角色/异常未写清；见 design-gap-audit）。
2. **自动归并无算法**（只有 D-028 原则）。
3. **科目可扩展未落到实体字段**（D-029）。
4. OCR 适配层与人机边界未澄清；引擎选型可后定。
5. Migration/G 清单/ERD 等为后置工程项，不挡 P0 设计。

## 下一步（建议顺序）

1. 按 `docs/06-validation/design-gap-audit.md` 补齐 P0。  
2. 补 P1 教练性规格（薄干预 + 验证）。  
3. 再写可执行 Migration / 可跑原型。  
4. 空库与闭环验收；未执行不得 PASS。

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
