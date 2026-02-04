import os
from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()

EMAIL = os.getenv("TEST_EMAIL")
PASSWORD = os.getenv("TEST_PASSWORD")

def test_login_acceptance(page):
    page.goto("https://www.ministryoftesting.com/signin?return_to_referer=yes")
    page.wait_for_selector("#user_login")
    page.get_by_placeholder("Email or Username").fill(EMAIL)
    page.fill("#user_password", PASSWORD)
    page.get_by_role("button", name="Sign In").click()


