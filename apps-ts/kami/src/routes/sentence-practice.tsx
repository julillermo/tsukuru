import { SelectedConstructs } from "@/components/constructed/SelectedConstructs";
import { ConstructBox } from "@/components/constructed/SentenceConstructs";
import { SentenceInput } from "@/components/constructed/SentenceInput";
import { type SentenceConstruct } from "@/types/client/constructs";
import { createFileRoute } from "@tanstack/react-router";
import { useState } from "react";
import * as styles from "./-sentence-practice.css";

export const Route = createFileRoute("/sentence-practice")({
  component: RouteComponent,
});

function RouteComponent() {
  const [constructs, setConstructs] = useState<SentenceConstruct[]>([]);
  const [selectedConstructs, setSelectedConstructs] = useState<SentenceConstruct[]>([]);

  return (
    <div className={styles.layout}>
      <div className={styles.sentenceCreationSection}>
        <SelectedConstructs selectedConstructs={selectedConstructs} />
        <div className={styles.sentenceInputGroup}>
          <SentenceInput />
        </div>
      </div>
      <div className={styles.sentenceConstructsBox}>
        <ConstructBox
          constructs={constructs}
          setConstructs={setConstructs}
          setSelectedConstructs={setSelectedConstructs}
        />
      </div>
    </div>
  );
}
