package utils

import (
	"log"
	"net/http"
	"strconv"

	"github.com/google/uuid"
)

func GetOptInt32Input(value *int) int32 {
	if value == nil {
		return 0
	} else {
		return int32(*value)
	}
}
func ValidateOptInt32Input(value *int) bool {
	return value != nil && *value > 0
}

func GetOptStringInput(value *string) string {
	if value == nil {
		return ""
	} else {
		return *value
	}
}
func ValidateOptStringInput(value *string) bool {
	return value != nil && len(*value) > 0
}

func GetOptSliceInput[T any](value *[]T) []T {
	if value != nil {
		return *value
	} else {
		return nil
	}
}

type ParseAPIReqUUIDStringProps struct {
	UUIDString string
	Writer     http.ResponseWriter
}

func ParseAPIReqUUIDString(props ParseAPIReqUUIDStringProps) uuid.UUID {
	parsedID, err := uuid.Parse(props.UUIDString)
	if err != nil {
		log.Print(err)
		_ = RespondWithError(props.Writer, http.StatusBadRequest, "failed to parse grammar concept UUID")
	}
	return parsedID
}

type ParseAPIReqIntProps struct {
	NumString    string
	Writer       http.ResponseWriter
	ErrorMessage string
}

func ParseAPIReqInt(props ParseAPIReqIntProps) int32 {
	value, err := strconv.ParseInt(props.NumString, 10, 32)
	if err != nil {
		log.Print(err)
		_ = RespondWithError(props.Writer, http.StatusBadRequest, props.ErrorMessage)
	}
	return int32(value)
}
