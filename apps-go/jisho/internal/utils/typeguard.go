package utils

import (
	"slices"

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
