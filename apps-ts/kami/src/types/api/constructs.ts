export type JLPTLevel = "n5" | "n4";

export type VocabularyApi = {
  id: string;
  jlpt_level: JLPTLevel;
  wiki_index: number;
  kana_writing: string;
  kanji: string;
  // TODO: Be more specific on possible classification options later on. Can be determined from Jisho backend
  classification: string[];
  definition: string;
};

export type GrammarConceptApi = {
  id: string;
  jlpt_level: JLPTLevel;
  concept: string;
  definition: string;
  examples: ExampleSentence[];
};

export type ExampleSentence = {
  id: string;
  japanese_text: string;
  english_meaning: string;
};

export type ConstructsApi = {
  vocabularies: VocabularyApi[];
  grammar_concepts: GrammarConceptApi[];
};
