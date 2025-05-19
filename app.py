from render_engine import Site, Page

navigation = [
    {"text": "Home", "url": "/", "fa": "fa fa-home fa-fw"},
    {"text": "Blog", "url": "/blog/", "fa": "fa fa-newspaper fa-fw"},
    {"text": "About Us", "url": "/about/", "fa": "fa fa-info-circle fa-fw"},
    {"text": "Events", "url": "/events/", "fa": "fa fa-calendar fa-fw"},
    {"text": "Community", "url": "/community/", "fa": "fa fa-users fa-fw"},
    {"text": "Support Us", "url": "/support/", "fa": "fa-solid fa-money-check-dollar"},
]

app = Site()
app.template_path = "_layouts"
app.static_paths.add("assets")
app.site_vars["locales"] = ["en"]
app.site_vars["navigation"] = navigation

@app.page
class Index(Page):
    template = "index.html"
    current = "nav-current"
    content_path = "index.html"
