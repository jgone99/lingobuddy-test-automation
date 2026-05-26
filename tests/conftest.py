import pytest
import psycopg2
from playwright.sync_api import (
    sync_playwright,
    Page,
    Browser
)
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.snowman_page import SnowmanPage
from config import (
    TEST_DATABASE_URL,
    TEST_USER_ID,
    TEST_EMAIL,
    TEST_PASSWORD,
    HOMEPAGE_URL,
    HEADLESS
)

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        yield browser
        browser.close()

@pytest.fixture
def page(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()

@pytest.fixture
def auth_page(browser: Browser):
    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()
    yield page
    page.close()
    context.close()

@pytest.fixture
def home_page(page: Page):
    home = HomePage(page)
    home.navigate()
    return home

@pytest.fixture
def auth_home_page(auth_page: Page):
    home = HomePage(auth_page)
    home.navigate()
    return home

@pytest.fixture
def snowman_page(auth_page: Page):
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

@pytest.fixture
def reset_snowman_progress(db: psycopg2.extensions.cursor):
    db.execute("UPDATE progress SET snowman_highscore = 0 WHERE user_id = %s", (TEST_USER_ID,))
    db.connection.commit()
    yield
    db.execute("UPDATE progress SET snowman_highscore = 0 WHERE user_id = %s", (TEST_USER_ID,))
    db.connection.commit()

# auth.json is invalidated after logout so I create their own session when a logout is required
# instead of loading from storageState
@pytest.fixture
def fresh_auth_page(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    login = LoginPage(page)
    login.navigate()
    login.login(TEST_EMAIL, TEST_PASSWORD)
    page.wait_for_url(HOMEPAGE_URL)
    yield page
    page.close()
    context.close()