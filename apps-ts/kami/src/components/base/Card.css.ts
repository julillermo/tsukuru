import { createVar, fallbackVar, style } from "@vanilla-extract/css";

export const cardBackgroundColor = createVar();
export const cardOutlineColor = createVar();
export const cardOutlineStyle = createVar();
export const cardOutlineWidth = createVar();
export const cardBoxShadow = createVar();

export const card = style({
  display: "flex",
  flexDirection: "column",
  gap: 8,
  borderRadius: 8,
  padding: 8,
  margin: 2,
  height: "fit-content",

  backgroundColor: cardBackgroundColor,
  outlineStyle: fallbackVar(cardOutlineStyle, "solid"),
  outlineColor: fallbackVar(cardOutlineColor, "inherit"),
  outlineWidth: fallbackVar(cardOutlineWidth, "2px"),
  boxShadow: fallbackVar(cardBoxShadow, "none"),
});
