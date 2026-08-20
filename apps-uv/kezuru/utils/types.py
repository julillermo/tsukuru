from typing import Literal, TypedDict

JLPTLevelType = Literal["n5", "n4", "n3", "n2", "n1"]
JLPTComponentType = Literal["vocab", "kanji", "grammar"]

CJKGyouGroupType = Literal[
    "あ行",
    "か行",
    "さ行",
    "た行",
    "な行",
    "は行",
    "ま行",
    "や行",
    "ら行",
    "わ行",
]
RomanjiGyouGroupType = Literal[
    "a",
    "ka",
    "sa",
    "ta",
    "na",
    "ha",
    "ma",
    "ya",
    "ra",
    "wa",
]

CJKMiscGroupType = Literal["/misc", "misc"]
CJKGyouOrMiscType = CJKGyouGroupType | CJKMiscGroupType

JlptResourceRootType = Literal["root"]
JlptResourceVocabObjKeysType = RomanjiGyouGroupType | JlptResourceRootType
JlptRscRootGyouObjType = dict[JlptResourceVocabObjKeysType, str]

CJKDanGroupType = Literal["あ段", "い段", "う段", "え段", "お段"]
RomanjiDanGroupType = Literal["a", "i", "u", "e", "o"]

CJKWordClassKanjiType = Literal[
    "名",  # noun
    "代",  # pronoun
    "動I",  # type I verb
    "動II",  # type II verb
    "動III",  # type III verb
    "形",  # adjective
    "形動",  # adjectival noun
    "副",  # adverb
    "連体",  # attribute
    "接",  # conjunction
    "感",  # interjection
    "助動",  # auxiliary
    "助",  # particle
    "頭",  # prefix
    "尾",  # suffix
    "連",  # compound
]
EnglishWordClassType = Literal[
    "noun",
    "pronoun",
    "type I verb",
    "type II verb",
    "type III verb",
    "adjective",
    "adjectival noun",
    "adverb",
    "attribute",
    "conjunction",
    "interjection",
    "auxiliary",
    "particle",
    "prefix",
    "suffix",
    "compound",
]


class VocabEntryType(TypedDict):
    wikipediaIndex: int | None
    kana: str
    kanji: str | None
    classification: list[EnglishWordClassType]
    definition: str


class ExampleSentenceType(TypedDict):
    sentence: str
    meaning: str


class GrammarEntryType(TypedDict):
    concept: str
    definition: str
    examples: list[ExampleSentenceType]
