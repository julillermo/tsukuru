import { Card } from "@/components/base/Card";
import { API_URL } from "@/constants";
import { useQuery } from "@tanstack/react-query";
import { createFileRoute } from "@tanstack/react-router";
import * as styles from "./-history.css";

export const Route = createFileRoute("/history")({
  component: RouteComponent,
});

// TODO: Better organize tanstack query functions and related into their own files/folders
type queryData = {
  sentences: selectedQueryData[];
};

type selectedQueryData = {
  id: string;
  japanese_text: string;
  english_meaning: string;
};

// TODO: Consider pagination of data
// TODO: Eventually include related vocabularies and concepts
// TODO: Use zod to enforce types
function RouteComponent() {
  const { data: createdSentences } = useQuery<queryData, Error, selectedQueryData[]>({
    queryKey: ["createdSentencesHistory"],
    queryFn: async () => {
      const response = await fetch(`${API_URL}/tsukuru/sentences`, { method: "GET" });
      return await response.json();
    },
    select: (createdSentenceRes) =>
      createdSentenceRes.sentences.filter((sntc) => sntc.japanese_text.length > 0),
  });

  return (
    <div className={styles.layout}>
      <div className={styles.sentencesContainer}>
        {/* TODO: this undefined/null check is a little wierd. Address it in the future */}
        {createdSentences != undefined &&
          createdSentences.map((sentence: selectedQueryData) => (
            <Card key={sentence.id} backgroundColor="#c6e4e6" outlineColor="inherit">
              <div className={styles.constructCardHeaderContent}>{sentence.japanese_text}</div>
              <i>{sentence.english_meaning}</i>
            </Card>
          ))}
      </div>
    </div>
  );
}
