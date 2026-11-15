# Physical model: Evidence / Event

**Migration target:** `003_evidence_event.sql`

## Tables

`evidence`, `evidence_source`, `evidence_relation`, `evidence_link`, `learning_event`, `event_relation`, `event_evidence_link`, `transactional_outbox`

## Key rules

- Evidence 内容不可变；修正新建 Evidence + relation  
- EvidenceLink 多态；有效唯一索引策略统一（PG15+ NULLS NOT DISTINCT）  
- LearningEvent append-only；与 Outbox 同事务  
- Outbox：publication_status、attempt_count、available_at、lock、published_at、last_error  
- 不宣称 exactly-once；消费者幂等  
- Outbox pending 索引只建一次（避免 batch-17 重复）
