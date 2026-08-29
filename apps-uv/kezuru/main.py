import argparse
from pathlib import Path

from lang_component.grammar import scrape_grammar
from lang_component.vocab import scrape_vocab
from utils.types import JLPTLevelType


def main():
    args = setup_cli_arguments()

    # ! As of checking on 17 Aug 2026,
    #   only n5 and n4 can be properly scraped for vocab, kanji, and grammar
    # These already cover 1200+ scraped words; n5 (~ 650 words), n4 (~ 630 words)
    # And ~ 90-100 grammar concepts
    jlpt_levels: list[JLPTLevelType] = [
        "n5",
        "n4",
        # "n3", # missing / empty / malformed wiki page
        # "n2", # missing / empty / malformed wiki page
        # "n1", # missing / empty / malformed wiki page
    ]

    scrape_vocab(
        levels=jlpt_levels,
        delay_seconds=5,
        output_dir=Path(args.output_dir),
        saving_strategy=args.saving_strategy,
        pretty_print=args.pretty_print,
    )
    scrape_grammar(
        levels=jlpt_levels,
        delay_seconds=5,
        output_dir=Path(args.output_dir),
        pretty_print=args.pretty_print,
    )

    # TODO CONTINUATION IDEAS:
    # - Continue to scrape N5 & N4 Kanji
    # - Add unit test to test against a known value
    # - Use an API (if available) to check whether the page has been updated
    #       before fetching. If not updated, use the cached html instead.
    # - Have a separate dedicated CLI for check for updates.
    #       Based on the last updates to the page, I don't think it would get
    #       any meaningful update anytime soon.
    # - Host the output in a dedicated repo, potential updates can be
    #       tracked with git diff
    # - Make more use of rich (package) primitives for CLI visuals improvement
    # - Extend the main() to be usable and a CLI tool
    # - Refactor + trim down unused code.
    # - CI/CD integration
    #   - Install "vulture" package to determine dead/unused code
    #   - Install a static analysis tool for vulnerabilities like `gosec`
    # - Address TODO comments, in general


def setup_cli_arguments() -> argparse.Namespace:
    """
    -o, --output_dir
    -ss, --saving-strategy
    -pp, --pretty-print
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default="../../data/",
        help=("Specify output directory\n(default): '../../data/'"),
    )
    parser.add_argument(
        "-ss",
        "--saving-strategy",
        choices=("combined", "individual"),
        default="combined",
        help=(
            "Determines whether to combine or separate outputted vocabulary JSON files.\n"
            "- 'combined' (default) - save same jlpt level vocabulary as one file.\n"
            "- 'individual' - save same jlpt leve as separate files based on first character."
        ),
    )
    parser.add_argument(
        "-pp",
        "--pretty-print",
        default=False,
        action="store_true",
        help="Add flag to apply pretty-printed JSON formatting. Omit to retain as minified.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main()
