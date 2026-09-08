import { assignInlineVars } from "@vanilla-extract/dynamic";
import type * as CSS from "csstype";
import type { ReactNode } from "react";
import * as styles from "./Card.css";

export type CardProps = {
  children: ReactNode;
  backgroundColor?: CSS.Property.BackgroundColor;
  outlineColor?: CSS.Property.OutlineColor;
};
export function Card(props: CardProps) {
  return (
    <div
      className={styles.card}
      style={assignInlineVars({
        [styles.cardBackgroundColor]: props.backgroundColor,
        [styles.cardOutlineColor]: props.outlineColor,
      })}
    >
      {props.children}
    </div>
  );
}
