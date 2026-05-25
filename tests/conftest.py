import pytest
import psycopg2
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.snowman_page import SnowmanPage
from config import TEST_DATABASE_URL

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
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

@pytest.fixture
def snowman_page(auth_page):
    snowman = SnowmanPage(auth_page)
    snowman.navigate()
    return snowman

@pytest.fixture
def db():
    conn = psycopg2.connect(TEST_DATABASE_URL)
    conn.autocommit = False
    cursor = conn.cursor()
    yield cursor
    cursor.close()
    conn.rollback()
    conn.close()