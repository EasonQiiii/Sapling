-- 003_evidence_event.sql
-- Requires: 001, 002

BEGIN;

CREATE SCHEMA IF NOT EXISTS evidence;

CREATE TABLE evidence.evidence (
  id                    uuid PRIMARY KEY,
  family_id             uuid NOT NULL REFERENCES identity.family(id),
  evidence_type         text NOT NULL,
  content_storage_type  text NOT NULL,
  content_inline        jsonb,
  content_uri           text,
  content_hash          text,
  evidence_status       text NOT NULL DEFAULT 'ACTIVE',
  captured_at           timestamptz,
  created_at            timestamptz NOT NULL DEFAULT now(),
  created_by_actor_type text,
  created_by_actor_id   uuid
);

CREATE TABLE evidence.evidence_relation (
  id                uuid PRIMARY KEY,
  from_evidence_id  uuid NOT NULL REFERENCES evidence.evidence(id),
  to_evidence_id    uuid NOT NULL REFERENCES evidence.evidence(id),
  relation_type     text NOT NULL,
  created_at        timestamptz NOT NULL DEFAULT now(),
  CHECK (from_evidence_id <> to_evidence_id)
);

CREATE TABLE assessment.learning_response_evidence_link (
  id                    uuid PRIMARY KEY,
  learning_response_id  uuid NOT NULL REFERENCES assessment.learning_response(id),
  evidence_id           uuid NOT NULL REFERENCES evidence.evidence(id),
  link_role             text,
  created_at            timestamptz NOT NULL DEFAULT now(),
  UNIQUE (learning_response_id, evidence_id)
);

CREATE TABLE evidence.learning_event (
  id                    uuid PRIMARY KEY,
  family_id             uuid NOT NULL REFERENCES identity.family(id),
  event_type            text NOT NULL,
  event_schema_version  text NOT NULL,
  subject_type          text NOT NULL,
  subject_id            uuid NOT NULL,
  actor_type            text,
  actor_id              uuid,
  occurred_at           timestamptz NOT NULL,
  recorded_at           timestamptz NOT NULL DEFAULT now(),
  event_sequence        bigint,
  correlation_id        uuid,
  causation_id          uuid,
  event_payload         jsonb NOT NULL,
  created_at            timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE evidence.transactional_outbox (
  id                  uuid PRIMARY KEY,
  learning_event_id   uuid NOT NULL REFERENCES evidence.learning_event(id),
  publication_status  text NOT NULL DEFAULT 'PENDING',
  attempt_count       integer NOT NULL DEFAULT 0,
  available_at        timestamptz NOT NULL DEFAULT now(),
  locked_by           text,
  locked_at           timestamptz,
  published_at        timestamptz,
  last_error          text,
  created_at          timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX evidence_outbox_pending_idx
  ON evidence.transactional_outbox (available_at)
  WHERE publication_status = 'PENDING';

COMMIT;
