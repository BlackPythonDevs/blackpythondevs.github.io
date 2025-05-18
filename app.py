from render_engine import Site, Page

app = Site()
app.template_path = "_layouts"
app.site_vars["locales"] = ["en"]


@app.page
class Index(Page):
    template = "index.html"
    content_path = "index.html"
