# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

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
