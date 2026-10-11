from datetime import datetime, timezone
import html
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import URLError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import update_recent_posts as updater

NOW = datetime(2026, 10, 11, tzinfo=timezone.utc)
DATE = "Sun, 06 Sep 2026 22:47:45 +0000"


def rss(*entries):
    items = []
    for title, link, date in entries:
        items.append(
            f"<item><title>{html.escape(title)}</title><link>{html.escape(link)}</link>"
            f"<pubDate>{date}</pubDate></item>"
        )
    return ("<rss version='2.0'><channel>" + "".join(items) + "</channel></rss>").encode()


class FeedTests(unittest.TestCase):
    def test_real_hugo_url_forms_dates_sorting_deduplication_and_limit(self):
        data = rss(
            ("Older", "/2026/2610.html", "Sun, 28 Jun 2026 01:25:45 +0000"),
            ("Latest", "//owent.net/2026/2611.html", DATE),
            ("Duplicate", "http://owent.net/2026/2611.html", DATE),
            ("About", "//owent.net/about.html", DATE),
            ("External", "https://example.com/2026/2612.html", DATE),
            ("Future", "/2027/2701.html", "Fri, 01 Jan 2027 00:00:00 +0000"),
        )
        posts = updater.parse_posts(data, 6, NOW)
        self.assertEqual([p[2] for p in posts], [
            "https://owent.net/2026/2611.html", "https://owent.net/2026/2610.html"
        ])
        self.assertEqual(posts[0][1], "Latest")
        self.assertEqual(len(updater.parse_posts(data, 1, NOW)), 1)
        self.assertIn("2026-09-07 ·", updater.render_posts(posts))

    def test_titles_render_as_plain_text(self):
        title = "A [link](url) <img> & *bold* _text_ `code` \\ end"
        rendered = updater.render_posts(updater.parse_posts(rss((title, "/2026/2611.html", DATE)), 6, NOW))
        self.assertIn(r"A \[link\](url) &lt;img&gt; &amp; \*bold\* \_text\_ \`code\` \\ end", rendered)
        self.assertNotIn("<img>", rendered)

    def test_empty_or_non_rss_feeds_fail(self):
        for data in (b"<rss><channel/></rss>", b"<html>error</html>", b"<rss"):
            with self.subTest(data=data), self.assertRaises((ValueError, updater.ET.ParseError)):
                updater.parse_posts(data, 6, NOW)

    def test_invalid_or_unzoned_dates_fail(self):
        for date in ("", "bad date", "Sun, 06 Sep 2026 22:47:45"):
            with self.subTest(date=date), self.assertRaises(ValueError):
                updater.parse_posts(rss(("Title", "/2026/2611.html", date)), 6, NOW)

    def test_oversized_feed_and_nonpositive_limit_fail(self):
        with self.assertRaises(ValueError):
            updater.parse_posts(b" " * (updater.MAX_FEED_BYTES + 1), 6, NOW)
        with self.assertRaises(ValueError):
            updater.parse_posts(rss(("Title", "/2026/2611.html", DATE)), 0, NOW)

    def test_network_retry_returns_valid_feed(self):
        data = rss(("Title", "/2026/2611.html", DATE))
        response = unittest.mock.MagicMock()
        response.__enter__.return_value.read.return_value = data
        with patch.object(updater, "urlopen", side_effect=[URLError("temporary"), response]) as request, \
                patch.object(updater.time, "sleep") as sleep:
            self.assertEqual(updater.fetch_feed(), data)
        self.assertEqual(request.call_count, 2)
        sleep.assert_called_once_with(2)


class ReadmeTests(unittest.TestCase):
    def test_preserves_all_text_outside_block_and_newline_style(self):
        for newline in ("\n", "\r\n"):
            with self.subTest(newline=newline):
                prefix = f"\ufeff# Intro 中文{newline}{updater.START}"
                suffix = f"{updater.END}{newline}## Projects{newline}"
                original = prefix + newline + "old" + newline + suffix
                self.assertEqual(updater.replace_block(original, "one\ntwo"),
                                 prefix + newline + "one" + newline + "two" + newline + suffix)

    def test_missing_duplicate_or_reversed_markers_fail(self):
        for readme in ("no markers", updater.START, updater.START * 2 + updater.END,
                       updater.START + updater.END * 2, updater.END + updater.START):
            with self.subTest(readme=readme), self.assertRaises(ValueError):
                updater.replace_block(readme, "content")

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.readme = Path(self.temp.name) / "README.md"
        self.feed = Path(self.temp.name) / "feed.xml"
        self.original = (f"# Keep me\r\n{updater.START}\r\nold\r\n"
                         f"{updater.END}\r\nFooter 中文\r\n").encode("utf-8")
        self.readme.write_bytes(self.original)
        self.feed.write_bytes(rss(("Latest", "//owent.net/2026/2611.html", DATE)))
        self.args = ["--readme", str(self.readme), "--feed-file", str(self.feed)]
        self.stdout = patch("sys.stdout", new_callable=io.StringIO).start()
        self.stderr = patch("sys.stderr", new_callable=io.StringIO).start()
        self.addCleanup(patch.stopall)

    def test_offline_update_is_idempotent_and_skips_unchanged_write(self):
        self.assertEqual(updater.main(self.args), 0)
        updated = self.readme.read_bytes()
        self.assertIn(b"2026-09-07", updated)
        with patch.object(updater, "write_atomic", side_effect=AssertionError("Unexpected write")):
            self.assertEqual(updater.main(self.args), 0)
        self.assertEqual(self.readme.read_bytes(), updated)

    def test_check_mode_reports_stale_without_writing(self):
        self.assertEqual(updater.main(self.args + ["--check"]), 1)
        self.assertEqual(self.readme.read_bytes(), self.original)
        self.assertEqual(updater.main(self.args), 0)
        self.assertEqual(updater.main(self.args + ["--check"]), 0)

    def test_invalid_feed_preserves_readme(self):
        for data in (b"<html>unavailable</html>", b"<rss><channel/></rss>", b"broken XML"):
            with self.subTest(data=data):
                self.feed.write_bytes(data)
                self.assertEqual(updater.main(self.args), 1)
                self.assertEqual(self.readme.read_bytes(), self.original)

    def test_network_failure_preserves_readme(self):
        with patch.object(updater, "urlopen", side_effect=URLError("offline")) as request, \
                patch.object(updater.time, "sleep"):
            self.assertEqual(updater.main(["--readme", str(self.readme)]), 1)
        self.assertEqual(request.call_count, 3)
        self.assertEqual(self.readme.read_bytes(), self.original)

    def test_failed_atomic_replace_preserves_readme_and_cleans_temporary_file(self):
        with patch.object(updater.os, "replace", side_effect=PermissionError("Cannot replace README")):
            self.assertEqual(updater.main(self.args), 1)
        self.assertEqual(self.readme.read_bytes(), self.original)
        self.assertEqual(sorted(p.name for p in self.readme.parent.iterdir()), ["README.md", "feed.xml"])

    def test_invalid_readme_or_limit_fails_before_network_access(self):
        with patch.object(updater, "fetch_feed", side_effect=AssertionError("Unexpected network call")):
            self.assertEqual(updater.main(["--readme", str(self.readme), "--limit", "0"]), 1)
            self.assertEqual(self.readme.read_bytes(), self.original)
            self.readme.write_text("No markers", encoding="utf-8")
            self.assertEqual(updater.main(["--readme", str(self.readme)]), 1)


if __name__ == "__main__":
    unittest.main()
