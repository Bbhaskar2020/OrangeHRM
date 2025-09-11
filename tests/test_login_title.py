# tests/test_login_title.py
import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_login_page_title(setup):
    page = setup
    login = LoginPage(page)
    login.open()
    actual = login.get_title()
    expected = "OrangeHRM"
    assert actual == expected, f"Expected title '{expected}', got '{actual}'"
