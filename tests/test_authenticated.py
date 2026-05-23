import pytest
from config import (
    BASE_URL,
    COURSE_LIST_URL,
    CHATBOT_URL,
    SNOWMAN_URL,
    MATCHING_URL,
    SIGN_IN_URL
)

PROTECTED_URLS = [
    COURSE_LIST_URL,
    CHATBOT_URL,
    SNOWMAN_URL,
    MATCHING_URL
]

@pytest.mark.parametrize("url", PROTECTED_URLS)
def test_protected_routes_redirect_when_logged_out(page, url):
    page.goto(url)
    page.wait_for_url(f"{SIGN_IN_URL}**")
    assert page.url.startswith(SIGN_IN_URL), f"Expected redirect to sign-in, got {page.url}"

@pytest.mark.parametrize("url", PROTECTED_URLS)
def test_routes_accessible_when_logged_in(auth_page, url):
    auth_page.goto(url)
    assert auth_page.url.startswith(url), f"Expected to stay on {url}, got {auth_page.url}"