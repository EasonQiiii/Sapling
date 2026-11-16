# Physical model: Evidence / Event

**Migration target:** `003_evidence_event.sql`  
**Status:** Design recovered Ch22 / batch 17.

## Tables

| Table | Role |
|---|---|
| `evidence` | 证据头；内容不可变 |
| `evidence_source` | 来源描述 |
| `evidence_relation` | 证据谱系（多父、禁自环、无环） |
| `evidence_link` | 通用多态引用目标 |
| `learning_event` | 业务事实事件；append-only |
| `event_relation` | 事件关系 |
| `event_evidence_link` | 事件↔证据 |
| `transactional_outbox` | 可靠发布 |

## Evidence content storage

`INLINE_JSON` · `OBJECT_STORAGE` · `EXTERNAL_URI` · `REFERENCE_ONLY`

## Evidence status

`ACTIVE` · `WITHDRAWN` · `INVALIDATED` · `PENDING_DELETION` · `DELETED`

## EvidenceRelation types

`DERIVED_FROM` · `CORRECTED_FROM` · `TRANSFORMED_FROM` · `AGGREGATED_FROM` · `EXTRACTED_FROM` · `RELATED_TO`

## LearningEvent

保存：`event_type`, `event_schema_version`, subject/actor refs, `occurred_at`, `recorded_at`, `event_sequence`, `correlation_id`, `causation_id`, `event_payload`, `family_id`。  
Event 是事实不是命令。

## Outbox

- `publication_status`: PENDING / PUBLISHING / PUBLISHED / FAILED / CANCELLED  
- `attempt_count`, `available_at`, lock fields, `published_at`, `last_error`  
- Event 与 Outbox **同事务**写入（D-019 / G-23）  
- 允许重复发布；消费者幂等；不宣称 exactly-once  
- pending 索引只建一次（G-05）  
- EvidenceLink 有效唯一：PG15+ `NULLS NOT DISTINCT`（G-04）

多态目标归属由领域接口校验（G-06）。Validation: `NOT_RUN`
