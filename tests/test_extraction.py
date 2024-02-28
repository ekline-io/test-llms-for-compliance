import pytest

from app.extraction.extract_webpage import extract_text_from_url


@pytest.mark.parametrize("url", ["https://www.joinguava.com/", "https://stripe.com/docs/treasury/marketing-treasury", "https://www.seiright.com/"])
def test_extract_text_from_url(url):

    result = extract_text_from_url(url)
    assert result is not None
    assert len(result) > 0
    assert isinstance(result, str)

