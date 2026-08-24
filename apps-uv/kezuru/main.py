from lang_component.grammar import scrape_grammar
from lang_component.vocab import scrape_vocab
from utils.types import JLPTLevelType


def main():
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

    scrape_vocab(levels=jlpt_levels, delay_seconds=5)
    scrape_grammar(levels=jlpt_levels, delay_seconds=5)

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


if __name__ == "__main__":
    main()
