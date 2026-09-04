import UndrawBuildMode from "@/assets/undraw/build-mode.svg";
import * as styles from "./PageUnderConstruction.css";
import { useLocation } from "@tanstack/react-router";
import { Text } from "../base/Text";

export function PageUnderConstruction() {
  const location = useLocation();

  return (
    <div className={styles.layout}>
      <div className={styles.imageContainer}>
        <img height="640px" src={UndrawBuildMode} />
      </div>
      <div className={styles.textGroup}>
        <div className={styles.titleGroup}>
          <Text className={styles.title}>{location.pathname}</Text>
        </div>
        <div className={styles.bodyGroup}>
          <Text>🚧 This page is currently under construction ...</Text>
          <Text>⏳️ Please visit again at a later time ...</Text>
        </div>
      </div>
    </div>
  );
}
