import socket
import urllib.error
from unittest.mock import patch

import pytest

from forge_demo.core import FetchError, fetch
from conftest import make_response


def test_fetch_success():
    response = make_response("<html><body>Hello</body></html>")
    with patch("urllib.request.urlopen", return_value=response):
        result = fetch("http://example.com")
    assert "Hello" in result


def test_fetch_http_error():
    http_error = urllib.error.HTTPError(
        url="http://example.com/missing",
        code=404,
        msg="Not Found",
        hdrs={},
        fp=None,
    )
    with patch("urllib.request.urlopen", side_effect=http_error):
        with pytest.raises(FetchError) as exc_info:
            fetch("http://example.com/missing")
    assert "HTTP 404" in str(exc_info.value)
    assert "http://example.com/missing" in str(exc_info.value)


def test_fetch_timeout():
    url_error = urllib.error.URLError(reason=socket.timeout("timed out"))
    with patch("urllib.request.urlopen", side_effect=url_error):
        with pytest.raises(FetchError) as exc_info:
            fetch("http://example.com")
    assert "Connection error" in str(exc_info.value)
