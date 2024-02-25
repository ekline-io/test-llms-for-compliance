from goose3 import Goose

from log import logger
from app.utils.text_utils import text_clean_up


def extract_text_from_url(url):
    # Initialize Goose
    g = Goose()
    # Extract the article content from the webpage
    content = g.extract(url)
    # Clean the article text
    text = content.cleaned_text
    preprocessed_text = text_clean_up(text)
    # Log success message and return the preprocessed text
    logger.info(f"Extracted URL: {url}")
    return preprocessed_text
