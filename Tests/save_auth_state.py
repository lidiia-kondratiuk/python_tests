import os
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT_DIR = Path(__file__).resolve().parent.parent
AUTH_STATE_PATH = ROOT_DIR / "playwright/.auth/state.json"

EMAIL = os.getenv("TEST_EMAIL")
PASSWORD = os.getenv("TEST_PASSWORD")

def test_generate_auth_state():
    assert EMAIL, "TEST_EMAIL is not set"
    assert PASSWORD, "TEST_PASSWORD is not set"

    AUTH_STATE_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.ministryoftesting.com/signin?return_to_referer=yes")

        page.get_by_placeholder("Email or Username").fill(EMAIL)
        page.fill("#user_password", PASSWORD)
        page.get_by_role("button", name="Sign In").click()

        page.wait_for_selector(
            "div.alert.alert-success",
            timeout=15000
        )

        context.storage_state(path=str(AUTH_STATE_PATH))
        browser.close()
