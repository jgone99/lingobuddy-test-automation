from playwright.sync_api import Page, expect

class Navbar:
    
    def __init__(self, page: Page):
        self.page = page
        self.user_button = page.locator("button.cl-userButtonTrigger")
        self.logout_button = page.locator("button.cl-userButtonPopoverActionButton__signOut")

    def wait_for_authentication(self):
        return expect(self.user_button).to_be_visible()

    def logout(self):
        self.user_button.click()
        self.logout_button.wait_for()
        self.logout_button.click()