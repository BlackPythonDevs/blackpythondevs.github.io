import pytest

ROUTES = [
    "",
    "blog",
    "about.html",
    "support.html",
]


@pytest.fixture(params=ROUTES)
def loaded_route(request):
    return request.param
