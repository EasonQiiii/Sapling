# Changelog

本项目变更记录。文档与 Migration 的重要变更应在此摘要。

## [Unreleased]

### Added

- **D-033**：标准知识体系以课标 2022 为权威基准；教材做映射；依赖关系候选制；标准体系与个人知识地图分离（产品 2026-11-13 方案 C，2026-11-16 落档）。
- 自编数学 42 点种子与 catalog v0 标为 **INVALID DRAFT**（非权威）。

### Added

- 正式项目目录结构：`docs/`、`database/`、`deployment/`、`delivery/`。
- `docs/00-overview/recovery-baseline.md`：Family Learning OS Recovery Baseline 1.0 入库。
- `PROJECT_STATUS.md`、决策登记与未决事项文档。
- 逻辑模型、架构、业务流程等首批拆分文档。
- `docs/03-domain-model/entity-dictionary.md`：Chapter 15 字段字典重建草稿（RECONSTRUCTED，已应用 C-01…C-10 修复）。
- `database/migrations/` 与 `database/tests/` 占位说明（状态均为待整合 / `NOT_RUN`）。
- `docs/DOC_MAP.md`：文档整图导航（完成度、阅读路径、三层改表规则）。
- 补全 `docs/04-physical-model/` 各域说明与 `global-conflicts.md`（G-01…G-24）。
- `docs/diagrams/erd-overview.mmd`：RECONSTRUCTED 总览图。

### Added

- 正式决策 D-025…D-028：V1 精简范围、缓建 Goal、Workflow 真表、Finding→KI **自动**归并。
- 纠正「V1 先人工归并」误默认；U-011 收窄为算法规格。
- 正式决策 D-029：产品范围为**中小学全科**，落地**先做数学**（纠正基线「仅小学四至六年级」）。
- D-031 KI 归并解法（KC+Newman）；D-032 练习建议默认自动。
- P1 教练/权限/验证规格；适配层契约；数学 KC 骨架。
- Migration `001`–`009` 可执行（005/006 DEFERRED no-op）；空库执行 **PASS**（2026-11-15）。
- Migration 空库结构 PASS；种子仅结构 smoke，**非**课标权威内容（见 D-033）。
- D-031 KI 归并；D-032 练习自动；P1 教练规格与适配契约。

### Notes

- 标准知识体系首版内容仍属 U-012；不得把 INVALID 种子当业务真相。
