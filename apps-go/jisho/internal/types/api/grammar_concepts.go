package api

import "github.com/julillermo/tsukuru/apps-go/jisho/internal/types"

type GrammarConceptDbEntryDetails struct {
	CreatedAt string `json:"created_at"`
	UpdatedAt string `json:"updated_at"`
}

type GrammarConceptDbEntry struct {
	Id         string          `json:"id"`
	JLPTLevel  types.JLPTLevel `json:"jlpt_level" validate:"required"`
	Concept    string          `json:"concept" validate:"required"`
	Definition string          `json:"definition" validate:"required"`
}

// TODO: think about whether ID should also be part of the Update struct
type GrammarConceptDbEntryUpdate struct {
	JLPTLevel  types.JLPTLevel `json:"jlpt_level"`
	Concept    *string         `json:"concept"`
	Definition *string         `json:"definition"`
}

type ReqCreateGrammarConcept struct {
	GrammarConceptDbEntry
}
type ResCreateGrammarConcept struct {
	GrammarConceptDbEntryDetails
	GrammarConceptDbEntry
}

type ReqUpdateGrammarConceptById struct {
	GrammarConceptDbEntryUpdate
}
type ResUpdateGrammarConceptById struct {
	GrammarConceptDbEntryDetails
	GrammarConceptDbEntry
}

type ResGetGrammarConceptById struct {
	GrammarConceptDbEntryDetails
	GrammarConceptDbEntry
	Examples []ExampleSentenceDbEntry `json:"examples"`
}

type GrammarConceptWithExampleSetenceJoin struct {
	GrammarConceptDbEntryDetails
	GrammarConceptDbEntry
	ExampleSentenceID           string `json:"example_sentence_id"`
	ExampleSentenceJapaneseText string `json:"example_japanese_text"`
	ExampleSentenceEnglishText  string `json:"example_english_text"`
}

type ResGetRandomGrammarConcept struct {
	GrammarConceptDbEntryDetails
	GrammarConceptDbEntry
	Examples []ExampleSentenceDbEntry `json:"examples"`
}
