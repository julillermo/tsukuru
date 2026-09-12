import {
  ToggleButton as RACToggleButton,
  type ToggleButtonProps as RACToggleButtonProps,
} from "react-aria-components";
import * as styles from "./ToggleButton.css";

type ToggleButtonProps = {
  id: string;
  position: "top" | "bottom" | "left" | "right" | "middle";
};

export function ToggleButton({ position, ...props }: RACToggleButtonProps & ToggleButtonProps) {
  return (
    <RACToggleButton
      id={props.id}
      className={[
        styles.toggleButtonStyle,
        getPositionStyle(position),
        props.isSelected && styles.selected,
      ].join(" ")}
    >
      {props.children}
    </RACToggleButton>
  );
}

function getPositionStyle(position: "top" | "bottom" | "left" | "right" | "middle") {
  switch (position) {
    case "top":
      return styles.positionTop;
    case "bottom":
      return styles.positionMiddle;
    case "left":
      return styles.positionLeft;
    case "right":
      return styles.positionRight;
    case "middle":
      return styles.positionMiddle;
  }
}
