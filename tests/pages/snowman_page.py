from config import SNOWMAN_URL
from playwright.sync_api import Page, expect
from psycopg2.extensions import cursor as _cursor
from helpers import (
    get_translation
)

class SnowmanPage:
    URL = SNOWMAN_URL
    SCORE_PREFIX = "Score: "
    RECORD_PREFIX = "Record: "

    def __init__(self, page: Page):
        self.page = page
        self.untranslated_word = page.locator("div.word-sign > div")
        self.modal_continue_button = page.get_by_role("button", name="Continue")
        self.modal_try_again_button = page.get_by_role("button", name="Try Again")
        self.current_score = page.locator("div.score-sign > div.small-sign-box")
        self.high_score = page.locator("div.record-sign > div.small-sign-box")

    def navigate(self):
        self.page.goto(self.URL)

    def get_word(self):
        return self.untranslated_word.inner_text().lower()
    
    def get_current_score(self):
        return int(self.current_score.inner_text()[len(self.SCORE_PREFIX):])

    def get_high_score(self):
        return int(self.high_score.inner_text()[len(self.RECORD_PREFIX):])
    
    def wait_for_current_score_update(self, previous_score: int):
        expect(self.current_score).not_to_have_text(f"{self.SCORE_PREFIX}{previous_score}")

    def wait_for_high_score_update(self, previous_score: int):
        expect(self.high_score).not_to_have_text(f"{self.RECORD_PREFIX}{previous_score}")

    def input_word(self, translated_word: str):
        # used a set to avoid clicking duplicate letters
        letters = set(translated_word)
        for letter in letters:
            self.page.locator(f"button.alpha-button.games-button[value=\"{letter.lower()}\"]").click()

    def click_continue(self):
        self.modal_continue_button.click()
        
    def click_try_again(self):
        self.modal_try_again_button.click()

    def answer_correctly(self, db: _cursor):
        word = self.get_word()
        translated_word = get_translation(db, word)
        self.input_word(translated_word)
        self.click_continue()

    def answer_incorrectly(self, db: _cursor):
        alpha = set("abcdefghijklmnopqrstuvwxyz")
        word = self.get_word()
        translated_word = get_translation(db, word)
        alpha = alpha.difference(set(translated_word))
        wrong_word =  "".join(list(alpha)[:4])
        self.input_word(wrong_word)
        self.click_continue()