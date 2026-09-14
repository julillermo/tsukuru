import { API_URL } from "@/constants";
import type { SentenceConstruct } from "@/types/client/constructs";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { useState } from "react";
import { Button } from "../base/Button";
import { TextArea } from "../base/TextArea";
import * as styles from "./SentenceInput.css";

type SentenceInputProps = {
  selectedConstructs: SentenceConstruct[];
};
export function SentenceInput(props: SentenceInputProps) {
  const queryClient = useQueryClient();
  const [japaneseSentence, setJapaneseSentence] = useState<string>();
  const [englishMeaning, setEnglishMeaning] = useState<string>();

  const postSentenceMutation = useMutation({
    mutationFn: async () => {
      // TODO: revisit how error handling is done with fetch()
      // Also checkout the useQuery in /sentence-practice
      const response = await fetch(`${API_URL}/tsukuru/sentences`, {
        method: "POST",
        body: JSON.stringify({
          japanese_text: japaneseSentence,
          english_meaning: englishMeaning,
          vocabulary_ids: props.selectedConstructs
            .filter((con) => con.type === "vocabulary")
            .map((con) => con.id),
          grammar_concept_ids: props.selectedConstructs
            .filter((con) => con.type === "grammar_concept")
            .map((con) => con.id),
        }),
      });

      const body = await response.text();

      if (!response.ok) {
        throw new Error(`POST failed (${response.status}):\n ${body}`);
      }

      return body ? JSON.parse(body) : null;
    },
    onSuccess: async (_data) => {
      // TODO: Revisit this. This should correspond with the /history page
      // The history page will eventually query to load all past created_sentences entries
      await queryClient.invalidateQueries({
        queryKey: ["createdSentences"],
      });
    },
  });

  return (
    <div className={styles.sentenceInputContainer}>
      <div className={styles.sentenceInput}>
        <TextArea
          value={japaneseSentence}
          onChange={setJapaneseSentence}
          label="Constructed Japanese sentence:"
          description="Create a sentence from the selected constructs into the above field."
        />
        <TextArea
          value={englishMeaning}
          onChange={setEnglishMeaning}
          label="Intended English meaning:"
          description="Give your best english translation of the japanese sentence you just constructed."
        />
      </div>
      <Button
        backgroundColor="#763ba5"
        onClick={() => {
          postSentenceMutation.mutate();
        }}
      >
        Submit
      </Button>
    </div>
  );
}
