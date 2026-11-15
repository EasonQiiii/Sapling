# Physical model: Platform / Identity

**Migration target:** `001_platform_identity.sql`  
**Status:** Design recovered from baseline Ch21 / batch 15. Executable SQL: PLACEHOLDER.

## Tables

| Table | Role |
|---|---|
| `family` | 家庭租户 |
| `person` | 自然人 |
| `account` | 系统账号 |
| `account_person_link` | 账号↔人 |
| `family_member` | 家庭成员关系 |
| `child_autonomy_profile` | 孩子自主权配置头 |
| `autonomy_profile_revision` | 自主权不可变修订 |
| `authorization` | 授权记录 |
| `authorization_reference` | 授权依据引用 |
| `on_behalf_of` | 代操作关系 |

## Key rules

- UUID 主键；时间 `TIMESTAMPTZ`
- `family_member` 复合唯一：`UNIQUE(id, family_id, member_role)`（G-01）
- 家庭数据隔离以 `family_id` 为租户边界
- 授权与审计最终需真 FK 对齐（G-19 / batch 23）
- 隐私删除走受控治理，不能普通 DELETE 了事（U-014）

## Open

- 完整列级 DDL 待整合进 Migration
- 角色权限防绕过触发器（U-017）
- Validation: `NOT_RUN`
