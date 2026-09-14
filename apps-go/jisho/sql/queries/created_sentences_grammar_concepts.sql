-- name: CreateCreatedSentencesGrammarConcepts :one
INSERT INTO created_sentences_grammar_concepts(
    id,
    created_at,
    updated_at,
    created_sentence_id,
    grammar_concept_id
)
VALUES(
    gen_random_uuid(),
    NOW(),
    NOW(),
    $1,
    $2
)
RETURNING *;
