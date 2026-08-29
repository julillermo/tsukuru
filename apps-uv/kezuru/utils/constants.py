from utils.types import (
    CJKDanGroupType,
    CJKGyouGroupType,
    CJKMiscGroupType,
    CJKWordClassKanjiType,
    EnglishWordClassType,
    JLPTComponentType,
    JLPTLevelType,
    JlptRscRootGyouObjType,
    RomanjiDanGroupType,
    RomanjiGyouGroupType,
)

JLPT_LEVELS: list[JLPTLevelType] = ["n5", "n4", "n3", "n2", "n1"]

WIKI_BOOKS_ROOT_URL = "https://en.wikibooks.org"
WIKI_JLPT_GUIDE_BASE_URL = f"{WIKI_BOOKS_ROOT_URL}/wiki/JLPT_Guide"
WIKI_JLPT_LEVEL_RESOUCE_LINK: dict[
    JLPTLevelType,
    dict[JLPTComponentType, JlptRscRootGyouObjType],
] = {
    "n5": {
        "vocab": {
            "root": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N5_Vocabulary",
            "a": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N5_Vocabulary/Row_A",
            "ka": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N5_Vocabulary/Row_Ka",
            "sa": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N5_Vocabulary/Row_Sa",
            "ta": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N5_Vocabulary/Row_Ta",
            "na": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N5_Vocabulary/Row_Na",
            "ha": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N5_Vocabulary/Row_Ha",
            "ma": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N5_Vocabulary/Row_Ma",
            "ya": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N5_Vocabulary/Row_Ya",
            "ra": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N5_Vocabulary/Row_Ra",
            "wa": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N5_Vocabulary/Row_Wa",
        },
        "kanji": {
            "root": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N5_Kanji",
        },
        "grammar": {
            "root": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N5_Grammar",
        },
    },
    "n4": {
        "vocab": {
            "root": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N4_Vocabulary",
            "a": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N4_Vocabulary/Row_A",
            "ka": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N4_Vocabulary/Row_Ka",
            "sa": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N4_Vocabulary/Row_Sa",
            "ta": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N4_Vocabulary/Row_Ta",
            "na": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N4_Vocabulary/Row_Na",
            "ha": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N4_Vocabulary/Row_Ha",
            "ma": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N4_Vocabulary/Row_Ma",
            "ya": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N4_Vocabulary/Row_Ya",
            "ra": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N4_Vocabulary/Row_Ra",
            "wa": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N4_Vocabulary/Row_Wa",
        },
        "kanji": {
            "root": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N4_Kanji",
        },
        "grammar": {
            "root": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N4_Grammar",
        },
    },
    "n3": {
        "vocab": {
            "root": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N3_Vocabulary",
            "a": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N3_Vocabulary/Row_A",
            "ka": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N3_Vocabulary/Row_Ka",
            "sa": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N3_Vocabulary/Row_Sa",
            "ta": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N3_Vocabulary/Row_Ta",
            "na": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N3_Vocabulary/Row_Na",
            "ha": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N3_Vocabulary/Row_Ha",
            "ma": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N3_Vocabulary/Row_Ma",
            "ya": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N3_Vocabulary/Row_Ya",
            "ra": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N3_Vocabulary/Row_Ra",
            "wa": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N3_Vocabulary/Row_Wa",
        },
        "kanji": {
            "root": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N3_Kanji",
        },
        "grammar": {
            "root": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N3_Grammar",
        },
    },
    "n2": {
        "vocab": {
            "root": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N2_Vocabulary",
            "a": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N2_Vocabulary/Row_A",
            "ka": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N2_Vocabulary/Row_Ka",
            "sa": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N2_Vocabulary/Row_Sa",
            "ta": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N2_Vocabulary/Row_Ta",
            "na": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N2_Vocabulary/Row_Na",
            "ha": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N2_Vocabulary/Row_Ha",
            "ma": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N2_Vocabulary/Row_Ma",
            "ya": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N2_Vocabulary/Row_Ya",
            "ra": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N2_Vocabulary/Row_Ra",
            "wa": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N2_Vocabulary/Row_Wa",
        },
        "kanji": {
            "root": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N2_Kanji",
        },
        "grammar": {
            "root": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N2_Grammar",
        },
    },
    "n1": {
        "vocab": {
            "root": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N1_Vocabulary",
            "a": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N1_Vocabulary/Row_A",
            "ka": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N1_Vocabulary/Row_Ka",
            "sa": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N1_Vocabulary/Row_Sa",
            "ta": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N1_Vocabulary/Row_Ta",
            "na": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N1_Vocabulary/Row_Na",
            "ha": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N1_Vocabulary/Row_Ha",
            "ma": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N1_Vocabulary/Row_Ma",
            "ya": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N1_Vocabulary/Row_Ya",
            "ra": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N1_Vocabulary/Row_Ra",
            "wa": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N1_Vocabulary/Row_Wa",
        },
        "kanji": {
            "root": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N1_Kanji",
        },
        "grammar": {
            "root": WIKI_JLPT_GUIDE_BASE_URL + "/JLPT_N1_Grammar",
        },
    },
}

