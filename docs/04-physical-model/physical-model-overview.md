# 物理模型总览

**层次：** 本目录解释物理表与约束设计。  
**执行源：** 仅 `database/migrations/`。  
**禁止：** 将第30章聊天批次 SQL 直接拼接为最终 Migration（D-020）。

## 数据库

- PostgreSQL 核心库；大文件对象存储。  
- V1：单实例，按逻辑域分 schema。  
- V1 不强制：Redis、独立 MQ、独立向量库。  
- 重要 Event：Transactional Outbox（D-019）。  

## Schema 规划

`platform`, `identity`, `learning`, `assessment`, `evidence`, `diagnosis`, `decision`, `policy`, `workflow`, `methodology`, `ai_execution`, `audit`

## 推荐 Migration 顺序

见 `database/migrations/`（001…009）。最终按真实 FK 依赖拓扑排序。

## 全局字段规范

| 概念 | 规范 |
|---|---|
| ID | UUID |
| 时间 | TIMESTAMPTZ |
| 命名 | snake_case |
| 幂等 | execution_request_id |
| 链路 | correlation_id / causation_id |
| 并发 | status_revision（历史表）；OCC 参数不入库 |
| 修订 | revision_number / current_revision_id |

## 冲突清单 G-01…G-24

完整表：[global-conflicts.md](./global-conflicts.md)。  
未决跟踪：[unresolved-decisions U-015](../05-decisions/unresolved-decisions.md)。  
收口前 Migration 不得宣称完成。

## 子文档

| 文件 | 批次对应 |
|---|---|
| platform-identity.md | Ch21 / batch15 |
| learning-assessment.md | Ch21 / batch16 |
| evidence-event.md | Ch22 / batch17 |
| diagnosis-state.md | Ch22–23 / batch18–19 |
| intervention.md | Ch25 / batch20 |
| policy-methodology.md | Ch26 / batch21 |
| decision.md / workflow.md | Ch24+26 / batch22 |
| ai-execution-audit.md | Ch27 / batch23 |
