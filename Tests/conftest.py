import pytest
from pathlib import Path

AUTH_STATE = Path("playwright/.auth/state.json")

@pytest.fixture
def logged_page(browser):
    context = browser.new_context(
        storage_state=AUTH_STATE
    )
    page = context.new_page()

    yield page

    page.close()
    context.close()
