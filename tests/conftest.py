import pytest

ROUTES = [
    "",
    "blog",
    "about.html",
    "bpd-events",
    "support.html",
]


@pytest.fixture(params=ROUTES)
def loaded_route(request):
    return request.param
