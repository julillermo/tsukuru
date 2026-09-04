import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/folder/file")({
  component: RouteComponent,
});

function RouteComponent() {
  return <div>Hello "/folder/file"!</div>;
}
