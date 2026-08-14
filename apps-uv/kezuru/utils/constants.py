from utils.types import (
    CJKDanGroupType,
    CJKGyouGroupType,
    CJKMiscGroupType,
    RomanjiDanGroup,
    RomanjiGyouGroupType,
)

GYOU_GROUPS: list[CJKGyouGroupType | CJKMiscGroupType] = [
    "あ行",  # a-line / a-row
    "か行",  # k-line / k-row
    "さ行",  # s-line / s-row
    "た行",  # t-line / t-row
    "な行",  # n-line / n-row
    "は行",  # h-line / h-row
    "ま行",  # m-line / m-row
    "や行",  # y-line / y-row
    "ら行",  # r-line / r-row
    "わ行",  # w-line / w-row
    "/misc",  # miscellaneous
]

ROMANJI_GYOU_DICT: dict[RomanjiGyouGroupType, CJKGyouGroupType] = {
    "a": "あ行",
    "ka": "か行",
    "sa": "さ行",
    "ta": "た行",
    "na": "な行",
    "ma": "ま行",
    "ya": "や行",
    "ra": "ら行",
    "wa": "わ行",
}

DAN_GROUPS: list[CJKDanGroupType] = [
    "あ段",  # a-words
    "い段",  # i-words
    "う段",  # u-words
    "え段",  # e-words
    "お段",  # o-words
]

ROMANJI_DAN_DICT: dict[RomanjiDanGroup, CJKDanGroupType] = {
    "a": "あ段",
    "i": "い段",
    "u": "う段",
    "e": "え段",
    "o": "お段",
}
