import { Button } from "../base/Button";
import { TextArea } from "../base/TextArea";
import * as styles from "./SentenceInput.css";

export function SentenceInput() {
  return (
    <div className={styles.sentenceInputContainer}>
      <div className={styles.sentenceInput}>
        <TextArea
          label="Constructed Japanese sentence:"
          description="Create a sentence from the selected constructs into the above field."
        />
        <TextArea
          label="Intended English meaning:"
          description="Give your best english translation of the japanese sentence you just constructed."
        />
      </div>
      <Button backgroundColor="#763ba5">Submit</Button>
    </div>
  );
}
