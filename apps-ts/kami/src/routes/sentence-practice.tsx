import { ConstructBox } from "@/components/constructed/SentenceConstructs";
import { createFileRoute } from "@tanstack/react-router";
import * as styles from "./-sentence-practice.css";
// import { TextArea } from "@/components/base/TextArea";

export const Route = createFileRoute("/sentence-practice")({
  component: RouteComponent,
});

function RouteComponent() {
  return (
    <div className={styles.layout}>
      {/*<TextArea />*/}
      <ConstructBox />
    </div>
  );
}
