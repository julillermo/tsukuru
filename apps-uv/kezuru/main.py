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
        delay_seconds=args.delay_seconds,
        output_dir=Path(args.output_dir),
        saving_strategy=args.saving_strategy,
        pretty_print=args.pretty_print,
        ignore_cache=args.ignore_cache,
    )
    scrape_grammar(
        levels=jlpt_levels,
        delay_seconds=args.delay_seconds,
        output_dir=Path(args.output_dir),
        pretty_print=args.pretty_print,
        ignore_cache=args.ignore_cache,
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
    # - Have a CLI flag downloading the latest available verison off of github
    #       instead of generating the JLPT data.
    # - Extend the main() to have an optional interactive TUI
    # - Make more use of rich (package) primitives for CLI visuals improvement
    # - Refactor + trim down unused code.
    # - CI/CD integration
    #   - Install "vulture" package to determine dead/unused code
    #   - Install a static analysis tool for vulnerabilities like `gosec`
    # - Address TODO comments, in general


def setup_cli_arguments() -> argparse.Namespace:
    """
    -o, --output-dir
    -ss, --saving-strategy
    -pp, --pretty-print
    -ds, --delay-seconds
    -ic, --ignore-cache
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
        "-ds",
        "--delay-seconds",
        default=5,
        type=int,
        help=("Set waiting time (in seconds) between each scrape.\n(default): 5"),
    )
    parser.add_argument(
        "-pp",
        "--pretty-print",
        default=False,
        action="store_true",
        help="Add flag to apply pretty-printed JSON formatting. Omit to retain as minified.",
    )
    parser.add_argument(
        "-ic",
        "--ignore-cache",
        default=False,
        action="store_true",
        help="Add flag to ignore existing web page cache. Omit to retain read from cache if available.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main()
