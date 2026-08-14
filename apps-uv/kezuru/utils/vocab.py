from bs4 import NavigableString, PageElement

from utils.constants import ROMANJI_GYOU_DICT
from utils.types import RomanjiGyouGroupType


def filter_from_page_element_list(
    list_var: list[PageElement], pattern: PageElement | str
) -> list[PageElement]:
    """
    Remove from a list elements based on a provided pattern

    Args:
        - `list_var` -> List of elements to filter
        - `pattern` -> Pattern to remove from the resulting list
    """
    pattern_to_use = (
        pattern if isinstance(pattern, PageElement) else NavigableString(pattern)
    )

    return [item for item in list_var if item != pattern_to_use]


def get_cjk(romanji_group: RomanjiGyouGroupType):
    return ROMANJI_GYOU_DICT[romanji_group]
