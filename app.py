from render_engine import Site, Page

app = Site()
app.template_path = "_layouts"
app.static_paths.add("assets")
app.site_vars["locales"] = ["en"]


@app.page
class Index(Page):
    template = "index.html"
    content_path = "index.html"


@app.page
class About(Page):
    content_path = "pages/about.html"
    template = "default.html"
