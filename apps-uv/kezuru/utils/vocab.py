import warnings
from typing import cast

from bs4 import NavigableString, PageElement

from utils.constants import CJK_ENGLISH_WORD_CLASS_DICT
from utils.string import remove_parenthesis_plus
from utils.types import (
    CJKWordClassKanjiType,
    EnglishWordClassType,
)


def filter_from_page_element_list(
    list_var: list[PageElement], pattern: PageElement | str
) -> list[PageElement]:
    """
    Remove from a list of `PageElement`s based on a provided pattern

    Args:
        - `list_var` -> List of elements to filter
        - `pattern` -> Pattern to remove from the resulting list
    """
    pattern_to_use = (
        pattern if isinstance(pattern, PageElement) else NavigableString(pattern)
    )

    return [item for item in list_var if item != pattern_to_use]


def get_english_word_class(
    cjk_word_class: CJKWordClassKanjiType,
) -> EnglishWordClassType:
    if cjk_word_class in CJK_ENGLISH_WORD_CLASS_DICT:
        return CJK_ENGLISH_WORD_CLASS_DICT[cjk_word_class]
    else:
        raise KeyError(f"Unrecognzied word classification: {cjk_word_class}")


def get_english_word_class_list(
    cjk_word_class_list: list[CJKWordClassKanjiType],
) -> list[EnglishWordClassType]:
    english_word_class_list: list[EnglishWordClassType] = []
    for cjk_word_class in cjk_word_class_list:
        try:
            eng_word_class = get_english_word_class(cjk_word_class)
            english_word_class_list.append(eng_word_class)
        except KeyError as err:
            warnings.warn(f"KeyError: {err}")
            print(
                f"Ignored word classification annotation '{cjk_word_class}'. Proceeding ...\n"
            )
            continue

    return english_word_class_list


def extract_english_word_classes(cjk_word_class_str: str) -> list[EnglishWordClassType]:
    cjk_word_class_list = cast(
        list[CJKWordClassKanjiType],
        remove_parenthesis_plus(str_with_parenthesis=cjk_word_class_str).split("，"),
    )
    return get_english_word_class_list(cjk_word_class_list)
