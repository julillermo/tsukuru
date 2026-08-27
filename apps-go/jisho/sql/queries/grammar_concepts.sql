-- name: CreateGrammarConcept :one
INSERT INTO grammar_concepts
    (id, created_at, updated_at, concept, definition)
VALUES(
    gen_random_uuid(),
    NOW(),
    NOW(),
    $1,
    $2
)
RETURNING *;

-- name: GetGrammarConceptById :one
SELECT * FROM grammar_concepts WHERE id=$1;

-- name: UpdateGrammarConceptById :one
UPDATE grammar_concepts
SET
    updated_at = NOW(),
    concept = COALESCE(sqlc.narg('concept'), concept),
    definition = COALESCE(sqlc.narg('definition'), definition)
WHERE
    id=sqlc.arg('id')
RETURNING *;
