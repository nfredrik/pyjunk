#!/usr/bin/env python
"""
Command line BBC News reader, by oozie <root ooz ie>

$ ./bbcnews.py
"""
import urllib2
from xml.parsers import expat

GREEN = '\x1b[32m'
BLUE = '\x1b[34m'
NORMAL = '\x1b[30m'

BBC_NEWS_RSS = 'http://newsrss.bbc.co.uk/'+\
               'rss/newsonline_world_edition/front_page/rss.xml'

class NewsItem(object):
    """Class representing a news item."""
    category = None
    description = None
    link = None
    title = None
    def summary(self):
        """Summarize news item in color."""
        return '%s%s: %s%s %s%s' % (BLUE, self.title,
                                    GREEN, self.description,
                                    NORMAL, self.link)
    def headline(self):
        """Print news item title and corresponding link."""
        return '%s%s %s%s' % (BLUE, self.title,
                              NORMAL, self.link)

def get_news(rss_feed):
    """Get a list of news items."""

    class _CurrentData(object):
        """Class holding a set of current attributes."""
        item = None
        text = None

    def _start_element_handler(name, attrs):
        """Handle XML start-elements."""
        if name == 'item':
            # Allocate a new item.
            current.item = NewsItem()

    def _end_element_handler(name):
        """Handle XML end-elements."""
        if name == 'item':
            news_items.append(current.item)
        elif name in ('title', 'description', 'link', 'category'):
            try:
                setattr(current.item, name, current.text)
            except AttributeError:
                # The parser has run into a non-news item.
                pass

    def _char_data_handler(data):
        """Handle XML element character data."""
        current.text = data

    news_items = list()
    current = _CurrentData()

    parser = expat.ParserCreate()
    parser.StartElementHandler = _start_element_handler
    parser.EndElementHandler = _end_element_handler
    parser.CharacterDataHandler = _char_data_handler

    news_handle = urllib2.urlopen(rss_feed)
    xml_data = news_handle.read()
    
    parser.Parse(xml_data)

    return news_items


if __name__ == '__main__':

    for news_item in get_news(BBC_NEWS_RSS):
        print news_item.summary()