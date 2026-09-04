import type { ReactNode } from "react";
import * as styles from "./ChipLink.css";
import { Link as RACLink, type LinkProps } from "react-aria-components/Link";

type ChipLinkProps = {
  suffix?: ReactNode;
};

// TODO: add a chip-style outline to this for emphasis
export function ChipLink(props: LinkProps & ChipLinkProps) {
  return (
    <>
      <RACLink
        href="https://github.com/julillermo/tsukuru"
        target="_blank"
        referrerPolicy="no-referrer"
        className={styles.layout}
      >
        <>
          {props.children}
          {props.suffix}
        </>
      </RACLink>
    </>
  );
}
