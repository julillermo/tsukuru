package importer

type VocabularyJSON struct {
	WikiIndex      int      `json:"wiki_index"`
	Kana           string   `json:"kana_writing"`
	Kanji          string   `json:"kanji"`
	Classification []string `json:"classification"`
	Definition     string   `json:"definition"`
}
