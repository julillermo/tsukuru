package main

import (
	"database/sql"
	"log"
	"net/http"
	"os"
	"path/filepath"

	"github.com/joho/godotenv"
	"github.com/julillermo/tsukuru/apps-go/jisho/cmd/server/api"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/database"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/types"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/utils"

	_ "github.com/lib/pq"
)

func main() {
	repoRoot := os.Getenv("REPO_ROOT")
	if err := godotenv.Load(filepath.Join(repoRoot, "/.env")); err != nil {
		log.Printf("warning: could not load .env: %v", err)
	}

	dbURL := os.Getenv("DB_URL")

	dbConn, err := sql.Open("postgres", dbURL)
	if err != nil {
		log.Println("Error connecting to postgres")
		log.Fatal(err)
	}
	defer utils.CloseDB(dbConn)

	dbQueries := database.New(dbConn)
	serveMux := http.NewServeMux()
	jishoServer := &http.Server{
		Addr:    ":8081",
		Handler: serveMux,
	}

	jishoAPI := types.NewAPIConfig(dbQueries)

	api.HealthAPI(serveMux, jishoAPI)          // /api/kenko
	api.VocabulariesAPI(serveMux, jishoAPI)    // /api/vocabularies
	api.GrammarConceptsAPI(serveMux, jishoAPI) // /api/grammar_concepts

	log.Fatal(jishoServer.ListenAndServe())
}

// TODO CONTINUATION:
// - Learn how to setup go as a monorepo
// - Apply basic protection to select routes (in the future)
// - Add a condition where if no postgresql server was provided,
// 		trigger the kezuru scrape and load everything in memory.
// - Weigh in on whether the repeated API code should be generalized
