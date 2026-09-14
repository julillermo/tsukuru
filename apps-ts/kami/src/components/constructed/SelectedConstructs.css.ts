import { style } from "@vanilla-extract/css";

export const selectedConstructsContainer = style({
  display: "flex",
  flex: 1,
  flexDirection: "column",
  gap: 8,
  minHeight: 0,
});

export const selectedConstructsLabel = style({
  fontWeight: 600,
});

export const selectedConstructsDescription = style({
  marginLeft: 4,
  fontSize: 12,
});

export const constructsBox = style({});

export const constructCardContent = style({
  fontSize: 32,
  fontWeight: 800,
});
