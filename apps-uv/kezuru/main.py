import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup as bSoup
from custom_types import JLPTComponent, JLPTLevel
from utils import get_path_of_latest_file

WIKI_JLPT_GUIDE_URL = "https://en.wikibooks.org/wiki/JLPT_Guide"


TARGET_JLPT_GUIDE_URLS: dict[JLPTLevel, dict[JLPTComponent, str]] = {
    "n5": {
        "vocab": WIKI_JLPT_GUIDE_URL + "/JLPT_N5_Vocabulary",
        "kanji": WIKI_JLPT_GUIDE_URL + "/N5_KANJI_URL_PATH",
        "grammar": WIKI_JLPT_GUIDE_URL + "/JLPT_N5_Grammar",
    }
}

OUTPUT_PATHS: dict[JLPTLevel, dict[JLPTComponent, str]] = {
    "n5": {
        "vocab": "./data/n5_vocab.json",
        "kanji": "./data/n5_kanji.json",
        "grammar": "./data/n5_grammar.json",
    }
}

SCRAPER_HEADER = {
    "user-agent": "TsukuruKezuruScraper/1.0 (contact: https://github.com/julillermo)",
    "from": "https://github.com/julillermo/tsukuru",
}


def scrape_vocab(
    level: JLPTLevel, vocab_file_path: str | None = None, delay: int | None = None
):
    """
    Scrape specified Wikipedia JLPT Guide Vocab by level

    Args:
        delay: Seconds to wait after request. `None` = no sleep.
    """

    if vocab_file_path is not None:
        print(
            "Loading Wikipedia JLPT Guide from latest cached vocab file:",
            vocab_file_path,
        )

        with open(vocab_file_path, mode="r", encoding="utf-8") as file:
            vocab_page = file.read()

    else:
        print("Fetching Wikipedia JLPT Guide from the internet:")

        url = TARGET_JLPT_GUIDE_URLS["n5"]["vocab"]
        vocab_page = requests.get(url=url, headers=SCRAPER_HEADER).content

    vocab_soup = bSoup(vocab_page, "html.parser")

    current_time = datetime.now()
    current_time_string = current_time.strftime("%Y-%m-%dT%H:%M:%S")

    if vocab_file_path is None:
        with open(
            f"./.cache/{level}/vocab/{current_time_string}.html",
            mode="w",
            encoding="utf-8",
        ) as file:
            file.write(str(vocab_soup.prettify()))

    # Delay between requests to avoid overwhelming the server
    if delay is not None:
        time.sleep(delay)


def main():
    print("Hello from kezuru!\n")

    # optoinal for testing
    vocab_file_path = get_path_of_latest_file("./.cache/n5/vocab")

    jlpt_level: JLPTLevel = "n5"

    scrape_vocab(vocab_file_path=vocab_file_path, level=jlpt_level, delay=1)


if __name__ == "__main__":
    main()
