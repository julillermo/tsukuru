package service

import (
	"database/sql"
	"encoding/json"
	"log"
	"net/http"
	"time"

	"github.com/google/uuid"
	db "github.com/julillermo/tsukuru/apps-go/jisho/internal/database"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/types"
	apiType "github.com/julillermo/tsukuru/apps-go/jisho/internal/types/api"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/utils"
)

func CreatedSentences(serveMux *http.ServeMux, api *types.APIConfig, dbConn *sql.DB) {
	createSentence(serveMux, api, dbConn)
}

func createSentence(serveMux *http.ServeMux, api *types.APIConfig, dbConn *sql.DB) {
	serveMux.HandleFunc("POST /tsukuru/sentences", func(writer http.ResponseWriter, request *http.Request) {
		decoder := json.NewDecoder(request.Body)
		defer request.Body.Close()

		reqJSON := apiType.ReqCreateSentence{}
		if err := decoder.Decode(&reqJSON); err != nil {
			log.Print(err)
			_ = utils.RespondWithError(writer, http.StatusBadRequest, "failed to decode request json")
			return
		}

		vocabularyIDs, err := utils.ParseUUIDsFromStringList(reqJSON.VocabularyIds)
		if err != nil {
			log.Print(err)
			_ = utils.RespondWithError(writer, http.StatusBadRequest, "failed to parse vocabulary UUID")
			return
		}
		grammarConceptIDs, err := utils.ParseUUIDsFromStringList(reqJSON.GrammarConceptIds)
		if err != nil {
			log.Print(err)
			_ = utils.RespondWithError(writer, http.StatusBadRequest, "failed to parse grammar concept UUID")
			return
		}

		tx, err := dbConn.BeginTx(request.Context(), nil)
		if err != nil {
			log.Print(err)
			_ = utils.RespondWithError(writer, http.StatusInternalServerError, "failed to begin transaction")
			return
		}
		defer tx.Rollback()
		queries := api.DBQueries.WithTx(tx)

		sentenceRes, err := queries.CreateCreatedSentence(request.Context(),
			db.CreateCreatedSentenceParams{
				JapaneseText:   sql.NullString{String: reqJSON.JapaneseText, Valid: len(reqJSON.JapaneseText) > 0},
				EnglishMeaning: sql.NullString{String: reqJSON.EnglishMeaning, Valid: len(reqJSON.EnglishMeaning) > 0},
			},
		)
		if err != nil {
			log.Print(err)
			_ = utils.RespondWithError(writer, http.StatusInternalServerError, "failure to create created sentence entry")
			return
		}

		for _, vocabularyID := range vocabularyIDs {
			_, err = queries.CreateCreatedSentencesVocabularies(request.Context(),
				db.CreateCreatedSentencesVocabulariesParams{
					CreatedSentenceID: uuid.NullUUID{UUID: sentenceRes.ID, Valid: true},
					VocabularyID:      uuid.NullUUID{UUID: vocabularyID, Valid: true},
				})
			if err != nil {
				log.Print(err)
				_ = utils.RespondWithError(writer, http.StatusInternalServerError, "failure to create sentence vocabulary entry")
				return
			}
		}

		for _, grammarConceptID := range grammarConceptIDs {
			_, err = queries.CreateCreatedSentencesGrammarConcepts(request.Context(),
				db.CreateCreatedSentencesGrammarConceptsParams{
					CreatedSentenceID: uuid.NullUUID{UUID: sentenceRes.ID, Valid: true},
					GrammarConceptID:  uuid.NullUUID{UUID: grammarConceptID, Valid: true},
				})
			if err != nil {
				log.Print(err)
				_ = utils.RespondWithError(writer, http.StatusInternalServerError, "failure to create sentence grammar concept entry")
				return
			}
		}

		if err := tx.Commit(); err != nil {
			log.Print(err)
			_ = utils.RespondWithError(writer, http.StatusInternalServerError, "failed to commit transaction")
			return
		}

		_ = utils.RespondWithJSON(writer, http.StatusOK, apiType.ResCreateSentence{
			CreatedSentencDbEntryDetails: apiType.CreatedSentencDbEntryDetails{
				CreatedAt: sentenceRes.CreatedAt.Time.Format(time.RFC3339),
				UpdatedAt: sentenceRes.UpdatedAt.Time.Format(time.RFC3339),
			},
			CreatedSentenceDbEntry: apiType.CreatedSentenceDbEntry{
				Id:             sentenceRes.ID.String(),
				JapaneseText:   sentenceRes.JapaneseText.String,
				EnglishMeaning: sentenceRes.EnglishMeaning.String,
			},
		})
	})
}