# TODO: Cache and Output seem unnecessary if I could proceedurally create them.
# Revisit this idea later on.
CACHE_DIR = "./.cache/"
CACHE_DIRS: dict[
    JLPTLevelType,
    dict[JLPTComponentType, JlptRscRootGyouObjType],
] = {
    "n5": {
        "vocab": {
            "root": CACHE_DIR + "/JLPT_N5_Vocabulary/Root/",
            "a": CACHE_DIR + "/JLPT_N5_Vocabulary/Row_A/",
            "ka": CACHE_DIR + "/JLPT_N5_Vocabulary/Row_Ka/",
            "sa": CACHE_DIR + "/JLPT_N5_Vocabulary/Row_Sa/",
            "ta": CACHE_DIR + "/JLPT_N5_Vocabulary/Row_Ta/",
            "na": CACHE_DIR + "/JLPT_N5_Vocabulary/Row_Na/",
            "ha": CACHE_DIR + "/JLPT_N5_Vocabulary/Row_Ha/",
            "ma": CACHE_DIR + "/JLPT_N5_Vocabulary/Row_Ma/",
            "ya": CACHE_DIR + "/JLPT_N5_Vocabulary/Row_Ya/",
            "ra": CACHE_DIR + "/JLPT_N5_Vocabulary/Row_Ra/",
            "wa": CACHE_DIR + "/JLPT_N5_Vocabulary/Row_Wa/",
        },
        "kanji": {
            "root": CACHE_DIR + "/JLPT_N5_Kanji/",
        },
        "grammar": {
            "root": CACHE_DIR + "/JLPT_N5_Grammar/",
        },
    },
    "n4": {
        "vocab": {
            "root": CACHE_DIR + "/JLPT_N4_Vocabulary/",
            "a": CACHE_DIR + "/JLPT_N4_Vocabulary/Row_A/",
            "ka": CACHE_DIR + "/JLPT_N4_Vocabulary/Row_Ka/",
            "sa": CACHE_DIR + "/JLPT_N4_Vocabulary/Row_Sa/",
            "ta": CACHE_DIR + "/JLPT_N4_Vocabulary/Row_Ta/",
            "na": CACHE_DIR + "/JLPT_N4_Vocabulary/Row_Na/",
            "ha": CACHE_DIR + "/JLPT_N4_Vocabulary/Row_Ha/",
            "ma": CACHE_DIR + "/JLPT_N4_Vocabulary/Row_Ma/",
            "ya": CACHE_DIR + "/JLPT_N4_Vocabulary/Row_Ya/",
            "ra": CACHE_DIR + "/JLPT_N4_Vocabulary/Row_Ra/",
            "wa": CACHE_DIR + "/JLPT_N4_Vocabulary/Row_Wa/",
        },
        "kanji": {
            "root": CACHE_DIR + "/JLPT_N4_Kanji/",
        },
        "grammar": {
            "root": CACHE_DIR + "/JLPT_N4_Grammar/",
        },
    },
    "n3": {
        "vocab": {
            "root": CACHE_DIR + "/JLPT_N3_Vocabulary/",
            "a": CACHE_DIR + "/JLPT_N3_Vocabulary/Row_A/",
            "ka": CACHE_DIR + "/JLPT_N3_Vocabulary/Row_Ka/",
            "sa": CACHE_DIR + "/JLPT_N3_Vocabulary/Row_Sa/",
            "ta": CACHE_DIR + "/JLPT_N3_Vocabulary/Row_Ta/",
            "na": CACHE_DIR + "/JLPT_N3_Vocabulary/Row_Na/",
            "ha": CACHE_DIR + "/JLPT_N3_Vocabulary/Row_Ha/",
            "ma": CACHE_DIR + "/JLPT_N3_Vocabulary/Row_Ma/",
            "ya": CACHE_DIR + "/JLPT_N3_Vocabulary/Row_Ya/",
            "ra": CACHE_DIR + "/JLPT_N3_Vocabulary/Row_Ra/",
            "wa": CACHE_DIR + "/JLPT_N3_Vocabulary/Row_Wa/",
        },
        "kanji": {
            "root": CACHE_DIR + "/JLPT_N3_Kanji/",
        },
        "grammar": {
            "root": CACHE_DIR + "/JLPT_N3_Grammar/",
        },
    },
    "n2": {
        "vocab": {
            "root": CACHE_DIR + "/JLPT_N2_Vocabulary/",
            "a": CACHE_DIR + "/JLPT_N2_Vocabulary/Row_A/",
            "ka": CACHE_DIR + "/JLPT_N2_Vocabulary/Row_Ka/",
            "sa": CACHE_DIR + "/JLPT_N2_Vocabulary/Row_Sa/",
            "ta": CACHE_DIR + "/JLPT_N2_Vocabulary/Row_Ta/",
            "na": CACHE_DIR + "/JLPT_N2_Vocabulary/Row_Na/",
            "ha": CACHE_DIR + "/JLPT_N2_Vocabulary/Row_Ha/",
            "ma": CACHE_DIR + "/JLPT_N2_Vocabulary/Row_Ma/",
            "ya": CACHE_DIR + "/JLPT_N2_Vocabulary/Row_Ya/",
            "ra": CACHE_DIR + "/JLPT_N2_Vocabulary/Row_Ra/",
            "wa": CACHE_DIR + "/JLPT_N2_Vocabulary/Row_Wa/",
        },
        "kanji": {
            "root": CACHE_DIR + "/JLPT_N2_Kanji/",
        },
        "grammar": {
            "root": CACHE_DIR + "/JLPT_N2_Grammar/",
        },
    },
    "n1": {
        "vocab": {
            "root": CACHE_DIR + "/JLPT_N1_Vocabulary/",
            "a": CACHE_DIR + "/JLPT_N1_Vocabulary/Row_A/",
            "ka": CACHE_DIR + "/JLPT_N1_Vocabulary/Row_Ka/",
            "sa": CACHE_DIR + "/JLPT_N1_Vocabulary/Row_Sa/",
            "ta": CACHE_DIR + "/JLPT_N1_Vocabulary/Row_Ta/",
            "na": CACHE_DIR + "/JLPT_N1_Vocabulary/Row_Na/",
            "ha": CACHE_DIR + "/JLPT_N1_Vocabulary/Row_Ha/",
            "ma": CACHE_DIR + "/JLPT_N1_Vocabulary/Row_Ma/",
            "ya": CACHE_DIR + "/JLPT_N1_Vocabulary/Row_Ya/",
            "ra": CACHE_DIR + "/JLPT_N1_Vocabulary/Row_Ra/",
            "wa": CACHE_DIR + "/JLPT_N1_Vocabulary/Row_Wa/",
        },
        "kanji": {
            "root": CACHE_DIR + "/JLPT_N1_Kanji/",
        },
        "grammar": {
            "root": CACHE_DIR + "/JLPT_N1_Grammar/",
        },
    },
}

