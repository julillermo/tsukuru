import { createVar, fallbackVar, style } from "@vanilla-extract/css";

export const sectionBackgroundColor = createVar();
export const section = style({
  display: "flex",
  flex: 1,
  minHeight: 0,
  minWidth: 0,
  flexDirection: "column",
  backgroundColor: fallbackVar(sectionBackgroundColor, "#E4C9C6"),
  borderRadius: 8,
  padding: 18,

  gap: 12,
});

export const subSectionHeight = createVar();
export const subsection = style({
  display: "flex",
  flexDirection: "row",
  justifyContent: "space-between",
  height: fallbackVar(subSectionHeight, "auto"),
});
