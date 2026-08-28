package importer

import "github.com/julillermo/tsukuru/apps-go/jisho/internal/types"

type ExampleSentencePair struct {
	Sentence string `json:"sentence"`
	Meaning  string `json:"meaning"`
}

type GrammarConceptJSON struct {
	Concept    string                `json:"concept"`
	Definition string                `json:"definition"`
	Examples   []ExampleSentencePair `json:"examples"`
}

type GrammarConceptExampleSentenceDb struct {
	Id        string
	JLPTLevel types.JLPTLevel
	GrammarConceptJSON
	Examples []ExampleSentencePair
}
