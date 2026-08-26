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
			_ = utils.RespondWithError(writer, http.StatusBadRequest, "invalid vocabulary UUID")
			return
		}

		vocabRes, err := api.DBQueries.GetVocabularyById(request.Context(), vocabId)
		if err != nil {
			if errors.Is(err, sql.ErrNoRows) {
				_ = utils.RespondWithError(writer, http.StatusNotFound, "vocabulary not found")
				return
			}
			_ = utils.RespondWithError(writer, http.StatusInternalServerError, "could not get vocabulary")

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
			_ = utils.RespondWithError(writer, http.StatusBadRequest, "invalid vocabulary UUID")
			return
		}

		decoder := json.NewDecoder(request.Body)
		defer request.Body.Close()

		reqJSON := apiType.ReqCreateVocabulary{}
		if err := decoder.Decode(&reqJSON); err != nil {
			_ = utils.RespondWithError(writer, http.StatusBadRequest, "failed to decode request json")
		}

		vocabRes, err := api.DBQueries.UpdateVocabularyById(request.Context(), db.UpdateVocabularyByIdParams{
			ID: vocabId,
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
			_ = utils.RespondWithError(writer, http.StatusInternalServerError, fmt.Sprintf("failure to update vocabulary entry %v", vocabId))
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
				Kanji:          vocabRes.Kana.String,
				Classification: vocabRes.Classification,
				Definition:     vocabRes.Definition.String,
			},
		})
	})
}
