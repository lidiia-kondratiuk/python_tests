import pytest
import os
URL = os.getenv("URL")
def test_home_page_access(page):
    page.goto(URL)
    heading = page.get_by_role("heading", name="Welcome to the MoTaverse")
    assert heading.is_visible()

#Verify that nav items are present at home page
@pytest.mark.parametrize(
    "nav_bar",
    [
        "Learn",
        "Events",
        "Insights",
        "Certs",
        "Observatory",
        "Memories",
        "Join"
    ]
)
def test_navigation_items_availability(nav_bar, page):
    page.goto(URL)
    nav_item = page.locator("header").get_by_role("link", name=nav_bar, exact=True)
    assert nav_item.is_visible()

#Check search input in header
def test_serch_as_nav_items(page):
    page.goto(URL)
    search = page.get_by_placeholder("Search...")
    assert search.is_visible()

#Check sign in link in header
def test_signIn_availability_at_header(page):
    page.goto(URL)
    signIn = page.get_by_role("link", name="Sign In")
    assert signIn.is_visible()

def test_check_create_button_availability(page):
    page.goto(URL)
    create_button = page.get_by_role("button", name=" Create")
    assert create_button.is_visible()

