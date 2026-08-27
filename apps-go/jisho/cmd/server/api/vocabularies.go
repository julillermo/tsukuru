package api

import (
	"database/sql"
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
	"time"

	"github.com/google/uuid"
	db "github.com/julillermo/tsukuru/apps-go/jisho/internal/database"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/types"
	apiType "github.com/julillermo/tsukuru/apps-go/jisho/internal/types/api"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/utils"
)

// TODO: These endpoints likely needs to be protected
func VocabulariesAPI(serveMux *http.ServeMux, api *types.APIConfig) {
	CreateVocabulary(serveMux, api)
	GetVocabularyByID(serveMux, api)
	UpdateVocabularyById(serveMux, api)
}

func CreateVocabulary(serveMux *http.ServeMux, api *types.APIConfig) {
	serveMux.HandleFunc("POST /api/vocabularies", func(writer http.ResponseWriter, request *http.Request) {
		decoder := json.NewDecoder(request.Body)
		defer request.Body.Close()

		reqJSON := apiType.ReqCreateVocabulary{}
		if err := decoder.Decode(&reqJSON); err != nil {
			_ = utils.RespondWithError(writer, http.StatusBadRequest, "failed to decode request json")
			return
		}

		vocabRes, err := api.DBQueries.CreateVocabulary(request.Context(), db.CreateVocabularyParams{
			JlptLevel: db.NullJlptLevelEnum{
				JlptLevelEnum: db.JlptLevelEnum(reqJSON.JLPTLevel),
				Valid:         utils.IsJLPTLevel(reqJSON.JLPTLevel)},
			WikiIndex: sql.NullInt32{
				Int32: int32(reqJSON.WikiIndex),
				Valid: reqJSON.WikiIndex > 0,
			},
			Kana: sql.NullString{
				String: reqJSON.Kana,
				Valid:  len(reqJSON.Kana) > 0,
			},
			Kanji: sql.NullString{
				String: reqJSON.Kanji,
				Valid:  len(reqJSON.Kanji) > 0,
			},
			Classification: reqJSON.Classification,
			Definition: sql.NullString{
				String: reqJSON.Definition,
				Valid:  len(reqJSON.Definition) > 0,
			},
		})
		if err != nil {
			_ = utils.RespondWithError(writer, http.StatusInternalServerError, "failure to create vocabulary entry")
			return
		}

		_ = utils.RespondWithJSON(writer, http.StatusOK, apiType.ResCreateVocabulary{
			CommonVocabularyDbEntryDetails: apiType.CommonVocabularyDbEntryDetails{
				Id:        vocabRes.ID.String(),
				CreatedAt: vocabRes.CreatedAt.Time.Format(time.RFC3339),
				UpdatedAt: vocabRes.UpdatedAt.Time.Format(time.RFC3339),
			},
			VocabularyDbEntry: apiType.VocabularyDbEntry{
				JLPTLevel:      types.JLPTLevel(vocabRes.JlptLevel.JlptLevelEnum),
				WikiIndex:      int(vocabRes.WikiIndex.Int32),
				Kana:           vocabRes.Kana.String,
				Kanji:          vocabRes.Kana.String,
				Classification: vocabRes.Classification,
				Definition:     vocabRes.Definition.String,
			},
		})
	})
}

