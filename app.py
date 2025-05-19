from render_engine import Site, Page, Collection, Blog
from render_engine_markdown import MarkdownPageParser

navigation = [
    {"text": "Home", "url": "/index.html", "fa": "fa fa-home fa-fw"},
    {"text": "Blog", "url": "/blog", "fa": "fa fa-newspaper fa-fw"},
    {"text": "About Us", "url": "/about.html", "fa": "fa fa-info-circle fa-fw"},
    {"text": "Events", "url": "/events", "fa": "fa fa-calendar fa-fw"},
    {"text": "Community", "url": "/community.html", "fa": "fa fa-users fa-fw"},
    {"text": "Support Us", "url": "/support.html", "fa": "fa-solid fa-money-check-dollar"},
]

app = Site()
app.template_path = "_layouts"
app.static_paths.add("assets")
app.site_vars["locales"] = ["en"]
app.site_vars["navigation"] = navigation

@app.page
class Index(Page):
    template = "index.html"
    content_path = "index.html"


@app.page
class About(Page):
    content_path = "pages/about.html"
    template = "default.html"
    routes = ["about"]


@app.collection
class Events(Collection):
    content_path = "events"
    template = "default.html"
    routes = ["./events"]
    has_archive = True
    archive_template = "event-list.html"

@app.collection
class Blog(Blog):
    Parser = MarkdownPageParser
    subcollections = ["tags"]
    template = "default.html"
    routes = ["./blog"]
    has_archive = True
    items_per_page = 20
    content_path = "_posts"

