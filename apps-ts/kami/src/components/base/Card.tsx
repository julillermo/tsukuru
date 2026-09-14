import { assignInlineVars } from "@vanilla-extract/dynamic";
import type * as CSS from "csstype";
import type { ReactNode } from "react";
import * as styles from "./Card.css";

export type CardProps = {
  children: ReactNode;
  backgroundColor?: CSS.Property.BackgroundColor;
  outlineWidth?: CSS.Property.OutlineWidth;
  outlineStyle?: CSS.Property.OutlineStyle;
  outlineColor?: CSS.Property.OutlineColor;
  boxShadow?: CSS.Property.BoxShadow;
};
export function Card(props: CardProps) {
  return (
    <div
      className={styles.card}
      style={assignInlineVars({
        [styles.cardBackgroundColor]: props.backgroundColor,
        [styles.cardOutlineWidth]: String(props.outlineWidth),
        [styles.cardOutlineColor]: props.outlineColor,
        [styles.cardOutlineStyle]: props.outlineStyle,
        [styles.cardBoxShadow]: props.boxShadow,
      })}
    >
      {props.children}
    </div>
  );
}
