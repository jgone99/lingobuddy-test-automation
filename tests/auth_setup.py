from pages.login_page import LoginPage
from config import BASE_URL, TEST_EMAIL, TEST_PASSWORD

def test_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login(TEST_EMAIL, TEST_PASSWORD)
    page.wait_for_url(f"{BASE_URL}/home-page")
    page.context.storage_state(path="auth.json")