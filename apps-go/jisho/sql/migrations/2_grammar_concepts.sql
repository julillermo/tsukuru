-- +goose Up
CREATE TABLE grammar_concepts (
  id UUID PRIMARY KEY,
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  concept TEXT,
  definition TEXT
);

-- +goose Down
DROP TABLE IF EXISTS grammar_concepts;
