from playwright.sync_api import expect

from Tests.conftest import logged_page
from pathlib import Path
import re

def test_create_new_memory(logged_page):
    logged_page.goto("https://www.ministryoftesting.com/memories/new")
    logged_page.wait_for_selector("#memory_content_title")
    title = "Hello, it is my new memory"
    logged_page.locator("#memory_content_title").fill(title)
    logged_page.locator("#memory_content_commentary").fill(
        "It is my test commentary for the new memory"
    )
    logged_page.locator("#memory_content_description").fill(
        "Test text for the description")

    contributor = logged_page.get_by_role(
        "textbox", name="Who is in this memory?"
    )
    contributor.fill("Lul")
    logged_page.keyboard.press("ArrowDown")
    logged_page.keyboard.press("Enter")
    tags = logged_page.get_by_role("textbox", name="Tags *")
    tags.fill("test-tag")
    logged_page.keyboard.press("Enter")
    expect(
        logged_page.locator("#memory_content_title")
    ).to_have_value(title)
    logged_page.locator("#memory_content_image")
    file_path = Path(__file__).resolve().parents[2] / "assets" / "images.png"
    assert file_path.exists(), f"Test file not found: {file_path}"

    file_input = logged_page.locator("#memory_content_image")
    file_input.set_input_files(str(file_path))

    expect(file_input).to_have_value(
        re.compile(r".*images\.png")
    )
    logged_page.get_by_role("button", name="Save").click()
    expect(logged_page).to_have_url("https://www.ministryoftesting.com/memories/new")

