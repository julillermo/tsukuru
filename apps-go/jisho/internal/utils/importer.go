package utils

import (
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/types"
	apiType "github.com/julillermo/tsukuru/apps-go/jisho/internal/types/api"
	importerType "github.com/julillermo/tsukuru/apps-go/jisho/internal/types/importer"
)

func ConvertGrammarConceptJSONToDB(
	grammarConcepts []importerType.GrammarConceptJSON,
	level types.JLPTLevel,
) (
	grammarConceptsDb []importerType.GrammarConceptExampleSentenceDb,
) {
	for idx := range grammarConcepts {
		grammarConceptsDb = append(grammarConceptsDb,
			importerType.GrammarConceptExampleSentenceDb{
				JLPTLevel: level,
				GrammarConceptJSON: importerType.GrammarConceptJSON{
					Concept:    grammarConcepts[idx].Concept,
					Definition: grammarConcepts[idx].Definition,
				},
				Examples: grammarConcepts[idx].Examples,
			})
	}
	return grammarConceptsDb
}

func ConvertVocabularyJSONtoDB(
	vocabularies []importerType.VocabularyJSON,
	level types.JLPTLevel,
) (
	vocabulariesDb []apiType.VocabularyDbEntry,
) {
	for idx := range vocabularies {
		vocabulariesDb = append(vocabulariesDb, apiType.VocabularyDbEntry{
			JLPTLevel:      level,
			WikiIndex:      vocabularies[idx].WikiIndex,
			Kana:           vocabularies[idx].Kana,
			Kanji:          vocabularies[idx].Kanji,
			Classification: vocabularies[idx].Classification,
			Definition:     vocabularies[idx].Definition,
		})
	}
	return vocabulariesDb
}
