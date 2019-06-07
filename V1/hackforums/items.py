# -*- coding: utf-8 -*-

import scrapy

class HackforumsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Title = scrapy.Field()
    Time = scrapy.Field()
    Lastpost = scrapy.Field()
    Author = scrapy.Field()
    Link = scrapy.Field()
    pass
