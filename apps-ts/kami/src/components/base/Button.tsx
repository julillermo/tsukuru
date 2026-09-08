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
    <RACButton {...props} className={styles.button}>
      {composeRenderProps(props.children, (children) => (
        <div className={styles.content}>
          <div>{props.prefix}</div>
          <div>{children}</div>
          <div>{props.suffix}</div>
        </div>
      ))}
    </RACButton>
  );
}
