import json
import time
import warnings
from datetime import UTC, datetime
from pathlib import Path
from typing import Literal, cast

import requests
from bs4 import BeautifulSoup as bSoup
from bs4.element import Tag
from rich import print as rprint
from utils.constants import (
    CACHE_DIRS,
    CJK_GYOU_DICT,
    SCRAPER_HEADER,
    WIKI_BOOKS_ROOT_URL,
    WIKI_JLPT_LEVEL_RESOUCE_LINK,
)
from utils.file import (
    get_path_of_latest_file,
    save_text_to_file,
)
from utils.soup import (
    filter_navigablestring_from_element_list,
)
from utils.type_guard import isCJKMiscGroup, isNull
from utils.types import (
    CJKGyouGroupType,
    CJKGyouOrMiscType,
    JLPTLevelType,
    RomanjiGyouGroupType,
    VocabEntryType,
)
from utils.vocab import extract_english_word_classes


def scrape_vocab(
    levels: list[JLPTLevelType],
    delay_seconds: int | None = 5,
    output_dir: Path = Path("./output/"),
    saving_strategy: Literal["combined", "individual"] = "combined",
    pretty_print: bool = False,
    ignore_cache: bool = False,
) -> None:
    """
    Scrape specified Wikipedia JLPT Guide Vocab by level.

    Args:
        - `level` -> JLPT level to scrape vocab for.
        - `delay_seconds` [optional] -> Seconds to wait after request. `None` = no sleep.
    """

    for level in levels:
        cached_page = get_path_of_latest_file(CACHE_DIRS[level]["vocab"]["root"])
        if not ignore_cache and not isNull(cached_page):
            rprint(
                f"[green]Loading Wikipedia JLPT {level.capitalize()} root vocabulary page from latest cached html:[/green] \
                {cached_page}",
            )
            with open(cached_page, mode="r", encoding="utf-8") as file:
                vocab_page = file.read()
        else:
            url = WIKI_JLPT_LEVEL_RESOUCE_LINK[level]["vocab"]["root"]
            rprint(
                f"[green]Fetching Wikipedia JLPT {level.capitalize()} root vocabulary page from the internet:[/green] {url}"
            )
            if delay_seconds is not None:
                rprint(
                    f"[magenta]Practicing {delay_seconds} second delay before fetching as courtesy to not overwhelm host with requests ...[/magenta]"
                )
                time.sleep(delay_seconds)

            vocab_page = requests.get(url=url, headers=SCRAPER_HEADER).content

        vocab_soup = bSoup(vocab_page, "html5lib")

        current_time_string = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%S")

        if isNull(cached_page):
            save_text_to_file(
                dir=Path(CACHE_DIRS[level]["vocab"]["root"]),
                filename=f"{level}-root-vocab-page-{current_time_string}-utc.html",
                contents=vocab_soup.prettify(),
            )

        wiki_content = vocab_soup.find("div", class_="mw-content-ltr")
        if isNull(wiki_content):
            # TODO: address unhandled error
            raise ValueError("Error: Could not find wiki content in the page.")

        gyou_ul_element = wiki_content.find(name="ul", recursive=False)
        if isNull(gyou_ul_element):
            # TODO: address unhandled error
            raise ValueError("Error: Could not find gyou element in the page.")

        gyou_list = filter_navigablestring_from_element_list(
            list_var=gyou_ul_element.contents,
        )

        # The following doesn't pick up words classified under "/misc" or "misc"
        gyou_links_dict: dict[CJKGyouGroupType, str] = {}
        for gyou_element in gyou_list:
            a_tag = gyou_element.find_next("a")

            a_tag_exists = not isNull(a_tag)
            a_tag_href_exists = a_tag_exists and not isNull(a_tag["href"])
            a_tag_string_exists = a_tag_exists and not isNull(a_tag.string)

            if a_tag_href_exists and a_tag_string_exists:
                romanji_gyou_tag_string = cast(CJKGyouOrMiscType, a_tag.string.strip())
                if isCJKMiscGroup(romanji_gyou_tag_string):
                    continue
                gyou_links_dict[romanji_gyou_tag_string] = WIKI_BOOKS_ROOT_URL + str(
                    a_tag["href"]
                )

        if cached_page is None:
            save_text_to_file(
                dir=Path(CACHE_DIRS[level]["vocab"]["root"]),
                filename=f"{level}-gyou-link{current_time_string}.json",
                contents=json.dumps(obj=gyou_links_dict, ensure_ascii=False),
            )

        combined_word_list: list[VocabEntryType] = []
        for cjk_gyou in gyou_links_dict:
            romanji_gyou = CJK_GYOU_DICT[cjk_gyou]
            gyou_word_list = scrape_gyou_groups(
                level=level,
                romanji_gyou=CJK_GYOU_DICT[cjk_gyou],
                delay_seconds=delay_seconds,
                ignore_cache=ignore_cache,
                # link=gyou_links_dict[cjk_gyou] # The JLPT links to wrong pages
            )

            if saving_strategy == "individual":
                save_text_to_file(
                    dir=Path(output_dir),
                    filename=f"vocab_{level}_{romanji_gyou}.json",
                    contents=json.dumps(obj=gyou_word_list, ensure_ascii=False),
                )
            elif saving_strategy == "combined":
                combined_word_list.extend(gyou_word_list)

        if saving_strategy == "combined":
            save_text_to_file(
                dir=Path(output_dir),
                filename=f"vocab_{level}_combined.json",
                contents=json.dumps(
                    obj=combined_word_list,
                    ensure_ascii=False,
                    indent=(2 if pretty_print else None),
                ),
            )


