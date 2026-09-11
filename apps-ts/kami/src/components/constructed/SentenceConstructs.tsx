import { API_URL } from "@/constants";
import type { ExampleSentence } from "@/types/api/constructs";
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

type ConstructGeneratorProps = {
  constructs: SentenceConstruct[];
  setConstructs: React.Dispatch<React.SetStateAction<SentenceConstruct[]>>;
  setSelectedConstructs: React.Dispatch<React.SetStateAction<SentenceConstruct[]>>;
};
export function ConstructBox(props: ConstructGeneratorProps) {
  const [vocabNum, setVocabNum] = useState<number>(0);
  const [conceptNum, setConceptNum] = useState<number>(0);

  // TODO: Eventually add zod for data validation
  //    This means that I could also just use zod's infer instead of duplicating types
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
      props.setConstructs(transformConstructsApiToClient(constructsData));
    }
  }, [constructsData]);

  const handleConstructSelected = (constructId: string) => {
    props.setConstructs((prevConstructs) => {
      return prevConstructs.map((construct) =>
        construct.id === constructId ? { ...construct, selected: !construct.selected } : construct,
      );
    });

    const selectedConstruct = props.constructs.find((construct) => construct.id === constructId);
    if (selectedConstruct != undefined) {
      props.setSelectedConstructs((prev) => {
        const alreadySelected = !!prev.find((element) => element.id === selectedConstruct.id);
        if (alreadySelected) {
          return prev.filter((element) => element.id !== selectedConstruct.id);
        } else {
          return [...prev, selectedConstruct];
        }
      });
    }
  };

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
        <SentenceConstructs
          constructs={props.constructs}
          onConstructSelect={handleConstructSelected}
        />
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
  onConstructSelect: (constructId: string) => void;
};
function SentenceConstructs(props: SentenceConstructsProps) {
  return (
    <div className={styles.sentenceConstructs}>
      {props.constructs.map((construct) => {
        if (isVocabularyClient(construct)) {
          return (
            <VocabularyConstructCard
              key={construct.id}
              vocabConstruct={construct}
              onConstructSelect={props.onConstructSelect}
            />
          );
        } else if (isGrammarConceptClient(construct)) {
          return (
            <GrammarConceptConstructCard
              key={construct.id}
              grammarConceptConstruct={construct}
              onConstructSelect={props.onConstructSelect}
            />
          );
        }
      })}
    </div>
  );
}

type VocabularyConstructCardProps = {
  vocabConstruct: VocabularyClient;
  onConstructSelect: (constructId: string) => void;
};
function VocabularyConstructCard({
  vocabConstruct,
  onConstructSelect,
}: VocabularyConstructCardProps) {
  return (
    <Card
      key={vocabConstruct.id}
      backgroundColor="#e6b1b3"
      outlineWidth={vocabConstruct.selected ? "4px" : "2px"}
      outlineStyle={vocabConstruct.selected ? "solid" : "dashed"}
      outlineColor={vocabConstruct.selected ? "#b78d8e" : "#c99b9cFF"}
      boxShadow={vocabConstruct.selected ? "0px 10px 10px slategrey" : "none"}
    >
      <Disclosure
        heading={
          <div
            className={styles.constructCardHeader}
            onClick={() => onConstructSelect(vocabConstruct.id)}
          >
            <div className={styles.constructCardHeaderContent}>
              <div>{vocabConstruct.kana_writing}</div>
              {vocabConstruct.kanji && vocabConstruct.kanji.length > 0 && (
                <div>〖{vocabConstruct.kanji}〗</div>
              )}
              {/* TODO: JLPT-level looks like it needs more styling to be distinguishable */}
              <div className={styles.constructCardJLPTLevel}>{vocabConstruct.jlpt_level}</div>
            </div>
            {/*<div className={styles.constructControlsGroup}>
              <div
                onClick={() => onConstructSelect(vocabConstruct.id)}
                className={styles.constructControl}
              >
                {vocabConstruct.selected ? <SquareCheckBig /> : <SquareIcon />}
              </div>
            </div>*/}
          </div>
        }
        content={<div>"{vocabConstruct.definition}"</div>}
      />
    </Card>
  );
}

type GrammarConceptConstructCardProps = {
  grammarConceptConstruct: GrammarConceptClient;
  onConstructSelect: (constructId: string) => void;
};
function GrammarConceptConstructCard({
  grammarConceptConstruct,
  onConstructSelect,
}: GrammarConceptConstructCardProps) {
  return (
    <Card
      backgroundColor="#6ed8be"
      outlineWidth={grammarConceptConstruct.selected ? "4px" : "2px"}
      outlineStyle={grammarConceptConstruct.selected ? "solid" : "dashed"}
      outlineColor={grammarConceptConstruct.selected ? "#4e9c89" : "#5cb7a0FF"}
      boxShadow={grammarConceptConstruct.selected ? "0px 10px 10px slategrey" : "none"}
    >
      <Disclosure
        heading={
          <div
            className={styles.constructCardHeader}
            onClick={() => onConstructSelect(grammarConceptConstruct.id)}
          >
            <div className={styles.constructCardHeaderContent}>
              <div>{grammarConceptConstruct.concept}</div>
              <div className={styles.constructCardJLPTLevel}>
                {grammarConceptConstruct.jlpt_level}
              </div>
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
