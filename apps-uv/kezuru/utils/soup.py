from collections.abc import Iterator

from bs4.element import NavigableString, PageElement


def filter_navigablestring_from_element_list(
    list_var: list[PageElement],
) -> list[PageElement]:
    return [item for item in list_var if not isinstance(item, NavigableString)]


def reconstruct_stripped_strings(stripped_strings: Iterator[str]) -> str:
    reconstructed = " ".join(stripped_strings)
    return reconstructed
