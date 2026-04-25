import json
import time
from datetime import datetime
from typing import cast

import requests
from bs4 import BeautifulSoup as bSoup
from utils.types import CJKGyouGroup, JLPTComponent, JLPTLevel
from utils.vocab import filter_from_page_element_list

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
        - level -> JLPT level to scrape vocab for.
        - vocab_file_path [optional] -> Path to cached vocab HTML file.
            If `None`, fetches from the internet.
            If provided, the file will be loaded and used instead of making a new request.
        - delay [optional] -> Seconds to wait after request. `None` = no sleep.
    """

    if vocab_file_path is not None:
        print(
            "Loading Wikipedia JLPT Guide from latest cached vocab file:",
            vocab_file_path,
        )

        with open(vocab_file_path, mode="r", encoding="utf-8") as file:
            vocab_page = file.read()

    else:
        url = TARGET_JLPT_GUIDE_URLS["n5"]["vocab"]
        print(f"Fetching Wikipedia JLPT Guide from the internet: {url}")

        vocab_page = requests.get(url=url, headers=SCRAPER_HEADER).content

    vocab_soup = bSoup(vocab_page, "html.parser")

    current_time = datetime.now()
    current_time_string = current_time.strftime("%Y-%m-%dT%H:%M:%S")

    if vocab_file_path is None:
        with open(
            f"./.cache/{level}/vocab/html-page-{current_time_string}.html",
            mode="w",
            encoding="utf-8",
        ) as file:
            file.write(str(vocab_soup.prettify()))

    wiki_content = vocab_soup.find("div", class_="mw-content-ltr")
    if wiki_content is None:
        print("Error: Could not find wiki content in the page.")
        return

    gyou_ul_element = wiki_content.find(name="ul", recursive=False)
    if gyou_ul_element is None:
        print("Error: Could not find wiki content in the page.")
        return

    gyou_list = filter_from_page_element_list(
        listVar=gyou_ul_element.contents, pattern="\n"
    )

    gyou_links_dict: dict[CJKGyouGroup, str] = {}
    for gyou_element in gyou_list:
        a_tag = gyou_element.find_next("a")
        if a_tag is not None and a_tag["href"] is not None and a_tag.string is not None:
            romanji_casted_a_tag_string = cast(CJKGyouGroup, a_tag.string.strip())
            gyou_links_dict[romanji_casted_a_tag_string] = "https:" + str(a_tag["href"])

    if vocab_file_path is None:
        with open(
            f"./.cache/{level}/vocab/gyou-link{current_time_string}.json",
            mode="w",
            encoding="utf-8",
        ) as file:
            file.write(json.dumps(obj=gyou_links_dict, ensure_ascii=False))

    # Delay between requests to avoid overwhelming the server
    if delay is not None:
        time.sleep(delay)
