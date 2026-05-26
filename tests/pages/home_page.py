from config import BASE_URL
from playwright.sync_api import Page

class HomePage:
    URL = BASE_URL

    def __init__(self, page: Page):
        self.page = page
        self.translate_input = page.get_by_placeholder("Translate Spanish or English")
        self.translate_button = page.get_by_role("button", name="Translate")
        self.translate_result = page.locator("div.bg-gray-100 p")

    def navigate(self):
        self.page.goto(self.URL)

    def translate_word(self, word: str):
        self.translate_input.fill(word)
        self.translate_button.click()
        self.translate_result.wait_for()
        return self.translate_result.text_content()