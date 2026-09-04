import type { ReactNode } from "react";
import {
  Button as RACButton,
  type ButtonProps as RACButtonProps,
} from "react-aria-components/Button";
import { composeRenderProps } from "react-aria-components/composeRenderProps";
import * as styles from "./Button.css";

type TsukuruButtonProps = {
  prefix?: ReactNode;
  suffix?: ReactNode;
};

export function Button(props: RACButtonProps & TsukuruButtonProps) {
  return (
    <RACButton {...props}>
      {composeRenderProps(props.children, (children) => (
        <div className={styles.layout}>
          {props.prefix}
          {children}
          {props.suffix}
        </div>
      ))}
    </RACButton>
  );
}
