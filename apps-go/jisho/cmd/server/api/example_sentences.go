package api

import (
	"database/sql"
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/google/uuid"
	db "github.com/julillermo/tsukuru/apps-go/jisho/internal/database"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/types"
	apiType "github.com/julillermo/tsukuru/apps-go/jisho/internal/types/api"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/utils"
)

// TODO: These endpoints likely needs to be protected
func ExampleSentencesAPI(serveMux *http.ServeMux, api *types.APIConfig) {
	CreateExampleSentence(serveMux, api)
	GetExampleSentenceById(serveMux, api)
	UpdateExampleSentencById(serveMux, api)
}

func CreateExampleSentence(serveMux *http.ServeMux, api *types.APIConfig) {
	serveMux.HandleFunc("POST /api/example_sentences", func(writer http.ResponseWriter, request *http.Request) {
		decoder := json.NewDecoder(request.Body)
		defer request.Body.Close()

		reqJSON := apiType.ReqCreateExampleSentence{}
		if err := decoder.Decode(&reqJSON); err != nil {
			log.Print(err)
			_ = utils.RespondWithError(writer, http.StatusBadRequest, "failed to decode request json")
			return
		}

		grammarConceptID, err := uuid.Parse(reqJSON.GrammarConceptId)
		if err != nil {
			log.Print(err)
			_ = utils.RespondWithError(writer, http.StatusBadRequest, "failed to parse grammar concept UUID")
			return
		}

		sentenceRes, err := api.DBQueries.CreateExampleSentence(request.Context(),
			db.CreateExampleSentenceParams{
				GrammarConceptID: uuid.NullUUID{
					UUID:  grammarConceptID,
					Valid: true,
				},
				JapaneseText: sql.NullString{
					String: reqJSON.JapaneseText,
					Valid:  len(reqJSON.JapaneseText) > 0,
				},
				EnglishMeaning: sql.NullString{
					String: reqJSON.EnglishMeaning,
					Valid:  len(reqJSON.EnglishMeaning) > 0,
				},
			})
		if err != nil {
			log.Print(err)
			_ = utils.RespondWithError(writer, http.StatusInternalServerError,
				"failure to create example sentence entry",
			)
			return
		}

		_ = utils.RespondWithJSON(writer, http.StatusOK, apiType.ResCreateExampleSentence{
			ExampleSentenceDbEntryDetails: apiType.ExampleSentenceDbEntryDetails{
				CreatedAt: sentenceRes.CreatedAt.Time.Format(time.RFC3339),
				UpdatedAt: sentenceRes.UpdatedAt.Time.Format(time.RFC3339),
			},
			ExampleSentenceDbEntry: apiType.ExampleSentenceDbEntry{
				Id:             sentenceRes.ID.String(),
				JapaneseText:   sentenceRes.JapaneseText.String,
				EnglishMeaning: sentenceRes.EnglishMeaning.String,
			},
		})
	})
}

