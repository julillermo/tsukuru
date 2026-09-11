import { Divider } from "@/components/base/Divider";
import { ChipLink } from "@/components/constructed/ChipLink";
import { PageMissing } from "@/components/pages/PageMissing";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";
import { createRootRoute, Link, Outlet } from "@tanstack/react-router";
import { TanStackRouterDevtools } from "@tanstack/react-router-devtools";
import { SquareCodeIcon } from "lucide-react";
import * as styles from "./-root.css";

const queryClient = new QueryClient({
  // defaultOptions: {
  //   // Adjust accordingly
  //   queries: {
  //     staleTime: 5 * 60 * 1000,
  //     refetchInterval: 30 * 60 * 1000,
  //     gcTime: 60 * 60 * 1000, // By default, "inactive" queries are garbage collected after 5 minutes.
  //   },
  // },
});

const RootLayout = () => (
  <QueryClientProvider client={queryClient}>
    <div className={styles.appLayout}>
      <div className={styles.headerLayout}>
        <div id="navigation" className={styles.navigationLayout}>
          <Link to="/">Tsukuru</Link>
          <Link to="/sentence-practice">Sentence Practice</Link>
          {/*<Link to="/history">History</Link>*/}
          {/*<Link to="/bookmarks">Bookmarks</Link>*/}
          {/*<Link to="/reference">Reference</Link>*/}
        </div>
        <div id="extras" className={styles.extrasLayout}>
          <Link to="/about">About</Link>
          <Link to="/attribution">Attribution</Link>{" "}
          <ChipLink suffix={<SquareCodeIcon />}>Source Code</ChipLink>
        </div>
      </div>
      <Divider />
      <main className={styles.content}>
        <Outlet />
      </main>
    </div>
    <TanStackRouterDevtools />
    <ReactQueryDevtools />
  </QueryClientProvider>
);

export const Route = createRootRoute({
  component: RootLayout,
  notFoundComponent: PageMissing,
});
