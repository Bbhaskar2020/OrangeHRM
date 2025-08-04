import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_valid_login(page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.navigate()
    login_page.login("Admin", "admin123")

    assert dashboard_page.is_dashboard_displayed()
