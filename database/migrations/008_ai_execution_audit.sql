-- 008_ai_execution_audit.sql
-- Minimal AI execution + audit (D-025)
-- Requires: 001

BEGIN;

CREATE SCHEMA IF NOT EXISTS ai_execution;
CREATE SCHEMA IF NOT EXISTS audit;

CREATE TABLE ai_execution.ai_execution_record (
  id                      uuid PRIMARY KEY,
  family_id               uuid REFERENCES identity.family(id),
  execution_type          text NOT NULL,
  execution_status        text NOT NULL,
  status_revision         integer NOT NULL DEFAULT 0,
  agent_name              text,
  provider                text,
  model                   text,
  prompt_config_version   text,
  execution_request_id    uuid,
  correlation_id          uuid,
  causation_id            uuid,
  started_at              timestamptz,
  completed_at            timestamptz,
  error_message           text,
  metadata                jsonb,
  created_at              timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE ai_execution.ai_execution_input (
  id                    uuid PRIMARY KEY,
  ai_execution_id       uuid NOT NULL REFERENCES ai_execution.ai_execution_record(id),
  content_inline        jsonb,
  content_ref           text,
  created_at            timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE ai_execution.ai_execution_output (
  id                    uuid PRIMARY KEY,
  ai_execution_id       uuid NOT NULL REFERENCES ai_execution.ai_execution_record(id),
  content_inline        jsonb,
  content_ref           text,
  output_status         text NOT NULL DEFAULT 'GENERATED',
  created_at            timestamptz NOT NULL DEFAULT now(),
  updated_at            timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE audit.audit_record (
  id                      uuid PRIMARY KEY,
  family_id               uuid REFERENCES identity.family(id),
  actor_type              text NOT NULL,
  actor_id                uuid,
  action_type             text NOT NULL,
  action_result           text NOT NULL,
  target_type             text,
  target_id               uuid,
  request_ref             text,
  occurred_at             timestamptz NOT NULL DEFAULT now(),
  details                 jsonb,
  created_at              timestamptz NOT NULL DEFAULT now()
);

COMMIT;
