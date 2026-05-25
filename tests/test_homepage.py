import pytest

@pytest.mark.ui
@pytest.mark.api
def test_translate_english_to_spanish(home_page):
    result = home_page.translate_word("library")
    assert result == "biblioteca"

@pytest.mark.ui
@pytest.mark.api
def test_translate_spanish_to_english(home_page):
    result = home_page.translate_word("biblioteca")
    assert result == "library"