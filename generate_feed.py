#!/usr/bin/env python3
"""Generate feed.xml from all story HTML files."""

import json
import os
import re
from datetime import datetime
from html.parser import HTMLParser

BASE = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://aymane11.github.io/daily-digest"

DAY_NAMES = {"Mon": "Mon", "Tue": "Tue", "Wed": "Wed", "Thu": "Thu",
             "Fri": "Fri", "Sat": "Sat", "Sun": "Sun"}
MONTH_MAP = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6,
             "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12}


def parse_issue_date(date_str):
    """Parse '2026-04-29' -> RFC 2822 string."""
    d = datetime.strptime(date_str, "%Y-%m-%d")
    return d.strftime("%a, %d %b %Y 07:00:00 +0000")


class StoryParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.h1 = ""
        self.description = ""
        self._in_title = False
        self._in_h1 = False
        self._in_tldr_p = False  # the <p> right after TL;DR label
        self._tldr_label_seen = False
        self._tldr_done = False
        self._h1_done = False
        self._buf = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "title":
            self._in_title = True
            self._buf = []
        elif tag == "h1" and not self._h1_done:
            self._in_h1 = True
            self._buf = []
        elif tag == "p" and self._tldr_label_seen and not self._tldr_done:
            self._in_tldr_p = True
            self._buf = []

    def handle_endtag(self, tag):
        if tag == "title" and self._in_title:
            self._in_title = False
            self.title = "".join(self._buf).strip()
        elif tag == "h1" and self._in_h1:
            self._in_h1 = False
            self._h1_done = True
            self.h1 = "".join(self._buf).strip()
        elif tag == "p" and self._in_tldr_p:
            self._in_tldr_p = False
            self._tldr_done = True
            self.description = "".join(self._buf).strip()

    def handle_data(self, data):
        if self._in_title:
            self._buf.append(data)
        elif self._in_h1:
            self._buf.append(data)
        elif self._in_tldr_p:
            self._buf.append(data)
        # Detect TL;DR label text
        if "TL;DR" in data and not self._tldr_done:
            self._tldr_label_seen = True


def extract_story(html_path):
    with open(html_path, encoding="utf-8") as f:
        content = f.read()
    parser = StoryParser()
    parser.feed(content)
    title = parser.title or parser.h1
    # Normalize title: strip "Daily Digest — " prefix and " — Issue NNN" suffix
    title = re.sub(r"^Daily Digest\s*[—\-]+\s*", "", title)
    title = re.sub(r"\s*[—\-]+\s*Issue \d+\s*$", "", title)
    title = re.sub(r"\s+", " ", title).strip()
    # Fallback description: first <p> with substantial text if no TL;DR
    description = parser.description
    if not description:
        matches = re.findall(r"<p[^>]*>([\s\S]*?)</p>", content)
        for m in matches:
            clean = re.sub(r"<[^>]+>", "", m).replace("&mdash;", "—").replace("&amp;", "&").replace("&middot;", "·").strip()
            if len(clean) > 80 and not re.search(r"[A-Z]{3,}\s*[·&]", clean[:30]):
                description = clean
                break
    # Clean HTML entities from description
    description = re.sub(r"<[^>]+>", "", description)
    description = (description
                   .replace("&mdash;", "—").replace("&amp;", "&")
                   .replace("&middot;", "·").replace("&#8212;", "—")
                   .replace("&ldquo;", "“").replace("&rdquo;", "”")
                   .replace("&lsquo;", "‘").replace("&rsquo;", "’")
                   .replace("&nbsp;", " "))
    description = re.sub(r"\s+", " ", description).strip()
    return title, description


def story_sort_key(filename):
    """Sort stories: lead (01) first, then 02, 03, 04, then eng, paper."""
    name = os.path.basename(filename)
    order = {"01": 0, "02": 1, "03": 2, "04": 3, "en": 4, "pa": 5}
    prefix = name[:2]
    base = order.get(prefix, 9)
    # Sub-sort by full filename for consistency
    return (base, name)


def xml_escape(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def main():
    index_path = os.path.join(BASE, "issues", "index.json")
    with open(index_path) as f:
        issues = json.load(f)

    items = []
    # Process newest issue first
    for issue in reversed(issues):
        issue_num = issue["issue"]
        pub_date = parse_issue_date(issue["date"])
        stories_dir = os.path.join(BASE, "issues", issue_num, "stories")
        if not os.path.isdir(stories_dir):
            continue
        story_files = sorted(
            [os.path.join(stories_dir, f) for f in os.listdir(stories_dir) if f.endswith(".html")],
            key=story_sort_key
        )
        for story_path in story_files:
            rel = "issues/{}/stories/{}".format(issue_num, os.path.basename(story_path))
            url = "{}/{}".format(BASE_URL, rel)
            title, description = extract_story(story_path)
            items.append({
                "title": title,
                "link": url,
                "guid": url,
                "pubDate": pub_date,
                "description": description[:500] + ("…" if len(description) > 500 else ""),
            })

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">',
        '  <channel>',
        '    <title>Daily Digest</title>',
        '    <link>{}/</link>'.format(BASE_URL),
        '    <description>A daily AI &amp; tech news digest — curated, edited, published every morning.</description>',
        '    <language>en</language>',
        '    <atom:link href="{}/feed.xml" rel="self" type="application/rss+xml"/>'.format(BASE_URL),
        '',
    ]
    for item in items:
        lines += [
            '    <item>',
            '      <title>{}</title>'.format(xml_escape(item["title"])),
            '      <link>{}</link>'.format(xml_escape(item["link"])),
            '      <guid>{}</guid>'.format(xml_escape(item["guid"])),
            '      <pubDate>{}</pubDate>'.format(item["pubDate"]),
            '      <description>{}</description>'.format(xml_escape(item["description"])),
            '    </item>',
            '',
        ]
    lines += ['  </channel>', '</rss>', '']

    out_path = os.path.join(BASE, "feed.xml")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("Written {} items to feed.xml".format(len(items)))


if __name__ == "__main__":
    main()
