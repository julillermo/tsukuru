import {
  Button,
  FieldError,
  Group,
  Input,
  Label,
  NumberField as RACNumberField,
  Text,
  type NumberFieldProps as RACNumberFieldProps,
} from "react-aria-components/NumberField";
import { ChevronUpIcon, ChevronDownIcon } from "lucide-react";
import * as styles from "./NumberField.css";

type TsukuruNumberFieldProps = {
  label: string;
};

export function NumberField(props: RACNumberFieldProps & TsukuruNumberFieldProps) {
  return (
    <RACNumberField {...props} className={styles.numberField}>
      <Label>{props.label}</Label>
      <Group className={styles.inputGroup}>
        <Input className={styles.input} />
        <Group className={styles.buttonGroup}>
          <Button slot="increment" className={styles.button}>
            <ChevronUpIcon className={styles.chevronIcon} />
          </Button>
          <Button slot="decrement" className={styles.button}>
            <ChevronDownIcon className={styles.chevronIcon} />
          </Button>
        </Group>
      </Group>
      <Text slot="description" />
      <FieldError />
    </RACNumberField>
  );
}
