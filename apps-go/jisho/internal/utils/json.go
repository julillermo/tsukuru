package utils

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
)

func SaveJSONToFile(payload interface{}, path string) {
	// Use json.Marshal() to convert to []bytes with JSON considerations
	payloadByte, err := json.Marshal(payload)
	if err != nil {
		log.Printf("Error marshalling JSON: %s", err)
	}
	os.WriteFile(path, payloadByte, 0644)

	fmt.Printf("Successfully saved JSON as %s\n", path)
}

func RespondWithJSON(w http.ResponseWriter, code int, payload interface{}) error {
	response, err := json.Marshal(payload)
	if err != nil {
		return err
	}
	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.WriteHeader(code)
	w.Write(response)
	return nil
}

func RespondWithError(w http.ResponseWriter, code int, msg string) error {
	return RespondWithJSON(w, code, map[string]string{"error": msg})
}
