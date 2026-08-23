package api

import (
	"net/http"

	"github.com/julillermo/tsukuru/apps-go/jisho/internal/types"
)

func HealthAPI(serveMux *http.ServeMux, api *types.APIConfig) {
	serveMux.HandleFunc("GET /api/kenko", func(writer http.ResponseWriter, request *http.Request) {
		writer.Header().Set("Content-Type", "text/plain; charset=utf-8")
		writer.WriteHeader(http.StatusOK)

		body := "OK"
		writer.Write([]byte(body))
	})
}
