import pytest
from playwright.sync_api import Browser


@pytest.fixture
def logged_page(browser: Browser):
    context = browser.new_context(
        storage_state="auth_state.json"
    )
    page = context.new_page()

    yield page

    context.close()
