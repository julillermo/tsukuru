import { style, createVar, fallbackVar } from "@vanilla-extract/css";

export const section = style({
  display: "flex",
  flex: 1,
  minHeight: 0,
  minWidth: 0,
  flexDirection: "column",
  backgroundColor: "#E4C9C6",
  borderRadius: 8,
  padding: 18,

  gap: 12,

  maxWidth: 715, // TODO: Eventually remove this when the proper sizing has been determined
});

export const subSectionHeight = createVar();
export const subsection = style({
  display: "flex",
  flexDirection: "row",
  justifyContent: "space-between",
  height: fallbackVar(subSectionHeight, "auto"),
});
