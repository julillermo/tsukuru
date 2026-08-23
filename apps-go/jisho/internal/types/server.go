package types

import (
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/database"
)

// APIConfig holds dependencies and state shared by HTTP handlers
type APIConfig struct {
	DBQueries *database.Queries
}

// NewAPIConfig creates API configuration with database dependencies
func NewAPIConfig(dbQueries *database.Queries) *APIConfig {
	return &APIConfig{DBQueries: dbQueries}
}
