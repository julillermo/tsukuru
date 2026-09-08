import { style } from "@vanilla-extract/css";

export const button = style({
  borderRadius: 8,
  border: "none",
  backgroundColor: "#9e71c1FF",
  cursor: "pointer",
});

export const content = style({
  display: "flex",
  flexDirection: "row",
  alignItems: "center",

  fontSize: 18,
  color: "white",
  padding: "10px 20px",

  gap: 4,
});
