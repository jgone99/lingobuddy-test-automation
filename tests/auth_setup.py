from pages.login_page import LoginPage
from config import HOMEPAGE_URL, TEST_EMAIL, TEST_PASSWORD
from playwright.sync_api import Page

def test_login(page: Page):
    login = LoginPage(page)
    login.navigate()
    login.login(TEST_EMAIL, TEST_PASSWORD)
    page.wait_for_url(HOMEPAGE_URL)
    page.context.storage_state(path="auth.json")