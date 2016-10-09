#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Solomon Roberts'
SITENAME = u'BadgerOps'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Boise'

DEFAULT_LANG = u'en'

THEME = "themes/pelican-bootstrap3"
DISPLAY_CATEGORIES_ON_MENU = False
TWITTER_USERNAME = "badgerops"
TWITTER_WIDGET_ID = "775880837631975424"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('Pelican', 'http://getpelican.com/'),

        )
# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/badgerops'),
          ('Github', 'https://github.com/badgerops'),)

DEFAULT_PAGINATION = 10


PLUGIN_PATHS = ['./plugins']
# PLUGINS = ['extract_toc','render_math']
# MD_EXTENSIONS = ['codehilite','extra','smarty', 'toc']

PATH = '../raw'
OUTPUT_PATH = '../badgerops.net/'
STATIC_PATHS = ['extra', 'images', 'pdfs']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/htaccess': {'path': '.htaccess'}
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
