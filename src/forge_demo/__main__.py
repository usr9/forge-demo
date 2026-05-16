import argparse
import sys

from forge_demo.core import FetchError, fetch, to_markdown


def main():
    parser = argparse.ArgumentParser(
        prog="forge-demo",
        description="Fetch a URL and convert it to markdown.",
    )
    parser.add_argument("url", help="URL to fetch")
    parser.add_argument("--output", metavar="FILE", help="write output to FILE instead of stdout")
    args = parser.parse_args()

    try:
        html = fetch(args.url)
        markdown = to_markdown(html)
    except FetchError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(markdown)
    else:
        print(markdown, end="")


if __name__ == "__main__":
    main()
