import pytest
from playwright.sync_api import Page, expect

live_server_url = "http://127.0.0.1:4000"

routes = [
    ("about"),
    ("community"),
    ("conferences"),
    ("events"),
]


@pytest.mark.parametrize("url", routes)
def test_destination(
    page: Page,
    url: str,
) -> None:
    """Test that the destinations page loads with seeded data"""
    # Create a destination
    response = page.goto(f"{live_server_url}/{url}")
    page.on("response", lambda response: expect(response.status).to_equal(200))
    assert response.url.endswith(f"/{url}/")  # Load the index.html


@pytest.mark.parametrize(
    "title, url",
    (
        ("Acerca de", "/es/about/"),
        ("Inicio", "/es/"),
        ("Eventos", "/es/events/"),
        ("Comunidad", "/es/community/"),
        ("Conferencias", "/es/conferences/"),
    ),
)
def test_headers_in_language(page: Page, title: str, url: str) -> None:
    page.goto(live_server_url)
    lang = page.evaluate("document.documentElement.lang")
    assert lang == "en"
    page.get_by_label("Language").select_option("es")
    page.get_by_role("link", name=title).click()
    expect(page).to_have_url(f"{live_server_url}{url}")
    lang = page.evaluate("document.documentElement.lang")
    assert lang == "es"


def test_switching_lang_es_about(page: Page):
    about_path = "/about/"
    page.goto(f"{live_server_url}{about_path}")
    page.get_by_label("Language").select_option("es")
    # http://127.0.0.1:4000/es/about/
    expect(page).to_have_url(f"{live_server_url}/es{about_path}")


@pytest.mark.parametrize(
    "title, url",
    (
        ("Kutuhusu", "/sw/about/"),
        ("Nyumbani", "/sw/"),
        ("Matukio", "/sw/events/"),
        ("Jumuiya", "/sw/community/"),
        ("Mikutano", "/sw/conferences/"),
    ),
)
def test_headers_in_sw(page: Page, title: str, url: str) -> None:
    page.goto(live_server_url)
    lang = page.evaluate("document.documentElement.lang")
    assert lang == "en"
    page.get_by_label("Language").select_option("sw")
    page.get_by_role("link", name=title).click()
    expect(page).to_have_url(f"{live_server_url}{url}")
    lang = page.evaluate("document.documentElement.lang")
    assert lang == "sw"


def test_switching_lang_sw_about(page: Page):
    about_path = "/about/"
    page.goto(f"{live_server_url}{about_path}")
    page.get_by_label("Language").select_option("sw")
    # http://127.0.0.1:4000/sw/about/
    expect(page).to_have_url(f"{live_server_url}/sw{about_path}")
