import pytest
from playwright.sync_api import Page
from pages.nav_bar import Navbar

from config import (
    COURSE_LIST_URL,
    CHATBOT_URL,
    SNOWMAN_URL,
    MATCHING_URL,
    HOMEPAGE_URL
)

PROTECTED_URLS = [
    COURSE_LIST_URL,
    CHATBOT_URL,
    SNOWMAN_URL,
    MATCHING_URL
]

@pytest.mark.ui
@pytest.mark.auth
@pytest.mark.parametrize("url", PROTECTED_URLS)
def test_logout_from_protected_routes_redirects_to_homepage(fresh_auth_page: Page, url: str):
    fresh_auth_page.goto(url)
    fresh_auth_page.wait_for_url(url)
    print(fresh_auth_page.url)
    nav = Navbar(fresh_auth_page)
    nav.logout()
    fresh_auth_page.wait_for_url(f"{HOMEPAGE_URL}**")
    assert fresh_auth_page.url.startswith(HOMEPAGE_URL)