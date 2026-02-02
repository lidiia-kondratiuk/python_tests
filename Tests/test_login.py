import os
from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()

EMAIL = os.getenv("TEST_EMAIL")
PASSWORD = os.getenv("TEST_PASSWORD")

assert EMAIL, "TEST_EMAIL is not set"
assert PASSWORD, "TEST_PASSWORD is not set"


def test_login_acceptance(page):
    page.goto("https://www.ministryoftesting.com/signin")

    page.wait_for_selector("input[type='email']", timeout=60000)

    page.fill("input[type='email']", EMAIL)
    page.fill("input[type='password']", PASSWORD)

    page.click("button[type='submit']")

    expect(page).not_to_have_url("**/signin")

