export type JLPTLevel = "n5" | "n4";

export type VocabularyClassification =
  | "noun"
  | "pronoun"
  | "type I verb"
  | "type II verb"
  | "type III verb"
  | "adjective"
  | "adjectival noun"
  | "adverb"
  | "attribute"
  | "conjunction"
  | "interjection"
  | "auxiliary"
  | "particle"
  | "prefix"
  | "suffix"
  | "compound";

export type VocabularyApi = {
  id: string;
  jlpt_level: JLPTLevel;
  wiki_index: number;
  kana_writing: string;
  kanji: string;
  classification: VocabularyClassification;
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
