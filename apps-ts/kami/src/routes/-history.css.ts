import { style } from "@vanilla-extract/css";

export const layout = style({
  display: "flex",
  flexDirection: "column",
  flex: 1,

  marginBottom: 10,

  width: "100%",
  overflow: "auto",
});

export const sentencesContainer = style({
  display: "flex",
  flexDirection: "column",
  alignSelf: "center",

  width: 900,
  gap: 24,
});

export const constructCardHeaderContent = style({
  display: "flex",
  flexDirection: "row",
  gap: 16,
  alignItems: "center",
  fontSize: 32,
  fontWeight: 800,
});
