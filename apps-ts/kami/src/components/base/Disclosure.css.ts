import { style } from "@vanilla-extract/css";

export const disclosure = style({
  display: "flex",
  flexDirection: "column",
  gap: 8,
});

export const heading = style({
  display: "flex",
  flex: 1,
  flexDirection: "row",
  alignItems: "center",
  margin: 0,
  padding: 0,
  fontSize: 32,
  fontWeight: 800,
});

export const expandButton = style({
  border: 0,
  background: "transparent",
  color: "inherit",
  cursor: "pointer",
});

export const panel = style({
  marginLeft: 24,
});

export const chevronOpen = style({
  transform: "rotate(90deg)",
  color: "inherit",
});
