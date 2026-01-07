import pathlib
import pytest
from playwright.sync_api import Page, sync_playwright
import subprocess
import http.server
import socketserver
import threading
import time
import socket


def find_free_port():
    """Find a free port to use for the test server"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        s.listen(1)
        port = s.getsockname()[1]
    return port


@pytest.fixture(scope="session")
def built_site():
    """Build the site once for all tests"""
    print("Building site for design tests...")
    result = subprocess.run(
        ["uv", "run", "render-engine", "build"], capture_output=True, text=True
    )
    if result.returncode != 0:
        pytest.fail(f"Failed to build site: {result.stderr}")
    return pathlib.Path("output")


@pytest.fixture(scope="session")
def design_test_server(built_site):
    """Start a simple HTTP server to serve the built site"""
    port = find_free_port()

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(built_site), **kwargs)

    httpd = socketserver.TCPServer(("", port), Handler)

    # Start server in a thread
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    # Wait for server to start
    time.sleep(1)

    base_url = f"http://localhost:{port}"

    yield base_url

    httpd.shutdown()


@pytest.fixture(scope="module")
def per_device_page_url(design_test_server, loaded_profile):
    """Returns the url of the live server with device emulation"""
    with sync_playwright() as p:
        device = p.devices[loaded_profile]
        browser = p.chromium.launch()
        context = browser.new_context(**device)
        page = context.new_page()
        try:
            yield page, design_test_server
        finally:
            context.close()
            browser.close()


@pytest.fixture(scope="session")
def create_test_image():
    image_path = pathlib.Path("./").joinpath("test_images")

    if not image_path.is_dir():
        image_path.mkdir()
    return image_path


@pytest.mark.design
def test_route_designs(
    loaded_route: str,
    per_device_page_url: tuple[Page, str],
    create_test_image,
    request,
) -> None:
    """Test that the destinations page loads with seeded data"""
    page, base_url = per_device_page_url
    response = page.goto(f"{base_url}/{loaded_route}")
    page.screenshot(
        path=create_test_image.joinpath(request.node.name).with_suffix(".jpg"),
        full_page=True,
    )
    assert response.status == 200
