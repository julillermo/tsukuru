-- name: CreateCreatedSentence :one
INSERT INTO created_sentences
    (id, created_at, updated_at, japanese_text, english_meaning)
VALUES(
    gen_random_uuid(),
    NOW(),
    NOW(),
    $1,
    $2
)
RETURNING *;

-- TODO: when creating the getAllCreatedSentences, it has to retreive the vocab and concepts
-- name: GetAllCreatedSentences :many
SELECT * FROM created_sentences;
