import datetime
import json
import pathlib
import pluggy

from render_engine import Site, Page, Collection, Blog
from render_engine_markdown import MarkdownPageParser

from render_engine_clean_urls import CleanURLsPlugin
from scripts.map import generate_map

navigation = [
    {
        "text": "News",
        "url": "/blog/blog1.html",
        "icon": "iconoir-journal-page",
    },
    {
        "text": "About Us",
        "url": "/about.html",
        "icon": "iconoir-group",
    },
    {
        "text": "Events",
        "url": "/events.html",
        "icon": "iconoir-calendar",
    },
    {
        "text": "Support Us",
        "url": "/support.html",
        "icon": "iconoir-donate",
    },
]

markdown_extras = [
    "footnotes",
    "fenced-code-blocks",
    "header-ids",
    "tables",
]

hookimpl = pluggy.HookimplMarker("render_engine")


class GenerateMapPlugin:
    @staticmethod
    @hookimpl
    def pre_build_site():
        generate_map()


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

app.plugin_manager.register_plugin(GenerateMapPlugin)
app.plugin_manager.register_plugin(CleanURLsPlugin)


@app.page
class Index(Page):
    template = "index.html"
    content_path = "index.html"


@app.page
class Students(Page):
    content_path = "students.html"


@app.page
class Community(Page):
    content_path = "community.html"


@app.page
class Partnerships(Page):
    content_path = "partnerships.html"


@app.page
class Leadership(Page):
    content_path = "leadership.html"


@app.page
class Pycon(Page):
    content_path = "pycon.html"


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
    parser_extras = {"markdown_extras": markdown_extras}
    content_path = "events"
    template = "default.html"
    routes = ["./bpd-events"]


@app.collection
class Pages(Collection):
    Parser = MarkdownPageParser
    parser_extras = {"markdown_extras": markdown_extras}
    content_path = "pages"
    template = "default.html"


@app.collection
class Blog(Blog):
    Parser = MarkdownPageParser
    parser_extras = {"markdown_extras": markdown_extras}
    template = "post.html"
    content_path = "_posts"
    routes = ["./blog"]
    has_archive = True
    archive_template = "blog-list.html"
    items_per_page = 10
