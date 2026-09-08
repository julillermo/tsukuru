import type { GrammarConceptApi, VocabularyApi } from "../api/constructs";

export type ConstructType = "vocabulary" | "grammar_concept";

export type VocabularyClient = VocabularyApi & {
  type: ConstructType;
};

export type GrammarConceptClient = GrammarConceptApi & {
  type: ConstructType;
};

export type SentenceConstruct = VocabularyClient | GrammarConceptClient;

// ===== TypeGuards =====
export function isVocabularyClient(construct: SentenceConstruct): construct is VocabularyClient {
  return construct.type == "vocabulary";
}

export function isGrammarConceptClient(
  construct: SentenceConstruct,
): construct is GrammarConceptClient {
  return construct.type == "grammar_concept";
}
