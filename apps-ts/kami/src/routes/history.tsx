import { PageUnderConstruction } from "@/components/pages/PageUnderConstruction";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/history")({
  component: RouteComponent,
});

function RouteComponent() {
  return <PageUnderConstruction />;
}
