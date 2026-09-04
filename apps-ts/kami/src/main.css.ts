import { globalStyle } from "@vanilla-extract/css";

// #d4e6c6
// #c6e4e6
// #763ba5 purple 1
// #9e71c1 purple 2
// #e6c8c6

globalStyle("html, body, #root", {
  fontFamily: "Noto Sans, Helvetica, Arial, sans-serif",
  lineHeight: 1.5,
  fontWeight: 400,
  fontSize: 18,
  colorScheme: "light dark",
  color: "rgba(45, 45, 45, 0.85)",
  // color: "coral",
  backgroundColor: "#d4e6c6",
  textRendering: "optimizeLegibility",
});

globalStyle("a", {
  fontWeight: 500,
  color: "#763ba5",
  textDecoration: "inherit",
});

globalStyle("a:hover", {
  fontWeight: 500,
  color: "#a86bd8",
  textDecoration: "inherit",
});

// TODO: Pickup these globalStyle concepts if necessary later on
// globalStyle("body", {
//   margin: 8,
//   display: "flex",
//   placeItems: "center",
//   minWidth: "320px",
//   minHeight: "100vh",
// });

// globalStyle("h1", {
//   fontSize: "3.2em",
//   lineHeight: 1.1,
// });

// globalStyle("button", {
//   borderRadius: "8px",
//   border: "1px solid transparent",
//   padding: "0.6em 1.2em",
//   fontSize: "1em",
//   fontWeight: 500,
//   fontFamily: "inherit",
//   background: "linear-gradient(135deg, #6366f1, #8b5cf6)",
//   color: "#fff",
//   cursor: "pointer",
//   transition: "border-color 0.25s",
//   "@media": {
//     "(prefers-color-scheme: light)": {
//       backgroundColor: "#f9f9f9",
//     },
//   },
// });

// globalStyle("button:hover", {
//   borderColor: "#646cff",
// });

// globalStyle("button:focus, button:focus-visible", {
//   outline: "4px auto -webkit-focus-ring-color",
// });
