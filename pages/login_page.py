# pages/login_page.py
from playwright.sync_api import Page
from locators.login_locators import LoginLocators

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"):
        self.page.goto(url)

    def enter_username(self, username: str):
        self.page.fill(LoginLocators.USERNAME, username)

    def enter_password(self, password: str):
        self.page.fill(LoginLocators.PASSWORD, password)

    def click_login(self):
        self.page.click(LoginLocators.LOGIN_BUTTON)

    def get_dashboard_header(self) -> str:
        return self.page.text_content(LoginLocators.DASHBOARD_HEADER)

    def get_error_message(self) -> str:
        # may return None if not present
        return self.page.text_content(LoginLocators.ERROR_MESSAGE)

    def is_branding_visible(self) -> bool:
        return self.page.is_visible(LoginLocators.BRANDING_IMAGE)

    def get_title(self) -> str:
        return self.page.title()
