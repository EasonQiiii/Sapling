# Family Learning OS（家庭 AI 学习管家）

面向**中小学全科**的家庭学习系统（落地先做数学）。目标是帮助孩子形成可迁移的底层学习能力，而不是仅仅提高某次作业或考试成绩。

> 设计文档是设计事实的来源，聊天记录不是。

## 快速入口

| 文件 | 用途 |
|---|---|
| [docs/DOC_MAP.md](docs/DOC_MAP.md) | **整图导航**（完成度图例 + 阅读路径） |
| [PROJECT_STATUS.md](PROJECT_STATUS.md) | 当前进度、阻塞、下一步 |
| [docs/00-overview/recovery-baseline.md](docs/00-overview/recovery-baseline.md) | 历史设计恢复入口 |
| [docs/05-decisions/decision-register.md](docs/05-decisions/decision-register.md) | 已确认决策（D-xxx） |
| [docs/05-decisions/unresolved-decisions.md](docs/05-decisions/unresolved-decisions.md) | 未决事项 |
| [docs/03-domain-model/logical-data-model.md](docs/03-domain-model/logical-data-model.md) | 逻辑领域模型 |

## 目录结构

```
docs/00-overview/      项目概述、原则、术语、恢复基线
docs/01-architecture/  系统架构与模块边界
docs/02-business/      业务流程
docs/03-domain-model/  业务与逻辑模型（设计事实）
docs/04-physical-model/物理表结构及约束设计（解释，非执行）
docs/05-decisions/     决策登记 / 未决 / 废止
docs/06-validation/    验收与测试结果记录
docs/07-delivery/      冻结报告、限制、backlog
docs/diagrams/         Mermaid 图源

database/migrations/   可实际执行的 PostgreSQL Migration
database/tests/        结构与业务验收 SQL
database/seeds/        开发种子数据

deployment/            Docker Compose 等部署文件
delivery/              版本快照与交付物
```

## 三层模型约定

不要把聊天中的分批 SQL 直接拼成最终 Migration。

1. **`docs/03-domain-model/`** — 业务与逻辑模型  
2. **`docs/04-physical-model/`** — 物理表结构及约束设计  
3. **`database/migrations/`** — 经过整合、可以实际执行的 SQL  

修改表结构时，先更新物理模型说明，再改 Migration；逻辑模型仅在业务语义变化时更新。

## 维护规则

- 重要决策分配唯一 ID（`D-001`…），变更时保留旧决策与原因，不覆盖历史。
- SQL Migration 是数据库结构的执行来源；物理模型文档负责解释设计。
- 每次测试记录 `PASS` / `FAIL` / `NOT_RUN`；未执行验证不得标记 PASS。
- `PROJECT_STATUS.md` 记录最后更新时间、已完成工作、当前问题与下一步。
- 每次交付提供版本快照，不依赖聊天临时内容。

## 当前状态

见 [PROJECT_STATUS.md](PROJECT_STATUS.md)。总体：设计成果较完整，工程交付（可执行 Migration / 真实测试）尚未完成。
