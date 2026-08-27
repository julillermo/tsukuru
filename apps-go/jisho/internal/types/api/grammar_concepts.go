package api

type CommonGrammarConceptDbEntryDetails struct {
	Id        string `json:"id"`
	CreatedAt string `json:"created_at"`
	UpdatedAt string `json:"updated_at"`
}

type GrammarConceptDbEntry struct {
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
	CommonGrammarConceptDbEntryDetails
	GrammarConceptDbEntry
}

type ReqUpdateGrammarConceptById struct {
	GrammarConceptDbEntryUpdate
}
type ResUpdateGrammarConceptById struct {
	CommonGrammarConceptDbEntryDetails
	GrammarConceptDbEntry
}

type ResGetGrammarConceptById struct {
	CommonGrammarConceptDbEntryDetails
	GrammarConceptDbEntry
}
