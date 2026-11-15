# Family Learning OS — Documentation Map

整图导航。设计事实在文档里，不在聊天记录。

**图例：** `完整` = 可接手阅读 · `摘要` = 已拆分但仍指向基线细节 · `RECONSTRUCTED` = 非原文重建 · `PLACEHOLDER` = 待工程填充 · `NOT_RUN` = 未执行验证

## 入口（先读这五个）

| 节点 | 路径 | 状态 |
|---|---|---|
| 项目状态 | [`PROJECT_STATUS.md`](../PROJECT_STATUS.md) | 完整 |
| 恢复基线 | [`00-overview/recovery-baseline.md`](./00-overview/recovery-baseline.md) | 完整（历史视图） |
| 决策登记 | [`05-decisions/decision-register.md`](./05-decisions/decision-register.md) | 完整 |
| 未决事项 | [`05-decisions/unresolved-decisions.md`](./05-decisions/unresolved-decisions.md) | 完整 |
| 逻辑模型 | [`03-domain-model/logical-data-model.md`](./03-domain-model/logical-data-model.md) | 完整 |

## 00 Overview

| 文件 | 状态 | 下游 |
|---|---|---|
| [project-overview.md](./00-overview/project-overview.md) | 完整 | 原则、术语 |
| [product-principles.md](./00-overview/product-principles.md) | 完整 | D-001…D-006 |
| [glossary.md](./00-overview/glossary.md) | 完整 | 全库术语 |
| [recovery-baseline.md](./00-overview/recovery-baseline.md) | 完整 | 各领域拆分文档 |

## 01 Architecture

| 文件 | 状态 |
|---|---|
| [system-architecture.md](./01-architecture/system-architecture.md) | 完整 |
| [module-responsibilities.md](./01-architecture/module-responsibilities.md) | 完整 |
| [module-interfaces.md](./01-architecture/module-interfaces.md) | 摘要（schema 未冻） |
| [cross-module-collaboration.md](./01-architecture/cross-module-collaboration.md) | 完整 |
| [architecture-decisions.md](./01-architecture/architecture-decisions.md) | 完整（索引） |

图：[`diagrams/system-architecture.mmd`](./diagrams/system-architecture.mmd)

## 02 Business

| 文件 | 状态 |
|---|---|
| [learning-workflow.md](./02-business/learning-workflow.md) | 完整 |
| [paper-homework-process.md](./02-business/paper-homework-process.md) | 完整 |
| [ocr-and-correction.md](./02-business/ocr-and-correction.md) | 完整；选型 U-001 |
| [diagnosis-process.md](./02-business/diagnosis-process.md) | 完整；自动归并 D-028；算法 U-011 |
| [learning-intervention.md](./02-business/learning-intervention.md) | 完整；深度 U-013 |
| [learning-verification.md](./02-business/learning-verification.md) | 完整 |
| [parent-child-ai-boundaries.md](./02-business/parent-child-ai-boundaries.md) | 完整 |

图：[`learning-workflow.mmd`](./diagrams/learning-workflow.mmd)、[`intervention-lifecycle.mmd`](./diagrams/intervention-lifecycle.mmd)、[`data-lineage.mmd`](./diagrams/data-lineage.mmd)

## 03 Domain model（逻辑层）

| 文件 | 状态 |
|---|---|
| [domain-overview.md](./03-domain-model/domain-overview.md) | 完整 |
| [entity-catalog.md](./03-domain-model/entity-catalog.md) | 完整 |
| [entity-dictionary.md](./03-domain-model/entity-dictionary.md) | RECONSTRUCTED |
| [relationship-matrix.md](./03-domain-model/relationship-matrix.md) | RECONSTRUCTED 摘要 |
| [lifecycle-definitions.md](./03-domain-model/lifecycle-definitions.md) | 完整 |
| [logical-data-model.md](./03-domain-model/logical-data-model.md) | 完整 |

图：[`domain-relationships.mmd`](./diagrams/domain-relationships.mmd)、[`erd-overview.mmd`](./diagrams/erd-overview.mmd)

## 04 Physical model（说明层，非执行）

