package service

import (
	"fmt"
	"log"
	"net/http"

	"github.com/julillermo/tsukuru/apps-go/jisho/internal/types"
	apiType "github.com/julillermo/tsukuru/apps-go/jisho/internal/types/api"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/utils"
)

// TODO: These endpoints likely needs to be protected
func ConstructsAPI(serveMux *http.ServeMux, api *types.APIConfig) {
	getRandomSentenceConstructs(serveMux, api)
}

func getRandomSentenceConstructs(serveMux *http.ServeMux, api *types.APIConfig) {
	serveMux.HandleFunc("GET /tsukuru/constructs/random", func(writer http.ResponseWriter, request *http.Request) {
		vocabNumParam := request.URL.Query().Get("vocabs")
		conceptNumParam := request.URL.Query().Get("concepts")

		vocabNum := utils.ParseAPIReqInt(utils.ParseAPIReqIntProps{
			NumString:    vocabNumParam,
			Writer:       writer,
			ErrorMessage: fmt.Sprintf("invalid vocab parameter: %s", vocabNumParam),
		})
		conceptNum := utils.ParseAPIReqInt(utils.ParseAPIReqIntProps{
			NumString:    conceptNumParam,
			Writer:       writer,
			ErrorMessage: fmt.Sprintf("invalid concept parameter: %s", conceptNumParam),
		})

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
