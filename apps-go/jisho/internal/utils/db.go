package utils

import (
	"database/sql"
	"log"
)

func CloseDB(dbConn *sql.DB) {
	if err := dbConn.Close(); err != nil {
		log.Printf("error closing database: %v", err)
	}
}
