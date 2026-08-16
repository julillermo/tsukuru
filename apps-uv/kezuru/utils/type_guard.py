from typing import TypeIs

from bs4 import Tag

from utils.constants import GYOU_MISC_GROUPS
from utils.types import CJKMiscGroupType


def isCJKMiscGroup(var: object) -> TypeIs[CJKMiscGroupType]:
    return var in GYOU_MISC_GROUPS


def isNull[T](var: T | None) -> TypeIs[None]:
    if isinstance(var, list):
        return bool(not var or len(var) <= 0)
    else:
        return var is None


def isBs4Tag(var: object) -> TypeIs[Tag]:
    return bool(isinstance(var, Tag))
