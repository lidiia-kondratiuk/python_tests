import os

EMAIL = os.getenv("TEST_EMAIL")
PASSWORD = os.getenv("TEST_PASSWORD")

def test_login_ui(page):
    assert EMAIL is not None
    assert PASSWORD is not None

    page.goto("https://www.ministryoftesting.com/signin")
    page.fill("input[name='user[email]']", EMAIL)
    page.fill("input[name='user[password]']", PASSWORD)
    page.click("button[type='submit']")
