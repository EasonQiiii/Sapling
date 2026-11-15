# Unresolved Decisions

未决事项。**不得**视为已确认设计。关闭时移入 `decision-register.md` 并分配 `D-xxx`。

| ID | 主题 | 描述 | 阻塞影响 | 建议方向 |
|---|---|---|---|---|
| U-001 | OCR 选型 | PaddleOCR / Surya / pix2latex / TrOCR 等均未最终选型 | 纸质闭环无法工程落地 | 真实试卷样本 + 适配层；不凭公开 Benchmark 定案 |
| U-002 | PolicyPublication 冲突 | 范围继承与时间区间冲突规则未冻结 | Policy 生效语义不清 | 先定 FAMILY 范围，再扩展 TASK |
| U-003 | TASK 层 Policy | 任务归属与唯一性未确认 | 任务级策略无法实现 | V1 可仅 SYSTEM+FAMILY |
| U-004 | PolicyRelation 双层冲突 | 策略级与版本级关系并存时的处理 | 发布/校验不确定 | Engine 内明确优先级表 |
| U-005 | Policy Template | 是否需要尚未确认 | 可延后 | V1 不做 |
| U-006 | Workflow 图发布校验 | 完整规则集未定 | 定义发布门禁缺失 | 最小集：START/END、可达、分支完整、有退出的环 |
| U-007 | WorkflowRun 版本迁移 | 旧运行迁移策略未定 | 流程升级风险 | V1：旧运行不升级（已倾向）需正式写入 D |
| U-008 | Policy 检查点结果表 | 是否独立持久化 | 审计粒度 | 先 Event/审计，必要时再加表 |
| U-009 | GuidanceStrategy Schema | JSONB schema 未定 | Methodology 实现 | 先枚举强度与工具，再锁 schema |
| U-010 | 部分 JSONB Schema | StateContent 等 | 状态内容无法校验 | 按状态类型逐步冻结 |
| U-011 | Finding→KnowledgeIssue 归并**算法** | 是否自动已由 D-028 确认；置信度、合并/拆分、新建 vs 挂接策略未规格化 | 自动归并质量 | 写规则 v0 + 评测集；不改回人工闸门 |
| U-012 | 知识目录 ontology | knowledge_point / capability 目录缺失；需支持中小学多科目（D-029） | State/KI 无处附着 | v0 先数学；目录结构预留学段+科目扩展 |
| U-013 | Intervention V1 深度 | Stage 是否进 V1 | 已由 D-025 缓建 Stage | **关闭条件：** 补「薄干预行为规格」后可标 Resolved→D |
| U-014 | 隐私删除治理 | 受控删除 vs append-only Audit | 合规 | 完整治理设计后再实现 |
| U-015 | G-01…G-24 SQL 整合 | 物理冲突清单未在可执行 Migration 中收口 | 无法空库验收 | 见物理模型与 migrations README |
| U-016 | ERD Mermaid A–J | 第16章子图原文未恢复 | 关系图缺失 | 按 entity-catalog 重建并标 RECONSTRUCTED |
| U-017 | 数据库角色权限 | 防应用角色绕过触发器 | 约束可被绕过 | 部署前定义角色矩阵 |

## 使用规则

- 实现或文档中引用未决项时必须写 `U-xxx`，并保持 `NOT CONFIRMED`。
- AI / 开发接手时先读本文件，避免把未决当已定。
