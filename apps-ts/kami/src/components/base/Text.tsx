import { Text as RACText, type TextProps as RACTextProps } from "react-aria-components";

export function Text(props: RACTextProps) {
  return <RACText className={props.className}>{props.children}</RACText>;
}
