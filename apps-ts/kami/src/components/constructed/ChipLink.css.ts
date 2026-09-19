import { style } from "@vanilla-extract/css";

export const layout = style({
  display: "flex",
  alignItems: "center",
  gap: 4,

  outline: "2px solid #763ba5",
  borderRadius: 8,
  padding: "4px  8px",

  ":hover": {
    outline: "2px solid #a86bd8",
  },
});
