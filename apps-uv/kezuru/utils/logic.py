from collections.abc import Sequence
from typing import cast


def filter_from_list[T](items_list: Sequence[T], patterns: list[T]) -> list[T]:
    list_len = len(items_list)
    if list_len == 0:
        return []
    elif list_len == 1:
        single_item = cast(T, items_list)
        return [single_item]
    else:
        return [item for item in items_list if item not in patterns]
