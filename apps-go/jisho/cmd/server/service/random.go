package service

import (
	"fmt"
	"log"
	"net/http"
	"strconv"

	"github.com/julillermo/tsukuru/apps-go/jisho/internal/types"
	apiType "github.com/julillermo/tsukuru/apps-go/jisho/internal/types/api"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/utils"
)

// TODO: These endpoints likely needs to be protected
func RandomizationAPI(serveMux *http.ServeMux, api *types.APIConfig) {
	GetRandomSentenceConstructs(serveMux, api)
}

func GetRandomSentenceConstructs(serveMux *http.ServeMux, api *types.APIConfig) {
	serveMux.HandleFunc("GET /tsukuru/constructs/random", func(writer http.ResponseWriter, request *http.Request) {
		vocabNumParam := request.URL.Query().Get("vocabs")
		conceptNumParam := request.URL.Query().Get("concepts")

		// TODO: This feels like it could be a utility
		var vocabNum int32
		if len(vocabNumParam) <= 0 {
			vocabNum = 1
		} else {
			value, err := strconv.ParseInt(vocabNumParam, 10, 32)
			if err != nil {
				log.Print(err)
				_ = utils.RespondWithError(writer, http.StatusBadRequest,
					fmt.Sprintf("invalid vocab parameter: %s", vocabNumParam),
				)
				return
			}
			vocabNum = int32(value)
		}

		// TODO: This feels like it could be a utility
		var conceptNum int32
		if len(conceptNumParam) <= 0 {
			conceptNum = 1
		} else {
			value, err := strconv.ParseInt(conceptNumParam, 10, 32)
			if err != nil {
				log.Print(err)
				_ = utils.RespondWithError(writer, http.StatusBadRequest,
					fmt.Sprintf("invalid concept parameter: %s", conceptNumParam),
				)
				return
			}
			conceptNum = int32(value)
		}

		grammarConceptsRes, err := api.DBQueries.GetRandomGrammarConcepts(request.Context(), conceptNum)
		if err != nil {
			log.Print(err)
			_ = utils.RespondWithError(writer, http.StatusInternalServerError,
				fmt.Sprintf("could not retrieve %w number of random grammar concepts", conceptNum),
			)
		}

		vocabulariesRes, err := api.DBQueries.GetRandomVocabularies(request.Context(), vocabNum)
		if err != nil {
			log.Print(err)
			_ = utils.RespondWithError(writer, http.StatusInternalServerError,
				fmt.Sprintf("could not retrieve %w number of random sentences", vocabNum),
			)
		}

		_ = utils.RespondWithJSON(writer, http.StatusOK, apiType.ResTsukuruGetRandomConstructs{
			Vocabularies:    utils.ConvertVocabularySliceDBtoAPI(vocabulariesRes),
			GrammarConcepts: utils.ConvertGrammarConceptsRowDBtoAPI(grammarConceptsRes),
		})
	})
}
