import type { ConstructsApi } from "@/types/api/constructs";
import type {
  SentenceConstruct,
  VocabularyClient,
  GrammarConceptClient,
} from "@/types/client/constructs";

export function transformConstructsApiToClient(constructsApi: ConstructsApi): SentenceConstruct[] {
  const vocabClientList: VocabularyClient[] =
    constructsApi?.vocabularies?.map((vocab) => {
      return {
        type: "vocabulary",
        ...vocab,
      };
    }) ?? [];
  const conceptClientList: GrammarConceptClient[] =
    constructsApi?.grammar_concepts?.map((grammarConcept) => {
      return {
        type: "grammar_concept",
        ...grammarConcept,
      };
    }) ?? [];
  return [...vocabClientList, ...conceptClientList];
}
