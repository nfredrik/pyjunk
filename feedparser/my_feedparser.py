import feedparser
rawdata = """<rss version="2.0">
<channel>
<title>Sample Feed</title>
</channel>
</rss>"""


if __name__ == "__main__":
    
    p = feedparser