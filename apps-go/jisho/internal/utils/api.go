package utils

import (
	"log"
	"sort"
	"time"

	db "github.com/julillermo/tsukuru/apps-go/jisho/internal/database"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/types"
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

func ConvertExampleSetenceSliceDBToAPI(
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

func ConvertVocabularySliceDBtoAPI(
	vocabulariesDb []db.Vocabulary,
) (vocabulariesAPI []apiType.VocabularyDbEntry) {
	for idx := range vocabulariesDb {
		vocabulariesAPI = append(vocabulariesAPI,
			apiType.VocabularyDbEntry{
				Id:             vocabulariesDb[idx].ID.String(),
				JLPTLevel:      types.JLPTLevel(vocabulariesDb[idx].JlptLevel.JlptLevelEnum),
				WikiIndex:      int(vocabulariesDb[idx].WikiIndex.Int32),
				Kana:           vocabulariesDb[idx].Kana.String,
				Kanji:          vocabulariesDb[idx].Kanji.String,
				Classification: vocabulariesDb[idx].Classification,
				Definition:     vocabulariesDb[idx].Definition.String,
			})
	}
	return vocabulariesAPI
}

func ConvertGrammarConceptsSliceDBtoAPI(
	grammarConceptsDb []db.GrammarConcept,
) (grammarConceptsAPI []apiType.GrammarConceptDbEntry) {
	for idx := range grammarConceptsDb {
		grammarConceptsAPI = append(grammarConceptsAPI,
			apiType.GrammarConceptDbEntry{
				Id:         grammarConceptsDb[idx].ID.String(),
				JLPTLevel:  types.JLPTLevel(grammarConceptsDb[idx].JlptLevel.JlptLevelEnum),
				Concept:    grammarConceptsDb[idx].Concept.String,
				Definition: grammarConceptsDb[idx].Definition.String,
			})
	}
	return grammarConceptsAPI
}

func ConvertGrammarConceptsRowDBtoAPI(
	grammarConceptsDb []db.GetRandomGrammarConceptsRow,
) (grammarConceptsAPI []apiType.ResGetRandomGrammarConcept) {
	for _, gConcept := range grammarConceptsDb {
		conceptAlreadyIncluded := false
		for gcApiIdx, includedConcepts := range grammarConceptsAPI {
			if gConcept.ID.String() == includedConcepts.Id {
				conceptAlreadyIncluded = true
				grammarConceptsAPI[gcApiIdx].Examples = append(includedConcepts.Examples,
					apiType.ExampleSentenceDbEntry{
						Id:             gConcept.ExampleSentenceID.UUID.String(),
						JapaneseText:   gConcept.ExampleSentenceJapaneseText.String,
						EnglishMeaning: gConcept.ExampleSentenceEnglishText.String,
					})
			}
		}

		if !conceptAlreadyIncluded {
			grammarConceptsAPI = append(grammarConceptsAPI, apiType.ResGetRandomGrammarConcept{
				GrammarConceptDbEntry: apiType.GrammarConceptDbEntry{
					Id:         gConcept.ID.String(),
					JLPTLevel:  types.JLPTLevel(gConcept.JlptLevel.JlptLevelEnum),
					Concept:    gConcept.Concept.String,
					Definition: gConcept.Definition.String,
				},
				Examples: []apiType.ExampleSentenceDbEntry{{
					Id:             gConcept.ExampleSentenceID.UUID.String(),
					JapaneseText:   gConcept.ExampleSentenceJapaneseText.String,
					EnglishMeaning: gConcept.ExampleSentenceEnglishText.String,
				}},
			})
		}
	}

	return grammarConceptsAPI
}

func ConvertCreatedSentencesDBToAPI(
	createdSentencesDb []db.CreatedSentence,
	sorting types.Sorting, // "Ascending" | "Descending"
) (createdSentencesAPI []apiType.ResCreateSentence) {
	if !IsSorting(sorting) {
		log.Print("value for sorting is invalid and not of type Sorting")
		return createdSentencesAPI
	}

	for idx := range createdSentencesDb {
		createdSentencesAPI = append(createdSentencesAPI,
			apiType.ResCreateSentence{
				CreatedSentencDbEntryDetails: apiType.CreatedSentencDbEntryDetails{
					CreatedAt: createdSentencesDb[idx].CreatedAt.Time.Format(time.RFC3339),
					UpdatedAt: createdSentencesDb[idx].UpdatedAt.Time.Format(time.RFC3339),
				},
				CreatedSentenceDbEntry: apiType.CreatedSentenceDbEntry{
					Id:             createdSentencesDb[idx].ID.String(),
					JapaneseText:   createdSentencesDb[idx].JapaneseText.String,
					EnglishMeaning: createdSentencesDb[idx].EnglishMeaning.String,
				},
			})
	}

	sort.Slice(createdSentencesAPI, func(aIdx, bIdx int) bool {
		aUpdatedAt, err := time.Parse(time.RFC3339, createdSentencesAPI[aIdx].UpdatedAt)
		if err != nil {
			log.Print(err)
			log.Print("unable to parse created sentence updated at time")
			return false
		}
		bUpdatedAt, err := time.Parse(time.RFC3339, createdSentencesAPI[bIdx].UpdatedAt)
		if err != nil {
			log.Print(err)
			log.Print("unable to parse created sentence updated at time")
			return false
		}

		switch sorting {
		case "Ascending":
			return aUpdatedAt.Before(bUpdatedAt)
		case "Descending":
			return aUpdatedAt.After(bUpdatedAt)
		default:
			return aUpdatedAt.After(bUpdatedAt)
		}
	})

	return createdSentencesAPI
}
