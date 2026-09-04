import { PageUnderConstruction } from "@/components/pages/PageUnderConstruction";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/reference")({
  component: RouteComponent,
});

function RouteComponent() {
  return <PageUnderConstruction />;
}
