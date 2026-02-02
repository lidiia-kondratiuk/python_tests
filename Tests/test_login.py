import pytest
import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

# 1️⃣ Завантажуємо .env
load_dotenv()

# 2️⃣ Забираємо змінні
EMAIL = os.getenv("TEST_EMAIL")
PASSWORD = os.getenv("TEST_PASSWORD")

# 3️⃣ Захист від помилок конфігурації
if not EMAIL or not PASSWORD:
    raise RuntimeError("TEST_EMAIL or TEST_PASSWORD is not set in .env")

def test_login_and_save_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.ministryoftesting.com/signin")

        page.get_by_label("Email").fill(EMAIL)
        page.get_by_label("Password").fill(PASSWORD)
        page.get_by_role("button", name="Sign in").click()

        page.wait_for_url("**/")

        context.storage_state(path="storage_state.json")
        browser.close()
