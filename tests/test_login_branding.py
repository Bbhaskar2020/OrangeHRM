# tests/test_login_branding.py
import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_login_branding_visible(setup):
    page = setup
    login = LoginPage(page)
    login.open()
    assert login.is_branding_visible(), "Branding image not visible on login page"
