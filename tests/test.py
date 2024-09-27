import pytest
from playwright.sync_api import Page, expect

from _conferences.__main__ import parse_conference_details

live_server_url = "http://127.0.0.1:4000"

routes = [
    ("blog"),
    ("about"),
    ("events"),
    ("community"),
    ("leadership"),
]


@pytest.mark.parametrize("url", routes)
def test_destination(
    page: Page,
    url: str,
) -> None:
    """Test that the destinations page loads with seeded data"""
    # Create a destination
    response = page.goto(f"{live_server_url}/{url}")

    assert response.status == 200  # Check that the page loaded successfully
    assert response.url.endswith(f"/{url}/")  # Load the index.html


@pytest.mark.parametrize(
    "title, url",
    (
        ("Acerca de", "/es/about/"),
        ("Inicio", "/es/"),
        ("Eventos", "/es/events/"),
        ("Comunidad", "/es/community/"),
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


def test_switching_lang_es_about(page: Page) -> None:
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


def test_switching_lang_sw_about(page: Page) -> None:
    about_path = "/about/"
    page.goto(f"{live_server_url}{about_path}")
    page.get_by_label("Language").select_option("sw")
    # http://127.0.0.1:4000/sw/about/
    expect(page).to_have_url(f"{live_server_url}/sw{about_path}")


@pytest.mark.parametrize(
    "title, url",
    (
        ("Black Python Devs | Home", "/"),
        ("Black Python Devs | Blog", "/blog"),
        ("Black Python Devs | About Us", "/about/"),
        ("Black Python Devs | Events", "/events/"),
        ("Black Python Devs | Community", "/community/"),
    ),
)
def test_bpdevs_title_en(page: Page, title: str, url: str) -> None:
    page.goto(f"{live_server_url}/{url}")
    expect(page).to_have_title(title)


def test_mailto_bpdevs(page: Page) -> None:
    page.goto(f"{live_server_url}")
    mailto = page.get_by_role("link", name="email")
    expect(mailto).to_have_attribute("href", "mailto:contact@blackpythondevs.com")


def test_conference_parsing_valid_url():
    example_conf_issue = """### Conference Name

Test Conference Title

### URL

https://microsoft.com

### Conference Dates

10 - 15 Sep 2050

### Conference Type

both

### Conference Location

Redmond, WA, USA

### Summary

Test Conference Summary

### Speaking

* [Satya Nadella](https://www.linkedin.com/in/satyanadella/)
"""
    expected_name = "Test Conference Title"
    expected_url = "https://microsoft.com"
    parsed_conf = parse_conference_details(issue_body=example_conf_issue)

    assert parsed_conf["name"] == expected_name
    assert parsed_conf["url"] == expected_url


def test_conference_parsing_logic_no_url_scheme():
    example_conf_issue = """### Conference Name

Test Conference Title

### URL

microsoft.com

### Conference Dates

10 - 15 Sep 2050

### Conference Type

both

### Conference Location

Redmond, WA, USA

### Summary

Test Conference Summary

### Speaking

* [Satya Nadella](https://www.linkedin.com/in/satyanadella/)
"""
    expected_name = "Test Conference Title"
    expected_url = "https://microsoft.com"
    parsed_conf = parse_conference_details(issue_body=example_conf_issue)

    assert parsed_conf["name"] == expected_name
    assert parsed_conf["url"] == expected_url


def test_conference_parsing_logic_no_url():
    example_conf_issue = """### Conference Name

Test Conference Title

### URL


### Conference Dates

10 - 15 Sep 2050

### Conference Type

both

### Conference Location

Redmond, WA, USA

### Summary

Test Conference Summary

### Speaking

* [Satya Nadella](https://www.linkedin.com/in/satyanadella/)
"""
    expected_name = "Test Conference Title"
    expected_url = None
    parsed_conf = parse_conference_details(issue_body=example_conf_issue)

    assert parsed_conf["name"] == expected_name
    assert parsed_conf["url"] == expected_url
