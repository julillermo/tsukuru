import { PageUnderConstruction } from "@/components/pages/PageUnderConstruction";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/bookmarks")({
  component: RouteComponent,
});

function RouteComponent() {
  return <PageUnderConstruction />;
}
