import { StrictMode } from "react";
import ReactDOM from "react-dom/client";
import { RouterProvider, createRouter } from "@tanstack/react-router";
import "./main.css.ts";

// Import the generated route tree
import { routeTree } from "./routeTree.gen.ts";

// Create a new router instance
const router = createRouter({ routeTree });

// Register the router instance for type safety
declare module "@tanstack/react-router" {
  interface Register {
    router: typeof router;
  }
}

// Render the app
const rootElement = document.getElementById("root")!;
if (!rootElement.innerHTML) {
  const root = ReactDOM.createRoot(rootElement);
  root.render(
    <StrictMode>
      <RouterProvider router={router} />
    </StrictMode>,
  );
}

// TODO CONTINUATION:
// - Copy previous projects for vite CI/CD deployment to github
// - Add light/dark mode toggle
// - Better handle theming.
//    - Currently colors are hardcoded into the styling
//    - More generalized selections for font sizes
// - Move the components as part of their own UI/Components monorepo sub-application
// - Copy over the accent() utility function for colors from Learning-React
