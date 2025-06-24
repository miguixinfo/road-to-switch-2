import unicodedata

def normalize_text(text):
    """
    Normalize the input text by removing diacritical marks and converting it to lowercase.

    This function uses Unicode normalization to decompose characters into their base characters
    and combining characters. It then filters out the combining characters (diacritical marks)
    and returns the cleaned text in lowercase.

    Args:
        text (str): The input string to be normalized.

    Returns:
        str: The normalized string with diacritical marks removed and in lowercase.
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    ).lower()