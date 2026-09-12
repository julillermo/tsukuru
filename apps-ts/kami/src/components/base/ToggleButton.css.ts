import { style } from "@vanilla-extract/css";

export const toggleButtonStyle = style({
  border: "none",
  cursor: "pointer",
  padding: "10px 20px",

  backgroundColor: "#e68e8a",
  color: "white",
  fontSize: 18,
});

export const selected = style({
  backgroundColor: "#c97c78",
  boxShadow: "inset 4px 4px 8px rgba(0, 0, 0, 0.15)",
});

export const positionTop = style({
  borderRadius: "8px 8px 0px 0px",
});
export const positionBottom = style({
  borderRadius: "0px 0px 8px 8px",
});
export const positionLeft = style({
  borderRadius: "8px 0px 0px 8px",
});
export const positionRight = style({
  borderRadius: "0px 8px 8px 0px",
});
export const positionMiddle = style({
  borderRadius: "0px 0px 0px 0px",
});
