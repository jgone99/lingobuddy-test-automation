import pytest
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()

@pytest.fixture
def auth_page(browser):
    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()
    yield page
    page.close()
    context.close()

@pytest.fixture
def home_page(page):
    home = HomePage(page)
    home.navigate()
    return home

@pytest.fixture
def auth_home_page(auth_page):
    home = HomePage(auth_page)
    home.navigate()
    return home