from lang_component.vocab import scrape_vocab
from utils.file import get_path_of_latest_file
from utils.types import JLPTLevel


def main():
    print("Hello from kezuru!\n")

    # optoinal for testing
    vocab_file_path = get_path_of_latest_file("./.cache/n5/vocab")

    jlpt_level: JLPTLevel = "n5"

    scrape_vocab(
        vocab_file_path=vocab_file_path if vocab_file_path is not None else None,
        level=jlpt_level,
        delay=1,
    )


if __name__ == "__main__":
    main()
