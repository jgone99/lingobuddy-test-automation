from config import SNOWMAN_URL
from playwright.sync_api import Page, expect

class SnowmanPage:
    URL = SNOWMAN_URL

    def __init__(self, page: Page):
        self.page = page
        self.untranslated_word = page.locator("div.word-sign > div")
        self.modal_continue_button = page.get_by_role("button", name="Continue")
        self.modal_try_again_button = page.get_by_role("button", name="Try Again")
        self.current_score = page.locator("div.score-sign > div.small-sign-box")

    def navigate(self):
        self.page.goto(self.URL)

    def get_word(self):
        return self.untranslated_word.inner_text().lower()
    
    def get_current_score(self):
        return int(self.current_score.inner_text()[7:])
    
    def wait_for_score_update(self, previous_score: int):
        expect(self.current_score).not_to_have_text(f"Score: {previous_score}")

    def input_word(self, translated_word: str):
        # used a set to avoid clicking duplicate letters
        letters = set(translated_word)
        for letter in letters:
            self.page.locator(f"button.alpha-button.games-button[value=\"{letter.lower()}\"]").click()

    def click_continue(self):
        self.modal_continue_button.click()
        
    def click_try_again(self):
        self.modal_try_again_button.click()