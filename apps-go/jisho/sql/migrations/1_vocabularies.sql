-- +goose Up
CREATE TYPE jlpt_level_enum AS ENUM ('n5', 'n4', 'n3', 'n2', 'n1');
-- TODO: Revisit whether I would want TZ instead of just timestamp
CREATE TABLE vocabularies (
  id UUID PRIMARY KEY,
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  jlpt_level jlpt_level_enum,
  wiki_index INTEGER,
  kana TEXT,
  kanji TEXT,
  classification TEXT[],
  definition TEXT
);

-- +goose Down
DROP TABLE IF EXISTS vocabularies;
DROP TYPE IF EXISTS jlpt_level_enum;
