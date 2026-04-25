from utils.types import CJKGyouGroup, RomanjiGyouGroup

GYOU_GROUPS: list[CJKGyouGroup] = [
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
]

ROMANJI_GYOU_DICT: dict[RomanjiGyouGroup, CJKGyouGroup] = {
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
