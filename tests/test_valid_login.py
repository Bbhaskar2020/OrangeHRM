# tests/test_valid_login.py
import pytest
from pages.login_page import LoginPage
from utils.data_loader import get_login_scenario
from locators.login_locators import LoginLocators

data = get_login_scenario("valid_login")

@pytest.mark.valid
def test_valid_login(setup):
    page = setup
    login = LoginPage(page)
    login.open()
    login.enter_username(data["username"])
    login.enter_password(data["password"])
    login.click_login()

    # Wait explicitly for dashboard header
    login.wait_for_element(LoginLocators.DASHBOARD_HEADER, timeout=7000)
    header = login.get_dashboard_header()

    assert data["expected"] in (header or ""), f"Expected dashboard header to contain '{data['expected']}'"
