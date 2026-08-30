package api

type ResTsukuruGetRandomConstructs struct {
	Vocabularies    []VocabularyDbEntry     `json:"vocabularies"`
	GrammarConcepts []GrammarConceptDbEntry `json:"grammar_concepts"`
}
