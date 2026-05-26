import pytest
from playwright.sync_api import Page
from pages.nav_bar import Navbar
from pages.login_page import LoginPage
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

@pytest.mark.ui
@pytest.mark.auth
@pytest.mark.parametrize("url", PROTECTED_URLS)
def test_protected_routes_redirect_when_logged_out(page: Page, url: str):
    page.goto(url)
    login = LoginPage(page)
    login.wait_for_load()
    assert page.url.startswith(SIGN_IN_URL), f"Expected redirect to sign-in, got {page.url}"

@pytest.mark.ui
@pytest.mark.auth
@pytest.mark.parametrize("url", PROTECTED_URLS)
def test_routes_accessible_when_logged_in(auth_page: Page, url: str):
    auth_page.goto(url)
    nav = Navbar(auth_page)
    nav.wait_for_authentication()
    assert auth_page.url.startswith(url), f"Expected to stay on {url}, got {auth_page.url}"