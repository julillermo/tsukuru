import type * as CSS from "csstype";
import { ChevronRightIcon } from "lucide-react";
import { useState, type ReactNode } from "react";
import {
  Button as RACBUtton,
  Disclosure as RACDisclosure,
  DisclosurePanel as RACDisclosurePanel,
  Heading as RACHeading,
  type DisclosurePanelProps as RACDisclosurePanelProps,
  type DisclosureProps as RACDisclosureProps,
  type HeadingProps as RACHeadingProps,
} from "react-aria-components/Disclosure";
import * as styles from "./Disclosure.css";

type TsukuruDisclosureProps = {
  buttonIcon?: ReactNode;
  heading: ReactNode;
  headingStyle?: CSS.Properties;
  content: ReactNode;
  contentStyle?: CSS.Properties;
};

export function Disclosure({
  buttonIcon,
  headingStyle,
  ...props
}: RACDisclosureProps & TsukuruDisclosureProps) {
  let [isExpanded, setIsExpanded] = useState(
    props.defaultExpanded != undefined ? props.defaultExpanded : true,
  );

  const toggleExapnd = () => {
    setIsExpanded(!isExpanded);
  };

  return (
    <RACDisclosure isExpanded={isExpanded} {...props} className={styles.disclosure}>
      <DisclosureHeader
        buttonIcon={buttonIcon}
        customStyle={headingStyle}
        isExpanded={isExpanded}
        onExpand={toggleExapnd}
      >
        {props.heading}
      </DisclosureHeader>
      <DisclosurePanel customStyle={props.contentStyle}>{props.content}</DisclosurePanel>
    </RACDisclosure>
  );
}

type TsukuruDisclosureHeaderProps = {
  buttonIcon?: ReactNode;
  isExpanded?: boolean;
  onExpand?: () => void;
  customStyle?: CSS.Properties;
};
export function DisclosureHeader({
  buttonIcon,
  isExpanded,
  onExpand,
  customStyle,
  ...props
}: RACHeadingProps & TsukuruDisclosureHeaderProps) {
  return (
    <RACHeading {...props} className={styles.heading}>
      <RACBUtton slot="trigger" onClick={onExpand} className={styles.expandButton}>
        {buttonIcon ? (
          <div className={isExpanded ? styles.chevronOpen : undefined}>{buttonIcon}</div>
        ) : (
          <ChevronRightIcon className={isExpanded ? styles.chevronOpen : undefined} />
        )}
      </RACBUtton>
      <span style={customStyle}>{props.children}</span>
    </RACHeading>
  );
}

type TsukuruDisclosurePanelProps = {
  customStyle?: CSS.Properties;
};
export function DisclosurePanel(props: RACDisclosurePanelProps & TsukuruDisclosurePanelProps) {
  return (
    <RACDisclosurePanel {...props} className={styles.panel} style={props.customStyle}>
      <div>{props.children}</div>
    </RACDisclosurePanel>
  );
}
