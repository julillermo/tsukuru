import {
  composeRenderProps,
  ToggleButtonGroup as RACToggleButtonGroup,
  SelectionIndicator,
  type ToggleButtonGroupProps as RACToggleButtonGroupProps,
} from "react-aria-components";

import * as styles from "./ToggleButtonGroup.css";

export function ToggleButtonGroup(props: RACToggleButtonGroupProps) {
  return (
    <RACToggleButtonGroup {...props} className={styles.buttonGroup}>
      {composeRenderProps(props.children, (children) => (
        <>
          {/* SelctionIndicate is like a cursor to indicate selection, but requires styling
              It's an optional use set for ToggleButtonProps

              Instead of using SelectionIndicator, you can just style each ToggleButton with CSS
            */}
          <SelectionIndicator data-selected />
          <span>{children}</span>
        </>
      ))}
    </RACToggleButtonGroup>
  );
}
