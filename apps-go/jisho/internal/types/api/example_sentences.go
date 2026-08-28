package api

type ExampleSentenceDbEntryDetails struct {
	CreatedAt string `json:"created_at"`
	UpdatedAt string `json:"updated_at"`
}

type ExampleSentenceDbEntry struct {
	Id               string `json:"id"`
	GrammarConceptId string `json:"grammar_concept_id" validate:"required"`
	JapaneseText     string `json:"japanese_text" validate:"required"`
	EnglishMeaning   string `json:"english_meaning" validate:"required"`
}

type ReqCreateExampleSentence struct {
	ExampleSentenceDbEntry
}
type ResCreateExampleSentence struct {
	ExampleSentenceDbEntryDetails
	ExampleSentenceDbEntry
	// GrammarConcept GrammarConceptDbEntry `json:"grammar_concept"`
}

type ResGetExampleSentenceById struct {
	ExampleSentenceDbEntryDetails
	ExampleSentenceDbEntry
	GrammarConcept GrammarConceptDbEntry `json:"grammar_concept"`
}
