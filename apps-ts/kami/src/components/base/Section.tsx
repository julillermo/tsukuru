import type { ReactNode } from "react";
import * as styles from "./Section.css";
import { assignInlineVars } from "@vanilla-extract/dynamic";

export type SectionProps = {
  children?: ReactNode;
};
export function Section(props: SectionProps) {
  return <div className={styles.section}>{props.children}</div>;
}

export type SubectionProps = {
  children?: ReactNode;
  height?: "100%" | "auto";
  grow?: boolean;
};
export function Subsection(props: SubectionProps) {
  return (
    <div
      className={styles.subsection}
      style={{
        ...assignInlineVars({ [styles.subSectionHeight]: props.height }),
        ...(props.grow ? { grow: 1, minHeight: 0 } : {}),
      }}
    >
      {props.children}
    </div>
  );
}
