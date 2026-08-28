-- name: CreateVocabulary :one
INSERT INTO vocabularies
    (id, created_at, updated_at, jlpt_level, wiki_index, kana, kanji, classification, definition)
VALUES(
    gen_random_uuid(),
    NOW(),
    NOW(),
    $1,
    $2,
    $3,
    $4,
    $5,
    $6
)
RETURNING *;


-- name: GetVocabularyById :one
SELECT * FROM vocabularies WHERE id=$1;


-- TODO: This is missing JLPT level
-- name: UpdateVocabularyById :one
UPDATE vocabularies
SET
    updated_at = NOW(),
    wiki_index = COALESCE(sqlc.narg('wiki_index'), wiki_index),
    kana = COALESCE(sqlc.narg('kana'), kana),
    kanji = COALESCE(sqlc.narg('kanji'), kanji),
    classification = COALESCE(sqlc.narg('classification'), classification),
    definition = COALESCE(sqlc.narg('definition'), definition)
WHERE
    id=sqlc.arg('id')
RETURNING *;