func GetExampleSentenceById(serveMux *http.ServeMux, api *types.APIConfig) {
	serveMux.HandleFunc("GET /api/example_sentences/{id}", func(writer http.ResponseWriter, request *http.Request) {
		sentenceUUID, err := uuid.Parse(request.PathValue("id"))
		if err != nil {
			log.Print(err)
			_ = utils.RespondWithError(writer, http.StatusBadRequest, "malformed grammar UUID")
			return
		}

		sentenceRes, err := api.DBQueries.GetExampleSentenceWithGrammarConcept(
			request.Context(),
			sentenceUUID,
		)
		if err != nil {
			log.Print(err)
			if errors.Is(err, sql.ErrNoRows) {
				_ = utils.RespondWithError(writer, http.StatusNotFound,
					fmt.Sprintf("example_sentence with id %s not found", sentenceUUID),
				)
			} else {
				_ = utils.RespondWithError(writer, http.StatusInternalServerError,
					fmt.Sprintf("could not retrieve example sentence: %s", sentenceUUID),
				)
			}
			return
		}

		_ = utils.RespondWithJSON(writer, http.StatusOK, apiType.ResGetExampleSentenceById{
			ExampleSentenceDbEntryDetails: apiType.ExampleSentenceDbEntryDetails{
				CreatedAt: sentenceRes.CreatedAt.Time.Format(time.RFC3339),
				UpdatedAt: sentenceRes.UpdatedAt.Time.Format(time.RFC3339),
			},
			ExampleSentenceDbEntry: apiType.ExampleSentenceDbEntry{
				Id:             sentenceRes.ID.String(),
				JapaneseText:   sentenceRes.JapaneseText.String,
				EnglishMeaning: sentenceRes.EnglishMeaning.String,
			},
			GrammarConcept: apiType.GrammarConceptDbEntry{
				Id:         sentenceRes.GrammarConceptID.UUID.String(),
				JLPTLevel:  types.JLPTLevel(sentenceRes.GrammarConceptJlptLevel.JlptLevelEnum),
				Concept:    sentenceRes.GrammarConcept.String,
				Definition: sentenceRes.GrammarDefinition.String,
			},
		})
	})
}

func UpdateExampleSentencById(serveMux *http.ServeMux, api *types.APIConfig) {
	serveMux.HandleFunc("PATCH /api/example_sentences/{id}", func(writer http.ResponseWriter, request *http.Request) {
		sentenceId, err := uuid.Parse(request.PathValue("id"))
		if err != nil {
			log.Print(err)
			_ = utils.RespondWithError(writer, http.StatusBadRequest, "malformed example_sentence UUID")
			return
		}

		decoder := json.NewDecoder(request.Body)
		defer request.Body.Close()

		reqJSON := apiType.ReqUpdateExampleSentenceById{}
		if err := decoder.Decode(&reqJSON); err != nil {
			log.Print(err)
			_ = utils.RespondWithError(writer, http.StatusBadRequest, "failed to decode request json")
			return
		}

		// TODO: this could possibly become its own utility function
		// Might not need it depending on whether I figure out whether *ptr approach
		// 	is necessary for optional payload parameters
		var grammarConceptID uuid.NullUUID
		if reqJSON.GrammarConceptId != nil {
			parsedID, err := uuid.Parse(*reqJSON.GrammarConceptId)
			if err != nil {
				log.Print(err)
				_ = utils.RespondWithError(writer, http.StatusBadRequest, "failed to parse grammar concept UUID")
				return
			}
			grammarConceptID = uuid.NullUUID{
				UUID:  parsedID,
				Valid: true,
			}
		}

		sentenceRes, err := api.DBQueries.UpdateExampleSentenceById(request.Context(), db.UpdateExampleSentenceByIdParams{
			ID: sentenceId,
			JapaneseText: sql.NullString{
				String: utils.GetOptStringInput(reqJSON.JapaneseText),
				Valid:  utils.ValidateOptStringInput(reqJSON.JapaneseText),
			},
			EnglishMeaning: sql.NullString{
				String: utils.GetOptStringInput(reqJSON.EnglishMeaning),
				Valid:  utils.ValidateOptStringInput(reqJSON.EnglishMeaning),
			},
			GrammarConceptID: grammarConceptID,
		})

		_ = utils.RespondWithJSON(writer, http.StatusOK, apiType.ResUpdateExampleSentenceById{
			ExampleSentenceDbEntryDetails: apiType.ExampleSentenceDbEntryDetails{
				CreatedAt: sentenceRes.CreatedAt.Time.Format(time.RFC3339),
				UpdatedAt: sentenceRes.UpdatedAt.Time.Format(time.RFC3339),
			},
			ExampleSentenceDbEntry: apiType.ExampleSentenceDbEntry{
				Id:             sentenceRes.ID.String(),
				JapaneseText:   sentenceRes.JapaneseText.String,
				EnglishMeaning: sentenceRes.EnglishMeaning.String,
			},
		})
	})
}
