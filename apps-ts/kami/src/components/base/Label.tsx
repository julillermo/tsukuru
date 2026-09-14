import { Label as RACLabel, type LabelProps as RACLabelProps } from "react-aria-components";

export function Label(props: RACLabelProps) {
  return <RACLabel className={props.className}>{props.children}</RACLabel>;
}
