import type { ConstructsApi } from "@/types/api/constructs";
import type {
  GrammarConceptClient,
  SentenceConstruct,
  VocabularyClient,
} from "@/types/client/constructs";

export function transformConstructsApiToClient(constructsApi: ConstructsApi): SentenceConstruct[] {
  const vocabClientList: VocabularyClient[] =
    constructsApi?.vocabularies?.map((vocab) => {
      return {
        type: "vocabulary",
        selected: false,
        ...vocab,
      };
    }) ?? [];
  const conceptClientList: GrammarConceptClient[] =
    constructsApi?.grammar_concepts?.map((grammarConcept) => {
      return {
        type: "grammar_concept",
        selected: false,
        ...grammarConcept,
      };
    }) ?? [];
  return [...vocabClientList, ...conceptClientList];
}
