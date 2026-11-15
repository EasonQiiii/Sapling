-- 007_decision_workflow.sql
-- Thin decision + workflow tables + thin intervention (no Stage tree) D-025/D-027
-- Requires: 001–004

BEGIN;

CREATE SCHEMA IF NOT EXISTS decision;
CREATE SCHEMA IF NOT EXISTS workflow;

CREATE TABLE decision.decision_record (
  id                      uuid PRIMARY KEY,
  family_id               uuid NOT NULL REFERENCES identity.family(id),
  decision_status         text NOT NULL,
  selected_candidate_id   uuid,
  authority               text NOT NULL DEFAULT 'AUTO',
  created_at              timestamptz NOT NULL DEFAULT now(),
  updated_at              timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE decision.decision_candidate (
  id                    uuid PRIMARY KEY,
  decision_record_id    uuid NOT NULL REFERENCES decision.decision_record(id),
  candidate_payload     jsonb NOT NULL,
  created_at            timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE decision.decision_candidate_selection (
  id                    uuid PRIMARY KEY,
  decision_record_id    uuid NOT NULL REFERENCES decision.decision_record(id),
  decision_candidate_id uuid NOT NULL REFERENCES decision.decision_candidate(id),
  selected_at           timestamptz NOT NULL,
  selection_reason      text,
  created_at            timestamptz NOT NULL DEFAULT now()
);

ALTER TABLE decision.decision_record
  ADD CONSTRAINT decision_selected_candidate_fk
  FOREIGN KEY (selected_candidate_id) REFERENCES decision.decision_candidate(id);

CREATE TABLE decision.decision_approval (
  id                    uuid PRIMARY KEY,
  decision_record_id    uuid NOT NULL REFERENCES decision.decision_record(id),
  selection_id          uuid NOT NULL REFERENCES decision.decision_candidate_selection(id),
  approver_reference_type text NOT NULL,
  approver_reference_id uuid NOT NULL,
  approved_at           timestamptz NOT NULL,
  created_at            timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE decision.decision_status_history (
  id                    uuid PRIMARY KEY,
  decision_record_id    uuid NOT NULL REFERENCES decision.decision_record(id),
  from_status           text,
  to_status             text NOT NULL,
  status_revision       integer NOT NULL,
  changed_at            timestamptz NOT NULL,
  created_at            timestamptz NOT NULL DEFAULT now(),
  UNIQUE (decision_record_id, status_revision)
);

CREATE TABLE workflow.workflow_definition (
  id            uuid PRIMARY KEY,
  code          text NOT NULL UNIQUE,
  title         text NOT NULL,
  created_at    timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE workflow.workflow_definition_version (
  id                        uuid PRIMARY KEY,
  workflow_definition_id    uuid NOT NULL REFERENCES workflow.workflow_definition(id),
  version_number            integer NOT NULL,
  created_at                timestamptz NOT NULL DEFAULT now(),
  UNIQUE (workflow_definition_id, version_number)
);

CREATE TABLE workflow.workflow_step_definition (
  id                              uuid PRIMARY KEY,
  workflow_definition_version_id  uuid NOT NULL REFERENCES workflow.workflow_definition_version(id),
  step_key                        text NOT NULL,
  step_type                       text NOT NULL,
  created_at                      timestamptz NOT NULL DEFAULT now(),
  UNIQUE (workflow_definition_version_id, step_key)
);

CREATE TABLE workflow.workflow_step_transition (
  id                              uuid PRIMARY KEY,
  workflow_definition_version_id  uuid NOT NULL REFERENCES workflow.workflow_definition_version(id),
  from_step_id                    uuid NOT NULL REFERENCES workflow.workflow_step_definition(id),
  to_step_id                      uuid NOT NULL REFERENCES workflow.workflow_step_definition(id),
  created_at                      timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE workflow.workflow_run (
  id                              uuid PRIMARY KEY,
  learning_task_id                uuid NOT NULL REFERENCES learning.learning_task(id),
  workflow_definition_version_id  uuid NOT NULL REFERENCES workflow.workflow_definition_version(id),
  run_status                      text NOT NULL,
  current_step_run_id             uuid,
  execution_request_id            uuid NOT NULL UNIQUE,
  started_at                      timestamptz,
  completed_at                    timestamptz,
  created_at                      timestamptz NOT NULL DEFAULT now(),
  updated_at                      timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE workflow.workflow_step_run (
  id                        uuid PRIMARY KEY,
  workflow_run_id           uuid NOT NULL REFERENCES workflow.workflow_run(id),
  workflow_step_definition_id uuid NOT NULL REFERENCES workflow.workflow_step_definition(id),
  attempt_number            integer NOT NULL,
  step_status               text NOT NULL,
  created_at                timestamptz NOT NULL DEFAULT now(),
  UNIQUE (workflow_run_id, workflow_step_definition_id, attempt_number)
);

CREATE TABLE workflow.workflow_run_status_history (
  id                uuid PRIMARY KEY,
  workflow_run_id   uuid NOT NULL REFERENCES workflow.workflow_run(id),
  from_status       text,
  to_status         text NOT NULL,
  status_revision   integer NOT NULL,
  changed_at        timestamptz NOT NULL,
  created_at        timestamptz NOT NULL DEFAULT now(),
  UNIQUE (workflow_run_id, status_revision)
);

CREATE TABLE workflow.workflow_step_run_status_history (
  id                    uuid PRIMARY KEY,
  workflow_step_run_id  uuid NOT NULL REFERENCES workflow.workflow_step_run(id),
  from_status           text,
  to_status             text NOT NULL,
  status_revision       integer NOT NULL,
  changed_at            timestamptz NOT NULL,
  created_at            timestamptz NOT NULL DEFAULT now(),
  UNIQUE (workflow_step_run_id, status_revision)
);

-- Thin intervention (no stage tree)
CREATE TABLE learning.learning_intervention (
  id                          uuid PRIMARY KEY,
  family_id                   uuid NOT NULL REFERENCES identity.family(id),
  learner_family_member_id    uuid NOT NULL REFERENCES identity.family_member(id),
  subject_code                text NOT NULL,
  knowledge_issue_id          uuid REFERENCES diagnosis.knowledge_issue(id),
  intervention_status         text NOT NULL,
  created_at                  timestamptz NOT NULL DEFAULT now(),
  updated_at                  timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE learning.intervention_goal (
  id                        uuid PRIMARY KEY,
  learning_intervention_id  uuid NOT NULL REFERENCES learning.learning_intervention(id),
  current_revision_id       uuid,
  created_at                timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE learning.intervention_goal_revision (
  id                    uuid PRIMARY KEY,
  intervention_goal_id  uuid NOT NULL REFERENCES learning.intervention_goal(id),
  revision_number       integer NOT NULL,
  goal_text             text NOT NULL,
  created_at            timestamptz NOT NULL DEFAULT now(),
  UNIQUE (intervention_goal_id, revision_number)
);

ALTER TABLE learning.intervention_goal
  ADD CONSTRAINT intervention_goal_current_revision_fk
  FOREIGN KEY (current_revision_id) REFERENCES learning.intervention_goal_revision(id);

CREATE TABLE learning.intervention_task (
  id                        uuid PRIMARY KEY,
  learning_intervention_id  uuid NOT NULL REFERENCES learning.learning_intervention(id),
  learning_task_id          uuid NOT NULL REFERENCES learning.learning_task(id),
  created_at                timestamptz NOT NULL DEFAULT now(),
  UNIQUE (learning_intervention_id, learning_task_id)
);

COMMIT;
