import urllib.error
from unittest.mock import patch

import pytest

from forge_demo.__main__ import main
from conftest import make_response


def test_cli_stdout(capsys):
    response = make_response("<h1>Hello</h1>")
    with patch("urllib.request.urlopen", return_value=response):
        with patch("sys.argv", ["forge-demo", "http://example.com"]):
            main()
    captured = capsys.readouterr()
    assert "Hello" in captured.out


def test_cli_output_file(tmp_path):
    out_file = tmp_path / "out.md"
    response = make_response("<h1>Hello</h1>")
    with patch("urllib.request.urlopen", return_value=response):
        with patch("sys.argv", ["forge-demo", "http://example.com", "--output", str(out_file)]):
            main()
    assert out_file.exists()
    assert "Hello" in out_file.read_text()


def test_cli_fetch_error_exits_1():
    http_error = urllib.error.HTTPError(
        url="http://example.com",
        code=404,
        msg="Not Found",
        hdrs={},
        fp=None,
    )
    with patch("urllib.request.urlopen", side_effect=http_error):
        with patch("sys.argv", ["forge-demo", "http://example.com"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
    assert exc_info.value.code == 1
