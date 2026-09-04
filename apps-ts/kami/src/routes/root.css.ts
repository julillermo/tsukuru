import { style } from "@vanilla-extract/css";

const commonGap = 24;

export const appLayout = style({
  display: "flex",
  gap: 8,
  flexDirection: "column",
  minHeight: "98vh",
});

export const headerLayout = style({
  display: "flex",
  justifyContent: "space-between",
});

export const navigationLayout = style({
  display: "flex",
  gap: commonGap,
  alignItems: "center",
});

export const extrasLayout = style({
  display: "flex",
  gap: commonGap,
  alignItems: "center",
  alignSelf: "flex-end",
});

export const content = style({
  display: "flex",
  flex: 1,
  minHeight: "0",
});
