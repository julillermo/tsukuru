import { assignInlineVars } from "@vanilla-extract/dynamic";
import type * as CSS from "csstype";
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

  backgroundColor?: CSS.Property.BackgroundColor;
  maxWidth?: `${number}px`;
  alignSelf?: CSS.Property.AlignSelf;
};

export function Button({
  prefix,
  suffix,

  backgroundColor,
  maxWidth,
  alignSelf,
  ...props
}: RACButtonProps & TsukuruButtonProps) {
  return (
    <RACButton
      {...props}
      className={styles.button}
      style={{
        ...assignInlineVars({
          [styles.buttonMaxWidth]: maxWidth,
          [styles.buttonAlignSelf]: alignSelf,
          [styles.buttonBackgroundColor]: backgroundColor,
        }),
      }}
    >
      {composeRenderProps(props.children, (children) => (
        <div className={styles.content}>
          <div>{prefix}</div>
          <div>{children}</div>
          <div>{suffix}</div>
        </div>
      ))}
    </RACButton>
  );
}
