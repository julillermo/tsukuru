import { style } from "@vanilla-extract/css";

export const layout = style({
  display: "flex",
  flex: 1,
  flexDirection: "row",

  margin: 16,
  justifyContent: "center",
  gap: 24,
});

export const sentenceCreationSection = style({
  display: "flex",
  flexDirection: "column",
  flex: 1,
  flexGrow: 4,
  gap: 16,
});

export const sentenceInputGroup = style({
  display: "flex",
  flexDirection: "column",
  marginTop: "auto",
  marginBottom: 8,
});

export const sentenceConstructsBox = style({
  display: "flex",
  flex: 3,
});