SCRAPER_HEADER = {
    "user-agent": "TsukuruKezuruScraper/1.0 (contact: tuliog.projects@gmail.com)",
    "from": "https://github.com/julillermo/tsukuru",
}


GYOU_MISC_GROUPS: list[CJKMiscGroupType] = ["/misc", "misc"]
GYOU_GROUPS: list[CJKGyouGroupType] = [
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

CJK_GYOU_DICT: dict[CJKGyouGroupType, RomanjiGyouGroupType] = {
    "あ行": "a",
    "か行": "ka",
    "さ行": "sa",
    "た行": "ta",
    "な行": "na",
    "は行": "ha",
    "ま行": "ma",
    "や行": "ya",
    "ら行": "ra",
    "わ行": "wa",
}

DAN_GROUPS: list[CJKDanGroupType] = [
    "あ段",  # a-words
    "い段",  # i-words
    "う段",  # u-words
    "え段",  # e-words
    "お段",  # o-words
]

ROMANJI_DAN_DICT: dict[RomanjiDanGroupType, CJKDanGroupType] = {
    "a": "あ段",
    "i": "い段",
    "u": "う段",
    "e": "え段",
    "o": "お段",
}

CJK_ENGLISH_WORD_CLASS_DICT: dict[CJKWordClassKanjiType, EnglishWordClassType] = {
    "名": "noun",
    "代": "pronoun",
    "動I": "type I verb",
    "動II": "type II verb",
    "動III": "type III verb",
    "形": "adjective",
    "形動": "adjectival noun",
    "副": "adverb",
    "連体": "attribute",
    "接": "conjunction",
    "感": "interjection",
    "助動": "auxiliary",
    "助": "particle",
    "頭": "prefix",
    "尾": "suffix",
    "連": "compound",
}
