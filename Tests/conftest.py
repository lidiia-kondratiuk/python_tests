import os
import pytest

@pytest.fixture(scope="session")
def logged_page(browser):
    context = browser.new_context()
    page = context.new_page()

    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    page.goto("https://www.ministryoftesting.com/signin")
    page.fill("input[name='user[email]']", email)
    page.fill("input[name='user[password]']", password)
    page.click("button[type='submit']")

    page.wait_for_url("**/memories**")

    yield page
    context.close()
