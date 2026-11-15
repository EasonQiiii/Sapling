# PROJECT_STATUS

**最后更新：** 2026-11-15 21:10（Asia/Shanghai）  
**项目状态：** 已出设计缺口审核（闭环优先）；P0 为科目扩展/归并算法/逐步规格/OCR 人机边界  
**当前分支目标：** 按 `docs/06-validation/design-gap-audit.md` 补 P0 设计，再进入实现/落库

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

- [ ] P0 设计：学段/科目扩展字段 + 目录骨架（D-029 / U-012）
- [ ] P0 设计：自动归并算法 v0（D-028 / U-011）
- [ ] P0 设计：纸质闭环逐步规格 + OCR 人机边界
- [ ] P1 设计：薄干预/决策权限/验证（教练性）
- [ ] 其后：精简 Migration / 原型（仍 PLACEHOLDER 直至可执行）

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
