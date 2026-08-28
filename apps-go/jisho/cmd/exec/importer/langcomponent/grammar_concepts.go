package langcomponent

import (
	"context"
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"path/filepath"

	"github.com/google/uuid"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/database"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/types"
	importerType "github.com/julillermo/tsukuru/apps-go/jisho/internal/types/importer"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/utils"
)

func ReadAndCombineGrammarConcepts(
	fileDir string,
	levels ...types.JLPTLevel,
) (
	grammarConceptDbEntries []importerType.GrammarConceptExampleSentenceDb,
) {
	for _, level := range levels {
		if !utils.IsJLPTLevel(level) {
			continue
		}

		grammarConceptsPath := filepath.Join(fileDir,
			fmt.Sprintf("grammar_%s.json", level),
		)

		// Read as []byte
		data, err := os.ReadFile(grammarConceptsPath)
		if err != nil {
			log.Printf("Error reading file %s", grammarConceptsPath)
			log.Fatal(err)
		}

		// Parse as JSON-struct
		var grammarConcepts []importerType.GrammarConceptJSON
		if err := json.Unmarshal(data, &grammarConcepts); err != nil {
			log.Printf("Error parsing file %s", grammarConceptsPath)
			log.Fatal(err)
		}

		grammarConceptsDb := utils.ConvertGrammarConceptJSONToDB(grammarConcepts, level)
		grammarConceptDbEntries = append(grammarConceptDbEntries, grammarConceptsDb...)
	}

	return grammarConceptDbEntries
}

func CommitGrammarConceptsToDB(
	jlptGrammarConcepts []importerType.GrammarConceptExampleSentenceDb,
	dbConn *sql.DB,
	ctx context.Context,
	api *types.APIConfig,
) (conceptInsertCount, sentenceInsertCount int32) {
	// Use SQL Transactions
	tx, err := dbConn.BeginTx(ctx, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer tx.Rollback()

	conceptInsertCount = 0
	for _, concept := range jlptGrammarConcepts {
		conceptRes, err := api.DBQueries.CreateGrammarConcept(ctx, database.CreateGrammarConceptParams{
			JlptLevel: database.NullJlptLevelEnum{
				JlptLevelEnum: database.JlptLevelEnum(concept.JLPTLevel),
				Valid:         utils.IsJLPTLevel(concept.JLPTLevel),
			},
			Concept: sql.NullString{
				String: concept.Concept,
				Valid:  len(concept.Concept) > 0,
			},
			Definition: sql.NullString{
				String: concept.Definition,
				Valid:  len(concept.Definition) > 0,
			},
		})
		if err != nil {
			log.Fatal(err)
		} else {
			conceptInsertCount += 1
			for _, example := range concept.Examples {
				_, err := api.DBQueries.CreateExampleSentence(ctx, database.CreateExampleSentenceParams{
					GrammarConceptID: uuid.NullUUID{
						UUID:  conceptRes.ID,
						Valid: true,
					},
					JapaneseText: sql.NullString{
						String: example.Sentence,
						Valid:  len(example.Sentence) > 0,
					},
					EnglishMeaning: sql.NullString{
						String: example.Meaning,
						Valid:  len(example.Meaning) > 0,
					},
				})
				if err != nil {
					log.Fatal(err)
				} else {
					sentenceInsertCount += 1
				}
			}
		}
	}

	tx.Commit()
	return conceptInsertCount, sentenceInsertCount
}
