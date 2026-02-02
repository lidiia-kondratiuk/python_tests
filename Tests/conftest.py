import pytest
from pathlib import Path

AUTH_STATE = Path("playwright/.auth/state.json")

@pytest.fixture
def logged_page(browser):
    if not AUTH_STATE.exists():
        raise RuntimeError(
            "Auth state file not found: playwright/.auth/state.json"
        )

    context = browser.new_context(
        storage_state=str(AUTH_STATE)
    )
    page = context.new_page()
    yield page
    context.close()

