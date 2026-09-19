import { API_URL } from "@/constants";
import type { SentenceConstruct } from "@/types/client/constructs";
import { validateQueryResponseBody } from "@/utils/queries";
import { mutationOptions, queryOptions, type QueryClient } from "@tanstack/react-query";

// TODO: Consider pagination of data
// TODO: Eventually include related vocabularies and concepts
// TODO: Use zod to enforce types
export type CreatedSentenceHistoryQueryData = {
  sentences: CreatedSentenceHistorySelectedQueryData[];
};

export type CreatedSentenceHistorySelectedQueryData = {
  id: string;
  japanese_text: string;
  english_meaning: string;
};

export const getCreatedSentenceHistoryQuery = () =>
  queryOptions({
    queryKey: ["createdSentencesHistory"],
    queryFn: async () => {
      const response = await fetch(`${API_URL}/tsukuru/sentences`, { method: "GET" });
      return await validateQueryResponseBody(response);
    },
    select: (createdSentenceRes: CreatedSentenceHistoryQueryData) =>
      createdSentenceRes.sentences.filter((sntc) => sntc.japanese_text.length > 0),
  });

type GetSenteceMutationProps = {
  japaneseSentence: string | undefined;
  englishMeaning: string | undefined;
  selectedConstructs: SentenceConstruct[];
  queryClient: QueryClient;
};
export const getSentenceMutation = (props: GetSenteceMutationProps) =>
  mutationOptions({
    mutationFn: async () => {
      if (props.japaneseSentence == undefined || props.englishMeaning == undefined) {
        throw new Error("One or more inputs are undefined");
      }

      const response = await fetch(`${API_URL}/tsukuru/sentences`, {
        method: "POST",
        body: JSON.stringify({
          japanese_text: props.japaneseSentence,
          english_meaning: props.englishMeaning,
          vocabulary_ids: props.selectedConstructs
            .filter((con) => con.type === "vocabulary")
            .map((con) => con.id),
          grammar_concept_ids: props.selectedConstructs
            .filter((con) => con.type === "grammar_concept")
            .map((con) => con.id),
        }),
      });
      return await validateQueryResponseBody(response);
    },
    onSuccess: async () => {
      await props.queryClient.invalidateQueries({
        queryKey: ["createdSentencesHistory"],
      });
    },
  });
