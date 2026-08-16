from collections.abc import Sequence
from typing import cast

from bs4.element import NavigableString, PageElement


def filter_from_list[T](items_list: Sequence[T], patterns: list[T]) -> list[T]:
    list_len = len(items_list)
    if list_len == 0:
        return []
    elif list_len == 1:
        single_item = cast(T, items_list)
        return [single_item]
    else:
        return [item for item in items_list if item not in patterns]


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
