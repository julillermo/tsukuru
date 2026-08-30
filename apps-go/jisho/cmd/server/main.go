package main

import (
	"database/sql"
	"fmt"
	"log"
	"net/http"
	"os"
	"path/filepath"

	"github.com/joho/godotenv"
	"github.com/julillermo/tsukuru/apps-go/jisho/cmd/server/api"
	"github.com/julillermo/tsukuru/apps-go/jisho/cmd/server/service"
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

	api.HealthAPI(serveMux, jishoAPI)           // /api/kenko
	api.VocabulariesAPI(serveMux, jishoAPI)     // /api/vocabularies
	api.GrammarConceptsAPI(serveMux, jishoAPI)  // /api/grammar_concepts
	api.ExampleSentencesAPI(serveMux, jishoAPI) // /api/example_sentences

	service.RandomizationAPI(serveMux, jishoAPI) // /tsukuru

	fmt.Printf("Running Jisho Server on port %s\n", jishoServer.Addr)
	log.Fatal(jishoServer.ListenAndServe())
}

// TODO CONTINUATION:
// - Learn how to setup go as a monorepo
// - Apply basic protection to select routes (in the future)
// - Add a condition where if no postgresql server was provided,
// 		trigger the kezuru scrape and load everything in memory.
// - Weigh in on whether the repeated API code should be generalized/abstracted
// - Double check whether or not I can just stick with `validate:"required"` instead of
// 		also having ptrs to make optional payload entries
// - I read that it's bad practice to return direct database information.
// 		- Add a service layer
// 		- Don't return the entirety of database entries or errors
// - Backends typically follow the folloiwng flow
// 		HTTP client
// 		    ↓
// 		Route / router / handler (serveMux that directly gos to data-access)
// 			1. Read /api/vocabularies/{id}
// 			2. Parse the UUID
// 			3. Decode JSON
// 			4. Convert request DTO to UpdateInput
// 			5. Call the service
// 			6. Convert service errors to HTTP responses
// 			7. Convert the result to JSON
//		    ↓
// 		Controller (missing)
// 			↓
// 		Service layer (missing)
// 			1. Load the existing vocabulary
// 			2. Merge the PATCH fields with existing values
// 			3. Normalize values, such as trimming whitespace
// 			4. Check vocabulary-specific rules
// 			5. Decide what the update means
// 			6. Call the repository/sqlc layer
// 			7. Possibly coordinate multiple database operations
// 			Can be added as by separating the step that reads the payload ++
// 		    ↓
// 		Repository / data-access layer (sqlc)
// 			1. Convert the application values into database parameters
// 			2. Execute the generated query
// 			3. Return the database result or database error
// 		    ↓
// 		Database
