#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return qianduanzhidian

class qianduanzhidian(BaseFeedBook):
    title                 = u'前端之巅'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'前端之巅', 'http://feedmaker.kindle4rss.com/feeds/frontshow.weixin.xml', True)
           ]