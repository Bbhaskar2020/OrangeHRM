# pages/base_page.py
from playwright.sync_api import Page, TimeoutError

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url: str):
        """Navigate to a given URL and wait until page load."""
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    def wait_for_element(self, selector: str, timeout: int = 5000):
        """Wait until selector is visible within timeout."""
        try:
            self.page.wait_for_selector(selector, timeout=timeout, state="visible")
        except TimeoutError:
            raise AssertionError(f"Element not visible after {timeout} ms: {selector}")

    def click(self, selector: str, timeout: int = 5000):
        """Wait for and click an element."""
        self.wait_for_element(selector, timeout)
        self.page.click(selector)

    def fill(self, selector: str, value: str, timeout: int = 5000):
        """Wait for and fill a field."""
        self.wait_for_element(selector, timeout)
        self.page.fill(selector, value)

    def get_text(self, selector: str, timeout: int = 5000) -> str:
        """Wait for and return the element text."""
        self.wait_for_element(selector, timeout)
        return self.page.text_content(selector)

    def is_visible(self, selector: str, timeout: int = 3000) -> bool:
        """Return True if element becomes visible within timeout."""
        try:
            self.page.wait_for_selector(selector, timeout=timeout, state="visible")
            return True
        except TimeoutError:
            return False

    def take_screenshot(self, file_path: str):
        """Capture a screenshot manually (if needed)."""
        self.page.screenshot(path=file_path, full_page=True)
