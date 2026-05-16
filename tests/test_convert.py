from forge_demo.core import to_markdown


def test_to_markdown_returns_nonempty():
    result = to_markdown("<h1>Hello</h1><p>World</p>")
    assert len(result) > 0


def test_to_markdown_contains_text():
    result = to_markdown("<h1>Hello</h1><p>World</p>")
    assert "Hello" in result
    assert "World" in result
