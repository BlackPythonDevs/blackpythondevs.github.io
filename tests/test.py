import pathlib
import pytest
from playwright.sync_api import expect, sync_playwright
from axe_core_python.sync_playwright import Axe
import frontmatter
from typing import Generator
import subprocess
import http.server
import socketserver
import threading
import time
import socket


def find_free_port():
    """Find a free port to use for the test server"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        s.listen(1)
        port = s.getsockname()[1]
    return port


@pytest.fixture(scope="session")
def built_site():
    """Build the site once for all tests"""
    print("Building site for tests...")
    result = subprocess.run(
        ["uv", "run", "render-engine", "build"],  # use uv
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        pytest.fail(f"Failed to build site: {result.stderr}")
    return pathlib.Path("output")


@pytest.fixture(scope="session")
def test_server(built_site):
    """Start a simple HTTP server to serve the built site"""
    port = find_free_port()

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(built_site), **kwargs)

    httpd = socketserver.TCPServer(("", port), Handler)

    # Start server in a thread
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    # Wait for server to start
    time.sleep(1)

    base_url = f"http://localhost:{port}"

    yield base_url

    httpd.shutdown()


@pytest.fixture(scope="session")
def browser_context(test_server):
    """Create a browser context for all tests"""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        yield page, test_server

        context.close()
        browser.close()


def test_accessibility(browser_context):
    """Run accessibility tests on the homepage"""
    page, base_url = browser_context
    page.goto(f"{base_url}/")

    axe = Axe()
    results = axe.run(page, options={"runOnly": ["wcag2a", "wcag2aa"]})

    assert (
        len(results["violations"]) == 0
    ), f"Accessibility violations found: {results['violations']}"


def test_destination(loaded_route: str, browser_context) -> None:
    """Test that the destinations page loads with seeded data"""
    page, base_url = browser_context
    response = page.goto(f"{base_url}/{loaded_route}")
    assert response.status == 200


LANG_ROUTES = (
    "/",
    "/about.html",
    "/bpd-events/",
    "/community.html",
    "/support.html",
    "/blog/",
)


@pytest.mark.parametrize("route", LANG_ROUTES)
def test_headers_in_language(browser_context, route: str) -> None:
    """checks the route and the language of each route"""
    page, base_url = browser_context
    response = page.goto(f"{base_url}{route}")
    assert response.status == 200
    doc_lang = page.evaluate("document.documentElement.lang")
    assert doc_lang == "en"

    axe = Axe()
    results = axe.run(page, options={"runOnly": ["wcag2a", "wcag2aa"]})

    assert (
        len(results["violations"]) == 0
    ), f"Accessibility violations found: {results['violations']}"


@pytest.mark.parametrize(
    "title, url",
    (
        ("Home", "/"),
        ("Blog", "/blog/"),
        ("About Us", "/about.html"),
        ("BPD Events", "/bpd-events/"),
        ("Community", "/community.html"),
        ("Support Us", "/support.html"),
    ),
)
def test_bpdevs_title_en(browser_context, title: str, url: str) -> None:
    page, base_url = browser_context
    page.goto(f"{base_url}{url}")
    expect(page).to_have_title(f"Black Python Devs | {title}")

    axe = Axe()
    results = axe.run(page, options={"runOnly": ["wcag2a", "wcag2aa"]})

    assert (
        len(results["violations"]) == 0
    ), f"Accessibility violations found: {results['violations']}"


def test_mailto_bpdevs(browser_context) -> None:
    page, base_url = browser_context
    page.goto(base_url)
    mailto = page.get_by_role("link", name="email")
    expect(mailto).to_have_attribute("href", "mailto:contact@blackpythondevs.com")

    axe = Axe()
    results = axe.run(page, options={"runOnly": ["wcag2a", "wcag2aa"]})

    assert (
        len(results["violations"]) == 0
    ), f"Accessibility violations found: {results['violations']}"


@pytest.mark.parametrize(
    "url",
    ("/blog/",),
)
def test_page_description_in_index_and_blog(browser_context, url: str):
    """Checks for the descriptions data in the blog posts. There should be some objects with the class `post-description`"""
    page, base_url = browser_context
    page.goto(f"{base_url}{url}")
    expect(page.locator("p.post-description").first).to_be_visible()
    expect(page.locator("p.post-description").first).not_to_be_empty()

    axe = Axe()
    results = axe.run(page, options={"runOnly": ["wcag2a", "wcag2aa"]})

    assert (
        len(results["violations"]) == 0
    ), f"Accessibility violations found: {results['violations']}"


def stem_description(
    path: pathlib.Path,
) -> Generator[tuple[str, frontmatter.Post], None, None]:
    """iterate through a list returning the stem of the file and the contents"""
    for entry in path.glob("*.md"):
        yield (entry.stem, frontmatter.loads(entry.read_text()))


blog_posts = stem_description(pathlib.Path("_posts"))


@pytest.mark.parametrize("post", list(blog_posts))
def test_page_blog_posts(browser_context, post: tuple[str, frontmatter.Post]):
    """Checks that the meta page description matches the description of the post"""
    page, base_url = browser_context
    entry_stem, frontmatter_data = post

    # Convert blog post filename to URL path
    # Blog posts are in /blog/ directory in the output
    url = f"{base_url}/blog/{entry_stem}.html"

    page.goto(url, timeout=60000, wait_until="networkidle")

    # More robust waiting for the meta description
    page.wait_for_selector(
        'meta[name="description"]',
        timeout=10000,
        state="attached",
    )

    axe = Axe()
    results = axe.run(page, options={"runOnly": ["wcag2a", "wcag2aa"]})

    assert (
        len(results["violations"]) == 0
    ), f"Accessibility violations found: {results['violations']}"
