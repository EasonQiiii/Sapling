-- 001_platform_identity.sql
-- V1 lean slice (D-025). Status: executable draft — run against empty Postgres 16+.
-- Validation: NOT_RUN until CI/local empty-db pass recorded in docs/06-validation/

BEGIN;

CREATE SCHEMA IF NOT EXISTS platform;
CREATE SCHEMA IF NOT EXISTS identity;

CREATE TABLE identity.family (
  id            uuid PRIMARY KEY,
  display_name  text,
  created_at    timestamptz NOT NULL DEFAULT now(),
  updated_at    timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE identity.person (
  id            uuid PRIMARY KEY,
  display_name  text,
  created_at    timestamptz NOT NULL DEFAULT now(),
  updated_at    timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE identity.account (
  id            uuid PRIMARY KEY,
  login_name    text NOT NULL UNIQUE,
  status        text NOT NULL DEFAULT 'ACTIVE',
  created_at    timestamptz NOT NULL DEFAULT now(),
  updated_at    timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE identity.account_person_link (
  id            uuid PRIMARY KEY,
  account_id    uuid NOT NULL REFERENCES identity.account(id),
  person_id     uuid NOT NULL REFERENCES identity.person(id),
  created_at    timestamptz NOT NULL DEFAULT now(),
  UNIQUE (account_id, person_id)
);

CREATE TABLE identity.family_member (
  id            uuid NOT NULL,
  family_id     uuid NOT NULL REFERENCES identity.family(id),
  person_id     uuid NOT NULL REFERENCES identity.person(id),
  member_role   text NOT NULL,
  created_at    timestamptz NOT NULL DEFAULT now(),
  updated_at    timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (id),
  UNIQUE (id, family_id, member_role),
  UNIQUE (family_id, person_id, member_role)
);

COMMIT;
