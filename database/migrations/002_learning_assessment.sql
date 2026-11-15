-- 002_learning_assessment.sql
-- V1: catalog + task/question/response; NO learning_goal (D-026)
-- Requires: 001_platform_identity.sql

BEGIN;

CREATE SCHEMA IF NOT EXISTS learning;
CREATE SCHEMA IF NOT EXISTS assessment;
CREATE SCHEMA IF NOT EXISTS catalog;

CREATE TABLE catalog.knowledge_point (
  id              uuid PRIMARY KEY,
  subject_code    text NOT NULL,
  school_stage    text,
  parent_id       uuid REFERENCES catalog.knowledge_point(id),
  code            text NOT NULL,
  title           text NOT NULL,
  curriculum_ref  text,
  created_at      timestamptz NOT NULL DEFAULT now(),
  UNIQUE (subject_code, code)
);

CREATE TABLE learning.learning_task (
  id                          uuid PRIMARY KEY,
  family_id                   uuid NOT NULL REFERENCES identity.family(id),
  learner_family_member_id    uuid NOT NULL REFERENCES identity.family_member(id),
  school_stage                text NOT NULL,
  subject_code                text NOT NULL,
  grade_code                  text,
  task_type                   text NOT NULL,
  task_status                 text NOT NULL,
  task_source                 text NOT NULL,
  title                       text,
  description                 text,
  planned_start_at            timestamptz,
  due_at                      timestamptz,
  completed_at                timestamptz,
  created_at                  timestamptz NOT NULL DEFAULT now(),
  updated_at                  timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE assessment.question (
  id            uuid PRIMARY KEY,
  subject_code  text NOT NULL,
  created_at    timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE assessment.question_version (
  id                uuid PRIMARY KEY,
  question_id       uuid NOT NULL REFERENCES assessment.question(id),
  version_number    integer NOT NULL,
  stem_content      jsonb NOT NULL,
  standard_answer   jsonb,
  rubric            jsonb,
  created_at        timestamptz NOT NULL DEFAULT now(),
  UNIQUE (question_id, version_number)
);

CREATE TABLE assessment.question_knowledge_link (
  id                    uuid PRIMARY KEY,
  question_id           uuid NOT NULL REFERENCES assessment.question(id),
  question_version_id   uuid NOT NULL REFERENCES assessment.question_version(id),
  knowledge_point_id    uuid NOT NULL REFERENCES catalog.knowledge_point(id),
  created_at            timestamptz NOT NULL DEFAULT now(),
  UNIQUE (question_version_id, knowledge_point_id)
);

CREATE TABLE assessment.task_question (
  id                    uuid PRIMARY KEY,
  learning_task_id      uuid NOT NULL REFERENCES learning.learning_task(id),
  question_id           uuid NOT NULL REFERENCES assessment.question(id),
  question_version_id   uuid NOT NULL REFERENCES assessment.question_version(id),
  sequence_no           integer,
  created_at            timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE assessment.learning_response (
  id                          uuid PRIMARY KEY,
  learning_task_id            uuid NOT NULL REFERENCES learning.learning_task(id),
  task_question_id            uuid NOT NULL REFERENCES assessment.task_question(id),
  question_id                 uuid NOT NULL REFERENCES assessment.question(id),
  respondent_reference_type   text NOT NULL,
  respondent_reference_id     uuid NOT NULL,
  response_mode               text NOT NULL,
  support_level               text NOT NULL,
  response_status             text NOT NULL,
  response_content            jsonb,
  content_storage_ref         text,
  started_at                  timestamptz,
  submitted_at                timestamptz,
  confirmed_at                timestamptz,
  created_at                  timestamptz NOT NULL DEFAULT now(),
  updated_at                  timestamptz NOT NULL DEFAULT now()
);

COMMIT;
