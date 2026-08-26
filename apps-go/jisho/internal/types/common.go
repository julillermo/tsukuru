package types

import "github.com/julillermo/tsukuru/apps-go/jisho/internal/database"

// ! Unlike TypeScript and Python, Go doesn't support a type
// 	with limited possible string input. You can instead add
// 	a comment above on at the end of the line to pop-up as
// 	IDE type hints

// ["n5", "n4", "n3", "n2", "n1"]
type JLPTLevel string

// APIConfig holds dependencies and state shared by HTTP handlers
type APIConfig struct {
	DBQueries *database.Queries
}

// NewAPIConfig creates API configuration with database dependencies
func NewAPIConfig(dbQueries *database.Queries) *APIConfig {
	return &APIConfig{DBQueries: dbQueries}
}
