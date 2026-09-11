import { Text as RACText } from "react-aria-components";
import {
  FieldError as RACFieldError,
  Label as RACLabel,
  TextArea as RACTextArea,
  TextField as RACTextField,
  type TextFieldProps as RACTextFieldProps,
  type ValidationResult as RACValidationResult,
} from "react-aria-components/TextField";
import * as styles from "./TextArea.css";

type TsukuruTextAreaProps = {
  label?: string;
  description?: string;
  placeholder?: string;
  errorMessage?: string | ((validation: RACValidationResult) => string);
};

export function TextArea({
  label,
  description,
  placeholder,
  errorMessage,
  ...props
}: RACTextFieldProps & TsukuruTextAreaProps) {
  return (
    <RACTextField className={styles.layout} {...props}>
      {label !== undefined && <RACLabel className={styles.label}>{label}</RACLabel>}
      <RACTextArea className={styles.textArea} placeholder={placeholder} />
      {/* TODO: Eventually update the description to appear as a tool tip (or have an option for it) */}
      {description !== undefined && (
        <RACText slot="description" className={styles.description}>
          {description}
        </RACText>
      )}
      {errorMessage !== undefined && <RACFieldError>{errorMessage}</RACFieldError>}
    </RACTextField>
  );
}
