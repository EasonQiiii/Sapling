-- 009_cross_schema_constraints.sql
-- V1 subset cross-checks / helpful indexes (D-025)
-- Requires: 001–004, 007, 008
-- 005/006 remain DEFERRED placeholders

BEGIN;

CREATE INDEX IF NOT EXISTS learning_task_family_subject_idx
  ON learning.learning_task (family_id, subject_code);

CREATE INDEX IF NOT EXISTS finding_kp_idx
  ON diagnosis.finding (knowledge_point_id);

CREATE INDEX IF NOT EXISTS knowledge_issue_learner_subject_kp_idx
  ON diagnosis.knowledge_issue (learner_family_member_id, subject_code, primary_knowledge_point_id);

CREATE INDEX IF NOT EXISTS learning_event_family_type_idx
  ON evidence.learning_event (family_id, event_type, occurred_at);

-- Mark deferred migrations explicitly as no-op documentation tables (optional skip)
-- 005 / 006 intentionally empty beyond placeholders

COMMIT;
