#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return gizmodo

class gizmodo(BaseFeedBook):
    title                 = u'Gizmodo'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Gizmodo', 'http://gizmodo.com/rss', True)
           ]