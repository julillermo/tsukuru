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
SELECT * FROM grammar_concepts WHERE id=$1;

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
