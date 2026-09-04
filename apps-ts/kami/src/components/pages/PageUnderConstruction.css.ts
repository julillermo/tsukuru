import { style } from "@vanilla-extract/css";

// TODO: Styles between the default pages can be generalized and shared
export const layout = style({
  display: "flex",
  flex: 1,
  alignItems: "center",
  justifyContent: "center",
});

export const imageContainer = style({
  display: "flex",
  flexGrow: 2,
  justifyContent: "center",
  maxWidth: 1000,
});

export const textGroup = style({
  display: "flex",
  flexGrow: 1,
  flexDirection: "column",
  gap: 36,
  fontSize: 24,
  borderLeft: "2px solid rgba(45, 45, 45, 0.65)",
  padding: "24px 0px 24px 42px",
});
export const titleGroup = style({
  display: "flex",
  flexDirection: "column",
  fontWeight: 800,
  fontSize: 48,
});

export const title = style({
  color: "#9052c1",
  fontWeight: 800,
  fontSize: 48,
});

export const subtitle = style({
  fontWeight: 600,
  fontSize: 36,
});

export const bodyGroup = style({
  display: "flex",
  flexDirection: "column",
  gap: 18,
});
