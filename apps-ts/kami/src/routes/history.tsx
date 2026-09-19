import { Card } from "@/components/base/Card";

import {
  getCreatedSentenceHistoryQuery,
  type CreatedSentenceHistorySelectedQueryData,
} from "@/queries/createdSentences";
import { useQuery } from "@tanstack/react-query";
import { createFileRoute } from "@tanstack/react-router";
import * as styles from "./-history.css";

export const Route = createFileRoute("/history")({
  component: RouteComponent,
});

function RouteComponent() {
  const { data: createdSentences } = useQuery(getCreatedSentenceHistoryQuery());

  return (
    <div className={styles.layout}>
      <div className={styles.sentencesContainer}>
        {createdSentences &&
          createdSentences.map((sentence: CreatedSentenceHistorySelectedQueryData) => (
            <Card key={sentence.id} backgroundColor="#c6e4e6" outlineColor="inherit">
              <div className={styles.constructCardHeaderContent}>{sentence.japanese_text}</div>
              <i>{sentence.english_meaning}</i>
            </Card>
          ))}
      </div>
    </div>
  );
}
