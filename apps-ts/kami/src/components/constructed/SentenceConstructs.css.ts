import { style } from "@vanilla-extract/css";

export const sentenceConstructs = style({
  display: "flex",
  flex: 1,
  minWidth: 0,
  minHeight: "100%",
  flexDirection: "column",
  gap: 16,

  padding: 2, // Prevents outlines from being clipped when scrollbar present
  overflowY: "auto",
});

export const constructCardHeader = style({
  display: "flex",
  flexDirection: "row",
  gap: 16,
  alignItems: "center",

  fontSize: 32,
});

export const constructCardJLPTLevel = style({
  fontSize: 24,
});

export const exampleSentenceList = style({
  display: "flex",
  flexDirection: "column",
  gap: 16,
  marginLeft: 8,
});

export const exampleSentence = style({
  display: "flex",
  flexDirection: "column",
  gap: 8,
});

export const exampleSentenceBulletRow = style({
  display: "flex",
  flexDirection: "row",
  alignItems: "center",
  gap: 8,
});

export const exampleSentenceJapaneseText = style({
  fontWeight: 600,
});

export const exampleSentenceEnglishMeaning = style({
  marginLeft: 24,
});
