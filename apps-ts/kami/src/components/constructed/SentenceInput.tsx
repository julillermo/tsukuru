import { getSentenceMutation } from "@/queries/createdSentences";
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

  // TODO: Double check logic on preventing submission when inputs are undefined
  const postSentenceMutation = useMutation(
    getSentenceMutation({
      japaneseSentence,
      englishMeaning,
      selectedConstructs: props.selectedConstructs,
      queryClient,
    }),
  );

  return (
    <div className={styles.sentenceInputContainer}>
      <div className={styles.sentenceInput}>
        <TextArea
          value={japaneseSentence}
          onChange={setJapaneseSentence}
          label="Constructed Japanese sentence:"
          description="Create a sentence using the selected constructs above."
        />
        <TextArea
          value={englishMeaning}
          onChange={setEnglishMeaning}
          label="Intended English meaning:"
          description="Give your best english translation of the japanese sentence you just created."
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
