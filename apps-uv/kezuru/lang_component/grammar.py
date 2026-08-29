import json
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import cast

import requests
from bs4 import BeautifulSoup as bSoup
from bs4.element import Tag
from rich import print as rprint
from utils.constants import (
    CACHE_DIRS,
    SCRAPER_HEADER,
    WIKI_JLPT_LEVEL_RESOUCE_LINK,
)
from utils.file import (
    get_path_of_latest_file,
    save_text_to_file,
)
from utils.grammar import split_example_cjk_english_sentence
from utils.soup import reconstruct_stripped_strings
from utils.type_guard import isNull
from utils.types import GrammarEntryType, JLPTLevelType


def scrape_grammar(
    levels: list[JLPTLevelType],
    delay_seconds: int | None = 5,
    output_dir: Path = Path("./output/"),
    pretty_print: bool = False,
) -> None:
    """
    Scrape specified Wikipedia JLPT Guide Grammar by level.

    Args:
        - `level` -> JLPT level to scrape grammar for.
        - `delay_seconds` [optional] -> Seconds to wait after request. `None` = no sleep.
    """

    # TODO: There's a lot code repeated here from lang_component/vocab.py
    # Refactor to unite them as well as general cleanup

    for level in levels:
        cached_page = get_path_of_latest_file(CACHE_DIRS[level]["grammar"]["root"])
        if not isNull(cached_page):
            rprint(
                f"[green]Loading Wikipedia JLPT {level.capitalize()} root grammar page from latest cached html:[/green] \
                {cached_page}",
            )
            with open(cached_page, mode="r", encoding="utf-8") as file:
                grammar_page = file.read()
        else:
            url = WIKI_JLPT_LEVEL_RESOUCE_LINK[level]["grammar"]["root"]
            rprint(
                f"[green]Fetching Wikipedia JLPT {level.capitalize()} root vocabulary page from the internet:[/green] {url}"
            )
            if delay_seconds is not None:
                rprint(
                    f"[magenta]Practicing {delay_seconds} second delay before fetching as courtesy to not overwhelm host with requests ...[/magenta]"
                )
                time.sleep(delay_seconds)
            grammar_page = requests.get(url=url, headers=SCRAPER_HEADER).content

        grammar_soup = bSoup(grammar_page, "html5lib")

        current_time_string = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%S")

        if isNull(cached_page):
            save_text_to_file(
                dir=Path(CACHE_DIRS[level]["grammar"]["root"]),
                filename=f"{level}-root-grammar-page-{current_time_string}-utc.html",
                contents=str(grammar_soup.prettify()),
            )

        wiki_content = grammar_soup.find("div", class_="mw-content-ltr")
        if isNull(wiki_content):
            # TODO: address unhandled error
            raise ValueError("Error: Could not find wiki content in the page.")

        content_element = wiki_content.contents

        concepts_list: list[GrammarEntryType] = []
        grammar_concept_temp: GrammarEntryType = {
            "concept": "",
            "definition": "",
            "examples": [],
        }

        # Run through contents and scrape depending on the contents
        for element_idx in range(len(content_element)):
            element = content_element[element_idx]
            curr_concept_ptr: str | None = None

            if isinstance(element, Tag):
                class_list = cast(list[str], element.get("class"))
                if (
                    not isNull(class_list)
                    and "mw-heading3" in class_list
                    and not isNull(element.h3)
                ):
                    # Once the concept header changes, append the filled-up
                    #   grammar_concept_temp object to the list
                    if (
                        curr_concept_ptr != str(element.h3.get("id"))
                        and len(grammar_concept_temp["concept"]) > 0
                    ):
                        concepts_list.append(grammar_concept_temp)
                        grammar_concept_temp = {
                            "concept": "",
                            "definition": "",
                            "examples": [],
                        }

                    curr_concept_ptr = str(element.h3.get("id"))
                    grammar_concept_temp["concept"] = curr_concept_ptr

                if element.name == "p":
                    reconstructed = reconstruct_stripped_strings(
                        element.stripped_strings
                    )
                    if len(grammar_concept_temp["concept"]) > 0:
                        grammar_concept_temp["definition"] = " ".join(
                            [grammar_concept_temp["definition"], reconstructed]
                        ).strip()

                elif element.name == "ul":
                    # print(element)
                    list_items = element.find_all("li")
                    for item in list_items:
                        if isinstance(item, Tag):
                            (cjk_sentence, english_sentence) = (
                                split_example_cjk_english_sentence(
                                    reconstruct_stripped_strings(item.stripped_strings)
                                )
                            )
                            grammar_concept_temp["examples"].append(
                                {"sentence": cjk_sentence, "meaning": english_sentence}
                            )
            else:
                # Append the last filled-up grammar_concept_temp object to the list
                if element_idx == len(content_element) - 1:
                    concepts_list.append(grammar_concept_temp)

        save_text_to_file(
            dir=Path(output_dir),
            filename=f"grammar_{level}.json",
            contents=json.dumps(
                obj=concepts_list,
                ensure_ascii=False,
                indent=(2 if pretty_print else None),
            ),
        )
