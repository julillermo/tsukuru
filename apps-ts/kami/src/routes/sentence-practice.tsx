import { PageUnderConstruction } from "@/components/pages/PageUnderConstruction";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/sentence-practice")({
  component: RouteComponent,
});

function RouteComponent() {
  return <PageUnderConstruction />;
}
