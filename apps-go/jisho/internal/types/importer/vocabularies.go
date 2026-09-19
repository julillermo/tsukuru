package importer

type VocabularyJSON struct {
	WikiIndex int    `json:"wiki_index"`
	Kana      string `json:"kana_writing"`
	Kanji     string `json:"kanji"`
	// ["noun", "pronoun", "type I verb", "type II verb", "type III verb", "adjective", "adjectival noun", "adverb", "attribute", "conjunction", "interjection", "auxiliary", "particle", "prefix", "suffix", "compound" ]
	Classification []string `json:"classification"`
	Definition     string   `json:"definition"`
}
