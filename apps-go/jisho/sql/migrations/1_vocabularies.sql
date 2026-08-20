-- +goose Up
CREATE TABLE vocabularies (
  id UUID PRIMARY KEY,
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  wiki_index INTEGER,
  kana TEXT,
  kanji TEXT,
  classification TEXT[],
  definition TEXT
);

-- +goose Down
DROP TABLE IF EXISTS vocabularies;
