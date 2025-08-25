import datetime
import json
import pathlib

import yaml

from render_engine import Site, Page, Collection, Blog
from render_engine_markdown import MarkdownPageParser

navigation = [
    {"text": "Home", "url": "/index.html", "fa": "fa fa-home fa-fw"},
    {"text": "Blog", "url": "/blog/blog1.html", "fa": "fa fa-newspaper fa-fw"},
    {"text": "About Us", "url": "/about.html", "fa": "fa fa-info-circle fa-fw"},
    {"text": "BPD Events", "url": "/bpd-events", "fa": "fa fa-calendar fa-fw"},
    {
        "text": "Sponsored Events",
        "url": "/sponsored-events.html",
        "fa": "fa fa-handshake fa-fw",
    },
    {"text": "Community", "url": "/community.html", "fa": "fa fa-users fa-fw"},
    {
        "text": "Support Us",
        "url": "/support.html",
        "fa": "fa-solid fa-money-check-dollar",
    },
]

app = Site()
app.template_path = "_layouts"
app.static_paths.add("assets")
app.site_vars["locales"] = ["en"]
app.site_vars["navigation"] = navigation
app.site_vars["DATETIME_FORMAT"] = "%d %b %Y"


@app.page
class Index(Page):
    template = "index.html"
    content_path = "index.html"


@app.page
class About(Page):
    template = "about.html"
    data = yaml.safe_load(pathlib.Path("_data/leadership.yaml").read_text())


@app.page
class Support(Page):
    Parser = MarkdownPageParser
    content_path = "support.md"
    template = "support.html"
    data = json.loads(pathlib.Path("_data/foundational_supporters.json").read_text())


@app.page
class SponsoredEvents(Page):
    template = "sponsored-events.html"
    slug = "sponsored-events"
    data = json.loads(pathlib.Path("_data/sponsored_events.json").read_text())
    template_vars = {"year": str(datetime.date.today().year)}


@app.collection
class Pages(Collection):
    Parser = MarkdownPageParser
    content_path = "pages"
    template = "default.html"


@app.collection
class BPDEvents(Collection):
    Parser = MarkdownPageParser
    content_path = "events"
    template = "default.html"
    routes = ["./bpd-events"]
    has_archive = True
    archive_template = "event-list.html"


@app.collection
class Blog(Blog):
    Parser = MarkdownPageParser
    template = "post.html"
    content_path = "_posts"
    routes = ["./blog"]
    has_archive = True
    archive_template = "blog-list.html"
    items_per_page = 10
