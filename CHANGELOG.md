# Changelog

本项目变更记录。文档与 Migration 的重要变更应在此摘要。

## [Unreleased]

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
- Migration `001`/`002` 可执行草稿（空库验证仍 NOT_RUN）。

### Notes

- 文档地图（设计层）已闭合；可执行 Migration 仍未整合。
- 未执行数据库验收；无工程 PASS 测试结果。
