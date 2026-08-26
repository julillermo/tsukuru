package langcomponent

import (
	"context"
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"path/filepath"

	"github.com/julillermo/tsukuru/apps-go/jisho/internal/database"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/types"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/types/api"
	apiType "github.com/julillermo/tsukuru/apps-go/jisho/internal/types/api"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/utils"
)

func ReadAndCombineVocab(
	fileDir string,
	levels ...types.JLPTLevel,
) (
	vocabDbEntries []apiType.VocabularyDbEntry,
) {
	for _, level := range levels {
		if !utils.IsJLPTLevel(level) {
			continue
		}

		vocabPath := filepath.Join(fileDir,
			fmt.Sprintf("vocab_%s_combined.json", level),
		)

		// Read as []byte
		data, err := os.ReadFile(vocabPath)
		if err != nil {
			log.Printf("Error reading file %s", vocabPath)
			log.Fatal(err)
		}

		// Parse as JSON-struct
		var vocabularies []apiType.VocabularyDbEntry
		if err := json.Unmarshal(data, &vocabularies); err != nil {
			log.Printf("Error parsing file %s", vocabPath)
			log.Fatal(err)
		}

		for idx := range vocabularies {
			vocabularies[idx].JLPTLevel = level
		}

		vocabDbEntries = append(vocabDbEntries, vocabularies...)
	}

	return
}

func CommitVocabulariesToDB(
	jlptVocabularies []api.VocabularyDbEntry,
	dbConn *sql.DB,
	ctx context.Context,
	api *types.APIConfig,
) (insertCount int32) {
	// Use SQL Transactions
	tx, err := dbConn.BeginTx(ctx, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer tx.Rollback()

	insertCount = 0 // TODO: revisit this? I recall meaning to return the number of added rows
	for _, vocab := range jlptVocabularies {
		_, err := api.DBQueries.CreateVocabulary(ctx, database.CreateVocabularyParams{
			JlptLevel: database.NullJlptLevelEnum{
				JlptLevelEnum: database.JlptLevelEnum(vocab.JLPTLevel),
				Valid:         utils.IsJLPTLevel(vocab.JLPTLevel),
			},
			WikiIndex: sql.NullInt32{
				Int32: int32(vocab.WikiIndex),
				Valid: vocab.WikiIndex > 0,
			},
			Kana: sql.NullString{
				String: vocab.Kana,
				Valid:  len(vocab.Kana) > 0,
			},
			Kanji: sql.NullString{
				String: vocab.Kanji,
				Valid:  len(vocab.Kanji) > 0,
			},
			Classification: vocab.Classification,
			Definition: sql.NullString{
				String: vocab.Definition,
				Valid:  len(vocab.Definition) > 0,
			},
		})
		if err != nil {
			log.Fatal(err)
		} else {
			insertCount += 1
		}
	}

	tx.Commit()

	return insertCount
}
