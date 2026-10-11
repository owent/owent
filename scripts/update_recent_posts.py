#!/usr/bin/env python3
"""Update only the marked README block using the public owent.net RSS feed."""

import argparse
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
import html
import os
from pathlib import Path
import re
import sys
import tempfile
import time
from urllib.error import URLError
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

FEED_URL = "https://owent.net/index.xml"
START = "<!-- RECENT-POSTS:START -->"
END = "<!-- RECENT-POSTS:END -->"
MAX_FEED_BYTES = 2 * 1024 * 1024
SHANGHAI = timezone(timedelta(hours=8))


def fetch_feed():
    request = Request(FEED_URL, headers={"User-Agent": "owent-profile-rss/1.0"})
    for attempt in range(3):
        try:
            with urlopen(request, timeout=30) as response:
                data = response.read(MAX_FEED_BYTES + 1)
            if len(data) > MAX_FEED_BYTES:
                raise ValueError("RSS feed exceeds the 2 MiB limit")
            return data
        except (URLError, TimeoutError, OSError):
            if attempt == 2:
                raise
            time.sleep(2 ** (attempt + 1))


def parse_posts(data, limit, now=None):
    if limit < 1:
        raise ValueError("Post limit must be positive")
    if len(data) > MAX_FEED_BYTES:
        raise ValueError("RSS feed exceeds the 2 MiB limit")
    root = ET.fromstring(data)
    if root.tag != "rss" or root.find("channel") is None:
        raise ValueError("Expected an RSS channel")
    now = now or datetime.now(timezone.utc)
    posts = {}
    for item in root.findall("channel/item"):
        title = " ".join((item.findtext("title") or "").split())
        parts = urlsplit(urljoin(FEED_URL, (item.findtext("link") or "").strip()))
        # Root Hugo feeds may also include non-article pages. Only use blog posts.
        if (parts.scheme not in {"http", "https"} or parts.netloc != "owent.net"
                or not re.fullmatch(r"/\d{4}/\d+\.html", parts.path) or not title):
            continue
        try:
            published = parsedate_to_datetime(item.findtext("pubDate") or "")
        except (ValueError, TypeError, OverflowError) as error:
            raise ValueError(f"Invalid publication date for {parts.path}") from error
        if published.tzinfo is None:
            raise ValueError(f"Publication date lacks a timezone: {parts.path}")
        if published > now:
            continue
        url = f"https://owent.net{parts.path}"
        post = (published, title, url)
        if url not in posts or published > posts[url][0]:
            posts[url] = post
    if not posts:
        raise ValueError("RSS feed contains no published blog articles")
    return sorted(posts.values(), key=lambda post: (post[0], post[2]), reverse=True)[:limit]


def render_posts(posts):
    lines = [f"<!-- Generated from {FEED_URL}; do not edit this block manually. -->", ""]
    for published, title, url in posts:
        # Keep titles as plain text even when they contain HTML or Markdown syntax.
        title = html.escape(title, quote=False)
        title = re.sub(r"([\\`*\[\]_])", r"\\\1", title)
        date = published.astimezone(SHANGHAI).date().isoformat()
        lines.append(f"- {date} · [{title}]({url})")
    return "\n".join(lines) + "\n"


def replace_block(readme, block):
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise ValueError("README must contain exactly one pair of recent-post markers")
    start = readme.index(START) + len(START)
    end = readme.index(END)
    if start >= end:
        raise ValueError("Recent-post markers are in the wrong order")
    newline = "\r\n" if "\r\n" in readme else "\n"
    return readme[:start] + newline + block.replace("\n", newline) + newline + readme[end:]


def write_atomic(path, data):
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix=f".{path.name}.", delete=False) as output:
            temporary = Path(output.name)
            output.write(data)
        temporary.chmod(path.stat().st_mode)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", type=Path,
                        default=Path(__file__).resolve().parents[1] / "README.md")
    parser.add_argument("--feed-file", type=Path, help="Use a local RSS file instead of the network")
    parser.add_argument("--limit", type=int, default=6)
    parser.add_argument("--check", action="store_true", help="Exit 1 if the block needs updating; do not write")
    args = parser.parse_args(argv)
    try:
        original_bytes = args.readme.read_bytes()
        original = original_bytes.decode("utf-8")
        replace_block(original, "")  # Check boundaries before accessing the network.
        if args.limit < 1:
            raise ValueError("Post limit must be positive")
        data = args.feed_file.read_bytes() if args.feed_file else fetch_feed()
        updated = replace_block(original, render_posts(parse_posts(data, args.limit)))
        updated_bytes = updated.encode("utf-8")
        if updated_bytes == original_bytes:
            print("Recent writing is up to date.")
            return 0
        if args.check:
            print("Recent writing needs updating.")
            return 1
        write_atomic(args.readme, updated_bytes)
        print("Updated recent writing from owent.net RSS.")
        return 0
    except (OSError, ValueError, ET.ParseError, URLError) as error:
        print(f"Recent writing update failed; README was preserved: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
