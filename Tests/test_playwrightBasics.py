import time
from pydoc import visiblename

from playwright.sync_api import Page, expect


# def test_playwrightBasics (playwright):
#     browser=playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.tally.xyz/explore")

def test_playwrightShortCut(page:Page):
    page.goto("https://www.ministryoftesting.com/")
    page.goto("https://www.ministryoftesting.com/signin?return_to_referer=yes")
    page.get_by_label("Email or Username").fill("lidiiakondratiukliko@gmail.com")
    time.sleep(1)
    page.get_by_label("Password").fill("Lilili@333")
    page.get_by_role("button", name="Sign In").click()

    #Verify success alert
    page.get_by_role("alert").get_by_text("Signed in successfully")
    page.get_by_role("alert").get_by_role("button", name="Close").click()
    page.goto("https://www.ministryoftesting.com/")

    #Open Create dropdown
    page.get_by_role("button", name="Create").click()
    dropdown = page.locator("ul.dropdown-menu.show")
    options = ["Memory", "Meme", "Satellite", "Job"]
    for option in options:
        expect(dropdown.get_by_text(option)).to_be_visible()
    # Adding a new Memory
    page.get_by_role("button", name="Memory").click()
    page.get_by_label("Title").fill("Hello, it is my new memory")
    expect(page.get_by_label("Commentary")).to_be_visible()
    page.get_by_label("Commentary").fill("It is my test commentary for the new memory")
    page.get_by_text("Is there a story behind this memory? Is there any additional context for it?").is_visible()
    page.get_by_label("Alt text").fill("Test text for the description")

    # Activate contributor search
    search_input = page.get_by_role(
        "textbox",
        name="Who is in this memory?"
    )

    expect(search_input).to_be_visible()
    search_input.fill("Lul")

    # user-like selection
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")
    page.get_by_label("Tags ")













