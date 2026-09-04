import UndrawVoidSVG from "@/assets/undraw/the-void.svg";
import { Text } from "../base/Text";
import * as styles from "./PageMissing.css.ts";

export function PageMissing() {
  return (
    <div className={styles.layout}>
      <div className={styles.imageContainer}>
        <img height="640px" src={UndrawVoidSVG} />
      </div>
      <div className={styles.textGroup}>
        <div className={styles.titleGroup}>
          <Text className={styles.title}>404</Text>
          <Text className={styles.subtitle}>Not Found</Text>
        </div>
        <div className={styles.bodyGroup}>
          <Text>🔭 We can't seem to find what you're looking for.</Text>
        </div>
      </div>
    </div>
  );
}
