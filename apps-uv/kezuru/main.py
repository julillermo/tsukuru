from lang_component.vocab import scrape_vocab
from utils.types import JLPTLevelType


def main():
    # ! As of checking on 17 Aug 2026, only n5 and n4 can be properly scraped for vocab
    # Note however these already cover 1200+ scraped words
    #   n5 ~ 650 words
    #   n4 ~ 630 words
    jlpt_levels: list[JLPTLevelType] = [
        "n5",
        "n4",
        # "n3", # missing / empty / malformed wiki page
        # "n2", # missing / empty / malformed wiki page
        # "n1", # missing / empty / malformed wiki page
    ]

    scrape_vocab(levels=jlpt_levels, delay_seconds=5)

    # CONTINUATION:
    # - Continue to scrape N5 & N4 Kanji
    # - Continue to scrape N5, N4, N3 Grammar
    # - Use an API (if available) to check whether the page has been updated
    #       before fetching. If not updated, use the cached html instead.
    # - Have a separate dedicated CLI for check for updates.
    #       Based on the last updates to the page, I don't think it would get
    #       any meaningful update anytime soon.
    # - Host the output in a dedicated repo, potential updates can be
    #       tracked with git diff
    # - Make use of rich (package) primitives for CLI visuals improvement
    # - Extend the main() to be usable and a CLI tool
    # - Refactor + trim down unused code.
    # - CI/CD integration
    # - Address TODO comments


if __name__ == "__main__":
    main()
