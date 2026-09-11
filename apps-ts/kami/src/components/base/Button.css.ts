import { createVar, fallbackVar, style } from "@vanilla-extract/css";

export const buttonBackgroundColor = createVar();
export const buttonMaxWidth = createVar();
export const buttonAlignSelf = createVar();
export const button = style({
  borderRadius: 8,
  border: "none",
  cursor: "pointer",

  alignSelf: fallbackVar(buttonAlignSelf, "flex-end"),
  maxWidth: fallbackVar(buttonMaxWidth, "fit-content"),
  backgroundColor: fallbackVar(buttonBackgroundColor, "#9e71c1FF"),
});

export const content = style({
  display: "flex",
  flexDirection: "row",
  alignItems: "center",

  fontSize: 18,
  color: "white",
  padding: "10px 20px",

  gap: 4,
});
