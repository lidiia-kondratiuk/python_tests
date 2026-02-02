import pytest

@pytest.fixture(scope="function")
def logged_page(browser):
    context = browser.new_context(
        storage_state="storage_state.json",
        base_url="https://www.ministryoftesting.com",
    )
    page = context.new_page()
    yield page
    context.close()
