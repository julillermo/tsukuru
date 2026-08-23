package main

import (
	"database/sql"
	"log"
	"net/http"
	"os"

	"github.com/joho/godotenv"
	"github.com/julillermo/tsukuru/apps-go/jisho/cmd/server/api"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/database"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/types"
	_ "github.com/lib/pq"
)

func main() {
	if err := godotenv.Load("../../.env"); err != nil {
		log.Printf("warning: could not load .env: %v", err)
	}
	dbURL := os.Getenv("DB_URL")

	db, psqlConnErr := sql.Open("postgres", dbURL)
	if psqlConnErr != nil {
		log.Printf("Error marshalling JSON: %s", psqlConnErr)
		os.Exit(1)
	}
	defer func() {
		if err := db.Close(); err != nil {
			log.Printf("error closing database: %v", err)
		}
	}()

	dbQueries := database.New(db)
	serveMux := http.NewServeMux()
	jishoServer := &http.Server{
		Addr:    ":8081",
		Handler: serveMux,
	}

	jishoAPI := types.NewAPIConfig(dbQueries)

	api.HealthAPI(serveMux, jishoAPI)       // /api/kenko
	api.VocabulariesAPI(serveMux, jishoAPI) // /api/vocabularies

	log.Fatal(jishoServer.ListenAndServe())
}

// TODO CONTINUATION:
// - Learn how to setup go as a monorepo
// - Apply basic protection to select routes (in the future)
