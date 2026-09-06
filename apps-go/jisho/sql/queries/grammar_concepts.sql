-- name: CreateGrammarConcept :one
INSERT INTO grammar_concepts
    (id, created_at, updated_at, jlpt_level, concept, definition)
VALUES(
    gen_random_uuid(),
    NOW(),
    NOW(),
    $1,
    $2,
    $3
)
RETURNING *;


-- name: GetGrammarConceptById :one
SELECT *
FROM grammar_concepts
WHERE id=$1;


-- name: UpdateGrammarConceptById :one
UPDATE grammar_concepts
SET
    updated_at = NOW(),
    jlpt_level = COALESCE(sqlc.narg('jlpt_level'), jlpt_level),
    concept = COALESCE(sqlc.narg('concept'), concept),
    definition = COALESCE(sqlc.narg('definition'), definition)
WHERE
    id=sqlc.arg('id')
RETURNING *;

-- name: GetRandomGrammarConcepts :many
WITH selected_concepts AS (
    SELECT
        gc.id,
        gc.created_at,
        gc.updated_at,
        gc.jlpt_level,
        gc.concept,
        gc.definition
    FROM grammar_concepts AS gc
    ORDER BY RANDOM()
    LIMIT $1
)
SELECT
    sc.id,
    sc.created_at,
    sc.updated_at,
    sc.jlpt_level,
    sc.concept,
    sc.definition,
    es.id AS example_sentence_id,
    es.japanese_text AS example_sentence_japanese_text,
    es.english_meaning AS example_sentence_english_text
FROM selected_concepts AS sc
LEFT JOIN example_sentences AS es
    ON sc.id = es.grammar_concept_id;
