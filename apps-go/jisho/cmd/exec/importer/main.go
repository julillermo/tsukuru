package main

import (
	"context"
	"database/sql"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"time"

	"github.com/joho/godotenv"
	"github.com/julillermo/tsukuru/apps-go/jisho/cmd/exec/importer/langcomponent"
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
		log.Print("Error connecting to postgres")
		log.Fatal(err)
	}
	defer utils.CloseDB(dbConn)

	dbQueries := database.New(dbConn)
	jishoAPI := types.NewAPIConfig(dbQueries)

	ctx, cancel := context.WithTimeout(
		context.Background(),
		30*time.Second,
	)
	defer cancel()

	jlptLevels := []types.JLPTLevel{"n5", "n4"}

	jlptVocabularies := langcomponent.ReadAndCombineVocab(
		filepath.Join(repoRoot, "data"),
		jlptLevels...,
	)

	insertCount := langcomponent.CommitVocabulariesToDB(
		jlptVocabularies,
		dbConn,
		ctx,
		jishoAPI,
	)
	fmt.Printf("Successfully inserted %d words to the 'vocabluaries' table\n", insertCount)
}

// TODO Continuation:
// - It's possible to use COPYFROM in sql syntax if you use the pgx driver.
//	This should more easily allow for one large INSERT INTO query.
// 	The sever can maintain the pq driver, and importer can use pgx.
// 	Keeping them separate should maintain the existing server logic flow
// - It might be helpful to add a cascading delete ???
// - Might want to make use of Golang's way of functions throwing up errors.
// 	Current setup appears to generally assume the happy path.