| 文件 | Migration | 状态 |
|---|---|---|
| [physical-model-overview.md](./04-physical-model/physical-model-overview.md) | 001–009 | 完整 |
| [global-conflicts.md](./04-physical-model/global-conflicts.md) | 001–009 / tests | 完整 G-01…G-24 |
| [platform-identity.md](./04-physical-model/platform-identity.md) | 001 | 完整 |
| [learning-assessment.md](./04-physical-model/learning-assessment.md) | 002 | 完整 |
| [evidence-event.md](./04-physical-model/evidence-event.md) | 003 | 完整 |
| [diagnosis-state.md](./04-physical-model/diagnosis-state.md) | 004 | 完整；Diagnosis 字段级部分 RECONSTRUCTED |
| [intervention.md](./04-physical-model/intervention.md) | 005 | 完整 |
| [policy-methodology.md](./04-physical-model/policy-methodology.md) | 006 | 完整；未决 U-002… |
| [decision.md](./04-physical-model/decision.md) | 007 | 完整 |
| [workflow.md](./04-physical-model/workflow.md) | 007 | 完整 |
| [ai-execution-audit.md](./04-physical-model/ai-execution-audit.md) | 008 | 完整 |

## 05 Decisions

| 文件 | 状态 |
|---|---|
| [decision-register.md](./05-decisions/decision-register.md) | 完整 D-001…D-024 |
| [unresolved-decisions.md](./05-decisions/unresolved-decisions.md) | 完整 U-001…U-017 |
| [superseded-decisions.md](./05-decisions/superseded-decisions.md) | 完整（暂无废止项） |

## 06 Validation

| 文件 | 状态 |
|---|---|
| [logical-model-review.md](./06-validation/logical-model-review.md) | 部分 PASS / 部分缺失 |
| [physical-model-review.md](./06-validation/physical-model-review.md) | NOT_RUN 为主 |
| [migration-validation.md](./06-validation/migration-validation.md) | NOT_RUN |
| [end-to-end-validation.md](./06-validation/end-to-end-validation.md) | 设计层 PASS；SQL NOT_RUN |
| [privacy-security-validation.md](./06-validation/privacy-security-validation.md) | NOT_RUN |
| [design-gap-audit.md](./06-validation/design-gap-audit.md) | **对照目的/D-025…D-029 的设计缺口** |

## 07 Delivery

| 文件 | 状态 |
|---|---|
| [v1-freeze-report.md](./07-delivery/v1-freeze-report.md) | 未冻结清单 |
| [v1-slice-proposal.md](./07-delivery/v1-slice-proposal.md) | **已确认** D-025…D-028（精简 + 自动归并） |
| [known-limitations.md](./07-delivery/known-limitations.md) | 完整 |
| [v2-backlog.md](./07-delivery/v2-backlog.md) | 完整 |

## Database / Deployment / Delivery artifacts

| 节点 | 状态 |
|---|---|
| [`database/README.md`](../database/README.md) | 完整（三层规则） |
| `database/migrations/001…009.sql` | PLACEHOLDER |
| `database/tests/*.sql` | PLACEHOLDER · NOT_RUN |
| `database/seeds/development-seed.sql` | PLACEHOLDER |
| [`deployment/`](../deployment/) | 脚手架 |
| [`delivery/`](../delivery/) | 报告副本；zip 未生成 |

## 阅读路径（推荐）

```text
README
  → PROJECT_STATUS
  → docs/DOC_MAP (本文件)
  → 00 recovery-baseline + principles
  → 01 architecture
  → 02 paper-homework-process (主业务闭环)
  → 03 logical-data-model + entity-dictionary
  → 04 physical-model-overview
  → 05 decisions + unresolved
  → 06 validation (诚实结果)
  → database/README (仅当开始写 SQL)
```

## 三层改表规则

1. 业务语义变 → 更新 `03-domain-model/` + 决策 ID  
2. 表/约束设计变 → 更新 `04-physical-model/`  
3. 可执行结构变 → 只改 `database/migrations/` 并跑验证写入 `06-validation/`  

禁止把聊天分批 SQL 直接拼进最终 Migration（D-020）。
