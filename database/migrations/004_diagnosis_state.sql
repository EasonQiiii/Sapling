-- 004_diagnosis_state.sql
-- Diagnosis / Finding / KI / KnowledgeState only (D-025)
-- Requires: 001–003

BEGIN;

CREATE SCHEMA IF NOT EXISTS diagnosis;
CREATE SCHEMA IF NOT EXISTS learning_state;

CREATE TABLE diagnosis.diagnosis (
  id                  uuid PRIMARY KEY,
  family_id           uuid NOT NULL REFERENCES identity.family(id),
  diagnosis_version   text NOT NULL,
  diagnosed_at        timestamptz NOT NULL,
  input_context_ref   jsonb NOT NULL,
  basis_summary       text,
  diagnosis_status    text NOT NULL,
  created_at          timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE diagnosis.diagnosis_subject (
  id              uuid PRIMARY KEY,
  diagnosis_id    uuid NOT NULL REFERENCES diagnosis.diagnosis(id),
  subject_type    text NOT NULL,
  subject_id      uuid NOT NULL,
  created_at      timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE diagnosis.diagnosis_evidence_link (
  id              uuid PRIMARY KEY,
  diagnosis_id    uuid NOT NULL REFERENCES diagnosis.diagnosis(id),
  evidence_id     uuid NOT NULL REFERENCES evidence.evidence(id),
  created_at      timestamptz NOT NULL DEFAULT now(),
  UNIQUE (diagnosis_id, evidence_id)
);

CREATE TABLE diagnosis.finding (
  id                    uuid PRIMARY KEY,
  diagnosis_id          uuid NOT NULL REFERENCES diagnosis.diagnosis(id),
  knowledge_point_id    uuid REFERENCES catalog.knowledge_point(id),
  error_class           text,
  is_primary_blame      boolean DEFAULT true,
  finding_type          text NOT NULL,
  statement             text NOT NULL,
  confidence            text NOT NULL,
  causal_notes          jsonb,
  created_at            timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE diagnosis.finding_validity (
  id                uuid PRIMARY KEY,
  finding_id        uuid NOT NULL REFERENCES diagnosis.finding(id),
  validity_status   text NOT NULL,
  effective_at      timestamptz NOT NULL,
  reason            text,
  created_at        timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE diagnosis.finding_evidence_link (
  id            uuid PRIMARY KEY,
  finding_id    uuid NOT NULL REFERENCES diagnosis.finding(id),
  evidence_id   uuid NOT NULL REFERENCES evidence.evidence(id),
  created_at    timestamptz NOT NULL DEFAULT now(),
  UNIQUE (finding_id, evidence_id)
);

CREATE TABLE diagnosis.knowledge_issue (
  id                            uuid PRIMARY KEY,
  family_id                     uuid NOT NULL REFERENCES identity.family(id),
  learner_family_member_id      uuid NOT NULL REFERENCES identity.family_member(id),
  subject_code                  text NOT NULL,
  primary_knowledge_point_id    uuid REFERENCES catalog.knowledge_point(id),
  issue_kind                    text NOT NULL,
  title                         text NOT NULL,
  issue_status                  text NOT NULL,
  current_revision_id           uuid,
  merge_algorithm_version       text,
  opened_at                     timestamptz NOT NULL,
  resolved_at                   timestamptz,
  created_at                    timestamptz NOT NULL DEFAULT now(),
  updated_at                    timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE diagnosis.knowledge_issue_revision (
  id                      uuid PRIMARY KEY,
  knowledge_issue_id      uuid NOT NULL REFERENCES diagnosis.knowledge_issue(id),
  revision_number         integer NOT NULL,
  summary                 text NOT NULL,
  description             text,
  status_at_revision      text,
  created_at              timestamptz NOT NULL DEFAULT now(),
  UNIQUE (knowledge_issue_id, revision_number)
);

ALTER TABLE diagnosis.knowledge_issue
  ADD CONSTRAINT knowledge_issue_current_revision_fk
  FOREIGN KEY (current_revision_id) REFERENCES diagnosis.knowledge_issue_revision(id);

CREATE TABLE diagnosis.finding_issue_link (
  id                        uuid PRIMARY KEY,
  finding_id                uuid NOT NULL REFERENCES diagnosis.finding(id),
  knowledge_issue_id        uuid NOT NULL REFERENCES diagnosis.knowledge_issue(id),
  link_role                 text,
  merge_algorithm_version   text,
  created_at                timestamptz NOT NULL DEFAULT now(),
  UNIQUE (finding_id, knowledge_issue_id)
);

CREATE TABLE learning_state.knowledge_state (
  id                          uuid PRIMARY KEY,
  learner_family_member_id    uuid NOT NULL REFERENCES identity.family_member(id),
  knowledge_point_id          uuid NOT NULL REFERENCES catalog.knowledge_point(id),
  current_revision_id         uuid,
  updated_at                  timestamptz NOT NULL DEFAULT now(),
  UNIQUE (learner_family_member_id, knowledge_point_id)
);

CREATE TABLE learning_state.state_revision (
  id                      uuid PRIMARY KEY,
  state_type              text NOT NULL DEFAULT 'KNOWLEDGE',
  state_subject_id        uuid NOT NULL,
  revision_number         integer NOT NULL,
  state_content           jsonb NOT NULL,
  created_at              timestamptz NOT NULL DEFAULT now(),
  created_by_event_id     uuid REFERENCES evidence.learning_event(id),
  UNIQUE (state_type, state_subject_id, revision_number)
);

ALTER TABLE learning_state.knowledge_state
  ADD CONSTRAINT knowledge_state_current_revision_fk
  FOREIGN KEY (current_revision_id) REFERENCES learning_state.state_revision(id);

CREATE TABLE learning_state.state_revision_reference (
  id                      uuid PRIMARY KEY,
  state_revision_id       uuid NOT NULL REFERENCES learning_state.state_revision(id),
  reference_type          text NOT NULL,
  reference_id            uuid NOT NULL,
  reference_revision_id   uuid,
  created_at              timestamptz NOT NULL DEFAULT now()
);

COMMIT;
