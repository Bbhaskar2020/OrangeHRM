# tests/test_valid_login.py
import pytest
from pages.login_page import LoginPage
from utils.data_loader import get_login_scenario

data = get_login_scenario("valid_login")

@pytest.mark.valid
def test_valid_login(setup):
    page = setup
    login = LoginPage(page)
    login.open()
    login.enter_username(data["username"])
    login.enter_password(data["password"])
    login.click_login()
    # give page a moment to load; better to use wait_for_selector in real tests
    page.wait_for_timeout(1000)
    header = login.get_dashboard_header()
    assert data["expected"] in (header or ""), f"Expected dashboard header to contain '{data['expected']}'"
