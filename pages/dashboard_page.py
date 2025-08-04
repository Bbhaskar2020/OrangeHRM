class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.dashboard_header = page.locator("h6.oxd-topbar-header-breadcrumb-module")

    def is_dashboard_displayed(self):
        return self.dashboard_header.is_visible() and self.dashboard_header.inner_text() == "Dashboard"
