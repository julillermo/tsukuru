import { API_URL } from "@/constants";
import {
  isGrammarConceptClient,
  isVocabularyClient,
  type GrammarConceptClient,
  type SentenceConstruct,
  type VocabularyClient,
} from "@/types/client/constructs";
import { transformConstructsApiToClient } from "@/utils/api/transformations";
import { useQuery } from "@tanstack/react-query";
import { CircleSmallIcon } from "lucide-react";
import { useEffect, useState } from "react";
import { Button } from "../base/Button";
import { Card } from "../base/Card";
import { Disclosure } from "../base/Disclosure";
import { NumberField } from "../base/NumberField";
import { Section, Subsection } from "../base/Section";
import * as styles from "./SentenceConstructs.css";
import type { ExampleSentence } from "@/types/api/constructs";

type ConstructGeneratorProps = {};
export function ConstructBox(_props: ConstructGeneratorProps) {
  const [vocabNum, setVocabNum] = useState<number>(0);
  const [conceptNum, setConceptNum] = useState<number>(0);
  const [constructs, setConstructs] = useState<SentenceConstruct[]>([]);

  // TODO: Eventually add zod for data validation
  // TODO: It also seems that I don't need the created_at and updated_at from get random API
  const {
    data: constructsData,
    refetch: constructsRefetch,
    isFetched: constructsIsFetched,
  } = useQuery({
    queryKey: ["randomConstructs"],
    queryFn: async () => {
      const response = await fetch(
        `${API_URL}/tsukuru/constructs/random?concepts=${conceptNum}&vocabs=${vocabNum}`,
      );
      return await response.json();
    },
    enabled: false,
  });

  useEffect(() => {
    if (constructsIsFetched) {
      setConstructs(transformConstructsApiToClient(constructsData));
    }
  }, [constructsData]);

  return (
    <Section>
      {/* Query Control */}
      <Subsection>
        <ConstructQueryControl
          vocabNum={vocabNum}
          setVocabNum={setVocabNum}
          conceptNum={conceptNum}
          setConceptNum={setConceptNum}
          onButtonClick={constructsRefetch}
        />
      </Subsection>
      {/* List Control */}
      {/*<Subsection>
        <div></div>
      </Subsection>*/}
      {/* Sentence Constructs List */}
      <Subsection grow>
        <SentenceConstructs constructs={constructs} />
      </Subsection>
    </Section>
  );
}

type ConstructQueryControlProps = {
  vocabNum: number;
  setVocabNum: React.Dispatch<React.SetStateAction<number>>;
  conceptNum: number;
  setConceptNum: React.Dispatch<React.SetStateAction<number>>;
  onButtonClick: () => void;
};
function ConstructQueryControl({
  vocabNum,
  setVocabNum,
  conceptNum,
  setConceptNum,
  onButtonClick,
}: ConstructQueryControlProps) {
  return (
    <>
      <NumberField
        label="Vocabulary"
        value={vocabNum}
        onChange={setVocabNum}
        defaultValue={0}
        minValue={0}
        maxValue={10}
        isWheelDisabled={true}
      />
      <NumberField
        label="Concepts"
        value={conceptNum}
        onChange={setConceptNum}
        defaultValue={0}
        minValue={0}
        maxValue={10}
        isWheelDisabled={true}
      />
      <Button onClick={onButtonClick}>Get!</Button>
    </>
  );
}

type SentenceConstructsProps = {
  constructs: SentenceConstruct[];
};
function SentenceConstructs(props: SentenceConstructsProps) {
  return (
    <div className={styles.sentenceConstructs}>
      {props.constructs.map((construct) => {
        if (isVocabularyClient(construct)) {
          return <VocabularyConstructCard key={construct.id} vocabConstruct={construct} />;
        } else if (isGrammarConceptClient(construct)) {
          return (
            <GrammarConceptConstructCard key={construct.id} grammarConceptConstruct={construct} />
          );
        }
      })}
    </div>
  );
}

type VocabularyConstructCardProps = {
  vocabConstruct: VocabularyClient;
};
function VocabularyConstructCard({ vocabConstruct }: VocabularyConstructCardProps) {
  return (
    <Card key={vocabConstruct.id} backgroundColor="#e6b1b3" outlineColor="#c99b9cFF">
      <Disclosure
        heading={
          <div className={styles.constructCardHeader}>
            <div>{vocabConstruct.kana_writing}</div>
            {vocabConstruct.kanji && vocabConstruct.kanji.length > 0 && (
              <div>〖{vocabConstruct.kanji}〗</div>
            )}
            {/* TODO: JLPT-level looks like it needs more styling to be distinguishable */}
            <div className={styles.constructCardJLPTLevel}>{vocabConstruct.jlpt_level}</div>
          </div>
        }
        content={<div>"{vocabConstruct.definition}"</div>}
      />
    </Card>
  );
}

type GrammarConceptConstructCardProps = {
  grammarConceptConstruct: GrammarConceptClient;
};
function GrammarConceptConstructCard({
  grammarConceptConstruct,
}: GrammarConceptConstructCardProps) {
  return (
    <Card backgroundColor="#6ed8be" outlineColor="#5cb7a0FF">
      <Disclosure
        heading={
          <div className={styles.constructCardHeader}>
            <div>{grammarConceptConstruct.concept}</div>
            <div className={styles.constructCardJLPTLevel}>
              {grammarConceptConstruct.jlpt_level}
            </div>
          </div>
        }
        content={
          <Disclosure
            defaultExpanded={false}
            heading={<div>{grammarConceptConstruct.definition}</div>}
            headingStyle={{ fontSize: "18px", fontWeight: 400 }}
            content={
              <div className={styles.exampleSentenceList}>
                <>
                  {grammarConceptConstruct.examples.map((ex) => (
                    <ExampleSentenceBullet key={ex.id} sentence={ex} />
                  ))}
                </>
              </div>
            }
          />
        }
      />
    </Card>
  );
}

type ExampleSentenceBulletProps = {
  sentence: ExampleSentence;
};
function ExampleSentenceBullet({ sentence }: ExampleSentenceBulletProps) {
  return (
    <div className={styles.exampleSentence}>
      <div className={styles.exampleSentenceBulletRow}>
        <CircleSmallIcon size={16} />
        <div className={styles.exampleSentenceJapaneseText}>{sentence.japanese_text}</div>
      </div>
      <i className={styles.exampleSentenceEnglishMeaning}>{sentence.english_meaning}</i>
    </div>
  );
}
