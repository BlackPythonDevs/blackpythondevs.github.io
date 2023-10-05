import re

import pytest
from playwright.sync_api import Page, expect


live_server_url = "https://blackpythondevs.github.io"

routes = [
    ("about.html"),
    ("community.html"),
    ("conferences.html"),
    ("events.html"),
]

@pytest.mark.parametrize("url", routes)
def test_destination_options(
    page: Page,
    url: str,
):
    """Test that the destinations page loads with seeded data"""
    # Create a destination
    page.goto(f"{live_server_url}/{url}")
    page.on("response", lambda response: expect(response.status).to_equal(200))

@pytest.mark.parametrize("url", routes)
def test_destination_(
    page: Page,
    url: str,
) -> None:
    """Test that the destinations page loads with seeded data"""
    # Create a destination
    page.goto(f"{live_server_url}/{url}")
    page.on("response", lambda response: expect(response.status).to_equal(200))

@pytest.mark.parametrize(
        "title, url", 
        ("Acerca de", '/es/about.html'),
        ("Inicio", "/es"),
        ("Eventos", "/es/events.html"),
        ("Comunidad", "/es/community.html"),
        ("Conferencias", "/es/conferences.html")
        )
def test_headers_in_language(page: Page, title:str, url:str) -> None:
    page.goto("https://blackpythondevs.github.io/")
    page.get_by_label("Language").select_option("es")
    page.get_by_role("link", name=title).click()
    expect(page).to_have_url(f"https://blackpythondevs.github.io{url}")
