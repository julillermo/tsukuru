import json
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import cast

import requests
from bs4 import BeautifulSoup as bSoup
from bs4.element import Tag
from utils.file import save_text_to_file
from utils.type_guard import isNull
from utils.types import (
    CJKGyouGroupType,
    CJKGyouOrMiscType,
    JLPTComponentType,
    JLPTLevelType,
    VocabEntryType,
)
from utils.vocab import (
    extract_english_word_classes,
    filter_from_page_element_list,
)

WIKI_BOOKS_ROOT_URL = "https://en.wikibooks.org"
WIKI_JLPT_GUIDE_BASE_URL = f"{WIKI_BOOKS_ROOT_URL}/wiki/JLPT_Guide"
TARGET_RESOURCE_PATH: dict[JLPTLevelType, dict[JLPTComponentType, str]] = {
    "n5": {
        "vocab": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N5_Vocabulary",
        "kanji": WIKI_JLPT_GUIDE_BASE_URL + "/N5_KANJI_URL_PATH",
        "grammar": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N5_Grammar",
    }
}
# TODO: This OUTPUT_PATHS is unused. Incorporate it
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

    if isNull(vocab_file_path):
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

    # TODO: Implement this further later on
    # Delay between requests to avoid overwhelming the server
    # Currently irrelevent since I'm only making single requests at a time
    if delay_seconds is not None:
        time.sleep(delay_seconds)


def scrape_row_a_temp(
    vocab_row_file_path: str | None = None, delay_seconds: int | None = None
):
    # TODO: Add function description for intellisense
    # TODO: Currently a costant. Make this as input comming from scrape_vocab() outout
    url = "https://en.wikibooks.org/wiki/JLPT_Guide/JLPT_N5_Vocabulary/Row_A"
    cache_exists = not isNull(vocab_row_file_path)

    if cache_exists:
        print(
            "Loading JLPT N5 row A vocab from latest cached vocab file:",
            vocab_row_file_path,
        )
        with open(vocab_row_file_path, mode="r", encoding="utf-8") as file:
            vocab_page = file.read()
    else:
        print(f"Fetching JLPT N5 row A vocab from the internet: {url}")
        vocab_page = requests.get(url=url, headers=SCRAPER_HEADER).content

    vocab_soup = bSoup(vocab_page, "html.parser")

    current_time = datetime.now(UTC)
    current_time_string = current_time.strftime("%Y-%m-%dT%H:%M:%S")

    if not cache_exists:
        save_text_to_file(
            dir=Path("./.cache/n5/vocab/row"),
            filename=f"html-page-row_a-vocab-{current_time_string}-utc.html",
            contents=str(vocab_soup.prettify()),
        )

    wiki_content = vocab_soup.find("div", class_="mw-content-ltr")
    if isNull(wiki_content):
        # TODO: Make error messages distinguishable from other similarly messaged errors
        # TODO: Also check for uncaught errors later on
        raise ValueError("Error: Could not find wiki content in the page.")

    dan_group_list = wiki_content.find_all("div", class_="mw-heading2")
    word_list: list[VocabEntryType] = []

    for dan_element in dan_group_list:
        table_sibling = dan_element.find_next_sibling(name="table")
        if isNull(table_sibling):
            continue

        table_body = table_sibling.find(recursive=False)
        if isNull(table_body):
            continue

        for table_row in table_body.children:
            if isinstance(table_row, Tag):
                # Skip the header row
                if not isNull(table_row.th):
                    continue

                word_temp: VocabEntryType = {
                    "wikipediaIndex": None,
                    "kana": "",
                    "kanji": None,
                    "classification": [],
                    "definition": "",
                }

                for col_idx, col_data in enumerate(
                    filter_from_page_element_list(table_row.contents, "\n")
                ):
                    """
                    col_idx 0 -> Wikipedia word index
                    col_idx 1 -> Kana writing
                    col_idx 2 -> Kanji writing (if exists)
                    col_idx 3 -> Word classification
                    col_idx 4 -> Definition
                    """
                    col_data_tag = cast(Tag, col_data)
                    # Wikipedia word index
                    if col_idx == 0:
                        if not isNull(col_data_tag.string):
                            # TODO: improve int conversion. Works for now, but not general enough to work in other cases
                            word_temp["wikipediaIndex"] = int(col_data_tag.string)
                    # Kana writing
                    elif col_idx == 1:
                        if not isNull(col_data_tag.a) and not isNull(
                            col_data_tag.a.string
                        ):
                            word_temp["kana"] = col_data_tag.a.string.strip()
                    # Kanji writing
                    elif col_idx == 2:
                        if not isNull(col_data_tag.a) and not isNull(
                            col_data_tag.a.string
                        ):
                            word_temp["kanji"] = col_data_tag.a.string.strip()
                    # Word classification
                    elif col_idx == 3:
                        if not isNull(col_data_tag.string):
                            word_temp["classification"] = extract_english_word_classes(
                                cjk_word_class_str=col_data_tag.string
                            )
                    # Definition
                    elif col_idx == 4:  # noqa: SIM102
                        if not isNull(col_data_tag.string):
                            word_temp["definition"] = col_data_tag.string.replace(
                                "\n", ""
                            )

                word_list.append(word_temp)

    save_text_to_file(
        dir=Path("./.cache/n5/vocab"),
        filename="ABC.json",
        contents=json.dumps(obj=word_list, ensure_ascii=False),
    )

    # TODO: Implement this further later on
    # Delay between requests to avoid overwhelming the server
    # Currently irrelevent since I'm only making single requests at a time
    if not isNull(delay_seconds):
        time.sleep(delay_seconds)
