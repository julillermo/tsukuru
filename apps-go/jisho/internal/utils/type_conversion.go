package utils

import (
	"errors"
	"log"

	"github.com/google/uuid"
)

type ParseUUIDfromStringProps struct {
	UUIDString string
}

func ParseUUIDfromString(options ParseUUIDfromStringProps) (uuid.UUID, error) {
	UUID, err := uuid.Parse(options.UUIDString)
	if err != nil {
		log.Print(err)
		return uuid.Nil, errors.New("received invalid UUID string")
	}
	return UUID, nil
}

func ParseUUIDsFromStringList(uuidStringList []string) ([]uuid.UUID, error) {
	uuidSlice := make([]uuid.UUID, len(uuidStringList))
	for idx, uuidString := range uuidStringList {
		UUID, err := ParseUUIDfromString(ParseUUIDfromStringProps{UUIDString: uuidString})
		if err != nil {
			return nil, err
		}
		uuidSlice[idx] = UUID
	}
	return uuidSlice, nil
}
