import pathlib
import shutil
import subprocess
from html.parser import HTMLParser

import pytest


class HTMLMetaParser(HTMLParser):
    """Simple HTML parser to extract metadata from HTML files."""

    def __init__(self):
        super().__init__()
        self.title = ""
        self._in_title = False
        self.meta_description = None
        self.links = []
        self.classes = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "meta" and attrs_dict.get("name") == "description":
            self.meta_description = attrs_dict.get("content", "")
        elif tag == "a":
            self.links.append(attrs_dict)
        if "class" in attrs_dict:
            self.classes.extend(attrs_dict["class"].split())

    def handle_data(self, data):
        if self._in_title:
            self.title += data

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False


def parse_html(path: pathlib.Path) -> HTMLMetaParser:
    parser = HTMLMetaParser()
    parser.feed(path.read_text())
    return parser


OUTPUT_DIR = pathlib.Path("output")


@pytest.fixture(scope="session", autouse=True)
def built_site():
    """Build the site before tests and clean up after."""
    # Setup: build the site
    result = subprocess.run(
        ["uv", "run", "render-engine", "build"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        pytest.fail(f"Failed to build site: {result.stderr}")

    yield OUTPUT_DIR

    # Teardown: remove the output directory
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)


ROUTE_FILES = {
    "": "index.html",
    "blog": "blog/index.html",
    "about.html": "about.html",
    "support.html": "support.html",
}


def test_destination(loaded_route: str, built_site: pathlib.Path) -> None:
    """Test that the expected output files exist for each route."""
    file_name = ROUTE_FILES[loaded_route]
    output_file = built_site / file_name
    assert output_file.exists(), f"Expected output file not found: {output_file}"


@pytest.mark.parametrize(
    "title, file_path",
    (
        ("Black Python Devs", "index.html"),
        ("Blog | Black Python Devs", "blog/index.html"),
        ("About | Black Python Devs", "about.html"),
        ("Support | Black Python Devs", "support.html"),
    ),
)
def test_bpdevs_title_en(built_site: pathlib.Path, title: str, file_path: str) -> None:
    """Check that each page has the expected title."""
    parsed = parse_html(built_site / file_path)
    assert parsed.title == title, f"Expected title '{title}', got '{parsed.title}'"


def test_mailto_bpdevs(built_site: pathlib.Path) -> None:
    """Check that the homepage has a mailto link to contact@blackpythondevs.com."""
    parsed = parse_html(built_site / "index.html")
    mailto_links = [
        link for link in parsed.links if link.get("href", "").startswith("mailto:")
    ]
    assert any(
        link["href"] == "mailto:contact@blackpythondevs.com" for link in mailto_links
    ), "Expected mailto:contact@blackpythondevs.com link not found"


def test_community_redirects_to_about(built_site: pathlib.Path) -> None:
    """Check that community.html contains a redirect to the about page."""
    community = built_site / "community.html"
    assert community.exists(), "community.html should exist in build output"
    content = community.read_text()
    assert (
        "/about.html#join-the-community" in content
    ), "community.html should redirect to /about.html#join-the-community"


def test_partnerships_redirects_to_support(built_site: pathlib.Path) -> None:
    """Check that partnerships.html contains a redirect to the support page."""
    partnerships = built_site / "partnerships.html"
    assert partnerships.exists(), "partnerships.html should exist in build output"
    content = partnerships.read_text()
    assert (
        "/support.html#partnerships" in content
    ), "partnerships.html should redirect to /support.html#partnerships"


def test_pycon_redirects_to_blog_post(built_site: pathlib.Path) -> None:
    """Check that pycon.html contains a redirect to the PyCon US blog post."""
    pycon = built_site / "pycon.html"
    assert pycon.exists(), "pycon.html should exist in build output"
    content = pycon.read_text()
    assert (
        "https://blackpythondevs.com/blog/black-python-devs-at-pycon-us-2026.html"
        in content
    ), "pycon.html should redirect to the PyCon US 2026 blog post"


def _blog_post_files() -> list[pathlib.Path]:
    """Get all blog post HTML files (excluding index and pagination pages)."""
    blog_dir = OUTPUT_DIR / "blog"
    if not blog_dir.exists():
        return []
    skip = {"index.html"}
    return [
        f
        for f in sorted(blog_dir.glob("*.html"))
        if f.name not in skip and not f.stem.startswith("blog")
    ]


@pytest.mark.parametrize("post_file", _blog_post_files(), ids=lambda p: p.stem)
def test_blog_post_has_meta_description(
    built_site: pathlib.Path, post_file: pathlib.Path
) -> None:
    """Check that each blog post has a meta description tag."""
    parsed = parse_html(post_file)
    assert (
        parsed.meta_description is not None
    ), f"Missing meta description in {post_file.name}"
