def remove_parenthesis_plus(str_with_parenthesis: str) -> str:
    REMOVE_LIST = ["(", ")", " ", "\n"]
    # TODO: add unit test for this
    # Should generally work for the use case of this project.
    # - This has the limitation of not be able to tell whether the parenthesis wraps the text
    # - Also unable to tell whether the parenthesis comes in pairs
    rebuilt_str = ""
    for char in str_with_parenthesis:
        if char in REMOVE_LIST:
            continue
        else:
            rebuilt_str += char
    return rebuilt_str
