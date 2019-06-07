# -*- coding: utf-8 -*-

import scrapy

class HackforumsItem(scrapy.Item):
    Title = scrapy.Field()
    Time = scrapy.Field()
    Lastpost = scrapy.Field()
    Author = scrapy.Field()
    Link = scrapy.Field()
    pass