def scrape_gyou_groups(
    level: JLPTLevelType,
    romanji_gyou: RomanjiGyouGroupType,
    delay_seconds: int | None = 5,
    link: str | None = None,
    ignore_cache: bool = False,
) -> list[VocabEntryType]:
    # TODO: Add function description for intellisense
    # TODO: Currently a costant. Make this as input comming from scrape_vocab() outout
    cached_page = get_path_of_latest_file(CACHE_DIRS[level]["vocab"][romanji_gyou])

    if not ignore_cache and not isNull(cached_page):
        rprint(
            f"[green]Loading JLPT {level.capitalize()} row {romanji_gyou.capitalize()} vocab from latest cached html:[/green] \
            {cached_page}",
        )
        with open(cached_page, mode="r", encoding="utf-8") as file:
            vocab_page = file.read()
    else:
        if isNull(link):
            url = WIKI_JLPT_LEVEL_RESOUCE_LINK[level]["vocab"][romanji_gyou]
        else:
            url = link

        rprint(
            f"[green]Fetching JLPT {level.capitalize()} row {romanji_gyou.capitalize()} vocab from the internet:[/green] {url}"
        )
        if not isNull(delay_seconds):
            rprint(
                f"[magenta]Practicing {delay_seconds} second delay before fetching as courtesy to not overwhelm host with requests ...[/magenta]"
            )
            time.sleep(delay_seconds)
        vocab_page = requests.get(url=url, headers=SCRAPER_HEADER).content

    vocab_soup = bSoup(vocab_page, "html5lib")

    current_time = datetime.now(UTC)
    current_time_string = current_time.strftime("%Y-%m-%dT%H:%M:%S")

    if isNull(cached_page):
        save_text_to_file(
            dir=Path(CACHE_DIRS[level]["vocab"][romanji_gyou]),
            filename=f"html-page-row_a-vocab-{current_time_string}-utc.html",
            contents=str(vocab_soup.prettify()),
        )

    wiki_content = vocab_soup.find("div", class_="mw-content-ltr")
    if isNull(wiki_content):
        # TODO: Make error messages distinguishable from other similarly messaged errors
        # TODO: Also check for uncaught errors later on
        raise ValueError("Error: Could not find wiki content in the page.")

    dan_group_list = wiki_content.find_all("div", class_="mw-heading2")
    gyou_word_list: list[VocabEntryType] = []

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

                vocab_temp: VocabEntryType = {
                    "wiki_index": None,
                    "kana_writing": "",
                    "kanji": None,
                    "classification": [],
                    "definition": "",
                }
                is_column_error: bool = False

                for col_idx, col_data in enumerate(
                    filter_navigablestring_from_element_list(table_row.contents)
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
                            print(f"col_data_tag.string: {col_data_tag.string!r}")
                            try:
                                number_value = int(col_data_tag.string)
                                rprint(
                                    f"Scraping word: {level.capitalize()}#{number_value}"
                                )  # TODO: make this optional with a `verbose` flag/argument
                                vocab_temp["wiki_index"] = number_value
                            except ValueError as err:
                                warnings.warn(
                                    f"Invalid int() conversion error for Wikipedia {level.capitalize()!r} word index '{col_data_tag.string}': {err}"
                                )
                                rprint(
                                    f"[yellow]Ignored invalid entire row of Wikipedia {level.capitalize()} word index '{col_data_tag.string}'. Proceeding ...[/yellow]"
                                )
                                is_column_error = True
                                continue
                    # Kana writing
                    elif col_idx == 1:
                        if not isNull(col_data_tag.a) and not isNull(
                            col_data_tag.a.string
                        ):
                            vocab_temp["kana_writing"] = col_data_tag.a.string.strip()
                            continue
                        if not isNull(col_data_tag.string):
                            vocab_temp["kana_writing"] = col_data_tag.string.replace(
                                "\n", ""
                            ).strip()
                            continue
                    # Kanji writing
                    elif col_idx == 2:
                        if not isNull(col_data_tag.a) and not isNull(
                            col_data_tag.a.string
                        ):
                            vocab_temp["kanji"] = col_data_tag.a.string.replace(
                                "\n", ""
                            ).strip()
                    # Word classification
                    elif col_idx == 3:
                        if not isNull(col_data_tag.a) and not isNull(
                            col_data_tag.a.string
                        ):
                            vocab_temp["classification"] = extract_english_word_classes(
                                cjk_word_class_str=col_data_tag.a.string
                            )
                            continue
                        if not isNull(col_data_tag.string):
                            vocab_temp["classification"] = extract_english_word_classes(
                                cjk_word_class_str=col_data_tag.string
                            )
                            continue
                    # Definition
                    elif col_idx == 4:  # noqa: SIM102
                        if not isNull(col_data_tag.string):
                            vocab_temp["definition"] = col_data_tag.string.replace(
                                "\n", ""
                            ).strip()

                if is_column_error:
                    continue
                else:
                    gyou_word_list.append(vocab_temp)
                is_column_error = False

    return gyou_word_list
