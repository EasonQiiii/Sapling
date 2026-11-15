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

### Notes

- 尚未包含可执行的完整 PostgreSQL Migration 正文。
- 未执行数据库验收；无 PASS 测试结果。
