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
func GrammarConceptsAPI(serveMux *http.ServeMux, api *types.APIConfig) {
	CreateGrammarConcept(serveMux, api)
	GetGrammarConceptById(serveMux, api)
	UpdateGrammarConceptById(serveMux, api)
}

func CreateGrammarConcept(serveMux *http.ServeMux, api *types.APIConfig) {
	serveMux.HandleFunc("POST /api/grammar_concepts", func(writer http.ResponseWriter, request *http.Request) {
		decoder := json.NewDecoder(request.Body)
		defer request.Body.Close()

		reqJSON := apiType.ReqCreateGrammarConcept{}
		if err := decoder.Decode(&reqJSON); err != nil {
			_ = utils.RespondWithError(writer, http.StatusBadRequest, "failed to decode request json")
			return
		}

		conceptRes, err := api.DBQueries.CreateGrammarConcept(request.Context(), db.CreateGrammarConceptParams{
			Concept: sql.NullString{
				String: reqJSON.Concept,
				Valid:  len(reqJSON.Concept) > 0,
			},
			Definition: sql.NullString{
				String: reqJSON.Definition,
				Valid:  len(reqJSON.Definition) > 0,
			},
		})
		if err != nil {
			_ = utils.RespondWithError(writer, http.StatusInternalServerError, "failure to create vocabulary entry")
			return
		}

		_ = utils.RespondWithJSON(writer, http.StatusOK, apiType.ResCreateGrammarConcept{
			CommonGrammarConceptDbEntryDetails: apiType.CommonGrammarConceptDbEntryDetails{
				Id:        conceptRes.ID.String(),
				CreatedAt: conceptRes.CreatedAt.Time.Format(time.RFC3339),
				UpdatedAt: conceptRes.UpdatedAt.Time.Format(time.RFC3339),
			},
			GrammarConceptDbEntry: apiType.GrammarConceptDbEntry{
				Concept:    conceptRes.Concept.String,
				Definition: conceptRes.Definition.String,
			},
		})
	})
}

func GetGrammarConceptById(serveMux *http.ServeMux, api *types.APIConfig) {
	serveMux.HandleFunc("GET /api/grammar_concepts/{id}", func(writer http.ResponseWriter, request *http.Request) {
		conceptId, err := uuid.Parse(request.PathValue("id"))
		if err != nil {
			_ = utils.RespondWithError(writer, http.StatusBadRequest, "malformed grammar UUID")
			return
		}

		conceptRes, err := api.DBQueries.GetGrammarConceptById(request.Context(), conceptId)
		if err != nil {
			if errors.Is(err, sql.ErrNoRows) {
				_ = utils.RespondWithError(writer, http.StatusNotFound,
					fmt.Sprintf("grammar_concept with id %s not found", conceptId),
				)
			}
			_ = utils.RespondWithError(writer, http.StatusInternalServerError,
				fmt.Sprintf("could not get grammar_concept: %s", conceptId),
			)
			return
		}

		_ = utils.RespondWithJSON(writer, http.StatusOK, apiType.ResGetGrammarConceptById{
			CommonGrammarConceptDbEntryDetails: apiType.CommonGrammarConceptDbEntryDetails{
				Id:        conceptRes.ID.String(),
				CreatedAt: conceptRes.CreatedAt.Time.Format(time.RFC3339),
				UpdatedAt: conceptRes.UpdatedAt.Time.Format(time.RFC3339),
			},
			GrammarConceptDbEntry: apiType.GrammarConceptDbEntry{
				Concept:    conceptRes.Concept.String,
				Definition: conceptRes.Definition.String,
			},
		})
	})
}

func UpdateGrammarConceptById(serveMux *http.ServeMux, api *types.APIConfig) {
	serveMux.HandleFunc("PATCH /api/grammar_concepts/{id}", func(writer http.ResponseWriter, request *http.Request) {
		conceptId, err := uuid.Parse(request.PathValue("id"))
		if err != nil {
			_ = utils.RespondWithError(writer, http.StatusBadRequest, "malformed grammar_concept UUID")
			return
		}

		decoder := json.NewDecoder(request.Body)
		defer request.Body.Close()

		reqJSON := apiType.ReqUpdateGrammarConceptById{}
		if err := decoder.Decode(&reqJSON); err != nil {
			_ = utils.RespondWithError(writer, http.StatusBadRequest, "failed to decode request json")
			return
		}

		conceptRes, err := api.DBQueries.UpdateGrammarConceptById(request.Context(), db.UpdateGrammarConceptByIdParams{
			ID: conceptId,
			Concept: sql.NullString{
				String: utils.GetOptStringInput(reqJSON.Concept),
				Valid:  utils.ValidateOptStringInput(reqJSON.Concept),
			},
			Definition: sql.NullString{
				String: utils.GetOptStringInput(reqJSON.Definition),
				Valid:  utils.ValidateOptStringInput(reqJSON.Definition),
			},
		})
		if err != nil {
			_ = utils.RespondWithError(writer, http.StatusInternalServerError, fmt.Sprintf("failure to update grammar_concepts entry %v", conceptId))
			return
		}

		_ = utils.RespondWithJSON(writer, http.StatusOK, apiType.ResUpdateGrammarConceptById{
			CommonGrammarConceptDbEntryDetails: apiType.CommonGrammarConceptDbEntryDetails{
				Id:        conceptRes.ID.String(),
				CreatedAt: conceptRes.CreatedAt.Time.Format(time.RFC3339),
				UpdatedAt: conceptRes.UpdatedAt.Time.Format(time.RFC3339),
			},
			GrammarConceptDbEntry: apiType.GrammarConceptDbEntry{
				Concept:    conceptRes.Concept.String,
				Definition: conceptRes.Definition.String,
			},
		})
	})
}
