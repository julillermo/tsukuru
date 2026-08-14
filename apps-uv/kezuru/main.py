from lang_component.vocab import scrape_row_a_temp, scrape_vocab
from utils.file import get_path_of_latest_file
from utils.types import JLPTLevelType


def main():
    print("Hello from kezuru!\n")

    # # optional for testing
    vocab_file_path = get_path_of_latest_file("./.cache/n5/vocab")
    jlpt_level: JLPTLevelType = "n5"

    scrape_vocab(
        vocab_file_path=vocab_file_path,
        level=jlpt_level,
        delay_seconds=1,
    )

    # scrape_row_a_temp()


if __name__ == "__main__":
    main()
