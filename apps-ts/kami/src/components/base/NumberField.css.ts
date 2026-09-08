import { style } from "@vanilla-extract/css";

export const numberField = style({
  display: "flex",
  gap: 8,
  alignItems: "center",
});

export const label = style({});

export const inputGroup = style({
  display: "flex",
  flexDirection: "row",
});

export const input = style({
  background: "#ffdddb",
  borderRadius: "8px 0px 0px 8px",
  border: "none",
  width: "100%",
  textAlign: "center",

  fontSize: 18,

  ":focus": {
    outline: "none",
  },
});

export const buttonGroup = style({
  display: "flex",
  flexDirection: "column",

  background: "#ffdddb",
  borderRadius: "0px 8px 8px 0px",
});

export const button = style({
  display: "flex",
  flex: 1,
  appearance: "none",

  margin: 0,
  padding: 0,

  border: 0,
  background: "none",

  cursor: "pointer",
  color: "inherit",

  ":disabled": {
    color: "lightgray",
  },
});

export const chevronIcon = style({
  aspectRatio: 1,
  height: 16,
});
