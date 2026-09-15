package utils

import (
	"errors"
	"log"
	"slices"

	"github.com/google/uuid"
	"github.com/julillermo/tsukuru/apps-go/jisho/internal/types"
)

type StringOrJLPTLevel interface {
	string | types.JLPTLevel
}

func IsJLPTLevel[T StringOrJLPTLevel](text T) bool {
	return slices.Contains(
		[]types.JLPTLevel{"n5", "n4", "n3", "n2", "n1"},
		types.JLPTLevel(text),
	)
}

type StringOrSorting interface {
	string | types.Sorting
}

func IsSorting[T StringOrSorting](text T) bool {
	return slices.Contains(
		[]types.Sorting{"Ascending", "Descending"},
		types.Sorting(text),
	)
}

func ParseUUIDsFromStringList(uuidStringList []string) ([]uuid.UUID, error) {
	uuidSlice := make([]uuid.UUID, len(uuidStringList))
	for idx, uuidString := range uuidStringList {
		UUID, err := uuid.Parse(uuidString)
		if err != nil {
			log.Print(err)
			return nil, errors.New("received invalid UUID string")
		}
		uuidSlice[idx] = UUID
	}
	return uuidSlice, nil
}
