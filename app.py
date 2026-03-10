import datetime
import json
import pathlib

from render_engine import Site, Page, Collection, Blog
from render_engine_markdown import MarkdownPageParser

navigation = [
    {"text": "News", "url": "/blog/blog1.html", "fa": "fa fa-newspaper fa-fw"},
    {"text": "About Us", "url": "/about.html", "fa": "fa fa-info-circle fa-fw"},
    {"text": "Events", "fa": "fa fa-calendar fa-fw", "url": "/events.html"},
    {
        "text": "Support Us",
        "url": "/support.html",
        "fa": "fa-solid fa-hand-holding-heart",
    },
]

app = Site()
app.template_path = "_layouts"
app.static_paths.add("assets")
app.site_vars["locales"] = ["en"]
app.site_vars["navigation"] = navigation
app.site_vars["DATETIME_FORMAT"] = "%d %b %Y"
app.site_vars["year"] = str(datetime.date.today().year)
app.site_vars["SITE_AUTHORS"] = json.loads(
    pathlib.Path("_data/authors.json").read_text()
)


@app.page
class Index(Page):
    template = "index.html"
    content_path = "index.html"


@app.page
class About(Page):
    template = "about.html"
    data = json.loads(pathlib.Path("_data/leadership.json").read_text())


@app.page
class Support(Page):
    Parser = MarkdownPageParser
    content_path = "support.md"
    template = "support.html"
    data = {
        "foundational_supporters": json.loads(
            pathlib.Path("_data/foundational_supporters.json").read_text()
        ),
        "partnerships": json.loads(pathlib.Path("_data/partnerships.json").read_text()),
    }


@app.page
class Events(Page):
    template = "events.html"
    data = json.loads(pathlib.Path("_data/sponsored_events.json").read_text())


@app.collection
class BPDEvents(Collection):
    title = "BPD Events"
    Parser = MarkdownPageParser
    content_path = "events"
    template = "default.html"
    routes = ["./bpd-events"]


@app.collection
class Pages(Collection):
    Parser = MarkdownPageParser
    content_path = "pages"
    template = "default.html"


@app.collection
class Blog(Blog):
    Parser = MarkdownPageParser
    template = "post.html"
    content_path = "_posts"
    routes = ["./blog"]
    has_archive = True
    archive_template = "blog-list.html"
    items_per_page = 10
