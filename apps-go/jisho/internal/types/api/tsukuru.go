package api

type ResTsukuruGetRandomConstructs struct {
	Vocabularies    []VocabularyDbEntry          `json:"vocabularies"`
	GrammarConcepts []ResGetRandomGrammarConcept `json:"grammar_concepts"`
}
