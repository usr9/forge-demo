import io
from unittest.mock import MagicMock


def make_response(body: str, status: int = 200) -> MagicMock:
    mock = MagicMock()
    mock.read.return_value = body.encode("utf-8")
    mock.status = status
    mock.__enter__ = lambda s: s
    mock.__exit__ = MagicMock(return_value=False)
    return mock
