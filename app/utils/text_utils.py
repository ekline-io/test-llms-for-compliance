import re
from unidecode import unidecode
from bs4 import BeautifulSoup
from app.utils.constants import escape_sequences_list


def text_clean_up(text_):
    text = text_ if text_ is not None else ""

    # removing domain names from text
    regex = (
        r"(?:(http|https|ftp|ftps)?(\:\/\/)?(www)?([a-zA-Z0-9\-\.]+\.)"
        r"(com|org|edu|co|cms|in|uk|en|news|net|info|gov)(\/\S*)?)"
    )
    text = re.sub(regex, "", text)

    # removing unnecessary white spaces, and converting non-ascii to ascii characters using unidecode
    text = re.sub(r"(\[\s*[^\]]*\s*\])", "", unidecode(text))

    # replacing with octal characters
    text = re.sub(
        r'([a-z0-9]|\]|\)|\}|"|\')(\.\s*|\.\n*)([A-Z]|\{|\[|\(|")', r"\1. \3", text
    )

    # for removing HTML tags
    text = BeautifulSoup(text, features="html.parser").text

    # for removing duplicate & consecutive escape sequences
    for escape_seq in escape_sequences_list:
        text = re.sub(f"{escape_seq}{escape_seq}+", f"{escape_seq}", text)

    return text
