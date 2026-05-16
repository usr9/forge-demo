import urllib.error
import urllib.request

import html2text


class FetchError(Exception):
    pass


def fetch(url: str) -> str:
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        raise FetchError(f"HTTP {e.code}: {url}") from e
    except urllib.error.URLError as e:
        raise FetchError(f"Connection error: {e.reason}") from e


def to_markdown(html: str) -> str:
    return html2text.html2text(html)
