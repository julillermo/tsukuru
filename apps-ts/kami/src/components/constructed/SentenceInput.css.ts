import { style } from "@vanilla-extract/css";

export const sentenceInputContainer = style({
  display: "flex",
  flexDirection: "column",
});

export const sentenceInput = style({
  display: "flex",
  flexDirection: "row",
  gap: 24,
  marginBottom: 8,
});
