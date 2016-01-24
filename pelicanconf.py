#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Pouya MN'
SITENAME = u'Odoo Demystification'
SITEURL = 'http://0.0.0.0:8000'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DELETE_OUTPUT_DIRECTORY = False


# Blogroll
LINKS =  (('Odoo', 'http://odoo.com/'),
	  ('Odoo made Einfach', 'http://fshahy.github.io/'),
	  ('Odoo made easy','http://www.odoo.yenthevg.com/')
         )

# Social widget
SOCIAL = (('My github page', 'https://github.com/pouyamn/'),
          ('My linked-in profile', 'https://tr.linkedin.com/in/pouyamn'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#plugins
PLUGIN_PATH = 'plugins'
PLUGINS = ["googleplus_comments"]

#theme
THEME = "theme"
#google plus api key
GOOGLE_PLUS_API_KEY="AIzaSyD-a9IF8KKYgoC3cpgS-Al7hLQDbugrDcw"
# Urls
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
