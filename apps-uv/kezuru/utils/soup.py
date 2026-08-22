from collections.abc import Iterator

from bs4.element import NavigableString, PageElement


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


def filter_navigablestring_from_element_list(
    list_var: list[PageElement],
) -> list[PageElement]:
    return [item for item in list_var if not isinstance(item, NavigableString)]


def reconstruct_stripped_strings(stripped_strings: Iterator[str]) -> str:
    reconstructed = " ".join(stripped_strings)
    return reconstructed
