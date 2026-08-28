package utils

import (
	db "github.com/julillermo/tsukuru/apps-go/jisho/internal/database"
	apiType "github.com/julillermo/tsukuru/apps-go/jisho/internal/types/api"
)

func GetOptInt32Input(value *int) int32 {
	if value == nil {
		return 0
	} else {
		return int32(*value)
	}
}
func ValidateOptInt32Input(value *int) bool {
	return value != nil && *value > 0
}

func GetOptStringInput(value *string) string {
	if value == nil {
		return ""
	} else {
		return *value
	}
}
func ValidateOptStringInput(value *string) bool {
	return value != nil && len(*value) > 0
}

func GetOptSliceInput[T any](value *[]T) []T {
	if value != nil {
		return *value
	} else {
		return nil
	}
}

func ConvertExampleSetenceDBToApi(
	exampleSentencesDb []db.ExampleSentence,
) (exampleSentencesApi []apiType.ExampleSentenceDbEntry) {
	for idx := range exampleSentencesDb {
		exampleSentencesApi = append(exampleSentencesApi,
			apiType.ExampleSentenceDbEntry{
				Id:               exampleSentencesDb[idx].ID.String(),
				GrammarConceptId: exampleSentencesDb[idx].GrammarConceptID.UUID.String(),
				JapaneseText:     exampleSentencesDb[idx].JapaneseText.String,
				EnglishMeaning:   exampleSentencesDb[idx].EnglishMeaning.String,
			},
		)
	}
	return exampleSentencesApi
}
