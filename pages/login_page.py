# pages/login_page.py
from pages.base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def open(self, url: str = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"):
        self.open_url(url)

    def enter_username(self, username: str):
        self.fill(LoginLocators.USERNAME, username)

    def enter_password(self, password: str):
        self.fill(LoginLocators.PASSWORD, password)

    def click_login(self):
        self.click(LoginLocators.LOGIN_BUTTON)

    def get_dashboard_header(self) -> str:
        return self.get_text(LoginLocators.DASHBOARD_HEADER)

    def get_error_message(self) -> str:
        try:
            return self.get_text(LoginLocators.ERROR_MESSAGE)
        except AssertionError:
            return None

    def is_branding_visible(self) -> bool:
        return self.is_visible(LoginLocators.BRANDING_IMAGE)

    def get_title(self) -> str:
        return self.page.title()
