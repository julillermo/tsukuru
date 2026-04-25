from bs4 import NavigableString, PageElement

from utils.constants import ROMANJI_GYOU_DICT
from utils.types import RomanjiGyouGroup


def filter_from_page_element_list(
    listVar: list[PageElement], pattern: PageElement | str
) -> list[PageElement]:

    if type(pattern) is PageElement:
        pattern_to_use = pattern
    elif type(pattern) is str:
        pattern_to_use = NavigableString(pattern)

    return [item for item in listVar if item != pattern_to_use]


def get_cjk(romanji_group: RomanjiGyouGroup):
    return ROMANJI_GYOU_DICT[romanji_group]
