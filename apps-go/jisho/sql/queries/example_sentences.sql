-- name: CreateExampleSentence :one
INSERT INTO example_sentences
    (id, created_at, updated_at, japanese_text, english_meaning, grammar_concept_id)
VALUES(
    gen_random_uuid(),
    NOW(),
    NOW(),
    $1,
    $2,
    $3
)
RETURNING *;

-- name: GetExampleSentenceWithGrammarConcept :one
SELECT
  es.id,
  es.created_at,
  es.updated_at,
  es.japanese_text,
  es.english_meaning,
  es.grammar_concept_id,

  gc.id AS grammar_concept_id,
  -- gc.created_at AS grammar_concept_created_at,
  -- gc.updated_at AS grammar_concept_updated_at,
  gc.jlpt_level AS grammar_concept_jlpt_level,
  gc.concept AS grammar_concept,
  gc.definition AS grammar_definition
FROM example_sentences AS es
JOIN grammar_concepts AS gc
  ON gc.id = es.grammar_concept_id
WHERE es.id = $1;

-- name: GetExampleSentencesByGrammarConceptId :many
SELECT
    id,
    created_at,
    updated_at,
    japanese_text,
    english_meaning,
    grammar_concept_id
FROM example_sentences
WHERE grammar_concept_id = $1
ORDER BY created_at, id;
