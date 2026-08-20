import string

ENGLISH_SET = set(string.ascii_letters) | {'"', "'"}


def split_example_cjk_english_sentence(sentence: str) -> tuple[str, str]:
    sentence_chunks = sentence.replace("Example: ", "").split(" ")
    temp_2nd_half = " ".join(sentence_chunks[1:]).strip()

    cjk_sentence = sentence_chunks[0].strip()
    english_sentence = ""

    for idx, char in enumerate(temp_2nd_half):
        if char not in ENGLISH_SET or (char == " "):
            cjk_sentence += char
        else:
            english_sentence = temp_2nd_half[idx:].replace("' '", '"')
            break

    return (cjk_sentence.strip(), english_sentence.strip())
