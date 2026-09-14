-- name: CreateCreatedSentencesVocabularies :one
INSERT INTO created_sentences_vocabularies(
    id,
    created_at,
    updated_at,
    created_sentence_id,
    vocabulary_id
)
VALUES(
    gen_random_uuid(),
    NOW(),
    NOW(),
    $1,
    $2
)
RETURNING *;
