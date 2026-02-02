import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

EMAIL = os.getenv("TEST_EMAIL")
PASSWORD = os.getenv("TEST_PASSWORD")

if not EMAIL or not PASSWORD:
    raise RuntimeError("TEST_EMAIL or TEST_PASSWORD is not set")


def save_auth_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # 🔐 UI login (копія з acceptance)
        page.goto("https://www.ministryoftesting.com/signin")
        page.wait_for_selector("input[type='email']", timeout=60000)

        page.fill("input[type='email']", EMAIL)
        page.fill("input[type='password']", PASSWORD)
        page.click("button[type='submit']")

        page.wait_for_timeout(3000)

        if "signin" in page.url:
            raise RuntimeError("Login failed")

        # 💾 Зберігаємо стан
        context.storage_state(path="auth_state.json")

        browser.close()


if __name__ == "__main__":
    save_auth_state()
