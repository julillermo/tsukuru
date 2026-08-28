package api

type GrammarConceptDbEntryDetails struct {
	CreatedAt string `json:"created_at"`
	UpdatedAt string `json:"updated_at"`
}

type GrammarConceptDbEntry struct {
	Id         string `json:"id"`
	Concept    string `json:"concept" validate:"required"`
	Definition string `json:"definition" validate:"required"`
}

type GrammarConceptDbEntryUpdate struct {
	Concept    *string `json:"concept"`
	Definition *string `json:"definition"`
}

type ReqCreateGrammarConcept struct {
	GrammarConceptDbEntry
}
type ResCreateGrammarConcept struct {
	GrammarConceptDbEntryDetails
	GrammarConceptDbEntry
}

type ReqUpdateGrammarConceptById struct {
	GrammarConceptDbEntryUpdate
}
type ResUpdateGrammarConceptById struct {
	GrammarConceptDbEntryDetails
	GrammarConceptDbEntry
}

type ResGetGrammarConceptById struct {
	GrammarConceptDbEntryDetails
	GrammarConceptDbEntry
}
