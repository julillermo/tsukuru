import { createRootRoute, Link, Outlet } from "@tanstack/react-router";
import { TanStackRouterDevtools } from "@tanstack/react-router-devtools";
import { SquareCodeIcon } from "@/icons/lucide";
import { ChipLink } from "@/components/ChipLink";
import * as styles from "./root.css";
import { Divider } from "@/components/base/Divider";
import { PageMissing } from "@/components/pages/PageMissing";

const RootLayout = () => (
  <div className={styles.appLayout}>
    <div className={styles.headerLayout}>
      <div id="navigation" className={styles.navigationLayout}>
        <Link to="/">Tsukuru</Link>
        <Link to="/sentence-practice">Sentence Practice</Link>
        <Link to="/history">History</Link>
        <Link to="/bookmarks">Bookmarks</Link>
        <Link to="/reference">Reference</Link>
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
    <TanStackRouterDevtools />
  </div>
);

export const Route = createRootRoute({
  component: RootLayout,
  notFoundComponent: PageMissing,
});
