import { style } from "@vanilla-extract/css";

export const layout = style({
  display: "flex",
  flexDirection: "column",
  flex: 1,

  gap: 4,
});

export const label = style({
  fontWeight: 600,
});

export const textArea = style({
  fontSize: 28,
  color: "inherit",
  padding: 8,

  height: "8em",
  resize: "none",
  borderRadius: 8,
  backgroundColor: "#c6e4e6",
  border: "1px solid #94abad",

  ":focus": {
    outline: "2px solid #94abad",
  },
});

export const description = style({
  marginLeft: 4,
  fontSize: 12,
});
