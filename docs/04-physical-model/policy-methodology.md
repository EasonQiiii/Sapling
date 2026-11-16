# Physical model: Policy / Methodology

**Migration target:** `006_policy_methodology.sql`  
**Status:** 逻辑设计已恢复；具体 SQL 不完整（batch 21）。

## Policy tables

| Table | Role |
|---|---|
| `policy` | 策略稳定身份 |
| `policy_version` | 不可变版本 |
| `policy_publication` | 发布与生效（≠ 当前草稿版本） |
| `policy_relation` | 关系；支持策略级与版本级（C-07） |
| `policy_simulation` | 发布前模拟 |
| `policy_evaluation` | 实际效果评价 |
| `policy_evaluation_target` / `policy_evaluation_reference` | 评价对象与依据 |

### Policy rules

- 层级：SYSTEM / FAMILY / TASK
- 同一 Policy、范围不得有冲突的同时生效版本
- 范围继承与时间冲突：**未冻结**（U-002）
- TASK 归属/唯一性：**未冻结**（U-003）
- 双层 PolicyRelation 冲突：**未冻结**（U-004）
- **不**建 `policy_registry` 表（C-10 / D-017）
- Policy Template：倾向 V1 不做（U-005）

## Methodology tables

| Table | Role |
|---|---|
| `methodology` | 方法稳定身份 |
| `methodology_version` | 不可变版本 |
| `guidance_strategy` | 属于明确 MethodologyVersion |

- V1 **不**强制 `guidance_execution` 业务表（D-015）
- GuidanceStrategy JSONB schema 未定（U-009）

Validation: `NOT_RUN`
