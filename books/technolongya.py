#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return technolongya

class technolongya(BaseFeedBook):
    title                 = u'Economist/Science & Technology'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Economist/Science & Technology', 'http://feedmaker.kindle4rss.com/feeds/science-technology.economist.com.xml', True)
           ]