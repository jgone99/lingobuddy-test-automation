from pages.login_page import LoginPage
from config import HOMEPAGE_URL, TEST_EMAIL, TEST_PASSWORD

def test_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login(TEST_EMAIL, TEST_PASSWORD)
    page.wait_for_url(HOMEPAGE_URL)
    page.context.storage_state(path="auth.json")