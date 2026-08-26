package api

import (
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/types"
)

type CommonVocabularyDbEntryDetails struct {
	Id        string `json:"id"`
	CreatedAt string `json:"created_at"`
	UpdatedAt string `json:"updated_at"`
}

type VocabularyDbEntry struct {
	JLPTLevel      types.JLPTLevel `json:"jlpt_level" validate:"required"`
	WikiIndex      int             `json:"wiki_index" validate:"required"`
	Kana           string          `json:"kana_writing" validate:"required"`
	Kanji          string          `json:"kanji" validate:"required"`
	Classification []string        `json:"classification" validate:"required"`
	Definition     string          `json:"definition" validate:"required"`
}

type VocabularyDbEntryUpdate struct {
	JLPTLevel      *string   `json:"jlpt_level"`
	WikiIndex      *int      `json:"wiki_index"`
	Kana           *string   `json:"kana_writing"`
	Kanji          *string   `json:"kanji"`
	Classification *[]string `json:"classification"`
	Definition     *string   `json:"definition"`
}

type ReqCreateVocabulary struct {
	VocabularyDbEntry
}
type ResCreateVocabulary struct {
	CommonVocabularyDbEntryDetails
	VocabularyDbEntry
}

type ReqUpdateVocabularyById struct {
	VocabularyDbEntryUpdate
}
type ResUpdateVocabularyById struct {
	CommonVocabularyDbEntryDetails
	VocabularyDbEntry
}

type ResGetVocabularyById struct {
	CommonVocabularyDbEntryDetails
	VocabularyDbEntry
}
