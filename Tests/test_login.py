import os
from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()

EMAIL = os.getenv("TEST_EMAIL")
PASSWORD = os.getenv("TEST_PASSWORD")

def test_login_acceptance(page):
    # 1. Відкриваємо сторінку логіну
    page.goto("https://www.ministryoftesting.com/signin?return_to_referer=yes")

    # 2. Чекаємо поле email / username
    page.wait_for_selector("#user_login")

    # 3. Заповнюємо email
    page.get_by_placeholder("Email or Username").fill(EMAIL)

    # 4. Заповнюємо пароль
    page.fill("#user_password", PASSWORD)

    # 5. Натискаємо кнопку Sign In
    page.get_by_role("button", name="Sign In").click()


