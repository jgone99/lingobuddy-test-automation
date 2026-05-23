from config import BASE_URL

class LoginPage:
    URL = f"{BASE_URL}/sign-in"

    def __init__(self, page):
        self.page = page
        self.email_input = page.locator("#identifier-field")
        self.password_input = page.locator("#password-field")
        self.continue_button = page.get_by_role("button", name="Continue", exact=True)

    def navigate(self):
        self.page.goto(self.URL)

    def login(self, email, password):
        self.email_input.fill(email)
        self.continue_button.click()
        self.password_input.wait_for()
        self.password_input.fill(password)
        self.continue_button.click()
