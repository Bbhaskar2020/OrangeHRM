# conftest.py
import os
import datetime
import pytest
from playwright.sync_api import sync_playwright

# -- Playwright session-level context (one browser for session)
@pytest.fixture(scope="session")
def playwright_context():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=True)  # change to False while debugging
    context = browser.new_context()
    yield context
    context.close()
    browser.close()
    p.stop()

# -- page fixture (fresh page per test)
@pytest.fixture(scope="function")
def page(playwright_context):
    page = playwright_context.new_page()
    yield page
    page.close()

# -- compatibility alias
@pytest.fixture
def setup(page):
    """Alias fixture named 'setup' for backward compatibility with older tests."""
    return page

# pytest-html integration: expose plugin reference
def pytest_configure(config):
    global _pytest_html
    _pytest_html = config.pluginmanager.getplugin("html")

# Hook to populate report attributes (rep_setup, rep_call, rep_teardown)
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

# Auto screenshot on failure and attach to pytest-html
@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page, extra):
    """
    Automatically runs for every test. After test completes, if test failed (rep_call.failed),
    capture a screenshot and append to pytest-html extras.
    """
    yield
    # after test
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshots_dir = os.path.join(os.getcwd(), "reports", "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{request.node.name}_{timestamp}.png"
        file_path = os.path.join(screenshots_dir, filename)
        try:
            page.screenshot(path=file_path, full_page=True)
        except Exception:
            # fallback: try without full_page
            page.screenshot(path=file_path)
        # Attach image to pytest-html report using the provided 'extra' fixture
        try:
            extra.append(_pytest_html.extras.image(file_path))
        except Exception:
            # if pytest-html not available or other error, just print path
            print(f"[INFO] Screenshot saved: {file_path}")
