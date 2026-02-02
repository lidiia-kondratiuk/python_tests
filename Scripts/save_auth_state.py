import os
from pathlib import Path
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

EMAIL = os.getenv("TEST_EMAIL")
PASSWORD = os.getenv("TEST_PASSWORD")

assert EMAIL, "TEST_EMAIL is not set"
assert PASSWORD, "TEST_PASSWORD is not set"

AUTH_STATE_PATH = ROOT_DIR / "playwright/.auth/state.json"

def save_auth_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Login page
        page.goto("https://www.ministryoftesting.com/signin?return_to_referer=yes")

        page.wait_for_selector("#user_login")

        page.get_by_placeholder("Email or Username").fill(EMAIL)
        page.fill("#user_password", PASSWORD)
        page.get_by_role("button", name="Sign In").click()

        # ✅ КЛЮЧОВИЙ МОМЕНТ
        page.wait_for_selector(
            "div.alert.alert-success",
            timeout=15000
        )

        # (опційно, але красиво)
        assert page.locator("text=Signed in successfully").is_visible()

        # Save logged-in state
        context.storage_state(path=AUTH_STATE_PATH)

        browser.close()

if __name__ == "__main__":
    save_auth_state()
