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

type ExampleSentenceDbEntryUpdate struct {
	GrammarConceptId *string `json:"grammar_concept_id"`
	JapaneseText     *string `json:"japanese_text"`
	EnglishMeaning   *string `json:"english_meaning"`
}

type ReqCreateExampleSentence struct {
	ExampleSentenceDbEntry
}
type ResCreateExampleSentence struct {
	ExampleSentenceDbEntryDetails
	ExampleSentenceDbEntry
	// GrammarConcept GrammarConceptDbEntry `json:"grammar_concept"`
}

type ReqUpdateExampleSentenceById struct {
	ExampleSentenceDbEntryUpdate
}
type ResUpdateExampleSentenceById struct {
	ExampleSentenceDbEntryDetails
	ExampleSentenceDbEntry
}

type ResGetExampleSentenceById struct {
	ExampleSentenceDbEntryDetails
	ExampleSentenceDbEntry
	GrammarConcept GrammarConceptDbEntry `json:"grammar_concept"`
}
