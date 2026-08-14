import json
import sys
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import cast

import requests
from bs4 import BeautifulSoup as bSoup
from bs4.element import Tag
from utils.file import debug_save_text_to_file, save_text_to_file
from utils.type_guard import isNull
from utils.types import (
    CJKGyouGroupType,
    CJKGyouOrMiscType,
    JLPTComponentType,
    JLPTLevelType,
    VocabEntry,
)
from utils.vocab import filter_from_page_element_list

WIKI_BOOKS_ROOT_URL = "https://en.wikibooks.org"
WIKI_JLPT_GUIDE_BASE_URL = f"{WIKI_BOOKS_ROOT_URL}/wiki/JLPT_Guide"
TARGET_RESOURCE_PATH: dict[JLPTLevelType, dict[JLPTComponentType, str]] = {
    "n5": {
        "vocab": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N5_Vocabulary",
        "kanji": WIKI_JLPT_GUIDE_BASE_URL + "/N5_KANJI_URL_PATH",
        "grammar": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N5_Grammar",
    }
}
OUTPUT_PATHS: dict[JLPTLevelType, dict[JLPTComponentType, str]] = {
    "n5": {
        "vocab": "./data/n5_vocab.json",
        "kanji": "./data/n5_kanji.json",
        "grammar": "./data/n5_grammar.json",
    }
}
SCRAPER_HEADER = {
    "user-agent": "TsukuruKezuruScraper/1.0 (contact: tuliog.projects@gmail.com)",
    "from": "https://github.com/julillermo/tsukuru",
}


def scrape_vocab(
    level: JLPTLevelType,
    vocab_file_path: str | None = None,
    delay_seconds: int | None = None,
) -> None:
    """
    Scrape specified Wikipedia JLPT Guide Vocab by level

    Args:
        - `level` -> JLPT level to scrape vocab for.
        - `vocab_file_path` [optional] -> Path to cached vocab HTML file.
            If `None`, fetches from the internet.
            If provided, the file will be loaded and used instead of making a new request.
        - `delay_seconds` [optional] -> Seconds to wait after request. `None` = no sleep.
    """

    if not isNull(vocab_file_path):
        print(
            "Loading Wikipedia JLPT Guide from latest cached vocab file:",
            vocab_file_path,
        )
        with open(vocab_file_path, mode="r", encoding="utf-8") as file:
            vocab_page = file.read()
    else:
        url = TARGET_RESOURCE_PATH["n5"]["vocab"]
        print(f"Fetching Wikipedia JLPT Guide from the internet: {url}")

        vocab_page = requests.get(url=url, headers=SCRAPER_HEADER).content

    vocab_soup = bSoup(vocab_page, "html.parser")

    current_time = datetime.now(UTC)
    current_time_string = current_time.strftime("%Y-%m-%dT%H:%M:%S")

    if vocab_file_path is None:
        save_text_to_file(
            dir=Path(f"./.cache/{level}/vocab"),
            filename=f"html-page-{current_time_string}.html",
            contents=str(vocab_soup.prettify()),
        )

    wiki_content = vocab_soup.find("div", class_="mw-content-ltr")
    if isNull(wiki_content):
        raise ValueError("Error: Could not find wiki content in the page.")

    gyou_ul_element = wiki_content.find(name="ul", recursive=False)
    if isNull(gyou_ul_element):
        raise ValueError("Error: Could not find wiki content in the page.")

    gyou_list = filter_from_page_element_list(
        list_var=gyou_ul_element.contents, pattern="\n"
    )

    # The following doesn't pick up words classified under /misc
    gyou_links_dict: dict[CJKGyouGroupType, str] = {}
    for gyou_element in gyou_list:
        a_tag = gyou_element.find_next("a")

        a_tag_exists = not isNull(a_tag)
        a_tag_href_exists = a_tag_exists and not isNull(a_tag["href"])
        a_tag_string_exists = a_tag_exists and not isNull(a_tag.string)

        if a_tag_href_exists and a_tag_string_exists:
            romanji_gyou_tag_string = cast(CJKGyouOrMiscType, a_tag.string.strip())
            if romanji_gyou_tag_string == "/misc":
                continue
            gyou_links_dict[romanji_gyou_tag_string] = WIKI_BOOKS_ROOT_URL + str(
                a_tag["href"]
            )

    if vocab_file_path is None:
        save_text_to_file(
            dir=Path(f"./.cache/{level}/vocab"),
            filename=f"gyou-link{current_time_string}.json",
            contents=json.dumps(obj=gyou_links_dict, ensure_ascii=False),
        )

    # Delay between requests to avoid overwhelming the server
    # !: Currently not relevent since I'm only making single requests at a time
    # TODO: Implement this further later one
    if delay_seconds is not None:
        time.sleep(delay_seconds)


def scrape_row_a_temp(delay: int | None = None):
    url = "https://en.wikibooks.org/wiki/JLPT_Guide/JLPT_N5_Vocabulary/Row_A"

    print(f"Fetching Wikipedia JLPT N5 vocabulary Row A: {url}")

    vocab_page = requests.get(url=url, headers=SCRAPER_HEADER).content
    time.sleep(1)

    current_time = datetime.now(UTC)
    current_time_string = current_time.strftime("%Y-%m-%dT%H:%M:%S")

    vocab_soup = bSoup(vocab_page, "html.parser")
    wiki_content = vocab_soup.find("div", class_="mw-content-ltr")

    if wiki_content is None:
        raise ValueError("Error: Could not find wiki content in the page.")

    dan_group_list = wiki_content.find_all("div", class_="mw-heading2")
    nextcheck_temp = []
    word_list: list[VocabEntry] = []
    word_temp: VocabEntry = {
        "kana": "",
        "kanji": None,
        "classification": None,
        "definition": "",
    }

    for dan_element in dan_group_list:
        table_sibling = dan_element.find_next_sibling(name="table")

        if table_sibling is None:
            break

        table_body = table_sibling.find(recursive=False)

        if table_body is None:
            break

        for table_row in table_body.children:
            if isinstance(table_row, Tag):
                table_row.find(recursive=False)

                if table_row.name == "th":
                    continue

                for idx, row_contents in enumerate(table_row.children):
                    """
                    col 0 -> Word number in the book (can be skipped)
                    col 1 -> Kana writing
                    col 2 -> Kanji writing (if exists)
                    col 3 -> Word classification
                    col 4 -> Definition
                    """
                    if idx == 0:
                        continue
                    elif idx == 1:
                        if isinstance(row_contents, Tag):
                            a_tag = row_contents.a

                            a_tag_extists = a_tag is not None
                            a_tag_string_exists = (
                                a_tag_extists and a_tag.string is not None
                            )

                            if a_tag_extists and a_tag_string_exists:
                                word_temp["kana"] = a_tag.string.strip()
                    elif idx == 2:
                        if isinstance(row_contents, Tag):
                            a_tag = row_contents.a

                            a_tag_extists = a_tag is not None
                            a_tag_string_exists = (
                                a_tag_extists and a_tag.string is not None
                            )

                            if a_tag_extists and a_tag_string_exists:
                                word_temp["kanji"] = a_tag.string.strip()
                            # ? JULIUS: was las here!
                            # Was last trying to extract the contents from the row
                            # I didn't test this before leaving, so this likely doesn't work yet

        nextcheck_temp.append(table_body)

    with open(
        f"./.cache/n5/vocab/rowA.html",
        mode="w",
        encoding="utf-8",
    ) as file:
        file.write(str(nextcheck_temp))

    if delay is not None:
        time.sleep(delay)
