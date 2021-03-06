#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

THEME = "themes/pelican-bootstrap3"
SITEURL = 'https://badgerops.net'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

TYPOGRIFY = True
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

PLUGIN_PATHS = ['./plugins']
# PLUGINS = ['extract_toc','render_math','disqus_static','better_figures_and_images']
# MD_EXTENSIONS = ['codehilite','extra','smarty', 'toc']

PATH = '../raw'
OUTPUT_PATH = '../badgerops.net/'
STATIC_PATHS = ['extra', 'images', 'pdfs']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/htaccess': {'path': '.htaccess'}
}

# COLOPHON = True
# COLOPHON_TITLE = 'About'
# COLOPHON_CONTENT = "Mainly...."

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
