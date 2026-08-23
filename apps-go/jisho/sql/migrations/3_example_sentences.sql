-- +goose Up
CREATE TABLE example_sentences (
  id UUID PRIMARY KEY,
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  japanese_text TEXT,
  english_meaning TEXT,
  grammar_concept_id UUID REFERENCES vocabularies(id)
);

-- +goose Down
DROP TABLE IF EXISTS example_sentences;
