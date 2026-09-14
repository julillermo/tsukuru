-- +goose Up
CREATE TABLE created_sentences (
  id UUID PRIMARY KEY,
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  japanese_text TEXT,
  english_meaning TEXT
);
CREATE TABLE created_sentences_vocabularies (
    id UUID PRIMARY KEY,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    created_sentence_id UUID REFERENCES created_sentences(id),
    vocabulary_id UUID REFERENCES vocabularies(id)
);
CREATE TABLE created_sentences_grammar_concepts (
    id UUID PRIMARY KEY,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    created_sentence_id UUID REFERENCES created_sentences(id),
    grammar_concept_id UUID REFERENCES grammar_concepts(id)
);

-- +goose Down
DROP TABLE IF EXISTS created_sentences_grammar_concepts;
DROP TABLE IF EXISTS created_sentences_vocabularies;
DROP TABLE IF EXISTS created_sentences;
