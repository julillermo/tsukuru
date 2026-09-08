import { createVar, style } from "@vanilla-extract/css";

export const cardBackgroundColor = createVar();
export const cardOutlineColor = createVar();
export const card = style({
  display: "flex",
  flexDirection: "column",
  gap: 8,
  borderRadius: 8,
  padding: 8,
  backgroundColor: cardBackgroundColor,
  outline: `2px dashed ${cardOutlineColor}`,
});
