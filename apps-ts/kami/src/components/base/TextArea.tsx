import {
  Label as RACLabel,
  TextField as RACTextField,
  TextArea as RACTextArea,
  type TextFieldProps as RACTextFieldProps,
} from "react-aria-components";

type TsukuruTextAreaProps = {};

// TODO: Customization for this was left unfinished
export function TextArea(props: RACTextFieldProps & TsukuruTextAreaProps) {
  return (
    <RACTextField {...props}>
      <RACLabel></RACLabel>
      <RACTextArea placeholder={"text"} />
    </RACTextField>
  );
}
