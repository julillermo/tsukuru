package api

type CreatedSentencDbEntryDetails struct {
	CreatedAt string `json:"created_at"`
	UpdatedAt string `json:"updated_at"`
}

type CreatedSentenceDbEntry struct {
	Id             string `json:"id"`
	JapaneseText   string `json:"japanese_text" validate:"required"`
	EnglishMeaning string `json:"english_meaning" validate:"required"`
}

type ReqCreateSentence struct {
	ExampleSentenceDbEntry
	VocabularyIds     []string `json:"vocabulary_ids"`
	GrammarConceptIds []string `json:"grammar_concept_ids"`
}
type ResCreateSentence struct {
	CreatedSentencDbEntryDetails
	CreatedSentenceDbEntry
}

type ResGetAllCreatedSentences struct {
	CreatedSentences []ResCreateSentence `json:"sentences"`
}