func GetVocabularyByID(serveMux *http.ServeMux, api *types.APIConfig) {
	serveMux.HandleFunc("GET /api/vocabularies/{id}", func(writer http.ResponseWriter, request *http.Request) {
		vocabId, err := uuid.Parse(request.PathValue("id"))
		if err != nil {
			_ = utils.RespondWithError(writer, http.StatusBadRequest, "malformed vocabulary UUID")
			return
		}

		vocabRes, err := api.DBQueries.GetVocabularyById(request.Context(), vocabId)
		if err != nil {
			if errors.Is(err, sql.ErrNoRows) {
				_ = utils.RespondWithError(writer, http.StatusNotFound,
					fmt.Sprintf("vocabulary with id %s not found", vocabId),
				)
			}
			_ = utils.RespondWithError(writer, http.StatusInternalServerError,
				fmt.Sprintf("could not get vocabulary: %s", vocabId),
			)
			return
		}

		_ = utils.RespondWithJSON(writer, http.StatusOK, apiType.ResGetVocabularyById{
			CommonVocabularyDbEntryDetails: apiType.CommonVocabularyDbEntryDetails{
				Id:        vocabRes.ID.String(),
				CreatedAt: vocabRes.CreatedAt.Time.Format(time.RFC3339),
				UpdatedAt: vocabRes.UpdatedAt.Time.Format(time.RFC3339),
			},
			VocabularyDbEntry: apiType.VocabularyDbEntry{
				WikiIndex:      int(vocabRes.WikiIndex.Int32),
				Kana:           vocabRes.Kana.String,
				Kanji:          vocabRes.Kana.String,
				Classification: vocabRes.Classification,
				Definition:     vocabRes.Definition.String,
			},
		})
	})
}

func UpdateVocabularyById(serveMux *http.ServeMux, api *types.APIConfig) {
	serveMux.HandleFunc("PATCH /api/vocabularies/{id}", func(writer http.ResponseWriter, request *http.Request) {
		vocabId, err := uuid.Parse(request.PathValue("id"))
		if err != nil {
			_ = utils.RespondWithError(writer, http.StatusBadRequest, "malformed vocabulary UUID")
			return
		}

		decoder := json.NewDecoder(request.Body)
		defer request.Body.Close()

		reqJSON := apiType.ReqUpdateVocabularyById{}
		if err := decoder.Decode(&reqJSON); err != nil {
			_ = utils.RespondWithError(writer, http.StatusBadRequest, "failed to decode request json")
			return
		}

		vocabRes, err := api.DBQueries.UpdateVocabularyById(request.Context(), db.UpdateVocabularyByIdParams{
			ID: vocabId,
			WikiIndex: sql.NullInt32{
				Int32: utils.GetOptInt32Input(reqJSON.WikiIndex),
				Valid: utils.ValidateOptInt32Input(reqJSON.WikiIndex),
			},
			Kana: sql.NullString{
				String: utils.GetOptStringInput(reqJSON.Kana),
				Valid:  utils.ValidateOptStringInput(reqJSON.Kana),
			},
			Kanji: sql.NullString{
				String: utils.GetOptStringInput(reqJSON.Kanji),
				Valid:  utils.ValidateOptStringInput(reqJSON.Kanji),
			},
			Classification: utils.GetOptSliceInput(reqJSON.Classification),
			Definition: sql.NullString{
				String: utils.GetOptStringInput(reqJSON.Definition),
				Valid:  utils.ValidateOptStringInput(reqJSON.Definition),
			},
		})
		if err != nil {
			_ = utils.RespondWithError(writer, http.StatusInternalServerError, fmt.Sprintf("failure to update vocabularies entry %v", vocabId))
			return
		}

		_ = utils.RespondWithJSON(writer, http.StatusOK, apiType.ResUpdateVocabularyById{
			CommonVocabularyDbEntryDetails: apiType.CommonVocabularyDbEntryDetails{
				Id:        vocabRes.ID.String(),
				CreatedAt: vocabRes.CreatedAt.Time.Format(time.RFC3339),
				UpdatedAt: vocabRes.UpdatedAt.Time.Format(time.RFC3339),
			},
			VocabularyDbEntry: apiType.VocabularyDbEntry{
				WikiIndex:      int(vocabRes.WikiIndex.Int32),
				Kana:           vocabRes.Kana.String,
				Kanji:          vocabRes.Kanji.String,
				Classification: vocabRes.Classification,
				Definition:     vocabRes.Definition.String,
			},
		})
	})
}
