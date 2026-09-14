import { assignInlineVars } from "@vanilla-extract/dynamic";
import type * as CSS from "csstype";
import type { ReactNode } from "react";
import * as styles from "./Section.css";

export type SectionProps = {
  children?: ReactNode;
  backgroundColor?: CSS.Property.BackgroundColor;
};
export function Section({ children, backgroundColor }: SectionProps) {
  return (
    <div
      className={styles.section}
      style={{
        ...assignInlineVars({ [styles.sectionBackgroundColor]: backgroundColor }),
      }}
    >
      {children}
    </div>
  );
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
