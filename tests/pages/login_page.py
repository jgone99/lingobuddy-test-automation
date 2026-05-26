from config import SIGN_IN_URL
from playwright.sync_api import Page, expect

class LoginPage:
    URL = SIGN_IN_URL

    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("#identifier-field")
        self.password_input = page.locator("#password-field")
        self.continue_button = page.get_by_role("button", name="Continue", exact=True)

    def navigate(self):
        self.page.goto(self.URL)

    def wait_for_load(self):
        expect(self.email_input).to_be_visible()

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.continue_button.click()
        self.password_input.wait_for()
        self.password_input.fill(password)
        self.continue_button.click()
