import {
  isGrammarConceptClient,
  isVocabularyClient,
  type SentenceConstruct,
} from "@/types/client/constructs";
import { Card } from "../base/Card";
import { Label } from "../base/Label";
import { Section } from "../base/Section";
import { Text } from "../base/Text";
import * as styles from "./SelectedConstructs.css";

type SelectedConstructsProps = {
  selectedConstructs: SentenceConstruct[];
};

export function SelectedConstructs({ selectedConstructs }: SelectedConstructsProps) {
  return (
    <div className={styles.selectedConstructsContainer}>
      <Label className={styles.selectedConstructsLabel}>Selected constructs:</Label>
      <Section backgroundColor="#b6a7c1">
        <div
          style={{
            display: "flex",
            flexWrap: "wrap",
            gap: 16,
            padding: 8,
            overflow: "auto",
          }}
        >
          {selectedConstructs.map((construct) => {
            if (isVocabularyClient(construct)) {
              return (
                <Card
                  key={construct.id}
                  backgroundColor="#e6b1b3"
                  outlineWidth="4px"
                  outlineColor="#b78d8e"
                  boxShadow="0px 4px 8px slategrey"
                >
                  <span className={styles.constructCardContent}>{construct.kana_writing}</span>
                </Card>
              );
            } else if (isGrammarConceptClient(construct)) {
              return (
                <Card
                  key={construct.id}
                  backgroundColor="#6ed8be"
                  outlineWidth="4px"
                  outlineColor="#4e9c89"
                  boxShadow="0px 4px 8px slategrey"
                >
                  <span className={styles.constructCardContent}>{construct.concept}</span>
                </Card>
              );
            }
          })}
        </div>
      </Section>
      <Text className={styles.selectedConstructsDescription}>
        Selected constructs are recorded as part of constructed sentence (regardless of whether they
        were used).
      </Text>
    </div>
  );
}
